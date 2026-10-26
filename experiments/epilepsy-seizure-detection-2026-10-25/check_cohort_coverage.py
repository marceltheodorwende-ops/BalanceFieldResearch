"""Synthetic cohort completeness and real already-known manifest controls."""
import json
from pathlib import Path
from cohort_coverage import coverage_report
from record_scoring import score_record
checks=[]
def check(name,value):
 if not value:raise AssertionError(name)
 checks.append(name)
expected=[dict(record_id='a',person='same',seconds=8,events=1),dict(record_id='b',person='same',seconds=4,events=0)]
r=coverage_report(expected,{})
check('all missing retains full hours events and person group',not r['complete'] and r['expected_seconds']=='12' and r['expected_events']==1 and len(r['persons'])==1 and r['cohort_performance'] is None)
r=coverage_report(expected,{'b':dict(status='failed',reason='truncated')})
check('failure and missing kept separately without imputed negative result',r['persons']['same']['failed']==1 and r['persons']['same']['missing']==1 and r['persons']['same']['unassessed_seconds']=='12')
s=score_record('a','a','a','a',8,[(1,4)],1,[True]*8,[False]*8,[],1)
r=coverage_report(expected,{'a':dict(status='scored',result=s)})
check('scored subset never marks whole cohort complete',not r['complete'] and r['persons']['same']['unassessed_seconds']=='4')
sb=score_record('b','b','b','b',4,[],1,[True]*4,[False]*4,[],1)
r=coverage_report(expected,{'a':dict(status='scored',result=s),'b':dict(status='scored',result=sb)})
check('complete receipt set still is not a performance or confirmation claim',r['complete'] and r['cohort_performance'] is None)
for exp,rec in [(expected+expected,{}),(expected,{'other':dict(status='failed',reason='error')}),(expected,{'a':dict(status='failed',reason='')}),(expected,{'a':dict(status='missing')}),(expected,{'b':dict(status='scored',result=s)})]:
 try:coverage_report(exp,rec)
 except ValueError:pass
 else:raise AssertionError('invalid receipt accepted')
checks.append('5 duplicate unknown missing-reason forged-missing and identity cases rejected')
source=json.loads(Path('chb01_duration_reconciliation.json').read_text())
manifest=[dict(record_id=x['path'],person='chb01',seconds=x['join']['duration_seconds'],events=len(x['join']['events'])) for x in source['results']]
real=coverage_report(manifest,{})
check('real metadata cannot masquerade as detector outputs',real['expected_records']==42 and real['expected_seconds']=='145988' and real['expected_events']==7 and real['persons']['chb01']['missing']==42 and not real['complete'])
Path('chb01_detector_coverage.json').write_text(json.dumps(real,indent=2)+'\n')
result=dict(status='PASS',control_groups=len(checks),checks=checks,new_data_access=False,clinical_result=False)
Path('cohort_coverage_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
