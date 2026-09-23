from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import csv
import hashlib
import json

import numpy as np

from .types import BFGState, CoreStep, NumericalPolicy
from .core import canonical_reclosure, neutral_pair
from .carrier_sdk import CarrierSchema, ValidatedCarrierAdapter, write_carrier_schema
from .real_validation import HeldoutValidationPlan, plan_fingerprint
from .session import save_experiment_ledger
from .portfolio import ValidationPortfolio, BlindHeldoutGuard
from .sunspot_carrier import (
    DEFAULT_DATA,
    load_sunspots,
    build_window_measurements,
    _fit_ridge_ar,
    _graph_sigma_from_calibration,
    _window_graph,
    _resource_from_window,
    _state_vector,
    _neutral_load_aligned,
    _formation_operator_aligned,
    _recursive_operator_aligned,
    _ordinary_feature,
    ORDINARY_NULL_FEATURES,
)

BFG_FEATURE_CANDIDATES = (
    "neutral_retention",
    "formation_rayleigh",
    "crossfed_gain",
    "omega_keep",
    "lambda_up",
    "spectral_mismatch",
)

SUNSPOT_PREFLIGHT_FOLDS = (
    (1859, 1860, 1909),
    (1909, 1910, 1959),
    (1959, 1960, 2008),
)

FUTURE_HELDOUT_START = 2009
FUTURE_HELDOUT_END = 2025


@dataclass(frozen=True)
class SunspotValidationConfig:
    lag: int
    development_start_year: int
    development_end_year: int
    heldout_start_year: int
    heldout_end_year: int

    mean: float
    std: float
    graph_sigma: float
    temporal_scale: float
    neutral_load_scale: float
    stress_scale: float
    formation_drive: float
    formation_offset: float
    persistent_rank: int
    contraction: float
    phase_scale: float

    ar_ridge: float
    ar_intercept: float
    ar_coefficients: tuple[float, ...]

    bfg_feature_name: str
    bfg_feature_mean: float
    bfg_feature_std: float
    bfg_intercept: float
    bfg_slope: float

    null_feature_name: str
    null_feature_mean: float
    null_feature_std: float
    null_intercept: float
    null_slope: float

    development_dataset_sha256: str

    def to_jsonable(self) -> dict[str, Any]:
        return asdict(self)


def _sha256(path: str | Path) -> str:
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _fit_correction(
    actual: np.ndarray,
    ar: np.ndarray,
    persistence: np.ndarray,
    feature: np.ndarray,
):
    feature = np.asarray(feature, dtype=float)
    mean = float(np.mean(feature))
    std = float(np.std(feature))
    if std <= 1e-12:
        std = 1.0
    q = (feature - mean) / std

    d = np.asarray(persistence) - np.asarray(ar)
    X = np.column_stack([d, q * d])
    target = np.asarray(actual) - np.asarray(ar)
    beta = np.linalg.lstsq(X, target, rcond=None)[0]
    pred = np.asarray(ar) + X @ beta
    return float(beta[0]), float(beta[1]), mean, std, pred


def _rmse(y, p) -> float:
    return float(np.sqrt(np.mean((np.asarray(y) - np.asarray(p)) ** 2)))


def _mae(y, p) -> float:
    return float(np.mean(np.abs(np.asarray(y) - np.asarray(p))))


