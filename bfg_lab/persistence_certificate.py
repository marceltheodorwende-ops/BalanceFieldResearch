"""Exact verification of supplied real-rational invariant-splitting certificates.

No eigenvalue fitting, no float tolerance, no claim of automatic completeness.
"""
from fractions import Fraction


def _scalar(x):
    if isinstance(x, bool) or not isinstance(x, (int, str, Fraction)):
        raise ValueError('Use integers, rational strings or Fraction, not floats')
    try:
        return Fraction(x)
    except (ValueError, ZeroDivisionError) as e:
        raise ValueError('Invalid rational entry') from e


def _square(a, n):
    if len(a) != n or any(len(row) != n for row in a):
        raise ValueError('Wrong square matrix dimensions')
    return [[_scalar(x) for x in row] for row in a]


def _transpose(a):
    return [list(x) for x in zip(*a)]


def _mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), Fraction(0))
             for col in zip(*b)] for row in a]


def _inverse(a):
    n = len(a)
    rows = [list(row)+[Fraction(i == j) for j in range(n)]
            for i, row in enumerate(a)]
    for j in range(n):
        pivot = next((i for i in range(j, n) if rows[i][j]), None)
        if pivot is None:
            raise ValueError('Singular supplied basis')
        rows[j], rows[pivot] = rows[pivot], rows[j]
        v = rows[j][j]
        rows[j] = [x/v for x in rows[j]]
        for i in range(n):
            if i != j:
                v = rows[i][j]
                rows[i] = [x-v*y for x, y in zip(rows[i], rows[j])]
    return [row[n:] for row in rows]


def _positive(a):
    # Exact Schur-complement/LDL pivots, valid for symmetric positive definiteness.
    if a != _transpose(a):
        return False
    m = [row[:] for row in a]
    for k in range(len(m)):
        if m[k][k] <= 0:
            return False
        for i in range(k+1, len(m)):
            for j in range(k+1, len(m)):
                m[i][j] -= m[i][k]*m[k][j]/m[k][k]
    return True


def verify(r, basis, persistent_dimension, persistent_metric, stable_metric):
    """Certify R=S diag(A,T) S^-1, A^t M A=M, N-T^t N T > 0.

    Metrics must be positive definite. Empty blocks use []. A failed supplied
    certificate raises ValueError; this does not prove R is not power bounded.
    Returned projector is spectral/oblique, not a BFG graph-metric projector.
    """
    n = len(r)
    p = persistent_dimension
    if n == 0 or isinstance(p, bool) or not isinstance(p, int) or not 0 <= p <= n:
        raise ValueError('Invalid dimension')
    r, s = _square(r, n), _square(basis, n)
    mp, ms = _square(persistent_metric, p), _square(stable_metric, n-p)
    inv = _inverse(s)
    block = _mul(_mul(inv, r), s)
    if any(block[i][j] for i in range(n) for j in range(n) if (i < p) != (j < p)):
        raise ValueError('Supplied subspaces are not invariant')
    if p:
        a = [row[:p] for row in block[:p]]
        if not _positive(mp) or _mul(_mul(_transpose(a), mp), a) != mp:
            raise ValueError('Persistent block is not isometric in supplied metric')
    if p < n:
        t = [row[p:] for row in block[p:]]
        propagated = _mul(_mul(_transpose(t), ms), t)
        defect = [[ms[i][j]-propagated[i][j] for j in range(n-p)] for i in range(n-p)]
        if not _positive(ms) or not _positive(defect):
            raise ValueError('Stable block lacks supplied strict Lyapunov certificate')
    diagonal = [[Fraction(i == j and i < p) for j in range(n)] for i in range(n)]
    projector = _mul(_mul(s, diagonal), inv)
    return {'status': 'certified', 'persistent_dimension': p,
            'spectral_projector': projector, 'coordinate_transport': block}
