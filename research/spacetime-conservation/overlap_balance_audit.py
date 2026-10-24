"""Normalized overlap effects and antisymmetric full-source kernel currents."""
import json
from pathlib import Path
import itertools
import numpy as np
import sympy as sp
import audit
import pair_audit

def cover(n):
    effects=[]
    for i,j in itertools.combinations(range(n),2):
        p=np.zeros((n,n),complex); p[i,i]=p[j,j]=1; effects.append(p/(n-1))
    return effects

def currents(k,operators,effects):
    flux=np.zeros((len(effects),len(effects)))
    for t in operators:
        comm=t@k-k@t
        for a,ea in enumerate(effects):
            for b,eb in enumerate(effects):flux[a,b]+=np.trace(ea@t@eb@comm).real
    return flux

def symbolic():
    for n in (3,4):
        projectors=[]
        for i,j in itertools.combinations(range(n),2):
            p=sp.zeros(n); p[i,i]=p[j,j]=1; projectors.append(p)
        assert sum(projectors,sp.zeros(n))==(n-1)*sp.eye(n)
    I=sp.eye(2); sx=sp.Matrix([[0,1],[1,0]]); sy=sp.Matrix([[0,-sp.I],[sp.I,0]])
    effects=[(I+sx)/3,(I-sx/2+sp.sqrt(3)*sy/2)/3,(I-sx/2-sp.sqrt(3)*sy/2)/3]
    assert sum(effects,sp.zeros(2))==I and effects[0]*effects[1]!=effects[1]*effects[0]
    ts=[sp.diag(sp.sqrt(sp.Rational(8,13)),sp.sqrt(sp.Rational(32,77))),sp.diag(sp.sqrt(sp.Rational(5,13)),sp.sqrt(sp.Rational(45,77)))]
    assert sum((t*t for t in ts),sp.zeros(2))==I
    k=I+sx; kp=sum((t*k*t for t in ts),sp.zeros(2)); flux=sp.zeros(3)
    for a,ea in enumerate(effects):
        for b,eb in enumerate(effects):flux[a,b]=sp.simplify(sum(sp.re(sp.trace(ea*t*eb*(t*k-k*t))) for t in ts))
    assert sp.simplify(flux+flux.T)==sp.zeros(3)
    delta=sp.Matrix([sp.trace(e*(kp-k)) for e in effects]); assert sp.simplify(delta+flux*sp.ones(3,1))==sp.zeros(3,1)
    return dict(coordinate_cover='sum Pij=(n-1)I; Eij=Pij/(n-1)',common_line_obstruction='sum weights=1 by e1 expectation, but sum weights=3/2 by trace in n=3',outgoing_current='Jab=sum Re tr(Ea T Eb [T,K])',continuity='Delta qa + sum_b Jab =0',noncommuting_effect_check='exact positive normalized trine effects with pinned BFG two-mode channel',exact_noncommuting_delta=[str(sp.simplify(v)) for v in delta])

def source():
    rng=np.random.default_rng(20261128); update=audit.load_update(); calls=0; continuity=0.; anti=0.; partition=0.; total=0.; gauge=0.; maximum=0.; rows=[]
    for n in (3,4):
        effects=cover(n); partition=max(partition,float(np.linalg.norm(sum(effects)-np.eye(n))))
        f=np.diag(np.linspace(1,4,n)); w=np.eye(n)/n
        for case in range(3):
            u=audit.complex_unitary(rng,n); ys=np.linspace(.08,.14,n); y=(u*ys)@u.conj().T
            x=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=x@x.conj().T; k/=np.trace(k)
            model=audit.aligned(k,f,y); operators=[model['tc'],model['tb']]
            out=pair_audit.source_aligned(update,k,f,w,y); calls+=1
            flux=currents(k,operators,effects); q=np.array([np.trace(e@k).real for e in effects]); qn=np.array([np.trace(e@out['k']).real for e in effects])
            continuity=max(continuity,float(np.linalg.norm(qn-q+flux.sum(axis=1)))); anti=max(anti,float(np.linalg.norm(flux+flux.T)))
            total=max(total,abs(q.sum()-np.trace(k).real),abs(qn.sum()-np.trace(out['k']).real),abs((n-1)*q.sum()-(n-1)*np.trace(k).real))
            maximum=max(maximum,float(np.max(np.abs(flux))))
            if case==0:
                g=audit.complex_unitary(rng,n); conj=lambda z:g@z@g.conj().T
                gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y)); calls+=1
                gm=audit.aligned(conj(k),conj(f),conj(y)); ge=[conj(e) for e in effects]
                gf=currents(conj(k),[gm['tc'],gm['tb']],ge)
                gauge=max(gauge,float(np.linalg.norm(gf-flux)),float(np.linalg.norm(gout['k']-conj(out['k']))))
            rows.append(dict(n=n,case=case,sectors=len(effects),total_stock=float(q.sum()),unnormalized_pair_stock=float((n-1)*q.sum()),largest_current=float(np.max(np.abs(flux))),stock_change_norm=float(np.linalg.norm(qn-q))))
    assert calls==8 and max(continuity,anti,partition,total,gauge)<1e-10 and maximum>1e-6
    return dict(calls=calls,continuity_residual=continuity,antisymmetry_residual=anti,partition_residual=partition,total_stock_residual=total,gauge_residual=gauge,largest_current=maximum,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261128,symbolic=symbolic(),source=source(),scope='Normalized overlapping-effect kernel continuity in fixed full persistence. Cover choice and kernel coherences retained; no physical energy-momentum current or spatial law inferred.')
    Path(__file__).with_name('overlap_balance_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
