"""Exact instrument-algebra and metadata controls; no patient signals/network."""
from copy import deepcopy
from fractions import Fraction as F
import json
from pathlib import Path
import random
from channel_policy import *
from montage_audit import STANDARD,rank

ROOT=Path(__file__).resolve().parent
checks=[]
def check(name,x):
    if not x:raise AssertionError(name)
    checks.append(name)
def mul(a,b):return [[sum(x*y for x,y in zip(row,col)) for col in zip(*b)] for row in a]
def mv(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]

nodes=list(STANDARD);b17=incidence(TARGET17,nodes);b18=incidence(BIPOLAR18,nodes);r,s=reconstruction()
check('exact17 and18 incidence ranks both16',rank(b17)==rank(b18)==16)
check('exact reconstruction R B17=B18',mul(r,b17)==b18)
check('exact selection S B18=B17',mul(s,b18)==b17)
check('S R is identity17',mul(s,r)==[[F(int(i==j)) for j in range(17)] for i in range(17)])
check('path uses7 retained voltage differences',sum(abs(v) for v in r[BIPOLAR18.index('T8-P8')])==7)
random.seed(20261025)
for _ in range(200):
    v=[F(random.randint(-100,100),7) for n in nodes]
    assert mv(r,mv(b17,v))==mv(b18,v)
    assert mv(b17,[x+F(11,3) for x in v])==mv(b17,v)
checks.append('200 independent potential vectors and common-reference shifts')
# A noise vector only on omitted edge is lost: do not claim noisy-data equivalence.
noise=[F(int(x=='T8-P8')) for x in BIPOLAR18]
check('explicit noisy-data non-equivalence retained',mv(r,mv(s,noise))!=noise)
path=r[BIPOLAR18.index('T8-P8')];errors=[F(1 if x>0 else -1 if x<0 else 0) for x in path]
check('hypothetical unit-error bound7 is attained',sum(x*y for x,y in zip(path,errors))==7)

header=json.loads((ROOT/'development_header_audit.json').read_text())['metadata'];out=compile_map(header)
check('real development metadata has unique17 target map',out['eligible'] and len(out['mapping'])==17)
check('both duplicate T8-P8 copies omitted',not {14,22}&{x['source_index'] for x in out['mapping']})
shuffled=deepcopy(header);random.shuffle(shuffled['channels'])
check('metadata ordering irrelevant',compile_map(shuffled)==out)
formatted=deepcopy(header)
for c in formatted['channels']:c['label']=' '+c['label'].lower().replace('-',' - ')+' '
check('case/spacing normalization does not change target indices',
      [(x['target'],x['source_index'],x['sign']) for x in compile_map(formatted)['mapping']]==
      [(x['target'],x['source_index'],x['sign']) for x in out['mapping']])
changed=deepcopy(header);changed['channels'][0]['label']='F7-FP1'
rev=compile_map(changed)
check('unique reverse-only label gets explicit minus sign',rev['eligible'] and rev['mapping'][0]['sign']==-1)
c=header['channels'][0]
check('sign applied after physical offset calibration',signed_volts(c,0,-1)==-to_volts(c,0) and signed_volts(c,0,-1)!=to_volts(c,0))
check('reversing raw digital zero would be wrong',to_volts(c,-0)!=signed_volts(c,0,-1))
for kind in ('duplicate','missing','unknown_unit','rate','discontinuous','unknown_count'):
    h=deepcopy(header)
    if kind=='duplicate':h['channels'].append(deepcopy(h['channels'][0]))
    elif kind=='missing':h['channels']=[c for c in h['channels'] if normalize(c['label'])!='FP1-F7']
    elif kind=='unknown_unit':h['channels'][0]['unit']='unknown'
    elif kind=='rate':h['channels'][0]['sampling_hz']='128'
    elif kind=='discontinuous':h['discontinuous']=True
    elif kind=='unknown_count':h['records']=-1
    assert not compile_map(h)['eligible'],kind
checks.append('6 ambiguous/missing/unit/rate/timing cases explicitly ineligible')
result=dict(status='PASS',control_groups=len(checks),checks=checks,exact_rank=16,
    target_channels=list(TARGET17),path_terms=EDGE_PATH,path_noise_L1_bound=7,
    metadata_candidate_map=out,signal_equality_assumed=False,raw_waveform_access=False,
    clinical_or_BFG_prediction_result=False,confirmatory_freeze=False)
(ROOT/'channel_policy_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='metadata_candidate_map'},indent=2))
