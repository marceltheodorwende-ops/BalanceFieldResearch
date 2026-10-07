"""Additional mechanical input bridge; no inferred geometry-to-torque law."""
import numpy as np

def finite(*values):
    if not all(np.isfinite(v).all() for v in map(np.asarray,values)):raise ValueError('finite inputs required')

def energy(theta,w,a):
    finite(theta,w,a)
    if a<=0:raise ValueError('positive gravity calibration required')
    return np.asarray(w)**2/2+2*a*np.sin(np.asarray(theta)/2)**2

def kick(theta,w,a,j):
    finite(theta,w,a,j)
    if a<=0:raise ValueError('positive gravity calibration required')
    # Global mechanical angle/velocity map; no artificial libration restriction.
    return np.asarray(theta,float),np.asarray(w,float)+np.asarray(j,float)

def chart(theta,w,a):
    e=energy(theta,w,a)/a
    if np.any(abs(np.asarray(theta))>=np.pi) or np.any(e>=2):raise ValueError('outside libration chart')
    q=2*np.sin(np.asarray(theta)/2);p=np.asarray(w)/np.sqrt(a)
    return e,np.arctan2(-p,q),e==0

def qp_rhs(q,p,a,b,u):
    finite(q,p,a,b,u)
    if a<=0 or b<0 or np.any(abs(np.asarray(q))>=2):raise ValueError('flow chart/calibration domain')
    c=np.sqrt(1-np.asarray(q)**2/4)
    return np.sqrt(a)*np.asarray(p)*c,-np.sqrt(a)*np.asarray(q)*c-b*np.asarray(p)+np.asarray(u)
