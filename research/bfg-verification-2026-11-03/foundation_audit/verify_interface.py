"""Exact checks of quadratic-interface freedom and coordinate invariance.

The alternative completions are logical witnesses, not adopted BFG laws.
"""
from pathlib import Path
import json,platform
import sympy as s

OUT=Path(__file__).resolve().parent
H=s.diag(2,3);Hs=s.diag(s.sqrt(2),s.sqrt(3));I=s.eye(2)
def blocks(L,M):
    B=-H*L
    N=M+L.H*H*L
    J=H.row_join(B).col_join(B.H.row_join(N))
    return B,N,J
def load(L,M): return s.simplify(Hs*L*M.inv()*L.H*Hs)
def positive_definite(A):
    assert A==A.H
    return all(s.simplify(A[:j,:j].det())>0 for j in range(1,A.rows+1))

records=[]
for L,M in [(I/2,H),(I/3,H),
            (s.Matrix([[s.Rational(1,2),s.Rational(1,4)],[0,s.Rational(1,3)]]),s.Matrix([[3,1],[1,2]]))]:
    B,N,J=blocks(L,M)
    assert positive_definite(H) and positive_definite(M) and positive_definite(J)
    recovered_L=-H.inv()*B
    recovered_M=s.simplify(N-B.H*H.inv()*B)
    assert recovered_L==L and recovered_M==M
    Y=load(L,M)
    reduced=s.simplify(H-B*N.inv()*B.H)
    whitened=s.simplify(Hs.inv()*reduced*Hs.inv())
    assert s.simplify(whitened-(I+Y).inv())==s.zeros(2)
    # A nonorthogonal neutral-coordinate reparametrization is a true gauge change.
    T=s.Matrix([[1,1],[0,2]])
    Lt=L*T;Mt=T.H*M*T
    assert s.simplify(load(Lt,Mt)-Y)==s.zeros(2)
    change=s.diag(1,1,1,1);change[2:,2:]=T
    assert s.simplify(blocks(Lt,Mt)[2]-change.H*J*change)==s.zeros(4)
    records.append({'trace_Y':str(s.trace(Y)),'det_Y':str(Y.det()),'joint_positive_definite':True,'coordinate_invariance':True})

Y1=load(I/2,H);Y2=load(I/3,H)
assert Y1==I/4 and Y2==I/9
assert (I+Y1).inv()==4*I/5 and (I+Y2).inv()==9*I/10
assert s.trace(Y1)!=s.trace(Y2)
Tscale=2*I/3
assert (I/2)*Tscale==I/3
assert Tscale.H*H*Tscale==4*H/9
assert load((I/2)*Tscale,Tscale.H*H*Tscale)==Y1

# Mixed-Hessian and intrinsic-metric clauses fix independent information.
neutral_capacity=s.Matrix([[1,s.Rational(1,4)],[s.Rational(1,4),1]])
formation_capacity=s.diag(0,3)
expansion_capacity=s.Matrix([[2,s.Rational(1,4)],[s.Rational(1,4),2]])
K=formation_capacity+neutral_capacity-expansion_capacity
assert K==s.diag(-1,2)
e0=s.Matrix([1,0]);lam0=-1
assert K-lam0*I-2*lam0*(e0*e0.H)==H
assert positive_definite(neutral_capacity) and positive_definite(expansion_capacity)
Lnc=H.inv()*neutral_capacity
Bnc,Nnc,Jnc=blocks(Lnc,H)
assert Bnc==-neutral_capacity and positive_definite(Jnc)
assert s.simplify(load(Lnc,H)-(Hs.inv()*neutral_capacity*Hs.inv())**2)==s.zeros(2)
_,_,different_metric_joint=blocks(Lnc,2*H)
assert positive_definite(different_metric_joint)
assert s.simplify(load(Lnc,2*H)-load(Lnc,H)/2)==s.zeros(2)

result={'status':'PASS','date':'2026-11-03','python':platform.python_version(),'sympy':s.__version__,
 'scope':'All strictly positive finite quadratic completions of a fixed positive source Hessian; not all nonlinear or historical BFG models',
 'classification_fixture_cases':records,
 'source_formation_example_H_reproduced':True,
 'same_source_and_intrinsic_neutral_metric':{'H':'diag(2,3)','M':'diag(2,3)','L1':'I/2','L2':'I/3','Y1':'I/4','Y2':'I/9','retained_response1':'4I/5','retained_response2':'9I/10','not_coordinate_equivalent_as_metric_channel_pairs':True,'rescaling_L1_to_L2_requires_changing_M_to_4H_over_9':True},
 'proposed_L0_NC':{'mixed_Hessian_fixes_L':True,'intrinsic_metric_is_separate_clause':True,'adopted_by_this_audit':False},
 'general_proof':'INTERFACE_IDENTIFICATION.md','formal_proof_assistant':False,'new_physical_rule_adopted':False}
(OUT/'interface_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
