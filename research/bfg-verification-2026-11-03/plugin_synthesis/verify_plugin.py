"""Exact source-bridge, information-identifiability and history-metric checks."""
from pathlib import Path
from fractions import Fraction as Q
from math import lcm
import itertools,json,hashlib
import sympy as s

OUT=Path(__file__).resolve().parent
src=json.loads((OUT/'SOURCES.json').read_text(encoding='utf-8'))
assert len(src['references'])==20 and sum(x['parts'] for x in src['references'])==1728
assert all(len(x['sha256'])==len(x['extraction_sha256'])==64 for x in src['references'])
# Source field equations, without presuming a particular PDE solution.
phi,inf,beta,delta,i0,fp,fi,ib=s.symbols('phi inf beta delta i0 fp fi ib',real=True)
gp=beta*phi*(1-phi)/i0
AA=inf*fp+phi*fi;BB=inf*gp+phi*delta
assert s.simplify(ib-(inf*(fp+gp*ib)+phi*(fi+delta*ib))-((1-BB)*ib-AA))==0
values={phi:s.Rational(1,2),inf:2,beta:s.Rational(1,2),delta:s.Rational(1,4),i0:1,fp:s.Rational(1,3),fi:-s.Rational(1,5)}
assert s.simplify((AA/(1-BB)).subs(values))==s.Rational(68,75)
# Complex Hermitian information reconstruction from normalized profile functionals.
I=s.eye(2);J=s.Matrix([[2,1+s.I],[1-s.I,3]])
e1=s.Matrix([1,0]);e2=s.Matrix([0,1])
probes=[e1,e2,(e1+e2)/s.sqrt(2),(e1+s.I*e2)/s.sqrt(2)]
q=lambda j,v:s.simplify((v.conjugate().T*j*v)[0])
v=[q(J,p) for p in probes]
assert v==[2,3,s.Rational(7,2),s.Rational(3,2)]
real=v[2]-(v[0]+v[1])/2;imag=(v[0]+v[1])/2-v[3]
reconstructed=s.Matrix([[v[0],real+s.I*imag],[real-s.I*imag,v[1]]])
assert reconstructed==J and J.det()>0 and J.trace()>0
basis=[s.diag(1,0),s.diag(0,1),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,s.I],[-s.I,0]])]
measurement=s.Matrix([[q(b,p) for b in basis] for p in probes])
assert measurement.rank()==4 and measurement[:1,:].rank()==1
J2=J+s.diag(0,s.Rational(1,2))
assert q(J2,e1)==q(J,e1) and J2!=J and J2.det()>0
# Integrated foundational existence-domain packet on a fixed monitored profile.
core=[]
for decay in [s.Rational(1,2),s.Rational(3,4),s.Integer(1)]:
    R=s.diag(1,decay);N=I;E=I;Bop=I;Jcore=I
    Phi=q(E*Jcore,e1)/q(Bop*N,e1);information=q(Jcore,e1)
    residual=R*e1-e1
    assert Phi==information==1 and residual==s.zeros(2,1)
    assert max(R.eigenvals())==1 and all(0<x<=1 for x in R.eigenvals())
    assert s.trace(residual.T*residual)==0
    assert AA.subs({phi:1,inf:1,fp:0,fi:0})==0
    assert BB.subs({phi:1,inf:1,delta:s.Rational(1,2)})==s.Rational(1,2)
    core.append({'transverse_eigenvalue':str(decay),'peripheral_rank':len((R-I).nullspace()),'Lyapunov_cost':'0','affine_feedback':'A=0, B=1/2, IB=0','interface_drift':'0'})
# Exact eventually periodic histories: finite prefix, infinite repeating tail.
histories=[((),(Q(1),)),((Q(5,4),),(Q(1),)),((),(Q(5,4),)),
           ((),(Q(1),Q(5,4))),((Q(9,8),),(Q(1),Q(5,4))),
           ((Q(5,4),Q(1)),(Q(5,4),)),((Q(1),),(Q(1),))]
def value(h,n):
    prefix,tail=h
    return prefix[n] if n<len(prefix) else tail[(n-len(prefix))%len(tail)]
def f(x):return x/(1+x)
def distances(a,b):
    start=max(len(a[0]),len(b[0]));period=lcm(len(a[1]),len(b[1]))
    head=sum((Q(1,2)**n*f(abs(value(a,n)-value(b,n))) for n in range(start)),Q(0))
    cycle=sum((Q(1,2)**n*f(abs(value(a,n)-value(b,n))) for n in range(start,start+period)),Q(0))
    discount=head+cycle/(1-Q(1,2)**period)
    asymptotic=max(f(abs(value(a,n)-value(b,n))) for n in range(start,start+period))
    return discount,asymptotic
def shift(h):
    prefix,tail=h
    return (prefix[1:],tail) if prefix else ((),tail[1:]+tail[:1])
discount,tail=distances(histories[0],histories[1])
assert discount==Q(1,5) and tail==0
assert distances(histories[0],histories[0])==(0,0)
for a,b in itertools.product(histories,repeat=2):
    D,T=distances(a,b);Ds,Ts=distances(shift(a),shift(b))
    assert 0<=D<=2 and 0<=T<=1
    assert Ds==2*(D-f(abs(value(a,0)-value(b,0)))) and Ds<=2*D
    assert Ts==T and distances(b,a)==(D,T)
for a,b,c in itertools.product(histories,repeat=3):
    ab=distances(a,b);ac=distances(a,c);cb=distances(c,b)
    assert all(ab[i]<=ac[i]+cb[i] for i in range(2))
    if distances(a,c)[1]==0:
        assert distances(a,b)[1]==distances(c,b)[1]
x,y=s.symbols('x y',nonnegative=True)
assert s.factor(x/(1+x)+y/(1+y)-(x+y)/(1+x+y))==x*y*(x+y+2)/((x+1)*(y+1)*(x+y+1))
baseline=OUT.parent/'baseline/extended_controls.py'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()=='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
report={'status':'PASS','date':'2026-11-03',
 'plugin_reference_inventory':20,'indexed_parts':1728,'full_proof_audit_of_all_parts':False,
 'field_derived_feedback_identity':True,'exact_scalar_feedback_fixture':'68/75',
 'information_functional_complete_probe_rank':4,'single_profile_probe_rank':1,
 'information_operator_reconstruction':'exact complex Hermitian 2x2',
 'full_foundational_admissibility_family':core,
 'all_plugin_domain_specific_dynamics_solved_by_family':False,
 'printed_asymptotic_quotient_discount_distance_well_defined':False,
 'quotient_counterexample':{'discounted_distance':'1/5','asymptotically_equivalent':True},
 'exact_history_repair_shift_Lipschitz_constant':2,'asymptotic_repair_shift_isometry':True,
 'eventually_periodic_histories_checked':len(histories),'triangle_triples_checked':len(histories)**3,
 'unique_fundamental_initializer_derived':False,
 'new_physical_rule_adopted':False,'event_rule_modified':False,
 'scope':'Global plugin inventory plus focused source analysis, exact conditional bridges and quotient counterexample/repair proofs; no full historical independence, theorem certification or physical validation'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
