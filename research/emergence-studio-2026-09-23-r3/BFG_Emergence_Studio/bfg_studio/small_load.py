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
from .finite_closure import (
    ReducedClosureState,
    bfg_state_to_reduced,
    reduced_closure_step,
)
from .runtime_transfer import load_allowed_transfer_sources
from .core import graph_metric, neutral_pair, persistent_basis, graph_projector
from .session import source_tree_fingerprint


@dataclass(frozen=True)
class SmallLoadBound:
    y_norm: float
    delta: float
    rho_mass: float
    lambda_keep: float
    projector_norm_bound: float
    b_norm_bound: float
    alpha_bound: float
    contraction_constant: float
    successor_y_bound: float
    local_small_load_parameter: float

    def to_dict(self) -> dict[str,Any]:
        return asdict(self)


@dataclass(frozen=True)
class SmallLoadCertificate:
    carrier_id: str
    state_index: int
    depth: int
    success: bool
    theorem_applicable: bool
    y_norm: float
    successor_y_norm: float | None
    actual_quadratic_ratio: float | None
    contraction_constant: float | None
    bound_satisfied: bool | None
    local_small_load_parameter: float | None
    lambda_keep: float | None
    lambda_up: float | None
    projector_norm: float | None = None
    rho_mass: float | None = None
    lambda_up_bound: float | None = None
    alpha_bound: float | None = None
    lambda_up_bound_verified: bool | None = None
    alpha_bound_verified: bool | None = None
    successor_bound_verified: bool | None = None
    reason: str | None = None

    def to_dict(self) -> dict[str,Any]:
        return asdict(self)


def small_load_contraction_constant(
    projector_norm:float,
    rho_mass:float,
    lambda_keep:float,
) -> float:
    """
    Sharp-for-this-proof sufficient coefficient

        C = ||P||_2^2 (1 + mu / eta).

    Here mu=tr(rho) and eta=lambda_keep>0.

    The key neutral identity is stronger than a naive Euclidean estimate:
    because P is G-orthogonal,

        lambda_up = ||P B d||_G^2 <= ||B d||_G^2 <= mu ||Y||_2^2.

    Therefore alpha <= mu ||Y||^2 / eta.
    """
    p=float(projector_norm)
    mu=float(rho_mass)
    eta=float(lambda_keep)
    if not all(np.isfinite(x) for x in (p,mu,eta)):
        raise ValueError("small-load coefficient inputs must be finite")
    if p<0 or mu<=0 or eta<=0:
        raise ValueError("require projector_norm>=0, rho_mass>0, lambda_keep>0")
    return float(p*p*(1.0+mu/eta))


