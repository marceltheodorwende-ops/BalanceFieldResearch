"""Development-only mechanical identification; fit integral balance, forecast causally."""
import argparse,csv,hashlib,json,re,sys
from pathlib import Path
import numpy as np
from scipy.optimize import nnls

MODELS={'gravity':[0],'viscous':[0,1],'quadratic':[0,2],'dry':[0,3],'mixed':[0,1,2,3]}

def features(theta,w):
    return np.stack([np.sin(theta),w,abs(w)*w,np.sign(w)],axis=-1)

def blocks(data,step=10):
    starts=np.arange(0,len(data)-step,step); ends=starts+step
    t,theta,w=data.T
    h=np.diff(t)
    f=features(theta,w)
    increments=.5*(f[1:]+f[:-1])*h[:,None]
    integral=np.vstack([np.zeros(4),np.cumsum(increments,axis=0)])
    return starts,ends,integral[ends]-integral[starts],-(w[ends]-w[starts])

def forecast(theta,w,coeff,duration,substeps=20):
    theta=theta.copy();w=w.copy();h=duration/substeps
    def rhs(a,v): return v,-features(a,v)@coeff
    for _ in range(substeps):
        a1,v1=rhs(theta,w)
        a2,v2=rhs(theta+h*a1/2,w+h*v1/2)
        a3,v3=rhs(theta+h*a2/2,w+h*v2/2)
        a4,v4=rhs(theta+h*a3,w+h*v3)
        theta+=h*(a1+2*a2+2*a3+a4)/6
        w+=h*(v1+2*v2+2*v3+v4)/6
    return theta,w

def fit(x,target,cols):
    xx=x[:,cols];norm=np.linalg.norm(xx,axis=0)
    if np.any(norm==0): raise ValueError('unidentified zero column')
    scaled=xx/norm
    c,_=nnls(scaled,target)
    full=np.zeros(4);full[cols]=c/norm
    singular=np.linalg.svd(scaled,compute_uv=False)
    return full,float(singular[0]/singular[-1]) if singular[-1]>0 else float('inf')

def main(data_dir,out_dir):
    root=Path(data_dir);out=Path(out_dir);out.mkdir(parents=True,exist_ok=True)
    expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in root.glob('*.csv')}!=expected:raise ValueError('development allowlist mismatch')
    records=[];predictions=[];provenance=[]
    for path in sorted(root.glob('*.csv')):
        raw=path.read_bytes();provenance.append(dict(file=path.name,sha256=hashlib.sha256(raw).hexdigest()))
        rows=list(csv.DictReader(raw.decode().splitlines()))
        data=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in rows])
        if not np.isfinite(data).all() or not np.all(np.diff(data[:,0])>0):raise ValueError('invalid recording')
        starts,ends,x,target=blocks(data)
        train=data[ends,0]<30;validation=data[starts,0]>=30
        idx=starts[validation];j=ends[validation];dt=data[j,0]-data[idx,0]
        baseline=np.sqrt(np.mean((data[j,2]-data[idx,2])**2))
        for name,cols in MODELS.items():
            coeff,condition=fit(x[train],target[train],cols)
            th,w=forecast(data[idx,1],data[idx,2],coeff,dt)
            _,fine=forecast(data[idx,1],data[idx,2],coeff,dt,40)
            if not np.isfinite(w).all():raise ValueError('forecast failure')
            error=np.sqrt(np.mean((w-data[j,2])**2))
            rec=dict(recording=path.name,model=name,training_blocks=int(train.sum()),validation_blocks=int(validation.sum()),a_gravity=float(coeff[0]),b_viscous=float(coeff[1]),c_quadratic=float(coeff[2]),d_dry=float(coeff[3]),scaled_design_condition=condition,velocity_rmse=float(error),persistence_velocity_rmse=float(baseline),relative_increment_rmse=float(error/baseline),integration_step_sensitivity=float(np.max(abs(fine-w))),integral_training_rmse=float(np.sqrt(np.mean((x[train]@coeff-target[train])**2))))
            records.append(rec)
            for start,end,pred in zip(idx,j,w):
                predictions.append(dict(recording=path.name,model=name,start_time=float(data[start,0]),end_time=float(data[end,0]),initial_angle=float(data[start,1]),initial_velocity=float(data[start,2]),target_velocity=float(data[end,2]),predicted_velocity=float(pred)))
    def write(name,rows):
        with (out/name).open('w',newline='') as f:
            wr=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');wr.writeheader();wr.writerows(rows)
    write('models.csv',records);write('predictions.csv',predictions)
    summary=dict(stage='exploratory; attempt-1 temporal development split, no confirmatory holdout',recordings=15,holdout_accessed=False,fit_seconds='0 <= t < 30',validation_seconds='30 <= t < 60',horizon_seconds=.1,models={m:dict(mean_relative_increment_rmse=float(np.mean([r['relative_increment_rmse'] for r in records if r['model']==m])),mean_velocity_rmse=float(np.mean([r['velocity_rmse'] for r in records if r['model']==m]))) for m in MODELS},max_integration_sensitivity=max(r['integration_step_sensitivity'] for r in records),coefficients_identified='mg*ell/I, b/I, c/I, tau_c/I conditional on torque model',individual_mass_inertia_drag_identified=False)
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(out/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('data_dir');p.add_argument('out_dir');args=p.parse_args();main(args.data_dir,args.out_dir)
