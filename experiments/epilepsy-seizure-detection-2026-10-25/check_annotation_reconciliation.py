"""Synthetic binary/identity integrity controls; no patient timings."""
from pathlib import Path
import json
from annotation_reconciliation import boundary_subset,reconcile_block,reconcile_summary
checks=[]
def check(name,value):
 if not value:raise AssertionError(name)
 checks.append(name)
def w(a,d):return ((a<<10)|d).to_bytes(2,'little')
def sk(v):
 v=v%(2**32);return w(59,0)+(v>>16).to_bytes(2,'little')+(v&65535).to_bytes(2,'little')
note=b'## time resolution: 8'
head=w(22,0)+w(63,len(note))+note+(b'\0' if len(note)%2 else b'')+sk(-1)+w(0,1)
binary=head+w(32,16)+w(33,16)+w(32,16)+w(33,16)+b'\0\0'
check('independent synthetic sample positions',boundary_subset(binary)==(8,[16,32,48,64]))
lines=['fixture.edf\n','File Start Time: 01:00:00\n','File End Time: 02:00:00\n','Number of Seizures in File: 2\n','Seizure 1 Start Time: 2 seconds\n','Seizure 1 End Time: 4 seconds\n','Seizure 2 Start Time: 6 seconds\n','Seizure 1 End Time: 8 seconds\n']
r,n,fs=reconcile_block(lines,binary,[(2,'End',1)])
check('only explicitly approved index changed; source list intact',n==1 and fs==8 and r[:-1]==lines[:-1] and r[-1]=='Seizure 2 End Time: 8 seconds\n' and lines[-1]=='Seizure 1 End Time: 8 seconds\n')
for approvals in [[],[(1,'End',1)],[(2,'End',1),(2,'End',1)]]:
 try:reconcile_block(lines,binary,approvals)
 except ValueError:pass
 else:raise AssertionError('invalid approval accepted')
checks.append('3 missing stale duplicate approvals reject')
bad=list(lines);bad[-1]='Seizure 1 End Time: 9 seconds\n'
try:reconcile_block(bad,binary,[(2,'End',1)])
except ValueError:checks.append('binary disagreement cannot be repaired by approved label')
else:raise AssertionError('numerical repair')
for b in [binary[:-1],binary+b'\0\0',binary[:-2],head+w(33,16)+b'\0\0',head+w(32,16)+w(33,0)+b'\0\0',head+w(32,16)+b'\0\0']:
 try:boundary_subset(b)
 except ValueError:pass
 else:raise AssertionError('malformed binary accepted')
checks.append('6 truncated trailing unordered empty unpaired binary cases reject')
try:reconcile_summary(b'invented','chb01','chb01/chb01_01.edf',binary,[])
except ValueError:checks.append('original hash binding refuses synthetic replacement')
else:raise AssertionError('hash bypass')
try:reconcile_summary(b'','chb19','chb19/chb19_01.edf',b'',[])
except ValueError:checks.append('holdout guard rejects before source resolution')
else:raise AssertionError('holdout accepted')
report=dict(status='PASS',control_groups=len(checks),checks=checks,synthetic_only=True,new_data_access=False)
Path('annotation_reconciliation_checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
