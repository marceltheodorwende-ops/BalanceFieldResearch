from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any
import csv
import json
import math

import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import expm

from .types import NumericalPolicy
from .linalg import hermitize, blockdiag2
from .core import (
    neutral_pair,
    graph_metric,
    persistent_basis,
    graph_projector,
)
from .finite_closure import bfg_state_to_reduced, ReducedClosureState
from .runtime_transfer import load_allowed_transfer_sources
from .network_carrier import KarateInteractionCarrier
from .formation_robustness import (
    formation_margin,
    active_packet_formation_operator,
)
from .stratum_geometry import (
    persistent_runtime_rank_certificate,
    active_runtime_rank_certificate,
)
from .session import source_tree_fingerprint


@dataclass(frozen=True)
class ParentFormationBound:
    delta: float
    valid: bool
    reason: str | None
    active_margin: float
    active_rank: int
    persistent_rank: int
    persistent_gap: float | None
    persistent_subspace_bound: float | None
    weighted_projector_bound: float | None
    load_bound: float | None
    alpha_bound: float | None
    packet_bound: float | None
    active_subspace_sin_bound: float | None
    active_formation_bound: float | None

    def to_dict(self) -> dict[str,Any]:
        return asdict(self)


@dataclass(frozen=True)
class ParentFormationCertificate:
    eligible: bool
    active_margin: float
    parent_radius: float
    product_norm: str
    normality_residual: float
    contraction_excess: float
    persistent_rank: int
    persistent_gap: float | None
    active_rank: int
    active_singular_gap: float
    lambda_keep: float
    lambda_up: float
    alpha: float
    beta: float
    y_min: float
    rho_mass: float
    radius_bound: ParentFormationBound

    def to_dict(self) -> dict[str,Any]:
        out=asdict(self)
        out["radius_bound"]=self.radius_bound.to_dict()
        return out


@dataclass(frozen=True)
class RuntimeStratumRadiusCertificate:
    formation_eligible: bool
    conditional_parent_radius: float
    runtime_stratum_parent_radius: float
    persistent_runtime_native_radius: float
    active_runtime_native_radius: float
    persistent_rank: int
    active_rank: int
    active_packet_bound_at_radius: float
    active_formation_bound_at_radius: float
    persistent_utilization: float
    active_rank_utilization: float
    formation_utilization: float
    limiting_surface: str

    def to_dict(self) -> dict[str,Any]:
        return asdict(self)


def _base_parent_geometry(state, policy:NumericalPolicy) -> dict[str,Any]:
    if state.bottom:
        raise ValueError("bottom has no parent formation radius")

    K=hermitize(np.asarray(state.K,dtype=complex))
    Y=hermitize(np.asarray(state.Y,dtype=complex))
    R=np.asarray(state.R,dtype=complex)
    rho=hermitize(np.asarray(state.rho,dtype=complex))
    n=K.shape[0]

    yvals=np.linalg.eigvalsh(Y).real
    ymin=float(np.min(yvals))
    if ymin<=policy.psd_tol:
        raise ValueError("parent-radius theorem requires positive definite Y")

    rvals=np.linalg.eigvalsh(rho).real
    if float(np.min(rvals)) < -policy.psd_tol:
        raise ValueError("rho must be positive semidefinite")
    mu=float(np.real(np.trace(rho)))
    if mu<=policy.atol:
        raise ValueError("rho mass must be positive")

    normality=float(
        np.linalg.norm(
            R.conj().T@R-R@R.conj().T,
            2,
        )
    )
    rnorm=float(np.linalg.norm(R,2))
    contraction_excess=max(0.0,rnorm-1.0)

    C,B=neutral_pair(Y)
    G=graph_metric(Y)
    W,_=persistent_basis(R,G,policy)
    prank=int(W.shape[1])
    if prank==0:
        raise ValueError("no persistent peripheral sector")
    P=graph_projector(W,G)
    pnorm=float(np.linalg.norm(P,2))

    # For normal contractions, the Euclidean persistent subspace is the kernel
    # of H_R=I-R*R. Its first positive eigenvalue is the persistent/complement
    # separation controlling admissible subspace rotation.
    HR=hermitize(
        np.eye(n,dtype=complex)-R.conj().T@R
    )
    hvals=np.linalg.eigvalsh(HR).real
    if float(np.min(hvals)) < -100*policy.atol:
        raise ValueError("R is not contractive enough for the parent theorem")
    positive=hvals[hvals>max(policy.peripheral_tol,100*policy.atol)]
    if prank==n:
        persistent_gap=float("inf")
    elif positive.size:
        persistent_gap=float(np.min(positive))
    else:
        raise ValueError("persistent/complement singular gap is unresolved")

    keep=P@C
    up=P@B
    lk=float(np.real(np.trace(
        G@keep@rho@keep.conj().T
    )))
    lu=float(np.real(np.trace(
        G@up@rho@up.conj().T
    )))
    if lk<=policy.atol or lu<=policy.atol:
        raise ValueError("dual persistent load below admissibility threshold")
    S=lk+lu
    alpha=lu/S
    beta=lk/S

    A=np.vstack([
        np.sqrt(alpha)*(P@C),
        np.sqrt(beta)*(P@B),
    ])
    singular=np.sort(
        np.linalg.svd(A,compute_uv=False)
    )[::-1]
    if singular.size==0:
        raise ValueError("active packet is empty")
    active_cert=active_runtime_rank_certificate(A,policy)
    arank=int(active_cert.rank)
    if arank==0:
        raise ValueError("active packet is empty")
    sigma_floor=float(singular[arank-1])
    sigma_next=(
        float(singular[arank])
        if arank<len(singular)
        else 0.0
    )
    subspace_gap=float(sigma_floor-sigma_next)
    if subspace_gap<=0:
        raise ValueError("active singular subspace gap is unresolved")

    persistent_cert=persistent_runtime_rank_certificate(
        R,policy
    )
    if persistent_cert.rank!=prank:
        raise ValueError(
            "persistent singular/eigenvalue runtime ranks disagree"
        )

    _,Kplus=active_packet_formation_operator(state,policy)
    margin=formation_margin(Kplus,policy)

    return {
        "K":K,"Y":Y,"R":R,"rho":rho,
        "n":n,
        "y_norm":float(np.linalg.norm(Y,2)),
        "y_min":ymin,
        "g_norm":float(np.linalg.norm(G,2)),
        "r_norm":rnorm,
        "normality":normality,
        "contraction_excess":contraction_excess,
        "mu":mu,
        "P":P,
        "p_norm":pnorm,
        "persistent_rank":prank,
        "persistent_gap":persistent_gap,
        "lk":lk,
        "lu":lu,
        "S":S,
        "alpha":alpha,
        "beta":beta,
        "A":A,
        "active_rank":arank,
        "active_singular_gap":sigma_floor,
        "active_subspace_gap":subspace_gap,
        "active_runtime_radius":
            active_cert.certified_operator_radius,
        "persistent_runtime_radius":
            persistent_cert.certified_operator_radius,
        "active_margin":float(margin.absolute_boundary_distance),
        "eligible":bool(margin.eligible),
        "K_norm":float(np.linalg.norm(K,2)),
    }