class AnnualSunspotValidationCarrier(ValidatedCarrierAdapter):
    """
    Active annual-sunspot carrier used by the readiness-first portfolio.

    The state geometry remains graph-aligned. Forecast adaptation receives one
    frozen BFG feature chosen only from development data; the matched null gets
    the same two-coefficient correction family with one ordinary feature.
    """

    def __init__(self, config: SunspotValidationConfig):
        self.config = config
        schema = CarrierSchema(
            name="Annual Sunspot BFG Carrier",
            domain="solar activity / annual sunspot count",
            description=(
                "12-year causal recurrence-graph state with graph-aligned K, Y "
                "and R_C; active validation uses readiness-first rolling preflight."
            ),
            measurement_mapping={
                "D": "activity/resource state with phase from level + local gradient",
                "K": "graph Laplacian plus fixed offset minus one resource-supported formation mode",
                "Y": "PSD squared graph geometry plus scalar resource stress",
                "R_C": "same graph eigenbasis with persistent low modes and contractive complement",
            },
            invariant_parameters={
                **config.to_jsonable(),
                "forecast_family": (
                    "AR(12) endpoint plus two-coefficient correction along "
                    "(persistence - AR12)"
                ),
                "bfg_feature_family": list(BFG_FEATURE_CANDIDATES),
                "matched_null_feature_family": list(ORDINARY_NULL_FEATURES),
            },
            empirical_units={
                "YEAR": "calendar year",
                "SUNACTIVITY": "annual sunspot count",
            },
        )
        super().__init__(schema)

    def _z(self, measurement: dict[str, Any]) -> np.ndarray:
        values = np.asarray(measurement["window_values"], dtype=float)
        if len(values) != self.config.lag:
            raise ValueError("sunspot window length does not match frozen lag")
        return (values - self.config.mean) / self.config.std

    def map_measurement_to_state(
        self,
        measurement: Any,
        *,
        generation: int = 0,
    ) -> BFGState:
        self.assert_no_retuning()
        z = self._z(measurement)
        _, L, Ln = _window_graph(
            z, self.config.graph_sigma, self.config.temporal_scale
        )
        resource = _resource_from_window(z)
        D = _state_vector(z, resource)
        Y = _neutral_load_aligned(
            Ln,
            resource,
            self.config.neutral_load_scale,
            self.config.stress_scale,
        )
        K = _formation_operator_aligned(
            Ln,
            resource,
            self.config.formation_drive,
            self.config.formation_offset,
        )
        R = _recursive_operator_aligned(
            L,
            self.config.persistent_rank,
            self.config.contraction,
            self.config.phase_scale,
        )
        return BFGState(
            D=D,
            K=K.astype(complex),
            Y=Y.astype(complex),
            R_C=R,
            generation=int(generation),
            name=f"sunspots_{measurement['target_year']}",
            metadata={
                "domain": "annual_sunspots",
                "target_year": int(measurement["target_year"]),
                "mapping_fingerprint": self.mapping_fingerprint,
            },
        )

    def advance(
        self,
        previous: BFGState,
        step: CoreStep,
        policy: NumericalPolicy,
    ) -> BFGState:
        return previous

    def feature_bundle(
        self,
        measurement: dict[str, Any],
        policy: NumericalPolicy | None = None,
    ) -> tuple[dict[str, float], dict[str, float], bool, Any]:
        policy = policy or NumericalPolicy()
        z = self._z(measurement)
        state = self.map_measurement_to_state(measurement)
        step = canonical_reclosure(state, policy)

        C, _ = neutral_pair(state.Y)
        denom = max(float(np.real(np.vdot(state.D, state.D))), 1e-12)

        bfg = {
            "neutral_retention": float(
                np.real(np.vdot(state.D, C @ state.D)) / denom
            ),
            "formation_rayleigh": float(
                np.real(np.vdot(state.D, state.K @ state.D)) / denom
            ),
            "crossfed_gain": float(
                step.diagnostics.get("crossfed_gain", np.nan)
            ),
            "omega_keep": (
                float(step.omega_keep) if step.omega_keep is not None else np.nan
            ),
            "lambda_up": (
                float(step.lambda_up) if step.lambda_up is not None else np.nan
            ),
            "spectral_mismatch": (
                float(step.spectral_mismatch)
                if step.spectral_mismatch is not None
                else np.nan
            ),
        }
        ordinary = {
            name: _ordinary_feature(name, z)
            for name in ORDINARY_NULL_FEATURES
        }
        return bfg, ordinary, bool(step.success), step

    def endpoints(self, measurement: dict[str, Any]) -> tuple[float, float]:
        z = self._z(measurement)
        ar_z = (
            self.config.ar_intercept
            + float(
                np.dot(
                    np.asarray(self.config.ar_coefficients, dtype=float),
                    z,
                )
            )
        )
        ar = self.config.mean + self.config.std * ar_z
        persistence = float(measurement["window_values"][-1])
        return float(ar), persistence

    def forecast(self, measurement: dict[str, Any]) -> dict[str, float]:
        bfg, ordinary, _, _ = self.feature_bundle(measurement)
        ar, persistence = self.endpoints(measurement)

        bf = bfg[self.config.bfg_feature_name]
        bq = (
            (bf - self.config.bfg_feature_mean)
            / max(self.config.bfg_feature_std, 1e-12)
        )
        bw = self.config.bfg_intercept + self.config.bfg_slope * bq
        bfg_pred = ar + bw * (persistence - ar)

        nf = ordinary[self.config.null_feature_name]
        nq = (
            (nf - self.config.null_feature_mean)
            / max(self.config.null_feature_std, 1e-12)
        )
        nw = self.config.null_intercept + self.config.null_slope * nq
        null_pred = ar + nw * (persistence - ar)

        return {
            "ar12": float(ar),
            "persistence": float(persistence),
            "bfg_feature": float(bf),
            "bfg_weight": float(bw),
            "bfg": float(bfg_pred),
            "null_feature": float(nf),
            "null_weight": float(nw),
            "matched_null": float(null_pred),
        }


