"""Synthetic controls for an internally derived geometry delay chart."""
import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.optimize import root
from experiment import update
x,y=s.symbols('x y',positive=True)
p=s.Rational(1,3)
lc=p/(1+x)+(1-p)/(1+y)
lb=p*x*x/(1+x)+(1-p)*y*y/(1+y)
a=lb/(lc+lb)
r=s.Matrix([(a+(1-a)*v*v)/(1+v)**2 for v in (x,y)])
g=x-y
H=s.Matrix([g,r[0]-r[1]-g])
J=H.jacobian([x,y])
f=s.lambdify((x,y),r,'numpy');obs=s.lambdify((x,y),H,'numpy');jac=s.lambdify((x,y),J,'numpy')
R=lambda z:np.asarray(f(*z),float).reshape(2)
O=lambda z:np.asarray(obs(*z),float).reshape(2)
z=np.array([.2,.7]);exact=s.factor(J.subs({x:s.Rational(1,5),y:s.Rational(7,10)}).det())
exact_dr=s.factor(r.jacobian([x,y]).subs({x:s.Rational(1,5),y:s.Rational(7,10)}).det())
assert exact!=0 and exact_dr!=0
rng=np.random.default_rng(1008);ambient=[];fd=[];inverse=[]
for _ in range(40):
    zz=z+rng.uniform(-.002,.002,2)
    F=np.diag([1.,2.]);K=np.array([[1.,.2j],[-.2j,-1.]])
    out=update(K,F,np.eye(2)/2,np.diag(zz),np.eye(2))
    assert out['terminal'] is None
    back=out['v']@out['y']@out['v'].conj().T
    ambient.append(float(np.max(abs(back-np.diag(R(zz))))))
    eps=1e-6
    numeric=np.column_stack([(O(zz+eps*np.eye(2)[j])-O(zz-eps*np.eye(2)[j]))/(2*eps) for j in range(2)])
    fd.append(float(np.max(abs(numeric-jac(*zz)))))
    sol=root(lambda u:O(u)-O(zz),z,tol=1e-11)
    assert sol.success
    inverse.append(float(np.max(abs(sol.x-zz))))
assert max(ambient)<1e-10 and max(fd)<1e-7 and max(inverse)<1e-8
nextz=R(z);second=R(nextz)
# Exact internal kinematic identity, with h=A=1 for code control only.
q=O(z);qn=O(nextz)
assert abs(qn[0]-q[0]-q[1])<1e-14
# Collision counter-limit: symmetry forces det DH=0 at x=y.
assert s.simplify(J.subs(y,x).det())==0
result=dict(kind='synthetic mathematics/code controls only',weights=[1/3,2/3],initial_geometry=z.tolist(),exact_chart_determinant=str(exact),chart_determinant=float(exact),exact_geometry_determinant=str(exact_dr),geometry_determinant=float(exact_dr),chart_condition=float(np.linalg.cond(jac(*z))),initial_chart=q.tolist(),successor_geometry=nextz.tolist(),successor_chart=qn.tolist(),event_acceleration=float(qn[1]-q[1]),successor_chart_determinant=float(np.linalg.det(jac(*nextz))),max_ambient_residual=max(ambient),max_derivative_residual=max(fd),max_inverse_residual=max(inverse),cases=40,physical_seconds_calibrated=False,physical_force_derived=False,holdout_accessed=False)
Path(__file__).with_name('results').joinpath('controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
