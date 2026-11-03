"""Exact diagnostics for the formed-profile versus inherited-witness bridge."""
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
I=s.eye(2);Pi=s.diag(1,0);Q=I-Pi;K=s.diag(-2,1);rho=2*Pi
assert rho/s.trace(rho)==Pi
assert (K+2*I)==3*Q
def excess(w):return s.trace(K*w)+2
def distance2(w):return s.simplify(s.trace((w-Pi).conjugate().T*(w-Pi)))
for a in [s.Rational(0),s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)]:
    w=(1-a)*Pi+a*Q
    assert s.trace(w)==1 and all(v>=0 for v in w.eigenvals())
    assert K*w==w*K and I*w*I==w and s.trace(Pi*w)>0
    assert excess(w)==3*a
    assert (w==Pi)==(excess(w)==0)==(s.trace(Q*w)==0)
    assert distance2(w)<=2*excess(w)/3
v=s.Matrix([s.Rational(4,5),s.Rational(3,5)])
w=v*v.T
assert s.trace(w)==1 and w*w==w
assert excess(w)/3==s.Rational(9,25)
assert distance2(w)==2*excess(w)/3==s.Rational(18,25)
mixed=3*Pi/4+Q/4
assert distance2(mixed)==s.Rational(1,8)<2*excess(mixed)/3
# A zero excited diagonal entry cannot coexist with nonzero off-diagonal PSD mass.
z=s.symbols('z',real=True)
bad=s.Matrix([[1,z],[z,0]])
assert bad.det()==-z*z
# The full commuting stationary packet does not supply support or order domination.
assert Q*Q==Q and I*Q*I==Q and Q!=Pi
assert (Pi+I/2)/2!=Pi
U=s.Matrix([[0,1],[1,0]])
F=lambda p:(p+I/2)/2
assert F(U*Pi*U.T)==U*F(Pi)*U.T
assert Pi/rho[0,0]==rho/4  # finite c exists: Pi=(1/2)rho
assert Pi==rho/2
assert (rho-Q)[1,1]<0  # no positive multiple of rho can dominate Q
# Degenerate ground: both distinct projectors minimize the same quadratic value.
Kd=-I
assert s.trace(Kd*Pi)==s.trace(Kd*Q)==-1 and Pi!=Q
report={'status':'PASS','date':'2026-11-03',
 'formed_line_identifier':'rho_F / tr(rho_F) = Pi_0 for the fresh simple-ground formation',
 'equivalent_bridge_conditions':'support, zero transverse mass, minimum quadratic value, finite order domination',
 'sharp_pure_fixture':{'excess_over_gap':'9/25','squared_Frobenius_distance':'18/25'},
 'stationarity_commutation_overlap_alone_force_identification':False,
 'covariance_alone_forces_identification':False,
 'ground_degeneracy_still_unique_witness':False,
 'historical_premise_enforcing_bridge_established':False,
 'event_rule_modified':False,'new_physical_rule_adopted':False,
 'scope':'Analytic finite equivalence and quantitative bound, exact fixtures and targeted source trace; no full-corpus independence or empirical claim'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
