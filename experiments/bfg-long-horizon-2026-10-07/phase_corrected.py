"""Weakly nonlinear phase observable; additional mechanical approximation."""
import numpy as np

def prepare_corrected(theta,w,a,b):
    omega=np.sqrt(a-b*b/4)
    if not np.isfinite(omega) or omega<=0:raise ValueError('underdamped regime')
    q=w+b*theta/2
    amplitude=np.sqrt(theta*theta+(q/omega)**2)
    for _ in range(40):
        rate=omega-a*amplitude**2/(16*omega)
        if np.any(rate<=0):raise ValueError('phase rate gate')
        updated=np.sqrt(theta*theta+(q/rate)**2)
        if np.max(abs(updated-amplitude))<1e-13:
            amplitude=updated;break
        amplitude=updated
    else:raise ValueError('initial calibration failed')
    if np.any(amplitude>1):raise ValueError('outside declared small-angle amplitude domain')
    rate=omega-a*amplitude**2/(16*omega)
    phase=np.arctan2(-q/rate,theta)
    return amplitude**2,phase

def corrected_readout(F,K,event,a,b,step=.1):
    omega=np.sqrt(a-b*b/4);t=event*step
    integral=t if b==0 else -np.expm1(-b*t)/b
    phase=K+omega*t-a*F*integral/(16*omega)
    rate=omega-a*F*np.exp(-b*t)/(16*omega)
    amplitude=np.sqrt(F)*np.exp(-b*t/2)
    return amplitude*np.cos(phase),-amplitude*(b*np.cos(phase)/2+rate*np.sin(phase))
