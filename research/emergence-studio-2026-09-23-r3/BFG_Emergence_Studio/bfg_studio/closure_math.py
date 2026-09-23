from __future__ import annotations

from dataclasses import dataclass, asdict
from fractions import Fraction
from typing import Any

import numpy as np


def _q(x: Any) -> Fraction:
    if isinstance(x, bool) or isinstance(x, float):
        raise ValueError(
            "exact certificates accept integers, rational strings, or Fraction; "
            "floating-point entries are not exact"
        )
    if isinstance(x, Fraction):
        return x
    if isinstance(x, (int, str)):
        try:
            return Fraction(x)
        except (ValueError, ZeroDivisionError) as exc:
            raise ValueError("invalid rational entry") from exc
    raise ValueError("unsupported exact scalar type")


def _qmatrix(a: Any, rows: int | None=None, cols: int | None=None):
    if not isinstance(a, (list, tuple)):
        raise ValueError("exact matrix must be a nested list/tuple")
    m=[list(row) for row in a]
    if rows is not None and len(m)!=rows:
        raise ValueError("wrong matrix row count")
    if len(m)==0:
        if rows not in (None,0):
            raise ValueError("wrong empty matrix dimensions")
        return []
    width=len(m[0])
    if any(len(row)!=width for row in m):
        raise ValueError("ragged exact matrix")
    if cols is not None and width!=cols:
        raise ValueError("wrong matrix column count")
    return [[_q(x) for x in row] for row in m]


def _eye(n:int):
    return [
        [Fraction(int(i==j)) for j in range(n)]
        for i in range(n)
    ]


def _transpose(a):
    if not a:
        return []
    return [list(col) for col in zip(*a)]


def _mul(a,b):
    if not a:
        return []
    if not b:
        if len(a[0])==0:
            return [[] for _ in a]
        raise ValueError("incompatible empty exact matrix product")
    if len(a[0])!=len(b):
        raise ValueError("incompatible exact matrix product")
    bt=_transpose(b)
    return [
        [
            sum((x*y for x,y in zip(row,col)),Fraction(0))
            for col in bt
        ]
        for row in a
    ]


def _sub(a,b):
    if len(a)!=len(b) or any(len(x)!=len(y) for x,y in zip(a,b)):
        raise ValueError("incompatible exact matrix subtraction")
    return [
        [x-y for x,y in zip(ra,rb)]
        for ra,rb in zip(a,b)
    ]


def _inverse(a):
    n=len(a)
    if n==0 or any(len(row)!=n for row in a):
        raise ValueError("exact inverse requires a nonempty square matrix")
    aug=[
        list(row)+[
            Fraction(int(i==j)) for j in range(n)
        ]
        for i,row in enumerate(a)
    ]
    for col in range(n):
        pivot=next(
            (r for r in range(col,n) if aug[r][col]!=0),
            None,
        )
        if pivot is None:
            raise ValueError("singular supplied basis")
        aug[col],aug[pivot]=aug[pivot],aug[col]
        scale=aug[col][col]
        aug[col]=[x/scale for x in aug[col]]
        for r in range(n):
            if r==col:
                continue
            factor=aug[r][col]
            if factor:
                aug[r]=[
                    x-factor*y
                    for x,y in zip(aug[r],aug[col])
                ]
    return [row[n:] for row in aug]


def _symmetric_positive_definite(a) -> bool:
    n=len(a)
    if n==0:
        return True
    if any(len(row)!=n for row in a):
        return False
    if a!=_transpose(a):
        return False
    # Exact LDL^T factorization without square roots.
    L=[[Fraction(0) for _ in range(n)] for _ in range(n)]
    D=[Fraction(0) for _ in range(n)]
    for i in range(n):
        diag=a[i][i]-sum(
            (L[i][k]*L[i][k]*D[k] for k in range(i)),
            Fraction(0),
        )
        if diag<=0:
            return False
        D[i]=diag
        L[i][i]=Fraction(1)
        for j in range(i+1,n):
            numerator=a[j][i]-sum(
                (
                    L[j][k]*L[i][k]*D[k]
                    for k in range(i)
                ),
                Fraction(0),
            )
            L[j][i]=numerator/D[i]
    return True


