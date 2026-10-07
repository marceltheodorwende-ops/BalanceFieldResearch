"""Development-only force-family identifiability; no reserved attempts."""
import csv,json,hashlib,sys
from pathlib import Path
import numpy as np
from scipy.optimize import nnls
MODELS={'linear':[0,3],'sine':[1,3],'sine_second_harmonic':[1,2,3]}
def features(theta,w):return np.stack([theta,np.sin(theta),np.sin(2*theta),w],axis=-1)
def forecast(theta,w,c,duration):
    theta=theta.copy();w=w.copy();n=max(20,int(round(float(np.max(duration))/.005)));h=duration/n
    def rhs(x,v):return v,-features(x,v)@c
    for _ in range(n):
        x1,v1=rhs(theta,w);x2,v2=rhs(theta+h*x1/2,w+h*v1/2);x3,v3=rhs(theta+h*x2/2,w+h*v2/2);x4,v4=rhs(theta+h*x3,w+h*v3)
        theta+=h*(x1+2*x2+2*x3+x4)/6;w+=h*(v1+2*v2+2*v3+v4)/6
    return theta,w

def main(root,out):
    root=Path(root);out=Path(out);out.mkdir(exist_ok=True)
    expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in root.glob('*.csv')}!=expected:raise ValueError('development allowlist mismatch')
    records=[];scores=[];provenance=[]
    for p in sorted(root.glob('*.csv')):
        raw=p.read_bytes();provenance.append({'file':p.name,'sha256':hashlib.sha256(raw).hexdigest()})
        d=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in csv.DictReader(raw.decode().splitlines())]);t,x,v=d.T
        f=features(x,v);J=np.vstack([np.zeros(4),np.cumsum(.5*(f[1:]+f[:-1])*np.diff(t)[:,None],axis=0)])
        starts=np.arange(0,len(d)-10,10);ends=starts+10;mask=t[ends]<30;X=(J[ends]-J[starts])[mask];y=-(v[ends]-v[starts])[mask]
        for name,cols in MODELS.items():
            norm=np.linalg.norm(X[:,cols],axis=0);Z=X[:,cols]/norm;c=np.zeros(4);c[cols]=nnls(Z,y)[0]/norm
            condition=np.linalg.cond(Z)
            records.append(dict(recording=p.name,model=name,linear=float(c[0]),sine=float(c[1]),second_harmonic=float(c[2]),viscous=float(c[3]),equilibrium_stiffness=float(c[0]+c[1]+2*c[2]),scaled_condition=float(condition),training_blocks=int(mask.sum())))
            for horizon in [.1,6.4]:
                step=round(horizon/.01);i=np.arange(3000,len(d)-step,10);j=i+step
                theta,w=forecast(x[i],v[i],c,t[j]-t[i])
                scores.append(dict(recording=p.name,model=name,horizon_seconds=horizon,pairs=len(i),angle_relative_rmse=float(np.sqrt(np.mean((theta-x[j])**2)/np.mean(x[j]**2))),velocity_relative_rmse=float(np.sqrt(np.mean((w-v[j])**2)/np.mean(v[j]**2)))))
    for filename,rows in [('parameters.csv',records),('scores.csv',scores)]:
        with (out/filename).open('w',newline='') as h:
            wr=csv.DictWriter(h,fieldnames=list(rows[0]),lineterminator='\n');wr.writeheader();wr.writerows(rows)
    agg=[]
    for h in [.1,6.4]:
        for name in MODELS:
            r=[z for z in scores if z['horizon_seconds']==h and z['model']==name]
            agg.append(dict(model=name,horizon_seconds=h,pairs=sum(z['pairs'] for z in r),angle=float(np.mean([z['angle_relative_rmse'] for z in r])),velocity=float(np.mean([z['velocity_relative_rmse'] for z in r]))))
    summary=dict(recordings=15,holdout_accessed=False,stage='exploratory force selection; externally assumed potential',normalization='equal-record mean RMSE divided by target RMS',aggregate=agg,max_harmonic_condition=max(z['scaled_condition'] for z in records if z['model']=='sine_second_harmonic'))
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(out/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n');print(json.dumps(summary,indent=2))
if __name__=='__main__':main(*sys.argv[1:])
