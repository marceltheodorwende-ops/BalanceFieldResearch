"""Synthetic symbolic control of force nonidentifiability bump; no measurements."""
import json
from pathlib import Path
import sympy as s
z=s.symbols('z');p=z*z*(1-z*z)**4
assert p.subs(z,0)==s.diff(p,z).subs(z,0)==0
assert s.diff(p,z,2).subs(z,0)==2
for endpoint in [-1,1]:
 for k in range(4):assert s.diff(p,z,k).subs(z,endpoint)==0
out={'status':'passed','control':'symbolic compact C3 polynomial bump; smooth cutoff existence in proof','center_position_velocity':[0,0],'center_acceleration':2,'endpoint_derivatives_order_0_through_3':0,'synthetic_only':True}
Path(__file__).with_name('force_bump_control.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
