from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import csv
import json
import math

import numpy as np
import matplotlib.pyplot as plt

from .types import NumericalPolicy
from .linalg import hermitize
from .finite_closure import bfg_state_to_reduced
from .formation_robustness import (
    active_packet_formation_operator,
    formation_margin,
)
from .runtime_transfer import load_allowed_transfer_sources
from .network_carrier import KarateInteractionCarrier
from .session import source_tree_fingerprint


@dataclass(frozen=True)
class RuntimeRankTransitionCertificate:
    kind: str
    rank: int
    ambient_dimension: int
    threshold: float
    lower_clearance: float
    upper_clearance: float
    certified_operator_radius: float
    lower_surface: str
    upper_surface: str
    normality_required: bool
    normality_residual: float | None = None
    runtime_consistency: bool | None = None

    def to_dict(self) -> dict[str,Any]:
        return asdict(self)


@dataclass(frozen=True)
class FormationBifurcationLedger:
    carrier_id: str
    state_index: int
    formation_eligible: bool
    formation_sign_clearance: float
    formation_simplicity_clearance: float
    formation_operator_margin: float
    persistent_rank: int
    persistent_runtime_radius: float
    active_rank: int
    active_runtime_radius: float
    active_threshold: float
    persistent_threshold: float
    exact_rank_nonopen: bool

    def to_dict(self) -> dict[str,Any]:
        return asdict(self)


def persistent_runtime_rank_certificate(
    R:np.ndarray,
    policy:NumericalPolicy|None=None,
    *,
    normality_tol:float=1e-8,
) -> RuntimeRankTransitionCertificate:
    """
    Runtime persistent-rank certificate inside the normal-contraction category.

    The finite runtime declares an eigenvalue persistent when

        ||lambda|-1| <= peripheral_tol.

    For a normal contraction, eigenvalue moduli equal singular values and all
    moduli are <=1. Hence the runtime persistent count equals the number of
    singular values above

        tau_P = 1-peripheral_tol.

    Weyl's singular-value inequality then implies that a perturbation E with

        ||E||_2 < min(
            sigma_p(R)-tau_P,
            tau_P-sigma_{p+1}(R)
        )

    preserves the runtime persistent count, provided both the original and
    perturbed operators remain normal contractions.

    This is an operational finite-runtime statement. Exact unit-circle
    persistence (zero tolerance) remains non-open in ambient matrix space.
    """
    policy=policy or NumericalPolicy()
    R=np.asarray(R,dtype=complex)
    if R.ndim!=2 or R.shape[0]!=R.shape[1]:
        raise ValueError("R must be square")

    normality=float(
        np.linalg.norm(
            R.conj().T@R-R@R.conj().T,
            2,
        )
    )
    if normality>normality_tol:
        raise ValueError(
            "persistent runtime rank certificate requires normal R"
        )
    if float(np.linalg.norm(R,2))>1.0+normality_tol:
        raise ValueError(
            "persistent runtime rank certificate requires contraction R"
        )

    singular=np.sort(
        np.linalg.svd(R,compute_uv=False)
    )[::-1]
    threshold=1.0-float(policy.peripheral_tol)
    p=int(np.sum(singular>=threshold))

    lower=(
        float(singular[p-1]-threshold)
        if p>0 else float("inf")
    )
    upper=(
        float(threshold-singular[p])
        if p<len(singular) else float("inf")
    )
    radius=max(
        0.0,
        float(min(lower,upper)),
    )

    eig=np.linalg.eigvals(R)
    runtime_count=int(np.sum(
        np.abs(np.abs(eig)-1.0)<=policy.peripheral_tol
    ))

    return RuntimeRankTransitionCertificate(
        kind="persistent_runtime_rank",
        rank=p,
        ambient_dimension=int(R.shape[0]),
        threshold=threshold,
        lower_clearance=lower,
        upper_clearance=upper,
        certified_operator_radius=radius,
        lower_surface="persistent singular value crosses below 1-peripheral_tol",
        upper_surface="stable singular value crosses above 1-peripheral_tol",
        normality_required=True,
        normality_residual=normality,
        runtime_consistency=bool(runtime_count==p),
    )


