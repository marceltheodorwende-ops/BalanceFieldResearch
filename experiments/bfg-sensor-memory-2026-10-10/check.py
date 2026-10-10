"""P70 independent synthetic controls. No empirical data or network access."""
import hashlib
import json
import platform
from pathlib import Path
import numpy as np
import scipy
import sympy as s
from scipy.integrate import solve_ivp
from scipy.linalg import expm
from scipy.optimize import root

HERE = Path(__file__).resolve().parent
q, v, th, k, g = s.symbols('q v theta kappa gamma', real=True)
f = -k*s.sin(q)-g*s.cos(q/2)*v
F = s.Matrix([v, f]); z = s.Matrix([q, v])
T = z+th*F; D = T.jacobian(z); A = (D*F)[1]
identities = []
def exact(name, value):
    assert s.simplify(value) == 0, (name, value)
    identities.append(name)
exact('kinematic pushforward', (D*F)[0]-T[1])
exact('general determinant', D.det()-(1+th*s.diff(f,v)-th**2*s.diff(f,q)))
expanded = f+th*(-k*s.cos(q)*v+g*s.sin(q/2)*v**2/2
                 +g*k*s.cos(q/2)*s.sin(q)+g**2*s.cos(q/2)**2*v)
exact('nonlinear acceleration', A-expanded)
Q,W,x,y=s.symbols('Q W x y',real=True)
jet=s.Matrix([x,y,(Q-x)/th,(W-y)/th])
exact('four-state jet determinant',jet.jacobian([Q,W,x,y]).det()-1/th**2)
xd, yd, wd = s.symbols('xd yd wd',real=True)
exact('compatibility defect equation', (W-xd)/th-(W-y)/th+(xd-y)/th)
J=s.Matrix([[0,1],[-k,-g]]); S=s.eye(2)+th*J
assert all(s.simplify(e)==0 for e in S*J-J*S)
identities.append('harmonic commutation')
exact('harmonic inverse determinant',S.det()-(1-th*g+th**2*k))
target=-k*s.sin(th*v)-g*(1-th*g)*v*s.cos(th*v/2)
exact('fixed sine law nonpreservation coefficient',
      s.diff(target,v,3).subs(v,0)-(k*th**3+3*g*(1-th*g)*th**2/4))
a,om=s.symbols('a omega',positive=True)
h=a/(1+s.I*om*th)
exact('reference response-time inverse',-s.im(h)/(om*s.re(h))-th)
exact('reference gain inverse',(s.re(h)**2+s.im(h)**2)/s.re(h)-a)
exact('singular chart counterexample',D.det().subs({g:0,q:s.pi,v:0,th:1/s.sqrt(k)}))

harmonic=[]
j=np.array([[0.,1.],[-4.,-.15]]);z0=np.array([.4,.2])
for theta in [.02,.1,.5]:
    S0=np.eye(2)+theta*j;Z0=S0@z0
    def rhs(t,u): return np.r_[j@u[:2],(u[:2]-u[2:])/theta]
    sol=solve_ivp(rhs,[0,2],np.r_[Z0,z0],method='DOP853',
                  rtol=2e-12,atol=2e-14,dense_output=True)
    assert sol.success
    tt=np.linspace(0,2,81)
    exact_z=np.stack([expm(t*j)@z0 for t in tt],axis=1)
    error=float(np.max(abs(sol.sol(tt)[2:]-exact_z)))
    true_error=float(np.max(abs(sol.sol(tt)[:2]-S0@exact_z)))
    assert max(error,true_error)<2e-8
    # Inconsistent memory creates precisely the predicted transient.
    obs0=z0+np.array([.01,-.02])
    bad=solve_ivp(rhs,[0,2],np.r_[Z0,obs0],method='DOP853',
                  rtol=2e-12,atol=2e-14,dense_output=True)
    ub=bad.sol(tt)
    defect=(ub[0]-ub[2])/theta-ub[3]
    expected=((Z0[0]-obs0[0])/theta-obs0[1])*np.exp(-tt/theta)
    derr=float(np.max(abs(defect-expected)));assert derr<2e-8
    harmonic.append(dict(theta=theta,output_error=error,true_state_error=true_error,
                         defect_error=derr,determinant=float(np.linalg.det(S0))))

fn=s.lambdify((q,v),F.subs({k:4.,g:.15}),'numpy')
df=s.lambdify((q,v),F.jacobian(z).subs({k:4.,g:.15}),'numpy')
def field(z): return np.array(fn(*z),float).reshape(2)
def jac(z): return np.array(df(*z),float)
def tr(z,theta): return z+theta*field(z)
def dt(z,theta): return np.eye(2)+theta*jac(z)
def inv(Z,theta):
    r=root(lambda z:tr(z,theta)-Z,Z,jac=lambda z:dt(z,theta),tol=1e-11)
    assert np.max(abs(tr(r.x,theta)-Z))<1e-10
    return r.x
