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
from .linalg import hermitize, blockdiag2
from .core import (
    neutral_pair,
    graph_metric,
    persistent_basis,
    graph_projector,
)
from .finite_closure import bfg_state_to_reduced
from .runtime_transfer import load_allowed_transfer_sources
from .network_carrier import KarateInteractionCarrier
from .session import source_tree_fingerprint


@dataclass(frozen=True)
class FormationMarginCertificate:
    eligible: bool
    lowest_eigenvalue: float
    ground_gap: float
    sign_clearance: float
    simplicity_clearance: float
    signed_margin: float
    absolute_boundary_distance: float
    limiting_surface: str
    sign_threshold: float
    simplicity_threshold: float

    def to_dict(self) -> dict[str,Any]:
        return asdict(self)


def formation_margin_from_spectrum(
    lowest_eigenvalue:float,
    ground_gap:float,
    policy:NumericalPolicy|None=None,
) -> FormationMarginCertificate:
    """
    Exact operator-norm distance to the finite formation bifurcation surface.

    The gate is

        lambda_0 < -eps_sign
        gap=lambda_1-lambda_0 > eps_gap.

    Put

        s = -eps_sign - lambda_0
        g = gap - eps_gap.

    For an eligible Hermitian operator the distance to the complement is

        min(s, g/2).

    For an ineligible operator the infimum distance to the eligible set is

        max((-s)_+, (-g)_+/2).

    These are exact in Hermitian operator norm by Weyl's inequalities and
    matching diagonal perturbations in the lowest eigenspaces.
    """
    policy=policy or NumericalPolicy()
    lam=float(lowest_eigenvalue)
    gap=float(ground_gap)

    if not np.isfinite(lam):
        raise ValueError("lowest eigenvalue must be finite")
    if not (np.isfinite(gap) or math.isinf(gap)):
        raise ValueError("ground gap must be finite or +inf")
    if gap<0:
        raise ValueError("ground gap must be nonnegative")

    eps_sign=float(policy.atol)
    eps_gap=float(policy.simple_gap_tol)

    s=-eps_sign-lam
    g=gap-eps_gap
    eligible=bool(s>0 and g>0)

    if eligible:
        sign_distance=s
        gap_distance=(g/2.0 if np.isfinite(g) else float("inf"))
        radius=min(sign_distance,gap_distance)
        limiting=(
            "sign"
            if sign_distance<=gap_distance
            else "simplicity"
        )
        signed=float(radius)
    else:
        sign_violation=max(0.0,-s)
        gap_violation=(
            max(0.0,-g)/2.0
            if np.isfinite(g)
            else 0.0
        )
        radius=max(sign_violation,gap_violation)
        if sign_violation>=gap_violation and sign_violation>0:
            limiting="sign"
        elif gap_violation>0:
            limiting="simplicity"
        else:
            limiting="boundary"
        signed=-float(radius)

    return FormationMarginCertificate(
        eligible=eligible,
        lowest_eigenvalue=lam,
        ground_gap=gap,
        sign_clearance=float(s),
        simplicity_clearance=float(g),
        signed_margin=float(signed),
        absolute_boundary_distance=float(radius),
        limiting_surface=limiting,
        sign_threshold=-eps_sign,
        simplicity_threshold=eps_gap,
    )


def formation_margin(
    K_active:np.ndarray,
    policy:NumericalPolicy|None=None,
) -> FormationMarginCertificate:
    policy=policy or NumericalPolicy()
    K=hermitize(np.asarray(K_active,dtype=complex))
    if K.ndim!=2 or K.shape[0]!=K.shape[1] or K.shape[0]==0:
        raise ValueError("K_active must be nonempty square")
    vals=np.sort(np.linalg.eigvalsh(K).real)
    lam=float(vals[0])
    gap=(
        float("inf")
        if len(vals)==1
        else float(vals[1]-vals[0])
    )
    return formation_margin_from_spectrum(
        lam,gap,policy
    )


