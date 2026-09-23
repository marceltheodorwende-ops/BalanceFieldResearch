from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any

import numpy as np
from scipy.linalg import expm

from .types import NumericalPolicy
from .linalg import hermitize, blockdiag2
from .core import (
    graph_metric,
    neutral_pair,
    persistent_basis,
    graph_projector,
)
from .stability import recursive_stability_certificate


@dataclass
class ReducedClosureState:
    """
    Reduced finite closure category adopted by the master runtime.

    rho : nonzero positive rank-one formation density
    K   : Hermitian formation operator
    Y   : positive-definite neutral load
    R   : power-bounded recursive transport

    bottom=True is the absorbing terminal object.
    """
    rho: np.ndarray | None = None
    K: np.ndarray | None = None
    Y: np.ndarray | None = None
    R: np.ndarray | None = None
    generation: int = 0
    bottom: bool = False
    reason: str | None = None
    metadata: dict[str,Any] = field(default_factory=dict)

    @property
    def dim(self) -> int:
        if self.bottom or self.K is None:
            return 0
        return int(self.K.shape[0])


@dataclass
class ReducedClosureStep:
    generation: int
    success: bool
    terminal: bool
    reason: str | None
    alpha: float | None = None
    beta: float | None = None
    lambda_keep: float | None = None
    lambda_up: float | None = None
    active_rank: int = 0
    formation_eigenvalue: float | None = None
    formation_gap: float | None = None
    persistence_rank: int = 0
    diagnostics: dict[str,Any] = field(default_factory=dict)


def bottom_state(
    generation:int,
    reason:str,
    *,
    metadata:dict[str,Any]|None=None,
)->ReducedClosureState:
    return ReducedClosureState(
        generation=generation,
        bottom=True,
        reason=reason,
        metadata=dict(metadata or {}),
    )


def _validate_reduced_state(
    state:ReducedClosureState,
    policy:NumericalPolicy,
)->dict[str,Any]:
    if state.bottom:
        return {"valid":True,"bottom":True}

    if any(x is None for x in (state.rho,state.K,state.Y,state.R)):
        raise ValueError("nonterminal reduced closure state is incomplete")

    rho=np.asarray(state.rho,dtype=complex)
    K=np.asarray(state.K,dtype=complex)
    Y=np.asarray(state.Y,dtype=complex)
    R=np.asarray(state.R,dtype=complex)

    if K.ndim!=2 or K.shape[0]!=K.shape[1] or K.shape[0]==0:
        raise ValueError("K must be nonempty square")
    n=K.shape[0]
    if rho.shape!=(n,n) or Y.shape!=(n,n) or R.shape!=(n,n):
        raise ValueError("rho, Y and R must match K dimension")
    if not all(np.isfinite(x).all() for x in (rho,K,Y,R)):
        raise ValueError("reduced closure state contains non-finite values")

    k_res=float(np.linalg.norm(K-K.conj().T,2))
    y_res=float(np.linalg.norm(Y-Y.conj().T,2))
    rho_res=float(np.linalg.norm(rho-rho.conj().T,2))
    if k_res>10*policy.atol:
        raise ValueError("K must be Hermitian")
    if y_res>10*policy.atol:
        raise ValueError("Y must be Hermitian")
    if rho_res>10*policy.atol:
        raise ValueError("rho must be Hermitian")

    K=hermitize(K)
    Y=hermitize(Y)
    rho=hermitize(rho)

    yvals=np.linalg.eigvalsh(Y).real
    if float(np.min(yvals))<=policy.psd_tol:
        raise ValueError("reduced closure requires Y positive definite")

    rvals=np.linalg.eigvalsh(rho).real
    if float(np.min(rvals)) < -policy.psd_tol:
        raise ValueError("rho must be positive semidefinite")
    rank=int(np.sum(rvals>policy.rank_tol))
    if rank!=1:
        raise ValueError("rho must be nonzero rank one")

    stability=recursive_stability_certificate(
        R,
        unit_tol=policy.peripheral_tol,
        grouping_tol=max(10*policy.peripheral_tol,1e-7),
        svd_rtol=max(policy.rtol,1e-10),
        horizon=32,
    )
    if not stability.spectral_criterion_satisfied:
        raise ValueError(
            "R does not satisfy finite-dimensional power-boundedness criterion"
        )

    return {
        "valid":True,
        "bottom":False,
        "rho_rank":rank,
        "min_eig_Y":float(np.min(yvals)),
        "recursive_stability":stability.to_dict(),
    }


