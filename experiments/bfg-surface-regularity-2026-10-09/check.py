"""P61 synthetic derivative controls; no measurement access.
PYTHONPATH=experiments/real-eeg-covariance-2026-10-07 python check.py
Samples are not a calibration of the theorem's existential local radius.
"""
import json
from pathlib import Path
import sympy as sp
import mpmath as mp
import numpy as np
from experiment import update

t,q=sp.symbols('t q',positive=True);h=t*q
u=[t+h,t-h];c=[1/(1+y) for y in u];b=[y*z for y,z in zip(u,c)]
m=t*t+h*h*(1-t)/(1+t);al=m/(1+m);ev=[al*y*y+(1-al)*z*z for y,z in zip(c,b)]
A=sp.cancel(sum(ev)/2);V=sp.cancel((ev[0]-ev[1])/2);B=sp.cancel(V/(A*q))
g=sp.cancel((al*c[0]*c[1]+(1-al)*b[0]*b[1])**2/(ev[0]*ev[1]))
x,z=sp.symbols('x z',positive=True);d=1+x+x*x
AA=A.subs(q,sp.sqrt(x)*z);XX=x*g.subs(q,sp.sqrt(x)*z)
F2=z*z*B.subs(q,sp.sqrt(x)*z)**2*(1/g.subs(q,sp.sqrt(x)*z)+x)
assert sp.cancel(AA.subs(t,0))==0
assert sp.cancel(sp.diff(AA,t).subs(t,0))==0
assert sp.cancel(sp.diff(AA,t,2).subs(t,0)/2-2*(1+x*z*z))==0
assert sp.cancel(XX.subs({t:0,z:1})-x/d)==0
assert sp.cancel(sp.diff(x/d,x)-(1-x*x)/d**2)==0
assert sp.cancel(sp.diff(F2,x,2).subs({t:0,z:1}))==0
coef=4*(1+x)*(1-x*x)/d**2
assert sp.cancel(sp.diff(AA,t,2).subs({t:0,z:1})*sp.diff(x/d,x)-coef)==0
assert sp.simplify(sp.diff(sp.atan(sp.sqrt(x)),x)-1/(2*sp.sqrt(x)*(1+x)))==0
args=(t,x,z);forms=[AA,XX,F2]
ff=[sp.lambdify(args,v,'mpmath') for v in forms]
jj=[[sp.lambdify(args,sp.diff(v,w),'mpmath') for w in args] for v in forms]
hh=[[[sp.lambdify(args,sp.diff(v,wi,wj),'mpmath') for wj in args] for wi in args] for v in forms]
P=4*x**6+17*x**5+42*x**4+61*x**3+54*x**2+27*x+6
jet=1+(2+x)*t+P/d**2*t*t
jetf=sp.lambdify((t,x),jet,'mpmath');jetdf=[sp.lambdify((t,x),sp.diff(jet,v),'mpmath') for v in (t,x)]
jeth=[[sp.lambdify((t,x),sp.diff(jet,vi,vj),'mpmath') for vj in (t,x)] for vi in (t,x)]
mp.mp.dps=80

def event(tt,xx,zz):
    vals=[f(tt,xx,zz) for f in ff];f=mp.sqrt(vals[2])
    partials=[[p(tt,xx,zz) for p in row] for row in jj]
    partials[2]=[v/(2*f) for v in partials[2]]
    return [vals[0],vals[1],f],partials

def graph(tt,xx,n):
    if n==0:return jetf(tt,xx)
    def objective(zz):
        an,xn,fn=event(tt,xx,zz)[0];return fn-graph(an,xn,n-1)
    seed=jetf(tt,xx)
    return mp.findroot(objective,(seed,seed+tt*mp.mpf('.01')),tol=mp.mpf('1e-68'),verify=True)

def gradient(tt,xx,n):
    if n==0:return [f(tt,xx) for f in jetdf]
    zz=graph(tt,xx,n);(an,xn,fn),partials=event(tt,xx,zz);p,v=gradient(an,xn,n-1)
    ap,xp,fp=partials;den=fp[2]-p*ap[2]-v*xp[2]
    assert den>0
    return [(p*ap[i]+v*xp[i]-fp[i])/den for i in (0,1)]

def tangent(tt,xx,n):
    zz=graph(tt,xx,n);(_,_,_),partials=event(tt,xx,zz);gz=gradient(tt,xx,n)
    J=mp.matrix([[row[i]+row[2]*gz[i] for i in (0,1)] for row in partials[:2]])
    return gz,J

