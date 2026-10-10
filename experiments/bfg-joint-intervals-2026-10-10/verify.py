"""Independent exact boxes and 80-digit nearest real certificate check."""
import json,random
from fractions import Fraction as F
from pathlib import Path
import mpmath as mp
R=Path(__file__).resolve().parent;rng=random.Random(7301)
for _ in range(200):
    hl=F(rng.randrange(1,20),10);hr=F(rng.randrange(1,20),10);e=F(1,100)
    q=[F(rng.randrange(-100,100),100) for _ in range(3)]
    values=[]
    for signs in [(-1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,1,1),(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)]:
        z=[v+sg*e for v,sg in zip(q,signs)];values.append((z[2]-z[1])/hr-(z[1]-z[0])/hl)
    lo,hi=min(values),max(values)
    residual=(q[2]-q[1])/hr-(q[1]-q[0])/hl
    radius=2*e*(1/hl+1/hr)
    assert (lo,hi)==(residual-radius,residual+radius)
    best=F(0) if lo<=0<=hi else min(abs(lo),abs(hi))
    assert best==max(F(0),abs(residual)-radius)
# No real rejection exists: independently verify the most stringent nonrejection.
mp.mp.dps=80
r=json.loads((R/'results.json').read_text());best=None
for case in r['results']:
    for sc in case['scales']:
        if best is None or sc['max_joint_margin']>best[1]['max_joint_margin']:best=(case,sc)
case,sc=best;h=sc['halfspan'];n=round(h/.01)
import csv,argparse,hashlib
from analyze import ALLOW
parser=argparse.ArgumentParser();parser.add_argument('--data-dir',type=Path,required=True);data=parser.parse_args().data_dir
assert {p.name for p in data.iterdir() if p.is_file()}==ALLOW
assert case['file'] in ALLOW
audit={x['file']:x for x in json.loads((R/'data_audit.json').read_text())['files']}
assert hashlib.sha256((data/case['file']).read_bytes()).hexdigest()==audit[case['file']]['sha256']
with (data/case['file']).open() as f:
    rows=list(csv.DictReader(f))
x=lambda z:mp.mpf(str(z))
e=mp.pi/case['N']+x('.0005')+x(case['epsilon']);eta=x(case['eta']);ew=x('.0005')
L=x([.236,.330,.426,.518,.607][int(case['file'][3])-1]);k=x('9.799')/L
qinit=x(rows[0]['angle']);winit=x(rows[0]['angular_velocity']);p0=1-mp.cos(abs(qinit)+e)
V=mp.sqrt((abs(winit)+ew)**2+2*k*p0);env=k+2*mp.sqrt(k)*V+x(case['B'])*V**2
# Independently loop the relevant worst-case scale using decimal source strings.
def iv(d,H):
    terms=[(d+sg*2*e)/(H+ss*2*eta) for sg in [-1,1] for ss in [-1,1]]
    return min(terms),max(terms)
def distance(a,b):return max(mp.mpf(0),a[0]-b[1],b[0]-a[1])
maxmargin=-mp.inf;witness=None
for i in range(n,len(rows)-n):
    qm,q0,qp=[x(rows[j]['angle']) for j in [i-n,i,i+n]]
    tl,t0,tr=[x(rows[j]['time']) for j in [i-n,i,i+n]];H=tr-tl
    ap=2*distance(iv(q0-qm,t0-tl),iv(qp-q0,tr-t0))/(H+2*eta)
    ww=x(rows[i]['angular_velocity'])
    av=distance((ww-ew,ww+ew),iv(qp-qm,H))/((H+2*eta)/4+2*eta)
    margin=max(ap,av)-env
    if margin>maxmargin:maxmargin=margin;witness={'index':i,'times':[str(z) for z in [tl,t0,tr]],'angles':[str(z) for z in [qm,q0,qp]],'velocity':str(ww),'Apos':str(ap),'Avel':str(av)}
error=abs(maxmargin-x(sc['max_joint_margin']));assert error<mp.mpf('1e-8')
assert maxmargin<=0
out={'status':'passed','exact_box_cases':200,'precision_digits':80,'nearest_real_case':{k:case[k] for k in ['file','N','epsilon','eta','B']},
'halfspan':h,'margin':str(maxmargin),'floating_agreement_error':str(error),'witness':witness,'no_rejections_to_recheck':True}
(R/'verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
