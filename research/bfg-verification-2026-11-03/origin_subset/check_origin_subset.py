"""Fresh-origin restriction and continuation controls; baseline unchanged."""
from pathlib import Path
import json,runpy,hashlib
import sympy as s
import numpy as np

OUT=Path(__file__).resolve().parent
Pi=s.diag(1,0);I=s.eye(2);F=2*Pi;W=Pi
# Common rectangular transport, with deliberately non-isometric amplitude.
T=s.Matrix([[s.Rational(1,2),0],[s.Rational(1,3),1],[0,0]])
A=T*F*T.T;a=s.trace(A);f=s.trace(F);m=s.trace(T*W*T.T)
assert m==a/f and T*W*T.T/m==A/a
S=s.diag(0,0,3);E=s.diag(0,0,1)
assert E*A==s.zeros(3) and E*S==S
Wp=A/a;Fp=A+S;ss=s.trace(S);U=S/ss
D=Fp/s.trace(Fp)-Wp
assert s.trace(D.T*D)==s.factor((ss/(a+ss))**2*(s.trace(Wp*Wp)+s.trace(U*U)))>0
# Exact fresh-ground input and active rank witness.
K=s.diag(-2,-1);Y=s.Matrix([[s.Rational(1,4),s.Rational(1,8)],[s.Rational(1,8),s.Rational(1,4)]])
assert set(Y.eigenvals())=={s.Rational(1,8),s.Rational(3,8)}
G=I+Y;C=G.inv();B=Y*C;e=s.Matrix([1,0])
Pg=e*(e.T*G*e).inv()*e.T*G
assert Pg==s.Matrix([[1,s.Rational(1,10)],[0,0]])
assert Pg*C==s.diag(s.Rational(4,5),0)
assert Pg*B==s.Matrix([[s.Rational(1,5),s.Rational(1,10)],[0,0]])
assert (Pg*C).col_join(Pg*B).rank()==2
lc=s.trace(G*Pg*C*F*C*Pg.T);lb=s.trace(G*Pg*B*F*B*Pg.T)
assert lc>0 and lb>0
alpha=lb/(lc+lb);beta=lc/(lc+lb)
analysis=(s.sqrt(alpha)*Pg*C).col_join(s.sqrt(beta)*Pg*B)
Kdouble=s.diag(-2,-1,-2,-1)
assert Kdouble*analysis==-2*analysis
assert s.trace((I/2-Pi)**2)==s.Rational(1,2)
baseline=OUT.parent/'baseline/extended_controls.py'
expected='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()==expected
event=runpy.run_path(str(baseline))['event']
arr=lambda x:np.array(x.tolist(),dtype=float)
records=[]
for name,y in [('isotropic',I/4),('noncommuting',Y)]:
    out,info=event(tuple(arr(x) for x in [K,F,W,y,Pi]))
    assert out is not None,info
    kn,fn,wn,yn,pn=out
    residual=float(np.linalg.norm(wn-fn/np.trace(fn),'fro')**2)
    if name=='isotropic':
        assert len(kn)==1 and info['seed']==0
        assert np.allclose(fn,[[2.]]) and np.allclose(wn,[[1.]])
        assert np.allclose(yn,[[float(s.Rational(32,425))]]) and residual<1e-24
    else:
        assert len(kn)==2 and abs(info['seed']-2)<1e-12
        assert np.allclose(kn,-2*np.eye(2),atol=1e-12)
        assert np.allclose(fn,2*np.eye(2),atol=1e-12)
        assert abs(np.trace(wn)-1)<1e-12 and np.allclose(wn@wn,wn,atol=1e-12)
        assert abs(residual-.5)<1e-12
    records.append(dict(case=name,dimension=len(kn),seed=info['seed'],formation_trace=float(np.trace(fn).real),squared_alignment_residual=residual))
report={'status':'PASS','date':'2026-11-03','exact_common_transport_identity':True,
 'exact_seed_separation_identity':True,'exact_noncommuting_active_rank':2,
 'fresh_minimum_density':'diag(2,0) for K=diag(-2,-1)',
 'implementation_checks':records,'implementation_rank_policy':'preserved binary64 helper; exact rank derived separately',
 'origin_subset_consistent':True,'origin_subset_forced_by_no_ancestry_alone':False,
 'fundamental_origin_identification_derived':False,'conditional_origin_rule_installed':False,
 'event_rule_modified':False,'new_physical_rule_adopted':False,'baseline_sha256':expected}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
