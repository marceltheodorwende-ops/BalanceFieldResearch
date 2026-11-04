"""Exact covariance and inverse-Gram feasibility controls using the BFG source grammar.
No inverse-fitted metric or connection is adopted as a BFG origin law.
"""
from pathlib import Path
from itertools import combinations
import json
import sympy as s

OUT=Path(__file__).resolve().parent
def zero(M):return s.simplify(M)==s.zeros(*M.shape)
def serial(M):return [[str(v) for v in row] for row in M.tolist()]
def pd(M):return zero(M-M.H) and all(s.simplify(M[:k,:k].det())>0 for k in range(1,M.rows+1))
def psd(M):
    return zero(M-M.H) and all(s.simplify(M.extract(idx,idx).det())>=0
        for k in range(1,M.rows+1) for idx in combinations(range(M.rows),k))

t,a=s.symbols('t a',real=True)
I=s.eye(2); c=s.Matrix([[t*t,t],[t,3]])
connection=s.Matrix([[0,-a],[a,0]])
U=s.Matrix([[1-t*t,-2*t],[2*t,1-t*t]])/(1+t*t)
assert zero(U.T*U-I)
dc=c.diff(t)+connection*c-c*connection
ct=U*c*U.T
At=s.simplify(U*connection*U.T-U.diff(t)*U.T)
dct=s.simplify(ct.diff(t)+At*ct-ct*At)
assert zero(dct-U*dc*U.T)
assert zero(dc-dc.T) and zero(At+At.T)
at0=s.simplify(dc.subs({t:0,a:0})); atother=s.simplify(dc.subs({t:0,a:s.Rational(1,3)}))
assert at0==s.Matrix([[0,1],[1,0]]) and zero(atother)

H=s.diag(2,3); Hh=s.diag(s.sqrt(2),s.sqrt(3))
Q=s.Matrix([[1,s.Rational(1,4)],[s.Rational(1,4),1]])
Gamma=s.simplify(Q*H.inv()*Q); assert pd(Gamma)

def solve_weight(label,T,G):
    assert psd(G)
    compatible=all(zero(G*v) for v in T.nullspace())
    record=dict(name=label,shape=list(T.shape),operator_rank=T.rank(),target_rank=G.rank(),
        nonnegative_weight_exists=compatible,
        positive_definite_weight_exists=compatible and T.rank()==G.rank())
    if not compatible:return record
    pinv=T.pinv(); W=s.simplify(pinv.H*G*pinv)
    assert psd(W) and zero(T.H*W*T-G)
    complement=s.simplify(s.eye(T.rows)-T*pinv)
    extension=s.simplify(W+complement)
    assert psd(extension) and zero(T.H*extension*T-G)
    if record['positive_definite_weight_exists']:assert pd(extension)
    else:assert extension.det()==0
    record.update(weight=serial(W),extended_weight=serial(extension),pullback_verified=True)
    return record

T=at0*Hh
records=[solve_weight('square_covariant_jet',T,Gamma),
         solve_weight('rectangular_full_rank',s.Matrix([[1,0],[0,1],[1,1]]),Gamma),
         solve_weight('complex_rectangular_full_rank',s.Matrix([[1,s.I],[0,1],[1,0]]),Gamma),
         solve_weight('rank_one_matching_kernel',s.diag(1,0),s.diag(1,0)),
         solve_weight('rank_one_wrong_kernel',s.diag(1,0),I),
         solve_weight('zero_target_nonzero_map',s.diag(1,0),s.zeros(2))]
assert [r['nonnegative_weight_exists'] for r in records]==[True,True,True,True,False,True]
assert [r['positive_definite_weight_exists'] for r in records]==[True,True,True,True,False,False]
W=s.Matrix(records[0]['weight'])
Y=s.simplify(Hh.inv()*T.T*W*T*Hh.inv())
assert zero(Y-(Hh.inv()*Q*Hh.inv())**2)
assert not zero(T.T*T-Gamma)
assert zero(Hh.inv()*T.T*T*Hh.inv()-I)

# The complete pullback equation transforms covariantly when every object is changed.
U0=U.subs(t,s.Rational(1,2)); Qr=U0*Q*U0.T; Hr=U0*H*U0.T
Tr=U0*T*U0.T; Wr=U0*W*U0.T
assert zero(Tr.T*Wr*Tr-Qr*Hr.inv()*Qr)

# Arbitrary nonorthonormal coordinate frames require their transformed inner products.
Sframe=s.Matrix([[2,1],[0,1]]); Rframe=s.Matrix([[1,1],[0,3]])
hV=Sframe.H*Sframe; hK=Rframe.H*Rframe
Tf=s.simplify(Rframe.inv()*T*Sframe)
Wf=s.simplify(Rframe.inv()*W*Rframe)
Hf=Sframe.inv()*H*Sframe; Qf=Sframe.inv()*Q*Sframe
adjoint=s.simplify(hV.inv()*Tf.H*hK)
assert zero(adjoint*Wf*Tf-Qf*Hf.inv()*Qf)
assert zero(Hf.H*hV-hV*Hf) and zero(Qf.H*hV-hV*Qf)
assert zero(Wf.H*hK-hK*Wf)
assert not zero(Tf.H*Wf*Tf-Qf*Hf.inv()*Qf)

# Completion audit: positive weights and covariance alone still allow distinct Y.
half_weight=W/2; half_Y=s.simplify(Hh.inv()*T.H*half_weight*T*Hh.inv())
assert pd(W) and pd(half_weight)
assert zero(half_Y-Y/2) and not zero(half_Y-Y)
assert pd(I-Y) and pd(I-half_Y)

result=dict(status='PASS',date='2026-11-04',endomorphism_covariant_derivative_verified=True,
    gauge_pullback_identity_verified=True,
    nonorthonormal_frame_identity_verified=True,unchanged_adjoint_in_wrong_frame_rejected=True,
    connection_control=dict(same_capacity_field=True,rank_at_connection_zero=at0.rank(),
        rank_at_connection_one_third=atother.rank(),connection_change_alone_is_not_a_gauge_change=True),
    inverse_Gram_cases=records,candidate_Y=serial(Y),
    unit_weight_response='I; different from the candidate',
    completion_audit=dict(coordinate_equation_subtask_complete=True,original_Y_derivation_complete=False,
        same_map_two_positive_weights=True,both_responses_strictly_selected=True,
        candidate_trace=str(s.trace(Y)),comparison_trace=str(s.trace(half_Y)),
        scope='Relative to the typed positive-Gram and covariance packet; not every historical source premise.'),
    metric_completion_is_source_derivation=False,
    full_initial_Y_derived_from_original_assumptions=False,
    reference_runtime_modified=False,new_physical_rule_adopted=False,event_rule_modified=False)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
