"""Pinned development-source and independently constructed malformed controls."""
import copy
import json
from pathlib import Path
from annotation_import import parse_summary,load_pinned_chb01,join_header

checks=[]
def check(name, value):
    if not value:raise AssertionError(name)
    checks.append(name)

base='File Name: chb01_01.edf\nFile Start Time: 11:42:54\nFile End Time: 12:42:54\nNumber of Seizures in File: 1\nSeizure Start Time: 2 seconds\nSeizure End Time: 4 seconds\n'
parsed=parse_summary(base,'chb01')
check('exact event pair and person/path preserved',parsed['chb01/chb01_01.edf']['events']==[[2,4]] and parsed['chb01/chb01_01.edf']['person']=='chb01')
invalid=[base.replace('File End Time:','Missing End:'),base.replace('File Start Time: 11:42:54','File Start Time: 25:42:54'),base.replace('File: 1','File: 0'),base.replace('End Time: 4 seconds','End Time: 1 seconds'),base.replace('Start Time: 2 seconds','Start Time: 2.5 seconds'),base.replace('chb01_01.edf','../chb19_01.edf'),base+base,base+'Unexpected metadata\n',base.replace('Seizure End Time: 4 seconds\n',''),base.replace('Seizure Start Time:','Seizure 1 Start Time:')]
for text in invalid:
    try:parse_summary(text,'chb01')
    except ValueError:pass
    else:raise AssertionError(text)
checks.append('10 malformed count clock order duplicate identity and dialect cases refused')
try:parse_summary(base,'chb19')
except ValueError:checks.append('test case denied before source parsing')
else:raise AssertionError('test import accepted')
records=load_pinned_chb01()
from development_manifest import build_manifest
manifest,_=build_manifest()
check('exact chb01 manifest file coverage',set(records)=={r['path'] for r in manifest if r['case']=='chb01'})
check('all42 source blocks retained including35 zero-event files',len(records)==42 and sum(not r['events'] for r in records.values())==35)
# Independently transcribed from already-exposed source, not parser output.
expected={'03':(2996,3036),'04':(1467,1494),'15':(1732,1772),'16':(1015,1066),'18':(1720,1810),'21':(327,420),'26':(1862,1963)}
actual={r['path']:r['events'] for r in records.values() if r['events']}
check('seven original source pairs independently match',actual=={'chb01/chb01_'+k+'.edf':[list(v)] for k,v in expected.items()})
header=json.loads(Path('development_header_audit.json').read_text())
joined=join_header(records[header['path']],header,256)
check('zero-event first record keeps full3600seconds',joined['nonseizure_seconds']=='3600' and joined['seizure_seconds']=='0')
for mutation in ('path','duration','discontinuous'):
    h=copy.deepcopy(header)
    if mutation=='path':h['path']='chb01/chb01_02.edf'
    elif mutation=='duration':h['metadata']['recording_seconds']=None
    else:h['metadata']['discontinuous']=True
    try:join_header(records[header['path']],h,256)
    except ValueError:pass
    else:raise AssertionError(mutation)
checks.append('3 path unknown-duration and discontinuity joins reject')
try:join_header(parsed['chb01/chb01_01.edf'],dict(path=header['path'],metadata=dict(recording_seconds='3')),256)
except ValueError:checks.append('out-of-duration event rejected rather than clipped')
else:raise AssertionError('clipped event')
result=dict(status='PASS',control_groups=len(checks),checks=checks,source_records=42,source_original_events=7,duration_verified_records=1,new_data_access=False,clinical_result=False)
Path('annotation_import_checks.json').write_text(json.dumps(result,indent=2)+'\n')
Path('chb01_annotation_import.json').write_text(json.dumps(dict(source_sha256='77e86183845192d147c88a9bb4263c2b4a32e936c6236029770f86ca2ea023db',records=records,header_join={header['path']:joined},other_record_durations='UNVERIFIED'),indent=2)+'\n')
print(json.dumps(result,indent=2))
