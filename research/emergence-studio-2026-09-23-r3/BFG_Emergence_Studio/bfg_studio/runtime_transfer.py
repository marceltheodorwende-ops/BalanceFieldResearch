from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Iterable
from collections import Counter
import csv
import json

import numpy as np
import matplotlib.pyplot as plt

from .types import BFGState, NumericalPolicy
from .finite_closure import (
    ReducedClosureState,
    bfg_state_to_reduced,
    reduced_closure_step,
)
from .portfolio import ValidationPortfolio, STATUS_READY
from .session import source_tree_fingerprint

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


REQUIRED_CARRIERS = (
    "annual-sunspots",
    "mauna-loa-co2",
    "enso-pacific-sst",
)

TRANSFORMATION_METRICS = (
    "alpha",
    "load_log10_ratio",
    "active_rank_ratio",
    "formation_depth_normalized",
    "formation_gap_normalized",
    "neutral_load_density_ratio",
    "k_rms_ratio",
    "successor_y_log10_condition",
)

CORRIDOR_METRICS = (
    "alpha",
    "formation_depth_normalized",
    "formation_gap_normalized",
    "neutral_load_density_ratio",
    "k_rms_ratio",
)


@dataclass(frozen=True)
class TransferSource:
    carrier_id: str
    scope: str
    states: tuple[BFGState, ...]


@dataclass(frozen=True)
class TransferDomainSummary:
    carrier_id: str
    scope: str
    states: int
    processed: int
    exceptions: int
    first_step_successes: int
    first_step_terminals: int
    first_step_success_fraction: float
    maximum_successful_depth: int
    median_successful_depth: float
    q10_successful_depth: float
    q90_successful_depth: float
    terminal_reason_counts: dict[str,int]
    transformation_metrics: dict[str,dict[str,float|None]]
    maximum_unitarity_residual: float | None
    maximum_gram_rebuild_residual: float | None

    def to_dict(self) -> dict[str,Any]:
        return asdict(self)


def _quantiles(values: Iterable[float]) -> dict[str,float|None]:
    x=np.asarray(
        [float(v) for v in values if np.isfinite(v)],
        dtype=float,
    )
    if x.size==0:
        return {
            "mean":None,
            "std":None,
            "q10":None,
            "q25":None,
            "median":None,
            "q75":None,
            "q90":None,
            "min":None,
            "max":None,
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


def transformation_corridor_overlap(
    summaries:list[TransferDomainSummary],
    metric:str,
)->dict[str,Any]:
    lows=[]
    highs=[]
    medians=[]
    carriers=[]
    for summary in summaries:
        q=summary.transformation_metrics.get(metric,{})
        if q.get("q10") is None or q.get("q90") is None:
            continue
        lows.append(float(q["q10"]))
        highs.append(float(q["q90"]))
        medians.append(float(q["median"]))
        carriers.append(summary.carrier_id)

    if not lows:
        return {
            "metric":metric,
            "shared":False,
            "lower":None,
            "upper":None,
            "overlap_ratio":None,
            "median_spread":None,
            "carriers":carriers,
        }

    lower=max(lows)
    upper=min(highs)
    union_lower=min(lows)
    union_upper=max(highs)
    shared=lower<=upper
    overlap=max(0.0,upper-lower)
    union=max(union_upper-union_lower,1e-15)
    return {
        "metric":metric,
        "shared":bool(shared),
        "lower":float(lower) if shared else None,
        "upper":float(upper) if shared else None,
        "overlap_ratio":float(overlap/union),
        "median_spread":float(max(medians)-min(medians)),
        "carriers":carriers,
    }


def _assert_blind_portfolio(
    root:Path,
) -> ValidationPortfolio:
    portfolio=ValidationPortfolio(project_root=root)
    for carrier_id in REQUIRED_CARRIERS:
        entry=portfolio.get(carrier_id)
        if entry.status!=STATUS_READY:
            raise RuntimeError(
                "runtime transfer audit requires READY carrier: "
                f"{carrier_id} is {entry.status}"
            )
        if entry.heldout_metrics_evaluated is not False:
            raise RuntimeError(
                "runtime transfer audit refuses an opened active held-out carrier: "
                f"{carrier_id}"
            )
    return portfolio


def _sunspot_source(root:Path) -> TransferSource:
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
        years,
        values,
        carrier.config.lag,
    )
    states=tuple(
        carrier.map_measurement_to_state(m,generation=i)
        for i,m in enumerate(measurements)
    )
    return TransferSource(
        carrier_id="annual-sunspots",
        scope="development 1700-2008",
        states=states,
    )


