"""Paired synthetic comparison; no predictive score or empirical validation."""
import hashlib
import json
from pathlib import Path
import numpy as np
from .minimal import multimode_seed, simulate

RULES = ('packet', 'negative_spectrum', 'carried')


def run():
    runs=[]
    # 2 geometries x 2 capacities x 2 retentions x 3 perturbations = 24 cases.
    for mixed in (False,True):
        for scale in (.75,1.):
            for retention in (.8,1.):
                for epsilon in (-1e-6,0.,1e-6):
                    state=multimode_seed()
                    if mixed:
                        state['y']=np.array([[2.,.2,0.],[.2,1.,.1],[0.,.1,1.]])
                        state['coherence']=np.array([[1.,.1,0.],[.1,1.,0.],[0.,0.,1.]])
                    state['difference'] *= scale*(1+epsilon)
                    state['d'][0] += epsilon
                    encoded=json.dumps({k:v.tolist() for k,v in state.items()},sort_keys=True)
                    digest=hashlib.sha256(encoded.encode()).hexdigest()
                    case=f'mixed={mixed},scale={scale},retention={retention},epsilon={epsilon}'
                    for rule in RULES:
                        result=simulate(state,steps=12,retention=retention,transport_rule=rule)
                        runs.append(dict(case=case,input_hash=digest,rule=rule,mixed=mixed,
                                         scale=scale,retention=retention,epsilon=epsilon,**result))
    summary=[]
    for rule in RULES:
        rows=[r for r in runs if r['rule']==rule]
        summary.append(dict(rule=rule,cases=len(rows),
                            stopped=sum(r['status']=='formation_rejected' for r in rows),
                            budget_reached=sum(r['status']=='step_limit' for r in rows),
                            min_transitions=min(r['transitions'] for r in rows),
                            max_transitions=max(r['transitions'] for r in rows)))
    return dict(protocol='paired-toy-v1',steps=12,numpy=np.__version__,
                summary=summary,runs=runs)


if __name__ == '__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='results/comparison.json')
    args=parser.parse_args()
    result=run()
    path=Path(args.output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(result['summary']))
