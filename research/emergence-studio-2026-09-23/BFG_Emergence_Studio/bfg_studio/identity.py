from __future__ import annotations
from dataclasses import dataclass, field
from pathlib import Path
import csv
import json
import math
import numpy as np
import matplotlib.pyplot as plt

from .perspective import (
    PerspectiveRun,
    PerspectiveParameters,
    simulate_perspective,
)


IDENTITY_FEATURE_NAMES = (
    "resource_position",
    "stability_position",
    "maintenance_position",
    "retention_position",
    "export_position",
    "agency_position",
    "continuity_position",
)


@dataclass(frozen=True)
class IdentityParameters:
    recurrent_alpha: float = 0.965
    epsilon_identity: float = 0.0015
    max_identity_distance: float = 0.14
    export_component_threshold: float = 0.16
    minimum_self_index_similarity: float = 0.80
    minimum_transverse_adaptation: float = 0.0010
    recurrent_rho_max: float = 1.02
    norm_limit: float = 3.0

    def validate(self):
        if not (0.90 <= self.recurrent_alpha < 1.0):
            raise ValueError("recurrent_alpha must be in [0.90,1)")
        if self.epsilon_identity <= 0:
            raise ValueError("epsilon_identity must be positive")
        if self.max_identity_distance <= self.epsilon_identity:
            raise ValueError("max_identity_distance must exceed epsilon_identity")
        if self.export_component_threshold <= 0:
            raise ValueError("export_component_threshold must be positive")
        if not (0 < self.minimum_self_index_similarity <= 1):
            raise ValueError("minimum_self_index_similarity must lie in (0,1]")
        if self.minimum_transverse_adaptation < 0:
            raise ValueError("minimum_transverse_adaptation must be nonnegative")
        if self.recurrent_rho_max <= 0:
            raise ValueError("recurrent_rho_max must be positive")
        if self.norm_limit <= 0:
            raise ValueError("norm_limit must be positive")


@dataclass
class IdentityState:
    vector: np.ndarray
    initial_index: np.ndarray
    previous_vector: np.ndarray | None = None
    age: int = 0
    exports: int = 0
    closure_passes: int = 0
    closure_failures: int = 0
    fragmentation_failures: int = 0
    rigidity_failures: int = 0
    instability_failures: int = 0
    norm_failures: int = 0


@dataclass
class IdentityRun:
    perspective_run: PerspectiveRun
    frames: list[dict]
    events: list[dict]
    final_identity: IdentityState
    identity_enabled: bool

    def summary(self) -> dict:
        d = [
            f["historical_present_distance"]
            for f in self.frames
            if f["historical_present_distance"] is not None
        ]
        id_step = [
            f["identity_step_distance"]
            for f in self.frames
            if f["identity_step_distance"] is not None
        ]
        perspective_step = [
            f["perspective_step_distance"]
            for f in self.frames
            if f["perspective_step_distance"] is not None
        ]
        index = [
            f["self_index_similarity"]
            for f in self.frames
            if f["self_index_similarity"] is not None
        ]
        transverse = [
            f["transverse_adaptation"]
            for f in self.frames
            if f["transverse_adaptation"] is not None
        ]
        return {
            "identity_enabled": self.identity_enabled,
            "frames": len(self.frames),
            "lower_perspective_reclosures":
                self.perspective_run.successful_reclosures,
            "identity_closure_passes": self.final_identity.closure_passes,
            "identity_closure_failures": self.final_identity.closure_failures,
            "identity_exports": self.final_identity.exports,
            "fragmentation_failures":
                self.final_identity.fragmentation_failures,
            "rigidity_failures": self.final_identity.rigidity_failures,
            "recursive_instability_failures":
                self.final_identity.instability_failures,
            "identity_norm_failures": self.final_identity.norm_failures,
            "mean_historical_present_distance":
                float(np.mean(d)) if d else None,
            "mean_identity_step_distance":
                float(np.mean(id_step)) if id_step else None,
            "mean_perspective_step_distance":
                float(np.mean(perspective_step)) if perspective_step else None,
            "mean_self_index_similarity":
                float(np.mean(index)) if index else None,
            "minimum_self_index_similarity":
                float(np.min(index)) if index else None,
            "mean_transverse_adaptation":
                float(np.mean(transverse)) if transverse else None,
            "final_identity_rho":
                self.frames[-1]["identity_rho"] if self.frames else None,
            "final_identity_norm":
                float(np.linalg.norm(self.final_identity.vector)),
        }