def reduced_closure_step(
    state:ReducedClosureState,
    *,
    tau:float=1.0,
    policy:NumericalPolicy|None=None,
)->tuple[ReducedClosureState,ReducedClosureStep]:
    """
    Master finite closure profile.

    Implements the reduced finite model:
        C=(I+Y)^-1, B=Y(I+Y)^-1
        alpha=lambda_up/(lambda_keep+lambda_up)
        beta =lambda_keep/(...)
        A=[sqrt(alpha) P C ; sqrt(beta) P B]
        K_+=J^*(K xor K)J on active support
        Y_+=A^*A on active support
        rho_+=(-lambda0) Pi0
        R_+=exp(i tau K_+)

    The map is total after adjoining absorbing bottom.
    """
    policy=policy or NumericalPolicy()
    if not np.isfinite(tau):
        raise ValueError("tau must be finite")

    if state.bottom:
        return (
            state,
            ReducedClosureStep(
                generation=state.generation,
                success=False,
                terminal=True,
                reason=state.reason or "absorbing bottom",
            ),
        )

    validation=_validate_reduced_state(state,policy)

    rho=hermitize(np.asarray(state.rho,dtype=complex))
    K=hermitize(np.asarray(state.K,dtype=complex))
    Y=hermitize(np.asarray(state.Y,dtype=complex))
    R=np.asarray(state.R,dtype=complex)
    n=K.shape[0]

    C,B=neutral_pair(Y)
    G=graph_metric(Y)

    W,_=persistent_basis(R,G,policy)
    p_rank=int(W.shape[1])
    if p_rank==0:
        nxt=bottom_state(
            state.generation+1,
            "no persistent peripheral sector",
            metadata={"parent_generation":state.generation},
        )
        return nxt,ReducedClosureStep(
            generation=state.generation,
            success=False,
            terminal=True,
            reason=nxt.reason,
            persistence_rank=0,
            diagnostics={"validation":validation},
        )

    P=graph_projector(W,G)

    # Eq. (2): squared G-loads in density form.
    keep_op=P@C
    up_op=P@B
    lk=float(np.real(np.trace(
        G@keep_op@rho@keep_op.conj().T
    )))
    lu=float(np.real(np.trace(
        G@up_op@rho@up_op.conj().T
    )))

    if lk<=policy.atol or lu<=policy.atol:
        nxt=bottom_state(
            state.generation+1,
            "dual persistent load vanished",
            metadata={
                "lambda_keep":lk,
                "lambda_up":lu,
            },
        )
        return nxt,ReducedClosureStep(
            generation=state.generation,
            success=False,
            terminal=True,
            reason=nxt.reason,
            lambda_keep=lk,
            lambda_up=lu,
            persistence_rank=p_rank,
            diagnostics={"validation":validation},
        )

    alpha=lu/(lk+lu)
    beta=lk/(lk+lu)

    A=np.vstack([
        np.sqrt(alpha)*(P@C),
        np.sqrt(beta)*(P@B),
    ])

    # Polar support and active carrier H_a=(ker A)^perp.
    U,s,Vh=np.linalg.svd(A,full_matrices=False)
    if s.size==0:
        active_rank=0
    else:
        threshold=max(
            policy.rank_tol,
            policy.rtol*float(s[0]),
        )
        active_rank=int(np.sum(s>threshold))

    if active_rank==0:
        nxt=bottom_state(
            state.generation+1,
            "polar active support is empty",
        )
        return nxt,ReducedClosureStep(
            generation=state.generation,
            success=False,
            terminal=True,
            reason=nxt.reason,
            alpha=alpha,beta=beta,
            lambda_keep=lk,lambda_up=lu,
            persistence_rank=p_rank,
        )

    U_r=U[:,:active_rank]
    V_r=Vh.conj().T[:,:active_rank]
    s_r=s[:active_rank]

    # In active coordinates J|_{H_a}=U_r and Y_+=A^*A|_{H_a}.
    K_plus=hermitize(
        U_r.conj().T@blockdiag2(K)@U_r
    )
    Y_plus=np.diag(np.real(s_r*s_r)).astype(complex)

    kvals,kvecs=np.linalg.eigh(K_plus)
    order=np.argsort(kvals.real)
    kvals=kvals.real[order]
    kvecs=kvecs[:,order]
    lam0=float(kvals[0])
    gap=(
        float("inf")
        if len(kvals)==1
        else float(kvals[1]-kvals[0])
    )

    if not (
        lam0 < -policy.atol
        and gap > policy.simple_gap_tol
    ):
        nxt=bottom_state(
            state.generation+1,
            "formation gate failed: no simple negative lowest eigenvalue",
            metadata={
                "lowest_eigenvalue":lam0,
                "ground_gap":gap,
            },
        )
        return nxt,ReducedClosureStep(
            generation=state.generation,
            success=False,
            terminal=True,
            reason=nxt.reason,
            alpha=alpha,beta=beta,
            lambda_keep=lk,lambda_up=lu,
            active_rank=active_rank,
            formation_eigenvalue=lam0,
            formation_gap=gap,
            persistence_rank=p_rank,
        )

    v0=kvecs[:,0:1]
    Pi0=v0@v0.conj().T
    rho_plus=(-lam0)*Pi0

    # Chosen successor law: unitary by construction.
    R_plus=expm(1j*float(tau)*K_plus)
    unitary_res=float(np.linalg.norm(
        R_plus.conj().T@R_plus
        -np.eye(active_rank,dtype=complex),
        2,
    ))

    # Explicit square-root Gram factor gauge.
    B_C_plus=np.diag(s_r).astype(complex)
    W_N_plus=np.eye(active_rank,dtype=complex)
    L_C_plus=np.eye(active_rank,dtype=complex)
    gram_res=float(np.linalg.norm(
        L_C_plus.conj().T
        @B_C_plus.conj().T
        @W_N_plus
        @B_C_plus
        @L_C_plus
        -Y_plus,
        2,
    ))

    next_state=ReducedClosureState(
        rho=rho_plus,
        K=K_plus,
        Y=Y_plus,
        R=R_plus,
        generation=state.generation+1,
        bottom=False,
        metadata={
            "master_profile":"finite_reduced_closure",
            "tau":float(tau),
            "parent_dimension":n,
            "active_basis_in_parent":V_r,
            "gram_factor_gauge":{
                "B_C":B_C_plus,
                "W_N":W_N_plus,
                "L_C":L_C_plus,
            },
            "unitarity_residual":unitary_res,
            "gram_rebuild_residual":gram_res,
        },
    )

    _validate_reduced_state(next_state,policy)

    step=ReducedClosureStep(
        generation=state.generation,
        success=True,
        terminal=False,
        reason=None,
        alpha=float(alpha),
        beta=float(beta),
        lambda_keep=lk,
        lambda_up=lu,
        active_rank=active_rank,
        formation_eigenvalue=lam0,
        formation_gap=gap,
        persistence_rank=p_rank,
        diagnostics={
            "input_validation":validation,
            "unitarity_residual":unitary_res,
            "gram_rebuild_residual":gram_res,
            "singular_values":[float(x) for x in s_r],
        },
    )
    return next_state,step


