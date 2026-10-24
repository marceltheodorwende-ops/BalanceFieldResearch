"""Boundary summability and exact finite-source local coherence bounds."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import audit
import pair_audit

def symbolic():
    r,q,rho,c,b=sp.symbols('r q rho c b',positive=True)
    mu=1+r*r+q*q*r*r/2
    ratio=(1-r)**2/(mu*(1-q*q*r/4))
    rn=(r-q*q*r*r/4)/mu; bn=(1-r)*q*r/mu
    assert sp.cancel((bn*bn/rn)/(q*q*r)-ratio)==0
    # ratio <= 1-r follows from mu>=1 and q²/4<=1.
    assert sp.expand(mu*(1-q*q*r/4)-(1-r)-(mu-1)*(1-q*q*r/4)-r*(1-q*q/4))==0
    # Use the simpler factorized two-stage inequality, no polynomial positivity guess.
    assert sp.expand((1-q*q*r/4)-(1-r)-r*(1-q*q/4))==0
    n=rho+c*c-b*b
    assert sp.expand((rho+(c+b)**2)*(rho+(c-b)**2)-n*n)==4*rho*b*b
    v=c*c-b*b
    assert sp.expand((rho+v)**2-4*rho*v-(rho-v)**2)==0
    assert sp.Rational(3,4)**2-sp.Rational(1,8)**2==sp.Rational(35,64)
    return dict(V='b²/r',V_successor_ratio=str(ratio),proved_decrement='V-V_next >= b²',positive_source_local_bound='1-h <= b²/(2(c²-b²)) <= 32 b²/35')

def boundary():
    rows=[]
    for r0 in (.1,.2):
        for q0 in (.1,.5):
            r=r0; b=r*q0; v0=b*b/r; total=0.; product=1.
            for _ in range(2000):
                v=b*b/r; mu=1+r*r+b*b/2; rho=mu; c=1-r
                h=(rho+c*c-b*b)/np.sqrt((rho+c*c-b*b)**2+4*rho*b*b)
                rn=(r-b*b/4)/mu; bn=(1-r)*b/mu
                assert bn*bn/rn <= v-b*b+1e-16
                total+=b*b; product*=h; r,b=rn,bn
                assert total+b*b/r<=v0+1e-14
                assert 1-product <= (32/35)*total+1e-13
            rows.append(dict(r0=r0,q0=q0,events=2000,sum_b_squared=total,initial_V=v0,remaining_sum_bound=b*b/r,coherence_product=product,all_event_loss_bound=(32/35)*v0))
    return rows

def source():
    rng=np.random.default_rng(20261115); update=audit.load_update(); u=audit.complex_unitary(rng,4)
    cross=np.zeros((4,4),complex); x=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); cross[:2,2:]=x; cross[2:,:2]=x.conj().T; cross*=.1/np.linalg.norm(cross,2)
    f=u@(np.eye(4)+cross)@u.conj().T; w=np.eye(4)/4
    x=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); kb=x@x.conj().T; kb/=np.trace(kb); k=u@kb@u.conj().T
    calls=0; residual=0.; gauge=0.; normalized=0.; rows=[]
    for r in (.1,.2):
        for q in (.1,.5):
            b=r*q; c=1-r
            for s in (.001,.0001):
                ys=[sp.Rational(str(s))*sp.Rational(str(z)) for z in (1+r,1+r,c+b,c-b)]
                alpha=pair_audit.alpha_exact(ys,[sp.Integer(1)]*4); rho=float(alpha/(1-alpha))/s**2
                h=(rho+c*c-b*b)/np.sqrt((rho+c*c-b*b)**2+4*rho*b*b)
                assert 0<h<=1 and 1-h<=(32/35)*b*b+1e-14
                load=(u*np.array([float(y) for y in ys]))@u.conj().T
                out=pair_audit.source_aligned(update,k,f,w,load); calls+=1
                vals=np.array([float(pair_audit.g(y,alpha)) for y in ys]); expected_y=(u*vals)@u.conj().T
                normalized=max(normalized,float(np.linalg.norm(out['y']/(np.trace(out['y']).real/4)-expected_y/(np.trace(expected_y).real/4))))
                got=u.conj().T@out['k']@u; expected=kb[2:,2:].copy(); expected[0,1]*=h; expected[1,0]*=h
                residual=max(residual,float(np.linalg.norm(got[2:,2:]-expected)))
                if r==.1 and q==.1:
                    g=audit.complex_unitary(rng,4); conj=lambda z:g@z@g.conj().T
                    gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(load)); calls+=1
                    gauge=max(gauge,float(np.linalg.norm(gout['k']-conj(out['k']))))
                rows.append(dict(r=r,q=q,s=s,h=h,local_loss_bound=(32/35)*b*b))
    assert calls==10 and max(residual,gauge)<1e-10 and normalized<1e-8
    return dict(calls=calls,kernel_residual=residual,gauge_residual=gauge,normalized_load_residual=normalized,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261115,symbolic=symbolic(),boundary=boundary(),source=source(),scope='Uniform all-event memory at boundary; exact one-event positive-source bound. Positive-source summability OPEN.')
    Path(__file__).with_name('lower_pair_memory_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
