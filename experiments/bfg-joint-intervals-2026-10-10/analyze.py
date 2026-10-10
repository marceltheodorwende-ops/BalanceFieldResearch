"""P73 frozen development-only necessary certificates. Never downloads data."""
import argparse, hashlib, json, math
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parent
ALLOW={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
LENGTHS=[.236,.330,.426,.518,.607]
HALFSPANS=[.02,.05,.1,.25,.5,1,2]

def interval(d,e,H,eta):
    den=np.asarray(H)
    if np.any(den<=2*eta): raise ValueError('duration lower bound not positive')
    choices=np.array([(d+sign*2*e)/(den+tau*2*eta) for sign in (-1,1) for tau in (-1,1)])
    return choices.min(axis=0),choices.max(axis=0)
def gap(a,b):return np.maximum(0,np.maximum(a[0]-b[1],b[0]-a[1]))
def certificates(qm,q0,qp,w0,ew,hL,hR,e,eta):
    if not np.allclose(hL,hR,atol=1e-10,rtol=0): raise ValueError("symmetric reported times required for velocity certificate")
    left=interval(q0-qm,e,hL,eta);right=interval(qp-q0,e,hR,eta)
    apos=2*gap(left,right)/(hL+hR+2*eta)
    span=interval(qp-qm,e,hL+hR,eta)
    avel=gap((w0-ew,w0+ew),span)/((hL+hR+2*eta)/4+2*eta)
    return apos,avel

def load_records(data):
    if {p.name for p in data.iterdir() if p.is_file()}!=ALLOW:raise ValueError('exact allowlist required')
    audit={x['file']:x for x in json.loads((ROOT/'data_audit.json').read_text())['files']}
    manifest={Path(x['path']).name:x for x in json.loads((ROOT/'data_manifest.json').read_text())}
    rows={};provenance=[]
    for name in sorted(ALLOW):
        raw=(data/name).read_bytes();sha=hashlib.sha256(raw).hexdigest()
        blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if sha!=audit[name]['sha256'] or blob!=manifest[name]['git_blob_sha']:raise ValueError('data hash mismatch')
        ar=np.genfromtxt(data/name,delimiter=',',names=True)
        t=ar['time'];q=ar['angle'];w=ar['angular_velocity']
        if len(t)!=6000 or not np.all(np.diff(t)>0) or not np.allclose(np.diff(t),.01,atol=1e-12,rtol=0):raise ValueError('grid differs')
        rows[name]=(t,q,w)
        provenance.append({'file':name,'sha256':sha,'git_blob_sha':blob,'rows':len(t)})
    return rows,provenance

def run(data):
    records,provenance=load_records(data);result=[];witnesses=[]
    for name,(t,q,w) in records.items():
        L=LENGTHS[int(name[3])-1];kmax=9.799/L;kmin=9.799*L/(L*L+.02);ew=.0005
        for N in [2000,4000]:
          for epsilon in [0,.0005,.002,.01]:
            e=math.pi/N+.0005+epsilon
            p0=2 if abs(q[0])+e>=math.pi else 1-math.cos(abs(q[0])+e)
            u0=abs(w[0])+ew;V=math.sqrt(u0*u0+2*kmax*p0)
            corridor=bool(abs(q[0])+e<math.pi and p0+u0*u0/(2*kmin)<2)
            for eta in [0,.005]:
                allwindows=[]
                for h in HALFSPANS:
                    n=round(h/.01);idx=np.arange(n,len(t)-n)
                    hl=t[idx]-t[idx-n];hr=t[idx+n]-t[idx]
                    apos,avel=certificates(q[idx-n],q[idx],q[idx+n],w[idx],ew,hl,hr,e,eta)
                    allwindows.append((h,idx,apos,avel))
                for B in [0,.5,2]:
                    env=kmax+2*math.sqrt(kmax)*V+B*V*V
                    rows=[]
                    for h,idx,apos,avel in allwindows:
                        joint=np.maximum(apos,avel);im=int(np.argmax(joint))
                        rows.append({'halfspan':h,'windows':len(idx),'position_rejections':int(np.sum(apos>env+1e-9)),
                            'joint_rejections':int(np.sum(joint>env+1e-9)),
                            'max_position_lower':float(apos.max()),'max_velocity_lower':float(avel.max()),
                            'max_joint_margin':float(joint[im]-env)})
                        if joint[im]>env+1e-9:
                            i=int(idx[im]);n=round(h/.01)
                            witnesses.append({'file':name,'N':N,'epsilon':epsilon,'eta':eta,'B':B,'halfspan':h,
                                'index':i,'reported_times':[float(t[i-n]),float(t[i]),float(t[i+n])],
                                'angles':[float(q[i-n]),float(q[i]),float(q[i+n])],'velocity':float(w[i]),
                                'initial_angle':float(q[0]),'initial_velocity':float(w[0]),'length':L,
                                'margin':float(joint[im]-env),'clock_cos_available':corridor})
                    result.append({'file':name,'N':N,'epsilon':epsilon,'eta':eta,'B':B,'angle_error':e,'speed_ceiling':V,
                        'acceleration_ceiling':env,'clock_cos_available':corridor,'scales':rows})
    # Frozen monotonicity rules: wider boxes and larger beta cannot create rejection.
    lookup={(r['file'],r['N'],r['epsilon'],r['eta'],r['B']):r for r in result}
    for r in result:
        for eps2 in [x for x in [0,.0005,.002,.01] if x>=r['epsilon']]:
            rr=lookup[r['file'],r['N'],eps2,r['eta'],r['B']]
            assert all(y['joint_rejections']<=x['joint_rejections'] for x,y in zip(r['scales'],rr['scales']))
        if r['eta']==0:
            rr=lookup[r['file'],r['N'],r['epsilon'],.005,r['B']]
            assert all(y['joint_rejections']<=x['joint_rejections'] for x,y in zip(r['scales'],rr['scales']))
    summary=[]
    for N in [2000,4000]:
      for eps in [0,.0005,.002,.01]:
       for eta in [0,.005]:
        for B in [0,.5,2]:
            subset=[r for r in result if (r['N'],r['epsilon'],r['eta'],r['B'])==(N,eps,eta,B)]
            reject=[r['file'] for r in subset if any(s['joint_rejections'] for s in r['scales'])]
            summary.append({'N':N,'epsilon':eps,'eta':eta,'B':B,'rejected_records':len(reject),
                'rejected_names':reject,'clock_cos_unavailable_records':sum(not r['clock_cos_available'] for r in subset),
                'position_rejections':sum(s['position_rejections'] for r in subset for s in r['scales']),
                'joint_rejections':sum(s['joint_rejections'] for r in subset for s in r['scales']),
                'windows':sum(s['windows'] for r in subset for s in r['scales'])})
    out={'stage':'reused development necessary conjunction tests; no confirmation','source_commit':'cbf82673641ecd65e902ad5c38a048387649a2a0',
      'records':15,'rows':90000,'record_scenarios':len(result),'summary':summary,'results':result,'monotonicity':'passed','provenance':provenance}
    (ROOT/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    (ROOT/'witnesses.json').write_text(json.dumps(sorted(witnesses,key=lambda x:x['margin'],reverse=True),indent=2)+'\n')
    print(json.dumps({'scenarios':len(result),'worst_witness':max(witnesses,key=lambda x:x['margin']) if witnesses else None,'summary':summary},indent=2))
if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--data-dir',type=Path,required=True);run(parser.parse_args().data_dir)
