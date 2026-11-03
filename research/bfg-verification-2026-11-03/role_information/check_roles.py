"""Exact role-information diagnostics, not a new physical moment rule."""
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
def zero(M):return s.simplify(M)==s.zeros(*M.shape)
def serial(M):return [[str(x) for x in row] for row in M.tolist()]
cases=[]
for r in range(1,7):
    values=list(range(1,r+1)); V=s.Matrix([[a**k for a in values] for k in range(r)])
    assert V.det()!=0
    ranks=[V[:k,:].rank() for k in range(1,r+1)]
    assert ranks==list(range(1,r+1))
    for j in range(8):
        weights=s.Matrix([(a+j+1)**2 for a in range(r)])
        weights=weights/sum(weights)
        moments=V*weights
        assert zero(V.inv()*moments-weights)
        cases.append(dict(distinct_eigenvalues=r,fixture=j,reconstruction=True))

J=s.diag(1,2,3); I=s.eye(3)
m1,m2=s.symbols('m1 m2',real=True)
V=s.Matrix([[a**k for a in [1,2,3]] for k in range(3)])
p=s.simplify(V.inv()*s.Matrix([1,m1,m2]))
assert p==s.Matrix([(m2-5*m1+6)/2,-m2+4*m1-3,(m2-3*m1+2)/2])
fixed=s.simplify(p.subs(m1,2))
for theta in [s.Rational(1,8),s.Rational(1,4)]:
    assert zero(fixed.subs(m2,4+2*theta)-s.Matrix([theta,1-2*theta,theta]))

# Degenerate eigenspaces: equal component norms imply an explicit block-unitary equivalence.
Jdeg=s.diag(1,1,3)
q=s.Matrix([1/s.sqrt(2),0,1/s.sqrt(2)])
U=s.diag(s.Matrix([[1,1],[1,-1]])/s.sqrt(2),s.Integer(1)); w=U*q
assert zero(U.T*U-I) and zero(U*Jdeg-Jdeg*U)
assert all(s.simplify((q.T*Jdeg**k*q)[0]-(w.T*Jdeg**k*w)[0])==0 for k in range(5))

# Mixed densities are not reconstructed by moments of one operator.
rho1=I/3; rho2=rho1+s.Matrix([[0,s.Rational(1,12),0],[s.Rational(1,12),0,0],[0,0,0]])
assert all(v>0 for v in rho2.eigenvals())
assert all(s.trace(rho1*J**k)==s.trace(rho2*J**k) for k in range(9))
assert s.trace(rho1**2)!=s.trace(rho2**2)

# Fixed complete state/J moments and primitive roles still permit distinct quadratic
# responses in the packet that has no identification of old N with C_N(Y).
q=s.Matrix([s.sqrt(2)/4,s.sqrt(3)/2,s.sqrt(2)/4])
Eexp=J.inv(); F=J.inv()**2; R=J*F*J
assert zero(R-I) and zero(Eexp*J-I)
H=s.diag(4,3,5); Hh=H**s.Rational(1,2)
responses=[]
for Y in [J/s.trace(J),(J/s.trace(J))**2]:
    L=Hh.inv()*Y**s.Rational(1,2); M=I
    assert zero(Hh*L*M.inv()*L.T*Hh-Y)
    B=-H*L; N=M+L.T*H*L
    E=s.simplify(H-B*N.inv()*B.T)
    assert zero(E-Hh*(I+Y).inv()*Hh)
    assert all(v>0 for v in E.eigenvals())
    responses.append(dict(Y=serial(Y),E=serial(E),primitive_roles_unchanged=True))
assert responses[0]['Y']!=responses[1]['Y'] and responses[0]['E']!=responses[1]['E']
J2=s.diag(1,2); H2=s.diag(4,3); H2h=H2**s.Rational(1,2)
assert s.Matrix([[1,1],[1,2]]).inv()*s.Matrix([1,s.Rational(3,2)])==s.Matrix([s.Rational(1,2),s.Rational(1,2)])
two_mode=[]
for Y in [J2/s.trace(J2),(J2/s.trace(J2))**2]:
    L=H2h.inv()*Y**s.Rational(1,2)
    assert zero(H2h*L*L.T*H2h-Y)
    Ered=s.simplify(H2h*(s.eye(2)+Y).inv()*H2h)
    two_mode.append(dict(Y=serial(Y),E=serial(Ered)))
assert two_mode[0]['Y']!=two_mode[1]['Y']

result=dict(status='PASS',exact_moment_reconstruction_cases=len(cases),tested_distinct_eigenvalues=[1,2,3,4,5,6],
    normalized_three_mode_weights=[str(x) for x in p],mean_two_weights=[str(x) for x in fixed],
    degenerate_eigenspace_unitary_certificate=True,
    mixed_density_counterexample=dict(purity_a=str(s.trace(rho1**2)),purity_b=str(s.trace(rho2**2)),
        equal_power_moments_checked=9),
    same_state_primitive_roles_and_complete_moments_two_responses=responses,
    two_mode_mean_information_fixes_pure_class=True,two_mode_same_class_two_responses=two_mode,
    complete_pure_state_joint_class_given_moment_values=True,
    source_fixes_those_moment_values=False,
    moments_determine_mixed_density_joint_class=False,
    complete_state_moments_alone_fix_initial_Y=False,
    full_historical_independence_theorem=False,new_physical_rule_adopted=False,event_rule_modified=False)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
