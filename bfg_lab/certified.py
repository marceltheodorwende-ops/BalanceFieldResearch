"""Exact rational enclosures for a fixed undirected heat-reference family.

This is a sufficient exclusion/witness procedure, not a complete feasibility solver.
Decimal strings are interpreted exactly; float inputs use their decimal str().
"""
from fractions import Fraction as F


def _number(x):
    if isinstance(x,bool):
        raise ValueError('Boolean is not a measurement')
    try:
        return F(str(x))
    except (ValueError,ZeroDivisionError) as exc:
        raise ValueError('Finite rational or decimal input required') from exc


def _trajectory(a,x,t,terms):
    n=len(a); degree=[sum(row) for row in a]; rate=max(degree)
    if t==0 or rate==0 or all(v==x[0] for v in x):
        return [(v,v) for v in x]
    u=rate*t
    if u>=terms+2:
        return None
    # B=I-L/rate is nonnegative row stochastic. Propagate a nonnegative shift.
    base=min(x); width=max(x)-base
    b=[[a[i][j]/rate if i!=j else 1-degree[i]/rate for j in range(n)] for i in range(n)]
    z=[v-base for v in x]; total=z.copy(); coefficient=F(1); scalar=F(1)
    for k in range(1,terms+1):
        z=[sum(b[i][j]*z[j] for j in range(n)) for i in range(n)]
        coefficient*=u/k; scalar+=coefficient
        total=[total[i]+coefficient*z[i] for i in range(n)]
    # exp(u) tail <= first omitted term / (1-u/(N+2)).
    tail=(coefficient*u/(terms+1))/(1-u/(terms+2))
    return [(base+v/(scalar+tail),base+min(width,(v+width*tail)/scalar)) for v in total]


def assess_family(weight_lower,weight_upper,initial,samples,times,sensors,
                  initial_error=0,sensor_error=0,terms=24):
    lo=[[ _number(v) for v in row] for row in weight_lower]
    hi=[[ _number(v) for v in row] for row in weight_upper]
    n=len(lo)
    if not n or len(hi)!=n or any(len(row)!=n for row in lo+hi):
        raise ValueError('Square weight boxes required')
    for i in range(n):
        for j in range(n):
            if lo[i][j]<0 or hi[i][j]<lo[i][j] or lo[i][j]!=lo[j][i] or hi[i][j]!=hi[j][i]:
                raise ValueError('Symmetric nonnegative ordered weight bounds required')
        if lo[i][i]!=0 or hi[i][i]!=0:
            raise ValueError('No self loops')
    x=[_number(v) for v in initial]; ts=[_number(v) for v in times]
    data=[[_number(v) for v in row] for row in samples]
    indices=list(sensors)
    if (len(x)!=n or not ts or ts[0]!=0 or any(b<=a for a,b in zip(ts,ts[1:])) or
        len(data)!=len(ts) or any(len(row)!=len(indices) for row in data)):
        raise ValueError('Matching initial state and increasing times starting at zero required')
    if not indices or any(type(i)!=int or not 0<=i<n for i in indices) or len(set(indices))!=len(indices):
        raise ValueError('Unique integer node indices required')
    ex,ey=_number(initial_error),_number(sensor_error)
    if ex<0 or ey<0 or type(terms)!=int or not 0<=terms<=128:
        raise ValueError('Nonnegative errors and integer series budget 0..128 required')
    a=[[(lo[i][j]+hi[i][j])/2 for j in range(n)] for i in range(n)]
    # Infinity-norm Duhamel bound. Center at midpoint of extrema, not a fitted state.
    eta=2*max(sum((hi[i][j]-lo[i][j])/2 for j in range(n)) for i in range(n))
    contrast=(max(x)-min(x))/2
    witness=True; rows=[]
    for k,t in enumerate(ts):
        intervals=_trajectory(a,x,t,terms)
        if intervals is None:
            return dict(status='unresolved',reason='series_budget_insufficient',time_index=k,history=rows)
        family_error=ex+t*eta*contrast
        for j,i in enumerate(indices):
            left,right=intervals[i]; observed=data[k][j]
            lower=left-family_error-ey; upper=right+family_error+ey
            record=dict(time=str(t),sensor=i,nominal_lower=str(left),nominal_upper=str(right),
                        observation=str(observed),healthy_lower=str(lower),healthy_upper=str(upper))
            rows.append(record)
            if observed<lower or observed>upper:
                return dict(status='healthy_family_excluded',certificate=record,history=rows)
            # One fixed witness (midpoint weights and nominal initial state) for ALL times.
            witness &= observed-ey<=left and right<=observed+ey
    if witness:
        return dict(status='compatible_witness',witness=dict(weights=[[str(v) for v in row] for row in a],
                    initial=[str(v) for v in x]),history=rows)
    return dict(status='unresolved',reason='outer_overlap_without_certified_witness',history=rows)


if __name__=='__main__':
    import argparse,json
    from pathlib import Path
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,default=Path('results/certified.json'))
    args=p.parse_args()
    payload=json.loads(args.input.read_text(encoding='utf-8'),parse_float=str)
    result=assess_family(**payload)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(result['status'])