def _base_parameters(
    years: np.ndarray,
    values: np.ndarray,
    train_end: int,
    lag: int,
    dataset_hash: str,
) -> dict[str, Any]:
    train = values[years <= train_end]
    mean = float(np.mean(train))
    std = float(np.std(train))
    if std <= 0:
        raise ValueError("degenerate sunspot development variance")

    ar_intercept, ar_coeff = _fit_ridge_ar(
        train, lag, 1.0, mean, std
    )
    sigma = _graph_sigma_from_calibration(
        train, mean, std, lag
    )
    return {
        "lag": lag,
        "development_start_year": int(years[0]),
        "development_end_year": int(train_end),
        "heldout_start_year": FUTURE_HELDOUT_START,
        "heldout_end_year": FUTURE_HELDOUT_END,
        "mean": mean,
        "std": std,
        "graph_sigma": sigma,
        "temporal_scale": 4.0,
        "neutral_load_scale": 0.42,
        "stress_scale": 0.18,
        "formation_drive": 1.45,
        "formation_offset": 0.20,
        "persistent_rank": 4,
        "contraction": 0.76,
        "phase_scale": 0.40,
        "ar_ridge": 1.0,
        "ar_intercept": ar_intercept,
        "ar_coefficients": tuple(float(x) for x in ar_coeff),
        "development_dataset_sha256": dataset_hash,
    }


def _temporary_config(base: dict[str, Any]) -> SunspotValidationConfig:
    return SunspotValidationConfig(
        **base,
        bfg_feature_name=BFG_FEATURE_CANDIDATES[0],
        bfg_feature_mean=0.0,
        bfg_feature_std=1.0,
        bfg_intercept=0.0,
        bfg_slope=0.0,
        null_feature_name=ORDINARY_NULL_FEATURES[0],
        null_feature_mean=0.0,
        null_feature_std=1.0,
        null_intercept=0.0,
        null_slope=0.0,
    )


def _select_features(
    carrier: AnnualSunspotValidationCarrier,
    measurements: list[dict[str, Any]],
    values: np.ndarray,
):
    bundles = []
    actual = []
    ar = []
    persistence = []
    for m in measurements:
        bfg, ordinary, success, _ = carrier.feature_bundle(m)
        a, p = carrier.endpoints(m)
        bundles.append((bfg, ordinary, success))
        actual.append(float(values[int(m["target_index"])]))
        ar.append(a)
        persistence.append(p)

    actual = np.asarray(actual)
    ar = np.asarray(ar)
    persistence = np.asarray(persistence)

    def choose(names, bundle_index):
        rows = []
        best = None
        for name in names:
            feature = np.asarray(
                [b[bundle_index][name] for b in bundles],
                dtype=float,
            )
            if not np.all(np.isfinite(feature)):
                continue
            b0, b1, fm, fs, pred = _fit_correction(
                actual, ar, persistence, feature
            )
            row = {
                "feature": name,
                "rmse": _rmse(actual, pred),
                "mae": _mae(actual, pred),
                "intercept": b0,
                "slope": b1,
                "feature_mean": fm,
                "feature_std": fs,
            }
            rows.append(row)
            if best is None or row["rmse"] < best["rmse"]:
                best = row
        if best is None:
            raise RuntimeError("no finite feature candidate")
        return best, rows

    bfg_best, bfg_rows = choose(BFG_FEATURE_CANDIDATES, 0)
    null_best, null_rows = choose(ORDINARY_NULL_FEATURES, 1)
    reclosure = float(np.mean([b[2] for b in bundles]))
    return bfg_best, null_best, bfg_rows, null_rows, reclosure


