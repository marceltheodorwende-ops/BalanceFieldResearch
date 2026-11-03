"""Exact logical witnesses; no proposed physical law and no empirical data."""
from fractions import Fraction as F
from pathlib import Path
import json, platform
import sympy as sp

OUT=Path(__file__).resolve().parent
def f(y): return 2*y*y/((1+y)**2*(1+y*y))
def h(y): return y/(1+y)
def neutral(y): return 1/(1+y), y/(1+y)

# Same state, neutral split, density loads and analysis operator.
y=F(1,2);cn,bn=neutral(y);lc=1/(1+y);lb=y*y/(1+y)
alpha=lb/(lc+lb);beta=lc/(lc+lb)
gram=alpha*cn*cn+beta*bn*bn
assert alpha==F(1,5) and beta==F(4,5)
assert gram==f(y)==F(8,45)
alternative=h(gram)
assert alternative==F(8,53) and gram!=alternative
assert 0<alternative<gram<1
count=0
for y in [F(j,101) for j in range(1,101)]:
    a=f(y);b=h(a)
    assert 0<b<a<y<1
    for val in [y,a,b]:
        c,n=neutral(val);assert c+n==1 and 0<c<1 and 0<n<1
    count+=1

# Exact non-diagonal covariance under a rational orthogonal change of frame.
S=sp.Matrix([[sp.Rational(1,5),sp.Rational(1,10)],
             [sp.Rational(1,10),sp.Rational(3,10)]])
U=sp.Matrix([[sp.Rational(3,5),-sp.Rational(4,5)],
             [sp.Rational(4,5),sp.Rational(3,5)]])
I=sp.eye(2)
H=lambda A:A*(I+A).inv()
assert U.T*U==I
assert sp.simplify(H(U*S*U.T)-U*H(S)*U.T)==sp.zeros(2)
assert S.det()>0 and S[0,0]>0 and (I-S).det()>0 and (I-S)[0,0]>0
assert H(S).det()>0 and (I-H(S)).det()>0

# Feedback is a product-rule identity, not a uniquely determining evolution.
t=sp.symbols('t',real=True)
phi1=1+sp.exp(-t)/2;phi2=1+sp.exp(-2*t)/2
assert phi1.subs(t,0)==phi2.subs(t,0)==sp.Rational(3,2)
assert sp.diff(phi1,t).subs(t,0)!=sp.diff(phi2,t).subs(t,0)
for phi in [phi1,phi2]:
    information=sp.Integer(1);ib=sp.diff(phi*information,t)
    assert sp.simplify(ib-information*sp.diff(phi,t)-phi*sp.diff(information,t))==0

# Literal quantitative Level-0 stability claim: strict descent can miss balance.
n=sp.symbols('n',integer=True,nonnegative=True)
phi=2+1/(n+1)
L=(phi-1)**2/2-1 # failures 0, recurrence support 1, all weights 1
delta=sp.factor(L-L.subs(n,n+1))
assert sp.limit(phi,n,sp.oo)==2 and sp.limit(L,n,sp.oo)==-sp.Rational(1,2)
assert sp.factor(delta-(2*n**2+8*n+7)/(2*(n+1)**2*(n+2)**2))==0
assert sp.factor(L+sp.Rational(1,2))==(2*n+3)/(2*(n+1)**2)
for j in range(100):assert delta.subs(n,j)>0 and (L+sp.Rational(1,2)).subs(n,j)>0

# Process measure: exact telescoping and a closed cycle of nonzero changes.
products=[F(1),F(2),F(1)]
increments=[b-a for a,b in zip(products,products[1:])]
assert increments==[F(1),F(-1)] and sum(increments)==products[-1]-products[0]==0

result={'status':'PASS','python':platform.python_version(),'sympy':sp.__version__,
 'scope':'Relative nonuniqueness and source-local counterexamples; not a model of every historical BFG assertion',
 'successor_witness':{'input_load':str(F(1,2)),'original':str(gram),'alternative':str(alternative),'free_fit_parameters':0,'tested_scalar_inputs':count,'exact_orthogonal_covariance':True,'excluded_if_exact_Gram_rule_is_assumed':True},
 'feedback_witness':{'same_initial_phi':'3/2','initial_derivatives':['-1/2','-1'],'full_historical_PDEs_enforced':False},
 'stability_witness':{'strict_descent_formula':str(delta),'lower_bound':'-1/2','limit_phi':'2','limit_deviation_squared':'1','interpretation':'Refutes convergence to balance from the stated numerical inequalities alone; bounded-fluctuation wording needs a quantitative definition'},
 'process_measure':{'increments':[str(v) for v in increments],'total':'0','monotone_clock_from_definition_alone':False},
 'new_physical_rules_adopted':False,'formal_proof_assistant':False}
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
