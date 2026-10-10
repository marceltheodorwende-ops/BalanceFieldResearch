"""Independent exact-rational vertex and hidden-force verification."""
import json, random
from fractions import Fraction as Q
from pathlib import Path
import sympy as s
rng=random.Random(7201); maxdiff=0
for _ in range(200):
    z0=Q(rng.randrange(-100,100),100); z1=Q(rng.randrange(-100,100),100)
    e=Q(3,1000); H=Q(rng.randrange(2,100),100); eta=Q(1,10000)
    independent=[]
    for q0 in (z0-e,z0+e):
        for q1 in (z1-e,z1+e):
            for dt0 in (-eta,eta):
                for dt1 in (-eta,eta): independent.append((q1-q0)/(H+dt1-dt0))
    d=z1-z0
    formula=[(d+sig*2*e)/(H+tau*2*eta) for sig in (-1,1) for tau in (-1,1)]
    assert min(formula)==min(independent) and max(formula)==max(independent)
t,B,delta,n=s.symbols('t B delta n',positive=True)
q=delta/(8*(1+n))*s.cos(B*n*t/delta)
assert s.simplify(s.diff(q,t,2).subs(t,0)+B**2*n**2/(8*delta*(1+n)))==0
assert s.limit(B**2*n**2/(8*delta*(1+n)),n,s.oo)==s.oo
h=s.symbols('h',positive=True)
x=s.symbols('x',real=True)
assert s.simplify((s.integrate(-x,(x,-h/2,0))+s.integrate(x,(x,0,h/2)))/h-h/4)==0
out={'status':'passed','exact_vertex_cases':200,'symbolic_acceleration_identity':True,'symbolic_unbounded_force_limit':True,'symbolic_midpoint_bound':True,'synthetic_only':True}
Path(__file__).with_name('verification.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