def _normalized(v: np.ndarray) -> np.ndarray:
    v = np.asarray(v, dtype=float)
    n = float(np.linalg.norm(v))
    if n <= 1e-12:
        return np.zeros_like(v)
    return v/n


def _cosine(a: np.ndarray, b: np.ndarray) -> float:
    aa = _normalized(a)
    bb = _normalized(b)
    if np.linalg.norm(aa) <= 1e-12 or np.linalg.norm(bb) <= 1e-12:
        return 0.0
    return float(np.clip(np.dot(aa, bb), -1.0, 1.0))


def identity_distance(a: np.ndarray, b: np.ndarray) -> float:
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)
    return float(np.linalg.norm(a-b)/math.sqrt(max(len(a), 1)))


def transverse_adaptation(
    identity: np.ndarray,
    present: np.ndarray,
) -> float:
    """
    Magnitude of present change transverse to the persistent identity index.

    This is the operational counterpart of the stronger universal-realization
    criterion: persistent self-index while transverse carrier degrees adapt.
    """
    idx = _normalized(identity)
    delta = np.asarray(present, dtype=float)-np.asarray(identity, dtype=float)
    if np.linalg.norm(idx) <= 1e-12:
        return identity_distance(identity, present)
    parallel = np.dot(delta, idx)*idx
    transverse = delta-parallel
    return float(
        np.linalg.norm(transverse)/math.sqrt(max(len(delta), 1))
    )


def make_identity_state(initial_self: np.ndarray) -> IdentityState:
    initial = np.asarray(initial_self, dtype=float).copy()
    return IdentityState(
        vector=initial,
        initial_index=_normalized(initial),
    )


def identity_step(
    state: IdentityState,
    present_self: np.ndarray,
    params: IdentityParameters,
    generation: int | None = None,
) -> tuple[IdentityState, dict, list[dict]]:
    """
    Level-30 recursive identity closure.

    Historical self = current identity witness.
    Present self = current Perspective standpoint.

    Id(t+1) = Cl_NId(Id(t), Self(t+1))

    The implementation uses bounded historical retention plus selective export of
    incompatible historical coordinates. Export is applied only to individual
    obsolete components; a globally fragmented present self still fails the
    identity corridor.
    """
    params.validate()
    historical = np.asarray(state.vector, dtype=float).copy()
    present = np.asarray(present_self, dtype=float).copy()
    events: list[dict] = []

    if historical.shape != present.shape:
        raise ValueError("historical and present self must have the same shape")

    raw_distance = identity_distance(historical, present)
    rho = params.recurrent_alpha

    fragmentation = raw_distance >= params.max_identity_distance
    rigidity = raw_distance <= params.epsilon_identity
    instability = rho > params.recurrent_rho_max

    effective_history = historical.copy()
    exported = []
    if not fragmentation:
        delta = present-historical
        mask = np.abs(delta) > params.export_component_threshold
        for i in np.where(mask)[0]:
            # An obsolete historical coordinate no longer constrains the present
            # closure. Its incompatible historical residual is exported.
            exported.append(int(i))
            effective_history[i] = present[i]
            events.append({
                "event": "identity_export",
                "generation": generation,
                "feature_index": int(i),
                "feature": (
                    IDENTITY_FEATURE_NAMES[i]
                    if i < len(IDENTITY_FEATURE_NAMES)
                    else f"feature_{i}"
                ),
                "historical_value": float(historical[i]),
                "present_value": float(present[i]),
                "exported_residual": float(present[i]-historical[i]),
                "mode": "obsolete_or_non_integrable_historical_component",
            })
        state.exports += len(exported)

    # Neutral historical/present mediation. The historical pole remains dominant,
    # while the present pole changes the recursive identity at every admissible
    # cycle. Exported historical coordinates have already yielded to the present.
    candidate = (
        params.recurrent_alpha*effective_history
        + (1.0-params.recurrent_alpha)*present
    )
    candidate = np.clip(candidate, -params.norm_limit, params.norm_limit)

    candidate_norm = float(np.linalg.norm(candidate))
    norm_failure = (
        not np.isfinite(candidate_norm)
        or candidate_norm > params.norm_limit*math.sqrt(len(candidate))
    )

    step_distance = identity_distance(historical, candidate)
    self_index_similarity = _cosine(candidate, state.initial_index)
    transverse = transverse_adaptation(candidate, present)

    index_persistent = (
        self_index_similarity >= params.minimum_self_index_similarity
    )
    development_present = (
        transverse >= params.minimum_transverse_adaptation
        or raw_distance > params.epsilon_identity
    )

    closure = bool(
        not fragmentation
        and not rigidity
        and not instability
        and not norm_failure
        and index_persistent
        and development_present
    )

    failure = None
    if fragmentation:
        failure = "fragmentation"
        state.fragmentation_failures += 1
    elif rigidity:
        failure = "rigidity"
        state.rigidity_failures += 1
    elif instability:
        failure = "recursive_instability"
        state.instability_failures += 1
    elif norm_failure:
        failure = "identity_norm_failure"
        state.norm_failures += 1
    elif not index_persistent:
        failure = "self_index_loss"
    elif not development_present:
        failure = "developmental_freeze"

    if closure:
        state.closure_passes += 1
    else:
        state.closure_failures += 1

    state.previous_vector = historical
    if closure or exported:
        # Failed fragmentation / instability never silently overwrites identity.
        state.vector = candidate
    state.age += 1

    return state, {
        "closure": closure,
        "failure": failure,
        "raw_distance": raw_distance,
        "identity_step_distance": step_distance,
        "self_index_similarity": self_index_similarity,
        "transverse_adaptation": transverse,
        "rho": rho,
        "identity_norm": candidate_norm,
        "exported": exported,
        "identity_vector": state.vector.copy(),
    }, events


