"""Exact checks of the existing conditional derivation against program formulas.

No new evolution rule is adopted. This is not proof-assistant verification.
"""
from pathlib import Path
import json,platform,hashlib,runpy
import sympy as s
import numpy as np

OUT=Path(__file__).resolve().parent
U=s.Matrix([[s.Rational(3,5),0],[s.Rational(4,5),0],[0,1]])
V=s.Matrix([[s.Rational(3,5),s.I*s.Rational(4,5)],
            [s.I*s.Rational(4,5),s.Rational(3,5)]])
Sigma=s.diag(s.Rational(1,3),s.Rational(1,2))
A=U*Sigma*V.H
assert U.H*U==s.eye(2) and V.H*V==s.eye(2)
I=s.eye(2);It=s.eye(3)
Gsource=A.H*A
Gtarget=A*A.H
reduced=I-A.H*(It+Gtarget).inv()*A
assert s.simplify(reduced-(I+Gsource).inv())==s.zeros(2)
assert s.simplify(V.H*Gsource*V-Sigma**2)==s.zeros(2)
assert s.simplify(U.H*Gtarget*U-Sigma**2)==s.zeros(2)
assert Gsource.shape==(2,2) and Gtarget.shape==(3,3)

# The previous logical witness violates the same-completion identification.
old=s.Rational(8,45);alternative=old/(1+old)
c_old=1/(1+old);c_alt=1/(1+alternative)
assert alternative==s.Rational(8,53)
assert c_old==s.Rational(45,53) and c_alt==s.Rational(53,61)
assert c_alt-c_old==s.Rational(64,3233)

# Reciprocal weights uniquely solve equal weighted loads plus normalization.
lc,lb=s.symbols('lc lb',positive=True)
alpha=lb/(lc+lb);beta=lc/(lc+lb)
assert s.simplify(alpha+beta-1)==0
assert s.simplify(alpha*lc-beta*lb)==0
a,b=s.symbols('a b')
weights=s.solve([a+b-1,a*lc-b*lb],[a,b])
assert s.simplify(weights[a]-alpha)==0 and s.simplify(weights[b]-beta)==0

# Equal-metric channel contrast is exactly the neutral sign expression.
Y=s.Matrix([[s.Rational(1,2),s.Rational(1,5)],
            [s.Rational(1,5),s.Rational(3,4)]])
C=(I+Y).inv();B=Y*C;G=I+Y
assert s.simplify(C*C-B*B-(C-B))==s.zeros(2)
assert s.simplify(C*G*C-B*G*B-(I-Y))==s.zeros(2)

# The same inherited compression transports the capacity combination exactly.
D=s.diag(2,3,4);cap=s.diag(1,1,1)
neutral=s.Matrix([[1,s.Rational(1,4),0],[s.Rational(1,4),1,0],[0,0,1]])
K=cap+neutral-D
compress=lambda X:U.H*X*U
assert compress(cap)+compress(neutral)-compress(D)==compress(K)

# Quartic formation gives the seed magnitude after choosing the emergent block.
r,lam=s.symbols('r lam',real=True)
assert s.expand(lam*r*r/2+r**4/4-((r*r+lam)**2/4-lam*lam/4))==0
# A simple negative ground mode is needed for unique projector, not just a minimum.
z=s.symbols('z',real=True)
F=lambda x:-x*x/2+x**4/4
perturb=s.expand(F(1+z)-F(1))
assert perturb==z*z+z**3+z**4/4
x=s.symbols('x',nonnegative=True)
normalized_remainder=s.expand(perturb.subs(z,x/2)-x*x/4)
assert normalized_remainder==x**3/8+x**4/64

# Scope witness: the five-tuple does not recover separate capacity roles.
assert 0+1-2==0+2-3==-1

baseline=OUT.parent/'baseline/extended_controls.py'
event=runpy.run_path(str(baseline))['event']
state=(np.array([[-1.]]),np.eye(1),np.eye(1),np.array([[.5]]),np.eye(1))
successor,info=event(state)
assert successor is not None
fixture_error=float(abs(successor[3][0,0]-float(old)))
assert fixture_error<1e-14
assert all(np.allclose(successor[j],state[j],rtol=0,atol=1e-14) for j in [0,1,2,4])
result={'status':'PASS','python':platform.python_version(),'sympy':s.__version__,
 'rectangular_complex_channel':{'shape':[3,2],'source_Gram_shape':[2,2],'target_Gram_shape':[3,3],'active_SVD_Gram_identity':True,'exact_neutral_elimination_identity':True},
 'previous_countermodel':{'published_response':str(c_old),'alternative_response':str(c_alt),'response_difference':str(c_alt-c_old),'satisfies_same_quadratic_completion':False,'refutes_conditional_derivation':False},
 'weight_uniqueness_under_balance_and_normalization':True,
 'equal_metric_selector_identities':True,
 'capacity_combination_commutes_with_common_compression':True,
 'seed_quartic_square_completion':True,
 'normalized_quartic_remainder':str(normalized_remainder),
 'five_tuple_capacity_reconstruction_unique':False,
 'program_reference':{'path':'../baseline/extended_controls.py','sha256':hashlib.sha256(baseline.read_bytes()).hexdigest(),'scalar_fixture_executed_this_followup':True,'scalar_fixture_absolute_load_error':fixture_error,'full_suite_executed_this_followup':False,'note':'One fresh binary64 event fixture matches the exact 8/45 reference; the complete numeric event suite was run in the first milestone, not relabelled as rerun here'},
 'new_physical_rules_adopted':False,'formal_proof_assistant':False}
(OUT/'crosswalk_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
