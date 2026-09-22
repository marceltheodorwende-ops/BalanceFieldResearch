"""Independent bounded audit of the supplied 2026-09-22 canonical papers.
No full universal generator is implemented. NumPy only; no empirical data.
"""
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parent

def polar_reclosure(y,k,alpha):
    c=np.linalg.solve(np.eye(len(y))+y,np.eye(len(y)))
    b=y@c
    a=np.vstack((np.sqrt(alpha)*c,np.sqrt(1-alpha)*b))
    u,_,vh=np.linalg.svd(a,full_matrices=False)
    j=u@vh
    return j.conj().T@np.kron(np.eye(2),k)@j

def main():
    rng=np.random.default_rng(20260922)
    def unitary(n):
        return np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0]
    def hermitian(n):
        a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));return (a+a.conj().T)/2
    maxima={'polar_schur_relative':0.,'trace_identity_absolute':0.,'commuting_relative':0.,'ambient_relative':0.,'pinching_bound_excess':0.}
    positive_losses=0
    for _ in range(512):
        n=int(rng.integers(2,10));u=unitary(n);v=np.exp(rng.uniform(-2.5,2.5,n));y=(u*v)@u.conj().T;k=hermitian(n);alpha=float(rng.uniform(.02,.98));beta=1-alpha
        d=alpha+beta*v*v;chi=(alpha+beta*np.outer(v,v))/np.sqrt(np.outer(d,d));kh=u.conj().T@k@u
        direct=polar_reclosure(y,k,alpha);closed=u@(chi*kh)@u.conj().T
        err=np.linalg.norm(direct-closed)/max(1.,np.linalg.norm(k));maxima['polar_schur_relative']=max(maxima['polar_schur_relative'],float(err));assert err<1e-10
        loss=float(np.trace(k@k-direct@direct).real)
        weighted=float(np.sum(alpha*beta*(v[:,None]-v[None,:])**2*abs(kh)**2/np.outer(d,d)))
        maxima['trace_identity_absolute']=max(maxima['trace_identity_absolute'],abs(loss-weighted));assert abs(loss-weighted)<1e-9
        comm=np.linalg.norm(y@k-k@y)**2;lo=alpha*beta*comm/max(d)**2;hi=alpha*beta*comm/min(d)**2
        assert lo-1e-9<=loss<=hi+1e-9
        positive_losses+=loss>1e-10
        off=kh-np.diag(np.diag(kh));rate=float(np.max(chi[~np.eye(n,dtype=bool)]));after=(chi**25)*off
        excess=float(np.linalg.norm(after)-rate**25*np.linalg.norm(off));maxima['pinching_bound_excess']=max(maxima['pinching_bound_excess'],excess);assert excess<1e-10
    for _ in range(128):
        n=6;u=unitary(n);v=np.array([0.,0.,1.,1.,3.,3.]);kh=hermitian(n);kh*=v[:,None]==v[None,:];k=u@kh@u.conj().T;y=(u*v)@u.conj().T
        err=np.linalg.norm(polar_reclosure(y,k,.37)-k)/max(1.,np.linalg.norm(k));maxima['commuting_relative']=max(maxima['commuting_relative'],float(err));assert err<1e-10
    for _ in range(128):
        n=6;r=3;u=unitary(n);v=np.exp(rng.uniform(-2,2,n));y=(u*v)@u.conj().T;k=hermitian(n);basis=u[:,:r];p=basis@basis.conj().T;c=np.linalg.inv(np.eye(n)+y);b=y@c;alpha=.37
        a=np.vstack((np.sqrt(alpha)*p@c,np.sqrt(1-alpha)*p@b))@basis
        ul,_,vh=np.linalg.svd(a,full_matrices=False);j=ul@vh
        direct=j.conj().T@np.kron(np.eye(2),k)@j;restricted=polar_reclosure(basis.conj().T@y@basis,basis.conj().T@k@basis,alpha)
        err=np.linalg.norm(direct-restricted)/max(1.,np.linalg.norm(k));maxima['ambient_relative']=max(maxima['ambient_relative'],float(err));assert err<1e-10
    # Exact reasoning: e1 and e1+e2 both have bounded nonzero limits for
    # R=diag(1,1/2), but their span includes the decaying e2.
    witnesses=np.array([[1.,1.],[0.,1.]])
    assert np.linalg.det(witnesses)==1
    # Complex phase family: eigenvector e0 times 1,i,-1,-i all minimize.
    k=np.diag([-1.,2.]);values=[]
    for phase in [1,1j,-1,-1j]:
        z=np.array([phase,0],complex);values.append(float((.5*np.vdot(z,k@z)+.25*np.vdot(z,z)**2).real))
    assert values==[-.25]*4
    # Algebraically exact one-parameter family; numerical check is supplementary.
    family=[]
    for t in [.1,1.,10.]:
        alpha=t*t/(t*t+t+2);y=np.diag([0.,t]);k=np.array([[-2.,1.],[1.,2.]])
        got=polar_reclosure(y,k,alpha);want=np.array([[-2.,1/np.sqrt(t+3)],[1/np.sqrt(t+3),2.]])
        assert np.allclose(got,want,atol=1e-12);family.append({'t':t,'spectrum':np.linalg.eigvalsh(got).tolist()})
    # Nonzero [K,P] alone does not yield spectral novelty on inherited support.
    k=np.diag([-3.,1.,4.]);basis=np.array([[1/np.sqrt(2),0],[1/np.sqrt(2),0],[0,1.]])
    p=basis@basis.T;kp=basis.T@k@basis
    assert np.isclose(np.linalg.norm(k@p-p@k,2),2.)
    assert np.allclose(polar_reclosure(np.eye(2),kp,.5),kp)
    result={'seed':20260922,'numpy':np.__version__,'status':'all independent checks passed','random_trials':512,'commuting_controls':128,'ambient_controls':128,'positive_trace_losses':int(positive_losses),'max_residuals':maxima,'analytic_family_checks':family,'persistence_counterexample':{'witness_span_rank':2,'peripheral_rank':1,'conclusion':'Architecture Eq.23 does not in general define the peripheral space'},'complex_formation_counterexample':{'distinct_minimizers_checked':4,'functional_values':values,'conclusion':'Exactly two minima requires a real profile restriction or revised phase convention'},'scope':'Fresh bounded audit, not reproduction of the papers reported random streams; no empirical validation; no full universal update'}
    (ROOT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps(result,indent=2))

if __name__=='__main__':main()