def iterate_reduced_closure(
    state:ReducedClosureState,
    steps:int,
    *,
    tau:float=1.0,
    policy:NumericalPolicy|None=None,
)->dict[str,Any]:
    """
    Finite master iteration with absorbing bottom.
    """
    if isinstance(steps,bool) or not isinstance(steps,int) or steps<0:
        raise ValueError("steps must be a nonnegative integer")
    policy=policy or NumericalPolicy()

    states=[state]
    records=[]
    current=state
    for _ in range(steps):
        nxt,record=reduced_closure_step(
            current,tau=tau,policy=policy
        )
        records.append(record)
        states.append(nxt)
        current=nxt
        if current.bottom:
            break

    return {
        "states":states,
        "steps":records,
        "requested_steps":steps,
        "executed_steps":len(records),
        "terminal":current.bottom,
        "final_generation":current.generation,
    }


def scalar_nonterminal_seed(
    y:float=1.0,
    *,
    tau:float=1.0,
)->ReducedClosureState:
    """
    One-dimensional exact-model seed:
        rho=1, K=-1, Y=y>0, |R|=1.
    """
    if not np.isfinite(y) or y<=0:
        raise ValueError("y must be positive finite")
    return ReducedClosureState(
        rho=np.array([[1.0]],dtype=complex),
        K=np.array([[-1.0]],dtype=complex),
        Y=np.array([[float(y)]],dtype=complex),
        R=np.array([[np.exp(-1j*float(tau))]],dtype=complex),
        generation=0,
        metadata={"analytic_scalar_seed":True},
    )


def bounded_infinite_entry_contract() -> dict[str,Any]:
    """
    Source-level entry contract for the restricted infinite-dimensional reduction.

    The master runtime itself remains finite-dimensional after the first
    admissible reduction; this function records the mathematical input class.
    """
    return {
        "space":"separable Hilbert space",
        "K":"bounded self-adjoint",
        "Y":"bounded and Y >= m I for some m>0",
        "rho":"nonzero rank-one positive density d d*",
        "R":"bounded and power bounded",
        "peripheral_spectrum":"isolated",
        "peripheral_riesz_range":"finite-dimensional",
        "stable_complement":"spectral radius strictly below one",
        "consequence":(
            "the active support is finite-dimensional; one closure step reduces "
            "to the finite master profile, after which finite closure applies"
        ),
        "runtime_scope":"contract/documentation; no unbounded-operator engine",
    }
