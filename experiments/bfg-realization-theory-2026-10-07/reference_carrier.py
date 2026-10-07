"""Reference-instrument carrier candidate; no physical transition derivation."""
import numpy as np

def prepare(theta,velocity,theta_scale=1.,velocity_scale=1.):
    if min(theta_scale,velocity_scale)<=0:raise ValueError('positive scales required')
    v=np.array([1.,theta/theta_scale,velocity/velocity_scale])
    F=np.outer(v,v)
    J=np.diag([1.,0.,0.])
    A=np.zeros((3,3));A[0,1]=A[1,0]=.5
    B=np.zeros((3,3));B[0,2]=B[2,0]=.5
    return F,J,A,B

def readout(F,J,A,B,theta_scale=1.,velocity_scale=1.):
    mass=np.trace(J@F).real
    if mass<=0:raise ValueError('reference lost')
    return (theta_scale*np.trace(A@F).real/mass,
            velocity_scale*np.trace(B@F).real/mass)

if __name__=='__main__':
    rng=np.random.default_rng(20261007);errors=[]
    for _ in range(200):
        theta,w=rng.normal(size=2)
        F,J,A,B=prepare(theta,w,.3,2.)
        errors.extend(abs(np.array(readout(F,J,A,B,.3,2.))-[theta,w]))
        z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
        U,_=np.linalg.qr(z)
        rotated=[U@M@U.conj().T for M in [F,J,A,B]]
        errors.extend(abs(np.array(readout(*rotated,.3,2.))-[theta,w]))
        assert np.linalg.eigvalsh(F).min()>-1e-12
    print('200 reconstruction and joint-unitary controls; max error',max(errors))
