"""P53 synthetic controls; no measurements or holdout access.
Run: PYTHONPATH=/workspace/bfg-eeg python check.py
Dependency: archived experiment.py Ambient update, not its evaluate() routine.
"""
import json
from pathlib import Path
import numpy as np
import sympy as sp
from experiment import update
S=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
I=np.eye(2)
def split(A): return np.trace(A).real/2,np.array([np.trace(A@v).real/2 for v in S])
def factor(t,r,s,eta=.1):
    h=r*np.sqrt(1+4*eta**2*s*s); u=np.array([t+h,t-h]); c=1/(1+u); b=u*c
    lc=c.sum(); lb=(u*u*c).sum(); a=lb/(lc+lb)
    v=a*c*c+(1-a)*b*b
    gamma=(a*np.prod(c)+(1-a)*np.prod(b))/np.sqrt(np.prod(v))
    return np.array([v.mean(),abs(v[0]-v[1])/2,gamma*s]),gamma,(v[0]-v[1])/2,h
rng=np.random.default_rng(53); ambient=[]; orth=[]; gauges=[]; signs=[]; steps=0
for _ in range(60):
    t=rng.uniform(.25,.7); s=rng.uniform(.1,.8); h=rng.uniform(.02,.85*min(t,1-t)); r=h/np.sqrt(1+.04*s*s)
    y=np.array([r,0,0]); j=np.array([0,0,s]); Y=t*I+np.einsum('i,ijk->jk',y,S); J=np.einsum('i,ijk->jk',j,S)
    Z=Y+.1j*(Y@J-J@Y); expected,gamma,v,h=factor(t,r,s)
    out=update(J,1.7*I,I/2,Z,I); assert out['terminal'] is None
    V=out['v']; R=V@out['y']@V.conj().T; Jn=V@out['k']@V.conj().T
    tn,yn=split(R); j0,jn=split(Jn); z=y-.2*np.cross(y,j)
    errs=[np.max(abs(yn-v*z/h)),np.max(abs(jn-gamma*j)),abs(j0),np.max(abs(V@out['f']@V.conj().T-1.7*I)),np.max(abs(out['w']-I/2)),np.max(abs(np.array([tn,np.linalg.norm(yn),np.linalg.norm(jn)])-expected))]
    ambient.append(float(max(errs))); orth.append(float(abs(yn@jn))); assert 0<gamma<1
    # All three invariants unchanged under arbitrary common unitary changes.
    q,_=np.linalg.qr(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)))
    oo=update(q.conj().T@J@q,1.7*I,I/2,q.conj().T@Z@q,I); aa,bb=split(oo['y']); cc,dd=split(oo['k'])
    gauges.append(float(np.max(abs(np.array([aa,np.linalg.norm(bb),np.linalg.norm(dd)])-expected))))
    signs.append(float(np.max(abs(factor(t,r,s,-.1)[0]-expected))))
    # Repeat the declared gated policy, not a frozen natural-frame input.
    for k in range(4):
        tt,rr,ss=expected; hh=rr*np.sqrt(1+.04*ss*ss)
        assert 0<tt-hh<tt+hh<1
        expected,gg,_,_=factor(tt,rr,ss); steps+=1
assert max(ambient)<1e-11 and max(orth)<1e-12 and max(gauges)<1e-11 and max(signs)==0
# Independent exact symbolic derivative of the two geometry eigenvalues.
t,h=sp.symbols('t h',real=True); u=[t+h,t-h]; c=[1/(1+x) for x in u]
lc=sum(c);lb=sum(x*x*cc for x,cc in zip(u,c));a=lb/(lc+lb)
v=[a*cc**2+(1-a)*(x*cc)**2 for x,cc in zip(u,c)]
tp=sum(v)/2;vp=(v[0]-v[1])/2
point={t:sp.Rational(9,20),h:sp.Rational(3,25)}
mat=sp.Matrix([tp,vp]).jacobian([t,h]).subs(point);det=sp.factor(mat.det());assert det!=0
dtdh=sp.factor(sp.diff(tp,h).subs(point));assert dtdh!=0
# Restricted 2-coordinate (t,r) is not closed: s changes geometry at fixed t,r.
e0=factor(.45,.12,.3)[0];e1=factor(.45,.12,.8)[0];gap=float(np.linalg.norm(e0[:2]-e1[:2]));assert gap>1e-6
# Positive initial gate does not imply next prepared gate for unbounded J.
ex,g,_,_=factor(.5,.4/np.sqrt(401),100); nextmin=float(ex[0]-ex[1]*np.sqrt(1+.04*ex[2]**2));assert nextmin<0
zero,g0,_,_=factor(.45,0,.3);assert zero[1]==0 and abs(g0-1)<1e-14
vv=[sp.factor(x.subs({t:sp.Rational(1,2),h:sp.Rational(2,5)})) for x in v]
aa=sp.factor(a.subs({t:sp.Rational(1,2),h:sp.Rational(2,5)}))
cc=[sp.Rational(10,19),sp.Rational(10,11)];bb=[sp.Rational(9,19),sp.Rational(1,11)]
gam2=sp.factor((aa*cc[0]*cc[1]+(1-aa)*bb[0]*bb[1])**2/(vv[0]*vv[1]))
margin2=sp.factor(((vv[0]+vv[1])/2)**2-((vv[0]-vv[1])/2)**2*(1+400*gam2));assert margin2<0
res=dict(cases=60,max_ambient_error=max(ambient),max_orthogonality_error=max(orth),max_gauge_factor_error=max(gauges),eta_sign_gap=max(signs),gated_synthetic_successor_steps=steps,exact_geometry_jacobian_det=str(det),exact_trace_derivative_h=str(dtdh),two_geometry_coordinate_same_fiber_successor_gap=gap,admissibility_counterexample_next_min=nextmin,exact_next_prepared_squared_margin=str(margin2),kind='synthetic mathematics/code controls',force_derived=False,physical_phase_identified=False,holdout_accessed=False)
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res,indent=2))
