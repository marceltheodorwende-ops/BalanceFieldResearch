"""Conditional diffusion monitor. Partial sensors do not certify global recovery."""
import argparse
import json
from pathlib import Path
import numpy as np
from .diffusion import adjacency, heat_operator

ROUND=1e-10


def assess(samples, total_nodes, model_assumed=False, sample_error=0., target_step=None):
    """Rows are equal-time samples; columns are distinct fixed node sensors.

    sample_error bounds each scalar measurement's absolute error. All node
    coverage and fixed-heat assumptions are caller declarations, not inferred.
    """
    if np.iscomplexobj(samples):
        raise ValueError('Real node samples required')
    data=np.asarray(samples,dtype=float)
    if (data.ndim!=2 or data.shape[0]<2 or data.shape[1]<1 or
        not np.isfinite(data).all()):
        raise ValueError('At least two finite sample rows required')
    if (isinstance(total_nodes,bool) or not isinstance(total_nodes,(int,np.integer)) or
        total_nodes<data.shape[1]):
        raise ValueError('Total nodes must be an integer >= observed node count')
    if not isinstance(model_assumed,(bool,np.bool_)):
        raise ValueError('model_assumed must be boolean')
    if not np.isfinite(sample_error) or sample_error<0:
        raise ValueError('Nonnegative finite scalar error required')
    m=len(data)-1
    horizon=2*m if target_step is None else target_step
    if isinstance(horizon,bool) or not isinstance(horizon,(int,np.integer)) or horizon<m:
        raise ValueError('Integer target step >= current sample step required')
    result=dict(status='insufficient_coverage',reasons=[],forecast=None,
                observed_nodes=data.shape[1],total_nodes=int(total_nodes),current_step=m,
                target_step=int(horizon),sample_error=float(sample_error),
                largest_observed_step_change=float(np.max(np.abs(np.diff(data,axis=0)))))
    if data.shape[1]!=total_nodes:
        result['reasons']=['unobserved_nodes']; return result
    norms=np.linalg.norm(data-data.mean(axis=1,keepdims=True),axis=1)
    margin=np.sqrt(total_nodes)*sample_error
    low=np.maximum(norms-margin,0.); high=norms+margin
    sums=data.sum(axis=1)
    if np.max(sums)-np.min(sums)>2*total_nodes*sample_error+ROUND:
        result['reasons'].append('mass_changed')
    if np.any(low[1:]>high[:-1]+ROUND):
        result['reasons'].append('disagreement_increased')
    if np.any(low[1:-1]**2>high[:-2]*high[2:]+ROUND):
        result['reasons'].append('decay_not_log_convex')
    result['observed_disagreement']=norms.tolist()
    if result['reasons']:
        result['status']='assumption_violation'; return result
    if low[0]<=ROUND:
        result['status']='unresolved_initial_signal'
        result['reasons']=['initial_disagreement_not_resolved']; return result
    if not model_assumed:
        result['status']='model_unverified'
        result['reasons']=['fixed_heat_model_not_asserted']; return result
    # Conservative ratio interval: each norm has absolute error <= sqrt(n)*e.
    qlow=max(0.,min(1.,float(low[-1]/high[0])))
    qhigh=max(0.,min(1.,float(high[-1]/low[0])))
    result['forecast']=dict(lower=qlow**(horizon/m),upper=qhigh,
                            quantity='global_disagreement_relative_to_initial',
                            condition='fixed_symmetric_heat_without_forcing_through_target')
    result['status']='conditional_forecast'
    return result


def experiment():
    rows=[]
    for scenario in ('steady','cut','forcing','speedup'):
        a=adjacency('path',8,1.)
        r,_=heat_operator(a,.2)
        x=np.eye(8)[0]; history=[x.copy()]
        for step in range(1,21):
            if scenario=='cut' and step==7:
                a[3,4]=a[4,3]=0.; r,_=heat_operator(a,.2)
            if scenario=='speedup' and step==7:
                r,_=heat_operator(8*a,.2)
            x=r@x
            if scenario=='forcing' and step==7:
                x[-1]+=.5
            history.append(x.copy())
        data=np.array(history)
        for coverage,columns in [('full',list(range(8))),('partial',[0,1])]:
            observed=data[:,columns]
            before=assess(observed[:6],8,model_assumed=True,target_step=20)
            after=assess(observed,8,model_assumed=True,target_step=40)
            # Evaluation truth is outside assess and never passed to partial monitor.
            target=float(np.linalg.norm(data[-1]-data[-1].mean())/
                         np.linalg.norm(data[0]-data[0].mean()))
            interval=before['forecast']
            rows.append(dict(scenario=scenario,coverage=coverage,before=before,after=after,
                             evaluation_target=target,
                             earlier_interval_contains_target=None if interval is None else
                             bool(interval['lower']-ROUND<=target<=interval['upper']+ROUND)))
    return rows


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--input',type=Path,help='JSON matrix: time rows, distinct node columns')
    parser.add_argument('--nodes',type=int)
    parser.add_argument('--assume-fixed-heat',action='store_true')
    parser.add_argument('--sample-error',type=float,default=0.)
    parser.add_argument('--target-step',type=int)
    parser.add_argument('--output',type=Path,default=Path('results/monitor.json'))
    args=parser.parse_args()
    if args.input:
        if args.nodes is None:
            parser.error('--nodes required with --input')
        result=assess(json.loads(args.input.read_text(encoding='utf-8')),args.nodes,
                      model_assumed=args.assume_fixed_heat,sample_error=args.sample_error,
                      target_step=args.target_step)
    else:
        result=experiment()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(result if args.input else [dict(scenario=r['scenario'],coverage=r['coverage'],
          status=r['after']['status'],reasons=r['after']['reasons'],
          earlier_interval_contains_target=r['earlier_interval_contains_target']) for r in result]))


if __name__=='__main__':
    main()
