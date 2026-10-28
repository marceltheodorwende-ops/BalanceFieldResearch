"""Positive-load lower-pair Lyapunov certificate and finite source controls."""
import json
from pathlib import Path
import sympy as sp
import numpy as np
import mpmath as mp
import audit
import pair_audit

def certificate():
    s,r,q=sp.symbols('s r q'); b=r*q
    zs=[1+r,1+r,1-r+b,1-r-b]
    # Weighted diagonal entries of F are all one; cross blocks do not enter traces.
    lc=sp.cancel(sum(1/(1+s*z) for z in zs))
    lb=sp.cancel(sum(s*s*z*z/(1+s*z) for z in zs))
    rho=sp.cancel(lb/(s*s*lc))
    gs=[sp.cancel((rho+z*z)/(1+s*z)**2) for z in zs]
    total=2*gs[0]+gs[2]+gs[3]
    rn=sp.cancel((2*gs[0]-gs[2]-gs[3])/total)
    bn=sp.cancel(2*(gs[2]-gs[3])/total)
    L=sp.cancel((1-bn/(rn*q))/r)
    bounds={s:sp.Rational(1,100),r:sp.Rational(1,4),q:sp.Rational(1,2)}
    num,den=sp.fraction(sp.cancel(L-sp.Rational(1,2)))
    if den.subs({s:0,r:0,q:0})<0: num,den=-num,-den
    def enclosure(expr):
        p=sp.Poly(expr,s,r,q); constant=p.coeff_monomial(1)
        mass=sum(abs(coef)*sp.prod(bounds[v]**power for v,power in zip(p.gens,mon)) for mon,coef in p.terms())
        return sp.cancel(2*constant-mass),mass
    nl,nu=enclosure(num); dl,du=enclosure(den)
    result=dict(numerator_lower=str(nl),numerator_mass=str(nu),denominator_lower=str(dl),denominator_mass=str(du),method='constant minus absolute nonconstant coefficient mass')
    assert nl>0 and dl>0,result
    assert sp.cancel(L.subs(s,0)-(1-q*q/4)/(1-q*q*r/4))==0
    return result

def step(s,r,b):
    z=[1+r,1+r,1-r+b,1-r-b]
    rho=sum(v*v/(1+s*v) for v in z)/sum(1/(1+s*v) for v in z)
    g=[(rho+v*v)/(1+s*v)**2/(1+s*s*rho) for v in z]
    total=2*g[0]+g[2]+g[3]
    h=(rho+(1-r)**2-b*b)/mp.sqrt((rho+(1-r)**2-b*b)**2+4*rho*b*b)
    return s*s*total/4,(2*g[0]-g[2]-g[3])/total,2*(g[2]-g[3])/total,h

def prefixes():
    mp.mp.dps=500; rows=[]
    for rv in ('0.1','0.2'):
        for qv in ('0.1','0.5'):
            s=mp.mpf('.001'); r=mp.mpf(rv); b=r*mp.mpf(qv); v0=b*b/r; total=mp.mpf(0); product=mp.mpf(1)
            history=[]
            for event in range(6):
                oldv=b*b/r; oldr=r; oldq=b/r; olds=s; oldb=b
                s,r,b,h=step(s,r,b)
                assert 0<r<=oldr and 0<b/r<=oldq*(1-oldr/2)
                assert 0<s<=olds/32 and b*b/r<=oldv-oldb*oldb/2
                total+=oldb*oldb; product*=h
                assert total+2*b*b/r<=2*v0
                assert 1-product<=mp.mpf(32)/35*total
                history.append(dict(event=event+1,s=mp.nstr(s,18),r=mp.nstr(r,18),q=mp.nstr(b/r,18)))
            rows.append(dict(r0=rv,q0=qv,events=6,precision_digits=500,history=history,prefix_sum_b2=mp.nstr(total,18),remaining_sum_b2_bound=mp.nstr(2*b*b/r,18),coherence_product=mp.nstr(product,18),all_event_loss_bound=mp.nstr(mp.mpf(64)/35*v0,18)))
    return rows

def source():
    rng=np.random.default_rng(20261116); update=audit.load_update(); u=audit.complex_unitary(rng,4)
    cross=np.zeros((4,4),complex); x=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); cross[:2,2:]=x; cross[2:,:2]=x.conj().T; cross*=.1/np.linalg.norm(cross,2)
    f=u@(np.eye(4)+cross)@u.conj().T; w=np.eye(4)/4
    x=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); kb=x@x.conj().T; kb/=np.trace(kb); k=u@kb@u.conj().T
    calls=0; kr=0.; gr=0.; yr=0.; rows=[]
    for r in (.1,.2):
        for q in (.1,.5):
            b=r*q
            for s in (.001,.0001):
                sn,rn,bn,h=step(mp.mpf(str(s)),mp.mpf(str(r)),mp.mpf(str(b)))
                sn,rn,bn,h=map(float,(sn,rn,bn,h))
                assert rn<=r and bn/rn<=q*(1-r/2) and b*b/r-bn*bn/rn>=b*b/2
                ys=np.array([1+r,1+r,1-r+b,1-r-b]); load=(u*(s*ys))@u.conj().T
                out=pair_audit.source_aligned(update,k,f,w,load); calls+=1
                got=u.conj().T@out['k']@u; expected=kb[2:,2:].copy(); expected[0,1]*=h; expected[1,0]*=h
                kr=max(kr,float(np.linalg.norm(got[2:,2:]-expected)))
                ez=np.array([1+rn,1+rn,1-rn+bn,1-rn-bn]); ey=(u*ez)@u.conj().T
                yr=max(yr,float(np.linalg.norm(out['y']/(np.trace(out['y']).real/4)-ey)))
                if r==.1 and q==.1:
                    g=audit.complex_unitary(rng,4); conj=lambda z:g@z@g.conj().T
                    gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(load)); calls+=1
                    gr=max(gr,float(np.linalg.norm(gout['k']-conj(out['k']))))
                rows.append(dict(r=r,q=q,s=s,r_next=rn,q_next=bn/rn,V_decrement=b*b/r-bn*bn/rn,required_decrement=b*b/2))
    assert calls==10 and max(kr,gr)<1e-10 and yr<1e-8
    return dict(calls=calls,kernel_residual=kr,gauge_residual=gr,normalized_load_residual=yr,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261116,certificate=certificate(),positive_load_prefixes=prefixes(),source=source(),scope='Full positive-load lower cone and uniform local kernel-memory bound under stated n=4 assumptions; no physical four-current derived.')
    Path(__file__).with_name('lower_pair_lift_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
