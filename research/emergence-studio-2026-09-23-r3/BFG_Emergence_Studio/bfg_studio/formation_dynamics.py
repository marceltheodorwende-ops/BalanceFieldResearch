from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from collections import Counter, defaultdict
from typing import Any
import csv
import json

import numpy as np
import matplotlib.pyplot as plt

from .types import NumericalPolicy
from .finite_closure import (
    bfg_state_to_reduced,
    reduced_closure_step,
)
from .runtime_transfer import (
    load_allowed_transfer_sources,
    transformation_corridor_overlap,
    TransferDomainSummary,
)
from .session import source_tree_fingerprint


FORMATION_NORMALIZATIONS = (
    "depth_over_spectral_norm",
    "depth_over_rms_norm",
    "depth_over_gap",
    "depth_over_mean_abs_eigenvalue",
)

DECAY_METRICS = (
    "parent_y_density",
    "successor_y_density",
    "lambda_keep",
    "lambda_up",
    "dual_load_min",
    "alpha",
)


@dataclass(frozen=True)
class FormationDomainSummary:
    carrier_id: str
    states: int
    first_step_successes: int
    max_successful_depth: int
    median_successful_depth: float
    terminal_reason_counts: dict[str,int]
    first_step_normalizations: dict[str,dict[str,float|None]]
    loglog_y_decay_exponent: float | None
    loglog_y_decay_intercept: float | None
    y_decay_pairs: int
    median_log10_dual_margin_by_depth: dict[str,float|None]
    median_log10_y_margin_by_depth: dict[str,float|None]

    def to_dict(self) -> dict[str,Any]:
        return asdict(self)


def scalar_neutral_load_map(y: float) -> float:
    """
    Exact one-dimensional reduced-master recurrence for K=-1, rho=1, Y=y>0.

        y_+ = 2 y^2 / ((1+y)^2 (1+y^2))

    Hence y_+ ~ 2 y^2 as y -> 0+.
    """
    y=float(y)
    if not np.isfinite(y) or y<=0:
        raise ValueError("y must be positive finite")
    return float(
        2.0*y*y / ((1.0+y)**2 * (1.0+y*y))
    )


def _qstats(values:list[float]) -> dict[str,float|None]:
    x=np.asarray(
        [float(v) for v in values if np.isfinite(v)],
        dtype=float,
    )
    if x.size==0:
        return {
            "mean":None,"std":None,
            "q10":None,"q25":None,"median":None,
            "q75":None,"q90":None,
            "min":None,"max":None,
        }
    q=np.quantile(x,[.10,.25,.50,.75,.90])
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


def _parent_k_scales(K:np.ndarray) -> dict[str,float]:
    """
    Scale coordinates of the parent K.

    The formation-depth numerator itself comes from the reclosed K_+ through
    step.formation_eigenvalue. This preserves continuity with the original
    master-transfer metric.
    """
    kh=0.5*(K+K.conj().T)
    vals=np.linalg.eigvalsh(kh).real
    vals=np.sort(vals)

    spectral=max(float(np.max(np.abs(vals))),1e-300)
    rms=max(float(np.sqrt(np.mean(vals*vals))),1e-300)
    mean_abs=max(float(np.mean(np.abs(vals))),1e-300)
    spectral_range=(
        max(float(vals[-1]-vals[0]),1e-300)
        if len(vals)>1 else spectral
    )

    return {
        "parent_lambda0":float(vals[0]),
        "parent_k_spectral_norm":spectral,
        "parent_k_rms_norm":rms,
        "parent_k_mean_abs_eigenvalue":mean_abs,
        "parent_k_spectral_range":spectral_range,
    }


def _positive_density(Y:np.ndarray) -> tuple[float,float]:
    yh=0.5*(Y+Y.conj().T)
    vals=np.linalg.eigvalsh(yh).real
    density=float(np.real(np.trace(yh)))/len(vals)
    return density,float(np.min(vals))


