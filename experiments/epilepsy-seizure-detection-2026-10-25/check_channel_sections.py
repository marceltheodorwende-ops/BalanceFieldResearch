"""Synthetic section-preservation controls; no source annotations."""
from pathlib import Path
import json
from annotation_import import parse_summary
checks=[]
def check(name,value):
 if not value:raise AssertionError(name)
 checks.append(name)
base='File Name: chb01_01.edf\nFile Start Time: 01:00:00\nFile End Time: 02:00:00\nNumber of Seizures in File: 0\n'
section='Channels changed:\n*****************\nChannel 1: TEST-A\nChannel 2: TEST-B\n'
result=parse_summary(base+section,'chb01',channel_sections=True)['chb01/chb01_01.edf']
check('all labels and original indices retained with unresolved scope',result['following_channel_change_sections']==[dict(channels=[dict(index=1,label='TEST-A'),dict(index=2,label='TEST-B')],scope='between_file_blocks_unassigned')])
check('zero-event file preserved',result['events']==[] and not result['duration_verified'])
check('multiple channel sections not collapsed',len(parse_summary(base+section+section,'chb01',channel_sections=True)['chb01/chb01_01.edf']['following_channel_change_sections'])==2)
try:parse_summary(base+section,'chb01')
except ValueError:checks.append('default API still rejects unsupported sections')
else:raise AssertionError('default changed')
for tail in [section.replace('Channel 2','Channel 1'),section.replace('Channel 2','Channel 3'),section.replace('Channel 1','Channel 0'),section.replace('*****************','unknown'), 'Channels changed:\n***\n',section+'Seizure Start Time: 1 seconds\n',section.replace('Channel 2: TEST-B','Channel 2:')]:
 try:parse_summary(base+tail,'chb01',channel_sections=True)
 except ValueError:pass
 else:raise AssertionError('malformed section swallowed')
checks.append('7 duplicate skipped zero missing malformed and hidden-event cases reject')
check('no-section compatibility unchanged',parse_summary(base,'chb01',channel_sections=True)==parse_summary(base,'chb01'))
r=dict(status='PASS',control_groups=len(checks),checks=checks,synthetic_only=True,new_data_access=False)
Path('channel_sections_checks.json').write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
