"""Finite independent algebra and synthetic controls; never reads measurements."""
import json
from pathlib import Path
import sympy as s
import numpy as np
from scipy.special import jv
from scipy.linalg import expm
x,t,c=s.symbols('x theta c',real=True,nonzero=True)
A,v,w=(s.Function(n)(x) for n in ('A','v','Omega'))
L=lambda z:v*s.diff(z,x)+w*s.diff(z,t)
Q=A*s.cos(t); V=L(Q)/c; R=L(V)/c
D=v*v*s.diff(A,x,2)+v*s.diff(v,x)*s.diff(A,x)-A*w*w
E=2*v*s.diff(A,x)*w+v*A*s.diff(w,x)
B=v*s.diff(A,x); C=A*w
checks=[]
def check(name,z):
    assert s.simplify(s.expand(z))==0,name
    checks.append(name)
check('chain acceleration',R-(D*s.cos(t)-E*s.sin(t))/c**2)
det=s.det(s.Matrix([[s.diff(Q,x),s.diff(Q,t)],[s.diff(V,x),s.diff(V,t)]]))
expected=((A*s.diff(B,x)-s.diff(A,x)*B)*s.sin(t)*s.cos(t)-s.diff(A,x)*C*s.cos(t)**2-A*s.diff(C,x)*s.sin(t)**2)/c
check('observation determinant',det-expected)
ell=E/(A*w*c); k=(D-E*v*s.diff(A,x)/(A*w))/(A*c*c)
check('force elimination',R-k*Q-ell*V)
gamma,kappa=s.symbols('gamma kappa',real=True)
check('linear force coefficients',R+kappa*Q+gamma*V-((D+kappa*c*c*A+gamma*c*B)*s.cos(t)+(-E-gamma*c*C)*s.sin(t))/c**2)
a,delta,nu,u=s.symbols('a delta nu u',positive=True)
q=a*s.exp(-delta*u)*s.cos(t)
Lu=lambda z:s.diff(z,u)+nu*s.diff(z,t)
vq=Lu(q)/c; rq=Lu(vq)/c
check('linear positive control',rq+(delta*delta+nu*nu)/c**2*q+2*delta/c*vq)
detcontrol=s.det(s.Matrix([[s.diff(q,u),s.diff(q,t)],[s.diff(vq,u),s.diff(vq,t)]]))
check('rank positive control',detcontrol-delta*a*a*s.exp(-2*delta*u)*nu/c)
I=s.symbols('I',positive=True)
energy=I*(vq*vq+(delta*delta+nu*nu)/c**2*q*q)/2
check('energy derivative',Lu(energy)/c+I*2*delta/c*vq*vq)
amp=s.symbols('amp',positive=True)
f=s.sin(amp*s.cos(t))
check('nonharmonic diagnostic',s.diff(s.diff(f,t,2)+f,t).subs(t,s.pi/2)-amp**3)
phi=2*np.pi*np.arange(16384)/16384
cases=[]
for amplitude in [.1,.7,1.5]:
    values=np.sin(amplitude*np.cos(phi))
    third=float(2*np.mean(values*np.cos(3*phi)))
    expectedthird=float(-2*jv(3,amplitude))
    err=abs(third-expectedthird)
    small=float(np.max(abs(values-amplitude*np.cos(phi))))
    assert err<1e-12
    assert small<=amplitude**3/6+1e-14
    assert abs(third)>1e-6
    cases.append(dict(amplitude=amplitude,third_harmonic=third,bessel_expected=expectedthird,quadrature_error=err,small_angle_max_error=small,cubic_bound=amplitude**3/6))
endpoint_cases=[]
for decay, frequency, clock in [(0.1,0.7,0.03),(0.4,1.9,0.2)]:
    kappa_num=(decay**2+frequency**2)/clock**2
    gamma_num=2*decay/clock
    factor=expm(clock*np.array([[0,1],[-kappa_num,-gamma_num]]))
    co,si=np.cos(frequency),np.sin(frequency)
    direct=np.exp(-decay)*np.array([[co+decay/frequency*si,clock/frequency*si],[-(decay**2+frequency**2)/(clock*frequency)*si,co-decay/frequency*si]])
    discrepancy=float(np.max(abs(factor-direct)))
    assert discrepancy<1e-11
    endpoint_cases.append(dict(decay=decay,frequency=frequency,clock=clock,matrix_exponential_discrepancy=discrepancy))
result=dict(endpoint_cases=endpoint_cases,symbolic_checks=checks,synthetic_cases=cases,numerical_threshold=1e-12,scope='Algebra/synthetic controls only; conditional harmonic readout factor, no physical selection or empirical confirmation')
Path(__file__).with_name('controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(symbolic_checks=len(checks),cases=len(cases),max_quadrature_error=max(z['quadrature_error'] for z in cases),endpoint_cases=len(endpoint_cases),max_endpoint_error=max(z['matrix_exponential_discrepancy'] for z in endpoint_cases))))