def _standpoint_from_frame(frame: dict) -> np.ndarray:
    values = []
    i = 0
    while f"standpoint_{i}" in frame:
        values.append(float(frame[f"standpoint_{i}"]))
        i += 1
    if not values:
        raise ValueError(
            "Perspective frame does not contain standpoint coordinates; "
            "run the current Perspective module first."
        )
    return np.asarray(values, dtype=float)


def build_identity_from_perspective(
    perspective_run: PerspectiveRun,
    params: IdentityParameters | None = None,
    identity_enabled: bool = True,
) -> IdentityRun:
    params = params or IdentityParameters()
    params.validate()

    if not perspective_run.frames:
        raise ValueError("Perspective run has no frames")

    present0 = _standpoint_from_frame(perspective_run.frames[0])
    state = make_identity_state(present0)
    frames: list[dict] = []
    events: list[dict] = []

    previous_present = None

    for i, pframe in enumerate(perspective_run.frames):
        generation = int(pframe["generation"])
        present = _standpoint_from_frame(pframe)

        if i == 0:
            raw_distance = None
            identity_step_distance = 0.0
            perspective_step_distance = None
            index_similarity = 1.0
            transverse = 0.0
            closure = False
            failure = "identity_initialization"
            exported = []
            rho = params.recurrent_alpha
        elif identity_enabled:
            previous_identity = state.vector.copy()
            state, diag, step_events = identity_step(
                state, present, params, generation
            )
            events.extend(step_events)
            raw_distance = diag["raw_distance"]
            identity_step_distance = diag["identity_step_distance"]
            perspective_step_distance = identity_distance(
                previous_present, present
            )
            index_similarity = diag["self_index_similarity"]
            transverse = diag["transverse_adaptation"]
            closure = diag["closure"]
            failure = diag["failure"]
            exported = diag["exported"]
            rho = diag["rho"]

            events.append({
                "event": "identity_closure" if closure else "identity_failure",
                "generation": generation,
                "historical_present_distance": raw_distance,
                "identity_step_distance": identity_step_distance,
                "self_index_similarity": index_similarity,
                "transverse_adaptation": transverse,
                "failure": failure,
            })
        else:
            # Ablation: the current standpoint replaces the prior one. There is no
            # historical/present mediation, hence no Identity Closure claim.
            previous_identity = state.vector.copy()
            raw_distance = identity_distance(previous_identity, present)
            perspective_step_distance = identity_distance(
                previous_present, present
            )
            state.previous_vector = previous_identity
            state.vector = present.copy()
            state.age += 1
            identity_step_distance = identity_distance(
                previous_identity, state.vector
            )
            index_similarity = _cosine(
                state.vector, state.initial_index
            )
            transverse = 0.0
            closure = False
            failure = "identity_ablated"
            exported = []
            rho = 0.0

        frame = {
            "generation": generation,
            "environment": pframe.get("environment"),
            "perspective_closure": bool(
                pframe.get("perspective_closure", False)
            ),
            "historical_present_distance": raw_distance,
            "identity_step_distance": identity_step_distance,
            "perspective_step_distance": perspective_step_distance,
            "self_index_similarity": index_similarity,
            "transverse_adaptation": transverse,
            "identity_rho": rho,
            "identity_closure": bool(closure),
            "identity_failure": failure,
            "identity_exports_this_step": len(exported),
            "identity_exports_total": state.exports,
            "identity_norm": float(np.linalg.norm(state.vector)),
        }
        for j, value in enumerate(state.vector):
            frame[f"identity_{j}"] = float(value)
        for j, value in enumerate(present):
            frame[f"present_self_{j}"] = float(value)
        frames.append(frame)
        previous_present = present.copy()

    return IdentityRun(
        perspective_run=perspective_run,
        frames=frames,
        events=events,
        final_identity=state,
        identity_enabled=identity_enabled,
    )


