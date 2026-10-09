"""P65 synthetic symbolic controls; not a selected physical model."""
import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.interpolate import CubicHermiteSpline
x,p,c=s.symbols('x p c',positive=True);A=s.Function('A')(x);v=s.Function('v')(x);w=s.Function('w')(x)
Q=A*s.cos(p);V=(v*s.diff(A,x)*s.cos(p)-A*w*s.sin(p))/c
B=v*s.diff(A,x);C=A*w
det=s.det(s.Matrix([[s.diff(Q,x),s.diff(Q,p)],[s.diff(V,x),s.diff(V,p)]]))
expected=((A*s.diff(B,x)-s.diff(A,x)*B)*s.sin(p)*s.cos(p)-s.diff(A,x)*C*s.cos(p)**2-A*s.diff(C,x)*s.sin(p)**2)/c
assert s.simplify(det-expected)==0
R=(v*s.diff(V,x)+w*s.diff(V,p))/c
rex=((v*v*s.diff(A,x,2)+v*s.diff(v,x)*s.diff(A,x)-A*w*w)*s.cos(p)-(2*v*s.diff(A,x)*w+v*A*s.diff(w,x))*s.sin(p))/c**2
assert s.simplify(R-rex)==0
a,o=s.symbols('a o',positive=True)
assert s.simplify(expected.subs(A,a).doit()+a*a*s.diff(w,x)*s.sin(p)**2/c)==0
assert s.simplify(expected.subs({A:a,w:o}).doit())==0
# Illustrative finite printed channels: exact Hermite matches for both clocks.
times=np.array([0,.1,.3,.5]);angles=np.array([.2,.19,.15,.11]);vel=np.array([-.1,-.12,-.21,-.17])
errors=[]
for clock in [.01,.37]:
    u=2+times/clock;H=CubicHermiteSpline(u,angles,clock*vel)
    err=float(max(np.max(abs(H(u)-angles)),np.max(abs(H(u,1)/clock-vel))))
    assert err<1e-12;errors.append({'event_duration':clock,'sample_error':err})
res={'kind':'synthetic observable/force/clock controls','symbolic_checks':4,
     'Hermite_clock_cases':errors,'physical_clock_identified':False,'sine_force_derived':False,
     'controls_are_not_measurements':True,'holdout_accessed':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(json.dumps(res))
