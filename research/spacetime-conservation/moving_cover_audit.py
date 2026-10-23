"""Moving effects: separate source kernel current and cover reassignment."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import audit
import pair_audit
from overlap_balance_audit import cover,currents

def eigencover(k):
    values,u=np.linalg.eigh(k); assert np.min(np.diff(values))>1e-8
    return [u@e@u.conj().T for e in cover(len(k))],float(np.min(np.diff(values)))

def balance(k,kp,operators,old,new):
    trace=lambda e,x:float(np.trace(e@x).real)
    delta=np.array([trace(b,kp)-trace(a,k) for a,b in zip(old,new)])
    after=np.array([trace(b-a,kp) for a,b in zip(old,new)])
    before=np.array([trace(b-a,k) for a,b in zip(old,new)])
    cross=np.array([trace(b-a,kp-k) for a,b in zip(old,new)])
    jo=currents(k,operators,old); jn=currents(k,operators,new)
    residual=max(float(np.linalg.norm(delta+jo.sum(axis=1)-after)),float(np.linalg.norm(delta+jn.sum(axis=1)-before)),float(np.linalg.norm(after-before-cross)),abs(after.sum()),abs(before.sum()))
    return dict(residual=residual,delta=delta,after=after,before=before,cross=cross,old_current=jo,new_current=jn)

def symbolic():
    K=sp.diag(sp.Rational(1,5),sp.Rational(3,10),sp.Rational(1,2)); c=sp.sqrt(2)/2; R=sp.Matrix([[c,-c,0],[c,c,0],[0,0,1]])
    ps=[sp.diag(1,1,0)/2,sp.diag(1,0,1)/2,sp.diag(0,1,1)/2]
    shifts=[sp.simplify(sp.trace((R*p*R.T-p)*K)) for p in ps]
    assert shifts==[0,sp.Rational(1,40),-sp.Rational(1,40)]
    assert sum((R*p*R.T for p in ps),sp.zeros(3))==sp.eye(3)
    return dict(moving_continuity='Delta qa+sum_b Jab(E,K)=tr[(Enew-Eold)Kplus]',reassignment_total='0 for normalized old/new covers',ordering_cross_term='R_after-R_before=tr[(Enew-Eold)(Kplus-K)]',pure_reassignment=[str(v) for v in shifts],pure_source_kernel_change='0')

def source():
    rng=np.random.default_rng(20261129); update=audit.load_update(); calls=0; residual=0.; gauge=0.; rows=[]
    for n in (3,4):
        f=np.diag(np.linspace(1.,4.,n)); w=np.eye(n)/n
        for case in range(3):
            u=audit.complex_unitary(rng,n); y=(u*np.linspace(.08,.14,n))@u.conj().T
            x=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=x@x.conj().T; k/=np.trace(k)
            out=pair_audit.source_aligned(update,k,f,w,y); calls+=1; model=audit.aligned(k,f,y); operators=[model['tc'],model['tb']]
            old,gapold=eigencover(k); new,gapnew=eigencover(out['k']); b=balance(k,out['k'],operators,old,new); residual=max(residual,b['residual'])
            if case==0:
                g=audit.complex_unitary(rng,n); conj=lambda z:g@z@g.conj().T
                gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1; gm=audit.aligned(conj(k),conj(f),conj(y))
                go,_=eigencover(conj(k)); gn,_=eigencover(gout['k']); gb=balance(conj(k),gout['k'],[gm['tc'],gm['tb']],go,gn)
                gauge=max(gauge,gb['residual'],float(np.linalg.norm(gb['after']-b['after'])),float(np.linalg.norm(gb['old_current']-b['old_current'])),float(np.linalg.norm(gout['k']-conj(out['k']))))
            rows.append(dict(n=n,case=case,input_kernel_gap=gapold,output_kernel_gap=gapnew,stock_change_norm=float(np.linalg.norm(b['delta'])),reassignment_after_norm=float(np.linalg.norm(b['after'])),cross_term_norm=float(np.linalg.norm(b['cross']))))
    k=np.diag([.2,.3,.5]); f=np.diag([1.,2.,4.]); w=np.eye(3)/3; y=.1*np.eye(3)
    out=pair_audit.source_aligned(update,k,f,w,y); calls+=1; model=audit.aligned(k,f,y)
    c=np.sqrt(.5); R=np.array([[c,-c,0],[c,c,0],[0,0,1]]); old=cover(3); new=[R@e@R.T for e in old]
    b=balance(k,out['k'],[model['tc'],model['tb']],old,new); target=np.array([0.,1/40,-1/40])
    witness=max(b['residual'],float(np.linalg.norm(out['k']-k)),float(np.linalg.norm(b['after']-target)),float(np.linalg.norm(b['old_current'])))
    assert calls==9 and max(residual,gauge,witness)<1e-10
    return dict(calls=calls,moving_balance_residual=residual,gauge_residual=gauge,pure_reassignment_residual=witness,pure_reassignment_observed=b['after'].tolist(),pure_dynamical_current_norm=float(np.linalg.norm(b['old_current'])),cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261129,symbolic=symbolic(),source=source(),scope='Fixed ambient dimension, matched moving-effect labels. Reassignment separated from source current; no physical cover ordering, rank-event law, or spacetime transport selected.')
    Path(__file__).with_name('moving_cover_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
