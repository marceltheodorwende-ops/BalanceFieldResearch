"""V4 neutral split, metric projection and polar support transport.

Numerical tolerances are explicit computational conventions, not BFG axioms.
Persistence uses the peripheral spectral interpretation of Eq. 27; see docs.
"""
import numpy as np

TOL = 1e-10


def hermitian(a):
    a = np.asarray(a, dtype=complex)
    if a.ndim != 2 or a.shape[0] != a.shape[1] or not len(a):
        raise ValueError("Expected a nonempty square matrix")
    if not np.isfinite(a).all() or not np.allclose(a, a.conj().T, atol=TOL, rtol=0):
        raise ValueError("Expected a finite Hermitian matrix")
    return a


def neutral(y):
    y = hermitian(y)
    if np.linalg.eigvalsh(y).min() < -TOL:
        raise ValueError("Load must be positive semidefinite")
    eye = np.eye(len(y))
    c = np.linalg.solve(eye + y, eye)
    b = eye - c
    return c, b, c - b


def persistent_basis(r, tol=TOL):
    """Restricted to normal, power-bounded matrices (no nonnormal claims)."""
    r = np.asarray(r, dtype=complex)
    if r.ndim != 2 or r.shape[0] != r.shape[1] or not len(r) or not np.isfinite(r).all():
        raise ValueError("Expected a finite nonempty square transport")
    if not np.allclose(r.conj().T @ r, r @ r.conj().T, atol=tol, rtol=0):
        raise ValueError("This initial implementation supports normal transport only")
    values, vectors = np.linalg.eig(r)
    if np.max(np.abs(values)) > 1 + tol:
        raise ValueError("Transport is not power bounded")
    mask = np.abs(np.abs(values) - 1) <= tol
    w = vectors[:, mask]
    if w.shape[1]:
        w, _ = np.linalg.qr(w)
    return w


def metric_projector(w, g):
    g = hermitian(g)
    w = np.asarray(w, dtype=complex)
    if np.linalg.eigvalsh(g).min() <= 0:
        raise ValueError("Metric must be positive definite")
    if w.ndim != 2 or w.shape[0] != len(g) or not np.isfinite(w).all():
        raise ValueError("Invalid basis shape or values")
    if not w.shape[1]:
        return np.zeros_like(g)
    if np.linalg.matrix_rank(w, tol=TOL) != w.shape[1]:
        raise ValueError("Basis must have independent columns")
    return w @ np.linalg.solve(w.conj().T @ g @ w, w.conj().T @ g)


def split(y, d, w):
    y = hermitian(y)
    c, b, z = neutral(y)
    d = np.asarray(d, dtype=complex)
    if d.shape != (len(y),) or not np.isfinite(d).all():
        raise ValueError("State must be a finite vector matching the load")
    g = np.eye(len(y)) + y
    p = metric_projector(w, g)
    keep, up = p @ c @ d, p @ b @ d
    lk = max(0., float(np.vdot(keep, g @ keep).real))
    lu = max(0., float(np.vdot(up, g @ up).real))
    if min(lk, lu) <= TOL:
        return {"status": "no_dual_support", "loads": [lk, lu]}
    weights = np.array([lu, lk]) / (lk + lu)
    a = np.vstack([np.sqrt(weights[0]) * p @ c, np.sqrt(weights[1]) * p @ b])
    compact = .5 * np.vstack([np.sqrt(weights[0]) * p @ (np.eye(len(y)) + z),
                              np.sqrt(weights[1]) * p @ (np.eye(len(y)) - z)])
    packet = a @ d
    u, s, vh = np.linalg.svd(a, full_matrices=False)
    active = s > TOL
    j = u[:, active] @ vh[active, :]
    norm2 = float(np.vdot(d, g @ d).real)
    gain = np.sqrt(2 * lk * lu / ((lk + lu) * norm2))
    return dict(status="ok", loads=[lk, lu], weights=weights, packet=packet,
                analysis=a, compact=compact, polar=j, projector=p, gain=float(gain))
