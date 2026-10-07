"""Canonical scalar BFG + explicit calibrated clock/phase observable.
Physical coefficients are additional mechanical calibration, not BFG-derived.
"""
import math
import numpy as np

def scalar(y):return 2*y*y/((1+y)**2*(1+y*y))

def log_phi(y):
    if not 0<y<1:raise ValueError('scalar load domain')
    value=math.log(2*y);weight=.5
    for _ in range(80):
        value+=weight*(-2*math.log1p(y)-math.log1p(y*y))
        y=scalar(y);weight*=.5
        if y<1e-150:break
    return value

Y0=.25
REFERENCE=-log_phi(Y0)

def event_clock(y):return math.log2(-log_phi(y)/REFERENCE)

def prepare(theta,w,a,b):
    if a<=b*b/4:raise ValueError('requires underdamped calibration')
    omega=np.sqrt(a-b*b/4)
    quadrature=(w+b*theta/2)/omega
    F=theta*theta+quadrature*quadrature
    K=np.arctan2(-quadrature,theta)
    return F,K

def readout(F,K,event,a,b,step):
    omega=np.sqrt(a-b*b/4);t=step*event
    amplitude=np.sqrt(F)*np.exp(-b*t/2)
    phase=omega*t+K
    theta=amplitude*np.cos(phase)
    w=-amplitude*(b*np.cos(phase)/2+omega*np.sin(phase))
    return theta,w

def one_step(theta,w,a,b,step=.1):
    F,K=prepare(theta,w,a,b)
    return readout(F,K,event_clock(scalar(Y0)),a,b,step)

def stable_clock_step(log_internal_coordinate):
    # Exact coordinate identity log(phi(f(y)))=2*log(phi(y)).
    return 2*log_internal_coordinate
