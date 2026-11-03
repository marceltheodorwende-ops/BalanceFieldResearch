"""Exact finite symmetry diagnostics; no new BFG initialization law."""
from pathlib import Path
import json, importlib.util
import sympy as s
import numpy as np

OUT=Path(__file__).resolve().parent
def zero(M): return s.simplify(M)==s.zeros(*M.shape)
def commutant(matrices):
    n=matrices[0].rows
    xs=s.symbols('x:'+str(n*n)); X=s.Matrix(n,n,xs)
    A,_=s.linear_eq_to_matrix([v for M in matrices for v in X*M-M*X],xs)
    return [s.Matrix(n,n,v) for v in A.nullspace()]
def serial(M): return [[str(x) for x in row] for row in M.tolist()]
def exact_event_gram(Y):
    # All eigenvalues are below one in these fixtures, so selection is identity.
    G=s.eye(2)+Y; C=G.inv(); B=Y*C
    z=s.Matrix([1,0]); Pg=z*(z.T*G*z).inv()*z.T*G
    F=s.diag(2,0)
    lc=s.simplify(s.trace(G*Pg*C*F*C*Pg.T))
    lb=s.simplify(s.trace(G*Pg*B*F*B*Pg.T))
    a=s.simplify(lb/(lc+lb))
    gram=s.simplify(a*C.T*Pg.T*Pg*C+(1-a)*B.T*Pg.T*Pg*B)
    return gram,dict(lc=str(lc),lb=str(lb),alpha=str(a),gram=serial(gram),
                     gram_trace=str(s.trace(gram)),gram_determinant=str(gram.det()))

K=s.diag(-2,1); I=s.eye(2); Q=s.Matrix([[2,1],[1,2]])
c=I; D=c+Q-K; Pi=s.diag(1,0)
assert zero(c+Q-D-K)
assert all(M[0,0]>0 and M.det()>0 for M in [c,Q,D])
ck=commutant([K]); cs=commutant([c,Q,D])
dck=commutant(ck); dcs=commutant(cs)
assert [len(ck),len(dck),len(cs),len(dcs)]==[2,2,1,4]
Y1=Q/s.trace(Q); Y2=Y1**2
assert all(all(0<v<1 for v in Y.eigenvals()) for Y in [Y1,Y2])
assert all(not zero(K*Y-Y*K) for Y in [Y1,Y2])
V=s.Matrix([[1,1],[-1,1]])/s.sqrt(2)
for power in [1,2]:
    assert zero((V*Q*V.T/s.trace(V*Q*V.T))**power-V*(Q/s.trace(Q))**power*V.T)
    assert zero((7*Q/s.trace(7*Q))**power-(Q/s.trace(Q))**power)

# A noncommuting quotient class: phase representatives are jointly equivalent.
phase_checks=[]
for phase in [1,-1,s.I,-s.I]:
    U=s.diag(phase,1); Y=U*Y1*U.conjugate().T
    assert zero(U*K*U.conjugate().T-K)
    assert zero(Y.diagonal()-s.Matrix([[s.Rational(1,2),s.Rational(1,2)]]))
    assert Y.eigenvals()==Y1.eigenvals() and not zero(K*Y-Y*K)
    assert s.trace((K-s.trace(K)*I/2)*(Y-I/2))==0
    phase_checks.append(str(phase))
assert not zero(s.diag(1,-1)*Y1*s.diag(1,-1)-Y1)

spec=importlib.util.spec_from_file_location('preserved_event',OUT.parent/'baseline/extended_controls.py')
baseline=importlib.util.module_from_spec(spec); spec.loader.exec_module(baseline)
records=[]
for name,Y in [('spectral',s.diag(s.Rational(1,4),s.Rational(1,2))),('capacity_linear',Y1),('capacity_square',Y2)]:
    gram,exact=exact_event_gram(Y)
    rank=gram.rank()
    assert rank==(1 if name=='spectral' else 2)
    numeric=lambda M:np.array(M.evalf(),dtype=float)
    state=(numeric(K),numeric(2*Pi),numeric(Pi),numeric(Y),numeric(Pi))
    nxt,info=baseline.event(state)
    assert nxt is not None and info['r']==rank
    assert np.allclose(nxt[0],-2*np.eye(rank),atol=1e-12)
    assert np.isclose(np.trace(nxt[3]),float(s.trace(gram)),atol=1e-12)
    assert np.isclose(info['seed'],0 if rank==1 else 2,atol=1e-12)
    assert np.isclose(info['formation'],2 if rank==1 else 4,atol=1e-12)
    assert np.allclose(nxt[4],np.eye(rank),atol=1e-12)
    records.append(dict(name=name,Y=serial(Y),exact_rank=rank,exact=exact,implementation=info))
assert records[1]['exact']['gram_trace']!=records[2]['exact']['gram_trace']
assert records[0]['exact']['gram_trace']=='32/425'

# Independent exact commuting-sector algebra with two retained directions.
ys=[s.Rational(1,4),s.Rational(1,2)]; a=s.Rational(1,5)
C=s.diag(*[1/(1+y) for y in ys]); B=s.diag(*[y/(1+y) for y in ys])
A=(s.sqrt(a)*C).col_join(s.sqrt(1-a)*B)
assert A.rank()==2 and zero(A.T*s.diag(-2,1,-2,1)*A-K*(A.T*A))
assert zero((A.T*A)*K-K*(A.T*A))
result=dict(status='PASS',commutant_dimensions=dict(K=2,K_double=2,capacities=1,capacities_double=4),
    capacities=dict(c=serial(c),aleph=serial(Q),distinction=serial(D)),
    phase_equivalence_checks=phase_checks,noncommuting_unique_class_fixture=True,
    commuting_sector_compression_identity=True,event_checks=records,
    matrix_covariance_theorem_not_applied_to_quotient_rules=True,
    unique_source_initializer_derived=False,full_historical_independence_theorem=False,
    new_physical_rule_adopted=False,event_rule_modified=False)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
