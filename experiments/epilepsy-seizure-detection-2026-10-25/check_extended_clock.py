"""Synthetic lexical clock controls, no calendar/timeline inference."""
from pathlib import Path
import json
from annotation_import import parse_summary
from recording_time import clock_seconds
checks=[]
def check(name,value):
 if not value:raise AssertionError(name)
 checks.append(name)
def block(start='27:30:01',end='00:30:03'):
 return f'File Name: chb01_01.edf\nFile Start Time: {start}\nFile End Time: {end}\nNumber of Seizures in File: 0\n'
r=parse_summary(block(),'chb01',extended_clock_tokens=True)['chb01/chb01_01.edf']
check('source text preserved including reversed numerical clock order',r['source_start_clock']=='27:30:01' and r['source_end_clock']=='00:30:03')
check('no derived duration or date installed',not r['duration_verified'] and not {'duration','date','gap','epoch_seconds'}&set(r))
try:parse_summary(block(),'chb01')
except ValueError:checks.append('default API still rejects extended hours')
else:raise AssertionError('default changed')
for token in ['-1:00:00','100:00:00','27:60:00','27:00:60','27:1:00','27:00:00Z','27:00:00 extra','27.5:00:00']:
 try:parse_summary(block(token),'chb01',extended_clock_tokens=True)
 except ValueError:pass
 else:raise AssertionError(token)
checks.append('8 malformed or unsupported lexical formats reject')
check('ordinary source clock compatibility unchanged',parse_summary(block('01:00:00','02:00:00'),'chb01',extended_clock_tokens=True)==parse_summary(block('01:00:00','02:00:00'),'chb01'))
try:clock_seconds('27:30:01')
except ValueError:checks.append('numeric clock converter unchanged and separate')
else:raise AssertionError('implicit converter relaxation')
report=dict(status='PASS',control_groups=len(checks),checks=checks,synthetic_only=True,new_data_access=False)
Path('extended_clock_checks.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2))
