"""Formation imbalance in the BFG-derived two-level relative boundary map."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.optimize import brentq
import audit
import pair_audit

TOL=1e-10

def recurrence(scale,r,delta):
    q=(1+r*r+2*delta*r+scale*(1-r*r)*(1+delta*r))/(1+scale-delta*scale*r)
    gm=(q+(1-r)**2)/(1+scale*(1-r))**2/(1+scale*scale*q)
    gp=(q+(1+r)**2)/(1+scale*(1+r))**2/(1+scale*scale*q)
    h=(q+1-r*r)/np.sqrt((q+(1-r)**2)*(q+(1+r)**2))
    return scale*scale*(gm+gp)/2,(gp-gm)/(gp+gm),h

def symbolic():
    s,r,d,e,k,u=sp.symbols('s r d e k u',real=True)
    alpha=pair_audit.alpha_exact([s*(1-r),s*(1+r)],[(1-d)/2,(1+d)/2])
    q=(1+r*r+2*d*r+s*(1-r*r)*(1+d*r))/(1+s-d*s*r)
    assert sp.cancel(alpha/((1-alpha)*s*s)-q)==0
    qb=1+r*r+2*d*r
    gp=qb+(1+r)**2; gm=qb+(1-r)**2
    rp=r/(1+d*r+r*r)
    assert sp.cancel((gp-gm)/(gp+gm)-rp)==0
    assert sp.cancel(1/rp-1/r-d-r)==0
    hs=(1+d*r)**2/((1+d*r+r*r)**2-r*r)
    assert sp.cancel(hs.subs(r,-d)-(1-d*d))==0
    a=sp.symbols('a',positive=True)
    assert sp.cancel(a-rp.subs(d,-a)-(a-r)*(1-a*r)/(1-a*r+r*r))==0
    assert sp.limit((hs.subs({d:k*e,r:e*u})-1)/e**2,e,0)==-u*u
    return dict(boundary_amplitude=str(rp),boundary_h_squared=str(hs),reciprocal_increment='delta+r',negative_imbalance_fixed_h_squared='1-delta**2',critical_h_second_coefficient='-u**2/2')

def reference(kappa):
    if kappa==0:
        return 2**(-.5),2**(-.25)
    primitive=lambda u:np.log((kappa+u)/u)/kappa**2-1/(kappa*u)
    root=brentq(lambda u:primitive(1)-primitive(u)-.5,max(0.,-kappa)+1e-8,1.,xtol=1e-14)
    return root,np.sqrt((kappa+root)/(kappa+1))

def long_controls():
    rows=[]
    for kappa in (-.5,0.,.5):
        target_u,target_d=reference(kappa); cases=[]
        for index,epsilon in enumerate((.1,.05,.025,.0125)):
            delta=kappa*epsilon; r=epsilon; logd=0.; count=50*4**index
            for _ in range(count):
                h=(1+delta*r)/np.sqrt((1+delta*r+r*r)**2-r*r)
                logd+=np.log(h); r/=1+delta*r+r*r
            cases.append(dict(epsilon=epsilon,boundary_steps=count,scaled_amplitude=r/epsilon,kernel_decay=float(np.exp(logd)),amplitude_error=abs(r/epsilon-target_u),decay_error=abs(float(np.exp(logd))-target_d)))
        for key in ('amplitude_error','decay_error'):
            assert cases[-1][key]<.01 and cases[-1][key]<.4*cases[0][key]
        rows.append(dict(kappa=kappa,reference_u=target_u,reference_decay=target_d,cases=cases))
    fixed=[]
    for index,epsilon in enumerate((.1,.05,.025,.0125)):
        delta=.05; r=epsilon; count=50*4**index
        for _ in range(count):
            r/=1+delta*r+r*r
        upper=1/(1/epsilon+delta*count)
        assert r<=upper+TOL
        fixed.append(dict(epsilon=epsilon,boundary_steps=count,r=r,upper_bound=upper,scaled_amplitude=r/epsilon))
    return rows,fixed

def source_controls():
    update=audit.load_update(); rng=np.random.default_rng(20261111)
    maximum=0.; gauge=0.; calls=0
    for n in (2,4):
        u=audit.complex_unitary(rng,n); eig=np.r_[-np.ones(n//2),np.ones(n//2)]; a=(u*eig)@u.conj().T
        cross=np.zeros((n,n),complex); block=rng.normal(size=(n//2,n//2))+1j*rng.normal(size=(n//2,n//2))
        cross[:n//2,n//2:]=block; cross[n//2:,:n//2]=block.conj().T; cross*=.1/np.linalg.norm(cross,2)
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); initial=z@z.conj().T; initial/=np.trace(initial)
        w=np.eye(n)/n
        for delta in (-.05,0.,.025,.05):
            f=u@(np.diag(1+delta*eig)+cross)@u.conj().T
            assert abs(np.trace(f@a).real/np.trace(f).real-delta)<TOL
            scale=.001; r=.05; k=initial.copy()
            for event in range(2 if delta==.025 else 1):
                y=scale*(np.eye(n)+r*a); out=pair_audit.source_aligned(update,k,f,w,y); calls+=1
                sn,rn,h=recurrence(scale,r,delta)
                predicted=(k+a@k@a)/2+h*(k-a@k@a)/2
                maximum=max(maximum,float(np.linalg.norm(out['k']-predicted)),float(np.linalg.norm(out['y']-sn*(np.eye(n)+rn*a))))
                if delta==-.05:
                    g=audit.complex_unitary(rng,n); conj=lambda x:g@x@g.conj().T
                    gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1
                    gauge=max(gauge,float(np.linalg.norm(gout['k']-conj(out['k']))))
                scale,r,k=sn,rn,out['k']
    assert calls==12 and max(maximum,gauge)<TOL
    return dict(full_source_calls=calls,maximum_source_recurrence_residual=maximum,maximum_gauge_residual=gauge)

def run():
    exact=symbolic(); critical,fixed=long_controls()
    return dict(status='PASS: imbalance changes boundary scaling; critical imbalance family derived',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=20261111,symbolic=exact,critical_boundary=critical,fixed_positive_imbalance=fixed,source=source_controls(),scope='Imbalanced long-time conclusions are boundary-map statements; balanced positive-load lifting is not extended here')

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('imbalance_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
