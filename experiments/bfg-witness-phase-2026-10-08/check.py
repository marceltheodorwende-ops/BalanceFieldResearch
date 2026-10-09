"""P54 synthetic controls. Import canonical update only; no evaluate/data access.
From repository root: PYTHONPATH=experiments/real-eeg-covariance-2026-10-07 python experiments/bfg-witness-phase-2026-10-08/check.py
"""
import json
from pathlib import Path
import numpy as np
import sympy as sp
from experiment import update
S=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex);I=np.eye(2)
def split(A):return np.trace(A).real/2,np.array([np.trace(A@v).real/2 for v in S])
def phase(Y,J,W):
    t,y=split(Y);_,j=split(J);_,w=split(W);r=np.linalg.norm(y);s=np.linalg.norm(j);a=np.linalg.norm(w)
    return np.arctan2(j@np.cross(w,y)/(s*a*r),w@y/(a*r))
def circle_error(a,b):return abs(np.angle(np.exp(1j*(a-b))))
def params(t,h):
    u=np.array([t+h,t-h]);c=1/(1+u);b=u*c;m=(u*u*c).sum()/c.sum();alpha=m/(1+m)
    ev=alpha*c*c+(1-alpha)*b*b;g=(alpha*np.prod(c)+(1-alpha)*np.prod(b))/np.sqrt(np.prod(ev))
    return ev.mean(),(ev[0]-ev[1])/2,g
rng=np.random.default_rng(54);errs=[];gau=[];we=[]
for _ in range(60):
    t=rng.uniform(.25,.7);s=rng.uniform(.1,.8);h=rng.uniform(.02,.8*min(t,1-t));r=h/np.sqrt(1+.04*s*s);phi=rng.uniform(-np.pi,np.pi);a=rng.uniform(.1,.45)
    Y=t*I+r*(np.cos(phi)*S[0]+np.sin(phi)*S[1]);J=s*S[2];W=I/2+a*S[0];Z=Y+.1j*(Y@J-J@Y)
    oo=update(J,1.7*I,W,Z,I);assert oo['terminal'] is None;V=oo['v'];yn=V@oo['y']@V.conj().T;jn=V@oo['k']@V.conj().T;wn=V@oo['w']@V.conj().T
    tt,rr,g=params(t,h);assert rr>0 and 0<g<1
    phin=phase(yn,jn,wn);expected=phi+np.arctan(.2*s);errs.append(float(circle_error(phin,expected)));we.append(float(np.max(abs(wn-W))))
    q,_=np.linalg.qr(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)));out=update(q.conj().T@J@q,1.7*I,q.conj().T@W@q,q.conj().T@Z@q,I)
    gau.append(float(circle_error(phase(out['y'],out['k'],out['w']),expected)))
assert max(errs)<1e-10 and max(gau)<1e-10 and max(we)<1e-10
# Exact hidden-amplitude derivative of gamma² at a rational point; no finite difference proof.
t,h=sp.symbols('t h',real=True);u=[t+h,t-h];c=[1/(1+x) for x in u];b=[x*cc for x,cc in zip(u,c)];m=sum(x*x*cc for x,cc in zip(u,c))/sum(c);alpha=m/(1+m)
ev=[alpha*cc**2+(1-alpha)*bb**2 for cc,bb in zip(c,b)];g2=(alpha*c[0]*c[1]+(1-alpha)*b[0]*b[1])**2/(ev[0]*ev[1]);point={t:sp.Rational(9,20),h:sp.Rational(3,25)}
m_closed=t*t+h*h*(1-t)/(1+t);assert sp.cancel(m-m_closed)==0
assert sp.cancel(ev[0]-ev[1]-4*h*(t-t**3-h*h*(2-t))/((1+m)*(1+u[0])**2*(1+u[1])**2))==0
dg2=sp.factor(sp.diff(g2,h).subs(point));assert dg2!=0
# Same (phi,s) with different admissible h changes s+, hence destroys pair closure.
left=params(.45,.12);right=params(.45,.2);gap=abs(.3*(left[2]-right[2]));assert gap>1e-5
# Squared-potential candidates are unconstrained in their coefficient; endpoint contains no seconds.
res=dict(cases=60,max_phase_endpoint_error=max(errs),max_gauge_phase_error=max(gau),max_witness_inheritance_error=max(we),exact_hidden_amplitude_derivative_gamma_squared=str(dg2),same_phase_kernel_pair_successor_gap=gap,phase_increment_at_s_point=float(np.arctan(.06)),kind='synthetic mathematics/code controls',physical_force_derived=False,seconds_calibrated=False,holdout_accessed=False)
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