def _fit_loglog(
    x:list[float],
    y:list[float],
) -> tuple[float|None,float|None,int]:
    pairs=[
        (float(a),float(b))
        for a,b in zip(x,y)
        if np.isfinite(a) and np.isfinite(b)
        and a>0 and b>0
    ]
    if len(pairs)<2:
        return None,None,len(pairs)
    lx=np.log10([p[0] for p in pairs])
    ly=np.log10([p[1] for p in pairs])
    X=np.column_stack([np.ones(len(lx)),lx])
    beta=np.linalg.lstsq(X,ly,rcond=None)[0]
    return float(beta[1]),float(beta[0]),len(pairs)


def _analyze_one_state(
    state,
    *,
    carrier_id:str,
    index:int,
    horizon:int,
    tau:float,
    policy:NumericalPolicy,
) -> tuple[list[dict[str,Any]],dict[str,Any]]:
    current=bfg_state_to_reduced(state)
    transitions=[]
    summary={
        "carrier_id":carrier_id,
        "index":index,
        "successful_depth":0,
        "terminal_reason":None,
        "terminal_depth":None,
    }

    for depth_index in range(horizon):
        depth=depth_index+1
        parent_K=np.asarray(current.K,dtype=complex)
        parent_Y=np.asarray(current.Y,dtype=complex)
        parent_scales=_parent_k_scales(parent_K)
        y_density,y_min=_positive_density(parent_Y)

        successor,step=reduced_closure_step(
            current,
            tau=tau,
            policy=policy,
        )

        lk=(
            float(step.lambda_keep)
            if step.lambda_keep is not None else float("nan")
        )
        lu=(
            float(step.lambda_up)
            if step.lambda_up is not None else float("nan")
        )
        dual_min=(
            min(lk,lu)
            if np.isfinite(lk) and np.isfinite(lu)
            else float("nan")
        )
        dual_margin=(
            dual_min/policy.atol
            if np.isfinite(dual_min) and dual_min>0
            else 0.0
        )
        y_margin=(
            y_min/policy.psd_tol
            if np.isfinite(y_min) and y_min>0
            else 0.0
        )

        formation_eigenvalue=(
            float(step.formation_eigenvalue)
            if step.formation_eigenvalue is not None
            else float("nan")
        )
        formation_gap=(
            float(step.formation_gap)
            if step.formation_gap is not None
            else float("nan")
        )
        formation_depth=(
            -formation_eigenvalue
            if np.isfinite(formation_eigenvalue)
            else float("nan")
        )
        depth_over_gap=(
            formation_depth/formation_gap
            if (
                np.isfinite(formation_depth)
                and np.isfinite(formation_gap)
                and formation_gap>0
            )
            else float("nan")
        )

        row={
            "carrier_id":carrier_id,
            "state_index":index,
            "depth":depth,
            "success":bool(step.success),
            "terminal":bool(step.terminal),
            "reason":step.reason,
            **parent_scales,
            "formation_eigenvalue":formation_eigenvalue,
            "formation_depth":formation_depth,
            "formation_gap":formation_gap,
            "depth_over_spectral_norm":(
                formation_depth/parent_scales["parent_k_spectral_norm"]
                if np.isfinite(formation_depth)
                else float("nan")
            ),
            "depth_over_rms_norm":(
                formation_depth/parent_scales["parent_k_rms_norm"]
                if np.isfinite(formation_depth)
                else float("nan")
            ),
            "depth_over_gap":depth_over_gap,
            "depth_over_mean_abs_eigenvalue":(
                formation_depth
                /parent_scales["parent_k_mean_abs_eigenvalue"]
                if np.isfinite(formation_depth)
                else float("nan")
            ),
            "parent_y_density":y_density,
            "parent_y_min":y_min,
            "lambda_keep":lk,
            "lambda_up":lu,
            "dual_load_min":dual_min,
            "log10_dual_margin":(
                float(np.log10(dual_margin))
                if dual_margin>0 else float("-inf")
            ),
            "log10_y_margin":(
                float(np.log10(y_margin))
                if y_margin>0 else float("-inf")
            ),
            "alpha":(
                float(step.alpha)
                if step.alpha is not None else float("nan")
            ),
            "beta":(
                float(step.beta)
                if step.beta is not None else float("nan")
            ),
            "active_rank":int(step.active_rank),
            "persistence_rank":int(step.persistence_rank),
            "successor_y_density":float("nan"),
            "successor_y_min":float("nan"),
            "y_density_ratio":float("nan"),
            "unitarity_residual":float("nan"),
            "gram_rebuild_residual":float("nan"),
        }

        if step.success:
            sy_density,sy_min=_positive_density(
                np.asarray(successor.Y,dtype=complex)
            )
            row["successor_y_density"]=sy_density
            row["successor_y_min"]=sy_min
            row["y_density_ratio"]=sy_density/max(
                y_density,1e-300
            )
            row["unitarity_residual"]=float(
                step.diagnostics.get(
                    "unitarity_residual",np.nan
                )
            )
            row["gram_rebuild_residual"]=float(
                step.diagnostics.get(
                    "gram_rebuild_residual",np.nan
                )
            )
            summary["successful_depth"]+=1
            current=successor
        else:
            summary["terminal_reason"]=step.reason
            summary["terminal_depth"]=depth

        transitions.append(row)

        if not step.success:
            break

    return transitions,summary