def _co2_source(root:Path) -> TransferSource:
    frozen=json.loads(
        (root/"outputs/real_co2/co2_frozen_model.json")
        .read_text(encoding="utf-8")
    )
    cfg=dict(frozen["config"])
    carrier=CO2BFGCarrier(CO2CarrierConfig(**cfg))

    # Calibration only. The sealed 1991-2001 held-out targets are never loaded.
    monthly=load_monthly_calibration(
        calibration_end=carrier.config.calibration_end
    )
    measurements=_co2_measurements(
        monthly,
        carrier.config.lag,
    )
    states=tuple(
        carrier.map_measurement_to_state(m,generation=i)
        for i,m in enumerate(measurements)
    )
    return TransferSource(
        carrier_id="mauna-loa-co2",
        scope=f"calibration through {carrier.config.calibration_end}",
        states=states,
    )


def _enso_source(root:Path) -> TransferSource:
    frozen=json.loads(
        (root/"outputs/real_enso/enso_frozen_model.json")
        .read_text(encoding="utf-8")
    )
    cfg=dict(frozen["config"])
    cfg["month_climatology"]=tuple(cfg["month_climatology"])
    carrier=ENSOBFGCarrier(ENSOCarrierConfig(**cfg))
    series=load_enso_monthly()
    measurements=_enso_measurements(
        series,
        carrier.config.month_climatology,
        carrier.config.lag,
    )
    states=tuple(
        carrier.map_measurement_to_state(m,generation=i)
        for i,m in enumerate(measurements)
    )
    return TransferSource(
        carrier_id="enso-pacific-sst",
        scope="development 1950-01 through 2010-12",
        states=states,
    )


def load_allowed_transfer_sources(
    project_root:str|Path|None=None,
) -> tuple[TransferSource,...]:
    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )
    _assert_blind_portfolio(root)
    return (
        _sunspot_source(root),
        _co2_source(root),
        _enso_source(root),
    )


def _safe_condition(eigvals:np.ndarray) -> float:
    x=np.asarray(eigvals,dtype=float)
    if x.size==0:
        return float("nan")
    lo=float(np.min(x))
    hi=float(np.max(x))
    if lo<=0:
        return float("inf")
    return hi/lo


def _successful_metrics(
    parent:ReducedClosureState,
    successor:ReducedClosureState,
    step,
)->dict[str,float]:
    K=np.asarray(parent.K,dtype=complex)
    Y=np.asarray(parent.Y,dtype=complex)
    Kp=np.asarray(successor.K,dtype=complex)
    Yp=np.asarray(successor.Y,dtype=complex)
    Rp=np.asarray(successor.R,dtype=complex)

    n=K.shape[0]
    np1=Kp.shape[0]

    k_scale=max(float(np.linalg.norm(K,2)),1e-15)
    k_rms=max(float(np.linalg.norm(K,"fro"))/np.sqrt(n),1e-15)
    kp_rms=float(np.linalg.norm(Kp,"fro"))/np.sqrt(np1)

    y_density=max(
        float(np.real(np.trace(Y)))/n,
        1e-15,
    )
    yp_density=float(np.real(np.trace(Yp)))/np1

    ypeig=np.linalg.eigvalsh(
        0.5*(Yp+Yp.conj().T)
    ).real
    ycond=_safe_condition(ypeig)

    load_ratio=max(float(step.lambda_up),1e-300)/max(
        float(step.lambda_keep),1e-300
    )
    recursive_rho=float(
        np.max(np.abs(np.linalg.eigvals(Rp)))
    )

    return {
        "alpha":float(step.alpha),
        "beta":float(step.beta),
        "load_log10_ratio":float(np.log10(load_ratio)),
        "active_rank":float(step.active_rank),
        "persistent_rank":float(step.persistence_rank),
        "active_rank_ratio":float(step.active_rank/n),
        "formation_depth_normalized":
            float(-step.formation_eigenvalue/k_scale),
        "formation_gap_normalized":
            float(step.formation_gap/k_scale),
        "neutral_load_density_ratio":
            float(yp_density/y_density),
        "k_rms_ratio":float(kp_rms/k_rms),
        "successor_y_log10_condition":
            float(np.log10(ycond)) if np.isfinite(ycond) else float("inf"),
        "successor_recursive_rho":recursive_rho,
        "unitarity_residual":float(
            step.diagnostics.get("unitarity_residual",np.nan)
        ),
        "gram_rebuild_residual":float(
            step.diagnostics.get("gram_rebuild_residual",np.nan)
        ),
        "successor_rho_mass":float(
            np.real(np.trace(successor.rho))
        ),
    }


