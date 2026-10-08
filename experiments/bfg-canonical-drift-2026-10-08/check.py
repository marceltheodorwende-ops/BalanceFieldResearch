"""Canonical geometry bound and separately declared drift; synthetic controls."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
from scipy.integrate import solve_ivp
from experiment import update
x,y=sp.symbols('x y',positive=True);p=sp.Rational(1,3)
lc=p/(1+x)+(1-p)/(1+y);lb=p*x*x/(1+x)+(1-p)*y*y/(1+y);al=lb/(lc+lb)
R=sp.Matrix([(al+(1-al)*u*u)/(1+u)**2 for u in [x,y]])
J=R.jacobian([x,y]);L=sp.Matrix([[1,-1]]);V=R-sp.Matrix([x,y]);Q=(L*sp.Matrix([x,y]))[0];W=(L*V)[0]
B=sp.Matrix([Q,W]).jacobian([x,y]);ACC=(L*(J-sp.eye(2))*V)[0]
assert sp.simplify((sp.Matrix([[sp.diff(W,x),sp.diff(W,y)]])*V)[0]-ACC)==0
rf=sp.lambdify((x,y),R,'numpy');jf=sp.lambdify((x,y),J,'numpy');af=sp.lambdify((x,y),ACC,'numpy');bf=sp.lambdify((x,y),B,'numpy')
r=lambda z:np.asarray(rf(*z),float).reshape(2)
z=np.array([.2,.7]);exact=sp.factor(B.subs({x:sp.Rational(1,5),y:sp.Rational(7,10)}).det());assert exact!=0
rng=np.random.default_rng(1008);ratios=[];ambient=[]
for n in [2,3,5]:
    for _ in range(10):
        ys=rng.uniform(.02,.98,n);Y=np.diag(ys)
        raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));F=raw@raw.conj().T+np.eye(n)
        K=np.eye(n);out=update(K,F,np.eye(n)/n,Y,np.eye(n));assert out['terminal'] is None
        lc0=np.sum(np.diag(F).real/(1+ys));lb0=np.sum(np.diag(F).real*ys*ys/(1+ys));alpha=lb0/(lc0+lb0)
        pred=(alpha+(1-alpha)*ys*ys)/(1+ys)**2
        back=out['v']@out['y']@out['v'].conj().T;ambient.append(float(np.max(abs(back-np.diag(pred)))))
        ratio=float(max(pred)/max(ys));ratios.append(ratio);assert ratio<=.5+1e-14
assert max(ambient)<1e-10
v=r(z)-z;eps=1e-6
num=((r(z+eps*v)-(z+eps*v))-(r(z-eps*v)-(z-eps*v)))/(2*eps)
accerr=abs((num[0]-num[1])-af(*z));assert accerr<1e-8
sol=solve_ivp(lambda t,u:r(u)-u,[0,6],z,method='DOP853',rtol=1e-12,atol=1e-14,dense_output=True)
assert sol.success
times=np.linspace(0,6,121);values=sol.sol(times)
lower=z[:,None]*np.exp(-times)[None,:];upper=max(z)*np.exp(-times/2)
assert np.min(values)>0 and np.min(values-lower)>-1e-10 and np.max(np.max(values,axis=0)-upper)<1e-10
flow1=sol.sol(1);gap=float(np.linalg.norm(flow1-r(z)));assert gap>.01
# A rescaled duration changes drift speed; it does not change normalized one-event flow.
h=.25
other=solve_ivp(lambda t,u:(r(u)-u)/h,[0,h],z,method='DOP853',rtol=1e-12,atol=1e-14)
scaleerr=float(np.max(abs(other.y[:,-1]-flow1)));assert scaleerr<1e-10
# Differential chart gate at the end of the inspected trajectory, no global invertibility claim.
chartdets=[float(np.linalg.det(bf(*u))) for u in values.T]
sharp=[]
for ee in [1e-3,1e-4,1e-5]:
    yy=np.array([ee,1-ee]);ff=np.array([ee,1.]);lc0=np.sum(ff/(1+yy));lb0=np.sum(ff*yy*yy/(1+yy));aa=lb0/(lc0+lb0);rr=(aa+(1-aa)*yy*yy)/(1+yy)**2;sharp.append(dict(epsilon=ee,norm_ratio=float(max(rr)/max(yy))))
assert sharp[-1]['norm_ratio']>.4999
result=dict(sharp_bound_sequence=sharp,kind='synthetic mathematics/code controls only',canonical_bound='norm(Y_next)<=norm(Y)/2 on full persistence',ambient_cases=len(ambient),max_ambient_residual=max(ambient),maximum_sampled_norm_ratio=max(ratios),exact_readout_determinant=str(exact),initial_drift_acceleration=float(af(*z)),acceleration_chain_difference_residual=float(accerr),drift_canonical_endpoint=r(z).tolist(),drift_flow_at_one=flow1.tolist(),event_flow_defect=gap,clock_rescaling_residual=scaleerr,min_tested_chart_determinant=min(chartdets),max_tested_chart_determinant=max(chartdets),sampled_positive_geometry=True,duration_seconds_calibrated=False,canonical_time_h_flow_claimed=False,physical_sine_force_derived=False,holdout_accessed=False)
Path(__file__).with_name('results').joinpath('controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