def _domain_summary(
    carrier_id:str,
    state_summaries:list[dict[str,Any]],
    rows:list[dict[str,Any]],
) -> FormationDomainSummary:
    first=[
        r for r in rows
        if r["depth"]==1
    ]
    first_success=[
        r for r in first if r["success"]
    ]

    normalizations={
        name:_qstats([
            r[name] for r in first_success
        ])
        for name in FORMATION_NORMALIZATIONS
    }

    parent_y=[
        r["parent_y_density"]
        for r in rows
        if r["success"]
    ]
    successor_y=[
        r["successor_y_density"]
        for r in rows
        if r["success"]
    ]
    exponent,intercept,pairs=_fit_loglog(
        parent_y,successor_y
    )

    dual_by_depth=defaultdict(list)
    y_by_depth=defaultdict(list)
    for r in rows:
        if np.isfinite(r["log10_dual_margin"]):
            dual_by_depth[str(r["depth"])].append(
                r["log10_dual_margin"]
            )
        if np.isfinite(r["log10_y_margin"]):
            y_by_depth[str(r["depth"])].append(
                r["log10_y_margin"]
            )

    terminal_counts=Counter(
        s["terminal_reason"]
        for s in state_summaries
        if s["terminal_reason"]
    )
    depths=np.asarray([
        s["successful_depth"]
        for s in state_summaries
    ],dtype=float)

    return FormationDomainSummary(
        carrier_id=carrier_id,
        states=len(state_summaries),
        first_step_successes=len(first_success),
        max_successful_depth=int(np.max(depths))
            if depths.size else 0,
        median_successful_depth=float(np.median(depths))
            if depths.size else 0.0,
        terminal_reason_counts=dict(
            sorted(terminal_counts.items())
        ),
        first_step_normalizations=normalizations,
        loglog_y_decay_exponent=exponent,
        loglog_y_decay_intercept=intercept,
        y_decay_pairs=pairs,
        median_log10_dual_margin_by_depth={
            depth:float(np.median(vals))
            for depth,vals in sorted(
                dual_by_depth.items(),
                key=lambda kv:int(kv[0]),
            )
        },
        median_log10_y_margin_by_depth={
            depth:float(np.median(vals))
            for depth,vals in sorted(
                y_by_depth.items(),
                key=lambda kv:int(kv[0]),
            )
        },
    )


def _normalization_corridors(
    summaries:list[FormationDomainSummary],
) -> list[dict[str,Any]]:
    # Reuse the same corridor definition, but create the narrow summary shape
    # expected by the cross-domain helper.
    converted=[]
    for s in summaries:
        converted.append(
            TransferDomainSummary(
                carrier_id=s.carrier_id,
                scope="formation-analysis",
                states=s.states,
                processed=s.states,
                exceptions=0,
                first_step_successes=s.first_step_successes,
                first_step_terminals=(
                    s.states-s.first_step_successes
                ),
                first_step_success_fraction=(
                    s.first_step_successes/max(s.states,1)
                ),
                maximum_successful_depth=s.max_successful_depth,
                median_successful_depth=s.median_successful_depth,
                q10_successful_depth=0.0,
                q90_successful_depth=0.0,
                terminal_reason_counts=s.terminal_reason_counts,
                transformation_metrics=s.first_step_normalizations,
                maximum_unitarity_residual=None,
                maximum_gram_rebuild_residual=None,
            )
        )
    return [
        transformation_corridor_overlap(
            converted,
            metric,
        )
        for metric in FORMATION_NORMALIZATIONS
    ]