def active_runtime_rank_certificate(
    A:np.ndarray,
    policy:NumericalPolicy|None=None,
) -> RuntimeRankTransitionCertificate:
    """
    Certified local radius for the numerical active-rank decision.

    The runtime threshold is

        tau_A(A)=max(rank_tol, rtol*sigma_1(A)).

    Singular values are 1-Lipschitz in operator norm, while tau_A is
    rtol-Lipschitz. Therefore, if

        ||Delta A||_2
        <
        min(
            sigma_r-tau_A,
            tau_A-sigma_{r+1}
        )/(1+rtol),

    the runtime active rank cannot change.

    This is a sufficient radius. It becomes nearly exact when the absolute
    rank_tol branch dominates, as it does for many current carrier states.
    Exact algebraic rank is still non-open upward from a rank-deficient matrix.
    """
    policy=policy or NumericalPolicy()
    A=np.asarray(A,dtype=complex)
    if A.ndim!=2:
        raise ValueError("A must be a matrix")

    singular=np.sort(
        np.linalg.svd(A,compute_uv=False)
    )[::-1]
    if singular.size==0:
        return RuntimeRankTransitionCertificate(
            kind="active_runtime_rank",
            rank=0,
            ambient_dimension=0,
            threshold=float(policy.rank_tol),
            lower_clearance=float("inf"),
            upper_clearance=float(policy.rank_tol),
            certified_operator_radius=float(
                policy.rank_tol/(1.0+policy.rtol)
            ),
            lower_surface="active singular value crosses below threshold",
            upper_surface="latent singular value crosses above threshold",
            normality_required=False,
        )

    threshold=max(
        float(policy.rank_tol),
        float(policy.rtol)*float(singular[0]),
    )
    r=int(np.sum(singular>threshold))
    lower=(
        float(singular[r-1]-threshold)
        if r>0 else float("inf")
    )
    upper=(
        float(threshold-singular[r])
        if r<len(singular) else float("inf")
    )
    raw=max(0.0,float(min(lower,upper)))
    radius=raw/(1.0+float(policy.rtol))

    return RuntimeRankTransitionCertificate(
        kind="active_runtime_rank",
        rank=r,
        ambient_dimension=int(min(A.shape)),
        threshold=threshold,
        lower_clearance=lower,
        upper_clearance=upper,
        certified_operator_radius=radius,
        lower_surface="active singular value crosses below runtime threshold",
        upper_surface="latent singular value crosses above runtime threshold",
        normality_required=False,
    )


def state_bifurcation_ledger(
    state,
    *,
    carrier_id:str,
    state_index:int,
    policy:NumericalPolicy|None=None,
) -> FormationBifurcationLedger:
    policy=policy or NumericalPolicy()
    A,Kplus=active_packet_formation_operator(state,policy)
    f=formation_margin(Kplus,policy)
    p=persistent_runtime_rank_certificate(
        np.asarray(state.R,dtype=complex),
        policy,
    )
    a=active_runtime_rank_certificate(A,policy)

    return FormationBifurcationLedger(
        carrier_id=carrier_id,
        state_index=int(state_index),
        formation_eligible=bool(f.eligible),
        formation_sign_clearance=float(f.sign_clearance),
        formation_simplicity_clearance=float(
            f.simplicity_clearance
        ),
        formation_operator_margin=float(
            f.absolute_boundary_distance
        ),
        persistent_rank=int(p.rank),
        persistent_runtime_radius=float(
            p.certified_operator_radius
        ),
        active_rank=int(a.rank),
        active_runtime_radius=float(
            a.certified_operator_radius
        ),
        active_threshold=float(a.threshold),
        persistent_threshold=float(p.threshold),
        exact_rank_nonopen=True,
    )


def _qstats(values:list[float]) -> dict[str,float|None]:
    x=np.asarray(
        [float(v) for v in values if np.isfinite(v)],
        dtype=float,
    )
    if x.size==0:
        return {
            "q10":None,"median":None,"q90":None,
            "min":None,"max":None,"mean":None,
        }
    q=np.quantile(x,[.10,.50,.90])
    return {
        "q10":float(q[0]),
        "median":float(q[1]),
        "q90":float(q[2]),
        "min":float(np.min(x)),
        "max":float(np.max(x)),
        "mean":float(np.mean(x)),
    }


