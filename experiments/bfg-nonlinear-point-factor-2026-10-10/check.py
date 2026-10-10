"""Symbolic and synthetic controls only; does not load measurements."""
import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp
from scipy.linalg import expm
q,p,Q,W=s.symbols('q p Q W',real=True)
k,g,I=s.symbols('k g I',positive=True)
h=s.Function('h')(q)
L=lambda f:p*s.diff(f,q)+(-k*q-g*p)*s.diff(f,p)
hp=s.diff(h,q); hpp=s.diff(h,q,2)
checks=[]
def ck(name,z):
    assert s.simplify(s.trigsimp(z))==0,name
    checks.append(name)
ck('general chain',L(hp*p)-(hpp*p*p-hp*k*q-g*hp*p))
ck('point rank',s.det(s.Matrix([[hp,0],[hpp*p,hp]]))-hp*hp)
alpha=s.symbols('alpha',positive=True)
f=2*s.asin(alpha*q); fp=s.diff(f,q); fpp=s.diff(f,q,2)
ck('arcsine velocity square',fpp/fp**2-alpha*q/(2*s.sqrt(1-alpha**2*q**2)))
ck('arcsine restoring',q*fp-2*alpha*q/s.sqrt(1-alpha**2*q**2))
m=I/(4*alpha**2)*s.cos(Q/2)**2
U=I*k/(4*alpha**2)*(1-s.cos(Q))
r=s.tan(Q/2)*W*W/2-2*k*s.tan(Q/2)-g*W
ck('variable mass balance',m*r+s.diff(m,Q)*W*W/2+s.diff(U,Q)+g*m*W)
E=m*W*W/2+U
ck('energy',s.diff(E,Q)*W+s.diff(E,W)*r+g*m*W*W)
ck('constant inertia obstruction coefficient',s.diff((hpp/hp**2)*W**2-g*W-k*q*hp,W,2)-2*hpp/hp**2)
ck('impulse energy',m*((W+s.Symbol('kick'))**2-W**2)/2-m*(W*s.Symbol('kick')+s.Symbol('kick')**2/2))
# Freeze code-control domain, parameters and tolerances before integration.
cases=[]
for al,z0,clock in [(0.5,np.array([0.3,0.12]),0.2),(0.8,np.array([0.9,-0.05]),0.4),(0.5,np.array([1.98,0.0]),0.05)]:
    kn,gn=1.3,0.2
    F=np.array([[0.,1.],[-kn,-gn]])
    H=lambda z:np.array([2*np.arcsin(al*z[0]),2*al*z[1]/np.sqrt(1-al**2*z[0]**2)])
    DH=lambda z:np.array([[2*al/np.sqrt(1-al**2*z[0]**2),0.],[2*al**3*z[0]*z[1]/(1-al**2*z[0]**2)**1.5,2*al/np.sqrt(1-al**2*z[0]**2)]])
    def rhs(t,y):
        a,b=y[:2]; tan=np.tan(a/2)
        out=np.array([b,.5*tan*b*b-2*kn*tan-gn*b])
        J=np.array([[0.,1.],[.25/(np.cos(a/2)**2)*b*b-kn/(np.cos(a/2)**2),tan*b-gn]])
        return np.r_[out,(J@y[2:].reshape(2,2)).ravel()]
    y0=np.r_[H(z0),np.eye(2).ravel()]
    sol=solve_ivp(rhs,[0,clock],y0,rtol=2e-11,atol=2e-12,method='DOP853')
    assert sol.success
    M=expm(clock*F); end=M@z0
    ref=H(end); tangent=DH(end)@M@np.linalg.inv(DH(z0))
    endpoint_error=float(np.max(abs(sol.y[:2,-1]-ref)))
    tangent_error=float(np.max(abs(sol.y[2:,-1].reshape(2,2)-tangent)))
    assert endpoint_error<2e-8 and tangent_error<2e-7
    d=1-al**2*z0[0]**2
    cases.append(dict(alpha=al,initial=z0.tolist(),clock=clock,domain_margin=d,forward_angle_gain=2*al/np.sqrt(d),endpoint_error=endpoint_error,tangent_error=tangent_error))
# Adverse conditioning, compact finite disturbances and affine/polynomial controls.
rho,Pmax,al=.8,.5,.7
d=1-rho*rho; gainQ=2*al/np.sqrt(d); gainWp= gainQ; gainWq=2*al*al*rho*Pmax/d**1.5
z=np.array([.6,.2]); perturb=np.array([1e-5,-2e-5]); z2=z+perturb
H=lambda z:np.array([2*np.arcsin(al*z[0]),2*al*z[1]/np.sqrt(1-al**2*z[0]**2)])
error=abs(H(z2)-H(z)); bound=np.array([gainQ*abs(perturb[0]),gainWq*abs(perturb[0])+gainWp*abs(perturb[1])])
assert np.all(error<=bound+1e-14)
epsilon=s.symbols('epsilon',nonnegative=True)
poly=q+epsilon*q**3
ck('polynomial curvature',s.diff(poly,q,2)/s.diff(poly,q)**2-6*epsilon*q/(1+3*epsilon*q*q)**2)
ck('affine no curvature',s.diff(2*q+1,q,2))
result=dict(symbolic_checks=checks,synthetic_ode_cases=cases,thresholds=dict(endpoint=2e-8,tangent=2e-7,rtol=2e-11,atol=2e-12),perturbation=dict(rho=rho,Pmax=Pmax,alpha=al,error=error.tolist(),bound=bound.tolist()),scope='Exact transformed harmonic-readout control; no empirical pendulum confirmation or physical calibration')
Path(__file__).with_name('controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(symbolic_checks=len(checks),ode_cases=len(cases),max_endpoint_error=max(z['endpoint_error'] for z in cases),max_tangent_error=max(z['tangent_error'] for z in cases))))
