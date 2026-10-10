"""Independent high-precision, phase-bound and nonlinear delay checks."""
import hashlib
import json
from pathlib import Path
import mpmath as mp
import numpy as np
from scipy.integrate import solve_ivp

HERE=Path(__file__).resolve().parent
protocol=hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest()
assert json.loads((HERE/'controls.json').read_text())['protocol_sha256']==protocol
mp.mp.dps=70;prec=[]
for theta,gain,delay in [('0','1.2','.05'),('.03','.8','.02'),('.12','1.3','.1'),('10','1','.03')]:
    th,a,d=map(mp.mpf,[theta,gain,delay]);w1=mp.mpf(2);w2=mp.mpf(5)
    H1=a*mp.exp(-mp.j*w1*d)/(1+mp.j*w1*th)
    H2=a*mp.exp(-mp.j*w2*d)/(1+mp.j*w2*th)
    R=abs(H1)**2/abs(H2)**2;u=(R-1)/(w2*w2-R*w1*w1)
    assert u>=-mp.mpf('1e-65')
    recovered=mp.sqrt(max(0,u));aa=abs(H1)*mp.sqrt(1+w1*w1*u)
    error=max(abs(recovered-th),abs(aa-a))
    assert error<mp.mpf('1e-30')
    prec.append(dict(theta=theta,error=str(error)))
remote=2*mp.pi*13860
near=abs(mp.exp(-mp.j*mp.sqrt(2)*remote)-1)

rng=np.random.default_rng(171);max_violation=0.
w=2.;D=.2
for _ in range(300):
    th=.12;aa=1.;dd=.05
    th2=th+rng.uniform(-.001,.001);a2=aa+rng.uniform(-.0001,.0001)
    d2=dd+rng.uniform(-.0001,.0001)
    H=aa*np.exp(-1j*w*dd)/(1+1j*w*th)
    H2=a2*np.exp(-1j*w*d2)/(1+1j*w*th2)
    E=abs(H-H2);m=min(abs(H),abs(H2))
    rhs=np.pi/(2*w)*(2*E/m+w*abs(th-th2))
    assert abs(dd-d2)<=rhs+1e-12
    max_violation=max(max_violation,float(abs(dd-d2)-rhs))

# Independent nonlinear delayed factor/tangent. All times are synthetic.
def F(z):return np.array([z[1],-4*np.sin(z[0])-.15*np.cos(z[0]/2)*z[1]])
def DF(z):
    q,v=z
    return np.array([[0,1],[-4*np.cos(q)+.075*np.sin(q/2)*v,-.15*np.cos(q/2)]])
def flow(z,t):
    def rhs(t,u):return np.r_[F(u[:2]),(DF(u[:2])@u[2:].reshape(2,2)).ravel()]
    sol=solve_ivp(rhs,[0,t],np.r_[z,np.eye(2).ravel()],method='DOP853',rtol=2e-12,atol=2e-14)
    assert sol.success
    return sol.y[:2,-1],sol.y[2:,-1].reshape(2,2)
z=np.array([.4,.2]);delay=.05
physical,Dback=flow(z,delay)
C=lambda z:.4+.04*z[0]
end,DRfixed=flow(physical,C(physical))
delayed_end,DJ=flow(end,-delay)
equivalent,_=flow(z,C(physical))
endpoint_error=float(np.max(abs(delayed_end-equivalent)));assert endpoint_error<2e-8
DR=DRfixed+np.outer(F(end),[.04,0])
tangent=DJ@DR@Dback
def delayed_return(z):
    zz,_=flow(z,delay);ee,_=flow(zz,C(zz));return flow(ee,-delay)[0]
eps=1e-5
finite=np.column_stack([(delayed_return(z+eps*np.eye(2)[i])-delayed_return(z-eps*np.eye(2)[i]))/(2*eps) for i in range(2)])
tangent_error=float(np.max(abs(tangent-finite)));assert tangent_error<2e-6
omitted=float(np.max(abs(DJ@DRfixed@Dback-finite)));assert omitted>1e-3

# Explicit differentiation instability for arbitrarily small output errors,
# with no independent bandwidth restriction. Odd n, time pi/2: |sin(n t)|=1.
instability=[]
for n in [1001,10001,100001]:
    eps=1/n
    force_error=.12*n/1.3
    instability.append(dict(frequency=n,output_sup_error=eps,
                            response_second_derivative_term=force_error))
assert instability[-1]['response_second_derivative_term']>9000
out=dict(kind='independent synthetic verification, not instrument calibration',
         protocol_sha256=protocol,seventy_digit_inverse_controls=prec,
         seventy_digit_irrational_near_alias_phase_error=str(near),
         bounded_delay_inequality_checks=300,maximum_bound_violation=max_violation,
         nonlinear_delay_endpoint_error=endpoint_error,nonlinear_delay_tangent_error=tangent_error,
         omitted_clock_gradient_error=omitted,unrestricted_differentiation_instability=instability,
         physical_calibration=False,empirical_fit=False,holdout_accessed=False)
(HERE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
