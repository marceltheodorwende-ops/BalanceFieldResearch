"""Direct exact check of the existing proposed L0-NC initial-Y formula.
The proposal is not adopted; no historical derivation is inferred.
"""
from pathlib import Path
import json,importlib.util
import sympy as s
import numpy as np

OUT=Path(__file__).resolve().parent
def zero(M):return s.simplify(M)==s.zeros(*M.shape)
def serial(M):return [[str(v) for v in row] for row in M.tolist()]
def pd(M):return M==M.T and all(s.simplify(M[:k,:k].det())>0 for k in range(1,M.rows+1))

# Existing September proposal's noncommuting two-dimensional example.
I=s.eye(2); K=s.diag(-1,2); Pi=s.diag(1,0)
Q=s.Matrix([[1,s.Rational(1,4)],[s.Rational(1,4),1]])
c=s.diag(0,3); D=s.Matrix([[2,s.Rational(1,4)],[s.Rational(1,4),2]])
assert zero(c+Q-D-K)
H=K+I+2*Pi; Hh=s.diag(s.sqrt(2),s.sqrt(3))
assert H==s.diag(2,3) and pd(H)
A=s.simplify(Hh.inv()*Q*Hh.inv()); Y=s.simplify(A*A)
L=H.inv()*Q; M=H
assert zero(-H*L+Q)
assert zero(Hh*L*M.inv()*L.T*Hh-Y)
assert Y[0,0]==s.Rational(25,96) and Y[1,1]==s.Rational(35,288)
assert Y[0,1]==5/(24*s.sqrt(6))
assert pd(H-Q) and pd(H+Q) and pd(I-Y)
assert not zero(K*Y-Y*K)

variants=[]
for name,Lv,Mv in [('proposed',L,H),('mixed_clause_changed',L/2,H),('metric_clause_changed',L,2*H)]:
    B=-H*Lv; N=Mv+Lv.T*H*Lv
    joint=H.row_join(B).col_join(B.T.row_join(N))
    assert pd(joint)
    load=s.simplify(Hh*Lv*Mv.inv()*Lv.T*Hh)
    reduced=s.simplify(H-B*N.inv()*B.T)
    assert zero(reduced-Hh*(I+load).inv()*Hh)
    assert pd(I-load)
    variants.append(dict(name=name,Y=serial(load),trace_Y=str(s.trace(load)),
        mixed_clause=zero(B+Q),metric_clause=zero(Mv-H),E=serial(reduced)))
assert len({v['trace_Y'] for v in variants})==3

# Whole-carrier selection criterion: A has spectrum inside (-1,1).
# Exact Sylvester checks for source PD data with and without that property.
for q,h in [(s.Rational(1,2),s.Integer(2)),(s.Integer(2),s.Integer(2)),(s.Integer(3),s.Integer(2))]:
    a=q/h; y=a*a
    assert (y<1)==(-h<q<h)
    assert (y<1)==(-1<a<1)

# Direct rank-one persistent-input evaluation; P/W here are supplied test inputs.
e=s.Matrix([1,0]); G=I+Y; C=G.inv(); Bn=Y*C
Pg=e*(e.T*G*e).inv()*e.T*G
lc=s.simplify(s.trace(G*Pg*C*Pi*C*Pg.T))
lb=s.simplify(s.trace(G*Pg*Bn*Pi*Bn*Pg.T))
mu=Y[0,0];alpha=s.simplify(lb/(lc+lb))
assert lc==s.Rational(96,121) and lb==s.Rational(625,11616)
assert alpha==s.Rational(625,9841)
assert lc==1/(1+mu) and lb==mu**2/(1+mu)
gram=s.simplify(alpha*C.T*Pg.T*Pg*C+(1-alpha)*Bn.T*Pg.T*Pg*Bn)
assert gram.det()>0
spec=importlib.util.spec_from_file_location('preserved',OUT.parent/'baseline/extended_controls.py')
baseline=importlib.util.module_from_spec(spec);spec.loader.exec_module(baseline)
num=lambda Z:np.array(Z.evalf(),dtype=float)
nxt,info=baseline.event(tuple(num(Z) for Z in [K,Pi,Pi,Y,Pi]))
assert nxt is not None and info['r']==2
assert np.isclose(info['seed'],1) and np.isclose(info['formation'],2)
assert np.allclose(nxt[0],-np.eye(2),atol=1e-12)
assert np.isclose(np.trace(nxt[3]),float(s.trace(gram)),atol=1e-12)

# Proposal's scalar example: exact boundary Y=1 is excluded by strict selection.
scalar=s.Matrix([[1]])
stopped,reason=baseline.event((np.array([[-1.]]),np.ones((1,1)),np.ones((1,1)),np.ones((1,1)),np.ones((1,1))))
assert stopped is None and reason['terminal']=='selection'
assert (s.Integer(2)/s.Integer(2))**2==1

result=dict(status='PASS',date='2026-11-04',source_status='EXISTING PROPOSAL; NOT ADOPTED',
    explicit_candidate=dict(H=serial(H),neutral_capacity=serial(Q),A=serial(A),Y=serial(Y)),
    independent_clause_controls=variants,whole_carrier_selection_criterion_verified=True,
    rank_one_input=dict(mean_Y=str(mu),Lambda_C=str(lc),Lambda_B=str(lb),alpha=str(alpha),
        exact_Gram_determinant=str(gram.det()),event=info),
    existing_scalar_boundary=dict(Y='1',exact_selection='excluded',implementation_terminal=reason['terminal']),
    original_source_implication_of_mixed_and_metric_clauses_established=False,
    candidate_formula_computation_complete=True,proposal_adopted=False,
    historical_all_axioms_independence_theorem=False,new_physical_rule_adopted=False,event_rule_modified=False)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