def hessian(tt,xx,n):
    if n==0:return mp.matrix([[f(tt,xx) for f in row] for row in jeth])
    zz=graph(tt,xx,n);(an,xn,fn),partials=event(tt,xx,zz);p,v=gradient(an,xn,n-1)
    target_h=hessian(an,xn,n-1);gz=gradient(tt,xx,n);den=partials[2][2]-p*partials[0][2]-v*partials[1][2]
    hs=[mp.matrix([[f(tt,xx,zz) for f in row] for row in item]) for item in hh]
    raw=[f(tt,xx,zz) for f in jj[2]]
    hs[2]=mp.matrix([[hs[2][i,j]/(2*fn)-raw[i]*raw[j]/(4*fn**3) for j in range(3)] for i in range(3)])
    bv=[mp.matrix([1,0,gz[0]]),mp.matrix([0,1,gz[1]])]
    sv=[mp.matrix([sum(partials[row][j]*bi[j] for j in range(3)) for row in range(2)]) for bi in bv]
    ans=mp.matrix(2,2)
    for i in range(2):
        for j in range(2):
            ans[i,j]=(-(bv[i].T*hs[2]*bv[j])[0]+p*(bv[i].T*hs[0]*bv[j])[0]+v*(bv[i].T*hs[1]*bv[j])[0]+(sv[i].T*target_h*sv[j])[0])/den
    return ans

ht,hx=mp.mpf('.01'),mp.mpf('.02');H=hessian(ht,hx,2);step_h=mp.mpf('1e-8')
hfd=mp.matrix(2,2)
for j in range(2):
    plus=gradient(ht+(step_h if j==0 else 0),hx+(step_h if j==1 else 0),2)
    minus=gradient(ht-(step_h if j==0 else 0),hx-(step_h if j==1 else 0),2)
    for i in range(2):hfd[i,j]=(plus[i]-minus[i])/(2*step_h)
hessian_error=max(abs(H[i,j]-hfd[i,j]) for i in range(2) for j in range(2));assert hessian_error<mp.mpf('1e-10')
assert abs(H[0,1]-H[1,0])<mp.mpf('1e-60')

samples=[];gradient_errors=[]
for ts,xs in [('.005','.01'),('.01','.02'),('.02','.04')]:
    tt,xx=mp.mpf(ts),mp.mpf(xs);gz,J=tangent(tt,xx,2);step=mp.mpf('1e-12');fd=[]
    fd.append((graph(tt+step,xx,2)-graph(tt-step,xx,2))/(2*step))
    fd.append((graph(tt,xx+step,2)-graph(tt,xx-step,2))/(2*step))
    err=max(abs(gz[i]-fd[i]) for i in (0,1));assert err<mp.mpf('1e-18');gradient_errors.append(err)
    assert mp.det(J)>0
    samples.append({'t':ts,'x':xs,'depth':2,'gradient':list(map(str,gz)),'gradient_central_difference_error':str(err),'determinant':str(mp.det(J)),'radius_certified':False})
small_t=mp.mpf('1e-7');small_x=mp.mpf('.001');_,J=tangent(small_t,small_x,2)
leading=sp.lambdify(x,coef,'mpmath')(small_x);rank_error=abs(mp.det(J)/small_t-leading);assert rank_error<mp.mpf('1e-4')
# Independent complete Ambient event; inherited witness supplies gauge-invariant phase.
sig=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex);I=np.eye(2)
def vec(M):return np.array([np.trace(M@p).real/2 for p in sig])
def ambient(tt,xx):
    zz=float(graph(mp.mpf(str(tt)),mp.mpf(str(xx)),2));ss=np.sqrt(xx)/.2;qq=np.sqrt(xx)*zz;r=tt*qq/np.sqrt(1+xx)
    Y=tt*I+r*sig[0];J=ss*sig[2];W=I/2+.2*sig[0]
    out=update(J,1.7*I,W,Y+.1j*(Y@J-J@Y),I);assert out['terminal'] is None
    y,j,w=vec(out['y']),vec(out['k']),vec(out['w']);tn=np.trace(out['y']).real/2;xn=.04*float(j@j)
    phi=np.arctan2(np.dot(j/np.linalg.norm(j),np.cross(w,y)),np.dot(w,y))
    return np.array([tn,xn,phi])
ambient_errors=[]
for sample in samples:
    tt=float(sample['t']);xx=float(sample['x']);gz,J=tangent(mp.mpf(sample['t']),mp.mpf(sample['x']),2)
    expected=np.zeros((3,2));expected[:2,:2]=np.array(J.tolist(),float);expected[2,1]=1/(2*np.sqrt(xx)*(1+xx))
    step=1e-6;observed=np.column_stack([(ambient(tt+step,xx)-ambient(tt-step,xx))/(2*step),(ambient(tt,xx+step)-ambient(tt,xx-step))/(2*step)])
    error=float(np.max(np.abs(observed-expected)));assert error<1e-5;ambient_errors.append(error)
res={'kind':'synthetic mathematics/code derivative controls','symbolic_checks':8,'gradient_samples':samples,'max_gradient_difference_error':str(max(gradient_errors)),'ambient_jacobian_cases':3,'ambient_updates':12,'max_ambient_tangent_error':max(ambient_errors),'rank_asymptotic_error':str(rank_error),'hessian_difference_error':str(hessian_error),'hessian_sample':[[str(H[i,j]) for j in range(2)] for i in range(2)],'precision_digits':80,'proved_regularity':'local C1,1 proved; C2 and analyticity not established','physical_2D_flow_proved':False,'holdout_accessed':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
