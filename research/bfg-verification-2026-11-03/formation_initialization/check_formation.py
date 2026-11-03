"""Exact controls for the source-conditional formation initializer."""
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
x,y,lam=s.symbols('x y lam', real=True)
mu=s.symbols('mu', real=True)
t=x*x+y*y
F=(lam*x*x+mu*y*y)/2+t*t/4
gap=(mu-lam)*y*y/2+(t+lam)**2/4
assert s.expand(F+lam**2/4-gap)==0
K=s.diag(-2,1);pi=s.diag(1,0);rho=2*pi
d=s.Matrix([s.sqrt(2),0])
assert d*d.T==(-d)*(-d).T==rho
theta=s.symbols('theta',real=True)
dc=s.exp(s.I*theta)*d
assert s.simplify(dc*dc.conjugate().T-rho)==s.zeros(2)
assert s.trace(rho)==2
assert (d.T*K*d)[0]/2+(d.dot(d))**2/4==-1
# Distinct pure minimizers for a degenerate negative ground eigenvalue.
dg=[s.Matrix([1,0]),s.Matrix([0,1])]
assert all((v.T*(-s.eye(2))*v)[0]/2+v.dot(v)**2/4==-s.Rational(1,4) for v in dg)
assert dg[0]*dg[0].T!=dg[1]*dg[1].T
mixed=s.eye(2)/2
assert mixed.rank()==2 and s.trace(mixed)==1
# A zero ground eigenvalue still has only the zero minimizer.
Fzero=y*y/2+(x*x+y*y)**2/4
assert s.expand(Fzero.subs({x:0,y:0}))==0
assert s.expand(Fzero.subs(y,0))==x**4/4
# Rank-one support fixes every entry before normalization fixes the scalar.
a,b,c=s.symbols('a b c',real=True)
W=s.Matrix([[a,b],[b,c]])
assert pi*W*pi==s.diag(a,0)
assert (pi*W*pi).subs(a,1)==pi
Wa=pi;Wb=mixed
assert Wa!=Wb and s.trace(Wa)==s.trace(Wb)==1
assert all(v>=0 for w in [Wa,Wb] for v in w.eigenvals())
# Two power-bounded recursions preserve the formed line, with distinct peripheral spaces.
Ra=s.diag(1,s.Rational(1,2));Rb=s.eye(2)
assert Ra*d==Rb*d==d
assert [v for v in Ra.eigenvals() if abs(v)==1]==[s.Integer(1)]
assert (Ra-s.eye(2)).nullspace()==[s.Matrix([1,0])]
assert len((Rb-s.eye(2)).nullspace())==2
# An inherited sector and a seed sector cannot share a single witness role.
E=s.diag(0,1);inherited=pi;seed=3*E;total=2*pi+seed
assert E*inherited==s.zeros(2) and E*seed==seed
assert E*(total/s.trace(total))!=s.zeros(2)
report={'status':'PASS','date':'2026-11-03',
 'square_completion':'exact symbolic identity',
 'simple_ground_formation':{'density':str(rho),'trace':'2','minimum':'-1','phase_independent':True},
 'degenerate_ground_pure_density_unique':False,
 'nonnegative_ground_nonzero_minimizer':False,
 'witness_unique_given_same_rank_one_support':True,
 'witness_type_alone_unique':False,
 'formation_and_power_bounded_line_preservation_fix_P':False,
 'normalized_total_formation_can_replace_inherited_witness':False,
 'complete_initializer_derived':False,'new_physical_rule_adopted':False,
 'event_rule_modified':False,'scope':'Exact finite fixtures and analytic theorem; no full historical independence or empirical claim'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
