"""Reference mismatch and known initial excitation: paired sensitivity study."""
import hashlib
import json
from pathlib import Path
import numpy as np
from .diffusion import adjacency, heat_operator
from .reference import assess_reference


def run():
    rng=np.random.default_rng(20260917); rows=[]
    for family in ('path','cycle'):
        for weight in (.5,1.):
            sensor_noise=rng.uniform(-.001,.001,(21,8))
            calibration_noise=rng.uniform(-.001,.001,8)
            graph=adjacency(family,8,weight)
            for scale in (.9,1.,1.1):
                reference,_=heat_operator(scale*graph,.2)
                for calibration,bias,budget in [('unbiased',0.,.001),('bounded_bias',.02,.021),('understated',.02,.001)]:
                    for probe in (False,True):
                        x0=np.ones(8)/8
                        if probe:
                            x0[0]+=.5
                        initial=x0+calibration_noise; initial[0]+=bias
                        for cut in (False,True):
                            actual=graph.copy()
                            if cut:
                                actual[3,4]=actual[4,3]=0.
                            r,_=heat_operator(actual,.2)
                            x=x0.copy(); history=[x.copy()]
                            for _ in range(20):
                                x=r@x; history.append(x.copy())
                            samples=np.array(history)+sensor_noise
                            report=assess_reference(reference,initial,samples,list(range(8)),budget,.001)
                            rows.append(dict(family=family,weight=weight,reference_scale=scale,
                                             calibration=calibration,probe=probe,cut=cut,
                                             first_alarm=report['first_alarm'],status=report['status'],
                                             declared_initial_error=budget,
                                             samples_hash=hashlib.sha256(samples.tobytes()).hexdigest(),
                                             max_residual=max(h['max_residual'] for h in report['history'])))
    summary=[]
    for scale in (.9,1.,1.1):
        for calibration in ('unbiased','bounded_bias','understated'):
            for probe in (False,True):
                for cut in (False,True):
                    group=[r for r in rows if (r['reference_scale'],r['calibration'],r['probe'],r['cut'])==(scale,calibration,probe,cut)]
                    alarms=[r['first_alarm'] for r in group if r['first_alarm'] is not None]
                    summary.append(dict(reference_scale=scale,calibration=calibration,probe=probe,cut=cut,
                                        runs=len(group),alarms=len(alarms),no_alarm=len(group)-len(alarms),
                                        median_first_alarm=float(np.median(alarms)) if alarms else None))
    protocol=Path(__file__).resolve().parents[1]/'docs/REFERENCE_STRESS_PROTOCOL.md'
    return dict(protocol_sha256=hashlib.sha256(protocol.read_bytes()).hexdigest(),
                numpy=np.__version__,summary=summary,runs=rows)


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='results/reference_stress.json')
    args=parser.parse_args(); result=run()
    path=Path(args.output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps(result['summary']))
