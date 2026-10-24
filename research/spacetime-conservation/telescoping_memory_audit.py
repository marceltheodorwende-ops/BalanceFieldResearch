"""Conditioned all-event lower-pair memory via strong-convexity telescoping."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
import audit
import pair_audit

def symbolic():
    y,alpha,beta=sp.symbols('y alpha beta'); g=(alpha+beta*y*y)/(1+y)**2
    assert sp.cancel(sp.diff(g,y)-2*(beta*y-alpha)/(1+y)**3)==0
    assert sp.cancel(sp.diff(g,y,2)-2*(beta*(1-2*y)+3*alpha)/(1+y)**4)==0
    assert 1/sp.Rational(5,4)**4==sp.Rational(256,625)
    assert sp.Rational(256,625)/4==sp.Rational(64,625)
    assert sp.Rational(5,8)/sp.Rational(64,625)==sp.Rational(3125,512)
    return dict(curvature_lower='256*beta/625',derivative_upper='2*beta*M',relative_gap_decrement='1-eta_next/eta >= 64*(y3-y2)/(625*M)',comparison_constant='3125*n*kappa/[512*(1-eta0)]',telescoping='sum chi_j²/2 <= C0*(eta0²-etaN²)',scope='M<=1/4 in invariant class C; fixed full persistence')

def step(ys,weights):
    ell2=sum(w*y*y/(1+y) for w,y in zip(weights,ys))/sum(w/(1+y) for w,y in zip(weights,ys))
    out=[(ell2+y*y)/((1+y)**2*(1+ell2)) for y in ys]
    h=(ell2+ys[0]*ys[1])/mp.sqrt((ell2+ys[0]**2)*(ell2+ys[1]**2))
    chi2=(ys[1]-ys[0])**2/ell2
    return out,h,chi2

def prefixes():
    mp.mp.dps=500; rows=[]
    for ev in ('.01','.1'):
        for kv in (1,4,16):
            e=mp.mpf(ev); ys=[mp.mpf('.06'),mp.mpf('.06')+mp.mpf('.05')*e,mp.mpf('.11'),mp.mpf('.12')]
            weights=[mp.power(kv,mp.mpf(i)/3) for i in range(4)]; C=mp.mpf(3125)*4*kv/(512*(1-e)); total=mp.mpf(0); defects=mp.mpf(0); product=mp.mpf(1)
            for _ in range(6):
                eta=(ys[1]-ys[0])/(ys[2]-ys[0]); M=max(ys)
                assert M<=mp.mpf('.25') and min(ys)>=2*M*M
                out,h,chi2=step(ys,weights); en=(out[1]-out[0])/(out[2]-out[0])
                assert 1-en/eta>=mp.mpf(64)/625*(ys[2]-ys[1])/M
                assert chi2/2<=C*(eta*eta-en*en)
                total+=chi2/2; defects+=1-h; product*=h; ys=out
                assert defects<=total and total<=C*(e*e-en*en)
            rows.append(dict(initial_eta=ev,formation_condition=kv,events=6,precision_digits=500,final_M=mp.nstr(max(ys),18),final_eta=mp.nstr(en,18),half_chi_squared_sum=mp.nstr(total,18),defect_sum=mp.nstr(defects,18),coherence_product=mp.nstr(product,18),uniform_loss_bound=mp.nstr(min(1,C*e*e),18),remaining_half_chi_sum_bound=mp.nstr(C*en*en,18)))
    return rows

def source():
    rng=np.random.default_rng(20261122); update=audit.load_update(); kr=0.; yr=0.; gr=0.; calls=0; rows=[]
    for n in (3,4):
        u=audit.complex_unitary(rng,n); ys=.1*np.array([.6,.601,1.2] if n==3 else [.6,.601,1.1,1.2]); y=(u*ys)@u.conj().T; w=np.eye(n)/n
        x=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); kb=x@x.conj().T; kb/=np.trace(kb); k=u@kb@u.conj().T
        eta=(ys[1]-ys[0])/(ys[2]-ys[0]); M=ys[-1]
        for condition in (1.,4.,16.):
            v=audit.complex_unitary(rng,n); f=(v*np.geomspace(1.,condition,n))@v.conj().T; weights=np.diag(u.conj().T@f@u).real
            ell2=np.sum(weights*ys*ys/(1+ys))/np.sum(weights/(1+ys)); gy=(ell2+ys*ys)/((1+ys)**2*(1+ell2)); en=(gy[1]-gy[0])/(gy[2]-gy[0])
            h=(ell2+ys[0]*ys[1])/np.sqrt((ell2+ys[0]**2)*(ell2+ys[1]**2)); chi2=(ys[1]-ys[0])**2/ell2; C=3125*n*condition/(512*(1-eta))
            assert 1-en/eta>=64/625*(ys[2]-ys[1])/M-1e-12
            assert 1-h<=chi2/2+1e-12 and chi2/2<=C*(eta*eta-en*en)+1e-12
            out=pair_audit.source_aligned(update,k,f,w,y); calls+=1; got=u.conj().T@out['k']@u
            expected=kb[:2,:2].copy(); expected[0,1]*=h; expected[1,0]*=h
            kr=max(kr,float(np.linalg.norm(got[:2,:2]-expected))); yr=max(yr,float(np.linalg.norm(out['y']-(u*gy)@u.conj().T)))
            if n==4:
                gauge=audit.complex_unitary(rng,n); conj=lambda z:gauge@z@gauge.conj().T
                gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1; gr=max(gr,float(np.linalg.norm(gout['k']-conj(out['k']))),float(np.linalg.norm(gout['y']-conj(out['y']))))
            rows.append(dict(n=n,formation_condition=condition,eta=eta,eta_next=en,one_step_loss=1-h,half_chi_squared=chi2/2,telescoping_step_bound=C*(eta*eta-en*en),uniform_loss_bound=min(1,C*eta*eta)))
    assert calls==9 and max(kr,yr,gr)<1e-10
    return dict(calls=calls,kernel_residual=kr,load_residual=yr,gauge_residual=gr,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261122,symbolic=symbolic(),positive_load_prefixes=prefixes(),source=source(),scope='All-event conditioned lower-pair memory in class C with M<=1/4, n>=3 and y1<y2<y3. No upper block assumption. Not physical energy-momentum conservation.')
    Path(__file__).with_name('telescoping_memory_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
