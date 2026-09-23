from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Callable
import csv
import json

import numpy as np
import matplotlib.pyplot as plt

from .types import NumericalPolicy
from .core import canonical_reclosure, neutral_pair
from .portfolio import ValidationPortfolio, STATUS_READY

from .sunspot_carrier import load_sunspots, build_window_measurements
from .sunspot_validation import (
    SunspotValidationConfig,
    AnnualSunspotValidationCarrier,
)

from .co2_carrier import (
    CO2CarrierConfig,
    CO2BFGCarrier,
    load_monthly_calibration,
    _measurements_from_monthly as _co2_measurements,
)

from .enso_carrier import (
    ENSOCarrierConfig,
    ENSOBFGCarrier,
    load_enso_monthly,
    _measurements as _enso_measurements,
)


COMPARABLE_METRICS = (
    "neutral_retention",
    "formation_rayleigh",
    "crossfed_gain",
    "omega_keep",
    "lambda_up",
    "spectral_mismatch",
    "commutator_norm",
    "second_moment_loss",
    "recursive_rho",
)

CORRIDOR_METRICS = (
    "neutral_retention",
    "crossfed_gain",
    "omega_keep",
    "spectral_mismatch",
    "recursive_rho",
)


@dataclass
class DomainInvariantSummary:
    carrier_id: str
    samples: int
    successful_reclosures: int
    novelty_fraction_among_successful: float
    metrics: dict[str,dict[str,float|None]]

    def to_dict(self):
        return asdict(self)


def _quantiles(values:list[float])->dict[str,float|None]:
    x=np.asarray([v for v in values if np.isfinite(v)],dtype=float)
    if x.size==0:
        return {
            "mean":None,"std":None,
            "q10":None,"q25":None,"median":None,
            "q75":None,"q90":None,
            "min":None,"max":None,
        }
    q=np.quantile(x,[0.10,0.25,0.50,0.75,0.90])
    return {
        "mean":float(np.mean(x)),
        "std":float(np.std(x)),
        "q10":float(q[0]),
        "q25":float(q[1]),
        "median":float(q[2]),
        "q75":float(q[3]),
        "q90":float(q[4]),
        "min":float(np.min(x)),
        "max":float(np.max(x)),
    }


def _step_record(state,step)->dict[str,Any]:
    C,_=neutral_pair(state.Y)
    denom=max(float(np.real(np.vdot(state.D,state.D))),1e-12)
    neutral_retention=float(
        np.real(np.vdot(state.D,C@state.D))/denom
    )
    formation_rayleigh=float(
        np.real(np.vdot(state.D,state.K@state.D))/denom
    )
    rho=float(np.max(np.abs(np.linalg.eigvals(state.R_C))))
    return {
        "neutral_retention":neutral_retention,
        "formation_rayleigh":formation_rayleigh,
        "crossfed_gain":float(
            step.diagnostics.get("crossfed_gain",np.nan)
        ),
        "omega_keep":(
            float(step.omega_keep)
            if step.omega_keep is not None else np.nan
        ),
        "lambda_up":(
            float(step.lambda_up)
            if step.lambda_up is not None else np.nan
        ),
        "spectral_mismatch":(
            float(step.spectral_mismatch)
            if step.spectral_mismatch is not None else np.nan
        ),
        "commutator_norm":(
            float(step.commutator_norm)
            if step.commutator_norm is not None else np.nan
        ),
        "second_moment_loss":(
            float(step.second_moment_loss)
            if step.second_moment_loss is not None else np.nan
        ),
        "recursive_rho":rho,
        "neutral_partition_residual":float(
            step.diagnostics.get("neutral_partition_residual",np.nan)
        ),
        "reciprocal_balance_residual":float(
            step.diagnostics.get("reciprocal_balance_residual",np.nan)
        ),
        "persistent_rank":step.diagnostics.get("persistent_rank"),
        "support_rank":step.diagnostics.get("support_rank"),
        "reclosure_success":bool(step.success),
        "spectral_novelty":(
            bool(step.spectral_novelty)
            if step.spectral_novelty is not None else False
        ),
    }


