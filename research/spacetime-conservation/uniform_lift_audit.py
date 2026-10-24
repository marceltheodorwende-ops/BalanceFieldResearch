"""Uniform balanced-sector lifting: exact source recurrences and analytic tails."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import mpmath as mp
import audit
import pair_audit

TOL=1e-10

def recurrence(scale,r,root):
    q=1+r*r*(1-scale)/(1+scale)
    gm=(q+(1-r)**2)/(1+scale*(1-r))**2/(1+scale*scale*q)
    gp=(q+(1+r)**2)/(1+scale*(1+r))**2/(1+scale*scale*q)
    sn=scale*scale*(gp+gm)/2
    rn=(gp-gm)/(gp+gm)
    h=(q+1-r*r)/root((q+(1-r)**2)*(q+(1+r)**2))
    return sn,rn,h

def symbolic():
    s,r=sp.symbols('s r',positive=True)
    ym=s*(1-r); yp=s*(1+r)
    alpha=pair_audit.alpha_exact([ym,yp],[sp.Integer(1),sp.Integer(1)])
    assert sp.cancel(alpha/((1-alpha)*s*s)-(1+r*r*(1-s)/(1+s)))==0
    gm=pair_audit.g(ym,alpha); gp=pair_audit.g(yp,alpha)
    d=(1+s)**3+r*r*(1-2*s*s-s**3)+r**4*s*s
    rn=r*(1+s)*(1-s*s+r*r*(s*s-2*s))/d
    assert sp.cancel(rn-(gp-gm)/(gp+gm))==0
    p=2*(1+s)**2+r*r*(1-s*s)+r**4*(2+2*s-s*s)
    assert sp.cancel(r/(1+r*r)-rn-r*s*p/((1+r*r)*d))==0
    # Exact domain bounds used in the proof, s<=1/100, r<=1/4.
    upper=2*(1+sp.Rational(1,100))**2+sp.Rational(1,16)+sp.Rational(1,256)*(2+sp.Rational(2,100))
    assert upper<3
    assert 1-2*sp.Rational(1,100)**2-sp.Rational(1,100)**3>0
    return dict(relative_denominator=str(d),positive_difference_factor=str(p),exact_factor_upper_bound=str(upper))

def long_controls():
    mp.mp.dps=80; rows=[]
    for index in range(4):
        epsilon=mp.mpf(1)/(10*2**index); start=epsilon**2; scale=start; r=epsilon; logd=mp.mpf(0)
        count=50*4**index; prefix=0
        while scale>=mp.mpf('1e-60'):
            scale,r,h=recurrence(scale,r,mp.sqrt); logd+=mp.log(h); prefix+=1
            assert 0<r<=epsilon and 0<scale<=start
        cutoff=scale
        for _ in range(prefix,count):
            logd-=mp.log1p(r*r+r**4)/2; r/=1+r*r
        rb=epsilon; logb=mp.mpf(0)
        for _ in range(count):
            logb-=mp.log1p(rb*rb+rb**4)/2; rb/=1+rb*rb
        amplitude_tail=4*cutoff; log_tail=(4+5*epsilon**2)*cutoff
        amplitude_difference=abs(r-rb)/epsilon+amplitude_tail
        log_difference=abs(logd-logb)+log_tail
        assert amplitude_difference<=4*start+mp.mpf('1e-10')
        assert log_difference<=(4+5*epsilon**2)*start+mp.mpf('1e-10')
        rows.append(dict(epsilon=float(epsilon),initial_scale=float(start),derived_recurrence_steps=count,positive_scale_prefix=prefix,cutoff_scale=mp.nstr(cutoff,12),analytic_remaining_amplitude_bound=mp.nstr(amplitude_tail,12),analytic_remaining_log_bound=mp.nstr(log_tail,12),normalized_amplitude_difference=float(amplitude_difference),normalized_amplitude_bound=float(4*start),log_kernel_difference=float(log_difference),log_kernel_bound=float((4+5*epsilon**2)*start),continuum_amplitude_error=float(abs(r/epsilon-1/mp.sqrt(2))),continuum_decay_error=float(abs(mp.exp(logd)-mp.power(2,-mp.mpf(1)/4)))))
    for key in ('continuum_amplitude_error','continuum_decay_error'):
        assert rows[-1][key]<.01 and rows[-1][key]<.4*rows[0][key]
    return rows

def source_controls():
    update=audit.load_update(); rng=np.random.default_rng(20261110)
    maximum=0.; gauge=0.; calls=0
    for n in (2,4):
        u=audit.complex_unitary(rng,n); a=(u*np.r_[-np.ones(n//2),np.ones(n//2)])@u.conj().T
        cross=np.zeros((n,n),complex); block=rng.normal(size=(n//2,n//2))+1j*rng.normal(size=(n//2,n//2))
        cross[:n//2,n//2:]=block; cross[n//2:,:n//2]=block.conj().T; cross*=.2/np.linalg.norm(cross,2)
        f=u@(np.eye(n)+cross)@u.conj().T; w=np.eye(n)/n
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); initial=z@z.conj().T; initial/=np.trace(initial)
        for epsilon in (.1,.05,.025,.0125):
            scale=epsilon**2; r=epsilon; k=initial.copy()
            for event in range(2 if epsilon==.1 else 1):
                y=scale*(np.eye(n)+r*a)
                out=pair_audit.source_aligned(update,k,f,w,y); calls+=1
                sn,rn,h=recurrence(scale,r,np.sqrt)
                predicted=(k+a@k@a)/2+h*(k-a@k@a)/2
                maximum=max(maximum,float(np.linalg.norm(out['y']-sn*(np.eye(n)+rn*a))),float(np.linalg.norm(out['k']-predicted)))
                if epsilon==.1 and event==0:
                    g=audit.complex_unitary(rng,n); conj=lambda x:g@x@g.conj().T
                    gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1
                    gauge=max(gauge,float(np.linalg.norm(gout['k']-conj(out['k']))))
                scale,r,k=sn,rn,out['k']
    assert calls==12 and max(maximum,gauge)<TOL
    return dict(full_source_calls=calls,maximum_source_recurrence_residual=maximum,maximum_gauge_residual=gauge)

def run():
    return dict(status='PASS: uniform lifting in exact balanced positive-load sector; physical spacetime OPEN',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=20261110,symbolic=symbolic(),long_recurrence=long_controls(),source=source_controls(),precision_decimal_digits=80,scope='Analytic uniform theorem plus high-precision reduced recurrence prefixes and bounded boundary tails; not long original-source runs')

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('uniform_lift_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
