"""Explicit finite conditional BFG completion, not a uniquely derived universal law.

The state uses a rank-one positive profile operator to remove eigenvector phase.
Floating-point admissibility is diagnostic, not an exact spectral certificate.
"""
from dataclasses import dataclass
import numpy as np
from scipy.linalg import schur, solve_sylvester


class NumericalAmbiguity(ValueError):
    """A spectral decision is not reliable at the declared numerical scale."""


@dataclass
class State:
    rho: np.ndarray
    K: np.ndarray
    Y: np.ndarray
    R: np.ndarray


@dataclass
class Outcome:
    state: State | None
    reason: str
    diagnostics: dict


def hermitian(a):
    return (a + a.conj().T) / 2


def gram_factors(y):
    """An explicit positive-square-root gauge for this model, not a forced law."""
    vals, basis = np.linalg.eigh(y)
    if vals.min() <= 0:
        raise ValueError('positive definite load required')
    root = (basis*np.sqrt(vals))@basis.conj().T
    eye = np.eye(len(y), dtype=complex)
    return {'B_C': root, 'W_N': eye, 'L_C': eye, 'D_K': eye, 'F': root}


def validate(state):
    arrays = [np.asarray(getattr(state, key), complex) for key in ('rho', 'K', 'Y', 'R')]
    n = arrays[0].shape[0] if arrays[0].ndim == 2 else 0
    if not n or any(a.shape != (n, n) or not np.isfinite(a).all() for a in arrays):
        raise ValueError('finite nonempty equally sized square matrices required')
    rho, k, y, r = arrays
    for name, a in zip(('rho', 'K', 'Y'), arrays[:3]):
        if np.linalg.norm(a-a.conj().T) > 1e-10 * max(1., np.linalg.norm(a)):
            raise ValueError(name + ' must be Hermitian; input is not silently symmetrized')
    rho, k, y = map(hermitian, (rho, k, y))
    yr = np.linalg.eigvalsh(y)
    if yr.min() <= 0:
        raise ValueError('this completion requires strictly positive Y')
    if yr.min() <= 1e-12 * max(1., yr.max()):
        raise NumericalAmbiguity('positive load is numerically unresolved')
    rv = np.linalg.eigvalsh(rho)
    scale = max(1., float(rv.max()))
    if rv.min() < -1e-10*scale or np.count_nonzero(rv > 1e-10*scale) != 1:
        raise ValueError('rho must be nonzero positive rank one')
    return State(rho, k, y, r)


def persistent_projectors(r, g):
    """Numerical finite peripheral extraction, allowing stable Jordan blocks.

    Return the Riesz and graph-metric projectors separately. Reject clear growth,
    ill-conditioned peripheral eigenbases and the near-unit ambiguity band.
    """
    n = len(r)
    unit_tol = 100*np.finfo(float).eps*max(1., np.linalg.norm(r))*n
    if unit_tol >= 1e-8:
        raise NumericalAmbiguity('operator scale prevents reliable peripheral classification')
    values = np.linalg.eigvals(r)
    distance = np.abs(np.abs(values)-1)
    if np.any(np.abs(values) > 1+1e-8):
        raise ValueError('growing recursion is not power bounded')
    if np.any((distance > unit_tol) & (distance <= 1e-8)):
        raise NumericalAmbiguity('near-unit eigenvalue needs an exact separation certificate')
    t, z, rank = schur(r, output='complex', sort=lambda v: abs(abs(v)-1) <= unit_tol)
    if rank == 0:
        return np.zeros_like(r), np.zeros_like(r), 0
    tp = t[:rank, :rank]
    _, eigenvectors = np.linalg.eig(tp)
    sv = np.linalg.svd(eigenvectors, compute_uv=False)
    if sv[-1] <= 1e-8*sv[0]:
        raise NumericalAmbiguity('defective or unresolved peripheral eigenspace')
    w = z[:, :rank]
    pg = w@np.linalg.solve(w.conj().T@g@w, w.conj().T@g)
    es = np.zeros_like(r); es[:rank, :rank] = np.eye(rank)
    if rank < n:
        es[:rank, rank:] = solve_sylvester(tp, -t[rank:, rank:], t[:rank, rank:])
    e = z@es@z.conj().T
    if np.linalg.norm(e@r-r@e) > 1e-8*max(1., np.linalg.norm(e)*np.linalg.norm(r)):
        raise NumericalAmbiguity('spectral projector residual too large')
    return e, pg, rank


