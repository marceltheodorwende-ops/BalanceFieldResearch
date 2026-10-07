"""Exact libration energy-phase chart; externally supplied sine mechanics."""
import numpy as np

def encode(theta,w,a):
    if a<=0: raise ValueError('a must be positive')
    theta,w=np.broadcast_arrays(np.asarray(theta,float),np.asarray(w,float))
    e=w*w/(2*a)+2*np.sin(theta/2)**2
    if not np.isfinite(e).all() or np.any(abs(theta)>=np.pi) or np.any(e>=2):
        raise ValueError('outside open libration chart')
    phi=np.arctan2(-w/np.sqrt(a),2*np.sin(theta/2))
    return e,phi

def decode(e,phi,a):
    e=np.asarray(e,float)
    if a<=0 or not np.isfinite(e).all() or np.any(e<0) or np.any(e>=2):
        raise ValueError('outside energy domain')
    return 2*np.arcsin(np.sqrt(e/2)*np.cos(phi)),-np.sqrt(2*a*e)*np.sin(phi)

def rhs(loge,phi,a,b):
    e=np.exp(loge)
    if np.any(e>=2) or b<0 or a<=0: raise ValueError('invalid flow domain')
    return -2*b*np.sin(phi)**2,np.sqrt(a)*np.sqrt(1-e*np.cos(phi)**2/2)-b*np.cos(phi)*np.sin(phi)

def forecast(theta,w,a,b,horizon,step=.005):
    if horizon<0 or step<=0 or b<0: raise ValueError('invalid integration request')
    e,phi=encode(theta,w,a);rest=e==0
    loge=np.log(np.where(rest,1.,e))
    count=max(1,int(np.ceil(horizon/step)));h=horizon/count
    for _ in range(count):
        l1,p1=rhs(loge,phi,a,b)
        l2,p2=rhs(loge+h*l1/2,phi+h*p1/2,a,b)
        l3,p3=rhs(loge+h*l2/2,phi+h*p2/2,a,b)
        l4,p4=rhs(loge+h*l3,phi+h*p3,a,b)
        loge=loge+h*(l1+2*l2+2*l3+l4)/6
        phi=phi+h*(p1+2*p2+2*p3+p4)/6
    out=decode(np.where(rest,0.,np.exp(loge)),phi,a)
    if not all(np.isfinite(x).all() for x in out):raise FloatingPointError('nonfinite prediction')
    return out
