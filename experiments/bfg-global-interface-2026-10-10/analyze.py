"""P74 finite development analysis; no data download, exact allowlist/hashes."""
import argparse,csv,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
import numpy as np
from core import System,parameters
ROOT=Path(__file__).resolve().parent
ALLOW={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
LENGTHS=list(map(F,['.236','.330','.426','.518','.607']))
def run(data):
    if {p.name for p in data.iterdir() if p.is_file()}!=ALLOW:raise ValueError('exact attempt1 allowlist required')
    audit={x['file']:x for x in json.loads((ROOT/'data_audit.json').read_text())['files']}
    manifest={Path(x['path']).name:x for x in json.loads((ROOT/'data_manifest.json').read_text())}
    results=[];certs=[];provenance=[];started=time.monotonic();systems=None
    resume=0
    if (ROOT/'results.json').exists():
        old=json.loads((ROOT/'results.json').read_text());results=old['results'];resume=len(results)
        certs=json.loads((ROOT/'certificates.json').read_text())
        print(json.dumps({'resume_cases':resume,'bounded_retry':'single native-solver thread'}),flush=True)
    case_number=0
    for name in sorted(ALLOW):
        raw=(data/name).read_bytes();sha=hashlib.sha256(raw).hexdigest();blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
        if sha!=audit[name]['sha256'] or blob!=manifest[name]['git_blob_sha']:raise ValueError('hash mismatch')
        provenance.append({'file':name,'sha256':sha,'git_blob_sha':blob})
        with (data/name).open() as f:rows=list(csv.DictReader(f))
        t=[F(r['time']) for r in rows];q=[F(r['angle']) for r in rows];w=[F(r['angular_velocity']) for r in rows]
        if len(t)!=6000 or any(t[i+1]-t[i]!=F('.01') for i in range(5999)):raise ValueError('grid mismatch')
        if systems is None:
            knots=list(range(0,6000,5));
            if knots[-1]!=5999:knots.append(5999)
            systems=(System(t,knots,'outer'),System(t,knots,'inner'))
        outer,inner=systems;L=LENGTHS[int(name[3])-1]
        for N in [2000,4000]:
          for ew in [F('.0005'),F('.2')]:
           for B in [F(0),F(2)]:
            case_number+=1
            if case_number<=resume: continue
            if time.monotonic()-started>1800:raise RuntimeError('finite package time cap reached')
            e,A,corridor=parameters(q[0],w[0],L,N,ew,B)
            ro=outer.solve(q,w,e[1],ew,A[1]);co=outer.outer_certificate(ro,q,w,e[1],ew,A[1])
            outer_state='excluded_exact' if co and co['positive'] else 'not_excluded' if ro.success and ro.x[-1]<=1e-8 else 'inconclusive'
            # Inner is not needed after a proved outer exclusion.
            ri=None;ci=None
            if outer_state!='excluded_exact':
                ri=inner.solve(q,w,e[0],ew,A[0]);ci=inner.inner_certificate(ri,q,w,e[0],ew,A[0])
            inner_state='strict_path_exact' if ci else 'not_constructed' if ri is None or ri.status==2 else 'inconclusive'
            case={'file':name,'N':N,'ew':float(ew),'B':int(B),'eta':0,'angle_error_upper':float(e[1]),'acceleration_upper':float(A[1]),
                  'clock_cos_corridor':corridor,'outer_status':outer_state,'outer_solver_status':int(ro.status),'outer_phase1':float(ro.x[-1]) if ro.success else None,
                  'inner_status':inner_state,'inner_solver_status':int(ri.status) if ri is not None else None,'inner_sigma':float(ri.x[-1]) if ri is not None and ri.success else None,
                  'exact_outer_margin':co['margin'] if co and co['positive'] else None,'exact_inner_margin':ci['minimum_normalized_margin'] if ci else None}
            results.append(case)
            if co and co['positive']:certs.append({'case':len(results)-1,'kind':'outer','certificate':co})
            if ci:certs.append({'case':len(results)-1,'kind':'inner','certificate':ci})
            (ROOT/'results.json').write_text(json.dumps({'results':results,'provenance':provenance,'elapsed_seconds':time.monotonic()-started},indent=2)+'\n')
            (ROOT/'certificates.json').write_text(json.dumps(certs,indent=2)+'\n')
            print(json.dumps({'done':len(results),**case}),flush=True)
    summaries=[]
    for N in [2000,4000]:
     for ew in [.0005,.2]:
      for B in [0,2]:
        subset=[r for r in results if (r['N'],r['ew'],r['B'])==(N,ew,B)]
        summaries.append({'N':N,'ew':ew,'B':B,'records':len(subset),'outer_excluded':sum(r['outer_status']=='excluded_exact' for r in subset),
            'strict_inner_paths':sum(r['inner_status']=='strict_path_exact' for r in subset),'inconclusive':sum(r['outer_status']=='inconclusive' or r['inner_status']=='inconclusive' for r in subset)})
    (ROOT/'summary.json').write_text(json.dumps({'stage':'reused development; interval-path tests not force confirmation','record_cases':len(results),'samples_per_record':6000,'knots':outer.K,'summary':summaries,'elapsed_seconds':time.monotonic()-started,'provenance':provenance},indent=2)+'\n')
    print(json.dumps({'complete':True,'summary':summaries}),flush=True)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--data-dir',type=Path,required=True);run(p.parse_args().data_dir)
