"""Development-only mechanically constrained BFG frequency calibration."""
import csv,json,sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'pendulum-mechanical-identification-2026-10-07'))
sys.path.insert(0,str(ROOT/'bfg-pendulum-motion-2026-10-07'))
from identify import blocks
from motion import one_step

LENGTHS=[.236,.330,.426,.518,.607]
G=9.799

def frequency_coefficient(length,inertia_ratio):
    return G*length/(length*length+inertia_ratio)

def profile(inertia_ratio,records):
    loss=0.;parameters=[]
    for r in records:
        a=frequency_coefficient(r['length'],inertia_ratio)
        z=r['target']-a*r['x'][:,0];q=r['x'][:,1]
        b=max(0,float(q@z/(q@q)))
        residual=z-b*q
        loss+=float(np.mean(residual**2)/np.mean(r['target']**2))
        parameters.append((r['name'],a,b))
    return loss/len(records),parameters

def fit_shared(records):
    result=minimize_scalar(lambda v:profile(v,records)[0],bounds=(0,.02),method='bounded',options={'xatol':1e-12})
    if not result.success:raise ValueError('calibration optimizer failed')
    candidates=[0.,.02,float(result.x)]
    chosen=min(candidates,key=lambda v:profile(v,records)[0])
    return chosen,profile(chosen,records)[1]

def main(data_dir,models_csv,out_dir):
    root=Path(data_dir);out=Path(out_dir);out.mkdir(exist_ok=True)
    expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in root.glob('*.csv')}!=expected:raise ValueError('holdout forbidden')
    free={r['recording']:r for r in csv.DictReader(Path(models_csv).open()) if r['model']=='viscous'}
    records=[]
    for p in sorted(root.glob('*.csv')):
        raw=list(csv.DictReader(p.open()));data=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in raw])
        starts,ends,x,target=blocks(data,10);train=data[ends,0]<30
        records.append(dict(name=p.name,length=LENGTHS[int(p.name[3])-1],condition=int(p.name[9]),x=x[train],target=target[train],data=data,starts=starts,ends=ends))
    global_ratio,global_params=fit_shared(records)
    condition_ratios={};condition_params=[]
    for c in [1,2,3]:
        ratio,params=fit_shared([r for r in records if r['condition']==c]);condition_ratios[c]=ratio;condition_params+=params
    _,point_params=profile(0.,records)
    parameters={'shared_inertia':{n:(a,b) for n,a,b in global_params},'condition_inertia':{n:(a,b) for n,a,b in condition_params},'point_mass':{n:(a,b) for n,a,b in point_params},'free_frequency':{n:(float(r['a_gravity']),float(r['b_viscous'])) for n,r in free.items()}}
    rows=[]
    for record in records:
        d=record['data'];s=record['starts'];e=record['ends'];valid=d[s,0]>=30;s=s[valid];e=e[valid]
        for model,ps in parameters.items():
            a,b=ps[record['name']]
            angle,w=one_step(d[s,1],d[s,2],a,b,.1)
            ar=np.sqrt(np.mean((angle-d[e,1])**2)/np.mean((d[s,1]-d[e,1])**2))
            wr=np.sqrt(np.mean((w-d[e,2])**2)/np.mean((d[s,2]-d[e,2])**2))
            rows.append(dict(recording=record['name'],condition=record['condition'],length_m=record['length'],model=model,a=a,b=b,validation_pairs=len(s),relative_angle_increment_rmse=float(ar),relative_velocity_increment_rmse=float(wr)))
    with (out/'models.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');writer.writeheader();writer.writerows(rows)
    summary=dict(stage='exploratory shared mechanical constraints on BFG readout; not emergence proof',recordings=15,holdout_accessed=False,fit_seconds='0-30',validation_seconds='30-60',global_inertia_ratio_m2=global_ratio,condition_inertia_ratio_m2=condition_ratios,bounds_m2=[0,.02],parameter_counts={'point_mass':15,'shared_inertia':16,'condition_inertia':18,'free_frequency':30},scores={m:{k:float(np.mean([r[k] for r in rows if r['model']==m])) for k in ['relative_angle_increment_rmse','relative_velocity_increment_rmse']} for m in parameters},physical_hypothesis='same bob mass; center at stated length; extra pivot inertia constant globally or by condition',absolute_inertia_identified=False,seconds_derived_from_BFG=False)
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary,indent=2))

if __name__=='__main__':main(*sys.argv[1:])
