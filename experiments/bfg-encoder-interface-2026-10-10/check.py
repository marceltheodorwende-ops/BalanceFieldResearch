"""Synthetic mathematics controls only; no dataset or network access."""
import json, math, random
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def enclosure(d,e,H,eta):
    if H<=2*eta: raise ValueError('positive duration lacks positive lower bound')
    v=[x/t for x in (d-2*e,d+2*e) for t in (H-2*eta,H+2*eta)]
    return min(v),max(v)

def run():
    rng=random.Random(72); worst=0
    for i in range(1000):
        delta=2*math.pi/(2000 if i%2 else 4000)
        eps=.0002; r=.0005; eta=.0001
        t0=rng.uniform(-1,1); h=rng.uniform(.02,1); q0=rng.uniform(-2,2)
        v=rng.uniform(-3,3); acc=rng.uniform(-2,2)
        q1=q0+v*h+acc*h*h/2
        z=[]
        for q in (q0,q1):
            analog=q+rng.uniform(-eps,eps)
            digit=delta*math.floor(analog/delta+.5)
            z.append(digit+rng.uniform(-r,r))
        H=h+rng.uniform(-eta,eta)-rng.uniform(-eta,eta)
        lo,hi=enclosure(z[1]-z[0],delta/2+eps+r,H,eta)
        mean=(q1-q0)/h
        assert lo-1e-12<=mean<=hi+1e-12
        mid=v+acc*h/2
        assert lo-abs(acc)*(H+2*eta)/4-1e-12<=mid<=hi+abs(acc)*(H+2*eta)/4+1e-12
        worst=max(worst,hi-lo)
    def count(x,step): return math.floor(x/step+F(1,2))
    ys=[F(13,250),F(27,500)]; step=F(1,100)
    f=lambda y:2*y*y/((1+y)**2*(1+y*y))
    assert [count(y,step) for y in ys]==[5,5]
    assert [count(f(y),step) for y in ys]==[0,1]
    assert [count(q+F(1,2),F(1)) for q in [-F(1,4),F(1,4)]]==[0,1]
    assert count(F(1,2),F(1))==1
    rejected=0
    for H in [0,.0001,.0002]:
        try: enclosure(1,.01,H,.0001)
        except ValueError: rejected+=1
    assert rejected==3
    # Analytic Lipschitz integral: 2*(h/2)^2/2 / h = h/4.
    for h in [F(1,100),F(1),F(10)]: assert 2*(h/2)**2/2/h==h/4
    ns=[1,10,100,1000,10000]
    acceleration=[F(n*n,8*(1+n)) for n in ns] # delta=B=1
    for n in ns:
        a=F(1,8*(1+n)); assert a<F(1,2) and a*n<F(1,8)
    assert all(a<b for a,b in zip(acceleration,acceleration[1:]))
    return {'status':'passed','synthetic_only':True,'endpoint_cases':1000,'maximum_interval_width':worst,
        'canonical_successors':[float(f(y)) for y in ys],'canonical_counts':[0,1],
        'invalid_duration_cases':rejected,'acceleration_sequence':[float(a) for a in acceleration]}
if __name__=='__main__':
    out=run(); (ROOT/'controls.json').write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out))
