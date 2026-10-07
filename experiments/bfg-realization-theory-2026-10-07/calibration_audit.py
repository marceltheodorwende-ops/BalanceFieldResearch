"""Audit a fixed nonlinear scalar energy observable, development data only."""
import csv,gzip,io,json,math,statistics,sys
from pathlib import Path

def ratio_interval(a,b,epsilon=.0005):
    a,b=abs(a),abs(b)
    if min(a,b)<=epsilon or max(a,b)+epsilon>=math.pi:
        raise ValueError('angle domain')
    return ((math.sin((b-epsilon)/2)/math.sin((a+epsilon)/2))**2,
            (math.sin((b+epsilon)/2)/math.sin((a-epsilon)/2))**2)

def main(pairs_path):
    with gzip.open(pairs_path,'rt') as f: pairs=list(csv.DictReader(f))
    for pair in pairs:
        if not pair['recording'].endswith('_1.csv'):
            raise ValueError('holdout forbidden')
        pair['ratio_lo'],pair['ratio_hi']=ratio_interval(float(pair['angle']),float(pair['next_angle']))
    lower=max(pairs,key=lambda p:p['ratio_lo'])
    upper=min(pairs,key=lambda p:p['ratio_hi'])
    fields=['recording','time','angle','next_angle','ratio_lo','ratio_hi']
    result=dict(stage='development-only physical calibration feasibility',pairs=len(pairs),holdout_accessed=False,
                rounding_half_width_rad=.0005,intersection_lower=lower['ratio_lo'],intersection_upper=upper['ratio_hi'],
                common_constant_retention_feasible=lower['ratio_lo']<=upper['ratio_hi'],
                lower_bound_witness={k:lower[k] for k in fields},
                upper_bound_witness={k:upper[k] for k in fields},
                condition_median_retention={str(c):statistics.median(float(p['observed_ratio']) for p in pairs if f'cond{c}' in p['recording']) for c in range(1,4)},
                limitation='Only cleaned rounding uncertainty; not a full sensor-error model or causal confirmation')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main(sys.argv[1])
