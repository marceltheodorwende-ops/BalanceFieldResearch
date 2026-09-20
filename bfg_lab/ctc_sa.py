"""Separate CTC-SA reference, not the universal BFG engine.

Rational supplied-splitting certificates are exact. SA matrix calculations use
NumPy and an explicit resolution tolerance; they are not exact certificates.
Invalid/unresolved numerical data raise ValueError, never mathematical bottom.
"""
from dataclasses import dataclass
import json
import numpy as np
from . import persistence_certificate as certificate


TOL = 1e-10


def projectors_from_certificate(r, basis, persistent_dimension,
                               persistent_metric, stable_metric, graph_metric):
    """Exact real-rational Riesz and graph-orthogonal projectors.

    Reuses the existing invariant-splitting certificate, including its exact
    matrix arithmetic. Does not discover a splitting or certify arbitrary R.
    An empty stable block is allowed; an empty persistent block is rejected.
    """
    result = certificate.verify(r, basis, persistent_dimension,
                                persistent_metric, stable_metric)
    if persistent_dimension == 0:
        raise ValueError('No peripheral witness space')
    n = len(r)
    g = certificate._square(graph_metric, n)
    if not certificate._positive(g):
        raise ValueError('Graph metric must be symmetric positive definite')
    s = certificate._square(basis, n)
    z = [row[:persistent_dimension] for row in s]
    ztg = certificate._mul(certificate._transpose(z), g)
    metric_projector = certificate._mul(
        certificate._mul(z, certificate._inverse(certificate._mul(ztg, z))), ztg)
    return {**result, 'metric_projector': metric_projector,
            'scope': 'exact supplied real-rational certificate'}


@dataclass(frozen=True)
class State:
    """Primitive data. Y, R_C and reconstruction factors are derived only."""
    difference: np.ndarray
    coherence: np.ndarray
    neutral: np.ndarray
    d: np.ndarray
    eta: float


def _matrix(value, n, name):
    try:
        a = np.array(value, dtype=complex, copy=True)
    except (TypeError, ValueError) as exc:
        raise ValueError(f'{name}: invalid matrix') from exc
    if a.shape != (n, n) or not np.isfinite(a).all():
        raise ValueError(f'{name}: expected finite {n} by {n} matrix')
    if np.linalg.norm(a-a.conj().T) > TOL*max(1., np.linalg.norm(a)):
        raise ValueError(f'{name}: not Hermitian within tolerance')
    return (a+a.conj().T)/2


def operators(state):
    """Validate the numerical SA class and return derived matrices.

    Eigenvalues within TOL of a boundary or components below relative TOL
    are unresolved and rejected. No state projection or fitted repair occurs.
    """
    if not isinstance(state, State):
        raise ValueError('Expected State')
    d = np.array(state.d, dtype=complex, copy=True)
    if d.ndim != 1 or len(d) < 2 or not np.isfinite(d).all():
        raise ValueError('Difference vector must be finite with dimension >=2')
    n = len(d)
    if not np.isscalar(state.eta) or np.iscomplexobj(state.eta):
        raise ValueError('eta must be a positive finite real scalar')
    eta = float(state.eta)
    if not np.isfinite(eta) or eta <= 0:
        raise ValueError('eta must be a positive finite real scalar')
    caps = [_matrix(a, n, label) for a, label in
            zip((state.difference,state.coherence,state.neutral),
                ('difference','coherence','neutral'))]
    for i in range(3):
        for j in range(i):
            if np.linalg.norm(caps[i]@caps[j]-caps[j]@caps[i]) > TOL*max(
                    1., np.linalg.norm(caps[i])*np.linalg.norm(caps[j])):
                raise ValueError('Capacities do not commute within tolerance')
    coherence = caps[1]
    if np.linalg.eigvalsh(coherence).min() <= TOL*max(1., np.linalg.norm(coherence, 2)):
        raise ValueError('Coherence is not resolvably positive definite')
    k = coherence+caps[2]-caps[0]
    eigenvalues, eigenvectors = np.linalg.eigh(k)
    margin = TOL*max(1., float(np.max(np.abs(eigenvalues))))
    if (eigenvalues[0] >= -margin or eigenvalues[1] <= margin or
            np.any(np.diff(eigenvalues) <= margin)):
        raise ValueError('Formation spectrum must be simple: lambda1<0<lambda2<...')
    norm = np.linalg.norm(d)
    if not np.isfinite(norm) or norm == 0 or np.any(
            np.abs(eigenvectors.conj().T@d) <= TOL*norm):
        raise ValueError('Difference vector lacks resolvable full spectral support')
    z = eigenvectors[:, :-1]
    p = z@z.conj().T
    r = float((eigenvalues[-2]-eigenvalues[0])/(eigenvalues[-1]-eigenvalues[0]))
    identity = np.eye(n)
    dcov = np.sqrt(eta)*np.linalg.solve(coherence, identity)
    b = dcov@coherence
    return dict(d=d, eta=eta, capacities=caps, formation=k, eigenvalues=eigenvalues,
                basis=z, spectral_projector=p, metric_projector=p.copy(),
                r=r, recursion=p+r*(identity-p), persistence_gap=1-r,
                d_cov=dcov, b_c=b, w_n=identity, l_c=identity, n_r=identity,
                gram_from_factors=b.conj().T@b, y=eta*identity, g=(1+eta)*identity)


