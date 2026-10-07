import argparse,csv,hashlib,json
from pathlib import Path
import numpy as np
from bridge import energy,kick,chart

def main(root,models,out):
    root=Path(root);out=Path(out);out.mkdir(parents=True,exist_ok=True)
    allowed={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    if {p.name for p in root.glob('*.csv')}!=allowed:raise ValueError('strict development allowlist')
    coefficients={r['recording']:float(r['a_gravity']) for r in csv.DictReader(Path(models).open()) if r['model']=='viscous'}
    rows=[];provenance=[]
    for path in sorted(root.glob('*.csv')):
        raw=path.read_bytes();provenance.append(dict(file=path.name,sha256=hashlib.sha256(raw).hexdigest()))
        data=np.array([[float(r[k]) for k in ['time','angle','angular_velocity']] for r in csv.DictReader(raw.decode().splitlines())]);idx=np.flatnonzero(data[:,0]>=30)[::10]
        theta=data[idx,1];w=data[idx,2];a=coefficients[path.name];initial=energy(theta,w,a)
        for kappa in [-.05,0.,.05]:
            j=kappa*np.sqrt(a);t,v=kick(theta,w,a,j);final=energy(t,v,a)
            valid=(abs(t)<np.pi)&(final/a<2)
            residual=float(np.max(abs(final-initial-(w*j+j*j/2))))
            rows.append(dict(recording=path.name,kappa=kappa,states=len(idx),chart_valid=int(valid.sum()),chart_invalid=int((~valid).sum()),rest_after=int(np.sum((t==0)&(v==0))),minimum_after_energy=float(np.min(final/a)),maximum_after_energy=float(np.max(final/a)),energy_increases=int(np.sum(final>initial)),energy_decreases=int(np.sum(final<initial)),work_residual=residual))
    with (out/'domain_audit.csv').open('w',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n');wr.writeheader();wr.writerows(rows)
    summary=dict(kind='hypothetical impulse code/domain controls anchored to real passive states; NOT intervention measurements',recordings=15,unique_real_states=4500,control_applications=sum(r['states'] for r in rows),chart_invalid=sum(r['chart_invalid'] for r in rows),maximum_work_residual=max(r['work_residual'] for r in rows),holdout_accessed=False,models_sha256=hashlib.sha256(Path(models).read_bytes()).hexdigest())
    (out/'summary.json').write_text(json.dumps(summary,indent=2)+'\n');(out/'provenance.json').write_text(json.dumps(provenance,indent=2)+'\n');print(json.dumps(summary,indent=2))
    if summary['maximum_work_residual']>1e-12:raise AssertionError('fixed work tolerance failed')
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('data');p.add_argument('models');p.add_argument('out');args=p.parse_args();main(args.data,args.models,args.out)