def _parent_formation_bound_from_base(
    base:dict[str,Any],
    delta:float,
    *,
    policy:NumericalPolicy,
    normality_tol:float,
) -> ParentFormationBound:
    d=float(delta)
    margin=base["active_margin"]
    arank=base["active_rank"]
    prank=base["persistent_rank"]
    pgap=base["persistent_gap"]

    if base["normality"]>normality_tol:
        return ParentFormationBound(
            d,False,"R is not normal within theorem tolerance",
            margin,arank,prank,pgap,None,None,None,None,None,None,None
        )
    if base["contraction_excess"]>normality_tol:
        return ParentFormationBound(
            d,False,"R exceeds the contraction class",
            margin,arank,prank,pgap,None,None,None,None,None,None,None
        )
    if d>=base["y_min"]-policy.psd_tol:
        return ParentFormationBound(
            d,False,"Y positivity floor reached",
            margin,arank,prank,pgap,None,None,None,None,None,None,None
        )
    if d>=base["mu"]-policy.atol:
        return ParentFormationBound(
            d,False,"rho mass floor reached",
            margin,arank,prank,pgap,None,None,None,None,None,None,None
        )

    if prank==base["n"]:
        q=0.0
    else:
        hpert=2.0*base["r_norm"]*d+d*d
        if not np.isfinite(pgap) or hpert>=0.5*pgap:
            return ParentFormationBound(
                d,False,"persistent spectral gap budget exhausted",
                margin,arank,prank,pgap,None,None,None,None,None,None,None
            )
        q=2.0*hpert/pgap
        if q>=1.0:
            return ParentFormationBound(
                d,False,"persistent subspace rotation bound reached one",
                margin,arank,prank,pgap,q,None,None,None,None,None,None
            )

    g0=base["g_norm"]
    g1=g0+d
    metric_part=d*(g0+1.0)
    subspace_part=2.0*math.sqrt(2.0)*g1*(1.0+g1)*q
    dp=metric_part+subspace_part

    p0=base["p_norm"]
    p1=p0+dp
    dx=dp+p0*d

    mu1=base["mu"]+d
    load_bound=(
        d*p1*p1*mu1
        +g0*mu1*(p1+p0)*dx
        +g0*p0*p0*d
    )

    if load_bound>=min(base["lk"],base["lu"]):
        return ParentFormationBound(
            d,False,"dual-load positivity budget exhausted",
            margin,arank,prank,pgap,q,dp,load_bound,None,None,None,None
        )
    if 2.0*load_bound>=base["S"]:
        return ParentFormationBound(
            d,False,"reciprocal-weight denominator budget exhausted",
            margin,arank,prank,pgap,q,dp,load_bound,None,None,None,None
        )

    dalpha=load_bound/(base["S"]-2.0*load_bound)
    if dalpha>=min(base["alpha"],base["beta"]):
        return ParentFormationBound(
            d,False,"reciprocal-weight square-root budget exhausted",
            margin,arank,prank,pgap,q,dp,load_bound,dalpha,None,None,None
        )

    dsqrt_alpha=(
        dalpha
        /(
            math.sqrt(base["alpha"])
            +math.sqrt(base["alpha"]-dalpha)
        )
        if dalpha>0 else 0.0
    )
    dsqrt_beta=(
        dalpha
        /(
            math.sqrt(base["beta"])
            +math.sqrt(base["beta"]-dalpha)
        )
        if dalpha>0 else 0.0
    )
    e_keep=dsqrt_alpha*p1+math.sqrt(base["alpha"])*dx
    e_up=dsqrt_beta*p1+math.sqrt(base["beta"])*dx
    eA=math.sqrt(e_keep*e_keep+e_up*e_up)

    sigma=base["active_subspace_gap"]
    if eA>=0.5*sigma:
        return ParentFormationBound(
            d,False,"active singular-gap budget exhausted",
            margin,arank,prank,pgap,q,dp,load_bound,dalpha,eA,None,None
        )

    sintheta=2.0*eA/sigma
    active_bound=(
        d
        +2.0*math.sqrt(2.0)*base["K_norm"]*sintheta
    )

    if active_bound>=margin:
        return ParentFormationBound(
            d,False,"active formation margin exhausted",
            margin,arank,prank,pgap,q,dp,load_bound,dalpha,eA,
            sintheta,active_bound
        )

    return ParentFormationBound(
        delta=d,
        valid=True,
        reason=None,
        active_margin=margin,
        active_rank=arank,
        persistent_rank=prank,
        persistent_gap=pgap,
        persistent_subspace_bound=q,
        weighted_projector_bound=dp,
        load_bound=load_bound,
        alpha_bound=dalpha,
        packet_bound=eA,
        active_subspace_sin_bound=sintheta,
        active_formation_bound=active_bound,
    )


