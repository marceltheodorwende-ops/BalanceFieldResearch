"""Independent synthetic derivative/feedback controls; no measurement claims."""
import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.linalg import expm
x=s.symbols('x',positive=True)
f=2*x*x/((1+x)**2*(1+x*x))
long=s.diff(f,x).subs(x,s.Rational(1,2))
trans=(2*x*(1-x)/((1+x)**3*(1+x*x))).subs(x,s.Rational(1,2))
assert long==s.Rational(224,675) and trans==s.Rational(16,135)
def g(v):
    lc=np.sum(1/(1+v));lb=np.sum(v*v/(1+v));alpha=lb/(lc+lb)
    return (alpha+(1-alpha)*v*v)/(1+v)**2
J=np.array([[float((long+trans)/2),float((long-trans)/2)],
            [float((long-trans)/2),float((long+trans)/2)]])
v=np.array([.5,.5]);eps=1e-6
fd=np.column_stack([(g(v+eps*np.eye(2)[i])-g(v-eps*np.eye(2)[i]))/(2*eps) for i in range(2)])
fd_error=float(np.max(np.abs(J-fd)));assert fd_error<1e-8
errors=[]
for c in (1,2):
    A=np.array([[0.,1.],[-4.*c,-.5]])
    for tau in (.01,.2,np.pi/np.sqrt(4*c-.5**2/4)):
        M=expm(tau*A);Dd=np.linalg.solve(J,M)-np.eye(2)
        error=float(np.max(np.abs(J@(np.eye(2)+Dd)-M)))
        assert error<1e-12
        errors.append(error)
result={'kind':'synthetic mathematics control','long':str(long),'trans':str(trans),
        'determinant':str(long*trans),'baseline_input':'29/90',
        'endogenous_fd_error':fd_error,'feedback_tangent_max_error':max(errors),
        'rival_and_clock_cases':len(errors),'empirical_confirmation':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
