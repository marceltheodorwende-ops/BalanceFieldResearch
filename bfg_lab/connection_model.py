"""Experimental finite connection closure M3, not a universal BFG derivation."""
import numpy as np
from .core import TOL, hermitian
from .formation import prepare_candidate
from .gram import rebuild


def operators(state):
    """M3 assumptions: D_cov c=[A,c], W=L=I, R=Cayley(A)."""
    c = hermitian(state['coherence'])
    n = len(c)
    for key in ('difference', 'neutral', 'coherence'):
        q = hermitian(state[key])
        if q.shape != (n,n) or np.linalg.eigvalsh(q).min() < -TOL:
            raise ValueError('M3 requires matching positive capacities')
    a = np.asarray(state['connection'], dtype=complex)
    if a.shape != (n,n) or not np.isfinite(a).all():
        raise ValueError('Invalid connection')
    if not np.allclose(a+a.conj().T, 0, atol=TOL, rtol=0):
        raise ValueError('M3 connection must be skew-Hermitian')
    # Explicit roundoff symmetrization; exact model assumes skew-Hermitian A.
    a = (a-a.conj().T)/2
    b = a@c-c@a
    eye = np.eye(n)
    gram = rebuild(b, eye, eye)
    r = np.linalg.solve(eye-a, eye+a)
    return dict(connection=a, b_c=b, y=gram['y'], r=r, c_n=gram['c'])


def advance(state):
    """Return a full M3 next state or an explicitly reported gate rejection.

    None is absorbing. This model discards off-support connection information;
    it rebuilds from compressed fields rather than claiming G1 inheritance.
    """
    if state is None:
        return None, {'status': 'terminal'}
    op = operators(state)
    cand = prepare_candidate(op['y'], state['d'], op['r'],
                             state['difference'], state['coherence'], state['neutral'])
    report = dict(status=cand['status'], gate=cand['gate'])
    if not cand['gate']['passed']:
        return None, report
    t = cand['transport']
    u = t['basis']
    an = u.conj().T @ np.kron(np.eye(2),op['connection']) @ u
    next_state = dict(connection=(an-an.conj().T)/2,
                      difference=t['difference'], coherence=t['coherence'],
                      neutral=t['neutral'])
    newop = operators(next_state)
    next_state['d'] = newop['c_n'] @ cand['support_packet']
    inherited_y = u.conj().T @ np.kron(np.eye(2),op['y']) @ u
    compressed_b = u.conj().T @ np.kron(np.eye(2),op['b_c']) @ u
    report.update(g1_discrepancy=float(np.linalg.norm(newop['y']-inherited_y)),
                  derivative_discrepancy=float(np.linalg.norm(newop['b_c']-compressed_b)),
                  next_dimension=len(next_state['d']),
                  next_packet_norm=float(np.linalg.norm(next_state['d'])))
    return next_state, report


def seed():
    return dict(connection=np.array([[0.,-1.],[1.,0.]]),
                coherence=np.diag([1.,2.]), difference=5*np.eye(2),
                neutral=np.eye(2), d=np.ones(2))
