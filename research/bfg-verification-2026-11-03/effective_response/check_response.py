"""Exact response identification in the previously specified quadratic class.
No source-to-channel rule is installed by these comparison fixtures.
"""
from pathlib import Path
import hashlib,json
import sympy as s

OUT=Path(__file__).resolve().parent
def zero(X): return s.simplify(X)==s.zeros(*X.shape)
def serial(X): return [[str(v) for v in row] for row in X.tolist()]
def response(H,L,M):
    Hh=H**s.Rational(1,2)
    Y=s.simplify(Hh*L*M.inv()*L.conjugate().T*Hh)
    B=-H*L; N=M+L.conjugate().T*H*L
    E=s.simplify(H-B*N.inv()*B.conjugate().T)
    assert zero(E-Hh*(s.eye(H.rows)+Y).inv()*Hh)
    assert zero(Hh*E.inv()*Hh-s.eye(H.rows)-Y)
    assert (H-E).rank()==Y.rank()
    # Congruence factorization establishes strict joint positivity for H,M>0.
    F=s.eye(H.rows).row_join(-L).col_join(s.zeros(M.rows,H.rows).row_join(s.eye(M.rows)))
    J=H.row_join(B).col_join(B.conjugate().T.row_join(N))
    assert zero(J-F.conjugate().T*s.diag(H,M)*F)
    return Y,E,J

H=s.diag(4,3); Hh=s.diag(2,s.sqrt(3)); I=s.eye(2)
Q=s.Matrix([[2,1],[1,2]]); capacities=[I,Q,I+Q-s.diag(-2,1)]
K=capacities[0]+capacities[1]-capacities[2]
assert zero(H-(K+2*I+4*s.diag(1,0)))
fixtures=[]
for label,Y in [('capacity_linear',Q/4),('capacity_square',(Q/4)**2),
                ('rank_one',s.Matrix([[s.Rational(1,4),s.Rational(1,4)],[s.Rational(1,4),s.Rational(1,4)]])),
                ('complex_rank_one',s.Matrix([[s.Rational(1,4),s.I/8],[-s.I/8,s.Rational(1,16)]])),
                ('zero',s.zeros(2))]:
    if Y.rank()==2:
        T=Y.cholesky(); A=T.T
    elif Y.rank()==1:
        A=Y[0,:]/s.sqrt(Y[0,0])
    else:
        # The theoretical minimal neutral dimension is zero; this is a padded realization.
        A=s.zeros(1,2)
    m=A.rows; L=Hh.inv()*A.conjugate().T; M=s.eye(m)
    got,E,J=response(H,L,M)
    assert zero(got-Y)
    assert all(v>0 for v in E.eigenvals())
    assert all(v>=0 for v in (H-E).eigenvals())
    # Nonorthogonal neutral coordinates preserve the same response.
    Tn=s.Matrix([[2,1],[0,1]]) if m==2 else s.Matrix([[2]])
    changed,Ec,_=response(H,L*Tn,Tn.T*M*Tn)
    assert zero(changed-Y) and zero(Ec-E)
    # Extra uncoupled positive neutral degrees leave the effective response unchanged.
    padded,Ep,_=response(H,L.row_join(s.zeros(2,1)),s.diag(M,s.Integer(7)))
    assert zero(padded-Y) and zero(Ep-E)
    if m==2:
        U=s.Matrix([[0,-1],[1,0]])
        B=U*A
        assert zero(B.T*B-A.T*A)
        # For invertible minimal factors, their relative map is the exact unitary witness.
        witness=B*A.inv()
        assert zero(witness.T*witness-I) and zero(witness*A-B)
    fixtures.append(dict(name=label,Y=serial(Y),E=serial(E),
        effective_rank=Y.rank(),minimal_neutral_dimension=Y.rank(),realization_dimension=m,
        coordinate_invariance=True,uncoupled_padding_invisible=True))
assert fixtures[0]['E']!=fixtures[1]['E']

# A single fresh-ground probe cannot determine the whole response.
Ea=s.diag(2,1); Eb=s.diag(2,2)
Ya=s.simplify(Hh*Ea.inv()*Hh-I); Yb=s.simplify(Hh*Eb.inv()*Hh-I)
e=s.Matrix([1,0])
assert (e.T*Ea*e)[0]==(e.T*Eb*e)[0] and not zero(Ya-Yb)
assert all(v>=0 for Y in [Ya,Yb] for v in Y.eigenvals())

# The generic nested positive Gram admits every PSD load when its factors are free.
weighted=[]
for record in fixtures[:2]:
    Y=s.Matrix(record['Y']); LC=Y.cholesky().T; BC=I; W=I
    assert zero(LC.T*BC.T*W*BC*LC-Y)
    weighted.append(True)
result=dict(status='PASS',quadratic_fixtures=fixtures,
    exact_response_inverse=True,minimal_factor_equivalence_fixtures=2,
    fixed_capacity_two_effective_responses=True,single_ground_probe_insufficient=True,
    single_ground_probe=dict(E_a=serial(Ea),E_b=serial(Eb),Y_a=serial(Ya),Y_b=serial(Yb)),
    nested_Gram_realization_checks=len(weighted),
    physical_channel_uniqueness_required_for_finite_event=False,
    source_capacity_to_effective_response_derived=False,
    full_historical_independence_theorem=False,new_physical_rule_adopted=False,event_rule_modified=False)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
