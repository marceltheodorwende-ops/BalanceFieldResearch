"""Formation-aware one-event coherence bounds; summability kept separate."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import audit
import pair_audit

def symbolic():
    l,u,v=sp.symbols('l u v',positive=True)
    den=(l*l+u*u)*(l*l+v*v); numerator=(l*l+u*v)**2
    assert sp.expand(den-numerator-l*l*(v-u)**2)==0
    # h=(1+x)^(-1/2), x=l²(v-u)²/(l²+uv)²; use 1-h<=x/2 and l²+uv>=l².
    e=sp.symbols('e',positive=True); ys=[2*e*e,4*e*e,e]
    alpha=pair_audit.alpha_exact(ys,[sp.Integer(1),sp.Integer(1),e**6])
    chi2=sp.cancel((ys[1]-ys[0])**2*(1-alpha)/alpha)
    assert sp.limit(chi2,e,0)==sp.Rational(2,5)
    return dict(exact_defect_identity='(ell²+u²)(ell²+v²)-(ell²+uv)²=ell²(v-u)²',single_event='1-h<=chi²/2',formation_lower='ell²>=M²/[n*kappa*(1+M)]',conditioned_gap_bound='1-h<=3*n*kappa*eta²/4',counterfamily_chi_squared_limit='2/5',counterfamily_bound_limit='1/5, not zero')

def source():
    update=audit.load_update(); rng=np.random.default_rng(20261121); calls=0; kr=0.; yr=0.; gr=0.; rows=[]
    for n in (3,4):
        u=audit.complex_unitary(rng,n); z=np.array([1.,1.01,1.2] if n==3 else [1.,1.01,1.15,1.2]); ys=.02*z
        y=(u*ys)@u.conj().T; w=np.eye(n)/n
        x=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); kb=x@x.conj().T; kb/=np.trace(kb); k=u@kb@u.conj().T
        for condition in (1.,4.,16.):
            v=audit.complex_unitary(rng,n); f=(v*np.geomspace(1.,condition,n))@v.conj().T
            weights=np.diag(u.conj().T@f@u).real
            lc=np.sum(weights/(1+ys)); lb=np.sum(weights*ys*ys/(1+ys)); ell2=lb/lc
            d=ys[1]-ys[0]; eta=d/(ys[2]-ys[0]); chi2=d*d/ell2
            h=(ell2+ys[0]*ys[1])/np.sqrt((ell2+ys[0]**2)*(ell2+ys[1]**2))
            lower=ys[-1]**2/(n*condition*(1+ys[-1])); gap_bound=3*n*condition*eta*eta/4
            assert ell2>=lower-1e-12 and 1-h<=chi2/2+1e-12 and 1-h<=gap_bound+1e-12
            out=pair_audit.source_aligned(update,k,f,w,y); calls+=1
            got=u.conj().T@out['k']@u; expected=kb[:2,:2].copy(); expected[0,1]*=h; expected[1,0]*=h
            kr=max(kr,float(np.linalg.norm(got[:2,:2]-expected)))
            alpha=ell2/(1+ell2); gy=(alpha+(1-alpha)*ys*ys)/(1+ys)**2
            yr=max(yr,float(np.linalg.norm(out['y']-(u*gy)@u.conj().T)))
            if n==4:
                g=audit.complex_unitary(rng,n); conj=lambda x:g@x@g.conj().T
                gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1
                gr=max(gr,float(np.linalg.norm(gout['k']-conj(out['k']))),float(np.linalg.norm(gout['y']-conj(out['y']))))
            rows.append(dict(n=n,formation_condition=condition,ell_squared=ell2,ell_squared_lower=lower,chi_squared=chi2,eta=eta,one_step_loss=1-h,chi_loss_bound=chi2/2,conditioned_gap_loss_bound=gap_bound))
    assert calls==9 and max(kr,yr,gr)<1e-10
    return dict(calls=calls,kernel_residual=kr,load_residual=yr,gauge_residual=gr,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261121,symbolic=symbolic(),source=source(),scope='Formation-aware one-step and conditional finite-history bounds. No automatic summability or physical conservation inferred.')
    Path(__file__).with_name('formation_bound_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
