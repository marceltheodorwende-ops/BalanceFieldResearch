"""Independent paired-cluster enumeration; synthetic only."""
import itertools,json
from pathlib import Path
from patient_comparison import aggregate_pairs,paired_resamples
from record_scoring import score_record
checks=[]
def check(name,x):
 if not x:raise AssertionError(name)
 checks.append(name)
def receipt(key,duration,events,decisions):
 return dict(status='scored',result=score_record(key,key,key,key,duration,events,1,[True]*duration,[False]*duration,decisions,1))
def alarm(a,b):return dict(onset_sample_end=a,offset_sample_end=b,evidence_sample_end=a)
expected=[dict(record_id='x',person='p1',seconds=8,events=1),dict(record_id='y',person='p1',seconds=8,events=1),dict(record_id='z',person='p2',seconds=8,events=0)]
a={k:receipt(k,8,[(1,4)] if k!='z' else [],[alarm(2,3)] if k!='z' else [alarm(5,6)]) for k in ('x','y','z')}
b={k:receipt(k,8,[(1,4)] if k!='z' else [],[]) for k in ('x','y','z')}
p=aggregate_pairs(expected,a,b)
check('repeated sessions become one person with pooled counts',len(p)==2 and p[0]['seconds']=='16' and p[0]['events']==2 and p[0]['a_tp']==2)
r=paired_resamples(p,list(itertools.product(range(2),repeat=2)))
check('same patient draw applied to both models', [x['sensitivity_difference'] for x in r['resamples']]==['1','1','1',None])
check('zero-event draw retained undefined not dropped',r['undefined_sensitivity_draws']==1 and len(r['resamples'])==4)
check('pooled time rate independently matches count ratio',r['point']['false_activations_per24h_difference']=='3600')
selfr=paired_resamples(aggregate_pairs(expected,a,a),[(0,1),(1,0)])
check('identical methods give exact zero paired differences',all(x['sensitivity_difference']=='0' and x['false_activations_per24h_difference']=='0' for x in selfr['resamples']))
for args in [(p[:1],[(0,)]),(p,[(0,)]),(p,[(0,2)]),(p,[(True,0)]),(p,[])]:
 try:paired_resamples(*args)
 except ValueError:pass
 else:raise AssertionError(args)
checks.append('5 one-person malformed index and empty resampling cases rejected')
try:aggregate_pairs(expected,a,{})
except ValueError:checks.append('incomplete rival cannot silently alter comparison set')
else:raise AssertionError('unpaired cohort accepted')
check('no confidence interval or clinical decision fabricated',r['confidence_interval'] is None)
result=dict(status='PASS',control_groups=len(checks),checks=checks,synthetic_only=True,new_data_access=False,clinical_result=False)
Path('patient_comparison_checks.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
