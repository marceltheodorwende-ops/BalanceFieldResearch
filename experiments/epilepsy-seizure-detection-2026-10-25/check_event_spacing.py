"""Synthetic event-value separator controls, no real source annotations."""
from pathlib import Path
import json
from annotation_import import parse_summary
checks=[]
def check(name,value):
 if not value:raise AssertionError(name)
 checks.append(name)
base='File Name: chb01_01.edf\nFile Start Time: 01:00:00\nFile End Time: 02:00:00\nNumber of Seizures in File: 1\nSeizure 1 Start Time: 2 seconds\nSeizure 1 End Time: 4 seconds\n'
original=parse_summary(base,'chb01',numbered_events=True)
cases=0
for space in [' ','  ','   ','\t',' \t ']:
 candidate=base.replace('Time: 2 seconds','Time:'+space+'2 seconds').replace('Time: 4 seconds','Time:'+space+'4 seconds')
 check('separator variant '+str(cases),parse_summary(candidate,'chb01',numbered_events=True,event_value_spacing=True)==original)
 cases+=1
try:parse_summary(base.replace('Time: 4 seconds','Time:  4 seconds'),'chb01',numbered_events=True)
except ValueError:checks.append('default single-space dialect unchanged')
else:raise AssertionError('default changed')
for bad in [base.replace('Time: 4 seconds','Time:4 seconds'),base.replace('Time: 4 seconds','Time: 4.5 seconds'),base.replace('Time: 4 seconds','Time: -4 seconds'),base.replace('Time: 4 seconds','Time: 4 extra seconds'),base.replace('Seizure 1 End','Seizure 2 End'),base.replace('Time: 4 seconds','Time: \n4 seconds')]:
 try:parse_summary(bad,'chb01',numbered_events=True,event_value_spacing=True)
 except ValueError:pass
 else:raise AssertionError('invalid event syntax or number accepted')
checks.append('6 missing-separator numeric hidden-token identity and newline cases reject')
r=dict(status='PASS',control_groups=len(checks),checks=checks,synthetic_only=True,new_data_access=False)
Path('event_spacing_checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