def active_packet_formation_operator(
    state,
    policy:NumericalPolicy|None=None,
) -> tuple[np.ndarray,np.ndarray]:
    """
    Reconstruct (A,K_+) from a nonterminal reduced state before successor
    commitment.
    """
    policy=policy or NumericalPolicy()
    if state.bottom:
        raise ValueError("bottom has no active formation operator")

    K=hermitize(np.asarray(state.K,dtype=complex))
    Y=hermitize(np.asarray(state.Y,dtype=complex))
    R=np.asarray(state.R,dtype=complex)
    rho=hermitize(np.asarray(state.rho,dtype=complex))

    C,B=neutral_pair(Y)
    G=graph_metric(Y)
    W,_=persistent_basis(R,G,policy)
    if W.shape[1]==0:
        raise ValueError("no persistent peripheral sector")
    P=graph_projector(W,G)

    keep=P@C
    up=P@B
    lk=float(np.real(np.trace(
        G@keep@rho@keep.conj().T
    )))
    lu=float(np.real(np.trace(
        G@up@rho@up.conj().T
    )))
    if lk<=policy.atol or lu<=policy.atol:
        raise ValueError(
            "dual persistent load below admissibility threshold"
        )

    alpha=lu/(lk+lu)
    beta=lk/(lk+lu)
    A=np.vstack([
        np.sqrt(alpha)*(P@C),
        np.sqrt(beta)*(P@B),
    ])

    U,s,_=np.linalg.svd(A,full_matrices=False)
    if s.size==0:
        raise ValueError("polar active support is empty")
    threshold=max(
        policy.rank_tol,
        policy.rtol*float(s[0]),
    )
    r=int(np.sum(s>threshold))
    if r==0:
        raise ValueError("polar active support is empty")

    Ur=U[:,:r]
    Kplus=hermitize(
        Ur.conj().T@blockdiag2(K)@Ur
    )
    return A,Kplus


def _classify_active(
    K:np.ndarray,
    policy:NumericalPolicy,
) -> bool:
    return formation_margin(K,policy).eligible


def _adversarial_direction(
    K:np.ndarray,
    cert:FormationMarginCertificate,
    *,
    toward_opposite_status:bool=True,
) -> np.ndarray:
    """
    Unit/operator-norm direction that reaches the nearest gate surface.

    Returned matrix has operator norm 1 when the boundary distance is positive.
    """
    K=hermitize(np.asarray(K,dtype=complex))
    vals,vecs=np.linalg.eigh(K)
    order=np.argsort(vals.real)
    vals=vals.real[order]
    vecs=vecs[:,order]
    v0=vecs[:,0:1]
    P0=v0@v0.conj().T

    if cert.eligible:
        if cert.limiting_surface=="sign":
            return P0
        if len(vals)<2:
            return P0
        v1=vecs[:,1:2]
        P1=v1@v1.conj().T
        # Raise lambda0 and lower lambda1 equally: gap decreases by 2t.
        return P0-P1

    # Move an ineligible operator toward eligibility.
    sign_violation=max(0.0,-cert.sign_clearance)
    gap_violation=max(0.0,-cert.simplicity_clearance)
    radius=cert.absolute_boundary_distance
    if radius<=0:
        return -P0

    # Lower lambda0 by radius. This repairs sign and also increases the gap.
    E=-P0

    if len(vals)>=2 and gap_violation>radius:
        # Cannot occur because radius >= gap_violation/2, but the amount still
        # needed on lambda1 after lowering lambda0 is (D-radius).
        v1=vecs[:,1:2]
        P1=v1@v1.conj().T
        need=max(0.0,gap_violation-radius)
        coeff=min(1.0,need/radius)
        E=E+coeff*P1
    return hermitize(E)


