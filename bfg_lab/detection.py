"""Fixed synthetic catalogue for the unchanged conditional monitor."""
import hashlib
import json
from pathlib import Path
import numpy as np
from .diffusion import adjacency, heat_operator
from .monitor import assess


def run():
    rng=np.random.default_rng(20260916)
    rows=[]
    for family in ('path','cycle'):
        for weight in (.5,1.):
            random=rng.uniform(0,1,8); random/=random.sum()
            for label,x0 in [('impulse',np.eye(8)[0]),('random',random)]:
                for error in (0.,.001,.01):
                    noise=rng.uniform(-error,error,(21,8))
                    for scenario in ('steady','cut','forcing','speedup'):
                        a=adjacency(family,8,weight); r,_=heat_operator(a,.2)
                        x=x0.copy(); history=[x.copy()]
                        for step in range(1,21):
                            if step==7 and scenario=='cut':
                                a[3,4]=a[4,3]=0.; r,_=heat_operator(a,.2)
                            if step==7 and scenario=='speedup':
                                r,_=heat_operator(8*a,.2)
                            x=r@x
                            if step==7 and scenario=='forcing':
                                x[-1]+=.5
                            history.append(x.copy())
                        data=np.array(history)+noise
                        for columns in ([0,1],[0,1,4,5],list(range(8))):
                            samples=data[:,columns]
                            reports=[assess(samples[:step+1],8,model_assumed=True,
                                            sample_error=error) for step in range(1,21)]
                            statuses=[r['status'] for r in reports]
                            first=next((i+1 for i,s in enumerate(statuses) if s=='assumption_violation'),None)
                            abstained=all(s=='insufficient_coverage' for s in statuses)
                            outcome=('abstained' if abstained else 'pre_event_alarm' if first is not None and first<7
                                     else 'detected' if first is not None else 'no_alarm')
                            rows.append(dict(family=family,weight=weight,initial=label,noise=error,
                                             scenario=scenario,sensors=len(columns),outcome=outcome,
                                             first_alarm=first,delay=first-7 if scenario!='steady' and outcome=='detected' else None,
                                             prefix_hash=hashlib.sha256(samples[:7].tobytes()).hexdigest(),
                                             statuses=statuses,
                                             first_reasons=reports[first-1]['reasons'] if first else []))
    summary=[]
    for scenario in ('steady','cut','forcing','speedup'):
        for sensors in (2,4,8):
            group=[r for r in rows if r['scenario']==scenario and r['sensors']==sensors]
            delays=[r['delay'] for r in group if r['delay'] is not None]
            summary.append(dict(scenario=scenario,sensors=sensors,runs=len(group),
                                **{k:sum(r['outcome']==k for r in group) for k in
                                   ('abstained','pre_event_alarm','detected','no_alarm')},
                                false_alarms=sum(r['first_alarm'] is not None for r in group) if scenario=='steady' else None,
                                median_delay=float(np.median(delays)) if delays else None,
                                max_delay=max(delays) if delays else None))
    protocol=Path(__file__).resolve().parents[1]/'docs/DETECTION_PROTOCOL.md'
    return dict(protocol_sha256=hashlib.sha256(protocol.read_bytes()).hexdigest(),
                numpy=np.__version__,summary=summary,runs=rows)


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='results/detection.json')
    args=parser.parse_args()
    result=run()
    path=Path(args.output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(result['summary']))
