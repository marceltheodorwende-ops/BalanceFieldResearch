"""Exact normalization, joint-orbit and residual quotient diagnostics.
The enumerated finite source packet is not every historical BFG axiom.
"""
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
def zero(M):return s.simplify(M)==s.zeros(*M.shape)
def serial(M):return [[str(v) for v in row] for row in M.tolist()]

I=s.eye(3); J=s.diag(1,2,3); E=J.inv(); B=I; N=I
F=J.inv()**2; R=J*F*J
assert zero(R-I) and zero(E*J-B*N)
theta=s.symbols('theta',positive=True)
v=s.Matrix([s.sqrt(theta),s.sqrt(1-2*theta),s.sqrt(theta)])
assert s.simplify((v.T*v)[0])==1
assert s.simplify((v.T*J*v)[0])==2
assert s.simplify((v.T*J**2*v)[0])==4+2*theta
records=[]
for t in [s.Rational(1,8),s.Rational(1,4)]:
    q=v.subs(theta,t); tangent=s.simplify(v.diff(theta).subs(theta,t))
    constraints=(2*q.T).col_join(2*q.T*J)
    assert constraints.rank()==2 and zero(constraints*tangent)
    assert tangent!=s.zeros(3,1)
    assert s.simplify((2*q.T*J**2*tangent)[0])==2
    assert s.simplify((q.T*E*J*q)[0]/(q.T*B*N*q)[0])==1
    assert zero(R*q-q)
    # The common stabilizer of a simple J is diagonal; it preserves each |q_j|^2.
    xs=s.symbols('u:9'); X=s.Matrix(3,3,xs)
    equations=list(X*J-J*X)
    linear,_=s.linear_eq_to_matrix(equations,xs)
    assert len(linear.nullspace())==3
    records.append(dict(theta=str(t),state=serial(q),norm_squared='1',information='2',
        second_information_moment=str((q.T*J**2*q)[0]),balance='1',
        scalar_feedback='A=0, B=1/2, IB=0',recursive_radius='1',
        power_bound='1',interface_drift='0',Lyapunov_cost='0',
        constraint_rank=2,real_horizontal_tangent_dimension=1,
        invariant_derivative_along_tangent='2'))
assert records[0]['second_information_moment']=='17/4'
assert records[1]['second_information_moment']=='9/2'

# The actual displayed cost, with scalar neutral variation n I and Frobenius interface norm.
x=s.Matrix(s.symbols('x0:3',real=True)); n=s.symbols('n',positive=True)
lr,ln=s.symbols('lambda_R lambda_N',positive=True)
cost=(1/n-1)**2/2+lr*(1/n-1)**2*(x.T*x)[0]+3*ln*(n-1)**2
for t in [s.Rational(1,8),s.Rational(1,4)]:
    q=v.subs(theta,t); point=dict(zip(x,q));point[n]=1
    Hess=s.simplify(s.hessian(cost,[*x,n]).subs(point))
    assert zero(Hess[:3,:3]) and zero(Hess[:3,3:])
    assert Hess[3,3]==1+2*lr+6*ln

# Quotient criterion: ker(D|T)=V gives positive residual Hessian on T/V.
good=s.diag(1,2,0); bad=s.diag(1,0,0); horizontal=s.Matrix([[1,0],[0,1],[0,0]])
good_reduced=horizontal.T*good.T*good*horizontal
bad_reduced=horizontal.T*bad.T*bad*horizontal
assert good_reduced==s.diag(1,4) and bad_reduced==s.diag(1,0)
assert len(good.nullspace())==1 and len(bad.nullspace())==2

# The real simple-ground exact formation set has no continuous profile variation.
K=s.diag(-2,1,3); ground=s.Matrix([s.sqrt(2),0,0])
quartic=(x.T*K*x)[0]/2+((x.T*x)[0])**2/4
formed_hessian=s.simplify(s.hessian(quartic,list(x)).subs(dict(zip(x,ground))))
assert formed_hessian==s.diag(4,3,5)
assert all(s.simplify(s.diff(quartic,y).subs(dict(zip(x,ground))))==0 for y in x)

result=dict(status='PASS',fixed_operators=dict(information=serial(J),expansion=serial(E),
    binding=serial(B),neutral=serial(N),feedback_operator=serial(F),raw_recursion=serial(R)),
    normalized_fixed_information_family=records,joint_unitary_classes_distinct=True,
    flat_direction_survives_normalization_and_fixed_information=True,
    scalar_neutral_cost_Hessian_diagonal=['0','0','0','1+2*lambda_R+6*lambda_N'],
    quotient_positive_control=serial(good_reduced),quotient_singular_control=serial(bad_reduced),
    exact_real_formation_Hessian=serial(formed_hessian),
    all_plugin_dynamics_and_origin_axioms_realized=False,
    source_selects_initial_reduced_response=False,
    equivalence_identified_with_full_nine_role_state=False,
    new_physical_rule_adopted=False,event_rule_modified=False)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
