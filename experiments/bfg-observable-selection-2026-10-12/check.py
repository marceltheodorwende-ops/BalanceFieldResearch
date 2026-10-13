"""Independent P78 synthetic and selected real arithmetic checks.
Thresholds: exact rational controls equality; MP integral1e-70;
cubic ODE coefficient relative2e-3; exponential1e-12; real witness agreement1e-12.
No data download or holdout access. Read only published derived real summaries.
"""
from fractions import Fraction as F
import ast
import json
from pathlib import Path
import random
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp
from scipy.linalg import expm

here = Path(__file__).resolve().parent
mp.mp.dps = 100
rng = random.Random(78)
eps = F(1, 100)
rational_cases = 200
for _ in range(rational_cases):
    a = F(rng.randint(1, 19), 20)
    b, z = F(rng.randint(-10, 10)), F(rng.randint(-10, 10))
    q = [b+a**k*z+F(rng.randint(-100, 100), 10000) for k in range(20)]
    for j in range(1, len(q)-1):
        peak = min(q[j]-min(q[:j]), q[j]-min(q[j+1:]))
        trough = min(max(q[:j])-q[j], max(q[j+1:])-q[j])
        assert peak <= 2*eps and trough <= 2*eps
    residual = [q[k+1]-a*q[k] for k in range(len(q)-1)]
    c = (1-a)*b
    assert all(abs(v-c) <= (1+a)*eps for v in residual)
assert min(F(1)-F(0), F(1)-F(0)) > 2*eps  # q=(0,1,0)

# Independent exhaustive-triple oracle for the actual prefix/suffix algorithm.
tree = ast.parse((here/'analyze.py').read_text())
node = next(n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name=='best_reversal')
namespace = {}
exec(compile(ast.Module(body=[node], type_ignores=[]), 'isolated_reversal', 'exec'), namespace)
for _ in range(50):
    q = [F(rng.randint(-30, 30), 7) for _ in range(8)]
    expected = max(max(min(q[j]-q[i], q[j]-q[k]), min(q[i]-q[j], q[k]-q[j]))
                   for i in range(8) for j in range(i+1, 8) for k in range(j+1, 8))
    score, kind, indices = namespace['best_reversal'](q)
    assert score == expected

max_integral_error = mp.mpf(0)
max_cubic_relative_error = 0.
for gamma, omega, j in [(2., 2*np.pi, 1), (-2*np.log(16/135), 2*np.pi, 1), (2., 4*np.pi, 2)]:
    T = 2*np.pi*j/omega
    gm, om, tm = mp.mpf(gamma), mp.mpf(omega), mp.mpf(T)
    # Evaluate at the exact MP resonance duration, not a rounded floating T.
    tm = 2*mp.pi*j/om
    integral = mp.quad(lambda s: mp.exp(-gm*s)*mp.sin(om*s)*mp.cos(om*s)**3,
                       [tm*k/(8*j) for k in range(8*j+1)])
    formula = (1-mp.exp(-gm*tm))/(4*om)*(mp.mpf(5)/8-gm**2/(2*(gm**2+4*om**2))-gm**2/(8*(gm**2+16*om**2)))
    assert integral > 0
    max_integral_error = max(max_integral_error, abs(integral-formula))
    kappa = omega**2+gamma**2/4
    rho = np.exp(-gamma*T/2)
    coefficient = -rho*kappa/(6*omega)*float(formula)
    coefficients = []
    for e in [.02, .01, .005]:
        def rhs(_, z):
            return [z[1], -gamma*z[1]-kappa*np.sin(z[0])]
        sol = solve_ivp(rhs, [0, T], [e, -gamma*e/2], method='DOP853', rtol=2e-13, atol=2e-15)
        assert sol.success
        measured = (sol.y[0, -1]-rho*e)/e**3
        coefficients.append(measured)
        max_cubic_relative_error = max(max_cubic_relative_error, abs((measured-coefficient)/coefficient))
    assert coefficients[-1] < 0
assert max_integral_error < mp.mpf('1e-70')
assert max_cubic_relative_error < 2e-3

# Undamped boundary has a nonzero velocity cubic coefficient.
kappa, T, e = (2*np.pi)**2, 1., .005
sol = solve_ivp(lambda t, z: [z[1], -kappa*np.sin(z[0])], [0, T], [e, 0.],
                method='DOP853', rtol=2e-13, atol=2e-15)
assert sol.success and abs(sol.y[1, -1]/e**3-kappa*T/16)/(kappa*T/16) < 2e-3

