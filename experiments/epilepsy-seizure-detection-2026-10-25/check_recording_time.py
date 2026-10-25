"""Independent integer-grid and boundary checks; already-exposed metadata only."""
from fractions import Fraction
from pathlib import Path
import json
import re
from recording_time import reconcile, clock_seconds

checks=[]
def check(name, condition):
    if not condition: raise AssertionError(name)
    checks.append(name)

r=reconcile('10', [('0','2'),('2','3'),('9','10')],256)
check('adjacent original events remain separate and boundary end accepted',len(r['events'])==3 and r['events'][-1]['sample_interval']==[2304,2560])
check('exact seizure and full nonseizure duration retained',r['seizure_seconds']=='4' and r['nonseizure_seconds']=='6')
check('zero-event recording retains all time',reconcile(10,[],256)['nonseizure_seconds']=='10')
r=reconcile(1,[('1/3','2/3')],256)
check('off-grid event retained without rounding',r['events'][0]['sample_interval'] is None and r['seizure_seconds']=='1/3')
invalid=[(0,[],256),(1,[],0),('1/3',[],256),(1,[(-1,1)],256),(1,[(0,2)],256),(1,[(0,0)],256),(2,[(0,2),(1,2)],256),(2,[(1,2),(0,1)],256),(1,[(0,float('nan'))],256),(True,[],256),(1,[(0,1.0)],256)]
for args in invalid:
    try: reconcile(*args)
    except ValueError:pass
    else:raise AssertionError(args)
checks.append('11 invalid duration boundary overlap order and numeric cases reject without repair')
# Independent unit-cell counting oracle, not interval-length formula.
cases=0
for n in range(1,9):
 for bits in range(1<<n):
    active=[i for i in range(n) if bits>>i&1]
    events=[(i,i+1) for i in active]
    result=reconcile(n,events,1)
    assert int(result['seizure_seconds'])==len(active)
    assert int(result['nonseizure_seconds'])==len([i for i in range(n) if i not in active])
    cases+=1
checks.append('510 independent integer-cell coverage cases')
check('clock24 supported but no date inferred',clock_seconds('24:14:46')==87286 and reconcile(1,[],1)['inter_record_gap_seconds'] is None)
# Already-exposed pinned chb01 summary; no new data or annotations acquired.
text=Path('source_metadata/chb01-summary.txt').read_text()
blocks=re.split(r'File Name: ',text)[1:]
first=blocks[0]
start=re.search(r'File Start Time: (\S+)',first)[1];end=re.search(r'File End Time: (\S+)',first)[1]
header=json.loads(Path('development_header_audit.json').read_text())
check('first source-clock duration matches independently acquired EDF duration',clock_seconds(end)-clock_seconds(start)==int(header['metadata']['recording_seconds'])==3600)
check('source midnight ambiguity is present','24:14:46' in text and '00:14:53' in text)
result=dict(status='PASS',control_groups=len(checks),checks=checks,integer_oracle_cases=cases,source_summary_blocks=len(blocks),new_network_requests=0,new_annotation_files=0,clinical_result=False)
Path('recording_time_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
