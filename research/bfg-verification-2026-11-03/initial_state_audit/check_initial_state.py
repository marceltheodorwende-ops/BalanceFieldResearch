"""Complete finite state versus initialization history and numeric policy.

Tests the preserved audit event, not every program in the repository.
"""
from pathlib import Path
import json,platform,runpy,hashlib,inspect
import numpy as np
import sympy as s

OUT=Path(__file__).resolve().parent
baseline=OUT.parent/'baseline/extended_controls.py'
event=runpy.run_path(str(baseline))['event']
I=s.eye(2);H=2*I;Hs=s.sqrt(2)*I
L1=I/2;M1=H;L2=I;M2=4*H
Y1=s.simplify(Hs*L1*M1.inv()*L1.T*Hs)
Y2=s.simplify(Hs*L2*M2.inv()*L2.T*Hs)
assert Y1==Y2==I/4
T=2*I
assert L1*T==L2 and T.T*M1*T==M2
K=np.array([[0.,1.],[1.,0.]])
f=np.eye(2);w=np.eye(2)/2;p=np.eye(2)
def make(y):return (K.copy(),f.copy(),w.copy(),np.array(y.tolist(),dtype=float),p.copy())
state1=make(Y1);state2=make(Y2)
for a,b in zip(state1,state2):assert np.array_equal(a,b)
# The event receives no H, L or M argument once Y is supplied.
assert list(inspect.signature(event).parameters)==['state','tol']
for _ in range(3):
    out1,info1=event(state1);out2,info2=event(state2)
    assert out1 is not None and out2 is not None
    assert all(np.allclose(a,b,rtol=0,atol=1e-13) for a,b in zip(out1,out2))
    state1=out1;state2=out2

# Omit Y but keep K,rhoF,rhoW,P: the missing input can change the first successor.
step=lambda y:2*y*y/((1+y)**2*(1+y*y))
ya=s.Rational(1,2);yb=s.Rational(1,4)
assert step(ya)==s.Rational(8,45) and step(yb)==s.Rational(32,425)
def scalar_state(y):return (np.array([[-1.]]),np.ones((1,1)),np.ones((1,1)),np.array([[float(y)]]),np.ones((1,1)))
sa,ia=event(scalar_state(ya));sb,ib=event(scalar_state(yb))
assert sa is not None and sb is not None
assert abs(sa[3][0,0]-float(step(ya)))<1e-14
assert abs(sb[3][0,0]-float(step(yb)))<1e-14

# Exact math versus a tolerance-induced stop in the preserved audit script.
tiny=s.Rational(1,10**6)
lc=1/(1+tiny);lb=tiny*tiny/(1+tiny)
assert lc>0 and lb>0 and 0<step(tiny)<tiny
stopped,stop_info=event(scalar_state(tiny))
continued,continue_info=event(scalar_state(tiny),tol=1e-14)
assert stopped is None and stop_info['terminal']=='load'
assert continued is not None
assert abs(continued[3][0,0]-float(step(tiny)))<1e-25

# A rich state cannot be reconstructed losslessly from the reduced data.
assert 0+1-2==0+2-3==-1
R1=s.diag(1,s.Rational(1,2));R2=s.diag(1,s.Rational(1,4))
assert R1!=R2 and R1[0,0]==R2[0,0]==1
assert abs(R1[1,1])<1 and abs(R2[1,1])<1

result={'status':'PASS','date':'2026-11-03','python':platform.python_version(),'numpy':np.__version__,'sympy':s.__version__,
 'scope':'The November mathematical five-tuple and preserved event() audit implementation, not every BFG program or a universal physical initialization',
 'complete_state_inputs':['K','rho_F','rho_W','Y','P'],
 'same_Y_interface_representation':{'Y':'I/4','L1':'I/2','M1':'2I','L2':'I','M2':'8I','relation':'Same interface under neutral-coordinate scaling T=2I; not two inequivalent physical models','fresh_event_steps_compared':3,'successors_agree':True},
 'omit_Y_witness':{'same_other_four_scalar_coordinates':True,'input_Y':['1/2','1/4'],'first_successor_Y':['8/45','32/425'],'same_complete_state':False},
 'numerical_policy_witness':{'input_Y':str(tiny),'exact_Lambda_B':str(lb),'exact_successor_Y':str(step(tiny)),'exact_branch':'nonterminal full-persistence success','default_audit_tol':1e-10,'default_audit_result':'load-labelled stop','smaller_tol':1e-14,'smaller_tol_result':'success','interpretation':'Tolerance dependence in the preserved audit implementation, not physical indeterminism or exact zero load; no production program fix is made'},
 'rich_state_projection_injective':False,
 'baseline_sha256':hashlib.sha256(baseline.read_bytes()).hexdigest(),
 'event_rule_modified':False,'new_fundamental_input_added':False,'formal_proof_assistant':False,'hardware':False}
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