def advance(state):
    """One SA step; None denotes the explicit absorbing terminal state.

    The d=2 stop is a CTC policy, NOT the historical formation_gate behavior.
    Successful next states are expressed in orthonormal range coordinates.
    """
    if state is None:
        return None, {'status': 'terminal', 'reason': 'absorbing'}
    o = operators(state)
    n, eta, d = len(o['d']), o['eta'], o['d']
    if n == 2:
        return None, {'status': 'terminal', 'reason': 'ctc_dimension_floor', 'dimension': n}
    try:
        with np.errstate(over='raise', divide='raise', invalid='raise', under='ignore'):
            # hypot avoids forming eta**2; no clipping of a or eta_next.
            a = (eta/(1+eta))/np.hypot(1, eta)
            p, z = o['metric_projector'], o['basis']
            norm2 = float(np.vdot(d,d).real)
            pd = p@d
            t = float(np.vdot(pd,pd).real)/norm2
            eta_next = 2*a*a*t
            if not np.isfinite(eta_next) or eta_next <= 0:
                raise ValueError('Numerical resolution failure in eta_next')
            analysis = a*np.vstack((p,p))
            j = np.vstack((p,p))/np.sqrt(2)
            range_basis = np.vstack((z,z))/np.sqrt(2)
            packet = analysis@d
            caps_next = [range_basis.conj().T@np.kron(np.eye(2),cap)@range_basis
                         for cap in o['capacities']]
            d_next = range_basis.conj().T@packet/(1+eta_next)
            nxt = State(*caps_next, d_next, eta_next)
            no = operators(nxt)
            energy = (1+eta)*norm2
            energy_next = (1+eta_next)*float(np.vdot(d_next,d_next).real)
            ratio = energy_next/energy
            if not np.isfinite(ratio) or ratio >= .2:
                raise ValueError('Numerical energy invariant failed')
            projected_norm2=float(np.vdot(pd,pd).real)
            loads=[projected_norm2/(1+eta), (eta/(1+eta))*eta*projected_norm2]
            if not all(np.isfinite(x) and x>0 for x in loads):
                raise ValueError('Numerical resolution failure in branch loads')
    except (FloatingPointError, OverflowError, np.linalg.LinAlgError) as exc:
        raise ValueError('Numerical resolution failure; not mathematical termination') from exc
    return nxt, dict(status='advanced', dimension=n, next_dimension=n-1,
                     eta=eta, eta_next=eta_next, energy=energy, energy_next=energy_next,
                     energy_ratio=ratio, loads=loads, persistence_gap=o['persistence_gap'],
                     formation_gap=float(no['eigenvalues'][1]-no['eigenvalues'][0]),
                     gram_inheritance_defect=abs(eta-eta_next), analysis=analysis,
                     polar=j, initial_projector=j.conj().T@j, range_projector=j@j.conj().T,
                     range_basis=range_basis, tolerance=TOL,
                     scope='floating-point finite SA model, not empirical validation')


def seed(dimension=5):
    if isinstance(dimension, bool) or not isinstance(dimension,int) or dimension<2:
        raise ValueError('Seed dimension must be an integer >=2')
    return State(np.diag([3.]+[1.]*(dimension-1)),
                 np.diag(np.arange(1,dimension+1,dtype=float)),
                 np.eye(dimension), np.ones(dimension), 1.)


def main():
    state=seed()
    history=[]
    while state is not None:
        state, report=advance(state)
        history.append({k:v for k,v in report.items() if not isinstance(v,np.ndarray)})
    print(json.dumps({'model':'CTC-SA reference','history':history},indent=2))


if __name__ == '__main__':
    main()
