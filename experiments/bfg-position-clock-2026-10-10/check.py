"""Independent symbolic/ODE/clock-tangent controls; no measurements loaded."""
import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp, quad
from scipy.linalg import expm
from scipy.special import ellipk

q,p,Q,W=s.symbols('q p Q W',real=True)
k,g,kp,C,I,alpha=s.symbols('k g kp C I alpha',positive=True)
h=s.Function('h')(q); r=s.Function('r')(q)
hp=s.diff(h,q); rp=s.diff(r,q); B=hp/r
checks=[]
def ck(name,expr):
    assert s.simplify(s.trigsimp(expr))==0,name
    checks.append(name)
L=lambda f:p*s.diff(f,q)+(-k*q-g*p)*s.diff(f,p)
acc=L(B*p)/r
expected=(s.diff(h,q,2)/hp**2-rp/(r*hp))*(B*p)**2-g/r*(B*p)-k*q*hp/r**2
ck('general clock chain',acc-expected)
ck('general rank',s.det(s.Matrix([[hp,0],[s.diff(B,q)*p,B]]))-hp**2/r)
ck('cancel quadratic',s.diff(h,q,2)/hp**2-s.diff(C*hp,q)/(C*hp*hp))
f=2*s.asin(alpha*q); fp=s.diff(f,q)
rk=C*fp
ck('arcsine rank',fp/C-2*alpha/(C*s.sqrt(1-alpha**2*q*q)))
ck('sine restoring',k*q/(C*C*fp)-(k/(4*C*C*alpha*alpha))*2*alpha*q*s.sqrt(1-alpha*alpha*q*q))
ck('clock velocity',fp*p/rk-p/C)
gb=s.symbols('gb',positive=True)
F=-kp*s.sin(Q)-gb*s.cos(Q/2)*W
E=I*(W*W/2+kp*(1-s.cos(Q)))
ck('constant inertia energy',s.diff(E,Q)*W+s.diff(E,W)*F+I*gb*s.cos(Q/2)*W*W)
ck('factor tangent',s.diff(F,Q)+kp*s.cos(Q)-gb*s.sin(Q/2)*W/2)
ck('centered integrated force',s.diff(1-k*q*q/(2*C*C*kp),q)+k*q/(C*C*kp))
kick=s.symbols('kick',real=True)
ck('impulse energy',E.subs(W,W+kick)-E-I*(W*kick+kick*kick/2))
ck('damping angle derivative',s.diff(gb*s.cos(Q/2),Q)+gb*s.sin(Q/2)/2)
ck('transformed harmonic energy',E.subs({Q:f,W:p/C,kp:k/(4*C*C*alpha*alpha)},simultaneous=True)-I*(p*p+k*q*q)/(2*C*C))
lam=s.symbols('lam',nonnegative=True)
inverse=C/s.sqrt(k)*Q*s.sqrt(kp+lam*Q*Q/2)
ck('Duffing rival force',k*inverse*s.diff(inverse,Q)/(C*C)-kp*Q-lam*Q**3)

# Freeze domains/cases/decision thresholds before independent integrations.
rtol,atol=2e-11,2e-12
thresholds=dict(endpoint=2e-8,tangent=2e-7,clock_gradient=2e-7,
                rtol=rtol,atol=atol,quadrature_absolute=2e-12)
cases=[]
specs=[(2.3,.4,1.7,1.,[.3,.12],.2,.8),
       (1.3,.2,.7,.8,[.65,-.05],.4,.8),
       (1.3,.2,1.3,1.,[1.98,0.],.05,.995)]