def run_stratum_transition_audit(
    project_root:str|Path|None=None,
    *,
    limit_per_timeseries_carrier:int|None=None,
    include_full_network:bool=True,
) -> dict[str,Any]:
    """
    Audit the four finite-runtime bifurcation families:

      1. formation sign,
      2. formation simplicity,
      3. persistent runtime rank,
      4. active runtime rank.

    No held-out target metric is loaded.
    """
    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )
    policy=NumericalPolicy()
    sources=list(load_allowed_transfer_sources(root))
    source_rows=[]
    for source in sources:
        states=source.states
        if limit_per_timeseries_carrier is not None:
            if limit_per_timeseries_carrier<1:
                raise ValueError(
                    "limit_per_timeseries_carrier must be positive"
                )
            states=states[:limit_per_timeseries_carrier]
        source_rows.append((source.carrier_id,states))

    if include_full_network:
        carrier=KarateInteractionCarrier()
        source_rows.append((
            "zachary-karate-network",
            tuple(
                carrier.map_measurement_to_state(m,generation=i)
                for i,m in enumerate(carrier.measurements())
            ),
        ))

    rows=[]
    domains=[]
    for carrier_id,states in source_rows:
        drows=[]
        for i,bfg in enumerate(states):
            reduced=bfg_state_to_reduced(bfg)
            ledger=state_bifurcation_ledger(
                reduced,
                carrier_id=carrier_id,
                state_index=i,
                policy=policy,
            )
            row=ledger.to_dict()
            rows.append(row)
            drows.append(row)

        domains.append({
            "carrier_id":carrier_id,
            "states":len(drows),
            "formation_eligible":sum(
                int(r["formation_eligible"])
                for r in drows
            ),
            "persistent_ranks":sorted(set(
                int(r["persistent_rank"]) for r in drows
            )),
            "active_ranks":sorted(set(
                int(r["active_rank"]) for r in drows
            )),
            "formation_operator_margin":_qstats([
                r["formation_operator_margin"]
                for r in drows
            ]),
            "persistent_runtime_radius":_qstats([
                r["persistent_runtime_radius"]
                for r in drows
            ]),
            "active_runtime_radius":_qstats([
                r["active_runtime_radius"]
                for r in drows
            ]),
        })

    active_upward_bottleneck=0
    persistent_loss_bottleneck=0
    for carrier_id,states in source_rows:
        for bfg in states:
            reduced=bfg_state_to_reduced(bfg)
            A,_=active_packet_formation_operator(
                reduced,policy
            )
            ac=active_runtime_rank_certificate(A,policy)
            pc=persistent_runtime_rank_certificate(
                np.asarray(reduced.R),policy
            )
            if ac.upper_clearance<=ac.lower_clearance:
                active_upward_bottleneck+=1
            if pc.lower_clearance<=pc.upper_clearance:
                persistent_loss_bottleneck+=1

    return {
        "status":"STRATUM_TRANSITION_GEOMETRY_AUDIT",
        "source_fingerprint":source_tree_fingerprint(),
        "heldout_metrics_evaluated":False,
        "states_total":len(rows),
        "surfaces":{
            "formation_sign":
                "lambda0(K_+) = -atol",
            "formation_simplicity":
                "lambda1(K_+)-lambda0(K_+) = simple_gap_tol",
            "persistent_runtime_rank":
                "singular value of normal contraction R = 1-peripheral_tol",
            "active_runtime_rank":
                "singular value of packet A = max(rank_tol,rtol*sigma1(A))",
        },
        "exact_nonopenness":{
            "active_algebraic_rank":True,
            "exact_unit_circle_persistence":True,
            "consequence":(
                "positive rank-transition radii are operational runtime-stratum "
                "radii induced by declared numerical thresholds, not positive "
                "ambient radii for exact algebraic rank/persistence"
            ),
        },
        "active_upward_bottleneck_states":
            active_upward_bottleneck,
        "persistent_loss_bottleneck_states":
            persistent_loss_bottleneck,
        "domains":domains,
        "rows":rows,
        "interpretation_guard":{
            "unified_scalar_margin_claimed":False,
            "reason":(
                "formation, persistent-rank and active-rank surfaces live in "
                "different native operator coordinates. They are kept as a "
                "ledger until transported into a common parent-state norm."
            ),
        },
    }


