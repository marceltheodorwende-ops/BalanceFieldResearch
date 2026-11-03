"""Fixed-event coupling dependence: exact witnesses and bounded implementation checks."""
from pathlib import Path
import json,platform,runpy
import sympy as s
import numpy as np
import mpmath as mp

OUT=Path(__file__).resolve().parent
event=runpy.run_path(str(OUT.parent/'baseline/extended_controls.py'))['event']
I=s.eye(2);P=s.diag(1,0);rho=P
def state(K,Y,p=I,f=I,w=I/2):
    return tuple(np.array(m.tolist(),dtype=float) for m in [K,f,w,Y,p])

# A change of input coupling can change continuation vs absorption, with the
# original event (including its exact selector) held fixed.
K=s.diag(-1,2);H=s.diag(2,3);M=H
assert K+I+2*P==H
La=I/2;Lb=s.diag(2,s.Rational(1,2))
Ya=La*La;Yb=Lb*Lb
assert Ya==I/4 and Yb==s.diag(4,s.Rational(1,4))
Qa=I;Qb=s.diag(0,1)
assert s.trace(Qa*rho)==1 and s.trace(Qb*rho)==0
good,igood=event(state(K,Ya,f=rho,w=rho))
bad,ibad=event(state(K,Yb,f=rho,w=rho))
assert good is not None and bad is None and ibad['terminal']=='selection'

# Even with all initial eigenvalues <1 and both branches successful, eventual
# carrier dimension and formation stock can change.
K2=s.diag(-2,-1);H2=s.diag(4,1);Hs=s.diag(2,1)
assert K2+2*I+4*P==H2
Ydiag=I/4;Yoff=s.Matrix([[s.Rational(1,4),s.Rational(1,8)],
                       [s.Rational(1,8),s.Rational(1,4)]])
sqrtY=s.Matrix([[(s.sqrt(6)+s.sqrt(2))/8,(s.sqrt(6)-s.sqrt(2))/8],
                [(s.sqrt(6)-s.sqrt(2))/8,(s.sqrt(6)+s.sqrt(2))/8]])
Loff=Hs.inv()*sqrtY*Hs
assert s.simplify(Hs*Loff*H2.inv()*Loff.T*Hs-Yoff)==s.zeros(2)
assert ((I-P)*Ydiag*P).rank()==0 and ((I-P)*Yoff*P).rank()==1
diag_out,di=event(state(K2,Ydiag,p=P,f=P,w=P))
off_out,oi=event(state(K2,Yoff,p=P,f=P,w=P))
assert diag_out is not None and off_out is not None
assert len(diag_out[0])==1 and len(off_out[0])==2
assert abs(np.trace(diag_out[4])-1)<1e-12 and abs(np.trace(off_out[4])-2)<1e-12
assert abs(np.trace(diag_out[1])-1)<1e-12 and abs(np.trace(off_out[1])-3)<1e-12
assert di['seed']==0 and abs(oi['seed']-2)<1e-12

# Different limiting kernels, despite identical eventual load limit zero.
K3=s.Matrix([[0,1],[1,0]]);H3=2*I
ground=s.Matrix([[s.Rational(1,2),-s.Rational(1,2)],
                 [-s.Rational(1,2),s.Rational(1,2)]])
assert K3+I+2*ground==H3
Yiso=I/4;Yanis=s.diag(s.Rational(1,4),s.Rational(9,16))
ys=list(Yanis.diagonal());weights=[s.Rational(1,2)]*2
a=s.factor(sum(w*y*y/(1+y) for w,y in zip(weights,ys))/sum(w*(1+y*y)/(1+y) for w,y in zip(weights,ys)))
c2=s.factor((a+(1-a)*ys[0]*ys[1])**2/((a+(1-a)*ys[0]**2)*(a+(1-a)*ys[1]**2)))
assert 0<c2<1
isout,ii=event(state(K3,Yiso,f=ground,w=ground))
anout,ai=event(state(K3,Yanis,f=ground,w=ground))
assert isout is not None and anout is not None
norm_iso=float(np.linalg.norm(isout[0],'fro')**2)
norm_an=float(np.linalg.norm(anout[0],'fro')**2)
assert abs(norm_iso-2)<1e-12 and abs(norm_an-2*float(c2))<1e-12

# Full-support controls: scalar, anisotropic, near-boundary and singular formation.
# The proof, not this finite computation, establishes the infinite-time statement.
mp.mp.dps=90
initial_cases=[(['.25','.25'],['.5','.5']),(['.25','.5625'],['.5','.5']),
               (['.000001','.999999'],['1','0']),(['.01','.5','.9'],['0','1','0'])]
paths=[]
for initial,fw in initial_cases:
    yy=list(map(mp.mpf,initial));ff=list(map(mp.mpf,fw));logs=[]
    for k in range(15):
        mm=max(yy);logs.append(str(mp.log10(mm)))
        if k>=2:assert mm<=mp.mpf('.5')*mp.mpf('.8')**(2**(k-2))*(1+mp.mpf('1e-75'))
        alpha=sum(w*y*y/(1+y) for w,y in zip(ff,yy))/sum(w*(1+y*y)/(1+y) for w,y in zip(ff,yy))
        nxt=[(alpha+(1-alpha)*y*y)/(1+y)**2 for y in yy]
        assert 0<max(nxt)<mm and all(y>0 for y in nxt)
        yy=nxt
    paths.append({'initial_loads':initial,'formation_diagonal':fw,'log10_max_load':logs})

result={'status':'PASS','date':'2026-11-03','python':platform.python_version(),'sympy':s.__version__,'numpy':np.__version__,'mpmath':mp.__version__,
 'fixed_event_rule':True,'input_coupling_only_varied_within_each_pair':True,
 'outcome_pair':{'same_K':'diag(-1,2)','same_H_and_M':'diag(2,3)','same_rhoF_rhoW':'diag(1,0)','same_P':'I','Ya':'I/4','Yb':'diag(4,1/4)','exact_initial_witness_masses':['1','0'],'first_outcome':'full-persistence success, analytically infinite continuation','second_outcome':'exact first-selection absorption','implementation_terminal_reason':ibad['terminal']},
 'carrier_and_seed_pair':{'same_K':'diag(-2,-1)','same_H_and_M':'diag(4,1)','same_P_rhoF_rhoW':'diag(1,0)','exact_transverse_ranks':[0,1],'eventual_dimensions':[1,2],'seed_counts':[0,1],'formation_traces':[1,3],'both_infinite_by_full_persistence_theorem':True,'implementation_errors_below':1e-12},
 'kernel_limit_pair':{'same_K':'[[0,1],[1,0]]','same_H_and_M':'2I','same_P':'I','same_rhoF_rhoW':'negative-ground projector of K','isotropic_load':'I/4','anisotropic_load':'diag(1/4,9/16)','first_Schur_factor_squared_exact':str(c2),'isotropic_limit_off_diagonal':'1','anisotropic_limit_off_diagonal_upper_bound':'sqrt('+str(c2)+') < 1','limit_difference_status':'Analytic consequence of nonincreasing positive Schur products; not inferred by finite-time extrapolation'},
 'high_precision_paths':paths,'steps_recorded_per_path':15,'precision_digits':90,
 'formal_proof_assistant':False,'new_law_adopted':False,'hardware_data':False}
(OUT/'results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='high_precision_paths'},indent=2))
