"""Actual BFG small-load limit with retained normalized shape."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import audit
import pair_audit

TOL=1e-10

def run():
    scale=sp.symbols('s',positive=True)
    ys=[scale/2,3*scale/2]; alpha=pair_audit.alpha_exact(ys,[sp.Integer(1),sp.Integer(1)])
    assert sp.limit(alpha/scale**2,scale,0)==sp.Rational(5,4)
    exact=[sp.limit(pair_audit.g(v,alpha)/scale**2,scale,0) for v in ys]
    assert exact==[sp.Rational(3,2),sp.Rational(7,2)]
    h=sp.Rational(2)/sp.sqrt(sp.Rational(3,2)*sp.Rational(7,2))
    assert sp.simplify(h-4/sp.sqrt(21))==0 and h<1
    update=audit.load_update(); rng=np.random.default_rng(20261108)
    calls=0; source_residual=0.; gauge_residual=0.; scalar_residual=0.; rows=[]
    for n in (2,3,4):
        if n==2:
            f=np.eye(2); z=np.diag([.5,1.5]); k=np.ones((2,2))/2
        else:
            u=audit.complex_unitary(rng,n); z=(u*np.linspace(.7,1.3,n))@u.conj().T
            a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); f=a@a.conj().T+np.eye(n)
            z/=np.trace(f@z).real/np.trace(f).real
            a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=a@a.conj().T; k/=np.trace(k)
        w=np.eye(n)/n; mean=lambda a:float(np.trace(f@a).real/np.trace(f).real)
        mu=mean(z@z); shape_limit=(mu*np.eye(n)+z@z)/(2*mu)
        vals,u=np.linalg.eigh(z); inv=(u*(1/np.sqrt(mu+vals*vals)))@u.conj().T
        tc=np.sqrt(mu)*inv; tb=z@inv; kernel_limit=tc@k@tc+tb@k@tb
        expected_jump=float(np.linalg.norm(kernel_limit-k)); cases=[]
        for value in (.05,.025,.0125,.00625):
            y=value*z; aligned=audit.aligned(k,f,y)
            out=pair_audit.source_aligned(update,k,f,w,y); calls+=1
            splus=mean(out['y']); shape=out['y']/splus
            c=np.linalg.inv(np.eye(n)+value*z)
            relative_ratio=mean(z@z@c)/mean(c)
            exact_load=value**2*(relative_ratio*np.eye(n)+z@z)@c@c/(1+value**2*relative_ratio)
            relative_inv=(u*(1/np.sqrt(relative_ratio+vals*vals)))@u.conj().T
            exact_tc=np.sqrt(relative_ratio)*relative_inv; exact_tb=z@relative_inv
            exact_kernel=exact_tc@k@exact_tc+exact_tb@k@exact_tb
            source_residual=max(source_residual,float(np.linalg.norm(exact_load-out['y'])),float(np.linalg.norm(exact_kernel-out['k'])))
            source_residual=max(source_residual,float(np.linalg.norm(out['k']-aligned['k'])),float(np.linalg.norm(out['y']-aligned['y'])),float(np.linalg.norm(splus*shape-out['y'])))
            if value==.05:
                g=audit.complex_unitary(rng,n); conj=lambda a:g@a@g.conj().T
                gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1
                gauge_residual=max(gauge_residual,float(np.linalg.norm(gout['k']-conj(out['k']))),float(np.linalg.norm(gout['y']-conj(out['y']))))
            cases.append(dict(s=value,alpha_error=abs(float(out['alpha'])/value**2-mu),scale_error=abs(splus/value**2-2*mu),shape_error=float(np.linalg.norm(shape-shape_limit)),kernel_error=float(np.linalg.norm(out['k']-kernel_limit)),kernel_jump=float(np.linalg.norm(out['k']-k))))
        for key in ('alpha_error','scale_error','shape_error','kernel_error'):
            assert cases[-1][key]<.1 and (cases[0][key]<=1e-10 or cases[-1][key]<.4*cases[0][key])
        if n==2:
            assert cases[-1]['kernel_jump']>expected_jump/2
            for value in (.05,.025,.0125,.00625):
                out=pair_audit.source_aligned(update,k,f,w,value*np.eye(n)); calls+=1
                scalar_residual=max(scalar_residual,float(np.linalg.norm(out['k']-k)))
        rows.append(dict(n=n,mu2=mu,boundary_kernel_jump=expected_jump,cases=cases))
    assert calls==19 and max(source_residual,gauge_residual,scalar_residual)<TOL
    return dict(status='PASS: normalized boundary map; vanishing raw load alone does not ensure small kernel step',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=20261108,full_source_calls=calls,exact_witness_alpha=str(alpha),exact_witness_scaled_load_limit=[str(v) for v in exact],exact_witness_h=str(h),maximum_source_residual=source_residual,maximum_gauge_residual=gauge_residual,maximum_scalar_kernel_residual=scalar_residual,cases=rows,boundary_scope='s=0 is a mathematical relative-load chart, never a source call')

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('small_load_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
