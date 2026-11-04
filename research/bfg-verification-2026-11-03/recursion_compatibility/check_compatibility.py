"""Exact comparison of the two original recursion operators and finite rebuild.
No identification of old neutral N with C_N(Y) is adopted as a physical law.
"""
from pathlib import Path
import json,importlib.util
import sympy as s
import numpy as np

OUT=Path(__file__).resolve().parent
def zero(M):return s.simplify(M)==s.zeros(*M.shape)
def serial(M):return [[str(v) for v in row] for row in M.tolist()]
I=s.eye(2); e=s.Matrix([1,1])/s.sqrt(2); P=e*e.T

# Same-vector dual fixed points need not force N e=e when a -1 raw mode exists.
N_phase=s.diag(2,s.Rational(1,2)); S_phase=N_phase**s.Rational(1,2)
R_phase=s.Matrix([[0,1],[1,0]])
RN_phase=S_phase.inv()*R_phase*S_phase.inv(); RC_phase=S_phase*R_phase*S_phase
assert zero(RN_phase*e-e) and zero(RC_phase*e-e)
assert not zero(N_phase*e-e) and zero(RC_phase.T*RC_phase-I)
assert R_phase.eigenvals()=={s.Integer(-1):1,s.Integer(1):1}

# A one-sided neutral comparison can also evade the Hermitian theorem if raw R is nonnormal.
N=s.diag(s.Rational(9,16),s.Rational(16,25)); S=s.diag(s.Rational(3,4),s.Rational(4,5))
u=S.inv()*e; v=S*e
T=u.row_join(v); R=s.simplify(v.row_join(u)*T.inv())
assert zero(R*u-v) and zero(R*v-u) and zero(R**2-I)
assert not zero(R-R.T)
RN=s.simplify(S.inv()*R*S.inv()); RC=s.simplify(S*R*S)
assert zero(RN*e-e) and zero(RC*e-e)
assert set(RC.eigenvals())=={s.Integer(1),-s.Rational(9,25)}
assert set(RN.eigenvals())=={s.Integer(1),-s.Rational(25,9)}
assert zero(R*(u-v)+(u-v))
assert not zero(RC.T*RC-I)
Y=N.inv()-I; G=I+Y; C=N; B=I-N
assert all(0<q<1 for q in Y.eigenvals())
Pg=e*(e.T*G*e).inv()*e.T*G
F=2*P
lc=s.simplify(s.trace(G*Pg*C*F*C*Pg.T))
lb=s.simplify(s.trace(G*Pg*B*F*B*Pg.T))
assert lc>0 and lb>0
alpha=s.simplify(lb/(lc+lb))
gram=s.simplify(alpha*C.T*Pg.T*Pg*C+(1-alpha)*B.T*Pg.T*Pg*B)
assert gram.det()>0 and gram.rank()==2
peripheral=s.simplify((RC+s.Rational(9,25)*I)/(1+s.Rational(9,25)))
assert zero(peripheral**2-peripheral)
assert zero(RC-peripheral+s.Rational(9,25)*(I-peripheral))

# Preserved event confirmation, separated from the raw-recursion representative.
K=I-3*P
spec=importlib.util.spec_from_file_location('baseline',OUT.parent/'baseline/extended_controls.py')
baseline=importlib.util.module_from_spec(spec);spec.loader.exec_module(baseline)
numeric=lambda M:np.array(M.evalf(),dtype=float)
nxt,info=baseline.event(tuple(numeric(M) for M in [K,F,P,Y,P]))
assert nxt is not None and info['r']==2 and np.isclose(info['seed'],2)
assert np.allclose(nxt[0],-2*np.eye(2),atol=1e-12)
assert np.isclose(np.trace(nxt[3]),float(s.trace(gram)),atol=1e-12)

# Exact canonical representative and quantitative older-cost comparison.
can=P+(I-P)*C*(I-P)
assert zero(can-can.T) and all(q>0 for q in can.eigenvals())
R_can=s.simplify(S.inv()*can*S.inv())
RN_can=s.simplify(S.inv()*R_can*S.inv())
assert zero(S*R_can*S-can)
mean=s.simplify((e.T*Y*e)[0]); lower=s.simplify(2*mean+mean**2)
res=s.simplify(RN_can*e-e); residual2=s.simplify((res.T*res)[0])
assert residual2>=lower**2 and residual2>0
assert not zero(R_can-R)

# A commuting positive comparison reaches the residual lower bound exactly.
yc=s.Rational(1,4); Yc=yc*I; Nc=(I+Yc).inv()
Ac=P+(I-P)*Nc*(I-P)
RNc=(I+Yc)*Ac*(I+Yc)
rc=RNc*e-e
assert s.simplify((rc.T*rc)[0])==(2*yc+yc**2)**2
zeroY=s.diag(0,s.Rational(1,2)); ez=s.Matrix([1,0]); Pz=ez*ez.T
Cz=(I+zeroY).inv(); Az=Pz+(I-Pz)*Cz*(I-Pz)
RNz=(I+zeroY)*Az*(I+zeroY)
assert zero(RNz*ez-ez)

result=dict(status='PASS',date='2026-11-04',phase_flip_control=dict(N=serial(N_phase),R=serial(R_phase),
    both_fixed=True,globally_unitary_conjugate=True,neutral_not_fixed=True),
    nonselfadjoint_control=dict(N=serial(N),Y=serial(Y),raw_R=serial(R),normalized_R=serial(RN),conjugate_R=serial(RC),
        raw_involution=True,conjugate_eigenvalues=['1','-9/25'],normalized_eigenvalues=['1','-25/9'],
        both_fixed=True,global_norm_preservation=False,lc=str(lc),lb=str(lb),
        exact_event_Gram_determinant=str(gram.det()),exact_event_rank=2,event=info),
    canonical_comparison=dict(R=serial(R_can),normalized_R=serial(RN_can),mean_load=str(mean),
        exact_residual_squared=str(residual2),lower_residual_squared=str(lower**2),older_zero_cost=False),
    sharp_commuting_bound_verified=True,zero_load_boundary_verified=True,
    source_neutral_identification_adopted=False,raw_selfadjointness_assumed_universally=False,
    full_historical_independence_theorem=False,new_physical_rule_adopted=False,event_rule_modified=False)
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