def explicit_small_load_bound(
    state:ReducedClosureState,
    *,
    lambda_keep:float,
    projector_norm:float|None=None,
    delta:float|None=None,
    policy:NumericalPolicy|None=None,
) -> SmallLoadBound:
    """
    Explicit finite-dimensional sufficient bound for the adopted master map.

    Let y=||Y||_2, rho=d d^* with mass mu=tr(rho), and assume
    lambda_keep >= eta > 0. Since P is the G-orthogonal projector,

        lambda_up <= mu y^2,
        alpha <= mu y^2 / eta.

    Hence

        ||Y_+||_2 = ||A||_2^2
        <= ||P||_2^2 (alpha + ||B||_2^2)
        <= ||P||_2^2 (1 + mu/eta) y^2.

    Thus

        C = ||P||_2^2 (1 + mu/eta).

    If only y<=delta is known, ||P||_2^2 <= 1+delta gives the uniform
    corollary

        C <= (1+delta)(1+mu/eta).

    The returned bound uses the actual finite-state projector norm when one is
    not supplied. `delta` is retained as an optional uniform-envelope record.
    """
    if state.bottom:
        raise ValueError("small-load bound requires a nonterminal state")
    if lambda_keep<=0 or not np.isfinite(lambda_keep):
        raise ValueError("lambda_keep must be positive finite")
    policy=policy or NumericalPolicy()

    Y=np.asarray(state.Y,dtype=complex)
    rho=np.asarray(state.rho,dtype=complex)
    yh=0.5*(Y+Y.conj().T)
    rh=0.5*(rho+rho.conj().T)

    y=float(np.linalg.norm(yh,2))
    mu=float(np.real(np.trace(rh)))
    if y<0 or not np.isfinite(y):
        raise ValueError("invalid Y norm")
    if mu<=0 or not np.isfinite(mu):
        raise ValueError("rho mass must be positive finite")

    if projector_norm is None:
        G=graph_metric(yh)
        W,_=persistent_basis(
            np.asarray(state.R,dtype=complex),
            G,
            policy,
        )
        if W.shape[1]==0:
            raise ValueError("no persistent sector for small-load certificate")
        P=graph_projector(W,G)
        projector_norm=float(np.linalg.norm(P,2))
    else:
        projector_norm=float(projector_norm)

    if delta is None:
        delta=y
    delta=float(delta)
    if not np.isfinite(delta) or delta<y or delta<0:
        raise ValueError("delta must be finite and at least ||Y||_2")

    C=small_load_contraction_constant(
        projector_norm,
        mu,
        float(lambda_keep),
    )
    bound=C*y*y

    return SmallLoadBound(
        y_norm=y,
        delta=delta,
        rho_mass=mu,
        lambda_keep=float(lambda_keep),
        projector_norm_bound=float(projector_norm),
        b_norm_bound=float(y),
        alpha_bound=float(mu*y*y/lambda_keep),
        contraction_constant=float(C),
        successor_y_bound=float(bound),
        local_small_load_parameter=float(C*y),
    )


def quadratic_contraction_bound(
    y_norm:float,
    projector_norm:float,
    rho_mass:float,
    lambda_keep:float,
) -> float:
    """
    Return the theorem upper bound C*y^2.
    """
    y=float(y_norm)
    if y<0 or not np.isfinite(y):
        raise ValueError("y_norm must be nonnegative finite")
    C=small_load_contraction_constant(
        projector_norm,
        rho_mass,
        lambda_keep,
    )
    return float(C*y*y)


def quadratic_depth_bound(
    y0:float,
    contraction_constant:float,
    epsilon:float,
) -> int:
    """
    Compatibility name for the double-exponential depth bound.
    """
    return termination_depth_bound(
        y0,
        contraction_constant,
        epsilon,
    )


def termination_depth_bound(
    y0:float,
    contraction_constant:float,
    epsilon:float,
) -> int:
    """
    If y_{n+1} <= C y_n^2 and q=C y0 < 1, then

        y_n <= C^-1 q^(2^n).

    Returns the smallest n such that this upper bound is <= epsilon.
    """
    y0=float(y0)
    C=float(contraction_constant)
    eps=float(epsilon)
    if not all(np.isfinite(x) for x in (y0,C,eps)):
        raise ValueError("inputs must be finite")
    if y0<0 or C<=0 or eps<=0:
        raise ValueError("require y0 >=0, C>0, epsilon>0")
    if y0<=eps:
        return 0

    q=C*y0
    if not 0<q<1:
        raise ValueError(
            "termination-depth bound requires local contraction parameter C*y0 < 1"
        )

    if C*eps>=1:
        return 0

    ratio=math.log(C*eps)/math.log(q)
    if ratio<=1:
        return 0
    return int(math.ceil(math.log(ratio,2.0)))


