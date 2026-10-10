"""Independent direct-polynomial exact check of worst strict full path."""
import argparse,csv,hashlib,json
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
ROOT=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('--data-dir',type=Path,required=True);data=p.parse_args().data_dir
allow={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
assert {x.name for x in data.iterdir() if x.is_file()}==allow
results=json.loads((ROOT/'results.json').read_text());cases=results['results'];assert 0<len(cases)<=120 # Partial run explicitly reported; no full-grid completion implied.
certs=json.loads((ROOT/'certificates.json').read_text());inner=[x for x in certs if x['kind']=='inner'];assert inner
selected=min(inner,key=lambda x:x['certificate']['minimum_normalized_margin']);case=cases[selected['case']];assert case['file'] in allow
raw=(data/case['file']).read_bytes();audit={x['file']:x for x in json.loads((ROOT/'data_audit.json').read_text())['files']};assert hashlib.sha256(raw).hexdigest()==audit[case['file']]['sha256']
with (data/case['file']).open() as f:rows=list(csv.DictReader(f))
t=[F(x['time']) for x in rows];q=[F(x['angle']) for x in rows];w=[F(x['angular_velocity']) for x in rows]
knots=list(range(0,6000,5))+[5999];K=len(knots);state=list(map(F,selected['certificate']['states']));qq=state[:K];ww=state[K:]
# Input envelope helper uses exact elementary enclosures, not the LP/matrix builder.
from core import parameters
e,A,corridor=parameters(q[0],w[0],list(map(F,['.236','.330','.426','.518','.607']))[int(case['file'][3])-1],case['N'],F(str(case['ew'])),F(case['B']))
e=e[0];acc=A[0];ew=F(str(case['ew']));maxq=F(0);maxw=F(0);maxa=F(0);seg=0
for i,ti in enumerate(t):
 while seg<K-2 and i>=knots[seg+1]:seg+=1
 h=t[knots[seg+1]]-t[knots[seg]];u=(ti-t[knots[seg]])/h
 # Expanded Hermite polynomial with direct scalar derivative.
 c0=qq[seg];c1=h*ww[seg];c2=3*(qq[seg+1]-qq[seg])-h*(2*ww[seg]+ww[seg+1]);c3=2*(qq[seg]-qq[seg+1])+h*(ww[seg]+ww[seg+1])
 pv=c0+c1*u+c2*u*u+c3*u**3;dv=(c1+2*c2*u+3*c3*u*u)/h
 maxq=max(maxq,abs(pv-q[i]));maxw=max(maxw,abs(dv-w[i]))
for j in range(K-1):
 h=t[knots[j+1]]-t[knots[j]]
 c2=3*(qq[j+1]-qq[j])-h*(2*ww[j]+ww[j+1]);c3=2*(qq[j]-qq[j+1])+h*(ww[j]+ww[j+1])
 maxa=max(maxa,abs(2*c2/h**2),abs((2*c2+6*c3)/h**2))
assert maxq<e and maxw<ew and maxa<acc
mq=e-maxq;mw=ew-maxw
# Simple conservative mollifier radius: delta <= mq/A and mw/A, with tiny cap.
delta=min(F(1,10**6),mw/(2*acc),mq/(2*acc))
assert acc*delta<mw and acc*delta*delta/2<mq
mp.mp.dps=80
m=lambda f:mp.mpf(f.numerator)/f.denominator
L=mp.mpf(['.236','.330','.426','.518','.607'][int(case['file'][3])-1]);kap=mp.mpf('9.799')/L
et=mp.pi/case['N']+mp.mpf('.0005');v=mp.sqrt((abs(m(w[0]))+m(ew))**2+2*kap*(1-mp.cos(abs(m(q[0]))+et)))
at=kap+2*mp.sqrt(kap)*v+case['B']*v*v
el,al,c=parameters(q[0],w[0],F(str(L)),case['N'],ew,F(case['B']))
assert m(el[0])<et<m(el[1]) and m(al[0])<at<m(al[1])
def f(z):return 2*z*z/((1+z)**2*(1+z*z))
equilibria=[]
for d in ['.1','.3','.6']:
 dd=mp.mpf(d);lo=mp.mpf(0);hi=mp.mpf('.25')
 for _ in range(250):
  mid=(lo+hi)/2
  if f(mid+dd)>mid:lo=mid
  else:hi=mid
 y=(lo+hi)/2;z=y+dd
 ll=4*z*(1-z**3)/((1+z)**3*(1+z*z)**2);lt=2*z*(1-z)/((1+z)**3*(1+z*z))
 assert ll>2*lt>0
 equilibria.append({'d':d,'fixed_y':str(y),'return_longitudinal':str(ll),'return_transverse':str(lt),'fixed_residual':str(abs(f(z)-y))})
out={'status':'passed','completed_cases':len(cases),'planned_cases':120,'full_grid_complete':len(cases)==120,'independent_full_path_case':selected['case'],'case':case,'observations_checked':6000,'segments_checked':K-1,
 'max_angle_error':float(maxq),'angle_radius_lower':float(e),'max_velocity_error':float(maxw),'velocity_radius':float(ew),
 'max_continuous_acceleration':float(maxa),'acceleration_radius_lower':float(acc),'exact_angle_margin':str(mq),'exact_velocity_margin':str(mw),
 'certified_mollifier_radius_seconds':str(delta),'input_envelopes_80digit_check':True,'canonical_equilibria_80digits':equilibria}
(ROOT/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
(ROOT/'selected_path.json').write_text(json.dumps(selected,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items() if k not in ['canonical_equilibria_80digits','case','exact_angle_margin','exact_velocity_margin']}))