def write_stratum_transition_report(
    result:dict[str,Any],
    outdir:str|Path,
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"stratum_transition_geometry.json"
    json_path.write_text(
        json.dumps(result,indent=2),
        encoding="utf-8",
    )

    csv_path=outdir/"stratum_transition_rows.csv"
    rows=result["rows"]
    if rows:
        fields=sorted({k for r in rows for k in r})
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(
                f,fieldnames=fields,extrasaction="ignore"
            )
            w.writeheader()
            w.writerows(rows)

    md_path=outdir/"STRATUM_TRANSITION_GEOMETRY.md"
    lines=[
        "# BFG Stratum Transition Geometry",
        "",
        "**No held-out target is opened.**",
        "",
        "The finite runtime now records four separate bifurcation families:",
        "",
        "1. formation-sign surface;",
        "2. formation-simplicity surface;",
        "3. persistent-runtime-rank surface;",
        "4. active-runtime-rank surface.",
        "",
        "The two rank surfaces are operational runtime surfaces. Exact algebraic "
        "rank and exact unit-circle persistence remain non-open under arbitrary "
        "ambient perturbations.",
        "",
        f"States audited: `{result['states_total']}`",
        "",
        f"States whose nearest active-rank transition is upward activation: "
        f"`{result['active_upward_bottleneck_states']}/{result['states_total']}`",
        "",
        f"States whose nearest persistent-rank transition is loss of persistence: "
        f"`{result['persistent_loss_bottleneck_states']}/{result['states_total']}`",
        "",
        "| Carrier | Formation eligible | Persistent rank | Active rank | Median formation margin | Median persistent runtime radius | Median active runtime radius |",
        "|---|---:|---|---|---:|---:|---:|",
    ]
    for d in result["domains"]:
        fm=d["formation_operator_margin"]["median"]
        pr=d["persistent_runtime_radius"]["median"]
        ar=d["active_runtime_radius"]["median"]
        lines.append(
            f"| {d['carrier_id']} | {d['formation_eligible']}/{d['states']} | "
            f"{d['persistent_ranks']} | {d['active_ranks']} | "
            f"{format(fm,'.6g')} | {format(pr,'.6g')} | {format(ar,'.6g')} |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "The active-rank runtime surface is currently extremely close in packet "
        "operator norm because the latent singular values sit near zero while the "
        "declared rank threshold is around `1e-10`.",
        "",
        "This is a numerical/runtime geometry fact, not evidence for a physical "
        "critical scale.",
        "",
        "The next integration step is to transport the persistent- and active-rank "
        "radii into the parent product norm so all four surfaces can be compared "
        "inside one common continuity corridor.",
    ]
    md_path.write_text(
        "\n".join(lines)+"\n",
        encoding="utf-8",
    )

    # Log-scale comparison of the three native positive distances.
    plot_path=outdir/"native_bifurcation_margins.png"
    labels=[]
    formation=[]
    persistent=[]
    active=[]
    for d in result["domains"]:
        labels.append(d["carrier_id"])
        formation.append(
            d["formation_operator_margin"]["median"]
        )
        persistent.append(
            d["persistent_runtime_radius"]["median"]
        )
        active.append(
            d["active_runtime_radius"]["median"]
        )

    x=np.arange(len(labels),dtype=float)
    width=0.24
    fig,ax=plt.subplots(figsize=(10.0,5.2))
    ax.bar(x-width,formation,width,label="formation K+")
    ax.bar(x,persistent,width,label="persistent R")
    ax.bar(x+width,active,width,label="active packet A")
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(labels,rotation=15,ha="right")
    ax.set_ylabel("native operator-norm margin (log scale)")
    ax.set_title("BFG bifurcation ledger: native-coordinate medians")
    ax.legend()
    fig.tight_layout()
    fig.savefig(plot_path,dpi=170)
    plt.close(fig)

    return {
        "json":str(json_path),
        "csv":str(csv_path),
        "markdown":str(md_path),
        "plot":str(plot_path),
    }
