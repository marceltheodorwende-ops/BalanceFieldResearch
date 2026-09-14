"""Candidate transport and formation audit, not the full universal update.

Eq. 39/41 of Canonical Closure and V4. All spectral decisions use the lab's
explicit absolute tolerance TOL; a numerical rejection is not an exact theorem.
"""
import numpy as np
from .core import TOL, hermitian, persistent_basis, split


def transport_capacities(j, difference, coherence, neutral):
    """Compress on Ran(J) in orthonormal coordinates, excluding kernel zeros."""
    capacities = [hermitian(a) for a in (difference, coherence, neutral)]
    n = len(capacities[0])
    if any(a.shape != (n,n) for a in capacities):
        raise ValueError('Capacity dimensions must agree')
    j = np.asarray(j, dtype=complex)
    if j.shape != (2*n,n) or not np.isfinite(j).all():
        raise ValueError('Polar map must be finite with shape (2*n,n)')
    u, s, _ = np.linalg.svd(j, full_matrices=False)
    if not np.all((s <= TOL) | (np.abs(s-1) <= TOL)):
        raise ValueError('Expected a partial isometry')
    basis = u[:,s > TOL]
    if not basis.shape[1]:
        raise ValueError('Empty support has no formation operator')
    result = {'basis':basis}
    for name, a in zip(('difference','coherence','neutral'), capacities):
        lifted = np.kron(np.eye(2),a)
        reduced = basis.conj().T @ lifted @ basis
        result[name] = (reduced + reduced.conj().T)/2
    result['formation'] = result['coherence'] + result['neutral'] - result['difference']
    return result


def formation_gate(k, loads, persistence_gap):
    """Report all failed local conditions. One-dimensional isolation is vacuous."""
    k = hermitian(k)
    loads = np.asarray(loads, dtype=float)
    if (loads.shape != (2,) or not np.isfinite(loads).all() or
            np.any(loads < 0) or not np.isfinite(persistence_gap) or persistence_gap < 0):
        raise ValueError('Loads and persistence gap must be finite and nonnegative')
    eigenvalues = np.linalg.eigvalsh(k)
    minimum = float(eigenvalues[0])
    gap = float(eigenvalues[1]-minimum) if len(k)>1 else None
    reasons = []
    if np.any(loads <= TOL):
        reasons.append('no_dual_support')
    if persistence_gap <= TOL:
        reasons.append('no_persistence_gap')
    if minimum >= 0:
        reasons.append('nonnegative_minimum')
    elif minimum >= -TOL:
        reasons.append('minimum_within_tolerance')
    if gap is not None and gap <= TOL:
        reasons.append('nonisolated_minimum')
    return dict(passed=not reasons, reasons=reasons, minimum=minimum,
                formation_gap=gap, persistence_gap=float(persistence_gap),
                tolerance=TOL, eigenvalues=eigenvalues.tolist())


def prepare_candidate(y, d, r, difference, coherence, neutral):
    """Build split, transport capacities and test formation; no invented Y_next."""
    y = hermitian(y)
    for a in (difference,coherence,neutral):
        if hermitian(a).shape != y.shape:
            raise ValueError('Capacities must match load dimension')
    r = np.asarray(r, dtype=complex)
    if r.shape != y.shape:
        raise ValueError('Transport must match load dimension')
    w = persistent_basis(r)
    packet = split(y,d,w)
    if packet['status'] != 'ok':
        return dict(status='formation_rejected', gate=dict(passed=False,
                    reasons=['no_dual_support'], tolerance=TOL), split=packet)
    magnitudes = np.abs(np.linalg.eigvals(r))
    stable = magnitudes[np.abs(magnitudes-1) > TOL]
    # Empty stable complement: adopt sup(empty)=0 on nonnegative moduli.
    gap = 1-float(stable.max()) if stable.size else 1.
    transported = transport_capacities(packet['polar'],difference,coherence,neutral)
    gate = formation_gate(transported['formation'],packet['loads'],gap)
    return dict(status='formation_admitted' if gate['passed'] else 'formation_rejected',
                gate=gate, transport=transported, split=packet,
                support_packet=transported['basis'].conj().T @ packet['packet'])


if __name__ == '__main__':
    import json
    for label, difference in [('admitted',3*np.eye(2)), ('rejected',np.eye(2))]:
        result=prepare_candidate(np.eye(2),np.ones(2),np.diag([1.,.5]),
                                 difference,np.eye(2),np.eye(2))
        print(json.dumps(dict(example=label,status=result['status'],gate=result['gate'])))