def _scaled_policy(
    base:NumericalPolicy,
    scale:float,
)->NumericalPolicy:
    if not np.isfinite(scale) or scale<=0:
        raise ValueError("tolerance scale must be positive finite")
    return NumericalPolicy(
        atol=base.atol*scale,
        rtol=base.rtol,
        peripheral_tol=base.peripheral_tol,
        rank_tol=base.rank_tol,
        simple_gap_tol=base.simple_gap_tol,
        psd_tol=base.psd_tol*scale,
        novelty_tol=base.novelty_tol,
    )


def run_tolerance_sensitivity(
    project_root:str|Path|None=None,
    *,
    scales:tuple[float,...]=(0.1,1.0,10.0),
    horizon:int=8,
    tau:float=1.0,
    limit_per_carrier:int|None=None,
) -> dict[str,Any]:
    """
    Diagnose whether recursive bottom depth is controlled by the floating
    admissibility floor.

    Only atol and psd_tol are scaled. Rank, spectral and gap tolerances are kept
    fixed so the audit isolates the two numerical floors implicated by the
    observed terminal reasons.
    """
    if horizon<2:
        raise ValueError("horizon must be at least two")
    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )
    sources=load_allowed_transfer_sources(root)
    base=NumericalPolicy()
    results=[]

    for scale in scales:
        policy=_scaled_policy(base,float(scale))
        carrier_rows=[]
        all_depths=[]
        total_terminal=Counter()

        for source in sources:
            depths=[]
            reasons=Counter()
            states=source.states
            if limit_per_carrier is not None:
                if limit_per_carrier<1:
                    raise ValueError("limit_per_carrier must be positive")
                states=states[:limit_per_carrier]
            for state in states:
                current=bfg_state_to_reduced(state)
                successful=0
                reason=None
                for _ in range(horizon):
                    nxt,step=reduced_closure_step(
                        current,
                        tau=tau,
                        policy=policy,
                    )
                    if step.success:
                        successful+=1
                        current=nxt
                    else:
                        reason=step.reason
                        if reason:
                            reasons[reason]+=1
                            total_terminal[reason]+=1
                        break
                depths.append(successful)
                all_depths.append(successful)

            arr=np.asarray(depths,dtype=float)
            carrier_rows.append({
                "carrier_id":source.carrier_id,
                "states":len(depths),
                "median_successful_depth":
                    float(np.median(arr)),
                "q10_successful_depth":
                    float(np.quantile(arr,.10)),
                "q90_successful_depth":
                    float(np.quantile(arr,.90)),
                "max_successful_depth":
                    int(np.max(arr)),
                "terminal_reason_counts":
                    dict(sorted(reasons.items())),
            })

        arr=np.asarray(all_depths,dtype=float)
        results.append({
            "scale":float(scale),
            "atol":policy.atol,
            "psd_tol":policy.psd_tol,
            "states":len(all_depths),
            "median_successful_depth":
                float(np.median(arr)),
            "q10_successful_depth":
                float(np.quantile(arr,.10)),
            "q90_successful_depth":
                float(np.quantile(arr,.90)),
            "max_successful_depth":
                int(np.max(arr)),
            "carriers":carrier_rows,
            "terminal_reason_counts":
                dict(sorted(total_terminal.items())),
        })

    return {
        "scales":[float(s) for s in scales],
        "horizon":horizon,
        "limit_per_carrier":limit_per_carrier,
        "heldout_metrics_evaluated":False,
        "scaled_tolerances":["atol","psd_tol"],
        "fixed_tolerances":[
            "rtol","peripheral_tol","rank_tol",
            "simple_gap_tol","novelty_tol",
        ],
        "results":results,
    }


