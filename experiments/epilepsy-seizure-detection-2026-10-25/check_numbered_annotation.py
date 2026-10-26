"""Synthetic numbered grammar controls only; no source annotations."""
from pathlib import Path
import json
from annotation_import import parse_summary
checks=[]
def check(name,value):
    if not value:raise AssertionError(name)
    checks.append(name)
base='File Name: chb01_01.edf\nFile Start Time: 01:00:00\nFile End Time: 02:00:00\nNumber of Seizures in File: 1\nSeizure Start Time: 2 seconds\nSeizure End Time: 4 seconds\n'
# Explicit numbered dialect: preserve default, validate identity of every pair.
numbered=base.replace('Seizure Start','Seizure 1 Start').replace('Seizure End','Seizure 1 End')
check('explicit numbered dialect preserves original event values',parse_summary(numbered,'chb01',numbered_events=True)['chb01/chb01_01.edf']['events']==[[2,4]])
multi=numbered.replace('File: 1','File: 2')+'Seizure 2 Start Time: 5 seconds\nSeizure 2 End Time: 7 seconds\n'
check('two numbered events retained in source order',parse_summary(multi,'chb01',numbered_events=True)['chb01/chb01_01.edf']['events']==[[2,4],[5,7]])
for bad in [multi.replace('Seizure 2 End','Seizure 1 End'),multi.replace('Seizure 2 Start','Seizure 3 Start'),multi.replace('Seizure 2 End','Seizure End'),multi.replace('Seizure 1 Start','Seizure 0 Start'),multi.replace('Seizure 1 End','Seizure 2 End')]:
    try:parse_summary(bad,'chb01',numbered_events=True)
    except ValueError:pass
    else:raise AssertionError('ambiguous numbering repaired')
checks.append('5 duplicate mismatched skipped mixed and zero-index cases rejected')
try:parse_summary(numbered,'chb01')
except ValueError:checks.append('default unnumbered API remains strict')
else:raise AssertionError('default behavior changed')
check('explicit mode also preserves unnumbered original dialect',parse_summary(base,'chb01',numbered_events=True)==parse_summary(base,'chb01'))


result=dict(status='PASS',control_groups=len(checks),checks=checks,synthetic_only=True,new_data_access=False)
Path('numbered_annotation_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