def _fixed_config(
    base: dict[str, Any],
    bfg_best: dict[str, Any],
    null_best: dict[str, Any],
) -> SunspotValidationConfig:
    return SunspotValidationConfig(
        **base,
        bfg_feature_name=bfg_best["feature"],
        bfg_feature_mean=bfg_best["feature_mean"],
        bfg_feature_std=bfg_best["feature_std"],
        bfg_intercept=bfg_best["intercept"],
        bfg_slope=bfg_best["slope"],
        null_feature_name=null_best["feature"],
        null_feature_mean=null_best["feature_mean"],
        null_feature_std=null_best["feature_std"],
        null_intercept=null_best["intercept"],
        null_slope=null_best["slope"],
    )


def _evaluate_fixed(
    carrier: AnnualSunspotValidationCarrier,
    measurements: list[dict[str, Any]],
    values: np.ndarray,
):
    rows = []
    successful = 0
    novel = 0
    for i, m in enumerate(measurements):
        forecast = carrier.forecast(m)
        state, report = carrier.validate_measurement_state(m, generation=i)
        step = canonical_reclosure(state, NumericalPolicy())
        successful += int(step.success)
        novel += int(bool(step.spectral_novelty)) if step.success else 0
        rows.append({
            "year": int(m["target_year"]),
            "actual": float(values[int(m["target_index"])]),
            **forecast,
            "mapping_valid": report.valid,
            "reclosure_success": bool(step.success),
            "spectral_novelty": step.spectral_novelty,
        })

    actual = np.asarray([r["actual"] for r in rows])
    bfg = np.asarray([r["bfg"] for r in rows])
    null = np.asarray([r["matched_null"] for r in rows])
    ar = np.asarray([r["ar12"] for r in rows])
    return {
        "bfg_rmse": _rmse(actual, bfg),
        "null_rmse": _rmse(actual, null),
        "ar12_rmse": _rmse(actual, ar),
        "relative_improvement": 1.0 - _rmse(actual, bfg) / _rmse(actual, null),
        "reclosure_fraction": successful / max(len(rows), 1),
        "novelty_fraction_among_successful": novel / max(successful, 1),
        "rows": rows,
    }


def _preflight_fold(
    years: np.ndarray,
    values: np.ndarray,
    dataset_hash: str,
    lag: int,
    train_end: int,
    eval_start: int,
    eval_end: int,
):
    base = _base_parameters(
        years, values, train_end, lag, dataset_hash
    )
    temp = AnnualSunspotValidationCarrier(_temporary_config(base))
    all_measurements = build_window_measurements(years, values, lag)
    train = [
        m for m in all_measurements
        if int(m["target_year"]) <= train_end
    ]
    evaluation = [
        m for m in all_measurements
        if eval_start <= int(m["target_year"]) <= eval_end
    ]

    bfg_best, null_best, _, _, train_reclosure = _select_features(
        temp, train, values
    )
    config = _fixed_config(base, bfg_best, null_best)
    carrier = AnnualSunspotValidationCarrier(config)
    ev = _evaluate_fixed(carrier, evaluation, values)

    return {
        "train_end": train_end,
        "eval_start": eval_start,
        "eval_end": eval_end,
        "bfg_feature": bfg_best["feature"],
        "null_feature": null_best["feature"],
        "train_reclosure_fraction": train_reclosure,
        "bfg_rmse": ev["bfg_rmse"],
        "null_rmse": ev["null_rmse"],
        "ar12_rmse": ev["ar12_rmse"],
        "relative_improvement": ev["relative_improvement"],
        "eval_reclosure_fraction": ev["reclosure_fraction"],
        "eval_novelty_fraction_among_successful":
            ev["novelty_fraction_among_successful"],
    }


