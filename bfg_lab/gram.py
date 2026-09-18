"""Finite BFG Gram rebuild for explicitly supplied reconstruction operators.

Does not infer B_C, W_N or L_C from a state. Numerical checks are not certificates.
"""
import numpy as np


def rebuild(b_c, w_n, l_c, *, tol=1e-10):
    """Return H=B*WB and Y=L*HL and neutral responses in Euclidean coordinates.

    B has shape (m,k), W (m,m), L (k,n); W must be Hermitian PSD.
    Tiny negative W eigenvalues within tol are explicitly clipped and reported.
    """
    if not np.isfinite(tol) or tol < 0:
        raise ValueError('tol must be finite and nonnegative')
    b, w, l = [np.asarray(a, dtype=complex) for a in (b_c, w_n, l_c)]
    if any(a.ndim != 2 or 0 in a.shape or not np.isfinite(a).all()
           for a in (b, w, l)):
        raise ValueError('Operators must be finite nonempty matrices')
    if w.shape != (b.shape[0], b.shape[0]) or l.shape[0] != b.shape[1]:
        raise ValueError('Incompatible operator domains')
    if not np.allclose(w, w.conj().T, atol=tol, rtol=0):
        raise ValueError('W_N must be Hermitian')
    values, vectors = np.linalg.eigh((w+w.conj().T)/2)
    if values.min() < -tol:
        raise ValueError('W_N must be positive semidefinite')
    root = np.sqrt(np.maximum(values, 0))[:, None] * vectors.conj().T
    k = root @ b
    h = k.conj().T @ k
    kl = k @ l
    y = kl.conj().T @ kl
    if not np.isfinite(h).all() or not np.isfinite(y).all():
        raise ValueError('Gram computation overflowed')
    eye = np.eye(l.shape[1])
    g = eye+y
    c = np.linalg.solve(g, eye)
    return dict(h=h, y=y, g=g, c=c, b=eye-c, z=2*c-eye,
                clipped_weight_eigenvalues=int(np.count_nonzero(values < 0)),
                weight_symmetrization_norm=float(np.linalg.norm(w-w.conj().T)/2))
