"""Synthetic matrix/SVD controls, not physical measurements or proof substitutes."""
import json
from pathlib import Path
import numpy as np
def invroot(M):
    v,U=np.linalg.eigh(M)
    return (U/np.sqrt(v))@U.conj().T
def event(X,K,R):
    n=len(X);C=np.linalg.inv(np.eye(n)+X);B=X@C
    lc=np.trace(R@C).real;lb=np.trace(R@X@X@C).real
    alpha=lb/(lc+lb);A=np.vstack((np.sqrt(alpha)*C,np.sqrt(1-alpha)*B))
    M=A.conj().T@A;T=A@invroot(M)
    KK=T[:n].conj().T@K@T[:n]+T[n:].conj().T@K@T[n:]
    U,v,Vh=np.linalg.svd(A,full_matrices=False);V=Vh.conj().T
    block=np.kron(np.eye(2),K)
    svdK=V@(U.conj().T@block@U)@V.conj().T
    svdM=V@np.diag(v*v)@V.conj().T
    return M,KK,max(np.max(np.abs(KK-svdK)),np.max(np.abs(M-svdM)))
rng=np.random.default_rng(76);fdmax=0.;svdmax=0.;diammax=0.
for n in (2,3,4):
    for case in range(20):
        def herm():
            Z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));return (Z+Z.conj().T)/2
        K=herm();Z=herm();R=Z@Z+np.eye(n)
        E=herm();E/=np.linalg.norm(E)
        x=.2+.6*rng.random();a=2*x*(1-x)/((1+x)**3*(1+x*x))
        long=4*x*(1-x**3)/((1+x)**3*(1+x*x)**2)
        ell=np.trace(R@E).real/np.trace(R).real
        expected=a*E+(long-a)*ell*np.eye(n);eps=1e-6
        Mp,Kp,e1=event(x*np.eye(n)+eps*E,K,R)
        Mm,Km,e2=event(x*np.eye(n)-eps*E,K,R)
        fdmax=max(fdmax,float(np.max(np.abs((Mp-Mm)/(2*eps)-expected))),float(np.max(np.abs((Kp-Km)/(2*eps)))))
        U,_=np.linalg.qr(herm());values=rng.uniform(.05,.95,n);X=U@np.diag(values)@U.conj().T
        M,KK,e3=event(X,K,R);diam=np.ptp(np.linalg.eigvalsh(M))/np.ptp(values)
        diammax=max(diammax,float(diam));svdmax=max(svdmax,float(e1),float(e2),float(e3))
assert fdmax<1e-8 and svdmax<1e-12 and diammax<1
out={'kind':'synthetic independent matrix and SVD controls','cases':60,'dimensions':[2,3,4],
     'max_full_tangent_fd_error':fdmax,'max_ambient_svd_error':svdmax,'max_sampled_diameter_ratio':diammax,
     'even_resonance_full_nonlinear_closure':'unresolved','empirical_confirmation':False}
Path(__file__).with_name('controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