def certify_small_load_step(
    state:ReducedClosureState,
    *,
    tau:float=1.0,
    policy:NumericalPolicy|None=None,
):
    """
    Execute one master step and return its theorem certificate.

    This helper is used by the integrated mathematical audit and deliberately
    verifies the intermediate lambda_up and alpha inequalities, not only the
    final successor inequality.
    """
    policy=policy or NumericalPolicy()
    successor,step=reduced_closure_step(
        state,
        tau=tau,
        policy=policy,
    )
    if not step.success:
        cert=SmallLoadCertificate(
            carrier_id="internal",
            state_index=0,
            depth=1,
            success=False,
            theorem_applicable=False,
            y_norm=float(np.linalg.norm(state.Y,2)),
            successor_y_norm=None,
            actual_quadratic_ratio=None,
            contraction_constant=None,
            bound_satisfied=None,
            local_small_load_parameter=None,
            lambda_keep=step.lambda_keep,
            lambda_up=step.lambda_up,
            reason=step.reason,
        )
        return cert,successor,step

    Y=np.asarray(state.Y,dtype=complex)
    rho=np.asarray(state.rho,dtype=complex)
    G=graph_metric(Y)
    W,_=persistent_basis(
        np.asarray(state.R,dtype=complex),
        G,
        policy,
    )
    P=graph_projector(W,G)
    pnorm=float(np.linalg.norm(P,2))
    mu=float(np.real(np.trace(rho)))
    y=float(np.linalg.norm(Y,2))
    lk=float(step.lambda_keep)
    lu=float(step.lambda_up)
    alpha=float(step.alpha)

    lu_bound=mu*y*y
    alpha_bound=mu*y*y/lk
    C=small_load_contraction_constant(pnorm,mu,lk)
    yp=float(np.linalg.norm(successor.Y,2))
    successor_bound=C*y*y
    tol=max(policy.atol,1e-14)

    cert=SmallLoadCertificate(
        carrier_id="internal",
        state_index=0,
        depth=1,
        success=True,
        theorem_applicable=True,
        y_norm=y,
        successor_y_norm=yp,
        actual_quadratic_ratio=yp/(y*y) if y>0 else float("inf"),
        contraction_constant=C,
        bound_satisfied=bool(yp<=successor_bound+tol),
        local_small_load_parameter=C*y,
        lambda_keep=lk,
        lambda_up=lu,
        projector_norm=pnorm,
        rho_mass=mu,
        lambda_up_bound=lu_bound,
        alpha_bound=alpha_bound,
        lambda_up_bound_verified=bool(lu<=lu_bound+tol),
        alpha_bound_verified=bool(alpha<=alpha_bound+tol),
        successor_bound_verified=bool(yp<=successor_bound+tol),
        reason=None,
    )
    return cert,successor,step


