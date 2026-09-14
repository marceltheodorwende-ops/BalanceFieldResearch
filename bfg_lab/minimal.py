"""Explicit experimental closure, NOT the universal BFG map. See MINIMAL_MODEL.md."""
import json
import numpy as np
from .core import TOL, hermitian
from .formation import prepare_candidate


def seed():
    return dict(y=np.eye(2), d=np.ones(2), r=np.diag([1., .5]),
                difference=3*np.eye(2), coherence=np.eye(2), neutral=np.eye(2))


def advance(state, retention=1., rho=.5):
    """Return (new state or None, diagnostics); never mutate the input."""
    if not np.isfinite(retention) or not 0 <= retention <= 1:
        raise ValueError('retention must lie in [0,1]')
    if not np.isfinite(rho) or not 0 <= rho < 1-TOL:
        raise ValueError('rho must lie in [0,1-TOL)')
    for key in ('difference', 'coherence', 'neutral'):
        if np.linalg.eigvalsh(hermitian(state[key])).min() < -TOL:
            raise ValueError('Minimal model requires positive semidefinite capacities')
    candidate = prepare_candidate(**state)
    report = dict(status=candidate['status'], gate=candidate['gate'],
                  dimension=len(state['d']), loads=candidate['split']['loads'])
    if not candidate['gate']['passed']:
        return None, report
    packet = candidate['support_packet']
    norm = np.linalg.norm(packet)
    if norm <= TOL:
        raise ValueError('Admitted packet is numerically zero; cannot normalize')
    d = packet/norm
    t = candidate['transport']
    difference = retention*t['difference']
    coherence, neutral = t['coherence'].copy(), t['neutral'].copy()
    # Chosen Gram closure; it is not derived from the papers.
    y = (coherence+neutral)/(1+np.linalg.norm(difference, ord=2))
    # Clamp only roundoff-sized negative eigenvalues to keep a PSD load.
    values, vectors = np.linalg.eigh(y)
    y = (vectors*np.maximum(values, 0))@vectors.conj().T
    projector = np.outer(d, d.conj())
    r = rho*np.eye(len(d))+(1-rho)*projector
    nxt = dict(y=y, d=d, r=r, difference=difference,
               coherence=coherence, neutral=neutral)
    report['next_dimension'] = len(d)
    return nxt, report


def simulate(state, steps=10, retention=1., rho=.5):
    if isinstance(steps, bool) or not isinstance(steps, (int, np.integer)) or steps < 1:
        raise ValueError('steps must be a positive integer')
    history = []
    for i in range(steps):
        nxt, report = advance(state, retention=retention, rho=rho)
        history.append(dict(step=i, **report))
        if nxt is None:
            return dict(status='formation_rejected', transitions=i, history=history)
        state = nxt
    return dict(status='step_limit', transitions=steps, history=history)


if __name__ == '__main__':
    for label, retention in [('maintained', 1.), ('depleted', .8)]:
        print(json.dumps(dict(example=label, retention=retention,
                              **simulate(seed(), steps=12, retention=retention)), allow_nan=False))
