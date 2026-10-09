"""P62 finite synthetic controls, never an exact-surface or radius certificate.
Run: PYTHONPATH=experiments/real-eeg-covariance-2026-10-07 python check.py
Only imports the independent ambient implementation; no dataset is read.
"""
import json
from pathlib import Path
import sympy as sp
import mpmath as mp
import numpy as np
from experiment import update

t,Q,x,z,v,u=sp.symbols('t Q x z v u', real=True)
g=(Q*t-t-1)**2/((Q+t+1)**2-Q*(t+1)**2)
H=sp.cancel((1-g)/Q)
assert sp.cancel(g.subs(Q,0)-1)==0
assert H.subs({t:0,Q:0})==1
assert sp.cancel(g-(1-Q*H))==0
h=sp.symbols('h', real=True)
ys=[t+h,t-h];cs=[1/(1+y) for y in ys];bs=[y*c for y,c in zip(ys,cs)]
load=t*t+h*h*(1-t)/(1+t);alpha=load/(1+load)
ev=[alpha*c*c+(1-alpha)*b*b for c,b in zip(cs,bs)]
A=sp.cancel(sum(ev)/2).subs(h,t*sp.sqrt(Q))
A=sp.cancel(A)
assert sp.cancel(A.subs(t,0))==0
assert sp.cancel(sp.diff(A,t).subs(t,0))==0
assert sp.cancel(sp.diff(A,t,2).subs(t,0)/2-2*(1+Q))==0
Z=1+(2+x)*t+(4*x**6+17*x**5+42*x**4+61*x**3+54*x*x+27*x+6)/(1+x+x*x)**2*t*t
aj=A.subs(Q,x*Z**2);Xj=x*g.subs(Q,x*Z**2)
# Derivative limits independently check the estimates supporting the cone.
assert sp.cancel(sp.diff(aj,x).subs(t,0))==0
assert sp.cancel(sp.diff(aj,x,t,t).subs(t,0)/2-2)==0
assert sp.cancel(sp.diff(Xj,t).subs(x,0))==0
assert sp.cancel(sp.diff(Xj,t,x).subs(x,0))==0
y=(u-1)*v**3+2*(1-u)*v*v+u*v
assert y.subs(v,0)==0 and sp.simplify(y.subs(v,1)-1)==0
assert sp.diff(y,v).subs(v,0)==u
assert sp.simplify(sp.diff(y,v).subs(v,1)-1)==0
assert sp.simplify(sp.diff(y,v)-(u+(1-u)*(4*v-3*v*v)))==0
assert sp.simplify(sp.diff(y,v).subs(v,sp.Rational(2,3))-(4-u)/3)==0
mp.mp.dps=80
af=sp.lambdify((t,x),aj,'mpmath');xf=sp.lambdify((t,x),Xj,'mpmath')
jf=[[sp.lambdify((t,x),sp.diff(f,w),'mpmath') for w in (t,x)] for f in (aj,Xj)]
zf=sp.lambdify((t,x),Z,'mpmath')
cases=[];seams=[]
for tt,xx in [('0.00001','0.02'),('0.00002','0.03'),('0.00003','0.04')]:
    tt,xx=mp.mpf(tt),mp.mpf(xx);tn,xn=af(tt,xx),xf(tt,xx)
    D=(tt-tn)/(xx-xn);J=mp.matrix([[f(tt,xx) for f in row] for row in jf])
    m1=(J[0,1]+J[0,0]*D)/(J[1,1]+J[1,0]*D)
    assert 0<m1<D<mp.mpf('.5')
    uu=m1/D
    slopes=[D*(uu+(1-uu)*(4*mp.mpf(i)/100-3*(mp.mpf(i)/100)**2)) for i in range(101)]
    assert min(slopes)>0 and max(slopes)<1
    # Exact endpoint chain rule checked with independently differentiated seed.
    seed=lambda vv:tn+(tt-tn)*((uu-1)*vv**3+2*(1-uu)*vv**2+uu*vv)
    lower=mp.diff(seed,mp.mpf(0))/(xx-xn)
    upper=mp.diff(seed,mp.mpf(1))/(xx-xn)
    transported=(J[0,1]+J[0,0]*upper)/(J[1,1]+J[1,0]*upper)
    err=abs(lower-transported);assert err<mp.mpf('1e-70');seams.append(err)
    # Jet-surface cone checks only; NOT the exact graph or theorem radius.
    denoms=[];image_slopes=[]
    for mm in [mp.mpf(i)/100 for i in range(101)]:
        den=J[1,1]+J[1,0]*mm;nm=(J[0,1]+J[0,0]*mm)/den
        assert den>mp.mpf('.5') and 0<nm<mp.mpf('.5')
        denoms.append(den);image_slopes.append(nm)
    ot,ox=tt,xx
    for n in range(10):
        nt,nx=af(ot,ox),xf(ot,ox)
        assert 0<nt<ot and 0<nx<ox
        assert ox*ox/2<ox-nx<2*ox*ox
        ot,ox=nt,nx
    cases.append({'t':str(tt),'x':str(xx),'D':str(D),'m1':str(m1),
                  'min_denominator':str(min(denoms)),
                  'max_image_slope':str(max(image_slopes)),
                  'ten_event_t':str(ot),'ten_event_x':str(ox),
                  'surface':'P59 finite jet approximation; not exact Z*',
                  'radius_certified':False})

sig=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
I=np.eye(2)
def vec(M):return np.array([np.trace(M@p).real/2 for p in sig])
errors=[]
for case in cases:
    tt,xx=mp.mpf(case['t']),mp.mpf(case['x']);zz=zf(tt,xx)
    qq=mp.sqrt(xx)*zz;rr=tt*qq/mp.sqrt(1+xx);ss=mp.sqrt(xx)/mp.mpf('.2')
    phi=.37;Y=float(tt)*I+float(rr)*(np.cos(phi)*sig[0]+np.sin(phi)*sig[1])
    J=float(ss)*sig[2];W=I/2+.2*sig[0]
    out=update(J,1.7*I,W,Y+.1j*(Y@J-J@Y),I)
    assert out['terminal'] is None
    vy,vj,vw=vec(out['y']),vec(out['k']),vec(out['w'])
    obs=np.array([np.trace(out['y']).real/2,.04*float(vj@vj),
        np.arctan2(np.dot(vj/np.linalg.norm(vj),np.cross(vw,vy)),np.dot(vw,vy))])
    expected=np.array([float(af(tt,xx)),float(xf(tt,xx)),phi+float(mp.atan(mp.sqrt(xx)))])
    err=float(np.max(np.abs(obs-expected)));assert err<1e-10;errors.append(err)

result={'kind':'synthetic algebra, seed-seam, jet-cone and independent matrix controls',
        'symbolic_checks':16,'precision_digits':80,'cases':cases,
        'max_seed_tangent_seam_error':str(max(seams)),
        'independent_ambient_events':3,'max_ambient_quotient_error':max(errors),
        'exact_invariant_curve':'proved by fundamental segments, not numerically approximated here',
        'physical_continuous_flow_proved':False,'force_selected':False,
        'real_measurements_used':False,'holdout_accessed':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
