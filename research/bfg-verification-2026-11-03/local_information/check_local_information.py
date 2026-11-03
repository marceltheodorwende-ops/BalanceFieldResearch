"""Exact local information reconstruction; no new BFG state or dynamics."""
from pathlib import Path
import json,hashlib
import sympy as s

OUT=Path(__file__).resolve().parent

def family(n,t):
    eye=s.eye(n);e=eye[:,0];rows=[(('center',),e,s.Integer(1))]
    for j in range(1,n):
        for name,c in [('plus',t),('minus',-t),('imag',s.I*t)]:
            raw=e+c*eye[:,j];norm2=1+t*t
            rows.append(((name,j),raw/s.sqrt(norm2),norm2))
    for j in range(1,n):
        for k in range(j+1,n):
            for name,c in [('pair_real',t),('pair_imag',s.I*t)]:
                raw=e+t*eye[:,j]+c*eye[:,k];norm2=1+2*t*t
                rows.append(((name,j,k),raw/s.sqrt(norm2),norm2))
    assert len(rows)==n*n
    return rows

def hbasis(n):
    out=[]
    for j in range(n):
        a=s.zeros(n);a[j,j]=1;out.append(a)
    for j in range(n):
        for k in range(j+1,n):
            a=s.zeros(n);a[j,k]=a[k,j]=1;out.append(a)
            b=s.zeros(n);b[j,k]=s.I;b[k,j]=-s.I;out.append(b)
    return out

q=lambda j,v:s.simplify((v.conjugate().T*j*v)[0])
def reconstruct(n,t,observed):
    a=observed[('center',)];jmat=s.zeros(n);jmat[0,0]=a
    for j in range(1,n):
        rp=observed[('plus',j)];rm=observed[('minus',j)];ri=observed[('imag',j)]
        jmat[j,j]=s.simplify((rp+rm-2*a)/(2*t*t))
        re=s.simplify((rp-rm)/(4*t));im=s.simplify(((rp+rm)/2-ri)/(2*t))
        jmat[0,j]=re+s.I*im;jmat[j,0]=re-s.I*im
    for j in range(1,n):
        for k in range(j+1,n):
            re=s.simplify((observed[('pair_real',j,k)]-a-2*t*(s.re(jmat[0,j])+s.re(jmat[0,k]))-t*t*(jmat[j,j]+jmat[k,k]))/(2*t*t))
            im=s.simplify((a+2*t*s.re(jmat[0,j])-2*t*s.im(jmat[0,k])+t*t*(jmat[j,j]+jmat[k,k])-observed[('pair_imag',j,k)])/(2*t*t))
            jmat[j,k]=re+s.I*im;jmat[k,j]=re-s.I*im
    return s.simplify(jmat)

records=[]
for n in [2,3,4]:
    J=s.diag(*[10+j for j in range(n)])
    for j in range(n):
        for k in range(j+1,n):
            J[j,k]=s.Rational(j+k+1,10)+s.I*s.Rational(j-k,10)
            J[k,j]=s.conjugate(J[j,k])
    assert all(J[:j,:j].det()>0 for j in range(1,n+1))
    for t in [s.Rational(1,4),s.Rational(1,16)]:
        rows=family(n,t);e=s.eye(n)[:,0]
        observed={tag:s.simplify(norm2*q(J,v)) for tag,v,norm2 in rows}
        assert reconstruct(n,t,observed)==J
        measurement=s.Matrix([[q(b,v) for b in hbasis(n)] for _,v,_ in rows])
        assert measurement.rank()==n*n
        for _,v,norm2 in rows:
            assert s.simplify((v.conjugate().T*v)[0])==1
            dist2=s.simplify(((v-e).conjugate().T*(v-e))[0])
            assert dist2<=norm2-1<=2*t*t
        records.append(dict(dimension=n,t=str(t),profile_count=n*n,exact_measurement_rank=n*n,reconstruction='exact'))
# Symbolic n=2 determinant in coordinates J00,J11,ReJ01,ImJ01.
t=s.symbols('t',positive=True)
M=s.Matrix([[1,0,0,0],[1,t*t,2*t,0],[1,t*t,-2*t,0],[1,t*t,0,-2*t]])
for row in range(1,4):
    for col in range(4):M[row,col]/=1+t*t
assert s.factor(M.det())==8*t**4/(1+t*t)**3
# Real-only profiles cannot determine the imaginary Hermitian sector.
I=s.eye(2);imaginary=s.Matrix([[0,s.I],[-s.I,0]])
J1=I;J2=I+imaginary/2
x,y=s.symbols('x y',real=True);v=s.Matrix([x,y])
assert q(J2,v)==q(J1,v)
assert all(a>0 for a in J2.eigenvals())
assert q(J2,s.Matrix([1,s.I])/s.sqrt(2))!=q(J1,s.Matrix([1,s.I])/s.sqrt(2))
# Residual budget and a boundedness-domain obstruction.
qdec=s.Rational(1,2);lam=s.Integer(1);budget=s.Rational(1,10);tv=s.Rational(1,4)
assert 2*lam*(1-qdec)**2*tv**2<=budget
for _,v,_ in family(3,tv):
    R=s.diag(1,qdec,qdec)
    residual=(R-s.eye(3))*v
    assert q(s.eye(3),residual)<=budget
power=s.symbols('m',integer=True,nonnegative=True)
assert s.diag(1,2)**power==s.diag(1,2**power)
# Exact balance fixes J only with the remaining operators supplied and compatible.
E=s.diag(2,3);B=s.diag(6,12);N=I;Jbalance=E.inv()*B*N
assert Jbalance==s.diag(3,4)
for _,v,_ in family(2,s.Rational(1,4)):
    assert s.simplify(q(E*Jbalance,v)/q(B*N,v))==1
epsilon=s.Rational(1,10)
for candidate in [I,I+epsilon*s.diag(1,-1)/2]:
    assert all(1-epsilon<=a<=1+epsilon for a in candidate.eigenvals())
# Exact worst-case diagonal error amplification from normalized observation errors.
eta=s.Rational(1,10**6);error_rows=[]
for tv in [s.Rational(1,10),s.Rational(1,100)]:
    amplification=(2+tv*tv)/(tv*tv)
    achieved=((1+tv*tv)*eta+(1+tv*tv)*eta+2*eta)/(2*tv*tv)
    assert achieved==amplification*eta
    error_rows.append(dict(t=str(tv),normalized_value_error=str(eta),diagonal_error_bound=str(achieved),amplification=str(amplification)))
baseline=OUT.parent/'baseline/extended_controls.py'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()=='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
report={'status':'PASS','date':'2026-11-03','exact_reconstruction_cases':records,
 'arbitrarily_local_complex_profile_family':'n^2 normalized profiles; radius <= sqrt(2)t',
 'symbolic_2x2_measurement_determinant':'8*t^4/(1+t^2)^3',
 'real_only_profiles_identify_full_complex_operator':False,
 'residual_budget_fixture':'all n=3 local probes pass at t=1/4, q=1/2, lambda=1, budget=1/10',
 'full_dynamic_reachability_or_source_action_minimum_proved':False,
 'exact_balance_operator_identity_given_other_operators':'E J = B_op N',
 'approximate_balance_band_uniquely_fixes_J':False,
 'error_amplification':error_rows,
 'source_origin_functional_values_derived':False,'unique_fundamental_initializer_derived':False,
 'new_physical_rule_adopted':False,'event_rule_modified':False,
 'scope':'Finite conditional identifiability, explicit local reconstruction, admissible-domain restrictions and arithmetic conditioning; not empirical validation or a complete origin theorem'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
