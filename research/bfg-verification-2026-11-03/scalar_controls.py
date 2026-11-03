"""Exact arithmetic and symbolic certificates, not a proof-assistant check."""
from fractions import Fraction as Q
from pathlib import Path
import json,platform
import sympy as s
OUT=Path(__file__).resolve().parent
y=s.symbols('y',real=True)
d=(1+y)**2*(1+y*y)
f=2*y*y/d
# Universal polynomial identities; signs are justified in SCALAR_PROOF.md.
certificates={
 'strict_decay':s.expand(d-2*y-((1+y*y)**2+2*y**3)),
 'quarter_bound':s.expand(d-8*y*y-(1-y)**2*(y*y+4*y+1)),
 'quadratic_bound':s.expand(d-1-(2*y+2*y*y+2*y**3+y**4)),
 'derivative':s.factor(s.diff(f,y)-4*y*(1-y**3)/((1+y)**3*(1+y*y)**2)),
 'lipschitz_majorant':s.expand(16*(1+y)**3-108*y-4*(2*y-1)**2*(y+4)),
}
assert all(v==0 for v in certificates.values()),certificates
def step(x):return 2*x*x/((1+x)**2*(1+x*x))
cases=0;steps=0
for start in [Q(i,101) for i in range(1,101)]+[Q(1,10**12),1-Q(1,10**12)]:
    x=start
    for k in range(1,9):
        nxt=step(x)
        assert 0<nxt<x and nxt<Q(1,4)
        assert nxt<=2*x*x
        assert nxt<Q(1,2**(1+2**(k-1)))
        x=nxt;steps+=1
    cases+=1
# Necessary assumptions and finite-precision failure, not theorem refutations.
assert step(Q(0))==0
singular_denominator=((1+Q(-1))**2*(1+Q(-1)**2))==0
assert singular_denominator
assert step(Q(1))==Q(1,4)
assert 2.0*(1e-200)**2/((1+1e-200)**2*(1+(1e-200)**2))==0.0
assert step(Q(1,10**200))>0
result={'status':'PASS','python':platform.python_version(),'sympy':s.__version__,'symbolic_zero_identities':{k:str(v) for k,v in certificates.items()},'exact_initial_values':cases,'exact_steps':steps,'boundary_controls':{'zero_is_fixed':True,'minus_one_is_undefined':True,'one_maps_to_quarter':True,'binary64_false_zero_at_1e_minus_200':True},'scope':'Exact symbolic/rational controls plus an analytic proof; not Lean or another proof-assistant certificate'}
(OUT/'scalar_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
