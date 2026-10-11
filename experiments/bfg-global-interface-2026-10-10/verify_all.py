"""Independent exact scalar Hermite verification of every accepted full path.
No sparse LP, matrix builder, or numerical solver is used for the trajectory check.
"""
import csv,json,hashlib,argparse
from pathlib import Path
from fractions import Fraction as F
from core import parameters
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--data-dir',type=Path,required=True);data=p.parse_args().data_dir
allow={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
assert {x.name for x in data.iterdir() if x.is_file()}==allow
res=json.loads((ROOT/'results.json').read_text());cases=res['results'];assert len(cases)==120
assert len({(x['file'],x['N'],x['ew'],x['B']) for x in cases})==120
assert all(x['solver_method']=='highs-ipm' for x in cases)
audit={x['file']:x for x in json.loads((ROOT/'data_audit.json').read_text())['files']}
certs=json.loads((ROOT/'certificates.json').read_text());assert not any(x['kind']=='outer' for x in certs), 'extend independent weighted-inequality checker if a new outer exclusion exists'
assert {x['case'] for x in certs}=={i for i,x in enumerate(cases) if x['inner_status']=='strict_path_exact'}
checks=[]
for saved in certs:
 case=cases[saved['case']];name=case['file'];assert name in allow
 raw=(data/name).read_bytes();assert hashlib.sha256(raw).hexdigest()==audit[name]['sha256']
 with (data/name).open() as f: rows=list(csv.DictReader(f))
 t=[F(x['time']) for x in rows];q=[F(x['angle']) for x in rows];w=[F(x['angular_velocity']) for x in rows];assert len(t)==6000
 ks=list(range(0,6000,5))+[5999];K=len(ks);state=list(map(F,saved['certificate']['states']));assert len(state)==2*K
 qq,ww=state[:K],state[K:];e,A,_=parameters(q[0],w[0],list(map(F,['.236','.330','.426','.518','.607']))[int(name[3])-1],case['N'],F(str(case['ew'])),F(case['B']));e,A=e[0],A[0];ew=F(str(case['ew']))
 maxq=maxw=maxa=F(0);seg=0
 for i,ti in enumerate(t):
  while seg<K-2 and i>=ks[seg+1]:seg+=1
  h=t[ks[seg+1]]-t[ks[seg]];u=(ti-t[ks[seg]])/h
  c0=qq[seg];c1=h*ww[seg];c2=3*(qq[seg+1]-qq[seg])-h*(2*ww[seg]+ww[seg+1]);c3=2*(qq[seg]-qq[seg+1])+h*(ww[seg]+ww[seg+1])
  Q=c0+c1*u+c2*u*u+c3*u**3;W=(c1+2*c2*u+3*c3*u*u)/h
  maxq=max(maxq,abs(Q-q[i]));maxw=max(maxw,abs(W-w[i]))
 for j in range(K-1):
  h=t[ks[j+1]]-t[ks[j]];c2=3*(qq[j+1]-qq[j])-h*(2*ww[j]+ww[j+1]);c3=2*(qq[j]-qq[j+1])+h*(ww[j]+ww[j+1])
  maxa=max(maxa,abs(2*c2/h**2),abs((2*c2+6*c3)/h**2))
 mq,mw,ma=e-maxq,ew-maxw,A-maxa;assert min(mq,mw,ma)>0
 # Start with a stated time radius; halve until both dimensionally typed bounds hold.
 delta=F(1,10**6)
 while A*delta>=mw or A*delta*delta/2>=mq:delta/=2
 checks.append({'case':saved['case'],'file':name,'observations':6000,'segments':1200,'exact_angle_margin':str(mq),'exact_velocity_margin':str(mw),'exact_acceleration_margin':str(ma),'mollifier_radius_seconds':str(delta),'max_angle_error':float(maxq),'max_velocity_error':float(maxw),'max_continuous_acceleration':float(maxa),'sha256_certificate':hashlib.sha256(json.dumps(saved,sort_keys=True,separators=(',',':')).encode()).hexdigest()})
old=json.loads((ROOT/'interim/results.json').read_text())['results'];differences=[]
for i,a in enumerate(old):
 b=cases[i]
 assert (a['file'],a['N'],a['ew'],a['B'])==(b['file'],b['N'],b['ew'],b['B'])
 for field in ['outer_status','inner_status']:
  if a[field]!=b[field]:differences.append({'case':i,'field':field,'original':a[field],'ipm':b[field]})
out={'status':'passed','grid_cases':120,'paths_checked':len(checks),'observation_checks':6000*len(checks),'continuous_segment_checks':1200*len(checks),'original_cases_compared':len(old),'algorithm_status_disagreements':differences,'checks':checks}
(ROOT/'verification_all.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}),flush=True)
