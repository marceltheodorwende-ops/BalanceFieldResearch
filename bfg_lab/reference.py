"""Known-reference residual monitor with full initial calibration."""
import hashlib
import json
from pathlib import Path
import numpy as np
from .diffusion import adjacency, heat_operator


def assess_reference(r, initial, samples, sensors, initial_error=0., sensor_error=0.):
    for value in (r,initial,samples):
        if np.iscomplexobj(value):
            raise ValueError('Real reference and measurements required')
    r=np.asarray(r,dtype=float); x=np.asarray(initial,dtype=float)
    data=np.asarray(samples,dtype=float); indices=np.asarray(sensors)
    if (r.ndim!=2 or r.shape[0]!=r.shape[1] or len(r)<1 or
        not np.isfinite(r).all() or np.any(r < -1e-10) or
        not np.allclose(r,r.T,atol=1e-10,rtol=0) or
        not np.allclose(r.sum(axis=1),1,atol=1e-10,rtol=0)):
        raise ValueError('Finite symmetric stochastic reference operator required')
    if x.shape!=(len(r),) or not np.isfinite(x).all():
        raise ValueError('Full finite initial calibration required')
    if (indices.ndim!=1 or not len(indices) or indices.dtype.kind not in 'iu' or
        np.any(indices<0) or np.any(indices>=len(r)) or len(set(indices.tolist()))!=len(indices)):
        raise ValueError('Unique integer sensor indices required')
    if data.ndim!=2 or data.shape[1]!=len(indices) or len(data)<1 or not np.isfinite(data).all():
        raise ValueError('Finite time-by-sensor samples required')
    if any(not np.isfinite(e) or e<0 for e in (initial_error,sensor_error)):
        raise ValueError('Finite nonnegative scalar error bounds required')
    uncertainty=np.full(len(r),initial_error,dtype=float)
    first=None; rows=[]
    for step,observed in enumerate(data):
        budget=uncertainty[indices]+sensor_error+1e-10
        residual=np.abs(observed-x[indices])
        conflicts=[int(indices[j]) for j in np.flatnonzero(residual>budget)]
        if conflicts and first is None:
            first=step
        rows.append(dict(step=step,max_residual=float(residual.max()),
                         max_budget=float(budget.max()),conflicting_sensors=conflicts))
        x=r@x; uncertainty=np.abs(r)@uncertainty
    return dict(status='reference_inconsistent' if first is not None else 'no_observed_conflict',
                first_alarm=first,history=rows)


def run():
    rng=np.random.default_rng(20260916); rows=[]
    for family in ('path','cycle'):
        for weight in (.5,1.):
            random=rng.uniform(0,1,8); random/=random.sum()
            for label,x0 in [('impulse',np.eye(8)[0]),('random',random)]:
                for error in (0.,.001,.01):
                    noise=rng.uniform(-error,error,(21,8))
                    for scenario in ('steady','cut','forcing','speedup'):
                        a=adjacency(family,8,weight); reference,_=heat_operator(a,.2)
                        r=reference.copy(); x=x0.copy(); history=[x.copy()]
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
                        for sensors in ([0,1],[0,1,4,5],list(range(8))):
                            observed=data[:,sensors]
                            report=assess_reference(reference,data[0],observed,sensors,error,error)
                            first=report['first_alarm']
                            outcome=('pre_event_alarm' if first is not None and first<7 else
                                     'detected' if first is not None else 'no_alarm')
                            rows.append(dict(family=family,weight=weight,initial=label,noise=error,
                                             scenario=scenario,sensors=len(sensors),full_initial_calibration=True,
                                             prefix_hash=hashlib.sha256(observed[:7].tobytes()).hexdigest(),
                                             first_alarm=first,outcome=outcome,
                                             delay=first-7 if scenario!='steady' and outcome=='detected' else None,
                                             history=report['history']))
    summary=[]
    for scenario in ('steady','cut','forcing','speedup'):
        for sensors in (2,4,8):
            group=[r for r in rows if r['scenario']==scenario and r['sensors']==sensors]
            delays=[r['delay'] for r in group if r['delay'] is not None]
            summary.append(dict(scenario=scenario,sensors=sensors,runs=len(group),
                                **{k:sum(r['outcome']==k for r in group) for k in ('pre_event_alarm','detected','no_alarm')},
                                false_alarms=sum(r['first_alarm'] is not None for r in group) if scenario=='steady' else None,
                                median_delay=float(np.median(delays)) if delays else None,
                                max_delay=max(delays) if delays else None))
    protocol=Path(__file__).resolve().parents[1]/'docs/REFERENCE_PROTOCOL.md'
    return dict(protocol_sha256=hashlib.sha256(protocol.read_bytes()).hexdigest(),numpy=np.__version__,
                summary=summary,runs=rows)


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='results/reference.json')
    args=parser.parse_args(); result=run()
    path=Path(args.output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(result['summary']))