def simulate_identity(
    seed: int = 1341550191,
    generations: int = 120,
    identity_params: IdentityParameters | None = None,
    perspective_params: PerspectiveParameters | None = None,
    **perspective_kwargs,
) -> IdentityRun:
    perspective_run = simulate_perspective(
        seed=seed,
        generations=generations,
        perspective_params=(
            perspective_params or PerspectiveParameters()
        ),
        perspective_enabled=True,
        **perspective_kwargs,
    )
    return build_identity_from_perspective(
        perspective_run,
        params=identity_params or IdentityParameters(),
        identity_enabled=True,
    )


def compare_identity(
    seed: int = 1341550191,
    generations: int = 120,
    identity_params: IdentityParameters | None = None,
    perspective_params: PerspectiveParameters | None = None,
    **perspective_kwargs,
) -> dict:
    # Both branches consume the exact same Perspective trajectory. Therefore every
    # difference below is due to temporal identity mediation rather than a lower
    # carrier difference.
    perspective_run = simulate_perspective(
        seed=seed,
        generations=generations,
        perspective_params=(
            perspective_params or PerspectiveParameters()
        ),
        perspective_enabled=True,
        **perspective_kwargs,
    )
    enabled = build_identity_from_perspective(
        perspective_run,
        params=identity_params or IdentityParameters(),
        identity_enabled=True,
    )
    disabled = build_identity_from_perspective(
        perspective_run,
        params=identity_params or IdentityParameters(),
        identity_enabled=False,
    )

    es = enabled.summary()
    ds = disabled.summary()

    mean_id_step = es["mean_identity_step_distance"]
    mean_raw_step = es["mean_perspective_step_distance"]
    continuity_gain = (
        mean_raw_step-mean_id_step
        if mean_id_step is not None and mean_raw_step is not None
        else None
    )

    return {
        "identity": enabled,
        "ablated_control": disabled,
        "summary": {
            "compared_steps": min(
                len(enabled.frames), len(disabled.frames)
            ),
            "identity_closure_passes":
                enabled.final_identity.closure_passes,
            "identity_closure_failures":
                enabled.final_identity.closure_failures,
            "identity_exports": enabled.final_identity.exports,
            "mean_historical_present_distance":
                es["mean_historical_present_distance"],
            "mean_identity_step_distance": mean_id_step,
            "mean_raw_perspective_step_distance": mean_raw_step,
            "continuity_smoothing_gain": continuity_gain,
            "mean_self_index_similarity":
                es["mean_self_index_similarity"],
            "minimum_self_index_similarity":
                es["minimum_self_index_similarity"],
            "mean_transverse_adaptation":
                es["mean_transverse_adaptation"],
            "ablated_mean_self_index_similarity":
                ds["mean_self_index_similarity"],
            "final_identity_rho": es["final_identity_rho"],
        },
    }


