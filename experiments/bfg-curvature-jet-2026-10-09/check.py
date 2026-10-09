"""P59 synthetic math controls. Run with PYTHONPATH pointing to the existing EEG experiment module; no measurement access."""
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
G2=sp.cancel((al*c[0]*c[1]+(1-al)*b[0]*b[1])**2/(ev[0]*ev[1]))
x,z=sp.symbols('x z',positive=True);d=1+x+x*x;M=d/(1+x)**2
P=4*x**6+17*x**5+42*x**4+61*x**3+54*x*x+27*x+6
C2=-2*P/((1+x)**2*d);bb=P/d**2
# All factors are even in q. Substitute q^2 rather than introducing radicals.
def sub(expr,Q):
    return expr.subs(q,sp.sqrt(x)*Q)
F=z**2*sub(B,z)**2/sub(G2,z)+x*z**2*sub(B,z)**2
assert sp.cancel(sp.diff(F,t).subs({t:0,z:1})+2*(x+2)*M)==0
assert sp.cancel(sp.diff(F,z).subs({t:0,z:1})-2*M)==0
Z1=1+(2+x)*t
AA=sub(A,Z1);GG=sub(G2,Z1);BB=sub(B,Z1)
R1=Z1**2*BB**2/GG+x*Z1**2*BB**2-(1+(2+x*GG)*AA)**2
assert sp.cancel(R1.subs(t,0))==0
assert sp.cancel(sp.diff(R1,t).subs(t,0))==0
assert sp.cancel(sp.diff(R1,t,2).subs(t,0)/2-C2)==0
assert sp.cancel(C2+2*M*bb)==0
assert C2.subs(x,0)==-12
assert all(v>0 for v in sp.Poly(P,x).all_coeffs())
fa=sp.lambdify((t,q),A,'numpy');fg=sp.lambdify((t,q),G2,'numpy');fb=sp.lambdify((t,q),B,'numpy')
sig=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex);I=np.eye(2);rng=np.random.default_rng(59);errors=[];witness={}
def Z(tt,xx,order):
    pp=4*xx**6+17*xx**5+42*xx**4+61*xx**3+54*xx**2+27*xx+6
    return 1+(2+xx)*tt+(pp/(1+xx+xx**2)**2*tt**2 if order==2 else 0)
for case in range(40):
    tt=rng.uniform(.005,.05);xx=rng.uniform(.01,.16);ss=np.sqrt(xx)/.2;phi=rng.uniform(-np.pi,np.pi)
    for order in (1,2):
        zz=Z(tt,xx,order);qq=np.sqrt(xx)*zz;assert qq<1 and tt*(1+qq)<1
        r=tt*qq/np.sqrt(1+xx);Y=tt*I+r*(np.cos(phi)*sig[0]+np.sin(phi)*sig[1]);J=ss*sig[2]
        out=update(J,1.7*I,I/2+.2*sig[0],Y+.1j*(Y@J-J@Y),I);assert out['terminal'] is None
        yy=out['y'];jj=out['k'];tn=np.trace(yy).real/2;rn=np.sqrt(np.trace((yy-tn*I)@(yy-tn*I)).real/2);sn=np.sqrt(np.trace(jj@jj).real/2);xn=.04*sn*sn;qn=rn*np.sqrt(1+xn)/tn
        observed=(qn/(.2*sn))**2-Z(tn,xn,order)**2
        an=fa(tt,qq);gn=fg(tt,qq);bn=fb(tt,qq)
        expected=zz**2*bn**2/gn+xx*zz**2*bn**2-Z(an,xx*gn,order)**2
        errors.append(float(abs(observed-expected)))
        if order==1:assert observed<0
assert max(errors)<1e-10
mp.mp.dps=80;ma=sp.lambdify((t,q),A,'mpmath');mg=sp.lambdify((t,q),G2,'mpmath');mb=sp.lambdify((t,q),B,'mpmath')
def residual(tt,xx,order):
    zz=Z(tt,xx,order);qq=mp.sqrt(xx)*zz;aa=ma(tt,qq);gg=mg(tt,qq);bbb=mb(tt,qq)
    return zz**2*bbb**2/gg+xx*zz**2*bbb**2-Z(aa,xx*gg,order)**2
xx=mp.mpf('.04');orders=[]
for ts in ('.001','.0001','.00001'):
    tt=mp.mpf(ts);orders.append({'t':ts,'R1_over_t2':str(residual(tt,xx,1)/tt**2),'R2_over_t3':str(residual(tt,xx,2)/tt**3)})
coef=sp.lambdify(x,C2,'mpmath')(xx)
assert abs(residual(mp.mpf('1e-20'),xx,1)/mp.mpf('1e-40')-coef)<mp.mpf('1e-17')
assert abs(residual(mp.mpf('1e-20'),xx,2)/mp.mpf('1e-40'))<mp.mpf('1e-17')
for order in (1,2):witness[str(order)]=str(residual(mp.mpf('.02'),xx,order));assert abs(mp.mpf(witness[str(order)]))>mp.mpf('1e-12')
assert residual(mp.mpf('1e-10'),mp.mpf('1e-10'),1)<0
res={'symbolic_checks':8,'ambient_cases':80,'max_ambient_residual_error':max(errors),'precision_digits':80,'residual_orders':orders,'positive_geometry_witness_t':'.02','positive_geometry_witness_x':'.04','witness_residuals':witness,'first_truncation_exact_closure':'disproved near joint endpoint','second_jet':'necessary second-order cancellation only; no existence proof','kind':'synthetic mathematics/code controls','holdout_accessed':False,'physical_force_derived':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
