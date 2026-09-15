"""Early-observation intervals for fixed symmetric heat diffusion, not BFG-specific."""
import hashlib
import json
from pathlib import Path
import numpy as np
from .diffusion import heat_operator


def bounds(q, observed_step, target_step, error=0.):
    if (not np.isfinite(q) or not np.isfinite(error) or error<0 or
        not np.isfinite(observed_step) or not np.isfinite(target_step) or
        observed_step<=0 or target_step<observed_step):
        raise ValueError('Finite q, nonnegative error and 0<m<=H required')
    lower=max(0.,float(q-error)); upper=min(1.,float(q+error))
    if lower>upper:
        raise ValueError('Measurement interval incompatible with a contraction ratio')
    return lower**(target_step/observed_step), upper


def run():
    rng=np.random.default_rng(20260915)
    rows=[]
    for n in (7,9):
        for instance in range(20):
            a=np.zeros((n,n))
            for i in range(n-1):
                a[i,i+1]=a[i+1,i]=rng.uniform(.2,1.2)
            for i in range(n):
                for j in range(i+2,n):
                    if rng.random()<.25:
                        a[i,j]=a[j,i]=rng.uniform(.2,1.2)
            r,_=heat_operator(a,.2)
            impulse=np.eye(n)[0]
            random=rng.uniform(0,1,n); random/=random.sum()
            graph_hash=hashlib.sha256(a.tobytes()).hexdigest()
            for label,x in [('impulse',impulse),('random',random)]:
                z=x-x.mean(); norm=np.linalg.norm(z)
                current=z.copy()
                for _ in range(5):
                    current=r@current
                q=float(np.linalg.norm(current)/norm)
                lo,hi=bounds(q,5,20)
                noisy=[]
                for error in (-.01,0.,.01):
                    low,high=bounds(q+error,5,20,error=.01)
                    noisy.append(dict(measurement_error=error,lower=low,upper=high))
                # Construct every interval before computing the future target.
                for _ in range(15):
                    current=r@current
                target=float(np.linalg.norm(current)/norm)
                for interval in noisy:
                    interval['violation']=max(0.,interval['lower']-target,target-interval['upper'])
                rows.append(dict(n=n,instance=instance,graph_hash=graph_hash,initial=label,
                                 q=q,target=target,lower=lo,upper=hi,
                                 violation=max(0.,lo-target,target-hi),noisy=noisy))
    protocol=Path(__file__).resolve().parents[1]/'docs/EARLY_PROTOCOL.md'
    return dict(protocol_sha256=hashlib.sha256(protocol.read_bytes()).hexdigest(),
                numpy=np.__version__,cases=len(rows),
                max_violation=max(x['violation'] for x in rows),
                max_noisy_violation=max(y['violation'] for x in rows for y in x['noisy']),
                mean_width=float(np.mean([x['upper']-x['lower'] for x in rows])),
                mean_noisy_width=float(np.mean([y['upper']-y['lower'] for x in rows for y in x['noisy']])),
                runs=rows)


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='results/early.json')
    args=parser.parse_args()
    result=run()
    path=Path(args.output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='runs'}))