def advance(state, tau=1.0):
    """One explicit model step; None is the absorbing mathematical terminal state.

    Invalid input/numerical ambiguity raises rather than masquerading as physical
    termination. tau is a declared model parameter, not a fitted internal law.
    """
    if not np.isfinite(tau):
        raise ValueError('finite tau required')
    if state is None:
        return Outcome(None, 'absorbing terminal', {})
    s = validate(state); n = len(s.K); eye = np.eye(n)
    g = eye+s.Y
    e, p, rank = persistent_projectors(s.R, g)
    diagnostics = {'peripheral_rank': rank, 'numerical_admission_only': True,
                   'riesz_commutator': float(np.linalg.norm(e@s.R-s.R@e)),
                   'projector_difference': float(np.linalg.norm(e-p))}
    if rank == 0:
        return Outcome(None, 'empty persistent support', diagnostics)
    c = np.linalg.solve(eye+s.Y, eye); b = s.Y@c
    keep = p@c; up = p@b
    lk = float(np.trace(g@keep@s.rho@keep.conj().T).real)
    lu = float(np.trace(g@up@s.rho@up.conj().T).real)
    if min(lk, lu) < -1e-10:
        raise NumericalAmbiguity('negative computed channel norm')
    if min(lk, lu) <= 1e-12:
        # Exact zero terminates; small floating values cannot certify exact zero.
        if lk == 0. or lu == 0.:
            return Outcome(None, 'zero dual load', diagnostics)
        raise NumericalAmbiguity('dual load near zero')
    alpha = lu/(lk+lu); beta = lk/(lk+lu)
    a = np.vstack((np.sqrt(alpha)*keep, np.sqrt(beta)*up))
    u, singular, vh = np.linalg.svd(a, full_matrices=False)
    threshold = 1e-11*max(1., singular[0])
    active = singular > threshold
    if not np.any(active):
        raise NumericalAmbiguity('unresolved active support')
    v = vh[active, :].conj().T
    # On active input coordinates the polar isometry is u[:, active].
    j_active = u[:, active]
    k_next = hermitian(j_active.conj().T@np.kron(np.eye(2), s.K)@j_active)
    # Chosen law: intrinsic input Gram, restricted to the active carrier.
    y_next = hermitian(v.conj().T@a.conj().T@a@v)
    vals, basis = np.linalg.eigh(k_next)
    if vals[0] >= 0:
        return Outcome(None, 'no negative formation mode', diagnostics)
    if abs(vals[0]) < 1e-10:
        raise NumericalAmbiguity('ground eigenvalue near zero')
    if len(vals)>1 and vals[1]-vals[0] <= 1e-9:
        raise NumericalAmbiguity('degenerate or unresolved ground eigenspace')
    ground = basis[:, 0]
    rho_next = -vals[0]*np.outer(ground, ground.conj())
    r_next = (basis*np.exp(1j*tau*vals))@basis.conj().T
    next_state = validate(State(rho_next, k_next, y_next, r_next))
    diagnostics.update({'alpha': alpha, 'beta': beta,
        'real_polarity_claimed': False, 'formation_output': 'phase-orbit density',
        'min_next_load': float(np.linalg.eigvalsh(y_next).min()),
        'next_unitarity_residual': float(np.linalg.norm(r_next.conj().T@r_next-np.eye(len(vals)))),
        'support_load_commutator': float(np.linalg.norm(p@s.Y-s.Y@p))})
    return Outcome(next_state, 'formed', diagnostics)
