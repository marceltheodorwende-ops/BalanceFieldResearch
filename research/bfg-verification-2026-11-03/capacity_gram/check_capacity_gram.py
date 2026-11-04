"""Exact neutral-coordinate Gram criterion and typed master-factor rank controls.
No capacity/field identification or origin axiom is installed.
"""
from pathlib import Path
import json
import sympy as s

OUT=Path(__file__).resolve().parent
def zero(M):return s.simplify(M)==s.zeros(*M.shape)
def serial(M):return [[str(v) for v in row] for row in M.tolist()]
H=s.diag(2,3); Hh=s.diag(s.sqrt(2),s.sqrt(3)); I=s.eye(2)
Q=s.Matrix([[1,s.Rational(1,4)],[s.Rational(1,4),1]])
B=-Q; M=H; Gamma=s.simplify(B*M.inv()*B.T)
target=s.simplify(Q*H.inv()*Q)
assert zero(Gamma-target)
Y=s.simplify(Hh.inv()*Gamma*Hh.inv())
assert zero(Y-(Hh.inv()*Q*Hh.inv())**2)

records=[]
for label,T in [('nonorthogonal',s.Matrix([[2,1],[0,1]])),('orthogonal',s.Matrix([[0,1],[-1,0]]))]:
    Bt=B*T; Mt=T.T*M*T
    changed=s.simplify(Bt*Mt.inv()*Bt.T)
    assert zero(changed-Gamma)
    assert not zero(Bt+Q)
    records.append(dict(name=label,mixed_block=serial(Bt),intrinsic_metric=serial(Mt),
        invariant_Gamma=serial(changed),same_Y=True,
        literal_mixed_clause=zero(Bt+Q),literal_metric_clause=zero(Mt-H)))
assert not records[0]['literal_metric_clause']
Bp=B.row_join(s.zeros(2,1)); Mp=s.diag(M,s.Integer(7))
assert zero(Bp*Mp.inv()*Bp.T-Gamma)
U=s.Matrix([[s.Rational(3,5),-s.Rational(4,5)],[s.Rational(4,5),s.Rational(3,5)]])
Hr=U*H*U.T; Qr=U*Q*U.T
assert zero(Qr*Hr.inv()*Qr-U*target*U.T)

ranks=[]
for q in [s.zeros(2),s.Matrix([[1,1],[1,1]]),Q]:
    g=s.simplify(q*H.inv()*q)
    y=s.simplify(Hh.inv()*g*Hh.inv())
    assert q.rank()==g.rank()==y.rank()
    for column in g.nullspace():assert zero(q*column)
    ranks.append(dict(capacity_rank=q.rank(),Gamma_rank=g.rank(),Y_rank=y.rank()))

# Literal finite composition interpretation of B_C=D_cov c.
c=s.diag(0,3); Dcov=s.Matrix([[1,2],[3,4]])
BC=Dcov*c; W=I; LC=s.Matrix([[2,1],[1,1]])
master=s.simplify(LC.T*BC.T*W*BC*LC)
assert master.rank()<=c.rank()==1 and Y.rank()==2

# A derivative of a PSD field is not composition with its point value.
t=s.symbols('t',real=True)
field=s.Matrix([[t*t,t],[t,3]])
assert field.det()==2*t*t
point=field.subs(t,0); derivative=field.diff(t).subs(t,0)
assert point==c and derivative.rank()==2
assert derivative.T*derivative==I
constant=c
assert zero(field.subs(t,0)-constant) and zero(constant.diff(t))

# Target checking can be performed without separately choosing B and M.
wrong=s.simplify(B*(2*M).inv()*B.T)
assert not zero(wrong-target)
assert zero(wrong-target/2)
result=dict(status='PASS',date='2026-11-04',Gamma_target=serial(target),Y=serial(Y),
    neutral_coordinate_controls=records,uncoupled_neutral_padding_same_response=True,
    source_unitary_covariance=True,rank_controls=ranks,
    literal_composition_control=dict(coherence_rank=1,master_rank=master.rank(),target_rank=Y.rank(),
        same_finite_carrier_identification_possible=False),
    derivative_control=dict(point_rank=point.rank(),derivative_rank=derivative.rank(),
        positive_field_determinant='2*t**2',derivative_Gram=serial(derivative.T*derivative),
        same_point_constant_field_derivative_rank=0),
    target_identity_derived_from_original_sources=False,
    source_Dcov_typing_and_capacity_identification_resolved=False,
    proposed_blocks_adopted=False,new_physical_rule_adopted=False,event_rule_modified=False)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