def transfer_one_state(
    state:BFGState,
    *,
    carrier_id:str,
    index:int,
    recursive_horizon:int=4,
    tau:float=1.0,
    policy:NumericalPolicy|None=None,
)->dict[str,Any]:
    if recursive_horizon<1:
        raise ValueError("recursive_horizon must be at least one")
    policy=policy or NumericalPolicy()

    record={
        "carrier_id":carrier_id,
        "index":int(index),
        "source_generation":int(state.generation),
        "source_name":state.name,
        "source_dimension":int(len(state.D)),
        "processed":False,
        "exception":None,
        "first_step_success":False,
        "first_step_terminal":False,
        "first_step_reason":None,
        "successful_depth":0,
        "terminal_within_horizon":False,
        "terminal_reason_within_horizon":None,
    }

    try:
        reduced=bfg_state_to_reduced(state)
        parent=reduced
        current=reduced

        first_success_metrics={}
        for depth in range(1,recursive_horizon+1):
            successor,step=reduced_closure_step(
                current,
                tau=tau,
                policy=policy,
            )

            if depth==1:
                record["first_step_success"]=bool(step.success)
                record["first_step_terminal"]=bool(step.terminal)
                record["first_step_reason"]=step.reason
                record["first_step_alpha"]=step.alpha
                record["first_step_beta"]=step.beta
                record["first_step_lambda_keep"]=step.lambda_keep
                record["first_step_lambda_up"]=step.lambda_up
                record["first_step_active_rank"]=int(step.active_rank)
                record["first_step_persistence_rank"]=int(
                    step.persistence_rank
                )
                record["first_step_formation_eigenvalue"]=(
                    step.formation_eigenvalue
                )
                record["first_step_formation_gap"]=step.formation_gap

                if step.success:
                    first_success_metrics=_successful_metrics(
                        parent,
                        successor,
                        step,
                    )
                    record.update(first_success_metrics)

            if step.success:
                record["successful_depth"]+=1
                current=successor
                continue

            record["terminal_within_horizon"]=bool(
                successor.bottom or step.terminal
            )
            record["terminal_reason_within_horizon"]=(
                step.reason or successor.reason
            )
            break

        record["processed"]=True
        return record

    except Exception as exc:
        record["exception"]=f"{type(exc).__name__}: {exc}"
        return record


def _summarize_domain(
    source:TransferSource,
    records:list[dict[str,Any]],
) -> TransferDomainSummary:
    processed=sum(int(r["processed"]) for r in records)
    exceptions=sum(int(r["exception"] is not None) for r in records)
    success=sum(int(r["first_step_success"]) for r in records)
    terminal=sum(int(r["first_step_terminal"]) for r in records)

    depth=np.asarray(
        [r["successful_depth"] for r in records],
        dtype=float,
    )
    reasons=Counter(
        r["terminal_reason_within_horizon"]
        for r in records
        if r["terminal_reason_within_horizon"]
    )

    metrics={}
    for metric in TRANSFORMATION_METRICS:
        metrics[metric]=_quantiles([
            r.get(metric,np.nan)
            for r in records
            if r["first_step_success"]
        ])

    unitary=[
        r.get("unitarity_residual",np.nan)
        for r in records
        if r["first_step_success"]
    ]
    gram=[
        r.get("gram_rebuild_residual",np.nan)
        for r in records
        if r["first_step_success"]
    ]
    unitary_finite=[x for x in unitary if np.isfinite(x)]
    gram_finite=[x for x in gram if np.isfinite(x)]

    return TransferDomainSummary(
        carrier_id=source.carrier_id,
        scope=source.scope,
        states=len(records),
        processed=processed,
        exceptions=exceptions,
        first_step_successes=success,
        first_step_terminals=terminal,
        first_step_success_fraction=success/max(len(records),1),
        maximum_successful_depth=int(np.max(depth)) if depth.size else 0,
        median_successful_depth=float(np.median(depth)) if depth.size else 0.0,
        q10_successful_depth=float(np.quantile(depth,0.10))
            if depth.size else 0.0,
        q90_successful_depth=float(np.quantile(depth,0.90))
            if depth.size else 0.0,
        terminal_reason_counts=dict(sorted(reasons.items())),
        transformation_metrics=metrics,
        maximum_unitarity_residual=(
            float(max(unitary_finite)) if unitary_finite else None
        ),
        maximum_gram_rebuild_residual=(
            float(max(gram_finite)) if gram_finite else None
        ),
    )