def boundary_crossing_control(
    K_active:np.ndarray,
    policy:NumericalPolicy|None=None,
    *,
    inside_factor:float=0.99,
    outside_factor:float=1.01,
) -> dict[str,Any]:
    """
    Numerically verify the exact margin with aligned perturbations.

    `inside_factor * radius` must preserve the status.
    `outside_factor * radius` is constructed to cross the nearest boundary.
    """
    policy=policy or NumericalPolicy()
    K=hermitize(np.asarray(K_active,dtype=complex))
    cert=formation_margin(K,policy)
    r=cert.absolute_boundary_distance

    if r<=100*np.finfo(float).eps:
        return {
            "testable":False,
            "reason":"state is numerically on the gate boundary",
            "certificate":cert.to_dict(),
        }

    D=_adversarial_direction(K,cert)
    dnorm=float(np.linalg.norm(D,2))
    if dnorm<=0:
        raise RuntimeError("adversarial direction vanished")
    D=D/dnorm

    before=cert.eligible
    inside_amount=inside_factor*r

    # A gap-limited eligible state has an extremely thin non-eligible band
    # around the degeneracy surface. A fixed 1% overshoot can pass through that
    # band and restore a positive reordered gap. Move only eps_gap/4 beyond the
    # exact boundary instead.
    if cert.eligible and cert.limiting_surface=="simplicity":
        outside_amount=r+0.25*float(policy.simple_gap_tol)
    else:
        outside_amount=outside_factor*r

    Kin=hermitize(K+inside_amount*D)
    Kout=hermitize(K+outside_amount*D)

    inside_status=_classify_active(Kin,policy)
    outside_status=_classify_active(Kout,policy)

    return {
        "testable":True,
        "radius":float(r),
        "inside_factor":float(inside_factor),
        "outside_factor":float(
            outside_amount/r if r>0 else float("nan")
        ),
        "inside_norm":float(np.linalg.norm(Kin-K,2)),
        "outside_norm":float(np.linalg.norm(Kout-K,2)),
        "original_status":before,
        "inside_status":inside_status,
        "outside_status":outside_status,
        "inside_preserved":bool(inside_status==before),
        "outside_crossed":bool(outside_status!=before),
        "certificate":cert.to_dict(),
    }


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


