"""Analytic fallback for exact two-node observations at zero and one later time."""
from fractions import Fraction as F
from .certified import _number
from .certified_boundary import assess_boundary


def assess_exact_pair(weight_lower,weight_upper,initial,samples,times,sensors,
                      initial_error=0,sensor_error=0,terms=24,max_boxes=255,
                      max_depth=20,max_candidates=81,candidate_terms=64,log_terms=64):
    if type(log_terms)!=int or not 1<=log_terms<=256:
        raise ValueError('Integer log budget 1..256 required')
    previous=assess_boundary(weight_lower,weight_upper,initial,samples,times,sensors,
        initial_error,sensor_error,terms,max_boxes,max_depth,max_candidates,candidate_terms)
    if previous['status']!='unresolved':
        return previous
    if (len(initial)!=2 or len(times)!=2 or set(sensors)!={0,1}
            or _number(initial_error)!=0 or _number(sensor_error)!=0):
        return previous
    x=list(map(_number,initial)); t=_number(times[1])
    data=[dict(zip(sensors,map(_number,row))) for row in samples]
    def excluded(rule,**details):
        return dict(status='healthy_family_excluded',certificate_kind='analytic_two_node',
                    certificate=dict(rule=rule,**details))
    if any(data[0][i]!=x[i] for i in (0,1)):
        return excluded('initial_identity')
    y=[data[1][i] for i in (0,1)]
    if sum(y)!=sum(x):
        return excluded('mass_conservation',initial_sum=str(sum(x)),observed_sum=str(sum(y)))
    d=x[0]-x[1]
    if d==0:
        return previous  # Existing checker already handles constant trajectories.
    r=(y[0]-y[1])/d
    if r<=0 or r>1:
        return excluded('strict_positive_decay',ratio=str(r),time=str(t))
    # -log(r)/(2t) = atanh((1-r)/(1+r))/t.
    z=(1-r)/(1+r); power=z; lower=F(0)
    for k in range(log_terms):
        lower+=power/(2*k+1)
        power*=z*z
    upper=lower+power/((2*log_terms+1)*(1-z*z))
    lower/=t; upper/=t
    lo=_number(weight_lower[0][1]); hi=_number(weight_upper[0][1])
    bounds=dict(lower=str(lower),upper=str(upper),log_terms=log_terms)
    if upper<lo or lower>hi:
        return excluded('unique_weight_outside_box',ratio=str(r),time=str(t),weight_bounds=bounds)
    if lo<=lower and upper<=hi:
        return dict(status='compatible_witness',certificate_kind='analytic_two_node',
                    symbolic_witness=dict(expression='-log(ratio)/(2*time)',ratio=str(r),
                        time=str(t),initial=[str(v) for v in x],weight_bounds=bounds),
                    certificate=dict(rule='mass_and_decay',initial_sum=str(sum(x)),
                                     observed_sum=str(sum(y))))
    previous['analytic_reason']='log_enclosure_overlaps_weight_boundary'
    previous['analytic_weight_bounds']=bounds
    return previous


if __name__=='__main__':
    import argparse,json
    from pathlib import Path
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,default=Path('results/certified_exact.json'))
    args=p.parse_args()
    r=assess_exact_pair(**json.loads(args.input.read_text(encoding='utf-8'),parse_float=str))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(r['status'])