def one_step_small_load_certificate(
    state:ReducedClosureState,
    successor:ReducedClosureState,
    step,
    *,
    carrier_id:str,
    state_index:int,
    depth:int,
    delta:float|None=None,
    atol:float=1e-12,
) -> SmallLoadCertificate:
    if not step.success:
        return SmallLoadCertificate(
            carrier_id=carrier_id,
            state_index=state_index,
            depth=depth,
            success=False,
            theorem_applicable=False,
            y_norm=float(np.linalg.norm(state.Y,2)),
            successor_y_norm=None,
            actual_quadratic_ratio=None,
            contraction_constant=None,
            bound_satisfied=None,
            local_small_load_parameter=None,
            lambda_keep=step.lambda_keep,
            lambda_up=step.lambda_up,
            reason=step.reason,
        )

    if step.lambda_keep is None or step.lambda_keep<=0:
        return SmallLoadCertificate(
            carrier_id=carrier_id,
            state_index=state_index,
            depth=depth,
            success=True,
            theorem_applicable=False,
            y_norm=float(np.linalg.norm(state.Y,2)),
            successor_y_norm=float(np.linalg.norm(successor.Y,2)),
            actual_quadratic_ratio=None,
            contraction_constant=None,
            bound_satisfied=None,
            local_small_load_parameter=None,
            lambda_keep=step.lambda_keep,
            lambda_up=step.lambda_up,
            reason="positive keep-load hypothesis not satisfied",
        )

    Y=np.asarray(state.Y,dtype=complex)
    rho=np.asarray(state.rho,dtype=complex)
    policy=NumericalPolicy()
    G=graph_metric(Y)
    W,_=persistent_basis(
        np.asarray(state.R,dtype=complex),
        G,
        policy,
    )
    P=graph_projector(W,G)
    pnorm=float(np.linalg.norm(P,2))
    mu=float(np.real(np.trace(rho)))
    y=float(np.linalg.norm(Y,2))
    lk=float(step.lambda_keep)
    lu=float(step.lambda_up)
    alpha=float(step.alpha)

    bound=explicit_small_load_bound(
        state,
        lambda_keep=lk,
        projector_norm=pnorm,
        delta=delta,
        policy=policy,
    )
    yp=float(np.linalg.norm(successor.Y,2))
    ratio=yp/(y*y) if y>0 else float("inf")
    lu_bound=mu*y*y
    alpha_bound=mu*y*y/lk
    ok=yp<=bound.successor_y_bound+atol

    return SmallLoadCertificate(
        carrier_id=carrier_id,
        state_index=state_index,
        depth=depth,
        success=True,
        theorem_applicable=True,
        y_norm=y,
        successor_y_norm=yp,
        actual_quadratic_ratio=float(ratio),
        contraction_constant=bound.contraction_constant,
        bound_satisfied=bool(ok),
        local_small_load_parameter=bound.local_small_load_parameter,
        lambda_keep=lk,
        lambda_up=lu,
        projector_norm=pnorm,
        rho_mass=mu,
        lambda_up_bound=lu_bound,
        alpha_bound=alpha_bound,
        lambda_up_bound_verified=bool(lu<=lu_bound+atol),
        alpha_bound_verified=bool(alpha<=alpha_bound+atol),
        successor_bound_verified=bool(ok),
        reason=None if ok else "explicit quadratic bound violated",
    )


def _quantiles(values:list[float]) -> dict[str,float|None]:
    x=np.asarray(
        [float(v) for v in values if np.isfinite(v)],
        dtype=float,
    )
    if x.size==0:
        return {
            "mean":None,"q10":None,"median":None,
            "q90":None,"min":None,"max":None,
        }
    q=np.quantile(x,[.10,.50,.90])
    return {
        "mean":float(np.mean(x)),
        "q10":float(q[0]),
        "median":float(q[1]),
        "q90":float(q[2]),
        "min":float(np.min(x)),
        "max":float(np.max(x)),
    }


