"""Source count information, quadratic bridge consistency, and formation domain."""
from pathlib import Path
import json,hashlib
import sympy as s

OUT=Path(__file__).resolve().parent
def partition_data(sizes):
    labels=[];blocks=[];offset=0
    for size in sizes:
        block=list(range(offset,offset+size));blocks.append(block);labels.extend([len(blocks)-1]*size);offset+=size
    similarity=s.Matrix([[int(a==b) for b in labels] for a in labels])
    assert similarity==similarity.T and all(similarity[i,i]==1 for i in range(offset))
    threshold=s.Rational(1,2);counts=[]
    for block in blocks:
        i=block[0];counts.append(sum(1 for j in range(offset) if similarity[i,j]>=threshold))
    assert counts==sizes
    return [s.expand_log(s.log(c),force=True) for c in counts]

# Same configuration index and threshold; different comparison structure.
two_blocks=partition_data([2,2]);one_block=partition_data([4])
assert two_blocks[0]==s.log(2) and one_block[0]==2*s.log(2)
assert two_blocks[0]!=one_block[0]
I=s.eye(2);u=s.Matrix([1,0]);v=s.Matrix([0,1])
probes=[u,v,(u+v)/s.sqrt(2),(u-v)/s.sqrt(2),(u+s.I*v)/s.sqrt(2)]
basis=[s.diag(1,0),s.diag(0,1),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,s.I],[-s.I,0]])]
q=lambda j,p:s.simplify((p.conjugate().T*j*p)[0])
M=s.Matrix([[q(b,p) for b in basis] for p in probes])
bad=s.Matrix(partition_data([2,2,4,2,2]))
good=s.Matrix(partition_data([2,2,2,2,2]))
assert M.rank()==4 and M.row_join(bad).rank()==5
assert s.simplify(bad[2]+bad[3]-bad[0]-bad[1])==s.log(2)
assert M.row_join(good).rank()==4
sol=s.linsolve((M,good));expected=(s.log(2),s.log(2),s.Integer(0),s.Integer(0))
assert list(sol)==[expected]
J=sum((a*b for a,b in zip(expected,basis)),s.zeros(2))
assert J==s.log(2)*I and all(q(J,p)==s.log(2) for p in probes)
# The two fresh polarities normalize to one projector, not a full probe family.
K=s.diag(-2,1);Pi=s.diag(1,0);d=s.sqrt(2)*u
assert d*d.T==(-d)*(-d).T==2*Pi
vec=lambda a:s.Matrix([a[i,j] for i in range(2) for j in range(2)])
assert s.Matrix.hstack(vec(Pi),vec(Pi)).rank()==1
# Exact quartic variation at the fresh amplitude.
t=s.symbols('t',positive=True)
dw=s.sqrt(2)*(u+t*v)/s.sqrt(1+t*t)
F=lambda x:s.simplify((x.conjugate().T*K*x)[0]/2+((x.conjugate().T*x)[0])**2/4)
excess=s.factor(F(dw)+1)
assert excess==3*t*t/(1+t*t)
assert excess.subs(t,s.Rational(1,20))==s.Rational(3,401)<s.Rational(1,100)
assert excess.is_positive
# Generic finite ground-line formula for a real transverse coordinate.
lam,mu,z=s.symbols('lam mu z',real=True)
norm2=1+z*z
quartic_at_fixed_radius=(-lam)*(lam+mu*z*z)/(2*norm2)+lam**2/4
assert s.simplify(quartic_at_fixed_radius+lam**2/4+lam*z*z*(mu-lam)/(2*norm2))==0
baseline=OUT.parent/'baseline/extended_controls.py'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()=='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
report={'status':'PASS','date':'2026-11-03',
 'upstream_information_formula_found':'I_N0(X)=log|C_theta(X)|, Level-0 Section 14, PDF p.20',
 'same_threshold_comparison_example_information':['log(2)','log(4)'],
 'quadratic_measurement_rank':4,'incompatible_count_augmented_rank':5,
 'quadratic_identity_discrepancy':'log(2)',
 'compatible_count_operator':'log(2)*I',
 'exact_fresh_minimum_projector_span_rank':1,
 'transverse_quartic_excess':'3*t^2/(1+t^2)',
 'positive_budget_example_excess':'3/401 < 1/100; not an exact minimum',
 'finite_count_open_connected_exact_bridge':'only isotropic J=cI under the explicit bridge hypotheses',
 'actual_origin_similarity_and_representation_derived':False,
 'full_complex_admissible_origin_neighborhood_established':False,
 'unique_fundamental_initial_operator_derived':False,
 'new_physical_rule_adopted':False,'event_rule_modified':False,
 'scope':'Direct source count formula, exact candidate-bridge consistency controls and formation-domain distinction; not a full historical impossibility or empirical theorem'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