def run_formation_robustness_audit(
    project_root:str|Path|None=None,
    *,
    limit_per_timeseries_carrier:int|None=None,
    include_full_network:bool=True,
) -> dict[str,Any]:
    """
    First-step formation-margin and bifurcation audit.

    No target metric is loaded. The audit operates solely on the already
    declared carrier states and the master formation operator.
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
        network=KarateInteractionCarrier()
        source_rows.append((
            "zachary-karate-network",
            tuple(
                network.map_measurement_to_state(m,generation=i)
                for i,m in enumerate(network.measurements())
            ),
        ))

    rows=[]
    domains=[]
    for carrier_id,states in source_rows:
        drows=[]
        for i,bfg in enumerate(states):
            reduced=bfg_state_to_reduced(bfg)
            try:
                _,Kplus=active_packet_formation_operator(
                    reduced,policy
                )
            except ValueError as exc:
                row={
                    "carrier_id":carrier_id,
                    "state_index":i,
                    "gate_reached":False,
                    "reason":str(exc),
                }
                drows.append(row)
                rows.append(row)
                continue

            cert=formation_margin(Kplus,policy)
            control=boundary_crossing_control(
                Kplus,policy
            )
            row={
                "carrier_id":carrier_id,
                "state_index":i,
                "gate_reached":True,
                **cert.to_dict(),
                "inside_preserved":
                    control.get("inside_preserved"),
                "outside_crossed":
                    control.get("outside_crossed"),
                "inside_norm":
                    control.get("inside_norm"),
                "outside_norm":
                    control.get("outside_norm"),
                "reason":None,
            }
            drows.append(row)
            rows.append(row)

        reached=[
            r for r in drows
            if r.get("gate_reached")
        ]
        eligible=[
            r for r in reached if r["eligible"]
        ]
        terminal=[
            r for r in reached if not r["eligible"]
        ]
        controls=[
            r for r in reached
            if r.get("inside_preserved") is not None
        ]
        domains.append({
            "carrier_id":carrier_id,
            "states":len(states),
            "gate_reached":len(reached),
            "eligible":len(eligible),
            "terminal":len(terminal),
            "positive_margin":
                _qstats([
                    r["signed_margin"]
                    for r in eligible
                ]),
            "negative_margin":
                _qstats([
                    r["signed_margin"]
                    for r in terminal
                ]),
            "absolute_boundary_distance":
                _qstats([
                    r["absolute_boundary_distance"]
                    for r in reached
                ]),
            "limiting_surface_counts":{
                key:sum(
                    int(r["limiting_surface"]==key)
                    for r in reached
                )
                for key in ("sign","simplicity","boundary")
            },
            "inside_preserved":sum(
                int(r.get("inside_preserved") is True)
                for r in controls
            ),
            "outside_crossed":sum(
                int(r.get("outside_crossed") is True)
                for r in controls
            ),
            "boundary_controls":len(controls),
        })

    reached=[
        r for r in rows if r.get("gate_reached")
    ]
    controls=[
        r for r in reached
        if r.get("inside_preserved") is not None
    ]
    network_rows=[
        r for r in reached
        if r["carrier_id"]=="zachary-karate-network"
    ]
    network_success=[
        r for r in network_rows if r["eligible"]
    ]
    network_terminal=[
        r for r in network_rows if not r["eligible"]
    ]

    return {
        "status":"FORMATION_ROBUSTNESS_BIFURCATION_AUDIT",
        "source_fingerprint":source_tree_fingerprint(),
        "heldout_metrics_evaluated":False,
        "states_total":len(rows),
        "gate_states":len(reached),
        "theorem":{
            "gate_conditions":[
                "lambda0 < -eps_sign",
                "ground_gap > eps_simple",
            ],
            "eligible_distance":
                "min(-eps_sign-lambda0, (gap-eps_simple)/2)",
            "ineligible_distance":
                "max((lambda0+eps_sign)_+, (eps_simple-gap)_+/2)",
            "norm":"Hermitian operator 2-norm",
            "basis":"Weyl eigenvalue perturbation bounds with matching extremal eigenspace perturbations",
        },
        "boundary_controls":len(controls),
        "inside_preserved":sum(
            int(r.get("inside_preserved") is True)
            for r in controls
        ),
        "outside_crossed":sum(
            int(r.get("outside_crossed") is True)
            for r in controls
        ),
        "domains":domains,
        "network_bifurcation":{
            "eligible_count":len(network_success),
            "terminal_count":len(network_terminal),
            "nearest_eligible_margin":(
                min(r["signed_margin"] for r in network_success)
                if network_success else None
            ),
            "nearest_terminal_margin":(
                max(r["signed_margin"] for r in network_terminal)
                if network_terminal else None
            ),
            "eligible_margin_range":(
                [
                    min(r["signed_margin"] for r in network_success),
                    max(r["signed_margin"] for r in network_success),
                ]
                if network_success else None
            ),
            "terminal_margin_range":(
                [
                    min(r["signed_margin"] for r in network_terminal),
                    max(r["signed_margin"] for r in network_terminal),
                ]
                if network_terminal else None
            ),
            "sign_limited_states":sum(
                int(r["limiting_surface"]=="sign")
                for r in network_rows
            ),
            "simplicity_limited_states":sum(
                int(r["limiting_surface"]=="simplicity")
                for r in network_rows
            ),
        },
        "rows":rows,
        "interpretation_guard":{
            "exact_active_operator_distance":True,
            "parent_state_norm_radius_claimed":False,
            "empirical_universality_claimed":False,
            "note":(
                "The exact radius is in active K_+ operator norm. A separate "
                "parent-state perturbation theorem would additionally need "
                "control of the state-to-packet subspace map."
            ),
        },
    }


def write_formation_robustness_report(
    result:dict[str,Any],
    outdir:str|Path,
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"formation_robustness_audit.json"
    json_path.write_text(
        json.dumps(result,indent=2),
        encoding="utf-8",
    )

    csv_path=outdir/"formation_margin_rows.csv"
    if result["rows"]:
        fields=sorted({
            k for row in result["rows"] for k in row
        })
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            w=csv.DictWriter(
                f,fieldnames=fields,extrasaction="ignore"
            )
            w.writeheader()
            w.writerows(result["rows"])

    md_path=outdir/"FORMATION_ROBUSTNESS_AND_BIFURCATION.md"
    lines=[
        "# BFG Formation Robustness and Bifurcation Surface",
        "",
        "**No held-out target is opened.**",
        "",
        "The finite formation gate is",
        "",
        r"\[",
        r"\lambda_0<-\varepsilon_{\rm sign},",
        r"\qquad",
        r"\lambda_1-\lambda_0>\varepsilon_{\rm simple}.",
        r"\]",
        "",
        "Define",
        "",
        r"\[",
        r"s=-\varepsilon_{\rm sign}-\lambda_0,",
        r"\qquad",
        r"g=(\lambda_1-\lambda_0)-\varepsilon_{\rm simple}.",
        r"\]",
        "",
        "For an eligible active operator the exact operator-norm distance to loss "
        "of formation is",
        "",
        r"\[",
        r"\boxed{",
        r"r_+=\min\left(s,\frac{g}{2}\right).",
        r"}",
        r"\]",
        "",
        "For an ineligible operator the infimum distance to the eligible set is",
        "",
        r"\[",
        r"\boxed{",
        r"r_-=\max\left((-s)_+,\frac{(-g)_+}{2}\right).",
        r"}",
        r"\]",
        "",
        "The signed formation margin is `+r_+` for eligible states and `-r_-` "
        "for terminal states.",
        "",
        "These formulas are exact in Hermitian operator 2-norm by Weyl's "
        "inequalities, and the bounds are attained by perturbations aligned with "
        "the two lowest eigenspaces.",
        "",
        "## Audit",
        "",
        f"Gate states: `{result['gate_states']}`",
        "",
        f"Sub-boundary adversarial controls preserving status: "
        f"`{result['inside_preserved']}/{result['boundary_controls']}`",
        "",
        f"Just-beyond-boundary controls crossing status: "
        f"`{result['outside_crossed']}/{result['boundary_controls']}`",
        "",
        "| Carrier | Eligible | Terminal | Median |margin| | Sign-limited | Gap-limited |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for d in result["domains"]:
        med=d["absolute_boundary_distance"]["median"]
        lines.append(
            f"| {d['carrier_id']} | {d['eligible']} | {d['terminal']} | "
            f"{'' if med is None else f'{med:.6g}'} | "
            f"{d['limiting_surface_counts']['sign']} | "
            f"{d['limiting_surface_counts']['simplicity']} |"
        )

    nb=result["network_bifurcation"]
    lines += [
        "",
        "## Relational network",
        "",
        f"Eligible probes: `{nb['eligible_count']}`",
        "",
        f"Terminal probes: `{nb['terminal_count']}`",
        "",
        f"Nearest eligible state to the bifurcation surface: "
        f"`{nb['nearest_eligible_margin']:.9g}`",
        "",
        f"Nearest terminal state to the bifurcation surface: "
        f"`{nb['nearest_terminal_margin']:.9g}`",
        "",
        "The signed margin therefore resolves not only the `13/21` classification "
        "but also how much active-operator perturbation is required to change "
        "that classification.",
        "",
        "## Claim boundary",
        "",
        "The radius is exact for perturbations of the active Hermitian formation "
        "operator `K_+`. It is not yet a theorem giving the same radius directly "
        "in the parent `(K,Y,R,rho)` state norm, because parent perturbations can "
        "also rotate the active packet subspace.",
    ]
    md_path.write_text(
        "\n".join(lines)+"\n",
        encoding="utf-8",
    )

    # Signed margin plot for the relational carrier.
    network=[
        r for r in result["rows"]
        if r.get("gate_reached")
        and r["carrier_id"]=="zachary-karate-network"
    ]
    plot_path=outdir/"network_formation_signed_margin.png"
    fig,ax=plt.subplots(figsize=(9.0,4.8))
    x=np.asarray([r["state_index"] for r in network])
    y=np.asarray([r["signed_margin"] for r in network])
    ax.scatter(x,y)
    ax.axhline(0.0,linestyle="--")
    ax.set_xlabel("node-centered network probe")
    ax.set_ylabel("signed active-operator formation margin")
    ax.set_title("Formation bifurcation margin: relational carrier")
    fig.tight_layout()
    fig.savefig(plot_path,dpi=170)
    plt.close(fig)

    return {
        "json":str(json_path),
        "csv":str(csv_path),
        "markdown":str(md_path),
        "plot":str(plot_path),
    }
