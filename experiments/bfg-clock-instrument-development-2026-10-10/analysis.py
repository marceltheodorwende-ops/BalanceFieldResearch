"""P69 bounded real-development experiment. Only fifteen allowed attempt-1 CSVs."""
import csv, hashlib, json, sys
from pathlib import Path
import numpy as np
from scipy.optimize import minimize_scalar

ROOT=Path(__file__).parent
MODELS=['clock_cos','viscous','mixed_drag']
LENGTHS=np.array([.236,.330,.426,.518,.607]); GRAVITY=9.799
EPS=.0005; WIDTH=.5; DT=.01
HORIZONS=[.1,.5,1.,2.,5.,10.,20.,29.99]

def damping_fit(D,y,upper):
    """Exact box-constrained one/two-column LS by active-face enumeration."""
    if D.shape[1]==1:
        zz=float(D[:,0]@D[:,0])
        a=np.clip(float(D[:,0]@y)/zz,0,upper) if zz else 0.
        return np.array([a])
    candidates=[]
    x=np.linalg.lstsq(D,y,rcond=None)[0]
    if 0<=x[0]<=upper and x[1]>=0: candidates.append(x)
    for a in [0.,upper]:
        b=max(0.,float(D[:,1]@(y-a*D[:,0]))/float(D[:,1]@D[:,1])) if np.any(D[:,1]) else 0.
        candidates.append(np.array([a,b]))
    zz=float(D[:,0]@D[:,0])
    a=np.clip(float(D[:,0]@y)/zz,0,upper) if zz else 0.
    candidates.append(np.array([a,0.]))
    return min(candidates,key=lambda x:float(np.sum((D@x-y)**2)))

def moments(data,start,stop,coarse=False):
    out=[]
    for i in range(start,stop,50):
        if i+50>=len(data): break
        z=data[i:i+51:2 if coarse else 1]; t=z[:,0]-z[0,0]
        phi=np.sin(np.pi*t/WIDTH)**2
        phip=np.pi/WIDTH*np.sin(2*np.pi*t/WIDTH)
        Q,W=z[:,1],z[:,2]
        integ=lambda f:float(np.trapezoid(f,t))
        out.append([integ(W*phip),integ(np.sin(Q)*phi),integ(W*np.cos(Q/2)*phi),
                    integ(W*phi),integ(np.abs(W)*W*phi)])
    return np.array(out)

def vector_rhs(z,k,g,b,cosmask):
    Q,W=z[:,0],z[:,1]
    factor=np.where(cosmask,np.cos(Q/2),1.)
    return np.column_stack((W,-k*np.sin(Q)-g*factor*W-b*np.abs(W)*W))

def integrate(z0,k,g,b,cosmask,step,duration=29.99):
    """Vectorized fixed-work RK4: no asynchronous/background workload."""
    count=int(round(duration/step)); every=int(round(DT/step)); z=z0.copy()
    rows=[z.copy()]
    for j in range(count):
        f1=vector_rhs(z,k,g,b,cosmask)
        f2=vector_rhs(z+step*f1/2,k,g,b,cosmask)
        f3=vector_rhs(z+step*f2/2,k,g,b,cosmask)
        f4=vector_rhs(z+step*f3,k,g,b,cosmask)
        z+=step*(f1+2*f2+2*f3+f4)/6
        if (j+1)%every==0: rows.append(z.copy())
    return np.array(rows)

def max_potential(Q):
    a,b=Q-EPS,Q+EPS
    val=max(1-np.cos(a),1-np.cos(b))
    if np.ceil((a-np.pi)/(2*np.pi))<=np.floor((b-np.pi)/(2*np.pi)): val=2.
    return float(val)

def kinematic(data,k,g,b,dmax,common_kmin=None):
    rows=[]
    for i in range(0,len(data)-50,50):
        Q0,W0=data[i,1:3]; V=max_potential(Q0)
        E=(abs(W0)+EPS)**2/2+k*V
        admissible=abs(Q0)+EPS<np.pi and E<2*k
        if common_kmin is not None:
            admissible=admissible and V+(abs(W0)+EPS)**2/(2*common_kmin)<2
        t=data[i:i+51,0]; W=data[i:i+51,2]
        residual=float(data[i+50,1]-Q0-np.trapezoid(W,t))
        if admissible:
            vmax=np.sqrt(2*E); accel=k+g*vmax+b*vmax*vmax
            M2=k*vmax+g*(dmax*vmax*vmax+accel)+2*b*vmax*accel
            quad=WIDTH*DT*DT*M2/12
            bound=2*EPS+WIDTH*EPS+quad
            extra_angle=max(0.,(abs(residual)-WIDTH*EPS-quad)/2-EPS)
        else: bound=extra_angle=None
        rows.append(dict(start=float(t[0]),residual=residual,bound=bound,
          violation=bool(admissible and abs(residual)>bound),extra_angle_allowance=extra_angle,
          certificate_available=bool(admissible)))
    return rows

