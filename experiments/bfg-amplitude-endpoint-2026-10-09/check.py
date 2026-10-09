"""P55 synthetic exact/asymptotic controls; no measurement or holdout reads."""
import json
from pathlib import Path
import sympy as sp
import mpmath as mp
t,q=sp.symbols('t q',positive=True)
h=t*q
u=[t+h,t-h];c=[1/(1+x) for x in u];b=[x*y for x,y in zip(u,c)]
m=t*t+h*h*(1-t)/(1+t);alpha=m/(1+m)
ev=[alpha*x*x+(1-alpha)*y*y for x,y in zip(c,b)]
A=sp.cancel(sum(ev)/2);V=sp.cancel((ev[0]-ev[1])/2)
G2=sp.cancel((alpha*c[0]*c[1]+(1-alpha)*b[0]*b[1])**2/(ev[0]*ev[1]))
assert sp.simplify(sp.limit(A/t**2,t,0)-2*(1+q*q))==0
assert sp.simplify(sp.limit(V/t**2,t,0)-2*q)==0
assert sp.simplify(sp.limit(G2,t,0)-1/(1+q*q+q**4))==0
assert sp.cancel(G2.subs(q,0)-1)==0
assert sp.cancel(G2-G2.subs(q,-q))==0
mp.mp.dps=80
fa=sp.lambdify((t,q),A,'mpmath');fv=sp.lambdify((t,q),V,'mpmath');fg=sp.lambdify((t,q),G2,'mpmath')
errors=[]
for qq in ['0','.1','.5','.9','1']:
    x=mp.mpf('1e-12');z=mp.mpf(qq)
    errors += [abs(fa(x,z)/x**2-2*(1+z*z)),abs(fv(x,z)/x**2-2*z),abs(fg(x,z)-1/(1+z*z+z**4))]
assert max(errors)<mp.mpf('1e-9')
# Analytic positive-endpoint witness T=delta,R=delta²,eta=.1,s*=.3.
# It satisfies the initial gate for these deltas but fails invariance by order.
rows=[]
for d in [mp.mpf('1e-3'),mp.mpf('1e-5'),mp.mpf('1e-7')]:
    s=mp.mpf('.3')+d;hh=d*d*mp.sqrt(1+mp.mpf('.04')*s*s);z=hh/d
    sn=s*mp.sqrt(fg(d,z));rows.append({'delta':str(d),'graph_T_successor_over_T':float((sn-mp.mpf('.3'))/d),'canonical_T_successor_over_T':float(fa(d,z)/d)})
assert rows[-1]['graph_T_successor_over_T']>.99
assert rows[-1]['canonical_T_successor_over_T']<1e-5
out={'symbolic_checks':5,'asymptotic_cases':5,'max_asymptotic_error':str(max(errors)),'analytic_graph_countercheck':rows,'kind':'synthetic math/code only','holdout_accessed':False,'physical_force_derived':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