def run_small_load_contraction_audit(
    project_root:str|Path|None=None,
    *,
    recursive_horizon:int|None=None,
    horizon:int|None=None,
    tau:float=1.0,
    limit_per_carrier:int|None=None,
) -> dict[str,Any]:
    """
    Development/calibration-only theorem-hypothesis audit.

    For every successful master transition:
      - build the explicit sufficient C(delta,mu,eta),
      - verify ||Y_+|| <= C ||Y||^2,
      - record whether the stronger local condition C||Y||<1 already holds,
      - when it does, compute an epsilon-depth estimate.

    No held-out target is loaded.
    """
    if recursive_horizon is None:
        recursive_horizon=4 if horizon is None else int(horizon)
    elif horizon is not None and int(horizon)!=int(recursive_horizon):
        raise ValueError("horizon and recursive_horizon disagree")
    recursive_horizon=int(recursive_horizon)
    if recursive_horizon<1:
        raise ValueError("recursive_horizon must be positive")

    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )
    sources=load_allowed_transfer_sources(root)
    policy=NumericalPolicy()

    rows=[]
    domain_results=[]

    for source in sources:
        states=source.states
        if limit_per_carrier is not None:
            if limit_per_carrier<1:
                raise ValueError("limit_per_carrier must be positive")
            states=states[:limit_per_carrier]

        domain_rows=[]
        for i,bfg_state in enumerate(states):
            current=bfg_state_to_reduced(bfg_state)
            for depth in range(1,recursive_horizon+1):
                successor,step=reduced_closure_step(
                    current,
                    tau=tau,
                    policy=policy,
                )
                cert=one_step_small_load_certificate(
                    current,
                    successor,
                    step,
                    carrier_id=source.carrier_id,
                    state_index=i,
                    depth=depth,
                )
                row=cert.to_dict()

                if (
                    cert.theorem_applicable
                    and cert.local_small_load_parameter is not None
                    and 0<cert.local_small_load_parameter<1
                ):
                    epsilon=max(policy.psd_tol,policy.atol)
                    try:
                        row["predicted_steps_to_numerical_floor"]=(
                            termination_depth_bound(
                                cert.y_norm,
                                cert.contraction_constant,
                                epsilon,
                            )
                        )
                    except ValueError:
                        row["predicted_steps_to_numerical_floor"]=None
                else:
                    row["predicted_steps_to_numerical_floor"]=None

                domain_rows.append(row)
                rows.append(row)

                if step.success:
                    current=successor
                else:
                    break

        applicable=[
            r for r in domain_rows
            if r["theorem_applicable"]
        ]
        local=[
            r for r in applicable
            if r["local_small_load_parameter"] is not None
            and r["local_small_load_parameter"]<1
        ]
        domain_results.append({
            "carrier_id":source.carrier_id,
            "states":len(states),
            "certificates":len(applicable),
            "bound_passed":sum(
                int(r["bound_satisfied"] is True)
                for r in applicable
            ),
            "bound_pass_fraction":(
                sum(
                    int(r["bound_satisfied"] is True)
                    for r in applicable
                )/max(len(applicable),1)
            ),
            "local_contraction_certificates":len(local),
            "local_contraction_fraction":(
                len(local)/max(len(applicable),1)
            ),
            "actual_quadratic_ratio":
                _quantiles([
                    r["actual_quadratic_ratio"]
                    for r in applicable
                    if r["actual_quadratic_ratio"] is not None
                ]),
            "contraction_constant":
                _quantiles([
                    r["contraction_constant"]
                    for r in applicable
                    if r["contraction_constant"] is not None
                ]),
            "local_small_load_parameter":
                _quantiles([
                    r["local_small_load_parameter"]
                    for r in applicable
                    if r["local_small_load_parameter"] is not None
                ]),
            "depth_distribution":{
                str(d):sum(
                    int(r["depth"]==d)
                    for r in applicable
                )
                for d in range(1,recursive_horizon+1)
            },
        })

    applicable=[
        r for r in rows if r["theorem_applicable"]
    ]
    bound_pass=sum(
        int(r["bound_satisfied"] is True)
        for r in applicable
    )
    intermediate_pass=sum(
        int(
            r.get("lambda_up_bound_verified") is True
            and r.get("alpha_bound_verified") is True
            and r.get("successor_bound_verified") is True
        )
        for r in applicable
    )
    local=[
        r for r in applicable
        if r["local_small_load_parameter"] is not None
        and r["local_small_load_parameter"]<1
    ]

    # Depth-specific summary: expected to become increasingly local after entry.
    by_depth={}
    for depth in range(1,recursive_horizon+1):
        subset=[
            r for r in applicable
            if r["depth"]==depth
        ]
        local_subset=[
            r for r in subset
            if r["local_small_load_parameter"] is not None
            and r["local_small_load_parameter"]<1
        ]
        by_depth[str(depth)]={
            "certificates":len(subset),
            "bound_passed":sum(
                int(r["bound_satisfied"] is True)
                for r in subset
            ),
            "local_contraction_fraction":(
                len(local_subset)/max(len(subset),1)
            ),
            "actual_quadratic_ratio":
                _quantiles([
                    r["actual_quadratic_ratio"]
                    for r in subset
                    if r["actual_quadratic_ratio"] is not None
                ]),
            "local_small_load_parameter":
                _quantiles([
                    r["local_small_load_parameter"]
                    for r in subset
                    if r["local_small_load_parameter"] is not None
                ]),
        }

    observed_corridor_envelope={
        "actual_quadratic_ratio":_quantiles([
            r["actual_quadratic_ratio"]
            for r in applicable
            if r["actual_quadratic_ratio"] is not None
        ]),
        "contraction_constant":_quantiles([
            r["contraction_constant"]
            for r in applicable
            if r["contraction_constant"] is not None
        ]),
        "local_small_load_parameter":_quantiles([
            r["local_small_load_parameter"]
            for r in applicable
            if r["local_small_load_parameter"] is not None
        ]),
    }

    return {
        "status":"DEVELOPMENT_ONLY_SMALL_LOAD_CONTRACTION_AUDIT",
        "source_fingerprint":source_tree_fingerprint(),
        "heldout_metrics_evaluated":False,
        "recursive_horizon":recursive_horizon,
        "tau":tau,
        "limit_per_carrier":limit_per_carrier,
        "theorem":{
            "assumptions":[
                "finite-dimensional reduced master state",
                "Y positive semidefinite with ||Y||_2 <= delta",
                "rank-one positive rho with finite mass mu",
                "positive keep load lambda_keep >= eta > 0",
                "G-orthogonal persistent projector",
            ],
            "conclusion":
                "||Y_+||_2 <= C(delta,mu,eta) ||Y||_2^2",
            "constant":
                "C=||P||_2^2*(1+mu/eta)",
            "local_iteration_condition":"C*||Y||_2 < 1",
            "termination_upper_bound":
                "y_n <= C^-1 (C*y_0)^(2^n)",
        },
        "certificates":len(applicable),
        "successful_transitions":len(applicable),
        "bound_passed":bound_pass,
        "bound_pass_fraction":
            bound_pass/max(len(applicable),1),
        "intermediate_bounds_verified":intermediate_pass,
        "all_theorem_bounds_verified":bool(
            len(applicable)>0
            and bound_pass==len(applicable)
            and intermediate_pass==len(applicable)
        ),
        "local_contraction_certificates":len(local),
        "local_contraction_fraction":
            len(local)/max(len(applicable),1),
        "depth_summary":by_depth,
        "depth_summaries":by_depth,
        "domains":domain_results,
        "domain_summaries":domain_results,
        "observed_corridor_envelope":observed_corridor_envelope,
        "rows":rows,
        "interpretation_guard":{
            "empirical_universal_law_established":False,
            "heldout_used":False,
            "sharp_constant_claimed":False,
            "note":(
                "The theorem is a sufficient finite-dimensional operator bound. "
                "The real-carrier audit checks its hypotheses and numerical "
                "inequality on development/calibration states only."
            ),
        },
    }


