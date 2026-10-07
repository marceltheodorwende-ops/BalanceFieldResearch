import csv,json,sys,hashlib
from pathlib import Path
import numpy as np
from scipy.optimize import brentq,minimize_scalar
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'pendulum-mechanical-identification-2026-10-07'))
from identify import forecast

def f(y):return 2*y*y/((1+y)**2*(1+y*y))
def inverse(value):
    if not 0<value<.25:raise ValueError('inverse domain')
    return brentq(lambda x:f(x)-value,0,1,xtol=1e-14)
def feedback(y,r):
    d=inverse(r*y)-y
    if not 0<d<.75:raise ValueError('input policy outside paper domain')
    return d

def main(root,calibration,out):
    root=Path(root);out=Path(out);out.mkdir(exist_ok=True)
    expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in root.glob('*.csv')}!=expected:raise ValueError('holdout forbidden')
    coeff={r['recording']:r for r in csv.DictReader(Path(calibration).open()) if r['model']=='viscous'}
    rows=[];params=[];provenance=[]
    for path in sorted(root.glob('*.csv')):
        d=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in csv.DictReader(path.open())]);t,theta,w=d.T;a=float(coeff[path.name]['a_gravity']);b=float(coeff[path.name]['b_viscous']);E=w*w/2+a*(1-np.cos(theta));scale=8*np.max(E[t<30]);y=E/scale
        i=np.arange(0,len(d)-10,10);j=i+10;train=t[j]<30;x=y[i[train]];z=y[j[train]]
        r=float(np.clip(np.dot(x,z)/np.dot(x,x),0,1));fit=minimize_scalar(lambda dd:np.mean((f(x+dd)-z)**2),bounds=(1e-8,.74999999),method='bounded',options={'xatol':1e-12});const=float(fit.x)
        if not fit.success:raise ValueError('calibration failure')
        oracle=[];valid=0
        for left,right in zip(x,z):
            try:q=inverse(right)-left;oracle.append(q);valid+=int(0<q<.75)
            except ValueError:oracle.append(float('nan'))
        params.append(dict(recording=path.name,a=a,energy_scale=scale,retention=r,constant_input=const,training_pairs=len(x),oracle_admissible=valid,oracle_input_min=float(np.nanmin(oracle)),oracle_input_max=float(np.nanmax(oracle)),max_validation_y=float(np.max(y[t>=30]))))
        provenance.append(dict(recording=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        for horizon in [.1,1.6,6.4]:
            step=round(horizon/.01);i=np.arange(3000,len(d)-step,10);j=i+step;initial=y[i];target=y[j];events=round(horizon/.1)
            theta_pred,w_pred=forecast(theta[i],w[i],np.array([a,b,0.,0.]),t[j]-t[i],max(20,step*2))
            mechanical=(w_pred*w_pred/2+a*(1-np.cos(theta_pred)))/scale
            for model in ['persistence','autonomous','constant_input','retention','causal_feedback','mechanical_sine_energy']:
                pred=initial.copy();mask=np.ones(len(i),dtype=bool);logpred=np.log(initial)
                for k in range(events):
                    if model=='autonomous':
                        logpred=np.log(2)+2*logpred-2*np.logaddexp(0,logpred)-np.logaddexp(0,2*logpred);pred=np.exp(logpred)
                    elif model=='mechanical_sine_energy':pred=mechanical
                    elif model=='constant_input':
                        mask&=(pred+const<1)&(pred+const>0);pred=f(pred+const)
                    elif model=='retention':pred*=r
                    elif model=='causal_feedback':
                        # interval proof: if endpoints of initial range are admissible,
                        # every intervening y is checked independently below.
                        next_values=[]
                        for n,value in enumerate(pred):
                            if not mask[n]:next_values.append(float('nan'));continue
                            try:dd=feedback(value,r);next_values.append(f(value+dd))
                            except ValueError:mask[n]=False;next_values.append(float('nan'))
                        pred=np.array(next_values)
                mask&=np.isfinite(pred)
                score=float(np.sqrt(np.mean((pred-target)**2)/np.mean(target**2))) if np.all(mask) else None
                rows.append(dict(recording=path.name,horizon_seconds=horizon,model=model,pairs=len(i),covered=int(mask.sum()),relative_energy_rmse=score))
    for name,records in [('scores.csv',rows),('parameters.csv',params)]:
        with (out/name).open('w',newline='') as h:
            wr=csv.DictWriter(h,fieldnames=list(records[0]),lineterminator='\n');wr.writeheader();wr.writerows(records)
    aggregate=[]
    for h in [.1,1.6,6.4]:
        for model in ['persistence','autonomous','constant_input','retention','causal_feedback','mechanical_sine_energy']:
            rr=[r for r in rows if r['horizon_seconds']==h and r['model']==model]
            aggregate.append(dict(horizon_seconds=h,model=model,pairs=sum(r['pairs'] for r in rr),covered=sum(r['covered'] for r in rr),mean_relative_energy_rmse=float(np.mean([r['relative_energy_rmse'] for r in rr])) if all(r['relative_energy_rmse'] is not None for r in rr) else None))
    summary=dict(stage='exploratory input/energy bridge',holdout_accessed=False,recordings=15,aggregate=aggregate,feedback_equivalent_to_retention=True,oracle_forecasts_used=False,oracle_training_admissible=sum(r['oracle_admissible'] for r in params),oracle_training_pairs=sum(r['training_pairs'] for r in params),calibration_sha256=hashlib.sha256(Path(calibration).read_bytes()).hexdigest(),source_commit='cbf82673641ecd65e902ad5c38a048387649a2a0',source_files=provenance)
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in summary.items() if k not in ['source_files']},indent=2))
if __name__=='__main__':main(*sys.argv[1:])