def solve(z,duration):
    def rhs(t,u):return np.r_[field(u[:2]),(jac(u[:2])@u[2:].reshape(2,2)).ravel()]
    sol=solve_ivp(rhs,[0,duration],np.r_[z,np.eye(2).ravel()],
                  method='DOP853',rtol=2e-12,atol=2e-14)
    assert sol.success
    return sol.y[:2,-1],sol.y[2:,-1].reshape(2,2)
nonlinear=[]
for theta,z0 in [(.03,np.array([.4,.2])),(.12,np.array([1.,-.3])),(.25,np.array([2.2,.4]))]:
    Z0=tr(z0,theta)
    def aug_rhs(t,u):
        base=inv(u[:2],theta)
        G=dt(base,theta)@field(base)
        return np.r_[G,(u[:2]-u[2:])/theta]
    aug=solve_ivp(aug_rhs,[0,1],np.r_[Z0,z0],method='DOP853',rtol=2e-12,atol=2e-14)
    assert aug.success
    ze,_=solve(z0,1)
    err=float(np.max(abs(aug.y[:,-1]-np.r_[tr(ze,theta),ze])))
    assert err<2e-8
    # Synthetic state-dependent duration checks general F DC interface only.
    C=lambda z:.4+.04*z[0]
    re,M=solve(z0,C(z0));dc=np.array([.04,0])
    Rjac=M+np.outer(field(re),dc)
    analytic=dt(re,theta)@Rjac@np.linalg.inv(dt(z0,theta))
    def Rtheta(Z):
        base=inv(Z,theta);end,_=solve(base,C(base));return tr(end,theta)
    eps=1e-5
    finite=np.column_stack([(Rtheta(Z0+eps*np.eye(2)[i])-Rtheta(Z0-eps*np.eye(2)[i]))/(2*eps) for i in range(2)])
    terr=float(np.max(abs(finite-analytic)));assert terr<2e-6
    missing=dt(re,theta)@M@np.linalg.inv(dt(z0,theta))
    missing_error=float(np.max(abs(finite-missing)));assert missing_error>1e-3
    wrong=-4*np.sin(Z0[0])-.15*np.cos(Z0[0]/2)*Z0[1]
    force_difference=float((dt(z0,theta)@field(z0))[1]-wrong)
    nonlinear.append(dict(theta=theta,start=z0.tolist(),endpoint_error=err,
                          return_tangent_error=terr,omitted_clock_term_error=missing_error,
                          start_determinant=float(np.linalg.det(dt(z0,theta))),
                          fixed_sine_acceleration_difference=force_difference))

def recover(H,omega):
    return np.array([-H.imag/(omega*H.real),abs(H)**2/H.real])
calibration=[]
rng=np.random.default_rng(70)
for omega,theta,gain in [(2.,.03,1.2),(20.,.12,.8),(100.,10.,1.)]:
    H=gain/(1+1j*omega*theta)
    rt_error=float(np.max(abs(recover(H,omega)-[theta,gain])))
    assert rt_error<1e-10
    epsilon=H.real/4;r=H.real-epsilon;B=abs(H.imag)+epsilon
    adverse=0.
    for _ in range(100):
        dx,dy=rng.uniform(-epsilon,epsilon,2)
        rec=recover(H+dx+1j*dy,omega);err=abs(rec-[theta,gain])
        bound=np.array([B*abs(dx)/(omega*r*r)+abs(dy)/(omega*r),
                        (1+B*B/(r*r))*abs(dx)+2*B*abs(dy)/r])
        assert np.all(err<=bound+1e-12)
        adverse=max(adverse,float(err[0]))
    # A distinct response, gain and delay yields exactly the same single tone.
    other_theta=theta+.2;other_gain=abs(H)*np.sqrt(1+(omega*other_theta)**2)
    delay=(-np.angle(H)-np.arctan(omega*other_theta))/omega
    delay=delay%(2*np.pi/omega)
    H2=other_gain*np.exp(-1j*omega*delay)/(1+1j*omega*other_theta)
    alias_error=float(abs(H-H2));assert alias_error<1e-12
    calibration.append(dict(omega=omega,theta=theta,gain=gain,transfer=[H.real,H.imag],
                            inverse_roundtrip_error=rt_error,bounded_noise_max_theta_error=adverse,
                            error_rectangle_halfwidth=epsilon,alternative_delay=delay,
                            alternative_theta=other_theta,alternative_gain=other_gain,
                            unknown_delay_alias_error=alias_error))

out=dict(kind='synthetic mathematics/code controls only; no physical calibration',
         protocol_sha256=hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest(),
         symbolic_identities=identities,harmonic_nonidentifiability=harmonic,
         nonlinear_memory_and_tangent=nonlinear,reference_calibration=calibration,
         tolerances=dict(endpoint=2e-8,tangent=2e-6),physical_calibration=False,
         empirical_fit=False,holdout_accessed=False,
         versions=dict(python=platform.python_version(),numpy=np.__version__,
                       scipy=scipy.__version__,sympy=s.__version__))
(HERE/'controls.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