def parent_formation_bound(
    state,
    delta:float,
    *,
    policy:NumericalPolicy|None=None,
    normality_tol:float=1e-8,
) -> ParentFormationBound:
    """
    Sufficient parent-to-active perturbation bound in the componentwise product
    norm

        ||Delta S||_oplus
        = max(
            ||Delta K||_2,
            ||Delta Y||_2,
            ||Delta R||_2,
            ||Delta rho||_1
          ).

    Admissible perturbations are additionally required to remain inside:
      - Y positive definite,
      - rho nonzero rank-one PSD,
      - R normal contractive with the same peripheral rank.

    The last condition is essential: an arbitrary radial perturbation of a
    unit-circle eigenvalue can destroy persistence at arbitrarily small norm.
    """
    policy=policy or NumericalPolicy()
    d=float(delta)
    if not np.isfinite(d) or d<0:
        raise ValueError("delta must be nonnegative finite")

    try:
        base=_base_parent_geometry(state,policy)
    except ValueError as exc:
        return ParentFormationBound(
            delta=d,valid=False,reason=str(exc),
            active_margin=0.0,active_rank=0,persistent_rank=0,
            persistent_gap=None,persistent_subspace_bound=None,
            weighted_projector_bound=None,load_bound=None,
            alpha_bound=None,packet_bound=None,
            active_subspace_sin_bound=None,
            active_formation_bound=None,
        )

    return _parent_formation_bound_from_base(
        base,d,policy=policy,normality_tol=normality_tol
    )


def certify_parent_formation_radius(
    state,
    *,
    policy:NumericalPolicy|None=None,
    normality_tol:float=1e-8,
    relative_tolerance:float=1e-6,
    max_iterations:int=80,
) -> ParentFormationCertificate:
    """
    Compute a certified componentwise parent-state radius by monotone bisection.

    This is a sufficient radius, generally conservative.
    """
    policy=policy or NumericalPolicy()
    base=_base_parent_geometry(state,policy)

    if base["normality"]>normality_tol:
        raise ValueError("R is not normal within theorem tolerance")
    if base["contraction_excess"]>normality_tol:
        raise ValueError("R exceeds the contraction class")

    # Finite a-priori ceiling from positivity/mass and active margin.
    ceiling=min(
        0.49*max(base["y_min"]-policy.psd_tol,0.0),
        0.49*max(base["mu"]-policy.atol,0.0),
        0.49*base["active_singular_gap"],
        0.99*base["active_margin"],
    )
    if base["persistent_rank"]<base["n"] and np.isfinite(base["persistent_gap"]):
        # Solve 2||R||d+d^2 < gap/2 conservatively by a small ceiling.
        g=base["persistent_gap"]
        rr=base["r_norm"]
        root=max(0.0,-rr+math.sqrt(rr*rr+0.5*g))
        ceiling=min(ceiling,0.49*root)

    if ceiling<=0:
        raise ValueError("no positive parent-radius ceiling")

    lo=0.0
    hi=ceiling

    # Expand hi within the hard ceiling is unnecessary: ceiling already bounds
    # all admissibility floors.  If it is still valid, it is itself a valid
    # certified radius.
    hibound=_parent_formation_bound_from_base(
        base,hi,policy=policy,normality_tol=normality_tol
    )
    if hibound.valid:
        lo=hi
        best=hibound
    else:
        best=_parent_formation_bound_from_base(
            base,0.0,policy=policy,normality_tol=normality_tol
        )
        for _ in range(max_iterations):
            mid=0.5*(lo+hi)
            bound=_parent_formation_bound_from_base(
                base,mid,policy=policy,normality_tol=normality_tol
            )
            if bound.valid:
                lo=mid
                best=bound
            else:
                hi=mid
            if hi-lo<=max(
                1e-14,
                relative_tolerance*ceiling,
            ):
                break

    if lo<=0 or not best.valid:
        raise ValueError("no positive certified parent radius")

    return ParentFormationCertificate(
        eligible=base["eligible"],
        active_margin=base["active_margin"],
        parent_radius=float(lo),
        product_norm=(
            "max(||DeltaK||_2,||DeltaY||_2,||DeltaR||_2,"
            "||Deltarho||_1)"
        ),
        normality_residual=base["normality"],
        contraction_excess=base["contraction_excess"],
        persistent_rank=base["persistent_rank"],
        persistent_gap=(
            None
            if math.isinf(base["persistent_gap"])
            else base["persistent_gap"]
        ),
        active_rank=base["active_rank"],
        active_singular_gap=base["active_singular_gap"],
        lambda_keep=base["lk"],
        lambda_up=base["lu"],
        alpha=base["alpha"],
        beta=base["beta"],
        y_min=base["y_min"],
        rho_mass=base["mu"],
        radius_bound=best,
    )



