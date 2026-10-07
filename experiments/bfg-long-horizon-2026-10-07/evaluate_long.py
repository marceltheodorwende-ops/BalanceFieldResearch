"""Development horizon stress: calibrated linear BFG versus nonlinear mechanics."""
import csv,json,sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'bfg-pendulum-motion-2026-10-07'))
sys.path.insert(0,str(ROOT/'pendulum-mechanical-identification-2026-10-07'))
from motion import prepare,readout
from phase_corrected import prepare_corrected,corrected_readout
from identify import forecast
HORIZONS=[.1,.2,.4,.8,1.6,3.2,6.4]

def main(data_dir,free_csv,shared_csv,out_dir):
    root=Path(data_dir);out=Path(out_dir);out.mkdir(exist_ok=True)
    expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in root.glob('*.csv')}!=expected:raise ValueError('holdout forbidden')
    free={r['recording']:r for r in csv.DictReader(Path(free_csv).open()) if r['model']=='viscous'}
    shared={r['recording']:r for r in csv.DictReader(Path(shared_csv).open()) if r['model']=='shared_inertia'}
    rows=[]
    for path in sorted(root.glob('*.csv')):
        raw=list(csv.DictReader(path.open()));data=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in raw])
        for horizon in HORIZONS:
            step=int(round(horizon/.01));starts=np.arange(3000,len(data)-step,10);ends=starts+step
            initial=data[starts,1:];target=data[ends,1:];duration=data[ends,0]-data[starts,0]
            a=float(free[path.name]['a_gravity']);b=float(free[path.name]['b_viscous'])
            sa=float(shared[path.name]['a']);sb=float(shared[path.name]['b'])
            F,K=prepare(initial[:,0],initial[:,1],a,b)
            SF,SK=prepare(initial[:,0],initial[:,1],sa,sb)
            CF,CK=prepare_corrected(initial[:,0],initial[:,1],a,b)
            predictions={'persistence':(initial[:,0],initial[:,1]),'linear_BFG_free':readout(F,K,horizon/.1,a,b,.1),'linear_BFG_shared':readout(SF,SK,horizon/.1,sa,sb,.1),'phase_corrected_BFG':corrected_readout(CF,CK,horizon/.1,a,b,.1)}
            coeff=np.array([a,b,0.,0.]);predictions['nonlinear_mechanical']=forecast(initial[:,0],initial[:,1],coeff,duration,max(20,step*2))
            for model,(theta,w) in predictions.items():
                angle_error=theta-target[:,0];velocity_error=w-target[:,1]
                rows.append(dict(recording=path.name,model=model,horizon_seconds=horizon,pairs=len(starts),angle_rmse=float(np.sqrt(np.mean(angle_error**2))),velocity_rmse=float(np.sqrt(np.mean(velocity_error**2))),relative_angle_rmse=float(np.sqrt(np.mean(angle_error**2)/np.mean(target[:,0]**2))),relative_velocity_rmse=float(np.sqrt(np.mean(velocity_error**2)/np.mean(target[:,1]**2)))))
    with (out/'recordings.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');wr.writeheader();wr.writerows(rows)
    aggregate=[]
    for horizon in HORIZONS:
        for model in ['persistence','linear_BFG_free','linear_BFG_shared','phase_corrected_BFG','nonlinear_mechanical']:
            selected=[r for r in rows if r['horizon_seconds']==horizon and r['model']==model]
            aggregate.append(dict(horizon_seconds=horizon,model=model,recordings=len(selected),pairs=sum(r['pairs'] for r in selected),mean_relative_angle_rmse=float(np.mean([r['relative_angle_rmse'] for r in selected])),mean_relative_velocity_rmse=float(np.mean([r['relative_velocity_rmse'] for r in selected]))))
    summary=dict(stage='exploratory development-only horizon stress',holdout_accessed=False,calibration_seconds='0-30',prediction_starts='30 until 60 minus horizon',horizons=HORIZONS,normalization='per-record RMS of target, not persistence increment',aggregate=aggregate)
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    for row in aggregate:
        print(row)

if __name__=='__main__':main(*sys.argv[1:])
