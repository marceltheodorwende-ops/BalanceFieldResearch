"""Conditional nonlinear flow on the unchanged scalar BFG clock."""
import numpy as np
from scipy.integrate import solve_ivp

def prepare(theta,w):
    return 1+theta*theta+w*w,np.arctan2(-w,theta)

def decode(F,K):
    if F<1:raise ValueError('shifted formation must be >=1')
    r=np.sqrt(F-1)
    return np.array([r*np.cos(K),-r*np.sin(K)])

def flow(initial,t,a,b,alpha=1.):
    if a<0 or b<0 or not 0<=alpha<=1:raise ValueError('passive family domain')
    initial=np.asarray(initial,dtype=float)
    if t==0:return initial.copy()
    def rhs(_,x):return [x[1],-a*((1-alpha)*x[0]+alpha*np.sin(x[0]))-b*x[1]]
    result=solve_ivp(rhs,(0,t),initial,method='DOP853',rtol=1e-11,atol=1e-13)
    if not result.success:raise RuntimeError(result.message)
    return result.y[:,-1]

def readout(F,K,event,a,b,step=.1,alpha=1.):
    return flow(decode(F,K),step*event,a,b,alpha)

def energy(x,a,alpha=1.):
    theta,w=x
    return w*w/2+a*((1-alpha)*theta*theta/2+alpha*(1-np.cos(theta)))
