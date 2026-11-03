"""Synthetic RC feasibility study. No laboratory measurements or BFG validation."""
from pathlib import Path
import json,csv,platform
import numpy as np
OUT=Path(__file__).resolve().parent
SEED=20261103
rng=np.random.default_rng(SEED)
g=1e-5;c=1e-5;vref=1.;y0=.8;tau=c/g
L=g*np.array([[2.,-1.,0.],[-1.,3.,-1.],[0.,-1.,2.]])
assert np.allclose(L@np.ones(3),g*np.ones(3),rtol=1e-14,atol=1e-20)
t=np.linspace(0.,5.,501)
ideal=y0*np.exp(-t/tau)
def trajectory(gs,cs):
    g1,gm,g2,b1,b2=gs
    lap=np.array([[g1+b1,-b1,0.],[-b1,gm+b1+b2,-b2],[0.,-b2,g2+b2]])
    invsqrt=1/np.sqrt(cs)
    h=invsqrt[:,None]*lap*invsqrt[None,:]
    lam,u=np.linalg.eigh(h)
    assert min(lam)>0
    coeff=u.T@(np.sqrt(cs)*np.full(3,y0))
    return invsqrt[:,None]*(u@(coeff[:,None]*np.exp(-lam[:,None]*t)))
nominal=trajectory(np.full(5,g),np.full(3,c))
assert np.max(abs(nominal-ideal))<1e-14
# ±1% independent conductance and capacitance deviations, not a claim about
# available hardware specifications. Measurement noise is a separate stream.
errors=[];off_modes=[]
for _ in range(1000):
    gs=g*(1+rng.uniform(-.01,.01,5));cs=c*(1+rng.uniform(-.01,.01,3))
    x=trajectory(gs,cs)
    errors.append(float(np.max(abs(x.mean(axis=0)-ideal))))
    off_modes.append(float(np.max(np.ptp(x,axis=0))))
noise=rng.normal(0.,.001,size=nominal.shape)
measured=np.round((nominal+noise)/.001)*.001
assert np.max(abs(measured-nominal))>0
with (OUT/'synthetic_fixed_time_trace.csv').open('w',newline='',encoding='utf-8') as stream:
    w=csv.writer(stream);w.writerow(['time_seconds','ideal_common_voltage','synthetic_measured_v1','synthetic_measured_vm','synthetic_measured_v2'])
    for j,time in enumerate(t):w.writerow([time,ideal[j],*measured[:,j]])
events=[];y=y0;time=0.
for k in range(7):
    events.append({'k':k,'time_seconds':time,'threshold_volts':y*vref,'above_1mV_floor':bool(y*vref>=.001)})
    nxt=2*y*y/((1+y)**2*(1+y*y));time+=tau*np.log(y/nxt);y=nxt
assert all(events[j+1]['time_seconds']>events[j]['time_seconds'] for j in range(len(events)-1))
# Exact classical Johnson equilibrium scale; detector noise is NOT this bath.
kB=1.380649e-23;temperature=300.
thermal_sigma=np.sqrt(kB*temperature/c)
result={'status':'PASS','data_type':'SYNTHETIC_ONLY','seed':SEED,'python':platform.python_version(),'numpy':np.__version__,'nominal':{'ground_resistors_ohm':[1/g]*3,'branch_resistors_ohm':[1/g]*2,'capacitances_farad':[c]*3,'reference_voltage':vref,'initial_voltage':y0,'time_constant_seconds':tau,'sample_rate_hz':100},'tolerance_cases':1000,'tolerance_model':'Independent uniform +/-1% deviations in each conductance and capacitance; not a calibrated instrument uncertainty budget','largest_common_voltage_deviation_V':max(errors),'largest_node_spread_V':max(off_modes),'synthetic_detector_sigma_V':.001,'synthetic_quantization_step_V':.001,'events':events,'equilibrium_thermal_sigma_V':float(thermal_sigma),'identifiability':'The ideal RC law with the designed BFG clock and its classical RC null predict identical event values. This pilot cannot discriminate a BFG natural law.','hardware_run':False,'formal_proof':False}
(OUT/'rc_pilot_results.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