def prepare_sunspot_validation_current(
    outdir: str | Path,
    data_path: str | Path = DEFAULT_DATA,
    lag: int = 12,
):
    """
    Rebuild the active annual-sunspot plan under the readiness-first policy.

    All 1700-2008 observations are development data because the previous project
    already opened 1900-2008. The next confirmatory target is prospective
    2009-2025 and is not evaluated here.
    """
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    years, values = load_sunspots(data_path)
    dataset_hash = _sha256(data_path)

    folds = [
        _preflight_fold(
            years,
            values,
            dataset_hash,
            lag,
            *fold,
        )
        for fold in SUNSPOT_PREFLIGHT_FOLDS
    ]
    wins = sum(f["relative_improvement"] > 0 for f in folds)
    mean_improvement = float(np.mean(
        [f["relative_improvement"] for f in folds]
    ))
    worst_improvement = float(np.min(
        [f["relative_improvement"] for f in folds]
    ))
    min_reclosure = float(np.min(
        [f["eval_reclosure_fraction"] for f in folds]
    ))

    # Same readiness gate currently used for CO2.
    readiness = bool(
        wins >= 2
        and mean_improvement > 0
        and worst_improvement >= -0.02
        and min_reclosure >= 0.95
    )

    base = _base_parameters(
        years, values, int(years[-1]), lag, dataset_hash
    )
    temp = AnnualSunspotValidationCarrier(_temporary_config(base))
    dev_measurements = build_window_measurements(years, values, lag)
    bfg_best, null_best, bfg_candidates, null_candidates, _ = _select_features(
        temp, dev_measurements, values
    )
    config = _fixed_config(base, bfg_best, null_best)
    carrier = AnnualSunspotValidationCarrier(config)
    full = _evaluate_fixed(carrier, dev_measurements, values)

    # Prospective future indices are placeholders for the fixed annual calendar.
    calibration_indices = tuple(range(len(dev_measurements)))
    heldout_indices = tuple(
        range(
            len(dev_measurements),
            len(dev_measurements)
            + (FUTURE_HELDOUT_END - FUTURE_HELDOUT_START + 1),
        )
    )
    plan = HeldoutValidationPlan(
        domain="solar activity / annual sunspot count",
        dataset_name=(
            "Annual sunspot development snapshot 1700-2008; "
            "prospective annual continuation 2009-2025"
        ),
        target_statement=(
            "With one frozen 12-year graph-aligned annual-sunspot carrier, the "
            "BFG-feature adaptive correction will achieve lower 2009-2025 "
            "one-step RMSE than an equal-coefficient matched ordinary-feature "
            "adaptive null, while at least 95% of mapped future states pass "
            "canonical BFG reclosure."
        ),
        calibration_indices=calibration_indices,
        heldout_indices=heldout_indices,
        null_model_name=(
            "equal-coefficient adaptive correction using the best development-"
            "selected feature from six frozen ordinary window statistics"
        ),
        primary_metric="prospective annual one-step-ahead RMSE",
        success_criterion=(
            "BFG_RMSE < matched_null_RMSE AND "
            "heldout_reclosure_success_fraction >= 0.95"
        ),
        mapping_fingerprint=carrier.mapping_fingerprint,
    )
    plan.validate()

    preflight = {
        "readiness": readiness,
        "status": (
            "READY_FOR_VALIDATION"
            if readiness else "NOT_YET_VALIDATED"
        ),
        "folds": folds,
        "fold_wins": wins,
        "folds_total": len(folds),
        "mean_relative_improvement": mean_improvement,
        "worst_relative_improvement": worst_improvement,
        "minimum_eval_reclosure_fraction": min_reclosure,
        "readiness_rule": {
            "fold_wins_min": 2,
            "mean_relative_improvement_gt": 0.0,
            "worst_fold_relative_improvement_min": -0.02,
            "minimum_reclosure_fraction": 0.95,
        },
        "full_development": {
            "years": [int(years[0]), int(years[-1])],
            "bfg_feature": bfg_best["feature"],
            "null_feature": null_best["feature"],
            "bfg_rmse": full["bfg_rmse"],
            "null_rmse": full["null_rmse"],
            "ar12_rmse": full["ar12_rmse"],
            "relative_improvement": full["relative_improvement"],
            "reclosure_fraction": full["reclosure_fraction"],
            "novelty_fraction_among_successful":
                full["novelty_fraction_among_successful"],
        },
        "heldout_years": [
            FUTURE_HELDOUT_START, FUTURE_HELDOUT_END
        ],
        "heldout_metrics_evaluated": False,
    }

    write_carrier_schema(
        carrier.schema, outdir / "sunspot_carrier_schema.json"
    )
    plan_payload = asdict(plan)
    plan_payload["plan_fingerprint"] = plan_fingerprint(plan)
    plan_payload["development_years"] = [
        int(years[0]), int(years[-1])
    ]
    plan_payload["heldout_years"] = [
        FUTURE_HELDOUT_START, FUTURE_HELDOUT_END
    ]
    plan_payload["heldout_data_bundled"] = False
    (outdir / "sunspot_validation_plan.json").write_text(
        json.dumps(plan_payload, indent=2), encoding="utf-8"
    )

    frozen = {
        "config": config.to_jsonable(),
        "mapping_fingerprint": carrier.mapping_fingerprint,
        "plan_fingerprint": plan_fingerprint(plan),
        "development_dataset_sha256": dataset_hash,
        "bfg_candidates": bfg_candidates,
        "null_candidates": null_candidates,
        "preflight": preflight,
        "heldout_metrics_evaluated": False,
        "historical_1900_2008_role": (
            "development-only in this new hypothesis because that interval was "
            "already opened by the previous confirmatory plan"
        ),
    }
    (outdir / "sunspot_frozen_model.json").write_text(
        json.dumps(frozen, indent=2), encoding="utf-8"
    )
    (outdir / "sunspot_preflight.json").write_text(
        json.dumps(preflight, indent=2), encoding="utf-8"
    )

    if readiness:
        token_payload = {
            "mapping_fingerprint": carrier.mapping_fingerprint,
            "plan_fingerprint": plan_fingerprint(plan),
            "preflight_sha256": _sha256(outdir / "sunspot_preflight.json"),
            "future_heldout_years": [
                FUTURE_HELDOUT_START, FUTURE_HELDOUT_END
            ],
        }
        canonical = json.dumps(
            token_payload, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        token_payload["readiness_token"] = hashlib.sha256(
            canonical
        ).hexdigest()
        (outdir / "SUNSPOT_READINESS_TOKEN.json").write_text(
            json.dumps(token_payload, indent=2), encoding="utf-8"
        )

    save_experiment_ledger(
        outdir,
        experiment="sunspot_readiness_refresh",
        seed=None,
        parameters={
            "mapping_fingerprint": carrier.mapping_fingerprint,
            "plan_fingerprint": plan_fingerprint(plan),
            "development_years": [int(years[0]), int(years[-1])],
            "future_heldout_years": [
                FUTURE_HELDOUT_START, FUTURE_HELDOUT_END
            ],
        },
        summary=preflight,
        frames=folds,
        name="sunspot_preflight",
    )
    return {
        "status": preflight["status"],
        "readiness": readiness,
        "mapping_fingerprint": carrier.mapping_fingerprint,
        "plan_fingerprint": plan_fingerprint(plan),
        "preflight": preflight,
        "heldout_metrics_evaluated": False,
    }


def load_future_sunspots(
    path: str | Path,
    start_year: int = FUTURE_HELDOUT_START,
    end_year: int = FUTURE_HELDOUT_END,
) -> tuple[np.ndarray, np.ndarray]:
    years = []
    values = []
    with Path(path).open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            year = int(row["YEAR"])
            if start_year <= year <= end_year:
                years.append(year)
                values.append(float(row["SUNACTIVITY"]))
    expected = list(range(start_year, end_year + 1))
    if years != expected:
        raise ValueError(
            "future sunspot file must contain every held-out year exactly once: "
            f"{start_year}-{end_year}"
        )
    return np.asarray(years, dtype=int), np.asarray(values, dtype=float)


def validate_sunspot_future(
    prepared_dir: str | Path,
    future_data_path: str | Path,
    permit_path: str | Path,
    development_data_path: str | Path = DEFAULT_DATA,
):
    """
    Confirm the new prospective 2009-2025 hypothesis.

    This is not run during the refresh. It requires a one-time portfolio permit
    and a separate future-data file.
    """
    prepared_dir = Path(prepared_dir)
    frozen = json.loads(
        (prepared_dir / "sunspot_frozen_model.json").read_text(encoding="utf-8")
    )
    if frozen.get("heldout_metrics_evaluated") is not False:
        raise RuntimeError("future sunspot plan has already been evaluated")

    portfolio = ValidationPortfolio()
    guard = BlindHeldoutGuard(portfolio)
    guard.validate_confirmation_permit("annual-sunspots", permit_path)

    config_payload = dict(frozen["config"])
    config_payload["ar_coefficients"] = tuple(
        config_payload["ar_coefficients"]
    )
    config = SunspotValidationConfig(**config_payload)
    carrier = AnnualSunspotValidationCarrier(config)
    if carrier.mapping_fingerprint != frozen["mapping_fingerprint"]:
        raise RuntimeError("sunspot mapping fingerprint mismatch")

    dev_years, dev_values = load_sunspots(development_data_path)
    if _sha256(development_data_path) != config.development_dataset_sha256:
        raise RuntimeError("sunspot development snapshot changed")

    # Permit is consumed before any future target is read.
    permit_audit = guard.consume_confirmation_permit(
        "annual-sunspots", permit_path
    )
    future_years, future_values = load_future_sunspots(future_data_path)

    years = np.concatenate([dev_years, future_years])
    values = np.concatenate([dev_values, future_values])
    measurements = build_window_measurements(years, values, config.lag)
    held = [
        m for m in measurements
        if config.heldout_start_year
        <= int(m["target_year"])
        <= config.heldout_end_year
    ]
    ev = _evaluate_fixed(carrier, held, values)
    passed = bool(
        ev["bfg_rmse"] < ev["null_rmse"]
        and ev["reclosure_fraction"] >= 0.95
    )
    result = {
        "passed": passed,
        "heldout_years": [
            config.heldout_start_year, config.heldout_end_year
        ],
        "heldout_observations": len(held),
        "future_dataset_sha256": _sha256(future_data_path),
        "bfg_rmse": ev["bfg_rmse"],
        "matched_null_rmse": ev["null_rmse"],
        "ar12_rmse": ev["ar12_rmse"],
        "relative_improvement": ev["relative_improvement"],
        "heldout_reclosure_success_fraction": ev["reclosure_fraction"],
        "heldout_novelty_fraction_among_successful":
            ev["novelty_fraction_among_successful"],
        "mapping_fingerprint": carrier.mapping_fingerprint,
        "plan_fingerprint": frozen["plan_fingerprint"],
        "confirmation_permit": permit_audit,
        "retuning_after_heldout": False,
    }
    result_path = prepared_dir / "sunspot_future_heldout_result.json"
    result_path.write_text(
        json.dumps(result, indent=2), encoding="utf-8"
    )

    try:
        result_rel = str(result_path.relative_to(portfolio.project_root))
    except ValueError:
        result_rel = str(result_path)
    portfolio.record_confirmatory_result(
        "annual-sunspots",
        passed=passed,
        result_artifact=result_rel,
        metrics={
            "bfg_rmse": ev["bfg_rmse"],
            "matched_null_rmse": ev["null_rmse"],
            "relative_improvement": ev["relative_improvement"],
            "heldout_reclosure_success_fraction":
                ev["reclosure_fraction"],
        },
    )
    return result