def _block(matrix,r0,r1,c0,c1):
    return [row[c0:c1] for row in matrix[r0:r1]]


def _as_strings(a):
    return [[str(x) for x in row] for row in a]


@dataclass(frozen=True)
class ExactRecursiveCertificate:
    status: str
    dimension: int
    persistent_dimension: int
    stable_dimension: int
    persistent_isometry_verified: bool
    stable_lyapunov_verified: bool
    invariant_split_verified: bool
    spectral_projector: tuple[tuple[str,...],...]
    coordinate_transport: tuple[tuple[str,...],...]

    def to_dict(self):
        return asdict(self)


def verify_exact_recursive_certificate(
    r,
    basis,
    persistent_dimension:int,
    persistent_metric,
    stable_metric,
) -> ExactRecursiveCertificate:
    """
    Exact finite-dimensional nonnormal persistence certificate.

    The caller supplies a rational invariant splitting S and rational positive
    metrics M,N satisfying:

        S^-1 R S = diag(A,T)
        A^T M A = M
        N - T^T N T > 0

    A successful certificate proves power-boundedness for this supplied R.
    Failure of a supplied certificate does not prove instability or nonexistence
    of another certificate.
    """
    if isinstance(persistent_dimension,bool) or not isinstance(
        persistent_dimension,int
    ):
        raise ValueError("persistent_dimension must be an integer")

    if not isinstance(r,(list,tuple)) or len(r)==0:
        raise ValueError("R must be a nonempty exact matrix")
    n=len(r)
    R=_qmatrix(r,n,n)
    S=_qmatrix(basis,n,n)
    p=persistent_dimension
    if not 0<=p<=n:
        raise ValueError("invalid persistent dimension")

    M=_qmatrix(persistent_metric,p,p) if p else []
    N=_qmatrix(stable_metric,n-p,n-p) if p<n else []

    Sinv=_inverse(S)
    transformed=_mul(_mul(Sinv,R),S)

    for i in range(n):
        for j in range(n):
            if (i<p)!=(j<p) and transformed[i][j]!=0:
                raise ValueError(
                    "supplied persistent/stable subspaces are not invariant"
                )

    persistent_ok=True
    if p:
        A=_block(transformed,0,p,0,p)
        if not _symmetric_positive_definite(M):
            raise ValueError("persistent metric is not positive definite")
        if _mul(_mul(_transpose(A),M),A)!=M:
            raise ValueError(
                "persistent block is not isometric in supplied metric"
            )

    stable_ok=True
    if p<n:
        T=_block(transformed,p,n,p,n)
        if not _symmetric_positive_definite(N):
            raise ValueError("stable metric is not positive definite")
        propagated=_mul(_mul(_transpose(T),N),T)
        defect=_sub(N,propagated)
        if not _symmetric_positive_definite(defect):
            raise ValueError(
                "stable block lacks a strict Lyapunov certificate"
            )

    D=[
        [
            Fraction(int(i==j and i<p))
            for j in range(n)
        ]
        for i in range(n)
    ]
    projector=_mul(_mul(S,D),Sinv)

    return ExactRecursiveCertificate(
        status="certified",
        dimension=n,
        persistent_dimension=p,
        stable_dimension=n-p,
        persistent_isometry_verified=persistent_ok,
        stable_lyapunov_verified=stable_ok,
        invariant_split_verified=True,
        spectral_projector=tuple(
            tuple(str(x) for x in row) for row in projector
        ),
        coordinate_transport=tuple(
            tuple(str(x) for x in row) for row in transformed
        ),
    )


