"""Bounded audit of exactly the fifteen already authorized attempt-1 files.
Run python audit.py DATA_DIR (no fetching or dataset processor execution).
"""
import csv,hashlib,json,re,sys
from pathlib import Path
root=Path(__file__).parent
items=json.loads((root/'source_manifest.json').read_text())
allowed={f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4)}
assert len(items)==15 and {Path(i['path']).name for i in items}==allowed
data=Path(sys.argv[1]) if len(sys.argv)>1 else root/'data'
# Refuse mixed directories before opening any measurement file.
assert {p.name for p in data.glob('*.csv')}==allowed
out=[]
for item in items:
    p=data/Path(item['path']).name;raw=p.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert blob==item['git_blob_sha']
    rows=list(csv.DictReader(raw.decode().splitlines()))
    assert len(rows)==6000 and set(rows[0])=={'time','angle','angular_velocity','is_peak'}
    assert all(r['time']==f'{i/100:.2f}' for i,r in enumerate(rows))
    assert all(re.fullmatch(r'-?\d+\.\d{3}',r[k]) for r in rows for k in ['angle','angular_velocity'])
    assert all(r['is_peak'] in ['0','1'] for r in rows)
    out.append({'file':p.name,'git_blob_sha':blob,'sha256':hashlib.sha256(raw).hexdigest(),
                'rows':len(rows),'first_time':rows[0]['time'],'last_time':rows[-1]['time'],
                'angle_min':min(float(r['angle']) for r in rows),
                'angle_max':max(float(r['angle']) for r in rows),
                'one_centisecond_grid':True,'three_decimal_angle_and_velocity':True})
sources=json.loads((root/'source_evidence.json').read_text())
for src in sources:
    raw=src['content'].encode();assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==src['git_blob_sha']
res={'stage':'real development schema/instrument audit; not model confirmation',
     'source_commit':items[0]['source_commit'],'recordings':15,'total_rows':sum(r['rows'] for r in out),
     'source_metadata_blobs_verified':len(sources),'files':out,'holdout_accessed':False,
     'forecast_or_force_fit_performed':False,'BFG_state_or_event_clock_calibrated':False}
(root/'audit.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps({'recordings':15,'rows':res['total_rows'],'all_source_blobs_verified':True,'holdout_accessed':False}))
