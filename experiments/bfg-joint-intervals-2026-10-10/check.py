"""Synthetic containment/canonical matrix controls, no data accessed."""
import json,math,random
from pathlib import Path
import numpy as np
import sympy as s
from analyze import certificates
rng=random.Random(73)
for i in range(1000):
    h=rng.uniform(.02,2);eta=.005;e=.002;ew=.0005
    T=np.array([-h,0,h])+np.array([rng.uniform(-eta,eta) for _ in range(3)])
    a=rng.uniform(-50,50);v=rng.uniform(-3,3);q0=rng.uniform(-2,2)
    q=q0+v*T+a*T*T/2
    obs=q+np.array([rng.uniform(-e,e) for _ in range(3)])
    wm=v+a*T[1]+rng.uniform(-ew,ew)
    ap,av=certificates(*obs,wm,ew,h,h,e,eta)
    assert max(ap,av)<=abs(a)+1e-10
q,w,k,g,b=s.symbols('q w k g b',real=True);d=s.cos(q/2)
energy=k*(1-s.cos(q))+w*w/2
rate=s.diff(energy,q)*w+s.diff(energy,w)*(-k*s.sin(q)-g*d*w-b*w*w)
assert s.simplify(rate+g*d*w*w+b*w**3)==0 # positive w branch
x,y=s.symbols('x y',positive=True)
ys=s.Matrix([x,y]);lc=1/(1+x)+1/(1+y);lb=x*x/(1+x)+y*y/(1+y);alpha=lb/(lc+lb)
geom=s.Matrix([(alpha+(1-alpha)*z*z)/(1+z)**2 for z in (x,y)])
jac=geom.jacobian(ys)
J=np.array(jac.subs({x:s.Rational(1,5),y:s.Rational(3,5)}),dtype=float)
assert abs(np.linalg.det(J))>1e-6
func=s.lambdify((x,y),geom,'numpy');base=np.array([.2,.6]);dh=1e-6
FD=np.column_stack([(np.asarray(func(*(base+dh*np.eye(2)[j]))).ravel()-np.asarray(func(*(base-dh*np.eye(2)[j]))).ravel())/(2*dh) for j in range(2)])
assert np.max(abs(FD-J))<1e-7
F=np.ones(2);LC=np.sum(F/(1+base));LB=np.sum(F*base**2/(1+base));aa=LB/(LC+LB)
A=np.vstack([np.diag(math.sqrt(aa)/(1+base)),np.diag(math.sqrt(1-aa)*base/(1+base))])
sv=np.linalg.svd(A,compute_uv=False)**2;target=np.asarray(func(*base)).ravel()
assert np.max(abs(np.sort(sv)-np.sort(target)))<1e-12
out={'status':'passed','synthetic_cases':1000,'energy_identity':True,'canonical_tangent_determinant':float(np.linalg.det(J)),
 'canonical_tangent':J.tolist(),'canonical_successor':target.tolist(),'finite_difference_error':float(np.max(abs(FD-J))),
 'ambient_svd_error':float(np.max(abs(np.sort(sv)-np.sort(target))))}
Path(__file__).with_name('controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
