"""No-choice diagnostic packet: three covariant scale-invariant supports."""
from pathlib import Path
import json,hashlib,runpy
import sympy as s
import numpy as np

OUT=Path(__file__).resolve().parent
K=s.diag(-2,-1,1);I=s.eye(3);Pi=s.diag(1,0,0);F=2*Pi;Y=I/4
projectors=[Pi,s.diag(1,1,0),I]
def spectral_supports(k):
    eigs=sorted(k.eigenvects(),key=lambda v:v[0])
    ground=eigs[0][2][0];pg=ground*ground.T/(ground.dot(ground))
    pn=s.zeros(k.rows)
    for val,_,vectors in eigs:
        if val<0:
            for v in vectors:pn+=v*v.T/v.dot(v)
    return [pg,pn,s.eye(k.rows)]
U=s.Matrix([[s.Rational(3,5),-s.Rational(4,5),0],[s.Rational(4,5),s.Rational(3,5),0],[0,0,1]])
assert U.T*U==I and spectral_supports(K)==projectors
assert spectral_supports(U*K*U.T)==[U*p*U.T for p in projectors]
assert spectral_supports(7*K)==projectors
for p in projectors:
    assert p*p==p and p.T==p and p*Pi==Pi
    assert p*K==K*p and p*Y==Y*p
    rc=p+s.Rational(4,5)*(I-p)
    assert rc*Pi==Pi and all(0<x<=1 for x in rc.eigenvals())
    assert len((rc-I).nullspace())==p.rank()
    M=I/s.sqrt(2)
    assert s.simplify(M*(2*rc)*M.T)==rc
baseline=OUT.parent/'baseline/extended_controls.py'
expected='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()==expected
event=runpy.run_path(str(baseline))['event'];arr=lambda x:np.array(x.tolist(),dtype=float)
records=[]
for name,p,want in zip(['ground','negative','full'],projectors,[[-2],[-2,-1],[-2,-1,1]]):
    out,info=event(tuple(arr(x) for x in [K,F,Pi,Y,p]))
    assert out is not None,info
    kn,fn,wn,yn,pn=out;r=p.rank()
    assert len(kn)==r and info['seed']==0
    assert np.allclose(np.linalg.eigvalsh(kn),want,atol=1e-12)
    assert np.allclose(yn,float(s.Rational(32,425))*np.eye(r),atol=1e-12)
    assert abs(np.trace(fn)-2)<1e-12 and abs(np.trace(wn)-1)<1e-12
    records.append(dict(assignment=name,dimension=r,successor_spectrum=want,seed_trace=info['seed'],formation_trace=float(np.trace(fn).real)))
report={'status':'PASS','date':'2026-11-03','exact_covariance_fixture':True,
 'exact_positive_scale_fixture':True,'support_ranks':[1,2,3],
 'common_N_conjugate_product_fixture':True,'implementation_checks':records,
 'enumerated_packet_uniquely_selects_origin_support':False,
 'historical_all_axioms_independence_theorem':False,
 'no_choice_is_smallest_rank_rule':False,
 'new_physical_rule_adopted':False,'new_origin_rule_installed':False,'event_rule_modified':False,
 'baseline_sha256':expected,'scope':'Exact finite relative nonuniqueness and source interpretation; not an inconsistency of the complete event or empirical result'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
