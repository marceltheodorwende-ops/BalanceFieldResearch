"""Development-only measurement and estimation sensitivity; no model selection."""
import csv,json,sys
from pathlib import Path
import numpy as np
from identify import blocks,fit,forecast,MODELS

def write(path,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');w.writeheader();w.writerows(rows)

def main(root,out):
    root=Path(root);out=Path(out);out.mkdir(exist_ok=True)
    expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in root.glob('*.csv')}!=expected:raise ValueError('holdout forbidden')
    measurements=[];sens=[]
    for path in sorted(root.glob('*.csv')):
        rows=list(csv.DictReader(path.open()))
        data=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in rows])
        t,theta,w=data.T
        starts,ends,_,_=blocks(data,10)
        trapezoid=.5*(w[1:]+w[:-1])*np.diff(t)
        integral=np.r_[0,np.cumsum(trapezoid)]
        measured=theta[ends]-theta[starts];pred=integral[ends]-integral[starts]
        residual=measured-pred
        # Half-unit rounding propagation: two endpoint angles plus integrated velocity.
        rounding_bound=.001+.0005*(t[ends]-t[starts])
        encoder_bound=rounding_bound+2*np.pi/2000
        measurements.append(dict(recording=path.name,blocks=len(starts),angle_balance_rmse=float(np.sqrt(np.mean(residual**2))),angle_balance_bias=float(np.mean(residual)),fraction_beyond_rounding_only=float(np.mean(abs(residual)>rounding_bound)),relative_angle_balance_rmse=float(np.sqrt(np.mean(residual**2)/np.mean(measured**2))),fraction_beyond_illustrative_encoder_plus_rounding=float(np.mean(abs(residual)>encoder_bound)),angular_velocity_mean=float(np.mean(w)),angle_mean=float(np.mean(theta))))
        for step in [5,10,20,50]:
            starts,ends,x,target=blocks(data,step)
            validation=t[starts]>=40;idx=starts[validation];j=ends[validation];dt=t[j]-t[idx]
            persistence=float(np.sqrt(np.mean((w[j]-w[idx])**2)))
            for cutoff in [20,30,40]:
                training=t[ends]<cutoff
                for model,cols in MODELS.items():
                    coeff,condition=fit(x[training],target[training],cols)
                    _,v=forecast(theta[idx],w[idx],coeff,dt,substeps=max(20,step*2))
                    error=float(np.sqrt(np.mean((v-w[j])**2)))
                    sens.append(dict(recording=path.name,model=model,fit_until_seconds=cutoff,horizon_seconds=step*.01,training_blocks=int(training.sum()),validation_blocks=int(validation.sum()),relative_increment_rmse=error/persistence,velocity_rmse=error,a=float(coeff[0]),b=float(coeff[1]),c=float(coeff[2]),d=float(coeff[3]),scaled_design_condition=condition))
    write(out/'measurement_consistency.csv',measurements);write(out/'window_horizon_sensitivity.csv',sens)
    aggregate=[]
    for cutoff in [20,30,40]:
        for horizon in [.05,.1,.2,.5]:
            for model in MODELS:
                selected=[r for r in sens if r['fit_until_seconds']==cutoff and r['horizon_seconds']==horizon and r['model']==model]
                aggregate.append(dict(fit_until_seconds=cutoff,horizon_seconds=horizon,model=model,mean_relative_increment_rmse=float(np.mean([r['relative_increment_rmse'] for r in selected]))))
    summary=dict(stage='post-development diagnostic; no independent confirmation',recordings=15,holdout_accessed=False,measurement_assumption='theta_dot equals measured angular velocity',mean_fraction_balance_residual_beyond_rounding_only=float(np.mean([r['fraction_beyond_rounding_only'] for r in measurements])),mean_relative_angle_balance_rmse=float(np.mean([r['relative_angle_balance_rmse'] for r in measurements])),rounding_bound_excludes_quadrature_and_sensor_error=True,mean_fraction_beyond_illustrative_encoder_plus_rounding=float(np.mean([r['fraction_beyond_illustrative_encoder_plus_rounding'] for r in measurements])),encoder_assumption='illustrative half step per angle endpoint; not calibrated accuracy or velocity uncertainty',validation_seconds='40 to 60, common for all windows',model_window_horizon_scores=aggregate,no_best_configuration_selected=True)
    (out/'diagnostic_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps({k:v for k,v in summary.items() if k!='model_window_horizon_scores'},indent=2))

if __name__=='__main__': main(sys.argv[1],sys.argv[2])
