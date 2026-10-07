import csv,json,sys
from pathlib import Path
import numpy as np
from motion import one_step

root=Path(sys.argv[1]);models=Path(sys.argv[2]);out=Path(sys.argv[3]);out.mkdir(exist_ok=True)
expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
if {p.name for p in root.glob('*.csv')}!=expected:raise ValueError('holdout forbidden')
calibration={r['recording']:r for r in csv.DictReader(models.open()) if r['model']=='viscous'}
rows=[];predictions=[]
for path in sorted(root.glob('*.csv')):
    data=list(csv.DictReader(path.open()))
    t=np.array([float(r['time']) for r in data]);theta=np.array([float(r['angle']) for r in data]);w=np.array([float(r['angular_velocity']) for r in data])
    start=np.arange(0,len(t)-10,10);start=start[t[start]>=30];end=start+10
    a=float(calibration[path.name]['a_gravity']);b=float(calibration[path.name]['b_viscous'])
    tp,wp=one_step(theta[start],w[start],a,b,.1)
    angle_rmse=float(np.sqrt(np.mean((tp-theta[end])**2)));velocity_rmse=float(np.sqrt(np.mean((wp-w[end])**2)))
    angle_persistence=float(np.sqrt(np.mean((theta[start]-theta[end])**2)));velocity_persistence=float(np.sqrt(np.mean((w[start]-w[end])**2)))
    rows.append(dict(recording=path.name,a=a,b=b,pairs=len(start),angle_rmse=angle_rmse,velocity_rmse=velocity_rmse,relative_angle_increment_rmse=angle_rmse/angle_persistence,relative_velocity_increment_rmse=velocity_rmse/velocity_persistence,zero_amplitude_inputs=int(np.sum((theta[start]==0)&(w[start]==0)))))
    for i,j,ap,vp in zip(start,end,tp,wp):predictions.append(dict(recording=path.name,time=float(t[i]),target_time=float(t[j]),target_angle=float(theta[j]),predicted_angle=float(ap),target_velocity=float(w[j]),predicted_velocity=float(vp)))
def write(name,content):
    with (out/name).open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(content[0]),lineterminator='\n');wr.writeheader();wr.writerows(content)
write('recordings.csv',rows);write('predictions.csv',predictions)
summary=dict(stage='exploratory calibrated BFG representation; mechanically equivalent linear oscillator',recordings=15,pairs=sum(r['pairs'] for r in rows),holdout_accessed=False,mean_relative_angle_increment_rmse=float(np.mean([r['relative_angle_increment_rmse'] for r in rows])),mean_relative_velocity_increment_rmse=float(np.mean([r['relative_velocity_increment_rmse'] for r in rows])),zero_amplitude_inputs=sum(r['zero_amplitude_inputs'] for r in rows),calibration='viscous mechanical coefficients fitted on development seconds 0-30',validation='development seconds 30-60',horizon_seconds=.1,physical_coefficients_derived_from_BFG=False,independent_superiority_over_linear_oscillator=False)
(out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
