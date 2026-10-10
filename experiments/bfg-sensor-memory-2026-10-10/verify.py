"""Independent calibration-response and rank controls; synthetic only."""
import hashlib
import json
from pathlib import Path
import numpy as np
from scipy.integrate import solve_ivp, quad

HERE=Path(__file__).resolve().parent
protocol_hash=hashlib.sha256((HERE/'PROTOCOL.md').read_bytes()).hexdigest()
previous=json.loads((HERE/'controls.json').read_text())
assert previous['protocol_sha256']==protocol_hash

theta=.12;gain=1.3;offset=.02;Q0=.2;A=.4-.1j
reference=[]
for omega in [2.,5.,11.]:
    H=gain/(1+1j*omega*theta);dc=gain*Q0+offset
    def rhs(t,u):
        Q=Q0+np.real(A*np.exp(1j*omega*t))
        return [(gain*Q+offset-u[0])/theta]
    period=2*np.pi/omega
    times=np.linspace(0,2*period,257)
    sol=solve_ivp(rhs,[0,2*period],[dc+np.real(H*A)],method='DOP853',
                  rtol=2e-12,atol=2e-14,t_eval=times)
    assert sol.success
    design=np.column_stack([np.ones(len(times)),np.cos(omega*times),np.sin(omega*times)])
    coefficients=np.linalg.lstsq(design,sol.y[0],rcond=None)[0]
    measuredH=(coefficients[1]-1j*coefficients[2])/A
    fittedtheta=-measuredH.imag/(omega*measuredH.real)
    fittedgain=abs(measuredH)**2/measuredH.real
    fittedoffset=coefficients[0]-fittedgain*Q0
    error=float(max(abs(fittedtheta-theta),abs(fittedgain-gain),abs(fittedoffset-offset)))
    assert error<1e-8
    reference.append(dict(omega=omega,ode_reference_inverse_error=error,
                          response_time=fittedtheta,gain=fittedgain,offset=fittedoffset))

# Entire compatible exponential history: quadrature independently checks
# derivative/filter commutation on a bounded harmonic input.
omega=3.;theta=.2;t=.7
filteredQ=quad(lambda u:np.exp(-u/theta)/theta*np.cos(omega*(t-u)),0,np.inf,
               epsabs=1e-12,epsrel=1e-12)[0]
filteredW=quad(lambda u:np.exp(-u/theta)/theta*(-omega*np.sin(omega*(t-u))),0,np.inf,
               epsabs=1e-12,epsrel=1e-12)[0]
exact=np.exp(1j*omega*t)/(1+1j*omega*theta)
convolution_error=float(max(abs(filteredQ-exact.real),abs(filteredW-(1j*omega*exact).real)))
assert convolution_error<1e-10

# Known-theta output jets recover all four extended states; finite differences
# independently verify the observation-jet Jacobian (not sensor-data derivatives).
theta=.2;u=np.array([.3,-.4,.1,.2])
def obs(u):return np.r_[u[2:],(u[:2]-u[2:])/theta]
eps=1e-6
D=np.column_stack([(obs(u+eps*np.eye(4)[i])-obs(u-eps*np.eye(4)[i]))/(2*eps) for i in range(4)])
det_error=float(abs(np.linalg.det(D)-1/theta**2));assert det_error<1e-7
o=obs(u);reconstructed=np.r_[o[:2]+theta*o[2:],o[:2]]
assert max(abs(reconstructed-u))<1e-12

# Boundary/conditioning diagnostic at conservative q near pi, theta=1/2,
# kappa=4: DT=[[1,theta],[-theta*kappa*cos(q),1]].
conditioning=[]
for distance in [.1,.01,.001]:
    q=np.pi-distance;D=np.array([[1.,.5],[-2*np.cos(q),1.]])
    conditioning.append(dict(distance_to_pi=distance,determinant=float(np.linalg.det(D)),
                              condition_number=float(np.linalg.cond(D))))
assert conditioning[-1]['condition_number']>1e6

# Commensurate frequencies retain an exact unknown-delay alias.
alias=max(abs(np.exp(-1j*w*.1)-np.exp(-1j*w*(.1+2*np.pi))) for w in [2,5,11])
assert alias<1e-12
preparation=[]
J=np.array([[0.,1.],[-4.,-.15]])
for theta in [.02,.1,.5]:
    z0=np.array([.4,.2]);Z0=(np.eye(2)+theta*J)@z0
    identified=(Z0[0]-z0[0])/z0[1]
    error=float(abs(identified-theta));assert error<1e-12
    preparation.append(dict(theta=theta,independent_initial_angle_inverse_error=error))
assert np.all((np.eye(2)+.5*J)@np.zeros(2)==np.zeros(2))
out=dict(kind='independent synthetic controls; no instrument calibration',
         protocol_sha256=protocol_hash,reference_ode_controls=reference,
         common_history_convolution_error=convolution_error,
         independent_jet_determinant_error=det_error,
         singular_boundary_conditioning=conditioning,
         commensurate_frequency_delay_alias_error=float(alias),
         preparation_reference_controls=preparation,
         equilibrium_preparation_uninformative=True,
         physical_calibration=False,empirical_fit=False,holdout_accessed=False)
(HERE/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
