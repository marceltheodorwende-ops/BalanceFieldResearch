import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.optimize import root
from experiment import update
x,y=s.symbols('x y',positive=True)
lc=1/(1+x)+2/(1+y);lb=x*x/(1+x)+2*y*y/(1+y);a=lb/(lc+lb)
R=s.Matrix([(a+(1-a)*u*u)/(1+u)**2 for u in (x,y)])
J=R.jacobian((x,y));z=np.array([.2,.7]);rf=s.lambdify((x,y),R,'numpy');jf=s.lambdify((x,y),J,'numpy')
r=lambda u:np.asarray(rf(*u),float).reshape(2)
det=s.factor(J.subs({x:s.Rational(1,5),y:s.Rational(7,10)}).det());assert det== -s.Rational(321243859375,52720394616576)
j=np.asarray(jf(*z),float);eps=1e-6
fd=np.column_stack([(r(z+eps*e)-r(z-eps*e))/(2*eps) for e in np.eye(2)])
assert np.max(abs(fd-j))<1e-8
res=[];amb=[];controls=[]
for delta in ([1e-5,0],[0,1e-5],[-1e-5,1e-5],[2e-5,-1e-5]):
 target=r(z)+delta
 sol=root(lambda u:r(u)-target,z,jac=lambda u:np.asarray(jf(*u),float),tol=1e-11)
 assert np.max(abs(r(sol.x)-target))<1e-12 and np.all(sol.x>0) and np.all(sol.x<1)
 d=sol.x-z;controls.append(d.tolist());res.append(float(np.max(abs(r(sol.x)-target))))
 out=update(np.eye(2),np.diag([1.,2.]),np.eye(2)/2,np.diag(sol.x),np.eye(2));assert out['terminal'] is None
 natural=out['v']@out['y']@out['v'].conj().T
 amb.append(float(np.max(abs(natural-np.diag(target)))))
 assert max(target)<=max(sol.x)/2+1e-14
assert max(amb)<1e-10
# Linearized scalar actuator cannot span the orthogonal target direction.
b=j@np.ones(2);normal=np.array([-b[1],b[0]]);normal/=np.linalg.norm(normal)
assert abs(normal@b)<1e-14
result=dict(kind='synthetic mathematics/code controls only',exact_determinant=str(det),jacobian_difference=float(np.max(abs(fd-j))),inverse_condition_number=float(np.linalg.cond(j)),inverse_norm=float(np.linalg.norm(np.linalg.inv(j),2)),max_inverse_residual=max(res),max_ambient_residual=max(amb),inputs=controls,scalar_unreachable_unit_direction=normal.tolist(),physical_input_calibrated=False,force_derived=False,holdout_accessed=False)
Path(__file__).with_name('results').joinpath('controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