def main(data_dir,manifest_path):
    allowed={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
    data_dir=Path(data_dir)
    assert {p.name for p in data_dir.glob('*.csv')}==allowed,'Refusing non-development directory'
    manifest=json.loads(Path(manifest_path).read_text())
    assert {Path(x['path']).name for x in manifest}==allowed
    records=[]; provenance=[]
    for item in sorted(manifest,key=lambda x:x['path']):
        path=data_dir/Path(item['path']).name; raw=path.read_bytes()
        blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        assert blob==item['git_blob_sha']
        data=np.loadtxt(path,delimiter=',',skiprows=1,usecols=(0,1,2))
        assert data.shape==(6000,3) and np.max(abs(data[:,0]-np.arange(6000)*DT))<1e-12
        li=int(path.name[3])-1
        records.append(dict(file=path.name,length=float(LENGTHS[li]),data=data,
          train=moments(data,0,3000),test=moments(data,3000,5950),coarse=moments(data,0,3000,True)))
        provenance.append(dict(file=path.name,source_commit=item['source_commit'],
          git_blob_sha=blob,sha256=hashlib.sha256(raw).hexdigest()))
    fitted=[]; profiles=[]
    for model in MODELS:
        def fit(lam,coarse=False):
            params=[]; losses=[]
            for rec in records:
                m=rec['coarse' if coarse else 'train']; fine=rec['train']
                k=GRAVITY*rec['length']/(rec['length']**2+lam)
                cols=[2] if model=='clock_cos' else [3,4] if model=='mixed_drag' else [3]
                D=m[:,cols]; y=m[:,0]-k*m[:,1]
                damp=damping_fit(D,y,2*np.sqrt(k)*(1-1e-10))
                normalizer=max(float(np.mean(fine[:,0]**2)),1e-12)
                losses.append(float(np.mean((D@damp-y)**2))/normalizer)
                params.append(dict(model=model,file=rec['file'],kappa=float(k),gamma=float(damp[0]),
                  beta=float(damp[1]) if model=='mixed_drag' else 0.,
                  gamma_zero=bool(damp[0]==0.),train_normalized_loss=losses[-1]))
            return float(np.mean(losses)),params
        grid=np.linspace(0,.02,21)
        candidates=[(float(x),fit(float(x))[0]) for x in grid]
        opt=minimize_scalar(lambda x:fit(x)[0],bounds=(0.,.02),method='bounded',options={'xatol':1e-10})
        assert opt.success
        candidates.append((float(opt.x),float(opt.fun)))
        lam,best=min(candidates,key=lambda pair:pair[1]); loss,pars=fit(lam)
        coarse_loss,coarse_params=fit(lam,True)
        for j,par in enumerate(pars):
            par['lambda']=lam
            m=records[j]['test']; cols=[2] if model=='clock_cos' else [3,4] if model=='mixed_drag' else [3]
            coeff=np.array([par['gamma'],par['beta']]) if model=='mixed_drag' else np.array([par['gamma']])
            residual=m[:,0]-par['kappa']*m[:,1]-m[:,cols]@coeff
            par['temporal_weak_normalized_loss']=float(np.mean(residual**2))/max(float(np.mean(records[j]['train'][:,0]**2)),1e-12)
            par['coarse_gamma_change']=float(coarse_params[j]['gamma']-par['gamma'])
            par['coarse_beta_change']=float(coarse_params[j]['beta']-par['beta'])
            fitted.append(par)
        acceptable=[x for x,f in candidates if f<=best*1.01]
        profiles.append(dict(model=model,lambda_best=lam,loss=loss,coarse_loss_at_same_lambda=coarse_loss,
          sensitivity_1percent_range=[min(acceptable),max(acceptable)],profile=candidates))
    # Stable order: model then file, no reshaping ambiguity.
    z0=np.array([r['data'][3000,1:3] for model in MODELS for r in records])
    k=np.array([p['kappa'] for p in fitted]); g=np.array([p['gamma'] for p in fitted]); b=np.array([p['beta'] for p in fitted])
    mask=np.array([p['model']=='clock_cos' for p in fitted])
    coarse=integrate(z0,k,g,b,mask,.005); fine=integrate(z0,k,g,b,mask,.0025)
    diff=np.max(abs(coarse-fine),axis=(0,1)); repairs=[]
    if diff[0]>1e-5 or diff[1]>1e-4:
        refined=integrate(z0,k,g,b,mask,.00125)
        repairs.append(dict(previous_steps=[.005,.0025],previous_discrepancy=diff.tolist()))
        diff=np.max(abs(fine-refined),axis=(0,1)); fine=refined
    assert diff[0]<=1e-5 and diff[1]<=1e-4,'Numerical criterion failed after bounded repair'
    scores=[]; forecast_nodes=[]; all_kin=[]; ident=[]
    for j,par in enumerate(fitted):
        rec=records[j%15]; data=rec['data']; observed=data[3000:6000,1:3]
        y=fine[:,j]; E=.5*y[:,1]**2+par['kappa']*(1-np.cos(y[:,0]))
        corridor=bool(E[0]<2*par['kappa'] and abs(y[0,0])<np.pi)
        if par['model']!='clock_cos' or corridor:
            assert np.max(np.diff(E))<1e-8
        par['forecast_max_energy_increase']=float(max(0.,np.max(np.diff(E))))
        par['forecast_energy_corridor']=corridor
        par['forecast_max_abs_angle']=float(np.max(abs(y[:,0])))
        for horizon in HORIZONS:
            n=int(round(horizon/DT)); error=y[1:n+1]-observed[1:n+1]
            rmse=np.sqrt(np.mean(error**2,axis=0))
            persistence=np.sqrt(np.mean((observed[1:n+1]-observed[0])**2,axis=0))
            ratio=np.divide(rmse,persistence,out=np.full(2,np.nan),where=persistence>1e-12)
            assert np.all(np.isfinite(ratio))
            scores.append(dict(model=par['model'],file=par['file'],horizon=horizon,
              angle_rmse=float(rmse[0]),velocity_rmse=float(rmse[1]),
              angle_persistence_ratio=float(ratio[0]),velocity_persistence_ratio=float(ratio[1])))
            forecast_nodes.append(dict(model=par['model'],file=par['file'],horizon=horizon,
              predicted_angle=float(y[n,0]),predicted_velocity=float(y[n,1])))
        ks=kinematic(data,par['kappa'],par['gamma'],par['beta'],.5 if par['model']=='clock_cos' else 0.)
        all_kin.extend(dict(model=par['model'],file=par['file'],**row) for row in ks)
    family=[]
    for rec in records:
        kmax=GRAVITY/rec['length']; kmin=GRAVITY*rec['length']/(rec['length']**2+.02)
        rows=kinematic(rec['data'],kmax,2*np.sqrt(kmax),0.,.5,common_kmin=kmin)
        family.extend(dict(file=rec['file'],**row) for row in rows)
        D=rec['train'][:,[2,3]]; norms=np.linalg.norm(D,axis=0)
        sv=np.linalg.svd(D/norms,compute_uv=False) if np.all(norms>0) else np.array([0.,0.])
        ident.append(dict(file=rec['file'],calibration_max_abs_angle=float(np.max(abs(rec['data'][:3001,1]))),
          normalized_clock_viscous_singular_values=sv.tolist(),condition=float(sv[0]/sv[-1]) if sv[-1]>0 else None,
          relative_damping_column_difference=float(np.linalg.norm(D[:,0]-D[:,1])/norms[1])))
    summaries=[]
    for h in HORIZONS:
        for model in MODELS:
            rows=[x for x in scores if x['horizon']==h and x['model']==model]
            base=[x for x in scores if x['horizon']==h and x['model']=='viscous']
            summaries.append(dict(model=model,horizon=h,
              median_angle_ratio=float(np.median([x['angle_persistence_ratio'] for x in rows])),
              median_velocity_ratio=float(np.median([x['velocity_persistence_ratio'] for x in rows])),
              angle_rmse_range=[min(x['angle_rmse'] for x in rows),max(x['angle_rmse'] for x in rows)],
              velocity_rmse_range=[min(x['velocity_rmse'] for x in rows),max(x['velocity_rmse'] for x in rows)],
              angle_wins_vs_viscous=sum(a['angle_rmse']<v['angle_rmse'] for a,v in zip(rows,base)),
              velocity_wins_vs_viscous=sum(a['velocity_rmse']<v['velocity_rmse'] for a,v in zip(rows,base))))
    failures={m:sum(x['violation'] for x in all_kin if x['model']==m) for m in MODELS}
    result=dict(stage='P69 exploratory direct-instrument bridge; no BFG event calibration',
      protocol_sha256=hashlib.sha256((ROOT/'PROTOCOL.md').read_bytes()).hexdigest(),
      source_files=provenance,models=MODELS,fitted_coefficients=dict(clock_cos=16,viscous=16,mixed_drag=31),
      params=fitted,profiles=profiles,prediction_summary=summaries,identifiability=ident,
      integration_steps=[.005,.0025],integration_max_discrepancy=diff.tolist(),integration_repairs=repairs,
      kinematic_violations=failures,family_clock_kinematic_violations=sum(x['violation'] for x in family),
      family_unavailable_certificates=sum(not x['certificate_available'] for x in family),
      holdout_accessed=False,canonical_events_identified=False,physical_uncertainty_certified=False)
    for name,rows in [('scores.csv',scores),('forecast_nodes.csv',forecast_nodes),('kinematic.csv',all_kin),('family_kinematic.csv',family)]:
        with (ROOT/name).open('w',newline='') as f:
            writer=csv.DictWriter(f,fieldnames=list(rows[0])); writer.writeheader();writer.writerows(rows)
    (ROOT/'results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(dict(recordings=len(records),models=MODELS,kinematic_violations=failures,
      family_violations=result['family_clock_kinematic_violations'],family_unavailable=result['family_unavailable_certificates'],
      lambda_best={x['model']:x['lambda_best'] for x in profiles},
      integration_difference=diff.tolist(),long_horizon=[x for x in summaries if x['horizon']==29.99])))

if __name__=='__main__':
    main(sys.argv[1],sys.argv[2])