def run_formation_termination_analysis(
    project_root:str|Path|None=None,
    *,
    horizon:int=6,
    tau:float=1.0,
    limit_per_carrier:int|None=None,
    compute_tolerance_sensitivity:bool=True,
) -> dict[str,Any]:
    """
    Development/calibration-only analysis of:

        formation geometry
        -> neutral-load contraction
        -> dual-load margin
        -> terminal bottom surface.

    No normalization is selected based on held-out behavior.
    """
    if horizon<2:
        raise ValueError("horizon must be at least two")

    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )
    sources=load_allowed_transfer_sources(root)
    policy=NumericalPolicy()

    all_rows=[]
    domain_summaries=[]
    state_summaries=[]

    for source in sources:
        domain_rows=[]
        domain_states=[]
        states=source.states
        if limit_per_carrier is not None:
            if limit_per_carrier<1:
                raise ValueError("limit_per_carrier must be positive")
            states=states[:limit_per_carrier]
        for i,state in enumerate(states):
            rows,summary=_analyze_one_state(
                state,
                carrier_id=source.carrier_id,
                index=i,
                horizon=horizon,
                tau=tau,
                policy=policy,
            )
            domain_rows.extend(rows)
            domain_states.append(summary)
        all_rows.extend(domain_rows)
        state_summaries.extend(domain_states)
        domain_summaries.append(
            _domain_summary(
                source.carrier_id,
                domain_states,
                domain_rows,
            )
        )

    corridors=_normalization_corridors(
        domain_summaries
    )

    pooled_parent=[
        r["parent_y_density"]
        for r in all_rows if r["success"]
    ]
    pooled_successor=[
        r["successor_y_density"]
        for r in all_rows if r["success"]
    ]
    pooled_exp,pooled_intercept,pooled_pairs=_fit_loglog(
        pooled_parent,
        pooled_successor,
    )

    decay_by_depth={}
    for depth in sorted(set(r["depth"] for r in all_rows)):
        depth_rows=[
            r for r in all_rows
            if r["depth"]==depth and r["success"]
        ]
        dexp,dint,dpairs=_fit_loglog(
            [r["parent_y_density"] for r in depth_rows],
            [r["successor_y_density"] for r in depth_rows],
        )
        decay_by_depth[str(depth)]={
            "exponent":dexp,
            "intercept":dint,
            "pairs":dpairs,
        }

    degenerate_normalizations=[]
    for metric in FORMATION_NORMALIZATIONS:
        all_zero_spread=all(
            (
                s.first_step_normalizations[metric]["max"] is not None
                and s.first_step_normalizations[metric]["min"] is not None
                and abs(
                    s.first_step_normalizations[metric]["max"]
                    -s.first_step_normalizations[metric]["min"]
                )<=1e-12
            )
            for s in domain_summaries
        )
        if all_zero_spread:
            degenerate_normalizations.append(metric)

    scalar_probe=[
        {
            "y":10.0**(-k),
            "y_next":scalar_neutral_load_map(
                10.0**(-k)
            ),
            "ratio_to_2y2":(
                scalar_neutral_load_map(10.0**(-k))
                /(2.0*(10.0**(-k))**2)
            ),
        }
        for k in range(1,8)
    ]

    first_success=sum(
        s.first_step_successes
        for s in domain_summaries
    )
    total=sum(s.states for s in domain_summaries)

    terminal_counts=Counter(
        s["terminal_reason"]
        for s in state_summaries
        if s["terminal_reason"]
    )

    shared_candidates=[
        c["metric"]
        for c in corridors if c["shared"]
    ]

    tolerance_sensitivity=(
        run_tolerance_sensitivity(
            root,
            scales=(0.1,1.0,10.0),
            horizon=max(horizon,8),
            tau=tau,
            limit_per_carrier=limit_per_carrier,
        )
        if compute_tolerance_sensitivity
        else None
    )

    return {
        "status":
            "DEVELOPMENT_ONLY_FORMATION_TERMINATION_ANALYSIS",
        "source_fingerprint":source_tree_fingerprint(),
        "heldout_metrics_evaluated":False,
        "horizon":horizon,
        "tau":tau,
        "limit_per_carrier":limit_per_carrier,
        "states_total":total,
        "first_step_successes":first_success,
        "first_step_success_fraction":
            first_success/max(total,1),
        "formation_normalization_candidates":
            list(FORMATION_NORMALIZATIONS),
        "formation_normalization_corridors":
            corridors,
        "shared_formation_normalizations":
            shared_candidates,
        "degenerate_formation_normalizations":
            degenerate_normalizations,
        "shared_nontrivial_formation_normalizations":[
            m for m in shared_candidates
            if m not in degenerate_normalizations
        ],
        "domains":[
            s.to_dict() for s in domain_summaries
        ],
        "pooled_loglog_y_decay_exponent":pooled_exp,
        "pooled_loglog_y_decay_intercept":pooled_intercept,
        "pooled_y_decay_pairs":pooled_pairs,
        "loglog_y_decay_by_depth":decay_by_depth,
        "terminal_reason_counts":
            dict(sorted(terminal_counts.items())),
        "tolerance_sensitivity":tolerance_sensitivity,
        "scalar_exact_recurrence":{
            "formula":
                "2*y^2/((1+y)^2*(1+y^2))",
            "small_y_asymptotic":"2*y^2",
            "probe":scalar_probe,
        },
        "transition_rows":all_rows,
        "state_summaries":state_summaries,
        "interpretation_guard":{
            "normalization_selected_posthoc":False,
            "heldout_used":False,
            "note":(
                "All listed normalization candidates are reported. "
                "A shared corridor is descriptive development evidence, "
                "not a reason to discard candidates that do not overlap."
            ),
        },
    }