def run_master_runtime_transfer_audit(
    project_root:str|Path|None=None,
    *,
    recursive_horizon:int=4,
    tau:float=1.0,
    limit_per_carrier:int|None=None,
) -> dict[str,Any]:
    """
    Transport allowed real-domain development/calibration states through the
    same reduced finite master runtime.

    No held-out target values are opened.
    """
    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )
    portfolio=_assert_blind_portfolio(root)
    sources=load_allowed_transfer_sources(root)

    all_records=[]
    summaries=[]
    for source in sources:
        states=source.states
        if limit_per_carrier is not None:
            if limit_per_carrier<1:
                raise ValueError("limit_per_carrier must be positive")
            states=states[:limit_per_carrier]

        records=[
            transfer_one_state(
                state,
                carrier_id=source.carrier_id,
                index=i,
                recursive_horizon=recursive_horizon,
                tau=tau,
            )
            for i,state in enumerate(states)
        ]
        all_records.extend(records)
        summaries.append(
            _summarize_domain(
                TransferSource(
                    carrier_id=source.carrier_id,
                    scope=source.scope,
                    states=tuple(states),
                ),
                records,
            )
        )

    corridors=[
        transformation_corridor_overlap(summaries,metric)
        for metric in CORRIDOR_METRICS
    ]

    processed=sum(s.processed for s in summaries)
    total=sum(s.states for s in summaries)
    exceptions=sum(s.exceptions for s in summaries)
    first_success=sum(s.first_step_successes for s in summaries)

    max_unitary=max(
        (
            s.maximum_unitarity_residual
            for s in summaries
            if s.maximum_unitarity_residual is not None
        ),
        default=None,
    )
    max_gram=max(
        (
            s.maximum_gram_rebuild_residual
            for s in summaries
            if s.maximum_gram_rebuild_residual is not None
        ),
        default=None,
    )

    invariant_success=bool(
        (max_unitary is None or max_unitary<=1e-8)
        and (max_gram is None or max_gram<=1e-10)
    )

    return {
        "status":"DEVELOPMENT_ONLY_MASTER_RUNTIME_TRANSFER_AUDIT",
        "source_fingerprint":source_tree_fingerprint(),
        "audit_passed":bool(
            processed==total
            and exceptions==0
            and invariant_success
        ),
        "heldout_metrics_evaluated":False,
        "recursive_horizon":int(recursive_horizon),
        "tau":float(tau),
        "limit_per_carrier":limit_per_carrier,
        "states_total":total,
        "states_processed":processed,
        "exceptions":exceptions,
        "first_step_successes":first_success,
        "first_step_success_fraction":first_success/max(total,1),
        "maximum_unitarity_residual":max_unitary,
        "maximum_gram_rebuild_residual":max_gram,
        "carriers":[s.to_dict() for s in summaries],
        "shared_transformation_corridors":corridors,
        "records":all_records,
        "portfolio_status":{
            e.carrier_id:{
                "status":e.status,
                "heldout_metrics_evaluated":e.heldout_metrics_evaluated,
            }
            for e in portfolio.entries
            if e.carrier_id in REQUIRED_CARRIERS
        },
        "interpretation_guard":{
            "empirical_confirmation":False,
            "universal_natural_transformation_established":False,
            "note":(
                "This audit tests whether already-allowed development/calibration "
                "states are processed by one common finite master transform. "
                "Shared transformation corridors are exploratory structural "
                "results and do not open or replace confirmatory held-out tests."
            ),
        },
    }


