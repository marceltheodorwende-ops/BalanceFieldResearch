"""P64 synthetic controls; no dataset access. Run python check.py."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
u=sp.symbols('u',real=True)
assert sp.trigsimp(sp.sin(4*sp.pi*(u+sp.Rational(1,2)))-sp.sin(4*sp.pi*u))==0
assert sp.trigsimp(sp.sin(6*sp.pi*(u+sp.Rational(1,3)))-sp.sin(6*sp.pi*u))==0
a=sp.symbols('a',real=True);k=sp.symbols('k',integer=True)
assert sp.simplify((sp.exp(2*sp.I*sp.pi*k*a)-1).subs(a,0))==0
nodes=np.concatenate([np.array([0,.2,.4,.6,.9]),(np.array([0,.2,.4,.6,.9])+.13)%1])
def bump(v):
    z=((v-.82+.5)%1-.5)/.02
    return float(np.exp(1-1/(1-z*z))) if abs(z)<1 else 0.
assert all(bump(v)==0 for v in nodes)
assert abs(bump(.82)-1)<1e-14
step=1e-5;bump_second=(bump(.82+step)-2*bump(.82)+bump(.82-step))/step**2
assert abs(bump_second)>1000
H=4;J=11;ks=np.array(list(range(-H,0))+list(range(1,H+1)));grid=np.arange(J)/J
E=np.exp(2j*np.pi*grid[:,None]*ks[None,:])
coeff=np.array([.03/(kk*kk)*np.exp(.3j*kk) for kk in ks]);cases=[]
for lag in [.37,1/7,.499999]:
    mult=np.exp(2j*np.pi*ks*lag)-1;M=E*mult
    sv=np.linalg.svd(M/np.sqrt(J),compute_uv=False);expected=np.sort(np.abs(mult))[::-1]
    err=float(np.max(np.abs(sv-expected)));assert err<1e-13
    data=M@coeff;assert max(abs(data.imag))<1e-14
    recovered=(E.conj().T@data/J)/mult
    recovery=float(np.linalg.norm(recovered-coeff));assert recovery<1e-11
    weakest_mode=int(abs(ks[np.argmin(abs(mult))]))
    noise=1e-4*np.cos(2*np.pi*weakest_mode*grid+1.1);noise_norm=float(np.linalg.norm(noise)/np.sqrt(J))
    rec_noisy=(E.conj().T@(data+noise)/J)/mult;dc=rec_noisy-coeff
    sigma=float(min(abs(mult)));cbound=noise_norm/sigma
    coeff_err=float(np.linalg.norm(dc));accel_err=float(np.linalg.norm((2*np.pi*ks)**2*dc))
    abound=(2*np.pi*H)**2*cbound
    assert coeff_err<=cbound*(1+1e-8) and accel_err<=abound*(1+1e-8)
    cases.append({'lag':lag,'singular_value_error':err,'sigma_min':sigma,
       'condition_number':float(max(sv)/min(sv)),'exact_recovery_error':recovery,
       'noise_mode':weakest_mode,'noise_norm':noise_norm,'coefficient_error':coeff_err,'coefficient_bound':cbound,
       'acceleration_error':accel_err,'acceleration_bound':abound})
lags=[.5,1/3];H2=5;ks2=np.array(list(range(-H2,0))+list(range(1,H2+1)));J2=13;grid2=np.arange(J2)/J2
E2=np.exp(2j*np.pi*grid2[:,None]*ks2[None,:])
blocks=[E2*(np.exp(2j*np.pi*ks2*lag)-1) for lag in lags]
half_sv=np.linalg.svd(blocks[0]/np.sqrt(J2),compute_uv=False)
half_rank=int(sum(half_sv>1e-12));assert half_rank==6
combined=np.vstack(blocks)/np.sqrt(J2*len(lags));sv=np.linalg.svd(combined,compute_uv=False)
pred=np.sqrt(np.mean([abs(np.exp(2j*np.pi*ks2*lag)-1)**2 for lag in lags],axis=0))
comb_err=float(max(abs(sv-np.sort(pred)[::-1])));assert comb_err<1e-13 and min(sv)>.5
assert max(abs(np.sin(2*np.pi*J2*grid2)))<1e-13
res={'kind':'synthetic measurement-selection controls','symbolic_checks':3,
     'finite_node_bump_nodes':len(nodes),'invisible_bump_second_derivative':bump_second,
     'fourier_cases':cases,'half_lag_rank_H5':half_rank,'full_column_count_H5':10,
     'combined_lag_rank':int(sum(sv>1e-12)),'combined_min_singular_value':float(min(sv)),
     'combined_singular_value_error':comb_err,'bandwidth_is_additional_assumption':True,
     'seconds_or_inertia_calibrated':False,'empirical_experiment_started':False,
     'real_measurements_used':False,'holdout_accessed':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2))
