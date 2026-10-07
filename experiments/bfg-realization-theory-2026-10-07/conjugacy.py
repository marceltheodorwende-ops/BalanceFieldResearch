"""Explicit scalar BFG conjugacy; mathematical controls, no physical validation."""
import math

def f(y):
    return 2*y*y/((1+y)**2*(1+y*y))

def log_phi(y):
    if not 0<y<1: raise ValueError('scalar branch requires 0<y<1')
    value=math.log(2*y)
    weight=.5
    for _ in range(80):
        value+=weight*(-2*math.log1p(y)-math.log1p(y*y))
        y=f(y);weight*=.5
        if y<1e-150: break
    return value

def observable(y,p):
    if p<=0: raise ValueError('p must be positive')
    return (-log_phi(y))**(-p)

if __name__=='__main__':
    import json
    errors=[];obs=[]
    for i in range(1,1000):
        y=i/1000
        errors.append(abs(log_phi(f(y))-2*log_phi(y)))
        for p in [.01,.1,1,3]:
            obs.append(abs(observable(f(y),p)/observable(y,p)-2**(-p)))
    print(json.dumps(dict(inputs=999,log_conjugacy_max_absolute_residual=max(errors),observable_retention_max_absolute_residual=max(obs),empirical_claim=False),indent=2))
