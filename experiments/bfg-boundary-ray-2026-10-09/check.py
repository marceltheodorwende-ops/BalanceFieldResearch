"""P58 synthetic math/code checks, no data access.
PYTHONPATH=experiments/real-eeg-covariance-2026-10-07 python experiments/bfg-boundary-ray-2026-10-09/check.py
"""
import json
from pathlib import Path
import sympy as sp
import numpy as np
import mpmath as mp
from experiment import update
t,q=sp.symbols('t q',positive=True);h=t*q
u=[t+h,t-h];c=[1/(1+x) for x in u];b=[x*y for x,y in zip(u,c)]
m=t*t+h*h*(1-t)/(1+t);al=m/(1+m);ev=[al*x*x+(1-al)*y*y for x,y in zip(c,b)]
A=sp.cancel(sum(ev)/2);V=sp.cancel((ev[0]-ev[1])/2);B=sp.cancel(V/(A*q))
G2=sp.cancel((al*c[0]*c[1]+(1-al)*b[0]*b[1])**2/(ev[0]*ev[1]))
s,k,z=sp.symbols('s k z',positive=True);g0=1/(1+q*q+q**4)
assert sp.cancel(q*q*(1+q*q*g0)/(1+q*q)**2-q*q*g0)==0
slope=(1+z*z*s*s+z**4*s**4)+k*k*s*s-(1+z*z*s*s)**2
assert sp.expand(slope-(k*k-z*z)*s*s)==0
x=k*k*s*s;S=s/sp.sqrt(1+x+x*x)
assert sp.simplify(sp.diff(S,s)-(1-x*x)/(1+x+x*x)**sp.Rational(3,2))==0
E=(1+t)**3+q*q*(1-2*t*t-t**3)+q**4*t*t
F1=q**4*t*t-3*q*q*t*t-2*q*q*t+q*q+2*t*t+4*t+2
F2=q**4*t**3-q*q*t**3-4*q*q*t*t-3*q*q*t+2*t*t+4*t+2
defect=sp.cancel(q*q*(B*B*(1+q*q*G2)-G2))
assert sp.cancel(defect+q*q*t*F1*F2/E**2)==0
point={t:sp.Rational(1,10),q:sp.Rational(1,5)}
exact=defect.subs(point);assert exact==-sp.Rational(3599578559,286465800625)
fa=sp.lambdify((t,q),A,'numpy');fv=sp.lambdify((t,q),V,'numpy');fg=sp.lambdify((t,q),G2,'numpy');fd=sp.lambdify((t,q),defect,'numpy')
sig=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex);I=np.eye(2);rng=np.random.default_rng(58);errors=[]
for _ in range(40):
    tt=rng.uniform(.05,.5);qq=rng.uniform(.02,.85);ss=qq/.2;r=tt*qq/np.sqrt(1+qq*qq);phi=rng.uniform(-np.pi,np.pi)
    Y=tt*I+r*(np.cos(phi)*sig[0]+np.sin(phi)*sig[1]);J=ss*sig[2];W=I/2+.2*sig[0];Z=Y+.1j*(Y@J-J@Y)
    oo=update(J,1.7*I,W,Z,I);assert oo['terminal'] is None
    yy=oo['y'];jj=oo['k'];tn=np.trace(yy).real/2;rn=np.sqrt(np.trace((yy-tn*I)@(yy-tn*I)).real/2);sn=np.sqrt(np.trace(jj@jj).real/2);qn=rn*np.sqrt(1+.04*sn*sn)/tn
    delta=qn*qn-.04*sn*sn;assert delta<0
    errors.append(float(abs(delta-fd(tt,qq))))
assert max(errors)<1e-10
terminal=update(np.diag([.3,-.3]),I,I/2,np.zeros((2,2)),I)['terminal'];assert terminal=='T_load'
mp.mp.dps=80;mb=sp.lambdify((t,q),B,'mpmath');mg=sp.lambdify((t,q),G2,'mpmath');qq=mp.mpf('.2');ss=mp.mpf(1);tt=mp.mpf('1e-20')
sn=ss*mp.sqrt(mg(tt,qq));qn=qq*mb(tt,qq)*mp.sqrt(1+mp.mpf('.04')*sn*sn)
target=ss/mp.sqrt(1+qq*qq+qq**4);boundary_error=max(abs(sn-target),abs(qn-mp.mpf('.2')*target));assert boundary_error<mp.mpf('1e-18')
res={'symbolic_checks':5,'ambient_cases':40,'max_ambient_defect_error':max(errors),'exact_interior_ray_defect':str(exact),'canonical_zero_terminal':terminal,'boundary_limit_error':str(boundary_error),'boundary_rank2_physical_return_proved':False,'positive_geometry_straight_ray_lift':'disproved on stated domain','kind':'synthetic mathematics/code controls','holdout_accessed':False,'physical_force_derived':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
