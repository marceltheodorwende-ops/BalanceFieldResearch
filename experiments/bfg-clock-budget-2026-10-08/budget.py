"""Clock-only analytic error budgets on real development states."""
import csv,json,sys,hashlib
from pathlib import Path
import numpy as np

def clock_bounds(theta,w,a,b,h,epsilon):
    if a<=0 or b<0 or h<0 or not 0<=epsilon<=1:raise ValueError('passive domain')
    E=w*w/2+a*(1-np.cos(theta));speed=np.sqrt(2*E)
    acceleration=a*np.minimum(1,np.sqrt(2*E/a))+b*speed
    return speed*epsilon*h,acceleration*epsilon*h

def main(root,calibration,out):
    root=Path(root);out=Path(out);out.mkdir(exist_ok=True)
    expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in root.glob('*.csv')}!=expected:raise ValueError('holdout forbidden')
    coeff={r['recording']:r for r in csv.DictReader(Path(calibration).open()) if r['model']=='viscous'}
    rows=[];sources=[]
    for path in sorted(root.glob('*.csv')):
        sources.append(dict(file=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        d=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in csv.DictReader(path.open())]);a=float(coeff[path.name]['a_gravity']);b=float(coeff[path.name]['b_viscous'])
        for h in [.1,1.6,6.4]:
            step=round(h/.01);i=np.arange(3000,len(d)-step,10);j=i+step
            th,vel=clock_bounds(d[i,1],d[i,2],a,b,h,.01)
            target=np.sqrt(np.mean(d[j,1]**2));ar=np.sqrt(np.mean(th**2));vr=np.sqrt(np.mean(vel**2))
            rows.append(dict(recording=path.name,horizon_seconds=h,pairs=len(i),clock_error_fraction=.01,angle_rmse_bound_rad=float(ar),velocity_rmse_bound_rad_s=float(vr),angle_target_normalized_bound=float(ar/target),clock_fraction_for_extra_angle_nrmse_005=float(.01*.05*target/ar),clock_fraction_for_max_extra_angle_001rad=float(.01*.01/np.max(th))))
    with (out/'budgets.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');wr.writeheader();wr.writerows(rows)
    summary=dict(stage='exploratory analytic clock-only budgets, conditional mechanical model',holdout_accessed=False,recordings=15,calibration_sha256=hashlib.sha256(Path(calibration).read_bytes()).hexdigest(),source_commit='cbf82673641ecd65e902ad5c38a048387649a2a0',source_files=sources,horizons=[])
    for h in [.1,1.6,6.4]:
        r=[z for z in rows if z['horizon_seconds']==h];summary['horizons'].append(dict(horizon_seconds=h,mean_angle_normalized_bound_at_1percent=float(np.mean([z['angle_target_normalized_bound'] for z in r])),max_common_clock_fraction_extra_nrmse_005=min(z['clock_fraction_for_extra_angle_nrmse_005'] for z in r),max_common_clock_fraction_extra_max_angle_001rad=min(z['clock_fraction_for_max_extra_angle_001rad'] for z in r)))
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary['horizons'],indent=2))
if __name__=='__main__':main(*sys.argv[1:])
