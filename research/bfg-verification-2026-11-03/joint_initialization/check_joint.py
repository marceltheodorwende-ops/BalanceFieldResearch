"""Exact joint neutral/raw-recursion compatibility controls, not an origin law."""
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
I=s.eye(2);Pi=s.diag(1,0)
# Noncommuting positive-sector example with an exact protected formed line.
N=s.diag(s.Rational(1,2),s.Rational(1,3))
Nh=s.diag(1/s.sqrt(2),1/s.sqrt(3));Nih=Nh.inv()
e=s.Matrix([1/s.sqrt(2),1/s.sqrt(2)]);P=e*e.T
A=P+(I-P)/2;R=s.simplify(Nih*A*Nih);D=s.simplify(N.inv()-R)
assert s.simplify(Nh*R*Nh-A)==s.zeros(2)
assert s.simplify(I-A-Nh*D*Nh)==s.zeros(2)
assert s.simplify(D*Nh*e)==s.zeros(2,1) and D.rank()==1
assert s.simplify(A*e-e)==s.zeros(2,1)
assert s.simplify(N*e-e*(e.T*N*e)[0])!=s.zeros(2,1)
assert all(v>=0 for v in D.eigenvals())
# A fixed raw operator and common formed direction do not fix transverse Y.
Rfix=s.diag(s.Rational(5,4),1)
ys=[s.diag(s.Rational(1,4),s.Rational(1,4)),s.diag(s.Rational(1,4),s.Rational(1,2))]
closures=[]
H=s.diag(4,3);Hh=s.diag(2,s.sqrt(3))
for y in ys:
    c=(I+y).inv();ch=s.diag(*[s.sqrt(c[j,j]) for j in range(2)])
    a=s.simplify(ch*Rfix*ch);closures.append(a)
    assert a*Pi==Pi and (a-I).rank()==1
    assert all(0<x<=1 for x in a.eigenvals())
    yh=s.diag(*[s.sqrt(y[j,j]) for j in range(2)])
    L=s.simplify(Hh.inv()*yh*Hh)
    assert s.simplify(Hh*L*H.inv()*L.T*Hh-y)==s.zeros(2)
assert closures==[s.diag(1,s.Rational(4,5)),s.diag(1,s.Rational(2,3))]
y,r=s.symbols('y r',real=True)
assert s.solve(s.Eq(r/(1+y),1),y)==[r-1]
assert s.Rational(5,4)-1==s.Rational(1,4)
report={'status':'PASS','date':'2026-11-03','noncommuting_kernel_fixture':True,
 'fixed_raw_R_two_Ys_same_protected_line':True,
 'conditional_transverse_recursive_eigenvalues':['4/5','2/3'],
 'same_formed_H_and_intrinsic_neutral_metric_compatibility':True,
 'conditional_common_mode_matching':'y=r-1; surviving strict interval 1<r<2',
 'N_R_equals_neutral_resolvent_established_from_original_premises':False,
 'unique_joint_initializer_derived':False,
 'new_identification_or_origin_law_adopted':False,'event_rule_modified':False,
 'scope':'Exact finite positive-sector compatibility and explicitly conditional resolvent comparison; not a full historical independence or physical theorem'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
