"""P63 synthetic controls of a general construction, no dataset or BFG fit.
Run python check.py (numpy, scipy, sympy). P_ref is NOT the exact P62 map.
"""
import json
from pathlib import Path
import numpy as np
import sympy as s
from scipy.integrate import solve_ivp

p,Delta,v=s.symbols('p Delta v',positive=True)
w=(1-v)/p+v
assert s.simplify(w.subs(v,0)*p-w.subs(v,1))==0
assert s.simplify(s.integrate(w,(v,0,1))-(1+1/p)/2)==0
pp,np_,bp,bpp,theta_prime=s.symbols('Pprime Nprime bprime bprime_at_P theta_prime')
assert s.simplify(np_/(np_/pp)-pp)==0
assert s.simplify(((bp+theta_prime)/pp)*pp-bp-theta_prime)==0
u,e=s.symbols('u e',real=True)
h=e*s.sin(2*s.pi*u)
assert s.simplify(h.subs(u,u+1)-h)==0
assert s.simplify(s.diff(h,u)-2*s.pi*e*s.cos(2*s.pi*u))==0
assert s.simplify(s.diff(h,u,2)+4*s.pi**2*e*s.sin(2*s.pi*u))==0
assert s.simplify(s.diff(u+h,u)-(1+2*s.pi*e*s.cos(2*s.pi*u)))==0

x0=.2;x1=x0/(1+x0);d=x0-x1
theta0=np.arctan(np.sqrt(x0));p0=1/(1+x0)**2
m_lower=1/(2*np.sqrt(x0)*(1+x0)*p0)
def N(x):return 1/x-1/x0
def theta(x):return np.arctan(np.sqrt(x))
def tp(x):return 1/(2*np.sqrt(x)*(1+x))
def seed(x):
    v=(x-x1)/d
    return theta0*(2*v**3-3*v*v+1)+d*m_lower*(v**3-2*v*v+v)
def seedp(x):
    v=(x-x1)/d
    return theta0*(6*v*v-6*v)/d+m_lower*(3*v*v-4*v+1)
assert abs(seed(x0))<1e-14 and abs(seed(x1)-theta0)<1e-14
assert abs(seedp(x1)*p0-seedp(x0)-tp(x0))<1e-14
def phase_b(x):
    n=int(np.floor(N(x)+1e-12));r=1/(1/x-n)
    vals=[r/(1+j*r) for j in range(n)]
    return seed(r)+sum(theta(y) for y in vals)
def phase_bp(x):
    n=int(np.floor(N(x)+1e-12));r=1/(1/x-n)
    deriv=seedp(r)+sum(tp(r/(1+j*r))/(1+j*r)**2 for j in range(n))
    return deriv*(r/x)**2
def omega(x,eps=0):return -x*x*phase_bp(x)+2*np.pi*eps*np.cos(2*np.pi*N(x))
def b(x,eps=0):return phase_b(x)+eps*np.sin(2*np.pi*N(x))
def flow(state,lam,eps=0):
    x,phi=state;xl=x/(1+lam*x)
    return np.array([xl,phi+b(xl,eps)-b(x,eps)])

seams=[]
for n in range(1,6):
    xs=1/(1/x0+n);step=1e-9
    val_jump=abs(phase_b(xs+step)-phase_b(xs-step))
    deriv_jump=abs(phase_bp(xs+step)-phase_bp(xs-step))
    assert val_jump<1e-6 and deriv_jump<1e-3
    seams.append({'n':n,'value_difference_over_2e-9':val_jump,'derivative_difference_over_2e-9':deriv_jump})

cases=[];max_endpoint=0;max_tangent=0;max_ode=0;max_force=0;max_intermediate=0
for nu in [.13,.43,1.37,3.19,10.41]:
    xx=1/(1/x0+nu);state=np.array([xx,.23]);target=np.array([xx/(1+xx),.23+theta(xx)])
    for eps in [0,.03]:
        err=float(np.max(np.abs(flow(state,1,eps)-target)));assert err<1e-12;max_endpoint=max(max_endpoint,err)
        step=1e-7
        jac=np.column_stack([(flow(state+np.array([step,0]),1,eps)-flow(state-np.array([step,0]),1,eps))/(2*step),
                             (flow(state+np.array([0,step]),1,eps)-flow(state-np.array([0,step]),1,eps))/(2*step)])
        expected=np.array([[1/(1+xx)**2,0],[tp(xx),1]])
        terr=float(np.max(np.abs(jac-expected)));assert terr<1e-7;max_tangent=max(max_tangent,terr)
        sol=solve_ivp(lambda lam,y:[-y[0]**2,omega(y[0],eps)],(0,1),state,rtol=2e-11,atol=2e-12,max_step=.01)
        assert sol.success
        oerr=float(np.max(np.abs(sol.y[:,-1]-target)));assert oerr<1e-7;max_ode=max(max_ode,oerr)
    semigroup=float(np.max(np.abs(flow(flow(state,.37),.43)-flow(state,.8))))
    assert semigroup<1e-12
    diff=float(abs(flow(state,.37,.03)[1]-flow(state,.37,0)[1]));max_intermediate=max(max_intermediate,diff)
    step=1e-7
    accel=lambda eps:-xx*xx*(omega(xx+step,eps)-omega(xx-step,eps))/(2*step)
    fexpected=-.03*(2*np.pi)**2*np.sin(2*np.pi*N(xx))
    ferr=abs((accel(.03)-accel(0))-fexpected);assert ferr<1e-5;max_force=max(max_force,ferr)
    cases.append({'initial_Abel_coordinate':nu,'x':xx,'intermediate_phase_difference':diff,'acceleration_difference':fexpected,'force_difference_FD_error':ferr})
assert max_intermediate>.02
result={'kind':'synthetic general-construction controls; reference P=x/(1+x), not exact P62',
        'symbolic_checks':8,'seed_endpoint_checks':3,'seams':seams,'cases':cases,
        'max_unit_time_endpoint_error':max_endpoint,'max_unit_time_tangent_error':max_tangent,
        'max_independent_ODE_endpoint_error':max_ode,'max_acceleration_difference_FD_error':max_force,
        'max_between_event_phase_difference':max_intermediate,
        'ODE_tolerance':{'rtol':2e-11,'atol':2e-12,'max_step':.01,'endpoint_acceptance':1e-7},
        'fixed_clock_force_identifiable':False,'seconds_calibrated':False,
        'real_measurements_used':False,'holdout_accessed':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
