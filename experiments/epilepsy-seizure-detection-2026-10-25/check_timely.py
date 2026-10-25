"""Analytic and exhaustive independent oracle controls; no patient data."""
import itertools
import json
import math
from pathlib import Path
from timely import score_timely

checks = []
def check(name, value):
    if not value:
        raise AssertionError(name)
    checks.append(name)

def run(r, a, t=300, d=30):
    return score_timely(r, a, t, d)

x = run([(100,110)],[(150,151)])
check('postictal-only not detected', x['timely_events']==0 and x['false_activations']==1)
x = run([(100,110)],[(0,300)])
check('always on gets no fresh TP', x['timely_events']==0 and x['alarm_fraction']==1 and x['false_activations']==1)
x = run([(100,200)],[(140,141)])
check('late ictal distinct from false alarm', x['late_events']==1 and x['late_ictal_activations']==1 and x['false_activations']==0)
check('long reference remains one', run([(0,601)],[(1,2)],900)['reference_events']==1)
check('adjacent references stay two', run([(0,10),(10,20)],[(1,2),(10,11)])['timely_events']==2)
check('event endpoint excluded', run([(100,110)],[(110,111)])['timely_events']==0)
check('deadline included', run([(100,200)],[(130,131)])['timely_events']==1)
check('deadline after event does not extend event', run([(100,110)],[(120,121)])['timely_events']==0)
check('zero deadline exact onset', run([(100,110)],[(100,101)],d=0)['timely_events']==1)
check('no event sensitivity null', run([],[])['sensitivity'] is None)
check('false rate denominator full duration', run([],[(10,11)])['false_activations_per_24h']==288)
check('stale alarm cannot credit next reference', run([(10,20),(30,40)],[(11,39)])['timely_events']==1)
check('all activations in same event one TP', run([(10,20)],[(11,12),(14,15)])['timely_events']==1)
check('availability timestamp used without backdating', run([(10,20)],[(21,22)])['events_without_fresh_activation']==1)
check('tiny empty recording rates remain finite', run([],[],1e-310)['false_activations_per_24h']==0)
invalid = [([],[],0,30),([],[],300,-1),([],[],math.inf,30),([],[],300,math.nan),
           ([(2,1)],[],300,30),([(-1,1)],[],300,30), ([(0,301)],[],300,30),
           ([(0,2),(1,3)],[],300,30),([],[(0,1),(1,2)],300,30),
           ([],[(2,3),(0,1)],300,30),([],[(True,2)],300,30),([],[(0,math.inf)],300,30),
           ([],[],10**1000,30),([],[(0,1e-311)],1e-310,30)]
for args in invalid:
    try: score_timely(*args)
    except ValueError: pass
    else: raise AssertionError(('invalid accepted',args))
checks.append('14 invalid numeric/domain/adjacency/overflow controls rejected')

# Oracle operates on binary integer time cells, independently of interval sweep.
def intervals(mask):
    starts=[i for i,v in enumerate(mask) if v and (i==0 or not mask[i-1])]
    return [(s,next((j for j in range(s+1,len(mask)) if not mask[j]),len(mask))) for s in starts]
N=6
cases=0
for rm in itertools.product((0,1),repeat=N):
    refs=intervals(rm)
    for am in itertools.product((0,1),repeat=N):
        alarms=intervals(am)
        starts=[i for i,v in enumerate(am) if v and (i==0 or not am[i-1])]
        for d in (0,1,3):
            actual=run(refs,alarms,N,d)
            oracle_first=[min((j-s for j in starts if s<=j<e),default=None) for s,e in refs]
            expected_tp=sum(v is not None and v<=d for v in oracle_first)
            expected_fp=sum(not rm[j] for j in starts)
            assert actual['first_activation_latencies']==oracle_first
            assert actual['timely_events']==expected_tp and actual['false_activations']==expected_fp
            assert actual['alarm_seconds']==sum(am)
            assert actual['reference_events']==len(refs)
            cases+=1
checks.append('exhaustive independent binary-cell oracle')
x=run([(10,20),(30,60)],[(11,12),(29,35),(50,52)],100,15)
y=run([(20,40),(60,120)],[(22,24),(58,70),(100,104)],200,30)
check('time-scale count invariance', x['timely_events']==y['timely_events'] and x['false_activations']==y['false_activations'] and x['alarm_fraction']==y['alarm_fraction'])
check('time-scale rate covariance', x['false_activations_per_24h']==2*y['false_activations_per_24h'])
z=run([(10,20),(30,60)],[(11,12),(29,35),(50,52)],200,15)
check('added background keeps counts changes rate', z['timely_events']==x['timely_events'] and z['false_activations_per_24h']==x['false_activations_per_24h']/2)
result=dict(status='PASS',named_controls=len(checks),exhaustive_cases=cases,checks=checks,
            synthetic_only=True,confirmatory_freeze=False,empirical_result=False)
Path(__file__).with_name('timely_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
