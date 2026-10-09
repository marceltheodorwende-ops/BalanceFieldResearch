"""P56 synthetic controls; imports canonical update only, no data evaluation.
Run: PYTHONPATH=experiments/real-eeg-covariance-2026-10-07 python experiments/bfg-kernel-endpoint-2026-10-09/check.py
"""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
from experiment import update
t,q=sp.symbols('t q',positive=True);h=t*q
u=[t+h,t-h];c=[1/(1+x) for x in u];b=[x*y for x,y in zip(u,c)]
m=t*t+h*h*(1-t)/(1+t);al=m/(1+m)
ev=[al*x*x+(1-al)*y*y for x,y in zip(c,b)]
A=sp.cancel(sum(ev)/2);V=sp.cancel((ev[0]-ev[1])/2)
G2=sp.cancel((al*c[0]*c[1]+(1-al)*b[0]*b[1])**2/(ev[0]*ev[1]))
ratio=sp.cancel(V/(A*q))
assert sp.simplify(sp.limit(G2,t,0)-1/(1+q*q+q**4))==0
assert sp.limit(sp.limit(ratio,t,0),q,0)==1
assert sp.cancel(A.subs(q,0)-2*t*t/((1+t)**2*(1+t*t)))==0
assert sp.cancel(G2.subs(q,0)-1)==0
# Gram determinant: strict correlation when u+!=u-.
gram=sp.factor(ev[0]*ev[1]-(al*c[0]*c[1]+(1-al)*b[0]*b[1])**2)
assert sp.cancel(gram-al*(1-al)*(c[0]*b[1]-c[1]*b[0])**2)==0
for expr in [ratio,G2]:
    num,den=sp.fraction(expr)
    assert den.subs({t:0,q:0})!=0 and expr.subs({t:0,q:0})==1
fa=sp.lambdify((t,q),A,'numpy');fv=sp.lambdify((t,q),V,'numpy');fg=sp.lambdify((t,q),G2,'numpy')
S=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex);I=np.eye(2);rng=np.random.default_rng(56);errors=[]
for _ in range(40):
    tt=rng.uniform(.2,.7);s=rng.uniform(.1,.8);hh=rng.uniform(.02,.7*min(tt,1-tt));qq=hh/tt;r=hh/np.sqrt(1+.04*s*s)
    Y=tt*I+r*S[0];J=s*S[2];W=I/2+.2*S[0];Z=Y+.1j*(Y@J-J@Y)
    out=update(J,1.7*I,W,Z,I);assert out['terminal'] is None
    yy=out['y'];jj=out['k'];tn=np.trace(yy).real/2;rn=np.sqrt(max(0,np.trace((yy-tn*I)@(yy-tn*I)).real/2));sn=np.sqrt(np.trace(jj@jj).real/2)
    qn=rn*np.sqrt(1+.04*sn*sn)/tn
    expected=fv(tt,qq)*np.sqrt(1+.04*s*s*fg(tt,qq))/fa(tt,qq)
    errors.append(float(abs(qn-expected)));assert tn<tt
assert max(errors)<1e-10
mp.mp.dps=80;fr=sp.lambdify((t,q),ratio,'mpmath');gg=sp.lambdify((t,q),G2,'mpmath')
x=mp.mpf('1e-20');z=mp.mpf('1e-12');ss=mp.mpf('.3')
multiplier=fr(x,z)*mp.sqrt(1+mp.mpf('.04')*ss*ss*gg(x,z));lim=mp.sqrt(1+mp.mpf('.04')*ss*ss)
assert abs(multiplier-lim)<mp.mpf('1e-15') and multiplier>1
res={'symbolic_checks':7,'ambient_cases':40,'max_relative_anisotropy_endpoint_error':max(errors),'positive_endpoint_multiplier':str(multiplier),'multiplier_limit_error':str(abs(multiplier-lim)),'kind':'synthetic mathematics/code controls','holdout_accessed':False,'physical_force_derived':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