def write_small_load_report(
    result:dict[str,Any],
    outdir:str|Path,
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"small_load_contraction_audit.json"
    json_path.write_text(
        json.dumps(result,indent=2),
        encoding="utf-8",
    )

    rows=result["rows"]
    csv_path=outdir/"small_load_certificates.csv"
    if rows:
        fields=sorted({
            k for row in rows for k in row
        })
        with csv_path.open("w",newline="",encoding="utf-8") as f:
            writer=csv.DictWriter(
                f,
                fieldnames=fields,
                extrasaction="ignore",
            )
            writer.writeheader()
            writer.writerows(rows)

    md_path=outdir/"SMALL_LOAD_CONTRACTION_THEOREM.md"
    lines=[
        "# Multidimensional Small-Load Contraction",
        "",
        "**Development/calibration data only. No held-out target is opened.**",
        "",
        "## Sufficient theorem",
        "",
        "For a finite reduced master state with `Y >= 0`, rank-one positive `rho`, "
        "positive keep load `lambda_keep >= eta > 0`, and `||Y||_2 <= delta`,",
        "",
        r"\[",
        r"\|Y_+\|_2 \le C(\delta,\mu,\eta)\,\|Y\|_2^2,",
        r"\]",
        "",
        "where",
        "",
        r"\[",
        r"C=\|P\|_2^2\left(1+\frac{\mu}{\eta}\right),",
        r"\qquad \mu=\operatorname{tr}\rho.",
        r"\]",
        "",
        "The bound is sufficient and intentionally conservative.",
        "",
        "If additionally",
        "",
        r"\[",
        r"q=C\|Y_0\|_2<1,",
        r"\]",
        "",
        "then repeated application with the same uniform `C` gives",
        "",
        r"\[",
        r"\|Y_n\|_2 \le C^{-1}q^{2^n}.",
        r"\]",
        "",
        "This is double-exponential decay in recursive depth.",
        "",
        "## Current audit",
        "",
        f"Certificates evaluated: `{result['certificates']}`",
        "",
        f"Explicit bound satisfied: "
        f"`{result['bound_passed']}/{result['certificates']}` "
        f"(`{100*result['bound_pass_fraction']:.3f}%`)",
        "",
        f"Already inside the strict local condition `C||Y||<1`: "
        f"`{result['local_contraction_certificates']}/{result['certificates']}` "
        f"(`{100*result['local_contraction_fraction']:.3f}%`)",
        "",
        "## By recursive depth",
        "",
        "| Depth | Certificates | Bound pass | Local C||Y||<1 | "
        "Median actual ||Y+||/||Y||² | Median C||Y|| |",
        "|---:|---:|---:|---:|---:|---:|",
    ]
    for depth,row in result["depth_summary"].items():
        ratio=row["actual_quadratic_ratio"]["median"]
        q=row["local_small_load_parameter"]["median"]
        lines.append(
            f"| {depth} | {row['certificates']} | "
            f"{row['bound_passed']} | "
            f"{100*row['local_contraction_fraction']:.3f}% | "
            f"{'' if ratio is None else f'{ratio:.6g}'} | "
            f"{'' if q is None else f'{q:.6g}'} |"
        )

    lines += [
        "",
        "## Interpretation",
        "",
        "The theorem explains the observed near-quadratic recursive load contraction "
        "without fitting the exponent. The carrier data are used only to test whether "
        "the sufficient finite-dimensional inequality is respected by the current "
        "implemented states.",
        "",
        "A failed strict-local condition `C||Y||<1` does not refute one-step "
        "quadratic boundedness; it only means the conservative uniform iteration "
        "bound is not yet strong enough at that state.",
    ]
    md_path.write_text(
        "\n".join(lines)+"\n",
        encoding="utf-8",
    )

    # Plot actual ratio against the conservative constant.
    plot_path=outdir/"small_load_bound_scatter.png"
    x=np.asarray([
        r["contraction_constant"]
        for r in rows
        if r["theorem_applicable"]
        and r["contraction_constant"] is not None
        and r["actual_quadratic_ratio"] is not None
    ],dtype=float)
    y=np.asarray([
        r["actual_quadratic_ratio"]
        for r in rows
        if r["theorem_applicable"]
        and r["contraction_constant"] is not None
        and r["actual_quadratic_ratio"] is not None
    ],dtype=float)
    fig,ax=plt.subplots(figsize=(6.5,5.0))
    ax.scatter(x,y,s=8,alpha=.35)
    if x.size:
        lo=min(float(np.min(x)),float(np.min(y)))
        hi=max(float(np.max(x)),float(np.max(y)))
        ax.plot([lo,hi],[lo,hi],linestyle="--")
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel("explicit sufficient C")
    ax.set_ylabel("actual ||Y+|| / ||Y||²")
    ax.set_title("Small-load quadratic certificate")
    fig.tight_layout()
    fig.savefig(plot_path,dpi=170)
    plt.close(fig)

    return {
        "json":str(json_path),
        "csv":str(csv_path),
        "markdown":str(md_path),
        "plot":str(plot_path),
    }


def write_small_load_contraction_report(
    result:dict[str,Any],
    outdir:str|Path,
) -> dict[str,str]:
    return write_small_load_report(result,outdir)
