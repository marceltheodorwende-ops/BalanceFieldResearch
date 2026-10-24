"""Ordered-gap contraction and failure of formation-free memory control."""
import json
from pathlib import Path
import sympy as sp
import numpy as np
import audit
import pair_audit

def symbolic():
    e=sp.symbols('e',positive=True)
    ys=[2*e**2,4*e**2,e]; weights=[sp.Integer(1),sp.Integer(1),e**6]
    alpha=pair_audit.alpha_exact(ys,weights); beta=1-alpha
    gs=[sp.cancel(pair_audit.g(y,alpha)) for y in ys]
    eta=sp.cancel((ys[1]-ys[0])/(ys[2]-ys[0])); en=sp.cancel((gs[1]-gs[0])/(gs[2]-gs[0]))
    hs=sp.cancel((alpha+beta*ys[0]*ys[1])**2/((alpha+beta*ys[0]**2)*(alpha+beta*ys[1]**2)))
    assert sp.limit(eta,e,0)==0
    assert sp.limit(alpha/e**4,e,0)==10
    assert sp.limit(hs,e,0)==sp.Rational(81,91)
    assert sp.limit(en/eta,e,0)==0
    return dict(alpha=str(alpha),eta=str(eta),eta_next=str(en),h_squared=str(hs),limits=dict(eta='0',alpha_over_e4='10',h_squared='81/91',h='9/sqrt(91)',one_step_loss='1-9/sqrt(91) > 0',eta_next_over_eta='0')), (e,ys,alpha,gs,eta,en,hs)

def source(expressions):
    e,ys,alpha,gs,eta,en,hs=expressions; update=audit.load_update(); rng=np.random.default_rng(20261120)
    k=np.ones((3,3),complex)/3; w=np.eye(3)/3; calls=0; kr=0.; yr=0.; gr=0.; gapres=0.; rows=[]
    for ev in (sp.Rational(1,10),sp.Rational(1,20),sp.Rational(1,40)):
        val=float(ev); load=np.diag([float(y.subs(e,ev)) for y in ys]); f=np.diag([1.,1.,val**6])
        expected_y=np.diag([float(g.subs(e,ev)) for g in gs]); h=float(sp.sqrt(hs.subs(e,ev)))
        out=pair_audit.source_aligned(update,k,f,w,load); calls+=1
        kr=max(kr,float(np.linalg.norm(out['k'][:2,:2]-np.array([[1,h],[h,1]])/3)))
        yr=max(yr,float(np.linalg.norm(out['y']-expected_y)))
        diagonal=np.diag(out['y']).real; observed=(diagonal[1]-diagonal[0])/(diagonal[2]-diagonal[0]); target=float(en.subs(e,ev)); initial=float(eta.subs(e,ev))
        gapres=max(gapres,abs(observed-target)); assert 0<target<initial
        g=audit.complex_unitary(rng,3); conj=lambda z:g@z@g.conj().T
        gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(load)); calls+=1
        gr=max(gr,float(np.linalg.norm(gout['k']-conj(out['k']))),float(np.linalg.norm(gout['y']-conj(out['y']))))
        rows.append(dict(epsilon=val,formation_min_eigenvalue=val**6,initial_eta=initial,next_eta=target,lower_h=h,one_step_loss=1-h,m_equals_2M_squared=True))
    assert calls==6 and max(kr,yr,gr)<1e-10 and gapres<1e-8
    return dict(calls=calls,kernel_residual=kr,load_residual=yr,gauge_residual=gr,gap_residual=gapres,cases=rows)

if __name__=='__main__':
    exact,expressions=symbolic()
    result=dict(status='PASS: geometric contraction; formation-free memory candidate disproved',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261120,symbolic=exact,source=source(expressions),scope='No uniform lower-coherence bound tending to zero with ordered gap ratio alone for arbitrary positive F. Formation-aware or richer geometric bounds remain open.')
    Path(__file__).with_name('spectral_gap_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