a = 16/135
gamma = -2*np.log(a)
returns = []
extra_traces = []
max_expm_error = 0.
for j in range(1, 5):
    omega = 2*np.pi*j
    A = np.array([[0., 1.], [-(omega**2+gamma**2/4), -gamma]])
    max_expm_error = max(max_expm_error, np.max(np.abs(expm(A)-a*np.eye(2))))
    returns.append(expm(A))
    extra_traces.append(float(np.trace(expm(.37*A))/(2*np.exp(-gamma*.37/2))))
assert max_expm_error < 1e-12
trace_gap = min(abs(extra_traces[i]-extra_traces[j]) for i in range(4) for j in range(i))
assert trace_gap > 0.1
# A rational extra duration has an exact trace ambiguity for aliases1/3.
assert abs(np.cos(2*np.pi*.25)-np.cos(6*np.pi*.25)) < 1e-12
# Uncertainty interval propagation must retain the center predictions.
def cosine_range(j, rlo, rhi):
    assert j >= 1 and rlo <= rhi
    values = [np.cos(2*np.pi*j*rlo), np.cos(2*np.pi*j*rhi)]
    for k in range(int(np.ceil(2*j*rlo)), int(np.floor(2*j*rhi))+1):
        values.append((-1.)**k)
    return [float(min(values)-1e-12), float(max(values)+1e-12)]

expanded_intervals = []
for j, center in enumerate(extra_traces, 1):
    samples = [np.cos(2*np.pi*j*r) for r in np.linspace(.369, .371, 101)]
    lo, hi = cosine_range(j, .369, .371)
    assert lo <= min(samples) <= center <= max(samples) <= hi
    expanded_intervals.append([lo-.01, hi+.01])
for _ in range(100):
    j = rng.randint(1, 10)
    rlo = rng.random()
    rhi = rlo+rng.random()/10
    lo, hi = cosine_range(j, rlo, rhi)
    wider = cosine_range(j, rlo-.01, rhi+.01)
    assert wider[0] <= lo and wider[1] >= hi
    for k in range(5):
        r = mp.mpf(rlo)+(mp.mpf(rhi)-mp.mpf(rlo))*k/4
        exact = mp.cos(2*mp.pi*j*r)
        assert mp.mpf(lo) <= exact <= mp.mpf(hi)
interval_gap = min(max(expanded_intervals[i][0]-expanded_intervals[j][1],
                       expanded_intervals[j][0]-expanded_intervals[i][1])
                   for i in range(4) for j in range(i))
assert interval_gap > 0

records = json.loads((here/'record_results.json').read_text())
all_real_margins = []
for record in records:
    values = list(map(mp.mpf, record['reversal_angles']))
    score = min(values[1]-values[0], values[1]-values[2]) if record['reversal_kind']=='peak' else min(values[0]-values[1], values[2]-values[1])
    error = mp.pi/record['N']+mp.mpf('.0005')+mp.mpf(str(record['extra_angle_error']))
    exact_margin = score-2*error
    assert abs(exact_margin-mp.mpf(record['reversal_margin'])) < mp.mpf('1e-12')
    assert (exact_margin>mp.mpf('1e-9')) == record['affine_positive_contraction_rejected']
    all_real_margins.append(exact_margin)
worst = max(records, key=lambda r: r['reversal_margin'])
values = list(map(mp.mpf, worst['reversal_angles']))
score = min(values[1]-values[0], values[1]-values[2]) if worst['reversal_kind']=='peak' else min(values[0]-values[1], values[2]-values[1])
error = mp.pi/worst['N']+mp.mpf('.0005')+mp.mpf(str(worst['extra_angle_error']))
margin = score-2*error
assert margin > 0 and abs(margin-mp.mpf(worst['reversal_margin'])) < mp.mpf('1e-12')
result = dict(kind='independent_synthetic_and_selected_development_arithmetic_controls',
              rational_monotone_cases=rational_cases, precision_digits=100,
              exhaustive_triple_oracle_cases=50,
              real_margins_checked=len(all_real_margins),
              minimum_real_margin_mp=str(min(all_real_margins)),
              max_integral_error=str(max_integral_error),
              max_cubic_coefficient_relative_error=max_cubic_relative_error,
              max_expm_alias_error=max_expm_error,
              extra_time_ratio_synthetic=.37, finite_alias_count_synthetic=4,
              normalized_half_trace_min_gap=trace_gap,
              synthetic_ratio_interval=[.369, .371], synthetic_trace_error=.01,
              synthetic_expanded_trace_intervals=expanded_intervals,
              synthetic_min_interval_separation=interval_gap,
              independent_mp_interval_containment_checks=500,
              exact_rational_trace_alias_preserved=True,
              selected_real_witness=dict(file=worst['file'], N=worst['N'],
                                         extra_angle_error=worst['extra_angle_error'],
                                         indices=worst['reversal_indices'], margin_mp=str(margin)),
              independent_confirmation=False, physical_calibration=False,
              holdout_accessed=False)
(here/'verification.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
