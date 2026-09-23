from __future__ import annotations
import numpy as np

def hermitize(A: np.ndarray) -> np.ndarray:
    return 0.5 * (A + A.conj().T)

def psd_project(A: np.ndarray, floor: float = 0.0) -> np.ndarray:
    A = hermitize(A)
    vals, vecs = np.linalg.eigh(A)
    vals = np.maximum(vals.real, floor)
    return (vecs * vals) @ vecs.conj().T

def invsqrt_psd(A: np.ndarray, tol: float = 1e-12) -> np.ndarray:
    A = hermitize(A)
    vals, vecs = np.linalg.eigh(A)
    out = np.zeros_like(vals, dtype=float)
    mask = vals > tol
    out[mask] = 1.0 / np.sqrt(vals[mask])
    return (vecs * out) @ vecs.conj().T

def blockdiag2(A: np.ndarray) -> np.ndarray:
    z = np.zeros_like(A)
    return np.block([[A, z], [z, A]])

def g_norm_sq(x: np.ndarray, G: np.ndarray) -> float:
    return float(np.real(np.vdot(x, G @ x)))

def normalized_spectral_distance(A: np.ndarray, B: np.ndarray, eps: float = 1e-15) -> float:
    ea = np.sort(np.linalg.eigvalsh(hermitize(A)).real)
    eb = np.sort(np.linalg.eigvalsh(hermitize(B)).real)
    denom = max(float(np.linalg.norm(eb)), eps)
    return float(np.linalg.norm(ea - eb) / denom)

def fro_norm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, ord="fro"))


def power_boundedness_diagnostic(
    A: np.ndarray,
    unit_tol: float = 1e-8,
    grouping_tol: float = 1e-7,
    svd_rtol: float = 1e-9,
) -> dict:
    """
    Finite-dimensional diagnostic for the exact power-boundedness criterion:
    closed-unit-disk spectrum + semisimple unit-circle eigenvalues.
    """
    a=np.asarray(A,dtype=complex)
    if a.ndim!=2 or a.shape[0]!=a.shape[1]:
        raise ValueError("operator must be square")
    if not np.all(np.isfinite(a)):
        raise ValueError("operator contains non-finite values")

    eig=np.linalg.eigvals(a)
    mod=np.abs(eig)
    rho=float(np.max(mod)) if eig.size else 0.0
    unstable=int(np.sum(mod>1.0+unit_tol))

    per=eig[np.abs(mod-1.0)<=unit_tol]
    groups=[]
    for z in per:
        z=complex(z)
        placed=False
        for group in groups:
            center=sum(group)/len(group)
            if abs(z-center)<=grouping_tol*(1.0+abs(center)):
                group.append(z)
                placed=True
                break
        if not placed:
            groups.append([z])

    semisimple=True
    group_reports=[]
    n=a.shape[0]
    eye=np.eye(n,dtype=complex)
    for group in groups:
        rep=sum(group)/len(group)
        alg=len(group)
        s=np.linalg.svd(a-rep*eye,compute_uv=False)
        scale=max(float(s[0]) if s.size else 0.0,1.0)
        tol=svd_rtol*max(a.shape)*scale
        rank=int(np.sum(s>tol))
        geom=n-rank
        ok=geom>=alg
        semisimple=semisimple and ok
        group_reports.append({
            "real":float(np.real(rep)),
            "imag":float(np.imag(rep)),
            "algebraic_multiplicity":alg,
            "geometric_multiplicity":geom,
            "semisimple":bool(ok),
        })

    return {
        "power_bounded":bool(
            unstable==0 and semisimple and rho<=1.0+unit_tol
        ),
        "spectral_radius":rho,
        "unstable_count":unstable,
        "peripheral_count":int(len(per)),
        "semisimple_peripheral":bool(semisimple),
        "peripheral_groups":group_reports,
    }