def write_identity_report(
    run: IdentityRun,
    outdir: str | Path,
    stem: str = "identity",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    csv_path = outdir/f"{stem}_frames.csv"
    if run.frames:
        fields = list(run.frames[0].keys())
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fields)
            w.writeheader()
            w.writerows(run.frames)

    events_path = outdir/f"{stem}_events.json"
    events_path.write_text(
        json.dumps(run.events, indent=2), encoding="utf-8"
    )

    summary_path = outdir/f"{stem}_summary.json"
    summary_path.write_text(
        json.dumps(run.summary(), indent=2), encoding="utf-8"
    )

    identity_path = outdir/f"{stem}_final_identity.csv"
    np.savetxt(
        identity_path,
        run.final_identity.vector[None, :],
        delimiter=",",
        header=",".join(IDENTITY_FEATURE_NAMES),
        comments="",
    )

    plot_path = outdir/f"{stem}_continuity.png"
    if run.frames:
        g = np.array([f["generation"] for f in run.frames])
        raw = np.array([
            np.nan if f["historical_present_distance"] is None
            else f["historical_present_distance"]
            for f in run.frames
        ])
        idstep = np.array([
            np.nan if f["identity_step_distance"] is None
            else f["identity_step_distance"]
            for f in run.frames
        ])
        pstep = np.array([
            np.nan if f["perspective_step_distance"] is None
            else f["perspective_step_distance"]
            for f in run.frames
        ])
        index = np.array([
            f["self_index_similarity"]
            for f in run.frames
        ])

        fig, ax1 = plt.subplots(figsize=(8.5, 5.0))
        ax1.plot(g, raw, label="history/present distance")
        ax1.plot(g, pstep, label="raw perspective step", linestyle="--")
        ax1.plot(g, idstep, label="identity trajectory step")
        ax1.set_xlabel("Generation")
        ax1.set_ylabel("Temporal distance")
        ax2 = ax1.twinx()
        ax2.plot(
            g, index, linestyle=":", label="self-index similarity"
        )
        ax2.set_ylabel("Persistent self-index")
        lines = ax1.get_lines()+ax2.get_lines()
        ax1.legend(
            lines,
            [ln.get_label() for ln in lines],
            loc="best",
            fontsize=8,
        )
        ax1.set_title("BFG Identity Closure: continuity through change")
        fig.tight_layout()
        fig.savefig(plot_path, dpi=165)
        plt.close(fig)
    else:
        plot_path = Path("")

    return {
        "frames_csv": str(csv_path),
        "events_json": str(events_path),
        "summary_json": str(summary_path),
        "final_identity_csv": str(identity_path),
        "continuity_plot": str(plot_path),
    }


def write_identity_comparison(
    comparison: dict,
    outdir: str | Path,
    stem: str = "identity_comparison",
) -> dict[str, str]:
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    a = comparison["identity"]
    b = comparison["ablated_control"]
    n = min(len(a.frames), len(b.frames))
    rows = []
    for i in range(n):
        rows.append({
            "generation": a.frames[i]["generation"],
            "environment": a.frames[i]["environment"],
            "identity_closure": a.frames[i]["identity_closure"],
            "historical_present_distance":
                a.frames[i]["historical_present_distance"],
            "identity_step_distance":
                a.frames[i]["identity_step_distance"],
            "raw_perspective_step_distance":
                a.frames[i]["perspective_step_distance"],
            "self_index_similarity":
                a.frames[i]["self_index_similarity"],
            "ablated_self_index_similarity":
                b.frames[i]["self_index_similarity"],
            "transverse_adaptation":
                a.frames[i]["transverse_adaptation"],
        })

    csv_path = outdir/f"{stem}.csv"
    if rows:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)

    summary_path = outdir/f"{stem}_summary.json"
    summary_path.write_text(
        json.dumps(comparison["summary"], indent=2), encoding="utf-8"
    )

    return {
        "comparison_csv": str(csv_path),
        "comparison_summary": str(summary_path),
    }
