"""Coupled slow limit of the BFG-derived relative boundary map only."""
import json
from pathlib import Path
import numpy as np
import sympy as s
import audit
import pair_audit

TOL=1e-10

def run():
    r=s.symbols('r',positive=True)
    a=s.diag(-1,0,1); mu=s.Rational(2,3); z=s.eye(3)+r*a
    shape=(s.eye(3)+z*z/(1+r*r*mu))/2
    normal=s.eye(3)+(r*a+r*r*(a*a-mu*s.eye(3))/2)/(1+r*r*mu)
    assert (shape-normal).applyfunc(s.cancel)==s.zeros(3)
    assert a*a-mu*s.eye(3)!=s.zeros(3)
    za=1-r; zb=1+r; m=1+r*r
    h2=s.cancel((m+za*zb)**2/((m+za*za)*(m+zb*zb)))
    assert s.cancel(h2-1/(1+r*r+r**4))==0
    split=s.cancel(((m+zb*zb)/(2*m)-(m+za*za)/(2*m))/2)
    assert s.cancel(split-r/(1+r*r))==0
    boundary=[]
    for index,epsilon in enumerate((.1,.05,.025,.0125)):
        amplitude=epsilon; log_decay=0.; count=50*4**index
        for _ in range(count):
            log_decay-=.5*np.log1p(amplitude**2+amplitude**4)
            amplitude/=1+amplitude**2
        boundary.append(dict(epsilon=epsilon,boundary_iterations=count,scaled_amplitude=amplitude/epsilon,kernel_decay=float(np.exp(log_decay)),amplitude_error=abs(amplitude/epsilon-2**(-.5)),decay_error=abs(float(np.exp(log_decay))-2**(-.25))))
    for key in ('amplitude_error','decay_error'):
        assert boundary[-1][key]<.01 and boundary[-1][key]<.4*boundary[0][key]
    update=audit.load_update(); rng=np.random.default_rng(20261109)
    calls=0; source_residual=0.; gauge_residual=0.; boundary_error=0.; cases=[]
    for n in (2,4,3):
        u=audit.complex_unitary(rng,n)
        eigen=np.array([-1.,0.,1.]) if n==3 else np.r_[-np.ones(n//2),np.ones(n//2)]
        a=(u*eigen)@u.conj().T; f=np.eye(n); w=np.eye(n)/n
        q=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=q@q.conj().T; k/=np.trace(k)
        for amplitude in (.1,.05,.025,.0125):
            z=np.eye(n)+amplitude*a; y=.001*z
            out=pair_audit.source_aligned(update,k,f,w,y); calls+=1
            aligned=audit.aligned(k,f,y)
            source_residual=max(source_residual,float(np.linalg.norm(out['k']-aligned['k'])),float(np.linalg.norm(out['y']-aligned['y'])))
            mu=float(np.trace(z@z).real/n); limit=(mu*np.eye(n)+z@z)/(2*mu)
            actual=out['y']/(np.trace(out['y']).real/n)
            error=float(np.linalg.norm(actual-limit)); boundary_error=max(boundary_error,error)
            if n!=3 and amplitude==.1:
                g=audit.complex_unitary(rng,n); conj=lambda x:g@x@g.conj().T
                gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1
                gauge_residual=max(gauge_residual,float(np.linalg.norm(gout['k']-conj(out['k']))),float(np.linalg.norm(gout['y']-conj(out['y']))))
            cases.append(dict(n=n,r=amplitude,finite_source_to_boundary_shape_error=error))
    assert calls==14 and max(source_residual,gauge_residual)<TOL and boundary_error<.01
    return dict(status='PASS: coupled two-level relative-boundary limit; full-source uniform lifting OPEN',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=20261109,symbolic_h_squared=str(h2),symbolic_amplitude_successor=str(split),generic_quadratic_shape_defect=[str(v) for v in (s.diag(-1,0,1)**2-s.Rational(2,3)*s.eye(3)).diagonal()],full_source_calls=calls,maximum_source_residual=source_residual,maximum_gauge_residual=gauge_residual,maximum_finite_boundary_shape_error=boundary_error,boundary_scaling=boundary,source_cases=cases,scope='Boundary iterations are not complete source trajectories; no physical clock selected')

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('relative_slow_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