for kn,gn,kpn,Cn,initial,clock,rho in specs:
    al=np.sqrt(kn/kpn)/(2*Cn); r0=np.sqrt(kn/kpn); z0=np.array(initial)
    A=np.array([[0.,1.],[-kn,-gn]]); M=expm(clock*A)
    H=lambda z:np.array([2*np.arcsin(al*z[0]),z[1]/Cn])
    DH=lambda z:np.diag([2*al/np.sqrt(1-al*al*z[0]*z[0]),1/Cn])
    rate=lambda qn:r0/np.sqrt(1-al*al*qn*qn)
    ratep=lambda qn:r0*al*al*qn/(1-al*al*qn*qn)**1.5
    e0=(z0[1]**2+kn*z0[0]**2)/2
    assert 2*al*al*e0/kn<=rho*rho and kn>gn*gn/4
    def clock_rhs(t,y):
        mat=expm(t*A); z=mat@z0
        return np.r_[rate(z[0]),ratep(z[0])*mat[0]]
    cs=solve_ivp(clock_rhs,[0,clock],np.zeros(3),method='DOP853',rtol=rtol,atol=atol)
    assert cs.success
    T=cs.y[0,-1]; DT=cs.y[1:,-1]
    def duration(z):
        return quad(lambda t:rate((expm(t*A)@z)[0]),0,clock,epsabs=2e-12,epsrel=2e-12)[0]
    Tq=duration(z0)
    assert abs(T-Tq)<2e-9
    finite_DT=np.array([(duration(z0+np.eye(2)[j]*1e-6)-duration(z0-np.eye(2)[j]*1e-6))/2e-6 for j in range(2)])
    gradient_error=float(np.max(abs(finite_DT-DT)))
    assert gradient_error<thresholds['clock_gradient']
    gbn=gn*np.sqrt(kpn/kn)
    def vec(y):
        a,b=y[:2]; return np.array([b,-kpn*np.sin(a)-gbn*np.cos(a/2)*b])
    def rhs(t,y):
        a,b=y[:2]
        J=np.array([[0.,1.],[-kpn*np.cos(a)+gbn*np.sin(a/2)*b/2,-gbn*np.cos(a/2)]])
        return np.r_[vec(y),(J@y[2:].reshape(2,2)).ravel()]
    sol=solve_ivp(rhs,[0,T],np.r_[H(z0),np.eye(2).ravel()],method='DOP853',rtol=rtol,atol=atol)
    assert sol.success
    end=M@z0; ref=H(end); Jfixed=sol.y[2:,-1].reshape(2,2)
    endpoint_error=float(np.max(abs(sol.y[:2,-1]-ref)))
    Jtarget=DH(end)@M@np.linalg.inv(DH(z0))
    correction=np.outer(vec(ref),DT)@np.linalg.inv(DH(z0))
    tangent_error=float(np.max(abs(Jfixed+correction-Jtarget)))
    omitted_clock_error=float(np.max(abs(Jfixed-Jtarget)))
    assert endpoint_error<thresholds['endpoint'] and tangent_error<thresholds['tangent']
    assert omitted_clock_error>1e-6
    lo,hi=clock*r0,clock*r0/np.sqrt(1-rho*rho)
    assert lo<=T<=hi
    samples=sol.y[:2]
    energies=.5*samples[1]**2+kpn*(1-np.cos(samples[0]))
    assert np.max(np.diff(energies))<2e-10
    row_integral=quad(lambda t:np.linalg.norm(expm(t*A)[0]),0,clock)[0]
    DTbound=r0*al*rho/(1-rho*rho)**1.5*row_integral
    assert np.linalg.norm(DT)<=DTbound
    cases.append(dict(k0=kn,g0=gn,kp=kpn,C=Cn,alpha=al,initial=initial,old_event_time=clock,rho=rho,
      new_event_time=float(T),duration_bounds=[float(lo),float(hi)],quadrature_error=float(abs(T-Tq)),
      DT=DT.tolist(),DT_norm_bound=float(DTbound),clock_gradient_error=gradient_error,
      endpoint_error=endpoint_error,tangent_error=tangent_error,
      wrong_fixed_duration_tangent_error=omitted_clock_error,
      initial_energy=float(energies[0]),final_energy=float(energies[-1])))

# Conservative algebraic exception only: not an inherited delta=0 rank-two BFG.
periods=[]
for amplitude in [.1,.7,.95]:
    kn,kpn,al=1.3,.7,.5
    period=quad(lambda th:1/np.sqrt(1-amplitude**2*np.cos(th)**2),0,2*np.pi,epsabs=2e-12)[0]/np.sqrt(kpn)
    expected=4*ellipk(amplitude**2)/np.sqrt(kpn)
    assert abs(period-expected)<2e-10
    periods.append(dict(normalized_amplitude=amplitude,period=float(period),elliptic_error=float(abs(period-expected))))
assert periods[0]['period']<periods[1]['period']<periods[2]['period']
result=dict(symbolic_checks=checks,synthetic_cases=cases,thresholds=thresholds,
    conservative_exception_periods=periods,
    scope='Conditional position-clock representation; no physical calibration, measurements or holdout')
Path(__file__).with_name('controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(dict(symbolic_checks=len(checks),cases=len(cases),
 max_endpoint=max(x['endpoint_error'] for x in cases),max_tangent=max(x['tangent_error'] for x in cases),
 max_clock_gradient=max(x['clock_gradient_error'] for x in cases),
 min_wrong_tangent=min(x['wrong_fixed_duration_tangent_error'] for x in cases))))
