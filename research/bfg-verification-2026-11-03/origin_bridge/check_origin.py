"""Exact diagnostics for the origin representation gap; no new event law."""
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
I=s.eye(2);N=I/2;M=I/s.sqrt(2);Pi=s.diag(1,0);Q=I-Pi
d=s.Matrix([s.sqrt(2),0])
raw=[I,s.diag(2,1),2*I,s.diag(4,1)]
closed=[s.simplify(M*r*M.conjugate().T) for r in raw]
assert closed==[I/2,s.diag(1,s.Rational(1,2)),I,s.diag(2,s.Rational(1,2))]
assert closed[1]*d==closed[2]*d==d
assert [len((r-I).nullspace()) for r in closed]==[0,1,2,0]
# Exact isometry criterion; no inference from positive N alone.
for r,rc in zip(raw,closed):
    assert (s.simplify(rc.conjugate().T*rc-I)==s.zeros(2))==(s.simplify(r.conjugate().T*N*r-N.inv())==s.zeros(2))
assert closed[0].conjugate().T*closed[0]!=I
assert closed[3].eigenvals()[s.Integer(2)]==1
n=s.symbols('n',integer=True,nonnegative=True)
J=s.Matrix([[1,1],[0,1]])
Jn=s.Matrix([[1,n],[0,1]])
assert J*Jn==Jn.subs(n,n+1)
assert set(J.eigenvals())=={s.Integer(1)}
# Solve stationary Hermitian witnesses independently of the support lemma.
a,b,c,z=s.symbols('a b c z',real=True)
W=s.Matrix([[a,b+s.I*z],[b-s.I*z,c]])
R=closed[1]
equations=list(R*W*R.conjugate().T-W)+[s.trace(W)-1]
sol=s.solve(equations,[a,b,c,z],dict=True)
assert sol==[{a:1,b:0,c:0,z:0}]
assert W.subs(sol[0])==Pi
# Full persistent rank allows several stationary witnesses.
assert closed[2]*Pi*closed[2].T==Pi
assert closed[2]*(I/2)*closed[2].T==I/2
# Normalization has an extra fixed point on a decaying line.
decay=R*Q*R.T
assert decay==Q/4 and decay/s.trace(decay)==Q
assert R*Pi*R.T==Pi
# Density invariance does not force a fixed vector phase.
Rphase=s.diag(s.I,s.Rational(1,2))
assert Rphase*Pi*Rphase.conjugate().T==Pi
assert Rphase*d!=d
# No inherited overlap gives zero retained mass, so no normalized continuation.
T=s.zeros(2)
assert s.trace(T.conjugate().T*T*Pi)==0 and T*Pi*T.T==s.zeros(2)
report={'status':'PASS','date':'2026-11-03',
 'conjugate_form_alone_norm_preserving':False,
 'same_N_formed_line_and_bounded_criticality_fix_P':False,
 'middle_pair_peripheral_dimensions':[1,2],
 'spectral_radius_one_alone_implies_power_boundedness':False,
 'rank_one_protection_and_unnormalized_stationarity_unique_witness':True,
 'normalized_stationarity_alone_unique_witness':False,
 'density_stationarity_forces_fixed_vector_phase':False,
 'zero_overlap_retained_mass':'0',
 'primitive_identity_found_in_reviewed_origin_source':True,
 'original_to_operator_representation_theorem_established':False,
 'event_rule_modified':False,'new_physical_rule_adopted':False,
 'scope':'Exact algebraic diagnostics plus finite analytic theorem; bounded historical source audit, not empirical proof'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
