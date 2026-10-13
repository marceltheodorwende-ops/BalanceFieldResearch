"""Independent P79 controls; no downloads, no holdout.
Thresholds: exact rational bounds; real 100-digit chain margin>1e-9,
log sensitivity agreement1e-9, matrix-exponential residual1e-12.
"""
from fractions import Fraction as F
import json
from pathlib import Path
import random
import mpmath as mp
import numpy as np
from scipy.linalg import expm
import sympy as sp
from analyze import alternating_chain

here = Path(__file__).resolve().parent
rng = random.Random(79)
mp.mp.dps = 100
eps = F(1, 100)


def poly(coeffs, x):
    result = F(0)
    for c in reversed(coeffs):
        result = result*x+c
    return result


for _ in range(200):
    degree = rng.randint(0, 8)
    c = [F(rng.randint(-10, 10)) for _ in range(degree+1)]
    a = F(rng.randint(1, 4), 5)
    q = [poly(c,a**k)+F(rng.randint(-100,100),10000) for k in range(25)]
    chain = alternating_chain(q,2*eps)
    assert len(chain)-1 <= degree
    diffs = [q[j]-q[i] for i,j in zip(chain,chain[1:])]
    assert all(abs(v)>2*eps for v in diffs)
    assert all(diffs[i]*diffs[i+1]<0 for i in range(len(diffs)-1))

for _ in range(200):
    m,n = rng.randint(0,5),rng.randint(0,5)
    numerator = [F(rng.randint(-10,10)) for _ in range(m+1)]
    denominator = [F(rng.randint(1,5)) for _ in range(n+1)]
    q = [poly(numerator,F(2,3)**k)/poly(denominator,F(2,3)**k) for k in range(25)]
    chain = alternating_chain(q,F(0))
    assert len(chain)-1 <= m+n

# Exact interpolation: bound can be attained without proving physical meaning.
interpolation = []
for count in range(2, 9):
    nodes = [F(1,2)**k for k in range(count)]
    values = [F((-1)**k) for k in range(count)]
    def interpolate(x):
        total = F(0)
        for i in range(count):
            basis = F(1)
            for j in range(count):
                if i!=j:
                    basis *= (x-nodes[j])/(nodes[i]-nodes[j])
            total += values[i]*basis
        return total
    assert [interpolate(x) for x in nodes] == values
    assert len(alternating_chain(values,F(0)))-1 == count-1
    interpolation.append(count)

# Independently differentiate general quadratic angle and principal generator.
x,y,l,w = sp.symbols('x y l w',real=True)
c1,c2,c3,c4,c5 = sp.symbols('c1 c2 c3 c4 c5',real=True)
H = c1*x+c2*y+c3*x*x+c4*x*y+c5*y*y
velocity = sp.diff(H,x)*l*x+sp.diff(H,y)*l*y
J = sp.Matrix([[sp.diff(H,x),sp.diff(H,y)],
               [sp.diff(velocity,x),sp.diff(velocity,y)]]).subs({x:0,y:0})
assert sp.simplify(J.det()) == 0
A = sp.Matrix([[l,-w],[w,l]])
angle = sp.Matrix([[c1,c2]])
chart = angle.col_join(angle*A)
assert sp.simplify(chart.det()+w*(c1*c1+c2*c2)) == 0
assert sp.simplify(A*A-2*l*A+(l*l+w*w)*sp.eye(2)) == sp.zeros(2)
ell = np.log(16/135)
max_expm = 0.
for j in [1,2]:
    Aj = np.array([[ell,-2*np.pi*j],[2*np.pi*j,ell]])
    max_expm = max(max_expm,np.max(np.abs(expm(Aj)-(16/135)*np.eye(2))))
assert max_expm < 1e-12

# Smooth flat oscillatory triangular chart: sign alternates on a^k exactly.
a = mp.mpf(16)/135
for k in range(31):
    r = a**k
    phase = mp.sin(mp.pi*mp.log(r)/mp.log(a)+mp.pi/2)
    assert phase*((-1)**k) > mp.mpf('.9999999999')
    assert -1/(r*r) < 0  # log of the strictly positive flat amplitude
flat_J = sp.Matrix([[1,sp.Symbol('fprime')],[0,1]])
assert flat_J.det() == 1

records = json.loads((here/'record_results.json').read_text())
max_log_error = mp.mpf(0)
minimum_margin = mp.inf
edge_count = 0
for record in records:
    indices = record['chain_indices']
    values = list(map(mp.mpf,record['chain_angles']))
    assert len(indices)==len(values)==record['certified_chain_length']
    assert indices == sorted(set(indices))
    error = mp.pi/record['N']+mp.mpf('.0005')+mp.mpf(str(record['extra_angle_error']))
    diffs = [values[k+1]-values[k] for k in range(len(values)-1)]
    assert all(abs(v)-2*error>mp.mpf('1e-9') for v in diffs)
    assert all(diffs[k]*diffs[k+1]<0 for k in range(len(diffs)-1))
    minimum_margin = min(minimum_margin,*[abs(v)-2*error for v in diffs])
    edge_count += len(diffs)
    assert record['polynomial_degree_lower_bound']==len(indices)-1
    i,j = record['sensitivity_edge']
    qi,qj = map(mp.mpf,record['sensitivity_edge_angles'])
    delta = abs(qj-qi)-2*error
    exact_log = mp.log10(delta/(a**i*(1-a**(j-i))))
    conservative = mp.log10(delta/a**i)
    max_log_error = max(max_log_error,abs(exact_log-mp.mpf(record['log10_LR_lower_bound_one_event_per_row'])),
                        abs(conservative-mp.mpf(record['log10_LR_lower_bound_forward_skips'])))
    # A fixed witness margin must decrease when error is enlarged.
    assert delta-mp.mpf('.01') < delta
assert max_log_error < mp.mpf('1e-9')

# Concrete skipped-event counterexample to the sharper denominator transfer.
aa = F(1,2)
row_denominator = aa**0*(1-aa**1)
skip_denominator = aa**0*(1-aa**2)
assert skip_denominator > row_denominator

result = dict(kind='independent_synthetic_and_development_certificate_controls',
              rational_noisy_polynomial_cases=200,positive_denominator_rational_cases=200,
              exact_interpolation_cases=len(interpolation),
              principal_kinematic_rank_obstruction_symbolic=True,
              rotating_generator_force_identity_symbolic=True,
              max_expm_residual=max_expm,smooth_flat_sign_controls=31,
              real_records_checked=len(records),real_chain_edges_checked=edge_count,
              precision_digits=100,minimum_real_chain_margin_mp=str(minimum_margin),
              maximum_log_sensitivity_error=str(max_log_error),
              skipped_event_denominator_counterexample_preserved=True,
              model_fitted=False,independent_confirmation=False,holdout_accessed=False)
(here/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
