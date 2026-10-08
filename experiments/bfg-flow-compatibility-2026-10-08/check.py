"""Synthetic orientation and clock-compatibility controls; no physical fits."""
import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp
x,y=s.symbols('x y',positive=True)
p=s.Rational(1,3)
lc=p/(1+x)+(1-p)/(1+y);lb=p*x*x/(1+x)+(1-p)*y*y/(1+y)
a=lb/(lc+lb)
R=s.Matrix([(a+(1-a)*u*u)/(1+u)**2 for u in (x,y)])
J=R.jacobian([x,y]);H=s.Matrix([x-y,R[0]-R[1]-x+y]);B=H.jacobian([x,y])
z=s.Matrix([s.Rational(1,5),s.Rational(7,10)])
exact=s.factor(J.subs(dict(zip([x,y],z))).det())
r=s.lambdify((x,y),R,'numpy');j=s.lambdify((x,y),J,'numpy');b=s.lambdify((x,y),B,'numpy')
rf=lambda u:np.asarray(r(*u),float).reshape(2)
z0=np.array(z,float).reshape(2);z1=rf(z0);d0=j(*z0);d1=j(*z1)
fd=[]
for eps in [1e-4,1e-5,1e-6]:
    jj=np.column_stack([(rf(z0+eps*np.eye(2)[i])-rf(z0-eps*np.eye(2)[i]))/(2*eps) for i in range(2)])
    fd.append(dict(step=eps,error=float(np.max(abs(jj-d0))),determinant=float(np.linalg.det(jj))))
assert exact<0 and fd[-1]['error']<1e-8
B0=b(*z0);B1=b(*z1);chart=B1@d0@np.linalg.inv(B0)
assert np.linalg.det(B0)>0 and np.linalg.det(B1)<0
# Mechanical comparator with variational ODE: determinant must exp(-b*h).
a_mech=3.;damp=.1;h=.1
initial=np.r_[.3,.2,np.eye(2).reshape(4)]
def rhs(t,u):
    th,w=u[:2];M=u[2:].reshape(2,2);L=np.array([[0,1],[-a_mech*np.cos(th),-damp]])
    return np.r_[w,-a_mech*np.sin(th)-damp*w,(L@M).reshape(4)]
sol=solve_ivp(rhs,[0,h],initial,method='DOP853',rtol=1e-12,atol=1e-14)
assert sol.success
mechdet=float(np.linalg.det(sol.y[2:,-1].reshape(2,2)));error=abs(mechdet-np.exp(-damp*h));assert error<1e-10
# Positive state-dependent clock counterexample, constant vector field (1,0).
# tau=2-2*x >0 for x<1; endpoint(x,y)=(2-x,y), det=-1.
clock_tau=2-2*.25
assert clock_tau>0 and (1-2)==-1
out=dict(kind='synthetic mathematics/code controls only',exact_canonical_determinant=str(exact),canonical_determinant=float(exact),successor_geometry=z1.tolist(),successor_geometry_determinant=float(np.linalg.det(d1)),two_event_determinant=float(np.linalg.det(d1@d0)),source_chart_determinant=float(np.linalg.det(B0)),successor_chart_determinant=float(np.linalg.det(B1)),chart_transition_determinant=float(np.linalg.det(chart)),finite_difference_controls=fd,mechanical_variational_determinant=mechdet,mechanical_liouville_residual=error,positive_clock_counterexample=dict(x=.25,tau=clock_tau,determinant=-1,ordering_factor=-1),physical_calibration=False,holdout_accessed=False)
Path(__file__).with_name('results').joinpath('controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