def gram_rebuild_from_supplied_factors(
    b_c,
    w_n,
    l_c,
    *,
    tol:float=1e-10,
):
    """
    Finite Gram rebuild from explicitly supplied B_C, W_N and L_C.

    It deliberately does not infer those upstream factors from a BFG state.
    """
    if not np.isfinite(tol) or tol<0:
        raise ValueError("tol must be finite and nonnegative")
    b=np.asarray(b_c,dtype=complex)
    w=np.asarray(w_n,dtype=complex)
    l=np.asarray(l_c,dtype=complex)
    if any(
        x.ndim!=2 or 0 in x.shape or not np.isfinite(x).all()
        for x in (b,w,l)
    ):
        raise ValueError("operators must be finite nonempty matrices")
    if w.shape!=(b.shape[0],b.shape[0]):
        raise ValueError("W_N and B_C domains do not match")
    if l.shape[0]!=b.shape[1]:
        raise ValueError("L_C and B_C domains do not match")
    if not np.allclose(w,w.conj().T,atol=tol,rtol=0):
        raise ValueError("W_N must be Hermitian")

    wh=0.5*(w+w.conj().T)
    vals,vecs=np.linalg.eigh(wh)
    if float(vals.min()) < -tol:
        raise ValueError("W_N must be positive semidefinite")
    vals_clip=np.maximum(vals,0.0)
    root=np.diag(np.sqrt(vals_clip))@vecs.conj().T

    weighted_b=root@b
    h=weighted_b.conj().T@weighted_b
    weighted_bl=weighted_b@l
    y=weighted_bl.conj().T@weighted_bl

    eye=np.eye(l.shape[1],dtype=complex)
    g=eye+y
    c=np.linalg.solve(g,eye)
    return {
        "H":h,
        "Y":y,
        "G":g,
        "C_N":c,
        "B_N":eye-c,
        "Z":2*c-eye,
        "clipped_weight_eigenvalues":
            int(np.count_nonzero(vals<0)),
        "weight_hermitian_residual":
            float(np.linalg.norm(w-w.conj().T,2)),
    }


def retained_channel_gram_decomposition(
    b_doubled,
    support_basis,
    *,
    tol:float=1e-10,
):
    """
    Exact finite-dimensional identity in floating implementation coordinates:

        B_tan = U^* B2 U
        E     = (I-UU^*) B2 U

        U^* B2^* B2 U = B_tan^* B_tan + E^* E.

    This recovers the restricted Gram energy bookkeeping. It does not recover the
    direction of discarded channels or a future transport law.
    """
    b=np.asarray(b_doubled,dtype=complex)
    u=np.asarray(support_basis,dtype=complex)
    if b.ndim!=2 or b.shape[0]!=b.shape[1]:
        raise ValueError("b_doubled must be square")
    if u.ndim!=2 or u.shape[0]!=b.shape[0] or u.shape[1]==0:
        raise ValueError("support_basis has incompatible shape")
    eye_small=np.eye(u.shape[1],dtype=complex)
    orth_res=float(np.linalg.norm(u.conj().T@u-eye_small,2))
    if orth_res>tol:
        raise ValueError("support_basis must have orthonormal columns")

    p=u@u.conj().T
    b_tan=u.conj().T@b@u
    external=(np.eye(b.shape[0])-p)@b@u

    restricted=u.conj().T@b.conj().T@b@u
    reconstructed=(
        b_tan.conj().T@b_tan
        + external.conj().T@external
    )
    delta=external.conj().T@external
    residual=float(np.linalg.norm(restricted-reconstructed,2))

    return {
        "B_tangent":b_tan,
        "E_external":external,
        "Delta_external_gram":delta,
        "restricted_gram":restricted,
        "reconstructed_gram":reconstructed,
        "identity_residual":residual,
        "external_rank":int(np.linalg.matrix_rank(delta,tol)),
        "interpretation":{
            "gram_energy_recovered":bool(residual<=10*tol),
            "external_direction_recovered":False,
            "future_dynamics_recovered":False,
        },
    }


def g1_inherited_load(
    y,
    support_basis,
    *,
    tol:float=1e-10,
):
    r"""
    Conditional G1 proposal:
        Y_next = U^* (Y \oplus Y) U.

    This is an additional closure postulate unless its intertwining hypotheses
    are independently established.
    """
    y=np.asarray(y,dtype=complex)
    u=np.asarray(support_basis,dtype=complex)
    if y.ndim!=2 or y.shape[0]!=y.shape[1]:
        raise ValueError("Y must be square")
    y2=np.kron(np.eye(2,dtype=complex),y)
    if u.ndim!=2 or u.shape[0]!=y2.shape[0]:
        raise ValueError("support_basis must live in the doubled carrier")
    if np.linalg.norm(u.conj().T@u-np.eye(u.shape[1]),2)>tol:
        raise ValueError("support_basis must be orthonormal")
    result=u.conj().T@y2@u
    return 0.5*(result+result.conj().T)


