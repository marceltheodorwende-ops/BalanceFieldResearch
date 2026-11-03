"""Exact initial-support classification and unchanged-event diagnostics."""
from pathlib import Path
import json,runpy,hashlib
import sympy as s
import numpy as np

OUT=Path(__file__).resolve().parent
I=s.eye(2);Pi=s.diag(1,0);K=s.diag(-2,-1);F=2*Pi
Y=s.Matrix([[s.Rational(1,4),s.Rational(1,8)],[s.Rational(1,8),s.Rational(1,4)]])
e=s.Matrix([1,0]);C=(I+Y).inv()
assert e.row_join(Y*e).rank()==2
assert e.row_join((I/4)*e).rank()==1
for p in [Pi,I]:
    q=p-Pi
    assert q*q==q and q*Pi==Pi*q==s.zeros(2)
    r=p+(I-p)*C*(I-p)
    assert r*e==e and len((r-I).nullspace())==p.rank()
    assert all(0<v<=1 for v in r.eigenvals())
# Repeated neutral eigenvalues contribute only their projection of the formed vector.
Y3=s.diag(1,1,2);v=s.Matrix([1,1,1])
cyclic=v.row_join(Y3*v).row_join(Y3**2*v)
assert cyclic.rank()==2
assert s.Matrix.hstack(s.Matrix([1,1,0]),s.Matrix([0,0,1])).rank()==2
# Full-persistence polar trace identity, evaluated independently with rational functions.
G=I+Y;B=Y*C
lc=s.trace(G*C*F*C);lb=s.trace(G*B*F*B)
a=lb/(lc+lb);b=lc/(lc+lb);H=a*C*C+b*B*B
assert s.simplify(s.trace(K*H.inv()*(a*C*C+b*B*B)))==-3
baseline=OUT.parent/'baseline/extended_controls.py'
expected='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()==expected
event=runpy.run_path(str(baseline))['event'];arr=lambda x:np.array(x.tolist(),dtype=float)
records=[]
for name,p,seed,stock,trk in [('least_containing',Pi,2,4,-4),('least_neutral_invariant',I,0,2,-3)]:
    out,info=event(tuple(arr(x) for x in [K,F,Pi,Y,p]))
    assert out is not None,info
    kn,fn,wn,yn,pn=out
    assert len(kn)==2 and abs(info['seed']-seed)<1e-12
    assert abs(np.trace(fn)-stock)<1e-12 and abs(np.trace(kn)-trk)<1e-12
    records.append(dict(initial_support=name,initial_rank=p.rank(),active_dimension=len(kn),seed_trace=info['seed'],formation_trace=float(np.trace(fn).real),kernel_trace=float(np.trace(kn).real)))
report={'status':'PASS','date':'2026-11-03','containing_projectors_classified':True,
 'least_containing_projector':'Pi_0','least_neutral_invariant_support':'span(e,Y e,...,Y^(n-1)e)',
 'example_minimal_ranks':[1,2],'degenerate_neutral_example_cyclic_rank':2,
 'implementation_checks':records,'profile_preservation_and_power_boundedness_force_P':False,
 'origin_support_criterion_derived_from_original_premises':False,
 'new_origin_support_rule_installed':False,'new_physical_rule_adopted':False,'event_rule_modified':False,
 'baseline_sha256':expected,'scope':'Finite analytic classification, exact fixtures and bounded binary64 checks; no full historical independence or physical validation'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