def _summarize_records(
    carrier_id:str,
    records:list[dict[str,Any]],
)->DomainInvariantSummary:
    successful=sum(int(r["reclosure_success"]) for r in records)
    novel=sum(
        int(r["spectral_novelty"])
        for r in records if r["reclosure_success"]
    )
    metrics={
        name:_quantiles([
            float(r[name])
            for r in records
            if r.get(name) is not None
        ])
        for name in COMPARABLE_METRICS
    }
    return DomainInvariantSummary(
        carrier_id=carrier_id,
        samples=len(records),
        successful_reclosures=successful,
        novelty_fraction_among_successful=(
            novel/max(successful,1)
        ),
        metrics=metrics,
    )


def _sunspot_records(root:Path)->list[dict[str,Any]]:
    frozen=json.loads(
        (root/"outputs/real_sunspots/sunspot_frozen_model.json")
        .read_text(encoding="utf-8")
    )
    cfg=dict(frozen["config"])
    cfg["ar_coefficients"]=tuple(cfg["ar_coefficients"])
    carrier=AnnualSunspotValidationCarrier(
        SunspotValidationConfig(**cfg)
    )
    years,values=load_sunspots()
    measurements=build_window_measurements(
        years,values,carrier.config.lag
    )
    policy=NumericalPolicy()
    records=[]
    for i,m in enumerate(measurements):
        state=carrier.map_measurement_to_state(m,generation=i)
        step=canonical_reclosure(state,policy)
        records.append(_step_record(state,step))
    return records


def _co2_records(root:Path)->list[dict[str,Any]]:
    frozen=json.loads(
        (root/"outputs/real_co2/co2_frozen_model.json")
        .read_text(encoding="utf-8")
    )
    cfg=dict(frozen["config"])
    carrier=CO2BFGCarrier(CO2CarrierConfig(**cfg))
    # Critical guard: only the calibration period is transformed here.
    monthly=load_monthly_calibration(
        calibration_end=carrier.config.calibration_end
    )
    measurements=_co2_measurements(
        monthly,carrier.config.lag
    )
    policy=NumericalPolicy()
    records=[]
    for i,m in enumerate(measurements):
        state=carrier.map_measurement_to_state(m,generation=i)
        step=canonical_reclosure(state,policy)
        records.append(_step_record(state,step))
    return records


def _enso_records(root:Path)->list[dict[str,Any]]:
    frozen=json.loads(
        (root/"outputs/real_enso/enso_frozen_model.json")
        .read_text(encoding="utf-8")
    )
    cfg=dict(frozen["config"])
    cfg["month_climatology"]=tuple(cfg["month_climatology"])
    carrier=ENSOBFGCarrier(ENSOCarrierConfig(**cfg))
    series=load_enso_monthly()
    measurements=_enso_measurements(
        series,carrier.config.month_climatology,carrier.config.lag
    )
    policy=NumericalPolicy()
    records=[]
    for i,m in enumerate(measurements):
        state=carrier.map_measurement_to_state(m,generation=i)
        step=canonical_reclosure(state,policy)
        records.append(_step_record(state,step))
    return records


def corridor_overlap(
    summaries:list[DomainInvariantSummary],
    metric:str,
)->dict[str,Any]:
    lows=[]
    highs=[]
    medians=[]
    for s in summaries:
        q=s.metrics[metric]
        if q["q10"] is None or q["q90"] is None:
            continue
        lows.append(float(q["q10"]))
        highs.append(float(q["q90"]))
        medians.append(float(q["median"]))
    if not lows:
        return {
            "metric":metric,
            "shared":False,
            "lower":None,"upper":None,
            "overlap_ratio":None,
            "median_spread":None,
        }
    lower=max(lows)
    upper=min(highs)
    union_lower=min(lows)
    union_upper=max(highs)
    shared=lower<=upper
    overlap=max(0.0,upper-lower)
    union=max(union_upper-union_lower,1e-12)
    return {
        "metric":metric,
        "shared":shared,
        "lower":float(lower) if shared else None,
        "upper":float(upper) if shared else None,
        "overlap_ratio":float(overlap/union),
        "median_spread":float(max(medians)-min(medians)),
    }