def g1_intertwining_audit(
    b2,
    w2,
    l2,
    u,
    b_next,
    w_next,
    l_next,
    *,
    tol:float=1e-10,
):
    """
    Audit the explicit sufficient intertwining conditions for deriving G1.
    """
    b2,w2,l2,u,bn,wn,ln=[
        np.asarray(x,dtype=complex)
        for x in (b2,w2,l2,u,b_next,w_next,l_next)
    ]
    residuals={
        "B_intertwining":
            float(np.linalg.norm(b2@u-u@bn,2)),
        "L_intertwining":
            float(np.linalg.norm(l2@u-u@ln,2)),
        "W_compression":
            float(np.linalg.norm(wn-u.conj().T@w2@u,2)),
    }
    y_old=l2.conj().T@b2.conj().T@w2@b2@l2
    y_new=ln.conj().T@bn.conj().T@wn@bn@ln
    y_compressed=u.conj().T@y_old@u
    residuals["G1_load"]=float(np.linalg.norm(y_new-y_compressed,2))
    return {
        "residuals":residuals,
        "intertwining_satisfied":bool(
            all(v<=10*tol for v in residuals.values())
        ),
        "claim_scope":
            "sufficient conditional compatibility; not a universal BFG law",
    }


@dataclass(frozen=True)
class M3ConnectionState:
    connection: np.ndarray
    difference: np.ndarray
    coherence: np.ndarray
    neutral: np.ndarray
    packet: np.ndarray


def m3_operators(
    state:M3ConnectionState,
    *,
    tol:float=1e-10,
):
    """
    Experimental finite M3 upstream connection model.

    Assumptions:
      D_cov(c)=[A,c], W_N=I, L_C=I,
      R=(I-A)^-1(I+A), with A skew-Hermitian.

    This is a complete operator packet under additional assumptions, not a
    derivation of the universal BFG reconstruction map.
    """
    a=np.asarray(state.connection,dtype=complex)
    c=np.asarray(state.coherence,dtype=complex)
    dcap=np.asarray(state.difference,dtype=complex)
    ncap=np.asarray(state.neutral,dtype=complex)
    packet=np.asarray(state.packet,dtype=complex)

    if a.ndim!=2 or a.shape[0]!=a.shape[1]:
        raise ValueError("connection must be square")
    n=a.shape[0]
    if c.shape!=(n,n) or dcap.shape!=(n,n) or ncap.shape!=(n,n):
        raise ValueError("M3 capacities must match connection dimension")
    if packet.shape not in ((n,),(n,1)):
        raise ValueError("M3 packet has wrong dimension")
    if not np.allclose(a+a.conj().T,0,atol=tol,rtol=0):
        raise ValueError("M3 connection must be skew-Hermitian")

    a=0.5*(a-a.conj().T)
    capacities={}
    for name,q in (
        ("difference",dcap),
        ("coherence",c),
        ("neutral",ncap),
    ):
        qh=0.5*(q+q.conj().T)
        if np.linalg.norm(q-q.conj().T,2)>tol:
            raise ValueError(f"M3 {name} capacity must be Hermitian")
        if float(np.min(np.linalg.eigvalsh(qh))) < -tol:
            raise ValueError(f"M3 {name} capacity must be positive")
        capacities[name]=qh

    c=capacities["coherence"]
    b_c=a@c-c@a
    gram=gram_rebuild_from_supplied_factors(
        b_c,
        np.eye(n,dtype=complex),
        np.eye(n,dtype=complex),
        tol=tol,
    )
    eye=np.eye(n,dtype=complex)
    r=np.linalg.solve(eye-a,eye+a)
    unitarity=float(np.linalg.norm(r.conj().T@r-eye,2))

    return {
        "connection":a,
        "B_C":b_c,
        "Y":gram["Y"],
        "C_N":gram["C_N"],
        "R_C":r,
        "unitarity_residual":unitarity,
        "power_bounded_by_construction":bool(unitarity<=100*tol),
        "claim_scope":
            "finite M3 model under explicit additional connection assumptions",
    }
