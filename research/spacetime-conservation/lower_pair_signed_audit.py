"""Alternate q-squared Lyapunov bound with a signed formation interval."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
import audit
import pair_audit
from lower_pair_formation_audit import step

def certificate():
    s,r,a=sp.symbols('s r a'); d=-a
    rho=(1+r*r+2*d*r+s*(1-r*r)*(1+d*r))/(1+s-d*s*r)
    gm=(rho+(1-r)**2)/(1+s*(1-r))**2
    gp=(rho+(1+r)**2)/(1+s*(1+r))**2
    exact=sp.cancel((gp-gm)/(gp+gm)); boundary=r/(1+d*r+r*r)
    E=sp.cancel((boundary-exact)/(s*r))
    num,den=sp.fraction(E)
    if den.subs({s:0,r:0,a:0})<0:num,den=-num,-den
    bounds={s:sp.Rational(1,100),r:sp.Rational(1,4),a:sp.Rational(1,8)}
    def enclose(x):
        p=sp.Poly(x,s,r,a); mass=sum(abs(c)*sp.prod(bounds[v]**k for v,k in zip(p.gens,m)) for m,c in p.terms())
        return sp.cancel(2*p.coeff_monomial(1)-mass),sp.cancel(mass)
    nl,nu=enclose(num); dl,du=enclose(den)
    row=dict(numerator_lower=str(nl),numerator_mass=str(nu),denominator_lower=str(dl),denominator_mass=str(du))
    assert nl>0 and dl>0,row
    assert sp.cancel(boundary-exact-s*r*E)==0
    assert sp.cancel(sp.diff(boundary,r)-(1-r*r)/(1-a*r+r*r)**2)==0
    return row

def prefixes():
    mp.mp.dps=500; rows=[]
    for rv in ('.05','.2'):
        for dv in ('-.125','-.0625'):
            r=mp.mpf(rv); d=mp.mpf(dv); q=mp.mpf('.1'); b=r*q; s=mp.mpf('.001'); u0=q*q; total=mp.mpf(0); product=mp.mpf(1); grows=False
            for _ in range(6):
                oldr=r; oldq=b/r; oldb=b; olds=s
                s,r,b,h=step(s,r,b,d); grows|=r>oldr
                assert 0<r<=mp.mpf('.25') and 0<b/r<=oldq*(1-oldr/2) and s<=olds/32
                assert oldq**2-(b/r)**2>=2*oldb**2
                total+=oldb**2; product*=h
                assert total+(b/r)**2/2<=u0/2
                assert 1-product<=mp.mpf(32)/35*total
            rows.append(dict(r0=rv,delta=dv,events=6,precision_digits=500,r_grew=grows,final_s=mp.nstr(s,18),final_r=mp.nstr(r,18),final_q=mp.nstr(b/r,18),prefix_sum_b2=mp.nstr(total,18),remaining_sum_b2_bound=mp.nstr((b/r)**2/2,18),coherence_product=mp.nstr(product,18),all_event_loss_bound=mp.nstr(mp.mpf(16)/35*u0,18)))
    assert any(x['r_grew'] for x in rows)
    return rows

def source():
    rng=np.random.default_rng(20261118); update=audit.load_update(); u=audit.complex_unitary(rng,4)
    cross=np.zeros((4,4),complex); x=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); cross[:2,2:]=x; cross[2:,:2]=x.conj().T; cross*=.1/np.linalg.norm(cross,2)
    w=np.eye(4)/4; x=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); kb=x@x.conj().T; kb/=np.trace(kb); k=u@kb@u.conj().T
    kr=0.; gr=0.; yr=0.; calls=0; rows=[]
    for r in (.05,.2):
        for d in (-.125,-.0625,0.):
            s=.001; q=.1; b=r*q; f=u@(np.diag([1+d,1+d,1-d,1-d])+cross)@u.conj().T
            sn,rn,bn,h=map(float,step(mp.mpf(str(s)),mp.mpf(str(r)),mp.mpf(str(b)),mp.mpf(str(d))))
            load=(u*(s*np.array([1+r,1+r,1-r+b,1-r-b])))@u.conj().T
            out=pair_audit.source_aligned(update,k,f,w,load); calls+=1
            got=u.conj().T@out['k']@u; expected=kb[2:,2:].copy(); expected[0,1]*=h; expected[1,0]*=h
            kr=max(kr,float(np.linalg.norm(got[2:,2:]-expected)))
            ey=(u*np.array([1+rn,1+rn,1-rn+bn,1-rn-bn]))@u.conj().T
            yr=max(yr,float(np.linalg.norm(out['y']/(np.trace(out['y']).real/4)-ey)))
            assert 0<rn<=.25 and bn/rn<=q*(1-r/2)
            if r==.05 and d in (-.125,0.):
                gauge=audit.complex_unitary(rng,4); conj=lambda z:gauge@z@gauge.conj().T
                gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(load)); calls+=1; gr=max(gr,float(np.linalg.norm(gout['k']-conj(out['k']))))
            rows.append(dict(r=r,delta=d,r_next=rn,q_next=bn/rn,r_grew=rn>r))
    assert calls==8 and max(kr,gr)<1e-10 and yr<1e-8 and any(x['r_grew'] for x in rows)
    return dict(calls=calls,kernel_residual=kr,gauge_residual=gr,normalized_load_residual=yr,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261118,certificate=certificate(),positive_load_prefixes=prefixes(),source=source(),scope='Negative block imbalance delta in [-1/8,0], upper degeneracy retained; weaker all-event loss <=16q0²/35 despite possible r growth.')
    Path(__file__).with_name('lower_pair_signed_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
