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
