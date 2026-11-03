"""Exact simultaneous-unitary certificates for concrete Hermitian finite states."""
from pathlib import Path
import itertools,json,hashlib,runpy
import sympy as s
import numpy as np

OUT=Path(__file__).resolve().parent
def zero(matrix):return s.simplify(matrix)==s.zeros(*matrix.shape)
def equivalent(A,B):
    assert len(A)==len(B)>0
    n=A[0].rows
    if B[0].shape!=(n,n):return {'equivalent':False,'reason':'different carrier dimension'}
    for M in [*A,*B]:
        assert M.shape==(n,n) and zero(M-M.conjugate().T)
        assert not M.has(s.Float) and all(x.is_algebraic for x in M)
    xs=s.symbols('x0:'+str(n*n));X=s.Matrix(n,n,xs)
    equations=[q for a,b in zip(A,B) for q in (b*X-X*a)]
    linear,_=s.linear_eq_to_matrix(equations,xs)
    basis=[s.Matrix(n,n,v) for v in linear.nullspace()]
    if not basis:return {'equivalent':False,'intertwiner_dimension':0,'determinant_polynomial':'0'}
    zs=s.symbols('z0:'+str(len(basis)))
    combination=sum((z*T for z,T in zip(zs,basis)),s.zeros(n))
    determinant=s.factor(combination.det())
    poly=s.Poly(s.expand(determinant),*zs,extension=True)
    answer={'equivalent':not poly.is_zero,'intertwiner_dimension':len(basis),'determinant_polynomial':str(determinant)}
    if poly.is_zero:return answer
    witness=None
    # The mathematical decision above uses the exact polynomial, not a sample.
    # This bounded search only supplies a convenient explicit certificate.
    for coeff in itertools.islice(itertools.product(range(n+1),repeat=len(basis)),256):
        value=s.simplify(determinant.subs(dict(zip(zs,coeff))))
        if value.is_zero is False:
            witness=s.simplify(combination.subs(dict(zip(zs,coeff))));break
    answer['explicit_witness_found']=witness is not None
    if witness is not None:
        assert all(zero(b*witness-witness*a) for a,b in zip(A,B))
        H=s.simplify(witness.conjugate().T*witness)
        assert all(zero(H*a-a*H) for a in A)
        U=s.simplify(witness*H**(-s.Rational(1,2)))
        assert zero(U.conjugate().T*U-s.eye(n))
        assert all(zero(b-U*a*U.conjugate().T) for a,b in zip(A,B))
        answer['unitary_witness_verified']=True
        answer['unitary_witness']=[[str(q) for q in row] for row in U.tolist()]
    return answer

I=s.eye(2);Pi=s.diag(1,0);K=s.diag(-2,1);F=2*Pi;W=Pi
H=s.Matrix([[1,1],[1,-1]])/s.sqrt(2)
Ya=s.diag(s.Rational(1,4),s.Rational(1,2));Yb=s.simplify(H*Ya*H.T)
A=(K,F,W,Ya,I)
rotated=tuple(s.simplify(H*x*H.T) for x in A)
aligned=equivalent(A,rotated);assert aligned['equivalent'] and aligned['unitary_witness_verified']
B=(K,F,W,Yb,I)
misaligned=equivalent(A,B);assert not misaligned['equivalent']
assert all(x.eigenvals()==y.eigenvals() for x,y in zip(A,B))
assert s.trace(K*Ya)==0 and s.trace(K*Yb)==-s.Rational(3,8)
singular=equivalent(A,(s.diag(-2,3),F,W,Ya,I))
assert singular['intertwiner_dimension']==1 and not singular['equivalent']
assert singular['determinant_polynomial']=='0'
degenerate=(-I,I,I/2,I/4,I)
scalar=equivalent(degenerate,degenerate);assert scalar['equivalent']
# Different stored states can nevertheless have exactly the same scalar successor.
C=(K,F,W,I/4,Pi);D=(K,F,W,Ya,Pi)
discarded=equivalent(C,D);assert not discarded['equivalent']

def exact_alpha(y):
    g=I+y;c=g.inv();b=y*c
    lc=s.trace(g*c*F*c);lb=s.trace(g*b*F*b)
    return s.factor(lb/(lc+lb))
alpha_a=exact_alpha(Ya);alpha_b=exact_alpha(Yb)
assert alpha_a==s.Rational(1,17) and alpha_b==s.Rational(13,101)
eig=[s.Rational(1,4),s.Rational(1,2)]
def gram_values(alpha):return [s.factor((alpha+(1-alpha)*y*y)/(1+y)**2) for y in eig]
gram_a=gram_values(alpha_a);gram_b=gram_values(alpha_b)
assert gram_a==[s.Rational(32,425),s.Rational(20,153)]
assert gram_b==[s.Rational(296,2525),s.Rational(140,909)]
c2=s.factor((alpha_b+(1-alpha_b)*eig[0]*eig[1])**2/((alpha_b+(1-alpha_b)*eig[0]**2)*(alpha_b+(1-alpha_b)*eig[1]**2)))
assert c2==s.Rational(1152,1295)<1
norm_b=s.factor(s.Rational(1,2)+s.Rational(9,2)*c2)
assert norm_b==s.Rational(11663,2590)<5
baseline=OUT.parent/'baseline/extended_controls.py'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()=='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
event=runpy.run_path(str(baseline))['event'];arr=lambda x:np.array(x.tolist(),dtype=complex)
def run(state):
    out,info=event(tuple(arr(x) for x in state));assert out is not None,info
    return out
oa=run(A);ob=run(B)
assert np.allclose(np.linalg.eigvalsh(oa[3]),sorted(map(float,gram_a)),atol=1e-12)
assert np.allclose(np.linalg.eigvalsh(ob[3]),sorted(map(float,gram_b)),atol=1e-12)
assert abs(np.linalg.norm(oa[0],'fro')**2-5)<1e-12
assert abs(np.linalg.norm(ob[0],'fro')**2-float(norm_b))<1e-12
oc=run(C);od=run(D)
assert all(np.allclose(x,y,atol=1e-12,rtol=0) for x,y in zip(oc,od))
assert len(oc[0])==1 and abs(oc[3][0,0]-float(s.Rational(32,425)))<1e-12
report={'status':'PASS','date':'2026-11-03',
 'exact_certificate_domain':'concrete rational/algebraic Hermitian tuples; same carrier dimension',
 'simultaneous_coordinate_change':aligned,
 'same_individual_spectra_different_alignment':misaligned,
 'nonzero_but_singular_intertwiner_space':singular,
 'fully_degenerate_equivalent_case':scalar,
 'mixed_trace_KY':['0','-3/8'],
 'alignment_successors':{'alpha':['1/17','13/101'],'Gram_spectra':[[str(x) for x in gram_a],[str(x) for x in gram_b]],'kernel_Frobenius_squared':['5',str(norm_b)],'binary64_checks':'PASS; exact formulas derived separately'},
 'inequivalent_inputs_with_same_successor':{'input_certificate':discarded,'exact_scalar_successor':'K=-2, rhoF=2, rhoW=1, Y=32/425, P=1','binary64_checks':'PASS'},
 'stored_unitary_class_automatically_equals_full_source_behavioral_quotient':False,
 'source_origin_joint_values_derived':False,'unique_fundamental_initializer_derived':False,
 'new_physical_rule_adopted':False,'event_rule_modified':False,
 'scope':'Exact finite joint-state classification, source-canonical invariants and bounded preserved-helper controls; not a nine-role equivalence, origin derivation or physical validation'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