def _runtime_stratum_bound_from_base(
    base:dict[str,Any],
    delta:float,
    *,
    policy:NumericalPolicy,
    normality_tol:float,
) -> ParentFormationBound:
    """
    Strengthen the conditional parent bound by also preserving the two runtime
    rank decisions themselves.

    Persistent rank is protected directly in Delta R.  Active rank is protected
    by requiring the packet perturbation bound to remain below the certified
    numerical active-rank radius.
    """
    d=float(delta)
    if d>=base["persistent_runtime_radius"]:
        return ParentFormationBound(
            d,False,"persistent runtime-rank margin exhausted",
            base["active_margin"],base["active_rank"],
            base["persistent_rank"],base["persistent_gap"],
            None,None,None,None,None,None,None,
        )

    bound=_parent_formation_bound_from_base(
        base,d,policy=policy,normality_tol=normality_tol
    )
    if not bound.valid:
        return bound

    if (
        bound.packet_bound is None
        or bound.packet_bound>=base["active_runtime_radius"]
    ):
        return ParentFormationBound(
            d,False,"active runtime-rank margin exhausted",
            base["active_margin"],base["active_rank"],
            base["persistent_rank"],base["persistent_gap"],
            bound.persistent_subspace_bound,
            bound.weighted_projector_bound,
            bound.load_bound,
            bound.alpha_bound,
            bound.packet_bound,
            bound.active_subspace_sin_bound,
            bound.active_formation_bound,
        )
    return bound


def certify_runtime_stratum_radius(
    state,
    *,
    policy:NumericalPolicy|None=None,
    normality_tol:float=1e-8,
    relative_tolerance:float=1e-6,
    max_iterations:int=100,
) -> RuntimeStratumRadiusCertificate:
    """
    Certified parent-product-norm radius preserving:
      - runtime persistent rank,
      - runtime active rank,
      - formation status.

    The perturbed state is still required to remain in the admissible PSD /
    normal-contraction category, but equal runtime ranks are now consequences of
    the radius rather than assumptions.
    """
    policy=policy or NumericalPolicy()
    base=_base_parent_geometry(state,policy)
    conditional=certify_parent_formation_radius(
        state,
        policy=policy,
        normality_tol=normality_tol,
        relative_tolerance=relative_tolerance,
        max_iterations=max_iterations,
    )

    ceiling=min(
        conditional.parent_radius,
        0.99*base["persistent_runtime_radius"],
    )
    if ceiling<=0:
        raise ValueError("no positive runtime-stratum ceiling")

    lo=0.0
    hi=ceiling
    best=_runtime_stratum_bound_from_base(
        base,0.0,policy=policy,normality_tol=normality_tol
    )

    hibound=_runtime_stratum_bound_from_base(
        base,hi,policy=policy,normality_tol=normality_tol
    )
    if hibound.valid:
        lo=hi
        best=hibound
    else:
        for _ in range(max_iterations):
            mid=0.5*(lo+hi)
            b=_runtime_stratum_bound_from_base(
                base,mid,
                policy=policy,
                normality_tol=normality_tol,
            )
            if b.valid:
                lo=mid
                best=b
            else:
                hi=mid
            if hi-lo<=max(
                1e-22,
                relative_tolerance*max(lo,1e-20),
            ):
                break

    if lo<=0 or not best.valid:
        raise ValueError(
            "no positive certified runtime-stratum parent radius"
        )

    packet_at=float(
        best.packet_bound
        if best.packet_bound is not None else 0.0
    )
    formation_at=float(
        best.active_formation_bound
        if best.active_formation_bound is not None else 0.0
    )
    pu=lo/max(base["persistent_runtime_radius"],1e-300)
    au=packet_at/max(base["active_runtime_radius"],1e-300)
    fu=formation_at/max(base["active_margin"],1e-300)
    utilizations={
        "persistent_runtime_rank":pu,
        "active_runtime_rank":au,
        "formation_status":fu,
    }
    limiting=max(utilizations,key=utilizations.get)

    return RuntimeStratumRadiusCertificate(
        formation_eligible=bool(base["eligible"]),
        conditional_parent_radius=float(
            conditional.parent_radius
        ),
        runtime_stratum_parent_radius=float(lo),
        persistent_runtime_native_radius=float(
            base["persistent_runtime_radius"]
        ),
        active_runtime_native_radius=float(
            base["active_runtime_radius"]
        ),
        persistent_rank=int(base["persistent_rank"]),
        active_rank=int(base["active_rank"]),
        active_packet_bound_at_radius=packet_at,
        active_formation_bound_at_radius=formation_at,
        persistent_utilization=float(pu),
        active_rank_utilization=float(au),
        formation_utilization=float(fu),
        limiting_surface=limiting,
    )


