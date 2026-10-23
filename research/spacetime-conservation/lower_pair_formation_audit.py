"""One-sided formation robustness and a signed-imbalance boundary witness."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
import audit
import pair_audit

def certificate():
    s,r,q,t=sp.symbols('s r q t'); rho=1+t; b=r*q
    zs=[1+r,1-r+b,1-r-b]
    g=[(rho+z*z)/(1+s*z)**2 for z in zs]
    L=sp.cancel((1-2*(g[1]-g[2])/(q*(2*g[0]-g[1]-g[2])))/r)
    num,den=sp.fraction(sp.cancel(L-sp.Rational(1,2)))
    origin={s:0,r:0,q:0,t:0}
    if den.subs(origin)<0:num,den=-num,-den
    bounds={s:sp.Rational(1,100),r:sp.Rational(1,4),q:sp.Rational(1,2),t:sp.Rational(5,8)}
    def interval(expr):
        poly=sp.Poly(expr,s,r,q,t); mass=sum(abs(c)*sp.prod(bounds[v]**p for v,p in zip(poly.gens,mon)) for mon,c in poly.terms()); low=2*poly.coeff_monomial(1)-mass
        return sp.cancel(low),sp.cancel(mass)
    nl,nu=interval(num); dl,du=interval(den)
    result=dict(numerator_lower=str(nl),numerator_mass=str(nu),denominator_lower=str(dl),denominator_mass=str(du),rho_enclosure='[3/8,13/8] contains [25/64,25/16]',method='constant minus absolute nonconstant coefficient mass')
    assert nl>0 and dl>0,result
    assert sp.cancel(L.subs(s,0)-(1-q*q/4)/(1-q*q*r/4))==0
    return result

def symbolic():
    r,b,d=sp.symbols('r b d'); mu=1+r*r+2*d*r+(1-d)*b*b/2
    D=1+r*r+d*r+(2-d)*b*b/4
    upper=mu+(1+r)**2; lp=mu+(1-r+b)**2; lm=mu+(1-r-b)**2
    rn=(r-b*b/4)/D; bn=(1-r)*b/D
    assert sp.cancel((2*upper-lp-lm)/(2*upper+lp+lm)-rn)==0
    assert sp.cancel(2*(lp-lm)/(2*upper+lp+lm)-bn)==0
    witness={r:sp.Rational(1,20),b:sp.Rational(1,200),d:-sp.Rational(1,2)}
    value=sp.cancel(rn.subs(witness)); assert value>sp.Rational(1,20)
    return dict(boundary_r=str(rn),boundary_b=str(bn),boundary_mu=str(mu),negative_imbalance_witness=dict(r='1/20',q='1/10',delta='-1/2',r_next=str(value),old_monotonicity='FAIL as predicted: r_next > r'))

def step(s,r,b,d):
    zs=[1+r,1+r,1-r+b,1-r-b]; weights=[1+d,1+d,1-d,1-d]
    rho=sum(w*z*z/(1+s*z) for w,z in zip(weights,zs))/sum(w/(1+s*z) for w,z in zip(weights,zs))
    g=[(rho+z*z)/(1+s*z)**2/(1+s*s*rho) for z in zs]; total=2*g[0]+g[2]+g[3]
    h=(rho+(1-r)**2-b*b)/mp.sqrt((rho+(1-r)**2-b*b)**2+4*rho*b*b)
    return s*s*total/4,(2*g[0]-g[2]-g[3])/total,2*(g[2]-g[3])/total,h

def prefixes():
    mp.mp.dps=500; rows=[]
    for dv in ('0','.25','.5'):
        for qv in ('.1','.5'):
            d=mp.mpf(dv); r=mp.mpf('.1'); b=r*mp.mpf(qv); s=mp.mpf('.001'); v0=b*b/r; total=mp.mpf(0); product=mp.mpf(1)
            for _ in range(6):
                ov=b*b/r; ob=b; oldr=r; oldq=b/r; olds=s
                s,r,b,h=step(s,r,b,d)
                assert 0<r<=oldr and 0<b/r<=oldq*(1-oldr/2) and 0<s<=olds/32
                assert b*b/r<=ov-ob*ob/2
                total+=ob*ob; product*=h
                assert total+2*b*b/r<=2*v0 and 1-product<=mp.mpf(32)/35*total
            rows.append(dict(delta=dv,q0=qv,events=6,precision_digits=500,final_s=mp.nstr(s,18),final_r=mp.nstr(r,18),final_q=mp.nstr(b/r,18),prefix_sum_b2=mp.nstr(total,18),remaining_sum_bound=mp.nstr(2*b*b/r,18),coherence_product=mp.nstr(product,18),all_event_loss_bound=mp.nstr(mp.mpf(64)/35*v0,18)))
    return rows

def source():
    rng=np.random.default_rng(20261117); update=audit.load_update(); u=audit.complex_unitary(rng,4)
    cross=np.zeros((4,4),complex); x=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); cross[:2,2:]=x; cross[2:,:2]=x.conj().T; cross*=.1/np.linalg.norm(cross,2)
    w=np.eye(4)/4; x=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); kb=x@x.conj().T; kb/=np.trace(kb); k=u@kb@u.conj().T
    calls=0; kr=0.; gr=0.; yr=0.; rows=[]
    for r in (.1,.2):
        for q in (.1,.5):
            for d in (0.,.25,.5):
                s=.001; b=r*q; f=u@(np.diag([1+d,1+d,1-d,1-d])+cross)@u.conj().T
                assert np.linalg.eigvalsh(f).min()>0
                sn,rn,bn,h=map(float,step(mp.mpf(str(s)),mp.mpf(str(r)),mp.mpf(str(b)),mp.mpf(str(d))))
                load=(u*(s*np.array([1+r,1+r,1-r+b,1-r-b])))@u.conj().T
                out=pair_audit.source_aligned(update,k,f,w,load); calls+=1
                got=u.conj().T@out['k']@u; expected=kb[2:,2:].copy(); expected[0,1]*=h; expected[1,0]*=h
                kr=max(kr,float(np.linalg.norm(got[2:,2:]-expected)))
                ey=(u*np.array([1+rn,1+rn,1-rn+bn,1-rn-bn]))@u.conj().T
                yr=max(yr,float(np.linalg.norm(out['y']/(np.trace(out['y']).real/4)-ey)))
                if r==.1 and q==.1 and d in (0.,.5):
                    gauge=audit.complex_unitary(rng,4); conj=lambda x:gauge@x@gauge.conj().T
                    gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(load)); calls+=1; gr=max(gr,float(np.linalg.norm(gout['k']-conj(out['k']))))
                rows.append(dict(r=r,q=q,delta=d,r_next=rn,q_next=bn/rn,V_decrement=b*b/r-bn*bn/rn))
    assert calls==14 and max(kr,gr)<1e-10 and yr<1e-8
    return dict(calls=calls,kernel_residual=kr,gauge_residual=gr,normalized_load_residual=yr,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261117,certificate=certificate(),symbolic=symbolic(),positive_load_prefixes=prefixes(),source=source(),scope='One-sided block formation imbalance delta in [0,1/2]; upper load degeneracy retained. Negative-delta boundary counterexample to old r monotonicity retained.')
    Path(__file__).with_name('lower_pair_formation_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
