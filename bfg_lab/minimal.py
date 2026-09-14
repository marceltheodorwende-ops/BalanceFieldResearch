"""Explicit experimental closure, NOT the universal BFG map. See MINIMAL_MODEL.md."""
import json
import numpy as np
from .core import TOL, hermitian, persistent_basis
from .formation import prepare_candidate


def seed():
    return dict(y=np.eye(2), d=np.ones(2), r=np.diag([1., .5]),
                difference=3*np.eye(2), coherence=np.eye(2), neutral=np.eye(2))


def multimode_seed():
    return dict(y=np.eye(3), d=np.ones(3), r=np.diag([1., 1., .5]),
                difference=np.diag([4., 3., 1.]), coherence=np.eye(3), neutral=np.eye(3))


def spectral_transport(formation, rho=.5, tol=TOL):
    """Experimental rule: preserve the entire strictly negative spectral space."""
    if not np.isfinite(tol) or not 0 < tol < 1:
        raise ValueError('tol must lie in (0,1)')
    if not np.isfinite(rho) or not 0 <= rho < 1-TOL:
        raise ValueError('rho must lie in [0,1-TOL)')
    values, vectors = np.linalg.eigh(hermitian(formation))
    active = values < -tol
    w = vectors[:, active]
    p = w@w.conj().T
    r = rho*np.eye(len(values))+(1-rho)*p
    return r, dict(persistent_rank_next=int(active.sum()),
                   next_formation_eigenvalues=values.tolist(),
                   spectral_threshold=float(tol),
                   near_zero_modes=int(np.sum(np.abs(values) <= tol)))


def advance(state, retention=1., rho=.5, transport_rule='packet'):
    """Return (new state or None, diagnostics); never mutate the input."""
    if not np.isfinite(retention) or not 0 <= retention <= 1:
        raise ValueError('retention must lie in [0,1]')
    if not np.isfinite(rho) or not 0 <= rho < 1-TOL:
        raise ValueError('rho must lie in [0,1-TOL)')
    if transport_rule not in ('packet', 'negative_spectrum', 'carried'):
        raise ValueError('Unknown experimental transport rule')
    if transport_rule == 'carried':
        hermitian(state['r'])  # Compression of general normal R need not be normal.
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
    if transport_rule == 'packet':
        projector = np.outer(d, d.conj())
        r = rho*np.eye(len(d))+(1-rho)*projector
        report['persistent_rank_next'] = 1
    elif transport_rule == 'negative_spectrum':
        r, audit = spectral_transport(coherence+neutral-difference, rho=rho)
        report.update(audit)
    else:
        # Identify new support with the old initial polar support, then restrict R.
        q = candidate['split']['polar'].conj().T@t['basis']
        r = q.conj().T@state['r']@q
        r = (r+r.conj().T)/2
        report['persistent_rank_next'] = persistent_basis(r).shape[1]
    report['transport_rule'] = transport_rule
    nxt = dict(y=y, d=d, r=r, difference=difference,
               coherence=coherence, neutral=neutral)
    report['next_dimension'] = len(d)
    return nxt, report


def simulate(state, steps=10, retention=1., rho=.5, transport_rule='packet'):
    if isinstance(steps, bool) or not isinstance(steps, (int, np.integer)) or steps < 1:
        raise ValueError('steps must be a positive integer')
    history = []
    for i in range(steps):
        nxt, report = advance(state, retention=retention, rho=rho, transport_rule=transport_rule)
        history.append(dict(step=i, **report))
        if nxt is None:
            return dict(status='formation_rejected', transitions=i, history=history)
        state = nxt
    return dict(status='step_limit', transitions=steps, history=history)


if __name__ == '__main__':
    for rule, initial in [('packet', seed), ('negative_spectrum', multimode_seed)]:
        for label, retention in [('maintained', 1.), ('depleted', .8)]:
            print(json.dumps(dict(example=label, retention=retention, transport_rule=rule,
                                 **simulate(initial(), steps=12, retention=retention,
                                            transport_rule=rule)), allow_nan=False))
