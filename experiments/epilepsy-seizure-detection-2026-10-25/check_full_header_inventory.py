"""Full-manifest synthetic transport fixtures; no network or patient labels."""
from pathlib import Path
from tempfile import TemporaryDirectory
import json
from full_header_inventory import run_inventory
from development_manifest import build_manifest
from channel_policy import TARGET17
manifest,_=build_manifest();paths=sorted(r['path'] for r in manifest)
records={p:dict(path=p,events=[]) for p in paths}
checks=[]
def check(name,x):
 if not x:raise AssertionError(name)
 checks.append(name)
calls=[]
def fake(path,**kwargs):
 calls.append(path)
 if path==paths[0]:raise ValueError('Synthetic transport failure')
 channels=[dict(index=i,label=label,unit='uV',volts_per_digital_step='1',sampling_hz='256') for i,label in enumerate(TARGET17)]
 if path==paths[1]:channels=channels[1:]
 return dict(path=path,waveform_bytes_read=0,header_sha256='synthetic',header_bytes_read=256,
    metadata=dict(records=10,record_seconds='1',recording_seconds='10',channels=channels,discontinuous=False))
with TemporaryDirectory() as tmp:
 out=Path(tmp)/'run'
 summary=run_inventory(records,out,probe_fn=fake)
 check('all565 exact manifest files attempted once including zero-event files',len(calls)==len(set(calls))==565 and set(calls)==set(paths))
 check('failure and ineligible retained separately',summary['failed_files']==1 and summary['metadata_ineligible_files']==1 and summary['eligible_files']==563)
 check('incomplete duration never advertised as complete cohort',summary['full_cohort_recorded_seconds'] is None and summary['successfully_joined_seconds']=='5640')
 receipts=[p for p in out.glob('*.json') if p.name not in ('selection.json','summary.json')]
 check('all565 per-file checkpoint receipts persisted',len(receipts)==565 and all(json.loads(p.read_text())['path'] in records for p in receipts))
 before=len(calls)
 try:run_inventory(dict(records,**{'chb19/chb19_01.edf':dict(path='x',events=[])}),Path(tmp)/'bad',probe_fn=fake)
 except ValueError:check('test path rejected before any request',len(calls)==before)
 else:raise AssertionError('holdout guard')
 try:run_inventory(records,out,probe_fn=fake)
 except FileExistsError:check('previous run never silently overwritten',len(calls)==before)
 else:raise AssertionError('overwrite accepted')
result=dict(status='PASS',control_groups=len(checks),checks=checks,synthetic_header_requests=565,real_network_requests=0,clinical_result=False)
Path('full_header_inventory_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
