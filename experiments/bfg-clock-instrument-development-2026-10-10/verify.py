"""Independent certificate and real-path verification, limited to allowed files."""
import csv,hashlib,json,sys
from pathlib import Path
import numpy as np
import mpmath as mp
from scipy.integrate import solve_ivp

root=Path(__file__).parent; data_dir=Path(sys.argv[1])
allowed={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
assert {p.name for p in data_dir.glob('*.csv')}==allowed
r=json.loads((root/'results.json').read_text())
assert hashlib.sha256((root/'PROTOCOL.md').read_bytes()).hexdigest()==r['protocol_sha256']
sources={x['file']:x for x in r['source_files']}
data={}
for name in sorted(allowed):
    raw=(data_dir/name).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==sources[name]['sha256']
    data[name]=np.loadtxt(data_dir/name,delimiter=',',skiprows=1,usecols=(0,1,2))
family=list(csv.DictReader((root/'family_kinematic.csv').open()))
errors=[]; violations=[]; summaries=[]
for row in family:
    z=data[row['file']]; i=int(round(float(row['start'])*100))
    L=[.236,.330,.426,.518,.607][int(row['file'][3])-1]
    kmax=9.799/L;kmin=9.799*L/(L*L+.02);gmax=2*np.sqrt(kmax)
    Q,W=z[i,1:3]; eps=.0005
    assert abs(Q)+eps<np.pi
    V=max(1-np.cos(Q-eps),1-np.cos(Q+eps))
    assert V+(abs(W)+eps)**2/(2*kmin)<2
    vmax=np.sqrt((abs(W)+eps)**2+2*kmax*V)
    accel=kmax+gmax*vmax
    bound=.001+.5*eps+.5*.01**2*(kmax*vmax+gmax*(.5*vmax*vmax+accel))/12
    # Explicit weights, independently of np.trapezoid and reported timestamps.
    integ=.01*(z[i,2]/2+sum(z[i+1:i+50,2])+z[i+50,2]/2)
    residual=float(z[i+50,1]-z[i,1]-integ)
    errors.append(max(abs(bound-float(row['bound'])),abs(residual-float(row['residual']))))
    bad=abs(residual)>bound
    assert bad==(row['violation']=='True')
    if bad: violations.append(row)
assert len(violations)==r['family_clock_kinematic_violations']==35
assert max(errors)<1e-12
mp.mp.dps=60
excess=[]
for row in violations:
    z=data[row['file']]; i=int(round(float(row['start'])*100))
    length=mp.mpf(['.236','.330','.426','.518','.607'][int(row['file'][3])-1])
    exact=lambda value:mp.mpf(format(value,'.3f'))
    q0,w0=exact(z[i,1]),exact(z[i,2]);eps=mp.mpf('.0005')
    k=mp.mpf('9.799')/length;g=2*mp.sqrt(k)
    potential=max(1-mp.cos(q0-eps),1-mp.cos(q0+eps))
    vmax=mp.sqrt((abs(w0)+eps)**2+2*k*potential)
    M2=k*vmax+g*(vmax*vmax/2+k+g*vmax)
    bound=2*eps+eps/2+mp.mpf('.5')*mp.mpf('.01')**2*M2/12
    trap=mp.mpf('.01')*(exact(z[i,2])/2+sum(exact(v) for v in z[i+1:i+50,2])+exact(z[i+50,2])/2)
    resid=exact(z[i+50,1])-q0-trap
    gap=abs(resid)-bound
    assert gap>0
    excess.append(float(gap))
for name in sorted(allowed):
    rows=[x for x in family if x['file']==name]
    summaries.append(dict(file=name,windows=len(rows),family_violations=sum(x['violation']=='True' for x in rows),
      maximum_abs_residual=max(abs(float(x['residual'])) for x in rows),
      maximum_residual_bound_ratio=max(abs(float(x['residual']))/float(x['bound']) for x in rows)))
with (root/'family_violations.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=list(violations[0]));w.writeheader();w.writerows(violations)
nodes=list(csv.DictReader((root/'forecast_nodes.csv').open())); controls=[]
# Fixed first lexical record: independent ODE method at all eight declared horizons.
for model in r['models']:
    par=next(x for x in r['params'] if x['model']==model and x['file']=='len1_cond1_1.csv')
    selected=[x for x in nodes if x['model']==model and x['file']==par['file']]
    times=np.array([float(x['horizon']) for x in selected]);initial=data[par['file']][3000,1:3]
    def rhs(t,z):
        Q,W=z;factor=np.cos(Q/2) if model=='clock_cos' else 1.
        return [W,-par['kappa']*np.sin(Q)-par['gamma']*factor*W-par['beta']*abs(W)*W]
    sol=solve_ivp(rhs,[0,29.99],initial,t_eval=times,method='DOP853',rtol=2e-11,atol=2e-12)
    assert sol.success
    ref=np.array([[float(x['predicted_angle']),float(x['predicted_velocity'])] for x in selected])
    error=np.max(abs(sol.y.T-ref),axis=0)
    assert error[0]<1e-5 and error[1]<1e-4
    controls.append(dict(model=model,file=par['file'],angle_error=float(error[0]),velocity_error=float(error[1])))
out=dict(source_hashes_verified=15,protocol_hash_unchanged=True,family_windows_verified=len(family),
    family_violation_count=len(violations),family_numeric_max_discrepancy=max(errors),
    high_precision_countercertificates=len(excess),high_precision_decimal_digits=60,
    minimum_countercertificate_excess=min(excess),
    per_record_family_certificates=summaries,independent_real_forecasts=controls,
    scope='Conditional direct-instrument hypothesis, reused development records only')
(root/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