def write_formation_termination_report(
    result:dict[str,Any],
    outdir:str|Path,
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"formation_termination_analysis.json"
    json_path.write_text(
        json.dumps(result,indent=2),
        encoding="utf-8",
    )

    rows=result["transition_rows"]
    csv_path=outdir/"formation_termination_transitions.csv"
    if rows:
        fields=sorted({
            k for row in rows for k in row
        })
        with csv_path.open(
            "w",newline="",encoding="utf-8"
        ) as f:
            writer=csv.DictWriter(
                f,fieldnames=fields,
                extrasaction="ignore",
            )
            writer.writeheader()
            writer.writerows(rows)

    md_path=outdir/"FORMATION_TERMINATION_ANALYSIS.md"
    lines=[
        "# Formation Geometry → Dual-Load Decay → Termination Surface",
        "",
        "**Development/calibration data only. No held-out target is opened.**",
        "",
        f"States: `{result['states_total']}`",
        "",
        f"First-step master success: "
        f"`{result['first_step_successes']}/{result['states_total']}`",
        "",
        "## Formation-depth normalization candidates",
        "",
        "| Candidate | Shared q10-q90 corridor | Lower | Upper | Overlap ratio |",
        "|---|---:|---:|---:|---:|",
    ]
    for c in result["formation_normalization_corridors"]:
        lo="" if c["lower"] is None else f"{c['lower']:.6g}"
        hi="" if c["upper"] is None else f"{c['upper']:.6g}"
        ov=(
            ""
            if c["overlap_ratio"] is None
            else f"{c['overlap_ratio']:.4f}"
        )
        lines.append(
            f"| {c['metric']} | {c['shared']} | "
            f"{lo} | {hi} | {ov} |"
        )

    lines += [
        "",
        "All candidates are retained; none is selected merely because it overlaps.",
        "",
        "A zero-spread normalization is flagged as degenerate rather than counted as "
        "independent invariant evidence.",
        "",
        f"Degenerate candidates: `{', '.join(result['degenerate_formation_normalizations']) or 'none'}`",
        "",
        f"Shared nontrivial candidates: "
        f"`{', '.join(result['shared_nontrivial_formation_normalizations']) or 'none'}`",
        "",
        "## Neutral-load contraction",
        "",
        f"Pooled log-log fit:",
        "",
        r"\[",
        r"\log_{10} y_+ = a+p\log_{10} y,",
        r"\]",
        "",
        f"with `p = {result['pooled_loglog_y_decay_exponent']:.6f}` "
        f"over `{result['pooled_y_decay_pairs']}` successful transitions.",
        "",
        "Depth-specific fitted exponents:",
        "",
    ]
    for depth,row in result["loglog_y_decay_by_depth"].items():
        if row["exponent"] is not None:
            lines.append(
                f"- depth {depth}: `p={row['exponent']:.6f}` "
                f"over `{row['pairs']}` transitions"
            )
    lines += [
        "",
        "The exact scalar recurrence is",
        "",
        r"\[",
        r"y_+ = \frac{2y^2}{(1+y)^2(1+y^2)},",
        r"\]",
        "",
        "so for small load",
        "",
        r"\[",
        r"y_+\sim2y^2.",
        r"\]",
        "",
        "## Domain summaries",
        "",
    ]
    for d in result["domains"]:
        lines += [
            f"### {d['carrier_id']}",
            "",
            f"- states: `{d['states']}`",
            f"- maximum successful depth: `{d['max_successful_depth']}`",
            f"- median successful depth: `{d['median_successful_depth']:.3f}`",
            f"- fitted Y-decay exponent: "
            f"`{d['loglog_y_decay_exponent']:.6f}`",
            "",
            "Median log10 dual-load margin over the numerical gate:",
            "",
        ]
        for depth,value in d[
            "median_log10_dual_margin_by_depth"
        ].items():
            lines.append(
                f"- depth {depth}: `{value:.6f}`"
            )
        lines += [
            "",
            "Terminal reasons:",
            "",
        ]
        for reason,count in d[
            "terminal_reason_counts"
        ].items():
            lines.append(f"- `{reason}`: {count}")
        lines.append("")

    lines += [
        "## Tolerance sensitivity",
        "",
        "Only `atol` and `psd_tol` are scaled; spectral/rank/gap tolerances stay fixed.",
        "",
        "| Scale | Median successful depth | q10 | q90 | Max depth |",
        "|---:|---:|---:|---:|---:|",
    ]
    for row in result["tolerance_sensitivity"]["results"]:
        lines.append(
            f"| {row['scale']:.3g} | "
            f"{row['median_successful_depth']:.3f} | "
            f"{row['q10_successful_depth']:.3f} | "
            f"{row['q90_successful_depth']:.3f} | "
            f"{row['max_successful_depth']} |"
        )
    lines += [
        "",
        "If the terminal depth shifts when only the numerical floors move, the "
        "location of `bottom` is partly numerical even when the underlying load "
        "contraction is structural.",
        "",
    ]

    lines += [
        "## Interpretation",
        "",
        "The analysis separates two questions:",
        "",
        "1. whether a different dimensionless formation-depth coordinate has a "
        "three-domain corridor;",
        "2. whether repeated closure contracts the neutral/dual load toward the "
        "terminal surface.",
        "",
        "The exact scalar map already exhibits quadratic small-load contraction. "
        "The real-carrier log-log exponent tests whether the multidimensional "
        "master transport shows a related contraction regime.",
        "",
        "A numerical bottom caused by the declared tolerance is reported as such. "
        "It is not silently reinterpreted as an exact mathematical extinction.",
    ]
    md_path.write_text(
        "\n".join(lines)+"\n",
        encoding="utf-8",
    )

    # Plot 1: q10-q90 corridors for each normalization, by domain.
    plot_corr=outdir/"formation_normalization_intervals.png"
    fig,ax=plt.subplots(figsize=(9.2,5.2))
    x=np.arange(len(FORMATION_NORMALIZATIONS),dtype=float)
    offsets=np.linspace(-0.22,0.22,len(result["domains"]))
    for offset,domain in zip(offsets,result["domains"]):
        med=[]
        lo=[]
        hi=[]
        for metric in FORMATION_NORMALIZATIONS:
            q=domain["first_step_normalizations"][metric]
            med.append(q["median"])
            lo.append(q["median"]-q["q10"])
            hi.append(q["q90"]-q["median"])
        ax.errorbar(
            x+offset,
            med,
            yerr=np.vstack([lo,hi]),
            fmt="o",
            capsize=3,
            label=domain["carrier_id"],
        )
    ax.set_xticks(
        x,
        FORMATION_NORMALIZATIONS,
        rotation=25,
        ha="right",
    )
    ax.set_ylabel("dimensionless formation coordinate")
    ax.set_title("First-step formation-depth q10–q90 intervals")
    ax.legend()
    fig.tight_layout()
    fig.savefig(plot_corr,dpi=170)
    plt.close(fig)

    # Plot 2: pooled Y -> Y+ successful transitions in log-log space.
    plot_decay=outdir/"neutral_load_decay.png"
    xx=np.asarray([
        r["parent_y_density"]
        for r in rows
        if r["success"]
        and r["parent_y_density"]>0
        and r["successor_y_density"]>0
    ])
    yy=np.asarray([
        r["successor_y_density"]
        for r in rows
        if r["success"]
        and r["parent_y_density"]>0
        and r["successor_y_density"]>0
    ])
    fig,ax=plt.subplots(figsize=(6.4,5.2))
    ax.scatter(xx,yy,s=8,alpha=.35)
    if xx.size:
        lo=float(np.min(xx))
        hi=float(np.max(xx))
        grid=np.geomspace(lo,hi,200)
        p=result["pooled_loglog_y_decay_exponent"]
        a=result["pooled_loglog_y_decay_intercept"]
        fit=10.0**a * grid**p
        ax.plot(grid,fit,label=f"log-log fit p={p:.3f}")
        ax.plot(
            grid,
            2.0*grid*grid,
            linestyle="--",
            label="2 y² reference",
        )
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("parent neutral-load density")
    ax.set_ylabel("successor neutral-load density")
    ax.set_title("Neutral-load contraction across master reclosures")
    ax.legend()
    fig.tight_layout()
    fig.savefig(plot_decay,dpi=170)
    plt.close(fig)

    # Plot 3: median dual-load margin by depth and domain.
    plot_margin=outdir/"dual_load_margin_by_depth.png"
    fig,ax=plt.subplots(figsize=(7.4,4.8))
    for domain in result["domains"]:
        items=sorted(
            (
                (int(k),float(v))
                for k,v in domain[
                    "median_log10_dual_margin_by_depth"
                ].items()
            )
        )
        if items:
            ax.plot(
                [k for k,_ in items],
                [v for _,v in items],
                marker="o",
                label=domain["carrier_id"],
            )
    ax.axhline(0.0,linestyle="--")
    ax.set_xlabel("recursive depth")
    ax.set_ylabel("median log10(min dual load / atol)")
    ax.set_title("Approach to the dual-load terminal surface")
    ax.legend()
    fig.tight_layout()
    fig.savefig(plot_margin,dpi=170)
    plt.close(fig)


    # Plot 4: tolerance scale vs successful depth.
    plot_tolerance=outdir/"termination_tolerance_sensitivity.png"
    sens=result["tolerance_sensitivity"]["results"]
    scales=np.asarray([r["scale"] for r in sens],dtype=float)
    med=np.asarray([
        r["median_successful_depth"] for r in sens
    ],dtype=float)
    q10=np.asarray([
        r["q10_successful_depth"] for r in sens
    ],dtype=float)
    q90=np.asarray([
        r["q90_successful_depth"] for r in sens
    ],dtype=float)
    fig,ax=plt.subplots(figsize=(6.6,4.6))
    ax.errorbar(
        scales,
        med,
        yerr=np.vstack([med-q10,q90-med]),
        marker="o",
        capsize=4,
    )
    ax.set_xscale("log")
    ax.set_xlabel("scale applied to atol and psd_tol")
    ax.set_ylabel("successful master-reclosure depth")
    ax.set_title("Terminal-depth sensitivity to numerical admissibility floors")
    fig.tight_layout()
    fig.savefig(plot_tolerance,dpi=170)
    plt.close(fig)

    return {
        "json":str(json_path),
        "csv":str(csv_path),
        "markdown":str(md_path),
        "formation_plot":str(plot_corr),
        "decay_plot":str(plot_decay),
        "margin_plot":str(plot_margin),
        "tolerance_plot":str(plot_tolerance),
    }