def structured_parent_perturbation_control(
    state,
    certificate:ParentFormationCertificate,
    *,
    factor:float=0.5,
    radius_override:float|None=None,
    policy:NumericalPolicy|None=None,
) -> dict[str,Any]:
    """
    Deterministic admissible regression control inside the certified radius.

    The perturbation simultaneously changes K, Y, rho, and rotates the
    persistent/complement decomposition of R by unitary conjugation while
    preserving R's normal spectrum.
    """
    policy=policy or NumericalPolicy()
    if not 0<factor<1:
        raise ValueError("factor must lie in (0,1)")
    base_radius=(
        float(radius_override)
        if radius_override is not None
        else float(certificate.parent_radius)
    )
    d=factor*base_radius
    if d<=0:
        raise ValueError("certificate radius must be positive")

    K=hermitize(np.asarray(state.K,dtype=complex))
    Y=hermitize(np.asarray(state.Y,dtype=complex))
    R=np.asarray(state.R,dtype=complex)
    rho=hermitize(np.asarray(state.rho,dtype=complex))
    n=K.shape[0]

    # Hermitian K perturbation at the componentwise budget.
    e0=np.zeros((n,1),dtype=complex)
    e0[0,0]=1.0
    HK=e0@e0.conj().T
    Kt=hermitize(K+d*HK)

    # Rank-one PSD rho perturbation by a small positive mass rescaling.
    mu=float(np.real(np.trace(rho)))
    rho_scale=1.0+d/max(2.0*mu,1e-300)
    rhot=hermitize(rho_scale*rho)

    # Rotate the persistent/complement subspaces by a common unitary conjugation
    # of R and Y.  This changes the persistent projector while staying on the
    # current graph-aligned, fixed-active-rank stratum used by the real carriers.
    HR=hermitize(
        np.eye(n,dtype=complex)-R.conj().T@R
    )
    hvals,hvecs=np.linalg.eigh(HR)
    zero=np.where(
        hvals<=max(policy.peripheral_tol,100*policy.atol)
    )[0]
    positive=np.where(
        hvals>max(policy.peripheral_tol,100*policy.atol)
    )[0]

    Rt=R.copy()
    Yrot=Y.copy()
    if zero.size and positive.size:
        up=hvecs[:,zero[0]:zero[0]+1]
        uc=hvecs[:,positive[0]:positive[0]+1]
        S=up@uc.conj().T-uc@up.conj().T
        scale=max(
            float(np.linalg.norm(R,2)),
            float(np.linalg.norm(Y,2)),
            1.0,
        )
        theta=min(
            0.1,
            math.log1p(d/(8.0*scale)),
        )
        for _ in range(12):
            Q=expm(theta*S)
            Rcand=Q@R@Q.conj().T
            Ycand=hermitize(Q@Y@Q.conj().T)
            rmove=float(np.linalg.norm(Rcand-R,2))
            ymove=float(np.linalg.norm(Ycand-Y,2))
            if rmove<=0.25*d and ymove<=0.25*d:
                Rt=Rcand
                Yrot=Ycand
                break
            theta*=0.5

    # Add a positive metric perturbation while keeping the total Y movement
    # strictly below the componentwise budget.
    Yt=hermitize(Yrot+0.5*d*np.eye(n,dtype=complex))

    perturbed=ReducedClosureState(
        rho=rhot,
        K=Kt,
        Y=Yt,
        R=Rt,
        generation=state.generation,
        bottom=False,
        metadata={
            **dict(state.metadata),
            "structured_parent_perturbation_control":True,
        },
    )

    _,Kp=active_packet_formation_operator(state,policy)
    _,Kpt=active_packet_formation_operator(perturbed,policy)
    m0=formation_margin(Kp,policy)
    mt=formation_margin(Kpt,policy)

    ev0=np.sort(np.linalg.eigvalsh(Kp).real)
    evt=np.sort(np.linalg.eigvalsh(Kpt).real)
    same_active_rank=bool(len(ev0)==len(evt))
    spectral_shift=(
        float(np.max(np.abs(evt-ev0)))
        if same_active_rank
        else float("inf")
    )

    actual_components={
        "K":float(np.linalg.norm(Kt-K,2)),
        "Y":float(np.linalg.norm(Yt-Y,2)),
        "R":float(np.linalg.norm(Rt-R,2)),
        "rho_trace":float(
            np.linalg.norm(rhot-rho,ord="nuc")
        ),
    }
    actual_parent_norm=max(actual_components.values())

    # Re-evaluate the theorem bound at the actual componentwise radius.
    bound=parent_formation_bound(
        state,
        actual_parent_norm,
        policy=policy,
    )

    return {
        "factor":float(factor),
        "target_component_budget":float(d),
        "actual_components":actual_components,
        "actual_parent_norm":float(actual_parent_norm),
        "within_certificate":bool(
            actual_parent_norm<base_radius
        ),
        "same_active_rank":same_active_rank,
        "original_eligible":bool(m0.eligible),
        "perturbed_eligible":bool(mt.eligible),
        "status_preserved":bool(m0.eligible==mt.eligible),
        "active_spectral_shift":spectral_shift,
        "active_bound":bound.active_formation_bound,
        "active_bound_verified":bool(
            bound.active_formation_bound is not None
            and spectral_shift<=bound.active_formation_bound+1e-10
        ),
        "bound_valid":bool(bound.valid),
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


def run_parent_formation_radius_audit(
    project_root:str|Path|None=None,
    *,
    limit_per_timeseries_carrier:int|None=None,
    include_full_network:bool=True,
) -> dict[str,Any]:
    """
    Compute conditional certified parent-state radii on current first-step
    carriers.  No held-out target metric is loaded.
    """
    root=(
        Path(project_root)
        if project_root is not None
        else Path(__file__).resolve().parent.parent
    )
    sources=list(load_allowed_transfer_sources(root))

    source_rows=[]
    for source in sources:
        states=source.states
        if limit_per_timeseries_carrier is not None:
            if limit_per_timeseries_carrier<1:
                raise ValueError("limit_per_timeseries_carrier must be positive")
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
        control_indices=(
            set(range(len(states)))
            if carrier_id=="zachary-karate-network"
            else {0,max(0,len(states)//2),max(0,len(states)-1)}
        )
        for i,bfg in enumerate(states):
            reduced=bfg_state_to_reduced(bfg)
            try:
                cert=certify_parent_formation_radius(reduced)
                runtime_cert=certify_runtime_stratum_radius(reduced)
                row={
                    "carrier_id":carrier_id,
                    "state_index":i,
                    "certified":True,
                    **cert.to_dict(),
                    "runtime_stratum_parent_radius":
                        runtime_cert.runtime_stratum_parent_radius,
                    "runtime_persistent_native_radius":
                        runtime_cert.persistent_runtime_native_radius,
                    "runtime_active_native_radius":
                        runtime_cert.active_runtime_native_radius,
                    "runtime_persistent_utilization":
                        runtime_cert.persistent_utilization,
                    "runtime_active_rank_utilization":
                        runtime_cert.active_rank_utilization,
                    "runtime_formation_utilization":
                        runtime_cert.formation_utilization,
                    "runtime_limiting_surface":
                        runtime_cert.limiting_surface,
                    "reason":None,
                    "structured_control_run":False,
                    "structured_status_preserved":None,
                    "structured_active_bound_verified":None,
                    "structured_same_active_rank":None,
                    "runtime_control_run":False,
                    "runtime_status_preserved":None,
                    "runtime_same_active_rank":None,
                }
                if i in control_indices:
                    ctl=structured_parent_perturbation_control(
                        reduced,cert,factor=0.5
                    )
                    rctl=structured_parent_perturbation_control(
                        reduced,cert,factor=0.5,
                        radius_override=
                            runtime_cert.runtime_stratum_parent_radius,
                    )
                    row.update({
                        "structured_control_run":True,
                        "structured_status_preserved":
                            ctl["status_preserved"],
                        "structured_active_bound_verified":
                            ctl["active_bound_verified"],
                        "structured_same_active_rank":
                            ctl["same_active_rank"],
                        "structured_parent_norm":
                            ctl["actual_parent_norm"],
                        "structured_active_spectral_shift":
                            ctl["active_spectral_shift"],
                        "structured_active_bound":
                            ctl["active_bound"],
                        "runtime_control_run":True,
                        "runtime_status_preserved":
                            rctl["status_preserved"],
                        "runtime_same_active_rank":
                            rctl["same_active_rank"],
                        "runtime_control_within_radius":
                            rctl["within_certificate"],
                    })
            except ValueError as exc:
                row={
                    "carrier_id":carrier_id,
                    "state_index":i,
                    "certified":False,
                    "reason":str(exc),
                    "structured_control_run":False,
                }
            drows.append(row)
            rows.append(row)

        good=[r for r in drows if r["certified"]]
        controls=[
            r for r in drows
            if r.get("structured_control_run")
        ]
        domains.append({
            "carrier_id":carrier_id,
            "states":len(states),
            "certified":len(good),
            "certified_fraction":len(good)/max(len(states),1),
            "parent_radius":_qstats([
                r["parent_radius"] for r in good
            ]),
            "runtime_stratum_parent_radius":_qstats([
                r["runtime_stratum_parent_radius"]
                for r in good
            ]),
            "runtime_limiting_surface_counts":{
                key:sum(
                    int(r["runtime_limiting_surface"]==key)
                    for r in good
                )
                for key in (
                    "persistent_runtime_rank",
                    "active_runtime_rank",
                    "formation_status",
                )
            },
            "active_margin":_qstats([
                r["active_margin"] for r in good
            ]),
            "active_singular_gap":_qstats([
                r["active_singular_gap"] for r in good
            ]),
            "normality_residual":_qstats([
                r["normality_residual"] for r in good
            ]),
            "structured_controls":len(controls),
            "structured_status_preserved":sum(
                int(r.get("structured_status_preserved") is True)
                for r in controls
            ),
            "structured_active_bound_verified":sum(
                int(r.get("structured_active_bound_verified") is True)
                for r in controls
            ),
            "structured_same_active_rank":sum(
                int(r.get("structured_same_active_rank") is True)
                for r in controls
            ),
            "runtime_controls":sum(
                int(r.get("runtime_control_run") is True)
                for r in controls
            ),
            "runtime_status_preserved":sum(
                int(r.get("runtime_status_preserved") is True)
                for r in controls
            ),
            "runtime_same_active_rank":sum(
                int(r.get("runtime_same_active_rank") is True)
                for r in controls
            ),
        })

    good=[r for r in rows if r["certified"]]
    controls=[
        r for r in good
        if r.get("structured_control_run")
    ]
    network=[
        r for r in good
        if r["carrier_id"]=="zachary-karate-network"
    ]

    return {
        "status":"CONDITIONAL_PARENT_FORMATION_RADIUS_AUDIT",
        "source_fingerprint":source_tree_fingerprint(),
        "heldout_metrics_evaluated":False,
        "states_total":len(rows),
        "certified_states":len(good),
        "structured_controls":len(controls),
        "structured_status_preserved":sum(
            int(r.get("structured_status_preserved") is True)
            for r in controls
        ),
        "structured_active_bound_verified":sum(
            int(r.get("structured_active_bound_verified") is True)
            for r in controls
        ),
        "structured_same_active_rank":sum(
            int(r.get("structured_same_active_rank") is True)
            for r in controls
        ),
        "runtime_controls":sum(
            int(r.get("runtime_control_run") is True)
            for r in controls
        ),
        "runtime_status_preserved":sum(
            int(r.get("runtime_status_preserved") is True)
            for r in controls
        ),
        "runtime_same_active_rank":sum(
            int(r.get("runtime_same_active_rank") is True)
            for r in controls
        ),
        "runtime_limiting_surface_counts":{
            key:sum(
                int(r["runtime_limiting_surface"]==key)
                for r in good
            )
            for key in (
                "persistent_runtime_rank",
                "active_runtime_rank",
                "formation_status",
            )
        },
        "product_norm":
            "max(||DeltaK||_2,||DeltaY||_2,||DeltaR||_2,||Deltarho||_1)",
        "admissible_perturbation_class":[
            "Y remains positive definite",
            "rho remains nonzero rank-one positive semidefinite",
            "R and R_tilde are normal contractions with the same peripheral rank",
            "persistent singular gap remains open",
            "dual persistent loads remain positive",
            "active packet rank remains fixed (fixed-rank admissible stratum)",
        ],
        "theorem":{
            "persistent_rotation":
                "q <= 2(2||R||delta+delta^2)/gap_R under half-gap condition",
            "neutral_resolvent":
                "||Delta C||_2 <= ||Delta Y||_2 and Delta B=-Delta C",
            "packet_rotation":
                "sin Theta_U <= 2||Delta A||_2/sigma_r(A) under half-gap condition",
            "active_operator":
                "||Delta K_+||_2 <= delta_K + 2 sqrt(2)||K||_2 sin Theta_U",
            "status_preservation":
                "active-operator bound < exact formation margin",
        },
        "domains":domains,
        "network":{
            "certified":len(network),
            "radius":_qstats([
                r["parent_radius"] for r in network
            ]),
            "runtime_stratum_radius":_qstats([
                r["runtime_stratum_parent_radius"]
                for r in network
            ]),
            "eligible_radius":_qstats([
                r["parent_radius"]
                for r in network if r["eligible"]
            ]),
            "terminal_radius":_qstats([
                r["parent_radius"]
                for r in network if not r["eligible"]
            ]),
        },
        "rows":rows,
        "interpretation_guard":{
            "conditional_theorem":True,
            "arbitrary_R_perturbations_covered":False,
            "why":(
                "Peripheral persistence and exact packet rank are not open under "
                "arbitrary ambient perturbations. The theorem therefore quantifies "
                "admissible parent perturbations that remain inside a fixed "
                "persistent-rank and fixed-active-rank stratum."
            ),
        },
    }


def write_parent_formation_radius_report(
    result:dict[str,Any],
    outdir:str|Path,
) -> dict[str,str]:
    outdir=Path(outdir)
    outdir.mkdir(parents=True,exist_ok=True)

    json_path=outdir/"parent_formation_radius_audit.json"
    json_path.write_text(
        json.dumps(result,indent=2),
        encoding="utf-8",
    )

    csv_path=outdir/"parent_formation_radius_rows.csv"
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

    md_path=outdir/"PARENT_FORMATION_RADIUS.md"
    lines=[
        "# BFG Parent-State Formation Radius",
        "",
        "**Conditional theorem; no held-out target is opened.**",
        "",
        "The declared parent product norm is",
        "",
        r"\[",
        r"\|\Delta S\|_\oplus=",
        r"\max\{\|\Delta K\|_2,\|\Delta Y\|_2,\|\Delta R\|_2,",
        r"\|\Delta\rho\|_1\}.",
        r"\]",
        "",
        "The conditional theorem applies to admissible perturbations inside the "
        "normal-contraction BFG category. A stricter runtime-stratum certificate "
        "additionally proves preservation of the declared persistent and active "
        "numerical ranks.",
        "",
        f"States audited: `{result['states_total']}`",
        "",
        f"Positive parent-radius certificates: "
        f"`{result['certified_states']}/{result['states_total']}`",
        "",
        f"Structured admissible perturbation controls preserving status: "
        f"`{result['structured_status_preserved']}/{result['structured_controls']}`",
        "",
        f"Structured controls satisfying the predicted active spectral bound: "
        f"`{result['structured_active_bound_verified']}/{result['structured_controls']}`",
        "",
        f"Strict runtime-stratum controls preserving status and active rank: "
        f"`{result['runtime_status_preserved']}/{result['runtime_controls']}`",
        "",
        "| Carrier | Certified | Median conditional radius | Median full runtime-stratum radius |",
        "|---|---:|---:|---:|",
    ]
    for d in result["domains"]:
        q=d["parent_radius"]
        rq=d["runtime_stratum_parent_radius"]
        lines.append(
            f"| {d['carrier_id']} | {d['certified']}/{d['states']} | "
            f"{'' if q['median'] is None else format(q['median'],'.6g')} | "
            f"{'' if rq['median'] is None else format(rq['median'],'.6g')} |"
        )

    lines += [
        "",
        "## The transport chain",
        "",
        "1. `Delta R` is converted to a persistent-subspace rotation bound through "
        "the Hermitian gap of `I-R*R`.",
        "2. `Delta Y` controls the exact neutral resolvent through the resolvent "
        "identity.",
        "3. Persistent-projector, load and reciprocal-weight perturbations give "
        "an explicit `Delta A` bound.",
        "4. Wedin subspace perturbation controls the active left support.",
        "5. Compression of `K xor K` converts that support rotation into an "
        "explicit `Delta K_+` bound.",
        "6. If the resulting bound is smaller than the exact active formation "
        "margin, formation status is preserved.",
        "",
        "## Full runtime-stratum radius",
        "",
        "The stricter runtime-stratum radius additionally guarantees that the "
        "declared persistent and active numerical ranks themselves do not cross "
        "their runtime thresholds. In the current carriers this stricter radius "
        "is controlled overwhelmingly by the latent active-rank surface near the "
        "`rank_tol` threshold.",
        "",
        "This stricter radius is operational: it protects the declared finite "
        "runtime decision. It is not a positive radius for exact algebraic rank.",
        "",
        "## Essential restriction",
        "",
        "The theorem is not an unconstrained exact-rank ambient-matrix ball. An "
        "arbitrarily small radial inward perturbation can destroy exact unit-circle "
        "persistence, and exact matrix rank can increase under arbitrarily small "
        "perturbations. The stricter runtime-stratum radius instead protects the "
        "finite runtime's thresholded rank decisions inside the admissible "
        "positivity / normal-contraction category.",
    ]
    md_path.write_text(
        "\n".join(lines)+"\n",
        encoding="utf-8",
    )

    network=[
        r for r in result["rows"]
        if r.get("certified")
        and r["carrier_id"]=="zachary-karate-network"
    ]
    plot_path=outdir/"network_parent_formation_radius.png"
    fig,ax=plt.subplots(figsize=(9.0,4.8))
    x=np.asarray([r["state_index"] for r in network])
    y=np.asarray([r["parent_radius"] for r in network])
    ax.scatter(x,y)
    ax.set_xlabel("node-centered network probe")
    ax.set_ylabel("certified parent product-norm radius")
    ax.set_title("Parent-state formation robustness: relational carrier")
    fig.tight_layout()
    fig.savefig(plot_path,dpi=170)
    plt.close(fig)

    runtime_plot_path=outdir/"network_runtime_stratum_radius.png"
    fig,ax=plt.subplots(figsize=(9.0,4.8))
    yr=np.asarray([
        r["runtime_stratum_parent_radius"]
        for r in network
    ])
    ax.scatter(x,yr)
    ax.set_yscale("log")
    ax.set_xlabel("node-centered network probe")
    ax.set_ylabel("full runtime-stratum parent radius")
    ax.set_title("Runtime-stratum continuity radius: relational carrier")
    fig.tight_layout()
    fig.savefig(runtime_plot_path,dpi=170)
    plt.close(fig)

    return {
        "json":str(json_path),
        "csv":str(csv_path),
        "markdown":str(md_path),
        "plot":str(plot_path),
        "runtime_plot":str(runtime_plot_path),
    }
