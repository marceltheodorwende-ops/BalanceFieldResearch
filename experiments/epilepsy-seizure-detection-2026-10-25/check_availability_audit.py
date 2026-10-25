"""Independent cell-count oracle and causal-stream integration; synthetic only."""
from fractions import Fraction
from pathlib import Path
import json
import numpy as np
from availability_audit import audit_availability
from causal_stream import RecordStream

checks=[]
def check(name,value):
 if not value:raise AssertionError(name)
 checks.append(name)

r=audit_availability(4,[(0,1),(2,4)],1,[False]*4,[False]*4)
check('fully unavailable events and full time remain in denominators',r['original_sensitivity_denominator']==2 and r['full_record_rate_denominator_seconds']=='4' and all(x['ready_overlap_seconds']=='0' for x in r['per_event']))
r=audit_availability(1,[('1/3','2/3')],2,[True,False],[False,False])
check('off-grid overlap exact without rounding',r['per_event'][0]['ready_overlap_seconds']=='1/6' and r['per_event'][0]['unavailable_overlap_seconds']=='1/6')
cases=0
for n in range(1,6):
 for event_mask in range(1<<n):
  events=[(i,i+1) for i in range(n) if event_mask>>i&1]
  for ready_mask in range(1<<n):
   ready=[bool(ready_mask>>i&1) for i in range(n)]
   r=audit_availability(n,events,1,ready,[False]*n)
   expected=sum(1 for i in range(n) if event_mask>>i&1 and ready_mask>>i&1)
   assert sum(Fraction(x['ready_overlap_seconds']) for x in r['per_event'])==expected
   assert r['original_event_count']==len(events) and r['recorded_seconds']==str(n)
   cases+=1
checks.append('1364 independent event/readiness mask cell cases')
s=RecordStream('fixture',6,2,1,[.5,.5]);out=s.feed(0,np.ones((6,1)),np.array([True,True,False,True,True,True]));coverage=s.finish()
r=audit_availability(3,[(0,3)],2,out['ready'],out['invalid'])
check('stream ready invalid warmup counts join without time loss',r['ready_seconds']=='3/2' and r['invalid_seconds']=='1/2' and r['warmup_seconds']=='1' and coverage['declared_seconds']==r['recorded_seconds'])
check('cell accounting does not backdate sample-end availability',out['availability_sample_end'].tolist()==[1,2,3,4,5,6] and not r['alarm_matching_performed'])
for ready,invalid in [([1,0],[False,False]),([True],[False]),([True,False],[True,False])]:
 try:audit_availability(2,[],1,ready,invalid)
 except ValueError:pass
 else:raise AssertionError('invalid masks accepted')
checks.append('nonboolean truncated and contradictory masks refused')
result=dict(status='PASS',control_groups=len(checks),checks=checks,independent_oracle_cases=cases,synthetic_only=True,new_data_access=False,clinical_result=False)
Path('availability_audit_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
