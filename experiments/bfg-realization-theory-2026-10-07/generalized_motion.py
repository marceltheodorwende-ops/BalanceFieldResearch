"""General linear motion encoding through canonical scalar BFG state."""
import sys
from pathlib import Path
import numpy as np
from scipy.linalg import expm
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'bfg-pendulum-motion-2026-10-07'))
from motion import event_clock,scalar,Y0

def prepare(theta,w,theta_scale=1.,velocity_scale=1.):
    if min(theta_scale,velocity_scale)<=0:raise ValueError('positive scales')
    x=theta/theta_scale;q=w/velocity_scale
    return 1+x*x+q*q,np.arctan2(-q,x)

def readout(F,K,event,a,b,step,theta_scale=1.,velocity_scale=1.):
    if a<0 or b<0:raise ValueError('passive linear coefficients required')
    if F<1-1e-12:raise ValueError('invalid shifted formation encoding')
    r=np.sqrt(max(F-1,0.))
    initial=np.array([theta_scale*r*np.cos(K),-velocity_scale*r*np.sin(K)])
    return expm(np.array([[0.,1.],[-a,-b]])*(step*event))@initial

if __name__=='__main__':
    sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'real-eeg-covariance-2026-10-07'))
    from experiment import update
    cases=[(4.,0.),(4.,1.),(4.,4.),(4.,6.),(0.,0.)]
    rng=np.random.default_rng(20261007);errors=[]
    for a,b in cases:
        for theta,w in [(0.,0.),(.3,-.4)]+[tuple(x) for x in rng.normal(size=(20,2))]:
            F,K=prepare(theta,w)
            actual=update(np.array([[K]]),np.array([[F]]),np.ones((1,1)),np.array([[Y0]]),np.ones((1,1)))
            assert actual['terminal'] is None
            value=readout(actual['f'][0,0],actual['k'][0,0],event_clock(actual['y'][0,0]),a,b,.1)
            expected=expm(np.array([[0.,1.],[-a,-b]])*.1)@np.array([theta,w])
            errors.extend(abs(value-expected))
    F,K=prepare(1.,0.)
    critical=readout(F,K,1,4.,4.,.1)
    np.testing.assert_allclose(critical,[1.2*np.exp(-.2),-.4*np.exp(-.2)],atol=1e-12)
    F,K=prepare(.2,.3)
    np.testing.assert_allclose(readout(F,K,1,0.,0.,.1),[.23,.3],atol=1e-12)
    assert max(errors)<1e-12
    print('110 full ambient-state checks plus critical/free-motion controls; max residual',max(errors))
