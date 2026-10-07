import argparse,csv,hashlib,json,sys
from pathlib import Path
import numpy as np
from phase import encode,forecast
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'pendulum-mechanical-identification-2026-10-07'))
from identify import forecast as cartesian

def main(data_dir,models_path,out_dir):
    data_dir=Path(data_dir);out=Path(out_dir);out.mkdir(parents=True,exist_ok=True)
    allowed={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in data_dir.glob('*.csv')}!=allowed:raise ValueError('strict development allowlist mismatch')
    models={r['recording']:r for r in csv.DictReader(Path(models_path).open()) if r['model']=='viscous'}
    results=[];sources=[];maximum=0.;emax=0.;emin=2.
    for path in sorted(data_dir.glob('*.csv')):
        raw=path.read_bytes();sources.append({'file':path.name,'sha256':hashlib.sha256(raw).hexdigest()})
        data=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in csv.DictReader(raw.decode().splitlines())])
        a=float(models[path.name]['a_gravity']);b=float(models[path.name]['b_viscous'])
        for horizon in [.1,1.6,6.4]:
            shift=int(round(horizon/.01));idx=np.arange(3000,len(data)-shift,10);end=idx+shift
            e,_=encode(data[idx,1],data[idx,2],a);emax=max(emax,float(e.max()));emin=min(emin,float(e.min()))
            theta,w=forecast(data[idx,1],data[idx,2],a,b,horizon)
            ct,cw=cartesian(data[idx,1],data[idx,2],np.array([a,b,0.,0.]),np.full(len(idx),horizon),max(1,int(np.ceil(horizon/.005))))
            discrepancy=max(float(np.max(abs(theta-ct))),float(np.max(abs(w-cw))));maximum=max(maximum,discrepancy)
            for name,pt,pw in [('exact_energy_phase',theta,w),('sine_mechanics',ct,cw),('persistence',data[idx,1],data[idx,2])]:
                results.append(dict(recording=path.name,horizon=horizon,model=name,pairs=len(idx),angle_nrmse=float(np.sqrt(np.mean((pt-data[end,1])**2)/np.mean(data[end,1]**2))),velocity_nrmse=float(np.sqrt(np.mean((pw-data[end,2])**2)/np.mean(data[end,2]**2))),chart_cartesian_max_abs=discrepancy))
    with (out/'scores.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(results[0]),lineterminator='\n');wr.writeheader();wr.writerows(results)
    summary={'stage':'exploratory coordinate-equivalence validation; no new fitting','recordings':15,'holdout_accessed':False,'exclusions':0,'energy_dimensionless_range':[emin,emax],'max_chart_cartesian_absolute_discrepancy':maximum,'numerical_rule_passed':maximum<=1e-5,'models_sha256':hashlib.sha256(Path(models_path).read_bytes()).hexdigest(),'scores':[]}
    for horizon in [.1,1.6,6.4]:
        for model in ['exact_energy_phase','sine_mechanics','persistence']:
            rr=[r for r in results if r['horizon']==horizon and r['model']==model]
            summary['scores'].append(dict(horizon=horizon,model=model,pairs=sum(r['pairs'] for r in rr),angle_nrmse=float(np.mean([r['angle_nrmse'] for r in rr])),velocity_nrmse=float(np.mean([r['velocity_nrmse'] for r in rr]))))
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(out/'provenance.json').write_text(json.dumps(sources,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
    if not summary['numerical_rule_passed']:raise AssertionError('predeclared numerical rule failed')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('data');p.add_argument('models');p.add_argument('out');args=p.parse_args();main(args.data,args.models,args.out)
