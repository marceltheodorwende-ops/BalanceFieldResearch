"""Exact Hessian and elimination diagnostics for a bounded BFG source audit."""
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
def zero(M):return s.simplify(M)==s.zeros(*M.shape)
def serial(M):return [[str(v) for v in row] for row in M.tolist()]
x,z=s.symbols('x z',real=True)
H=s.diag(4,3); d=s.Matrix([x,z]); eta=s.symbols('eta',real=True)
L=s.Matrix([s.Rational(1,4),s.Rational(1,3)]); M=s.Integer(2)
base=((d-L*eta).T*H*(d-L*eta))[0]/2+M*eta**2/2
records=[]
for label,J,g in [('source_quartic_added',base+(eta-x)**4,x**4),
                  ('shared_joint_nonlinearity',base+(eta-x)**4,0)]:
    # Hessian of nonlinear assessment at zero; quartic terms do not affect it.
    J=J+g
    Q=s.hessian(J,(x,z,eta)).subs({x:0,z:0,eta:0})
    B=Q[:2,2:]; N=Q[2:,2:]
    E=s.simplify(Q[:2,:2]-B*N.inv()*B.T)
    assert zero(Q[:2,:2]-H) and N[0,0]>0
    a=s.simplify(-N.inv()*B.T*d)[0]
    # Any smooth minimizing branch has this first derivative by its stationarity equation.
    assert s.diff(J,eta).subs({x:0,z:0,eta:0})==0
    assert zero(s.hessian(J.subs(eta,a),(x,z)).subs({x:0,z:0})-E)
    Hh=s.diag(2,s.sqrt(3)); Y=s.simplify(Hh*E.inv()*Hh-s.eye(2))
    assert all(v>=0 for v in Y.eigenvals())
    records.append(dict(name=label,source_block=serial(H),mixed_block=serial(B),
                        neutral_block=serial(N),reduced_Hessian=serial(E),Y=serial(Y)))
assert records[0]['reduced_Hessian']==records[1]['reduced_Hessian']

# Nonlinear source coordinate changes at and away from a critical point.
u,a=s.symbols('u a',real=True)
coord=u+a*u**2
noncritical=s.diff((x+x**2/2).subs(x,coord),u,2).subs(u,0)
critical=s.diff((x**2/2).subs(x,coord),u,2).subs(u,0)
assert noncritical==1+2*a and critical==1

# Scalar specialization of the May neutral-interface Lyapunov expression.
state,n=s.symbols('state n',real=True,positive=True)
lr,ln=s.symbols('lambda_R lambda_N',positive=True)
Phi=1/n; RN=1/n
LC=(Phi-1)**2/2+lr*(RN*state-state)**2+ln*(n-1)**2
HLC=s.simplify(s.hessian(LC,(state,n)).subs({state:1,n:1}))
assert HLC==s.diag(0,1+2*lr+2*ln)
assert s.simplify(LC.subs(n,1))==0
assert all(s.simplify(s.diff(LC,t).subs({state:1,n:1}))==0 for t in (state,n))

# General least-squares residual identity in an exact nonlinear fixture.
r=s.Matrix([x+eta+x*z,z-eta**2]); lam=s.diag(2,3)
score=(r.T*lam*r)[0]/2
Jr=r.jacobian([x,z,eta]).subs({x:0,z:0,eta:0})
assert zero(s.hessian(score,(x,z,eta)).subs({x:0,z:0,eta:0})-Jr.T*lam*Jr)
assert Jr.rank()==2

# The source's local resolvent potential already depends on supplied Y.
y0,aa,bb=s.symbols('y0 aa bb',real=True)
Yq=y0+aa*x+bb*x**2/2; C=1/(1+Yq)
assert s.simplify(s.diff(C,x)+C*s.diff(Yq,x)*C)==0
assert s.simplify(s.diff(C,x,2)-(2*C**3*s.diff(Yq,x)**2-C**2*s.diff(Yq,x,2)))==0
V=x**2*C/2
assert s.simplify(s.diff(V,x,2).subs(x,0))==1/(1+y0)
# Nonnegative potential does not alone ensure a positive Hessian.
Vmax=1/(2*(2+x**2))
assert s.diff(Vmax,x).subs(x,0)==0 and s.diff(Vmax,x,2).subs(x,0)==-s.Rational(1,4)

# Original quartic has a positive source Hessian, with no neutral argument.
K=s.diag(-2,1)
quartic=(d.T*K*d)[0]/2+(d.dot(d))**2/4
formed=s.simplify(s.hessian(quartic,(x,z)).subs({x:s.sqrt(2),z:0}))
assert formed==H
result=dict(status='PASS',nonlinear_local_reduction=records,
    nonlinear_same_second_order_different_fourth_order=True,
    coordinate_change=dict(noncritical_Hessian=str(noncritical),critical_Hessian=str(critical)),
    source_Lyapunov_specialization=dict(Hessian=serial(HLC),flat_source_direction=True,
        scope='Scalar algebraic role specialization with E=B=I=R=1, N_star=1 and G=0; not a realization of every historical dynamics.'),
    residual_Gram_identity=True,residual_jacobian_rank=2,
    resolvent_derivative_identities=True,zero_profile_potential_Hessian=str(1/(1+y0)),
    positive_potential_negative_Hessian='-1/4',formed_quartic_Hessian=serial(formed),
    accepted_source_functional_to_initial_E_derived=False,
    local_Hessian_equals_full_nonlinear_law=False,
    source_Gram_rule_replaced=False,new_physical_rule_adopted=False,event_rule_modified=False)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