def run_cross_domain_invariants(
    project_root:str|Path|None=None,
)->dict[str,Any]:
    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )
    portfolio=ValidationPortfolio(project_root=root)
    required=("annual-sunspots","mauna-loa-co2","enso-pacific-sst")
    for carrier_id in required:
        entry=portfolio.get(carrier_id)
        if entry.status!=STATUS_READY:
            raise RuntimeError(
                f"cross-domain development analysis requires READY carrier: "
                f"{carrier_id} is {entry.status}"
            )
        if entry.heldout_metrics_evaluated is not False:
            raise RuntimeError(
                f"cross-domain analysis refuses opened active held-out carrier: "
                f"{carrier_id}"
            )

    domain_records={
        "annual-sunspots":_sunspot_records(root),
        "mauna-loa-co2":_co2_records(root),
        "enso-pacific-sst":_enso_records(root),
    }
    summaries=[
        _summarize_records(cid,records)
        for cid,records in domain_records.items()
    ]
    corridors=[
        corridor_overlap(summaries,m)
        for m in CORRIDOR_METRICS
    ]

    all_success=all(
        s.successful_reclosures==s.samples
        for s in summaries
    )
    all_novel=all(
        s.novelty_fraction_among_successful>=0.999
        for s in summaries
    )

    return {
        "status":"DEVELOPMENT_ONLY_CROSS_DOMAIN_ANALYSIS",
        "heldout_metrics_evaluated":False,
        "carriers":[s.to_dict() for s in summaries],
        "shared_corridors":corridors,
        "all_development_reclosures_successful":all_success,
        "all_successful_reclosures_novel":all_novel,
        "interpretation_guard":{
            "empirical_universal_invariant_established":False,
            "note":(
                "Shared development-coordinate corridors are exploratory carrier "
                "comparisons. They do not establish a universal natural invariant "
                "until independently frozen held-out carriers support the same "
                "structure without retuning."
            ),
        },
    }


def write_cross_domain_report(
    result:dict[str,Any],
    outdir:str|Path,
):
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"cross_domain_invariants.json"
    json_path.write_text(
        json.dumps(result,indent=2),encoding="utf-8"
    )

    # Domain/metric summary CSV.
    rows=[]
    for carrier in result["carriers"]:
        for metric,stats in carrier["metrics"].items():
            rows.append({
                "carrier_id":carrier["carrier_id"],
                "samples":carrier["samples"],
                "metric":metric,
                **stats,
            })
    csv_path=outdir/"cross_domain_invariants.csv"
    if rows:
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(f,fieldnames=list(rows[0].keys()))
            w.writeheader();w.writerows(rows)

    md_path=outdir/"CROSS_DOMAIN_INVARIANTS.md"
    lines=[
        "# BFG Cross-Domain Invariants — Development-Only Analysis",
        "",
        "Carriers: Annual Sunspots, Mauna Loa CO2, ENSO Pacific SST.",
        "",
        "**No active held-out target metric is opened by this analysis.**",
        "",
        "| Metric | Shared q10–q90 corridor | Lower | Upper | Overlap ratio |",
        "|---|---:|---:|---:|---:|",
    ]
    for c in result["shared_corridors"]:
        lines.append(
            "| {metric} | {shared} | {lower} | {upper} | {overlap} |".format(
                metric=c["metric"],
                shared=c["shared"],
                lower="" if c["lower"] is None else f"{c['lower']:.6g}",
                upper="" if c["upper"] is None else f"{c['upper']:.6g}",
                overlap="" if c["overlap_ratio"] is None else f"{c['overlap_ratio']:.4f}",
            )
        )
    lines += [
        "",
        f"All development reclosures successful: "
        f"`{result['all_development_reclosures_successful']}`",
        "",
        f"Novelty on all successful development reclosures: "
        f"`{result['all_successful_reclosures_novel']}`",
        "",
        "Interpretation: these are exploratory shared carrier-coordinate corridors, "
        "not proof of a universal empirical BFG invariant.",
    ]
    md_path.write_text("\n".join(lines)+"\n",encoding="utf-8")

    # One compact chart: overlap ratio for selected comparable dimensionless metrics.
    names=[c["metric"] for c in result["shared_corridors"]]
    vals=[c["overlap_ratio"] or 0.0 for c in result["shared_corridors"]]
    fig,ax=plt.subplots(figsize=(8.0,4.6))
    ax.bar(np.arange(len(names)),vals)
    ax.set_xticks(np.arange(len(names)),names,rotation=30,ha="right")
    ax.set_ylabel("q10–q90 overlap / union")
    ax.set_title("Cross-domain development corridor overlap")
    fig.tight_layout()
    plot_path=outdir/"cross_domain_corridor_overlap.png"
    fig.savefig(plot_path,dpi=170)
    plt.close(fig)

    return {
        "json":str(json_path),
        "csv":str(csv_path),
        "markdown":str(md_path),
        "plot":str(plot_path),
    }