def write_master_runtime_transfer_report(
    result:dict[str,Any],
    outdir:str|Path,
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    # Full machine-readable result without duplicating large records in Markdown.
    json_path=outdir/"master_runtime_transfer_audit.json"
    json_path.write_text(
        json.dumps(result,indent=2),
        encoding="utf-8",
    )

    records=result["records"]
    csv_path=outdir/"master_runtime_transfer_records.csv"
    if records:
        fieldnames=sorted({
            key
            for row in records
            for key in row.keys()
        })
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            writer=csv.DictWriter(
                f,
                fieldnames=fieldnames,
                extrasaction="ignore",
            )
            writer.writeheader()
            writer.writerows(records)

    md_path=outdir/"MASTER_RUNTIME_TRANSFER_AUDIT.md"
    lines=[
        "# BFG Master Runtime Transfer Audit",
        "",
        f"Audit: **{'PASS' if result['audit_passed'] else 'FAIL'}**",
        "",
        "**No active held-out target metric is opened by this audit.**",
        "",
        f"States processed: `{result['states_processed']}/{result['states_total']}`",
        "",
        f"First-step nonterminal transfers: "
        f"`{result['first_step_successes']}/{result['states_total']}` "
        f"(`{100*result['first_step_success_fraction']:.3f}%`)",
        "",
        f"Recursive diagnostic horizon: `{result['recursive_horizon']}`",
        "",
        "| Carrier | States | First-step success | Median successful depth | "
        "Max depth | Max unitarity residual | Max Gram residual |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for s in result["carriers"]:
        lines.append(
            f"| {s['carrier_id']} | {s['states']} | "
            f"{100*s['first_step_success_fraction']:.3f}% | "
            f"{s['median_successful_depth']:.3f} | "
            f"{s['maximum_successful_depth']} | "
            f"{s['maximum_unitarity_residual']:.3e} | "
            f"{s['maximum_gram_rebuild_residual']:.3e} |"
        )

    lines += [
        "",
        "## Terminal reasons within the recursive diagnostic horizon",
        "",
    ]
    for s in result["carriers"]:
        lines.append(f"### {s['carrier_id']}")
        reasons=s["terminal_reason_counts"]
        if not reasons:
            lines.append("- none")
        else:
            for reason,count in reasons.items():
                lines.append(f"- `{reason}`: {count}")
        lines.append("")

    lines += [
        "## Cross-domain transformation corridors",
        "",
        "| Metric | Shared q10-q90 corridor | Lower | Upper | Overlap ratio |",
        "|---|---:|---:|---:|---:|",
    ]
    for c in result["shared_transformation_corridors"]:
        lower="" if c["lower"] is None else f"{c['lower']:.6g}"
        upper="" if c["upper"] is None else f"{c['upper']:.6g}"
        overlap=(
            ""
            if c["overlap_ratio"] is None
            else f"{c['overlap_ratio']:.4f}"
        )
        lines.append(
            f"| {c['metric']} | {c['shared']} | "
            f"{lower} | {upper} | {overlap} |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "The first-step result asks whether heterogeneous real-domain states can "
        "enter the same finite BFG master transformation without a domain-specific "
        "successor law.",
        "",
        "The recursive-depth diagnostic is deliberately separate. A later bottom "
        "state is a legitimate total-map outcome; it is not reclassified as a "
        "software failure.",
        "",
        "Shared corridors are exploratory transformation coordinates, not "
        "confirmatory evidence of a universal natural law.",
    ]
    md_path.write_text(
        "\n".join(lines)+"\n",
        encoding="utf-8",
    )

    # Cross-domain corridor overlap chart.
    corridors=result["shared_transformation_corridors"]
    names=[c["metric"] for c in corridors]
    values=[
        float(c["overlap_ratio"] or 0.0)
        for c in corridors
    ]
    plot_path=outdir/"transformation_corridor_overlap.png"
    fig,ax=plt.subplots(figsize=(8.5,4.8))
    ax.bar(np.arange(len(names)),values)
    ax.set_xticks(
        np.arange(len(names)),
        names,
        rotation=30,
        ha="right",
    )
    ax.set_ylabel("q10-q90 overlap / union")
    ax.set_title(
        "Cross-domain master-transformation corridor overlap"
    )
    fig.tight_layout()
    fig.savefig(plot_path,dpi=170)
    plt.close(fig)

    return {
        "json":str(json_path),
        "csv":str(csv_path),
        "markdown":str(md_path),
        "plot":str(plot_path),
    }
