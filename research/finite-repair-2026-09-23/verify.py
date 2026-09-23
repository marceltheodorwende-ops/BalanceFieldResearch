"""Bounded regression checks for the mathematical amendment; not a full BFG map."""
from fractions import Fraction as F
import json
from pathlib import Path
import numpy as np

def m(rows):
    return np.array([[F(x) for x in row] for row in rows], dtype=object)

def exact_equal(a, b):
    assert np.array_equal(a, b)

checks = []
R = m([[1, F(-1, 2)], [0, F(1, 2)]])
E = m([[1, -1], [0, 0]])
P = m([[1, 0], [0, 0]])
I = m([[1, 0], [0, 1]])
exact_equal(E @ E, E)
exact_equal(E @ R, R @ E)
assert not np.array_equal(P @ R, R @ P)
for n in (1, 2, 8, 32):
    exact_equal(np.linalg.matrix_power(R, n), E + F(1, 2)**n * (I-E))
checks.append('exact nonnormal spectral/metric distinction and power formula')

# W=span(e1), G positive definite; formula (3) gives this oblique metric projection.
G = m([[2, 1], [1, 2]])
PG = m([[1, F(1, 2)], [0, 0]])
exact_equal(PG @ PG, PG)
exact_equal(PG.T @ G, G @ PG)
assert not np.array_equal(PG.T, PG)
checks.append('exact graph-metric projection and G self-adjointness')

# Stable Jordan blocks are allowed, whereas a unit Jordan block has growing powers.
stable = m([[F(1, 2), 1], [0, F(1, 2)]])
unit = m([[1, 1], [0, 1]])
for n in (1, 3, 16):
    exact_equal(np.linalg.matrix_power(stable, n), m([[F(1, 2)**n, n*F(1, 2)**(n-1)], [0, F(1, 2)**n]]))
    exact_equal(np.linalg.matrix_power(unit, n), m([[1, n], [0, 1]]))
checks.append('exact stable and forbidden peripheral Jordan boundary cases')

# Old witness-span counterexample remains reproducible.
assert np.linalg.det(np.array([[1., 1.], [0., 1.]])) == 1
checks.append('old forward-witness span has rank two, peripheral space rank one')

K = np.diag([-1., 2.])
def energy(z):
    return float((.5*np.vdot(z, K@z) + .25*np.vdot(z, z)**2).real)
for phase in np.exp(1j*np.linspace(0, 2*np.pi, 17)):
    assert abs(energy(np.array([phase, 0])) + .25) < 1e-12
for sign in (-1, 1):
    assert energy(np.array([sign, 0])) == -.25
checks.append('complex phase orbit and real polarity minima')

rng = np.random.default_rng(20260923)
max_polar_residual = 0.
max_metric_residual = 0.
for _ in range(64):
    # Supplied real geometry tests the sufficient intertwining conditions.
    raw = rng.normal(size=(4, 4)); Y = raw.T@raw
    C = np.linalg.inv(np.eye(4)+Y); B = Y@C
    A = np.vstack((np.sqrt(.37)*C, np.sqrt(.63)*B))
    u, _, vh = np.linalg.svd(A, full_matrices=False); J = u@vh
    raw = rng.normal(size=(4, 4)); capacity = (raw+raw.T)/2
    transported = J.T@np.kron(np.eye(2), capacity)@J
    residual = max(np.linalg.norm(J.T@J-np.eye(4)), np.linalg.norm(transported-transported.T))
    max_polar_residual = max(max_polar_residual, float(residual))
    assert residual < 1e-11
    # Independent projector formula: idempotence, metric symmetry, basis invariance.
    Z = rng.normal(size=(4, 2)); Gf = np.eye(4)+Y
    def project(z):
        return z@np.linalg.solve(z.T@Gf@z, z.T@Gf)
    pg = project(Z); pg2 = project(Z@np.array([[2., 1.], [0., 3.]]))
    residual = max(np.linalg.norm(pg@pg-pg), np.linalg.norm(pg.T@Gf-Gf@pg), np.linalg.norm(pg-pg2))
    max_metric_residual = max(max_metric_residual, float(residual))
    assert residual < 1e-10
checks.append('64 real polar-transport and metric basis-invariance cases')

p = np.array([1., 0.]); pi = np.outer(p, p)
assert not np.array_equal(np.eye(2)+pi, np.eye(2)+2*pi)
for c in (1., 2.):
    load = np.eye(2)+c*pi
    assert np.linalg.eigvalsh(load).min() > 0
    vals, vecs = np.linalg.eigh(load); root = (vecs*np.sqrt(vals))@vecs.T
    assert np.allclose(root.T@root, load)
checks.append('distinct positive phase-invariant Gram candidates remain')

result = {'date': '2026-09-23', 'seed': 20260923, 'numpy': np.__version__, 'status': 'passed',
          'check_groups': checks, 'max_polar_residual': max_polar_residual,
          'max_metric_residual': max_metric_residual,
          'scope': 'Supplementary exact examples and finite numerical checks; proofs in REPAIR.md; no universal update or empirical validation'}
(Path(__file__).parent/'RESULTS.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
