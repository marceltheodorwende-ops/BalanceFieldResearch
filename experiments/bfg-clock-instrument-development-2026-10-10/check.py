"""Independent controls for P69; synthetic inputs are not measurements."""
import json,platform
from pathlib import Path
import numpy as np
import scipy
import sympy as s
from scipy.integrate import solve_ivp
from scipy.optimize import lsq_linear
from analysis import damping_fit,integrate,vector_rhs

q,w,k,g,beta=s.symbols('q w k g beta',real=True)
b=s.Function('b')(q); F=-k*s.sin(q)-g*b*w-beta*s.Abs(w)*w
E=w*w/2+k*(1-s.cos(q))
expr=s.diff(E,q)*w+s.diff(E,w)*F+g*b*w*w+beta*s.Abs(w)*w*w
assert s.simplify(expr)==0
# Exact weak closure of a mechanical flow and independent integrator reference.
controls=[]
for model,cosflag,bn in [('clock_cos',True,0.),('viscous',False,0.),('mixed_drag',False,.3)]:
    kn,gn=3.,.4; z0=np.array([[.7,.1]])
    rhs=lambda t,y:vector_rhs(y.reshape(1,2),np.array([kn]),np.array([gn]),np.array([bn]),np.array([cosflag]))[0]
    ref=solve_ivp(rhs,[0,1.],z0[0],method='DOP853',rtol=2e-12,atol=2e-13,dense_output=True)
    assert ref.success
    rk=integrate(z0,np.array([kn]),np.array([gn]),np.array([bn]),np.array([cosflag]),.005,duration=1.)[:,0]
    t=np.arange(101)*.01
    error=float(np.max(abs(rk-ref.sol(t).T)))
    assert error<2e-8
    tx=np.linspace(0,.5,1001); Q,W=ref.sol(tx)
    phi=np.sin(2*np.pi*tx)**2; phip=2*np.pi*np.sin(4*np.pi*tx)
    damping=np.cos(Q/2) if cosflag else np.ones_like(Q)
    weak=float(np.trapezoid(W*phip-kn*np.sin(Q)*phi-gn*damping*W*phi-bn*abs(W)*W*phi,tx))
    assert abs(weak)<2e-5
    controls.append(dict(model=model,independent_DOP853_error=error,weak_identity_residual=weak))
# Active-face LS is independently compared with SciPy's bounded solver.
D=np.array([[1.,.2],[.4,1.],[-.6,-.2],[.3,1.2]])
fits=[]
for target in [D@np.array([.4,.2]),D@np.array([-.3,.7]),D@np.array([3.,-.2])]:
    own=damping_fit(D,target,1.)
    other=lsq_linear(D,target,bounds=([0.,0.],[1.,np.inf]),tol=1e-13)
    assert other.success
    discrepancy=float(np.linalg.norm(D@own-target)**2-np.linalg.norm(D@other.x-target)**2)
    assert abs(discrepancy)<2e-9
    fits.append(dict(own=own.tolist(),independent=other.x.tolist(),objective_discrepancy=discrepancy))
# A known exact kinematic path with adversarial errors saturates the bound.
t=np.linspace(0,.5,51); W=t*t/10; Q=t**3/30; eps=.0005
res=(Q[-1]-eps)-(Q[0]+eps)-np.trapezoid(W+eps,t)
bound=2*eps+.5*eps+.5*.01**2*.2/12
assert abs(abs(res)-bound)<1e-14
# One weak moment can miss a nonzero smooth between-node force residual.
tx=np.linspace(0,.5,10001); phi=np.sin(2*np.pi*tx)**2
hidden=np.sin(4*np.pi*(tx-.25))*np.sin(2*np.pi*tx)**4
moment=float(np.trapezoid(hidden*phi,tx))
assert abs(moment)<1e-14 and np.max(abs(hidden))>.2
out=dict(symbolic_energy_identity=True,synthetic_ODE_controls=controls,bounded_LS_controls=fits,
    adversarial_kinematic_residual=float(res),rigorous_kinematic_bound=float(bound),
    hidden_residual_moment=moment,versions=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__,sympy=s.__version__),
    scope='Implementation/mathematics controls only; no real measurements')
Path(__file__).with_name('controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out))
