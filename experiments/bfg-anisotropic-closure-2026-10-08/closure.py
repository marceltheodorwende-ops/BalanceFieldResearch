"""Canonical two-dimensional observable factor on simple-spectrum chart."""
import numpy as np

class ChartExit(ValueError):pass

def observe(K,F,Y):
    if np.shape(Y)!=(2,2):raise ValueError('two-dimensional carrier required')
    if not all(np.isfinite(v).all() for v in (K,F,Y)):raise ValueError('finite matrices required')
    for v in (K,F,Y):
        if not np.allclose(v,v.conj().T,atol=1e-12,rtol=0):raise ValueError('Hermitian matrices required')
    if np.min(np.linalg.eigvalsh(F))<=0:raise ValueError('positive definite formation')
    y,U=np.linalg.eigh(Y)
    if y[0]<=0 or y[1]>=1:raise ValueError('geometry domain0<Y<I')
    if y[1]-y[0]<=1e-12:raise ChartExit('simple-spectrum readout chart')
    ff=U.conj().T@F@U;kk=U.conj().T@K@U
    weights=np.diag(ff).real/np.trace(ff).real
    diagonal=float(np.dot(np.diag(ff).real,np.diag(kk).real))
    coherence=kk[0,1]*ff[1,0]
    return y,weights,diagonal,coherence

def advance(observation):
    y,weights,diagonal,z=observation;y=np.asarray(y,float);weights=np.asarray(weights,float)
    if len(y)!=2 or len(weights)!=2 or np.any(y<=0) or np.any(y>=1) or np.any(weights<=0) or not np.isclose(weights.sum(),1):raise ValueError('factor domain')
    lc=np.sum(weights/(1+y));lb=np.sum(weights*y*y/(1+y));alpha=lb/(lc+lb);beta=1-alpha
    c=1/(1+y);b=1-c;r=alpha*c*c+beta*b*b
    gamma=(alpha*c[0]*c[1]+beta*b[0]*b[1])/np.sqrt(r[0]*r[1])
    if abs(r[1]-r[0])<=1e-12:raise ChartExit('successor spectrum collision; not a canonical terminal')
    order=np.argsort(r);newz=gamma*z
    if order[0]==1:newz=np.conj(newz)
    return r[order],weights[order],diagonal,newz

# Collision-safe spectral measure factor. Group tolerance is numerical policy,
# not an assertion that two distinct exact eigenvalues are identical.
GROUP_TOL=1e-12

def groups(values):
    result=[]
    for i in np.argsort(values):
        if not result or abs(values[i]-values[result[-1][0]])>GROUP_TOL:result.append([int(i)])
        else:result[-1].append(int(i))
    return result

def spectral_observe(K,F,Y):
    y,U=np.linalg.eigh(Y)
    if np.min(np.linalg.eigvalsh(F))<=0 or y[0]<=0 or y[-1]>=1:raise ValueError('positive full-persistence domain')
    ff=U.conj().T@F@U;kk=U.conj().T@K@U
    weights=np.diag(ff).real/np.trace(ff).real
    return merge(y,weights,kk*ff.T)

def merge(y,weights,nu):
    g=groups(y)
    return np.array([y[v[0]] for v in g]),np.array([weights[v].sum() for v in g]),np.array([[nu[np.ix_(v,w)].sum() for w in g] for v in g])

def spectral_advance(observation):
    y,weights,nu=observation
    lc=np.sum(weights/(1+y));lb=np.sum(weights*y*y/(1+y));alpha=lb/(lc+lb)
    c=1/(1+y);b=1-c;r=alpha*c*c+(1-alpha)*b*b
    gamma=(alpha*np.outer(c,c)+(1-alpha)*np.outer(b,b))/np.sqrt(np.outer(r,r))
    return merge(r,weights,gamma*nu)
