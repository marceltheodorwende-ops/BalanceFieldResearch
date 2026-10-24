"""Exact rectangle certificates and uniform critical-imbalance source lift."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
import audit
import pair_audit
import imbalance_audit

TOL=1e-10

def certificates():
    s,r,d=sp.symbols('s r d')
    q=(1+r*r+2*d*r+s*(1-r*r)*(1+d*r))/(1+s-d*s*r)
    gm=(q+(1-r)**2)/(1+s*(1-r))**2
    gp=(q+(1+r)**2)/(1+s*(1+r))**2
    exact=sp.cancel((gp-gm)/(gp+gm)); boundary=r/(1+d*r+r*r)
    e=sp.cancel((exact-boundary)/(s*r))
    assert sp.cancel(exact-boundary-s*r*e)==0
    assert sp.cancel(sp.diff(q,s)+2*(1-d*d)*r*r/(1+s*(1-d*r))**2)==0
    h2=(1+d*r)**2/((1+d*r+r*r)**2-r*r)
    second=sp.cancel(sp.diff(h2,r,2)/(2*h2)-sp.diff(h2,r)**2/(2*h2*h2))
    bounds={s:sp.Rational(1,100),r:sp.Rational(1,4),d:sp.Rational(1,20)}
    rows={}
    for name,expression in (('C_R',e),('C_L',second)):
        num,den=map(sp.Poly,sp.fraction(expression))
        def mass(poly):
            return sum(abs(coef)*sp.prod(bounds[v]**power for v,power in zip(poly.gens,mon)) for mon,coef in poly.terms())
        constant=abs(den.eval({v:0 for v in den.gens}))
        lower=2*constant-mass(den); upper=mass(num)
        assert lower>0
        bound=sp.cancel(upper/lower); integer=int(sp.ceiling(bound))
        rows[name]=dict(numerator_mass=str(upper),denominator_lower=str(lower),rational_bound=str(bound),integer_bound=integer)
    return rows

def mp_step(scale,r,delta):
    q=(1+r*r+2*delta*r+scale*(1-r*r)*(1+delta*r))/(1+scale-delta*scale*r)
    gm=(q+(1-r)**2)/(1+scale*(1-r))**2/(1+scale*scale*q)
    gp=(q+(1+r)**2)/(1+scale*(1+r))**2/(1+scale*scale*q)
    h=(q+1-r*r)/mp.sqrt((q+(1-r)**2)*(q+(1+r)**2))
    return scale*scale*(gp+gm)/2,(gp-gm)/(gp+gm),h

def boundary_step(r,delta):
    h=(1+delta*r)/mp.sqrt((1+delta*r+r*r)**2-r*r)
    return r/(1+delta*r+r*r),h

def long_controls(cert):
    mp.mp.dps=80; cr=cert['C_R']['integer_bound']; cl=cert['C_L']['integer_bound']
    ct=3*cr*mp.exp(mp.mpf('1.5')); rows=[]
    for kappa in (-.5,0.,.5):
        target_u,target_d=imbalance_audit.reference(kappa); cases=[]
        for index in range(4):
            epsilon=mp.mpf(1)/(10*2**index); start=epsilon**4; scale=start; delta=mp.mpf(kappa)*epsilon
            r=epsilon; logd=mp.mpf(0); count=50*4**index; prefix=0
            assert ct*start<=mp.mpf('.5')
            while scale>=mp.mpf('1e-60'):
                old=scale; scale,r,h=mp_step(scale,r,delta); logd+=mp.log(h); prefix+=1
                assert 0<r<=2*epsilon and 0<scale<=old/32
            cutoff=scale
            for _ in range(prefix,count):
                r,h=boundary_step(r,delta); logd+=mp.log(h)
            rb=epsilon; logb=mp.mpf(0)
            for _ in range(count):
                rb,h=boundary_step(rb,delta); logb+=mp.log(h)
            # Residual tail is bounded in the same fixed epsilon coordinates.
            amplitude_difference=abs(r-rb)/epsilon+ct*cutoff
            log_difference=abs(logd-logb)+(17*epsilon**2+cl*ct)*cutoff
            amplitude_bound=ct*start; log_bound=(17*epsilon**2+cl*ct)*start
            assert amplitude_difference<=amplitude_bound+TOL and log_difference<=log_bound+TOL
            cases.append(dict(epsilon=float(epsilon),initial_scale=float(start),derived_steps=count,positive_scale_prefix=prefix,cutoff_scale=mp.nstr(cutoff,10),bootstrap_quantity=float(ct*start),normalized_amplitude_difference=float(amplitude_difference),amplitude_bound=float(amplitude_bound),log_kernel_difference=float(log_difference),log_kernel_bound=float(log_bound),continuum_amplitude_error=float(abs(r/epsilon-target_u)),continuum_decay_error=float(abs(mp.exp(logd)-target_d))))
        for key in ('continuum_amplitude_error','continuum_decay_error'):
            assert cases[-1][key]<.01 and cases[-1][key]<.4*cases[0][key]
        rows.append(dict(kappa=kappa,cases=cases))
    return dict(C_T_at_half=float(ct),cases=rows)

def source_controls():
    update=audit.load_update(); rng=np.random.default_rng(20261112); maximum=0.; gauge=0.; calls=0
    for n in (2,4):
        u=audit.complex_unitary(rng,n); eig=np.r_[-np.ones(n//2),np.ones(n//2)]; a=(u*eig)@u.conj().T
        off=np.zeros((n,n),complex); block=rng.normal(size=(n//2,n//2))+1j*rng.normal(size=(n//2,n//2))
        off[:n//2,n//2:]=block; off[n//2:,:n//2]=block.conj().T; off*=.1/np.linalg.norm(off,2)
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=z@z.conj().T; k/=np.trace(k); w=np.eye(n)/n
        for kappa in (-.5,0.,.5):
            for epsilon in (.1,.05):
                delta=kappa*epsilon; f=u@(np.diag(1+delta*eig)+off)@u.conj().T; scale=epsilon**4
                y=scale*(np.eye(n)+epsilon*a); out=pair_audit.source_aligned(update,k,f,w,y); calls+=1
                sn,rn,h=imbalance_audit.recurrence(scale,epsilon,delta)
                predicted=(k+a@k@a)/2+h*(k-a@k@a)/2
                maximum=max(maximum,float(np.linalg.norm(out['k']-predicted)),float(np.linalg.norm(out['y']-sn*(np.eye(n)+rn*a))))
                if kappa==-.5 and epsilon==.1:
                    g=audit.complex_unitary(rng,n); conj=lambda x:g@x@g.conj().T
                    gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1
                    gauge=max(gauge,float(np.linalg.norm(gout['k']-conj(out['k']))))
    assert calls==14 and max(maximum,gauge)<TOL
    return dict(full_source_calls=calls,maximum_source_residual=maximum,maximum_gauge_residual=gauge)

def run():
    cert=certificates()
    return dict(status='PASS: uniform critical-imbalance lifting to exact positive-load sector',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=20261112,rectangle_certificates=cert,long_recurrence=long_controls(cert),source=source_controls(),precision_decimal_digits=80,scope='Exact coefficient proof; reduced high-precision prefixes and bounded tails are separate from short original-source calls and physical time')

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('critical_lift_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
