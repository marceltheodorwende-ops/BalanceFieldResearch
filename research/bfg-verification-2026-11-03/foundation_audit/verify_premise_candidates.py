"""Check whether already specified balance and coordinate conditions fix input coupling.

The witness functions below are not adopted as physical laws or BFG amendments.
"""
from pathlib import Path
import json,platform
import sympy as s

OUT=Path(__file__).resolve().parent
I=s.eye(2);H=s.diag(2,3);R=H/s.trace(H)
# Both are fixed functions of the same source data, with no fitted scalar.
L1=(I+R).inv();L2=L1*L1
Y1=L1*L1;Y2=L2*L2 # M=H, commuting real L, same source and neutral metric.
assert Y1==s.diag(s.Rational(25,49),s.Rational(25,64))
assert Y2==s.diag(s.Rational(625,2401),s.Rational(625,4096))
assert s.trace(Y1)!=s.trace(Y2)
assert all(0<y<1 for y in list(Y1.diagonal())+list(Y2.diagonal()))
rho=s.diag(1,2)
def response_and_weights(Y):
    C=(I+Y).inv();B=Y*C;G=I+Y
    lc=s.trace(G*C*rho*C);lb=s.trace(G*B*rho*B)
    assert lc>0 and lb>0
    a=lb/(lc+lb);b=lc/(lc+lb)
    assert s.simplify(a+b-1)==0 and s.simplify(a*lc-b*lb)==0
    assert C+B==I
    # Gram of the actual declared cross-fed full-persistence analysis.
    S=s.simplify(a*C*C+b*B*B)
    assert all(0<y<1 for y in S.diagonal())
    return {'lc':str(lc),'lb':str(lb),'alpha':str(a),'beta':str(b),'next_Gram_diagonal':[str(y) for y in S.diagonal()]}
records=[response_and_weights(Y1),response_and_weights(Y2)]
# Frame covariance is not a selector between the two functions.
U=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
Hr=U*H*U.T;Rr=Hr/s.trace(Hr)
assert (I+Rr).inv()==U*L1*U.T
assert (I+Rr).inv()**2==U*L2*U.T
# Trace normalization removes a positive source-unit rescaling.
assert (7*H)/s.trace(7*H)==R

result={'status':'PASS','date':'2026-11-03','python':platform.python_version(),'sympy':s.__version__,
 'scope':'Witnesses against selection by source Hessian, shared metric, covariance, source-scale normalization, positive dual loads and reciprocal weighting alone; not all historical BFG premises',
 'witnesses':{'L1':'(I+H/tr(H))^-1','L2':'((I+H/tr(H))^-1)^2','M':'H','fitted_coefficients':0,'both_load_spectra_in_open_unit_interval':True,'different_load_spectra':True,'coordinate_covariance':True,'positive_source_scale_invariance':True},
 'reciprocal_weight_records':records,
 'what_balance_fixes':'The weights conditional on supplied loads; it does not fix which source-neutral interface supplied those loads',
 'original_intrinsic_Gram_update_used_for_both':True,'original_Gram_rule_changed':False,
 'L0_NC_adopted':False,'new_physical_rules_adopted':False,'formal_proof_assistant':False}
(OUT/'premise_candidate_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
