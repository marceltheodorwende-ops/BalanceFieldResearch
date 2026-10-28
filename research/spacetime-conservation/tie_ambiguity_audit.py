"""Retained formation and Witness select different persistent local pairs."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import audit
import pair_audit

def symbolic():
    F=sp.diag(1,2,4); W=sp.Matrix([[1,0,0],[0,4,-1],[0,-1,4]])/9; K=sp.diag(1,2,3)/6
    PF=sp.diag(1,1,0); PW=sp.Matrix([[1,0,0],[0,sp.Rational(1,2),sp.Rational(1,2)],[0,sp.Rational(1,2),sp.Rational(1,2)]])
    assert PF*PF==PF and PW*PW==PW and sp.trace(PF)==sp.trace(PW)==2
    assert F*W-W*F!=sp.zeros(3)
    assert sp.trace((PF-PW)**2)==1
    assert sp.trace(PF*K)==sp.Rational(1,2) and sp.trace(PW*K)==sp.Rational(7,12)
    y,t=sp.symbols('y t',positive=True); alpha=pair_audit.alpha_exact([y]*3,[1,2,4])
    assert sp.cancel(alpha-y*y/(1+y*y))==0
    assert sp.cancel(pair_audit.g(y,alpha)-2*y*y/((1+y)**2*(1+y*y)))==0
    # The first eigenvalue stays below the lower eigenvalue of the 2x2 block.
    assert sp.expand((2+t/3)**2-(1+t*t/81))==3+4*t/3+8*t*t/81
    P=sp.zeros(3); P[0,0]=1
    S=sp.Matrix([[1,t/9],[t/9,-1]])
    B=(sp.eye(2)+S/sp.sqrt(1+t*t/81))/2
    P[1:3,1:3]=B
    assert sp.simplify(P*P-P)==sp.zeros(3)
    assert sp.simplify((F+t*W)*P-P*(F+t*W))==sp.zeros(3)
    assert sp.simplify(sp.trace((P-PF)**2)-(1-1/sp.sqrt(1+t*t/81)))==0
    return dict(formation_witness_commutator_nonzero=True,projector_distance_squared='1',formation_pair_trace='1/2',witness_pair_trace='7/12',trace_difference='1/12',scalar_alpha='y²/(1+y²)',scalar_output_load='2y²/[(1+y)²(1+y²)]',candidate_H='F+tau*W',candidate_projector_distance_squared='1-1/sqrt(1+tau²/81)',scope='selector tau is added mathematical choice, not a source coupling')

def projector(a):
    values,vectors=np.linalg.eigh(a); v=vectors[:,:2]
    return v@v.conj().T

def source():
    update=audit.load_update(); rng=np.random.default_rng(20261125)
    F=np.diag([1.,2.,4.]); W=np.array([[1.,0,0],[0,4.,-1.],[0,-1.,4.]])/9; K=np.diag([1.,2.,3.])/6
    fields=0.; pr=0.; cr=0.; gr=0.; calls=0; rows=[]
    for y in (.05,.1,.2):
        Y=y*np.eye(3); out=pair_audit.source_aligned(update,K,F,W,Y); calls+=1
        expected=2*y*y/((1+y)**2*(1+y*y))*np.eye(3)
        fields=max(fields,float(np.linalg.norm(out['k']-K)),float(np.linalg.norm(out['f']-F)),float(np.linalg.norm(out['w']-W)),float(np.linalg.norm(out['y']-expected)))
        g=audit.complex_unitary(rng,3); conj=lambda z:g@z@g.conj().T
        gout=pair_audit.source_aligned(update,conj(K),conj(F),conj(W),conj(Y)); calls+=1
        for field in ('k','f','w','y'):gr=max(gr,float(np.linalg.norm(gout[field]-conj(out[field]))))
        candidates=[]
        for tau in (0.,1.,9.,90.,None):
            before=projector(W if tau is None else F+tau*W)
            after=projector(out['w'] if tau is None else out['f']+tau*out['w'])
            gauged=projector(gout['w'] if tau is None else gout['f']+tau*gout['w'])
            pr=max(pr,float(np.linalg.norm(after-before))); gr=max(gr,float(np.linalg.norm(gauged-conj(before))))
            cr=max(cr,float(np.linalg.norm(after@out['k']@after-before@K@before)))
            candidates.append(dict(tau=tau,local_trace=float(np.trace(before@K).real),distance_to_formation=float(np.linalg.norm(before-projector(F)))))
        rows.append(dict(input_y=y,candidate_pairs=candidates,original_carrier_rank=3))
    assert calls==6 and max(fields,pr,cr,gr)<1e-10
    return dict(calls=calls,field_residual=fields,projector_residual=pr,compressed_kernel_residual=cr,gauge_residual=gr,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS: competing persistent pair choices explicitly retained',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261125,symbolic=symbolic(),source=source(),scope='Covariance, scalar-load persistence and four local kernel constants do not uniquely select a rank-two observable sector. No impossibility of other source selection criteria claimed.')
    Path(__file__).with_name('tie_ambiguity_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
