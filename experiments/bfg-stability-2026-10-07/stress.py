import sys,csv,json,hashlib
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent.parent
sys.path.insert(0,str(ROOT/'bfg-long-horizon-2026-10-07'))
sys.path.insert(0,str(ROOT/'pendulum-mechanical-identification-2026-10-07'))
from phase_corrected import prepare_corrected,corrected_readout
from identify import forecast
SCENARIOS=['nominal']+[f'{kind}_{sign}' for kind in ['angle','velocity','gravity','damping','clock'] for sign in ['minus','plus']]

def main(data_root,calibration,out_root):
    root=Path(data_root);out=Path(out_root);out.mkdir(exist_ok=True)
    expected={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in root.glob('*.csv')}!=expected:raise ValueError('holdout forbidden')
    coeff={r['recording']:r for r in csv.DictReader(Path(calibration).open()) if r['model']=='viscous'}
    rows=[];basins=[];sources=[]
    for path in sorted(root.glob('*.csv')):
        sources.append(dict(file=path.name,sha256=hashlib.sha256(path.read_bytes()).hexdigest()))
        data=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in csv.DictReader(path.open())]);a=float(coeff[path.name]['a_gravity']);b=float(coeff[path.name]['b_viscous'])
        x=data[3000::10,1];v=data[3000::10,2];ea=v*v/(2*a)+1-np.cos(x)
        basins.append(dict(recording=path.name,states=len(x),certified=int(np.sum((abs(x)<np.pi)&(ea<2)&(b>0))),max_energy_over_a=float(np.max(ea)),viscous=b))
        for horizon in [.1,1.6,6.4]:
            step=round(horizon/.01);i=np.arange(3000,len(data)-step,10);j=i+step;target=data[j,1:];duration=data[j,0]-data[i,0]
            for scenario in SCENARIOS:
                theta=data[i,1].copy();w=data[i,2].copy();aa=a;bb=b;dd=duration.copy()
                if scenario!='nominal':
                    kind,sign=scenario.split('_');s=1 if sign=='plus' else -1
                    if kind=='angle':theta+=s*(np.pi/2000+.0005)
                    if kind=='velocity':w+=s*.0005
                    if kind=='gravity':aa*=1+s*.01
                    if kind=='damping':bb*=1+s*.01
                    if kind=='clock':dd*=1+s*.01
                full=forecast(theta,w,np.array([aa,bb,0.,0.]),dd,max(20,int(np.ceil(float(np.max(dd))/.005))))
                F,K=prepare_corrected(theta,w,aa,bb);phase=corrected_readout(F,K,dd/.1,aa,bb,.1)
                for model,p in [('sine_flow',full),('phase_observable',phase)]:
                    rows.append(dict(recording=path.name,horizon_seconds=horizon,scenario=scenario,model=model,pairs=len(i),angle=float(np.sqrt(np.mean((p[0]-target[:,0])**2)/np.mean(target[:,0]**2))),velocity=float(np.sqrt(np.mean((p[1]-target[:,1])**2)/np.mean(target[:,1]**2)))))
    with (out/'scores.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');wr.writeheader();wr.writerows(rows)
    agg=[]
    for h in [.1,1.6,6.4]:
        for model in ['sine_flow','phase_observable']:
            for scenario in SCENARIOS:
                r=[z for z in rows if z['horizon_seconds']==h and z['model']==model and z['scenario']==scenario]
                agg.append(dict(horizon_seconds=h,model=model,scenario=scenario,pairs=sum(z['pairs'] for z in r),angle=float(np.mean([z['angle'] for z in r])),velocity=float(np.mean([z['velocity'] for z in r]))))
    summary=dict(stage='exploratory deterministic one-factor stress on real development data',holdout_accessed=False,aggregate=agg,basins=basins,total_basin_states=sum(r['states'] for r in basins),total_certified_states=sum(r['certified'] for r in basins))
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(out/'provenance.json').write_text(json.dumps(dict(source_commit='cbf82673641ecd65e902ad5c38a048387649a2a0',source_files=sources,calibration_sha256=hashlib.sha256(Path(calibration).read_bytes()).hexdigest()),indent=2)+'\n')
    print('basin',summary['total_certified_states'],summary['total_basin_states'])
    for model in ['sine_flow','phase_observable']:
        r=[z for z in agg if z['horizon_seconds']==6.4 and z['model']==model];print(model,'nominal',r[0],'worst angle',max(r,key=lambda z:z['angle']),'worst velocity',max(r,key=lambda z:z['velocity']))
if __name__=='__main__':main(*sys.argv[1:])
