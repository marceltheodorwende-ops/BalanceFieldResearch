"""Finite count/transition Hilbert representation and exact compatibility tests."""
from pathlib import Path
import json,hashlib
import sympy as s

OUT=Path(__file__).resolve().parent
def transition_matrix(mapping):
    n=len(mapping);T=s.zeros(n)
    for x,y in enumerate(mapping):
        assert 0<=y<n;T[y,x]=1
    return T
def partition_kernel(blocks):
    n=sum(map(len,blocks));K=s.zeros(n);D=s.zeros(n);V=s.zeros(len(blocks),n)
    for a,block in enumerate(blocks):
        for x in block:
            D[x,x]=s.log(len(block));V[a,x]=1
            for y in block:K[x,y]=1
    assert V.T*V==K
    return K,D,V
def congruent(blocks,mapping):
    lookup={x:a for a,b in enumerate(blocks) for x in b}
    return all(len({lookup[mapping[x]] for x in block})==1 for block in blocks)

labels=['a','b','c','d','e'];blocks=[[0,1],[2,3,4]];mapping=[1,0,3,4,2]
K,D,V=partition_kernel(blocks);T=transition_matrix(mapping);n=5
assert T.T*T==s.eye(n) and T.T*D*T==D
assert K.rank()==2 and congruent(blocks,mapping)
Jclass=s.diag(s.log(2),s.log(3))
assert all((V[:,x].T*Jclass*V[:,x])[0]==D[x,x] for x in range(n))
assert s.eye(2)*V==V*T
# Positive operators with the same supplied class-basis values can differ.
off=s.sqrt(s.log(2)*s.log(3))/2
Jalt=Jclass+s.Matrix([[0,off],[off,0]])
assert Jalt.det()==s.Rational(3,4)*s.log(2)*s.log(3)>0
assert all(Jalt[a,a]==Jclass[a,a] for a in range(2))
assert s.simplify(s.trace(Jalt**2)-s.trace(Jclass**2))==s.log(2)*s.log(3)/2
# A feasible W for the fixed class Gram, and exact minimal-carrier reconstruction.
W=V.T*Jclass*V
assert all(W[x,x]==D[x,x] for x in range(n))
assert all(W*v==s.zeros(n,1) for v in K.nullspace())
# Normalize block indicators to form the square-root factors directly.
U=s.zeros(n,2)
for a,block in enumerate(blocks):
    for x in block:U[x,a]=1/s.sqrt(len(block))
assert U.T*U==s.eye(2)
Kh=U*s.diag(s.sqrt(2),s.sqrt(3))*U.T
Kph=U*s.diag(1/s.sqrt(2),1/s.sqrt(3))*U.T
assert s.simplify(Kh*Kh-K)==s.zeros(n)
Jlift=s.simplify(Kph*W*Kph)
assert s.simplify(Kh*Jlift*Kh-W)==s.zeros(n)
# A supplied positive count operator permits a factor only after role identification.
Fop=D.inv()*T*D.inv()
assert s.simplify(D*Fop*D-T)==s.zeros(n)
# A merging transition stays power bounded but need not preserve all quadratic values.
merge=transition_matrix([0,0,1]);_,Dc,_=partition_kernel([[0,1,2]])
assert all((merge.T*Dc*merge)[j,j]==Dc[j,j] for j in range(3))
assert merge.T*Dc*merge!=Dc
assert merge**2==s.Matrix([[1,1,1],[0,0,0],[0,0,0]])
assert merge**3==merge**2
for m in range(7):
    assert s.trace((merge**m).T*(merge**m))==3
# Similarity quotient need not support a well-defined induced transition.
assert not congruent([[0,1],[2,3]],[0,2,2,3])
# Symmetric reflexive similarity is not necessarily a Hilbert Gram.
chain=s.Matrix([[1,1,0],[1,1,1],[0,1,1]])
badvec=s.Matrix([1,-s.sqrt(2),1])
assert chain.det()==-1
assert s.simplify((badvec.T*chain*badvec)[0])==4-4*s.sqrt(2)<0
# A singleton count cannot be identified with both the information coupling and
# an identity transition on the full represented configuration carrier.
_,Dz,_=partition_kernel([[0,1],[2]])
zero=s.Matrix([0,0,1]);assert Dz*zero==s.zeros(3,1)
assert s.eye(3)*zero!=s.zeros(3,1)
assert (zero.T*Dz*zero)[0]==0  # positive binding denominator gives Phi=0
active=[j for j in range(3) if Dz[j,j]>0]
identity_transition=[0,1,2]
assert active==[0,1] and all(identity_transition[j] in active for j in active)
Da=Dz.extract(active,active);Ta=s.eye(3).extract(active,active)
assert s.simplify(Da*(Da.inv()*Ta*Da.inv())*Da-Ta)==s.zeros(2)
baseline=OUT.parent/'baseline/extended_controls.py'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()=='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
report={'status':'PASS','date':'2026-11-03',
 'worked_packet':{'labels':labels,'comparison_classes':[['a','b'],['c','d','e']],
 'transition':dict(zip(labels,[labels[j] for j in mapping])),
 'configuration_dimension':5,'class_dimension':2,
 'count_operator_diagonal':['log(2)','log(2)','log(3)','log(3)','log(3)'],
 'transition_matrix':T.tolist(),'unitary_transition':True,'full_count_quadratic_preserved':True},
 'same_class_information_unique_full_operator':False,
 'positive_fixed_Gram_information_compatibility_fixture':True,
 'merging_transition_power_bound':'sqrt(3)',
 'basis_information_conservation_implies_full_quadratic_conservation':False,
 'similarity_partition_automatically_dynamic_congruence':False,
 'reflexive_symmetric_similarity_automatically_positive_Gram':False,
 'singleton_zero_information_identity_transition_factorable_as_JFJ':False,
 'source_positive_order_excludes_zero_information_basis_under_role_identification':True,
 'invariant_positive_information_sector_factorization_fixture':True,
 'source_origin_configuration_packet_derived':False,'unique_fundamental_initializer_derived':False,
 'new_physical_rule_adopted':False,'event_rule_modified':False,
 'scope':'Exact finite conditional representation builder and compatibility controls; not a unique physical origin or full-source impossibility theorem'}
# Convert SymPy integer matrix entries only; retain exact source formula strings.
report['worked_packet']['transition_matrix']=[[int(x) for x in row] for row in T.tolist()]
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
