"""P60 independent synthetic controls; no measured data or holdout.
Run with PYTHONPATH=experiments/real-eeg-covariance-2026-10-07.
Finite roots do not certify the existential theorem's numerical radius.
"""
import json
from pathlib import Path
import sympy as sp
import numpy as np
import mpmath as mp
from experiment import update
t,q=sp.symbols('t q',positive=True);h=t*q
u=[t+h,t-h];c=[1/(1+y) for y in u];b=[y*z for y,z in zip(u,c)]
m=t*t+h*h*(1-t)/(1+t);al=m/(1+m);ev=[al*y*y+(1-al)*z*z for y,z in zip(c,b)]
A=sp.cancel(sum(ev)/2);V=sp.cancel((ev[0]-ev[1])/2);B=sp.cancel(V/(A*q))
g=sp.cancel((al*c[0]*c[1]+(1-al)*b[0]*b[1])**2/(ev[0]*ev[1]))
x,z=sp.symbols('x z',positive=True);d=1+x+x*x;M=d/(1+x)**2
AA=A.subs(q,sp.sqrt(x)*z);XX=x*g.subs(q,sp.sqrt(x)*z)
F2=z*z*B.subs(q,sp.sqrt(x)*z)**2*(1/g.subs(q,sp.sqrt(x)*z)+x)
assert sp.cancel(AA.subs(t,0))==0
assert sp.cancel(sp.diff(AA,t).subs(t,0))==0
assert sp.cancel(XX.subs({t:0,z:1})-x/d)==0
assert sp.cancel(F2.subs({t:0,z:1})-1)==0
assert sp.cancel(sp.diff(F2,z).subs({t:0,z:1})/2-M)==0
assert sp.cancel(sp.diff(F2,t).subs({t:0,z:1})/2+(2+x)*M)==0
assert sp.cancel(sp.diff(F2,x).subs({t:0,z:1}))==0
assert sp.cancel(sp.diff(AA,t,2).subs({t:0,x:0})/2-2)==0
ma=sp.lambdify((t,q),A,'mpmath');mg=sp.lambdify((t,q),g,'mpmath');mb=sp.lambdify((t,q),B,'mpmath')
mp.mp.dps=80

def jet(tt,xx):
    pp=4*xx**6+17*xx**5+42*xx**4+61*xx**3+54*xx**2+27*xx+6
    return 1+(2+xx)*tt+pp/(1+xx+xx**2)**2*tt**2

def event(tt,xx,zz):
    qq=mp.sqrt(xx)*zz;gg=mg(tt,qq)
    return ma(tt,qq),xx*gg,zz*mb(tt,qq)*mp.sqrt(1/gg+xx)

def graph(tt,xx,depth):
    if depth==0 or tt==0:return jet(tt,xx)
    def objective(zz):
        an,xn,fn=event(tt,xx,zz)
        return fn-graph(an,xn,depth-1)
    seed=jet(tt,xx)
    return mp.findroot(objective,(seed,seed+tt*mp.mpf('.01')),tol=mp.mpf('1e-68'),verify=True)

root_checks=[]
for ts,xs in [('0.0001','0.001'),('0.001','0.01'),('0.02','0.04')]:
    tt,xx=mp.mpf(ts),mp.mpf(xs);values=[graph(tt,xx,j) for j in range(4)]
    zz=values[-1];an,xn,fn=event(tt,xx,zz);res=fn-graph(an,xn,3)
    corrections=[abs(values[j+1]-values[j]) for j in range(3)]
    assert corrections[2]<corrections[1]<corrections[0]
    assert abs(res)<mp.mpf('1e-30')
    root_checks.append({'t':ts,'x':xs,'finite_depth':3,'z':str(zz),'corrections':list(map(str,corrections)),'next_invariance_residual':str(res),'numerical_radius_certified':False})
# Endpoint scalar identity gives an independent infinite-product check at x=0.
tt=mp.mpf('.02');product=mp.mpf(1);scalar_t=tt
for _ in range(10):
    product*=(1+scalar_t)/(1-scalar_t);scalar_t=ma(scalar_t,0)
assert abs(graph(tt,mp.mpf(0),3)-product)<mp.mpf('1e-30')
scalar_error=abs(graph(tt,mp.mpf(0),3)-product)
fa=sp.lambdify((t,q),A,'numpy');fg=sp.lambdify((t,q),g,'numpy');fb=sp.lambdify((t,q),B,'numpy')
sig=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex);I=np.eye(2);rng=np.random.default_rng(60);errors=[]
for _ in range(40):
    tt=rng.uniform(.005,.025);xx=rng.uniform(.005,.04);zz=float(jet(tt,xx));qq=np.sqrt(xx)*zz;ss=np.sqrt(xx)/.2;r=tt*qq/np.sqrt(1+xx);phi=rng.uniform(-np.pi,np.pi)
    Y=tt*I+r*(np.cos(phi)*sig[0]+np.sin(phi)*sig[1]);J=ss*sig[2]
    oo=update(J,1.7*I,I/2+.2*sig[0],Y+.1j*(Y@J-J@Y),I);assert oo['terminal'] is None
    yy,jj=oo['y'],oo['k'];tn=np.trace(yy).real/2;rn=np.sqrt(np.trace((yy-tn*I)@(yy-tn*I)).real/2);sn=np.sqrt(np.trace(jj@jj).real/2);xn=.04*sn*sn;qn=rn*np.sqrt(1+xn)/tn;zn=qn/np.sqrt(xn)
    an=fa(tt,qq);gn=fg(tt,qq);fn=zz*fb(tt,qq)*np.sqrt(1/gn+xx)
    errors.append(float(max(abs(tn-an),abs(xn-xx*gn),abs(zn-fn))))
assert max(errors)<1e-10
an,xn,fn=event(mp.mpf('.02'),mp.mpf('.04'),jet(mp.mpf('.02'),mp.mpf('.04')))
assert abs(fn-jet(an,xn))>mp.mpf('1e-6')
res={'kind':'synthetic mathematics/code controls','symbolic_checks':8,'ambient_cases':40,'max_ambient_factor_error':max(errors),'precision_digits':80,'nested_root_controls':root_checks,'scalar_product_error':str(scalar_error),'previous_second_jet_failure_preserved':True,'local_existence':'proved by weighted graph transform; radius specified by derivative bounds, not numerical samples','physical_2D_pendulum_proved':False,'holdout_accessed':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
