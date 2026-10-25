"""Synthetic end-to-end receipt/scoring controls; no EEG inference."""
from pathlib import Path
import json
from record_scoring import score_record

checks=[]
def check(name,value):
 if not value:raise AssertionError(name)
 checks.append(name)

def run(**kwargs):
 args=dict(record_id='r',annotation_record_id='r',mask_record_id='r',decision_record_id='r',duration=8,events=[(1,4),(6,8)],sampling_hz=1,ready=[True]*8,invalid=[False]*8,decisions=[],deadline=1)
 args.update(kwargs);return score_record(**args)

r=run(ready=[False]*8)
check('all unavailable events remain misses with full denominator',r['timely']['reference_events']==2 and r['timely']['events_without_fresh_activation']==2 and r['timely']['recording_seconds']==8 and r['timely']['sensitivity']==0)
d=dict(onset_sample_end=2,offset_sample_end=3,evidence_sample_end=2)
r=run(decisions=[d])
check('sample-end onset not backdated and deadline inclusive',r['timely']['first_activation_latencies']==[1,None] and r['timely']['timely_events']==1)
r=run(decisions=[d],deadline=0)
check('zero deadline does not gain a backdated hit',r['timely']['timely_events']==0 and r['timely']['late_events']==1)
r=run(events=[],decisions=[d])
check('false alarms use full recording time',r['timely']['false_activations']==1 and r['timely']['false_activations_per_24h']==10800)
invalid=[dict(mask_record_id='other'),dict(annotation_record_id='other'),dict(decision_record_id='other'),dict(decisions=[dict(d,evidence_sample_end=3)]),dict(decisions=[dict(d,onset_sample_end=0)]),dict(decisions=[dict(d,offset_sample_end=9)]),dict(decisions=[d],ready=[False]*8),dict(decisions=[dict(d,onset_sample_end=True)]),dict(deadline='1/3')]
for args in invalid:
 try:run(**args)
 except ValueError:pass
 else:raise AssertionError(args)
checks.append('9 identity future-evidence availability boundary and rounding cases reject')
try:run(decisions=[d,d])
except ValueError:checks.append('duplicate alarm intervals not silently merged')
else:raise AssertionError('duplicates accepted')
# Independently expected unit-rate onsets: activation>=1, event[1,4),D1.
cases=0
for onset in range(1,7):
 for deadline in range(4):
  r=run(events=[(1,4)],decisions=[dict(onset_sample_end=onset,offset_sample_end=onset+1,evidence_sample_end=onset)],deadline=deadline)
  assert r['timely']['timely_events']==int(onset in (1,2,3) and onset-1<=deadline)
  assert r['timely']['false_activations']==int(onset not in (1,2,3))
  cases+=1
checks.append('24 independent integer activation/deadline cases')
result=dict(status='PASS',control_groups=len(checks),checks=checks,independent_cases=cases,synthetic_only=True,new_data_access=False,clinical_result=False)
Path('record_scoring_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
