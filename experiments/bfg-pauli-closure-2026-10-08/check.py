import json
from pathlib import Path
import numpy as np
from experiment import update
S=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
def split(A): return float(np.trace(A).real/2),np.array([np.trace(A@s).real/2 for s in S])
def inv(Y,K,F):
 parts=[split(a) for a in (Y,K,F)];v=np.stack([a[1] for a in parts]);return np.r_[ [a[0] for a in parts],(v@v.T)[np.triu_indices(3)],np.linalg.det(v)]
def direct(Y,K,F,eta=.1):
 Z=Y+eta*1j*(Y@K-K@Y);C=np.linalg.inv(np.eye(2)+Z);B=Z@C
 lc=np.trace(F@C).real;lb=np.trace(F@Z@Z@C).real;a=lb/(lc+lb)
 R=a*C@C+(1-a)*B@B
 e,v=np.linalg.eigh(R);ri=(v*(1/np.sqrt(e)))@v.conj().T
 return R,ri@(a*C@K@C+(1-a)*B@K@B)@ri
rng=np.random.default_rng(51);errs=[];gau=[];cross=[]
for _ in range(30):
 Y=np.diag(rng.uniform(.2,.6,2));raw=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));K=(raw+raw.conj().T)*.1
 raw=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));F=raw@raw.conj().T+np.eye(2)
 Z=Y+.1j*(Y@K-K@Y);assert np.min(np.linalg.eigvalsh(Z))>0 and np.max(np.linalg.eigvalsh(Z))<1
 sy,vy=split(Y);sk,vk=split(K);sd,vd=split(.1j*(Y@K-K@Y));cross.append(float(np.max(abs(vd+.2*np.cross(vy,vk)))))
 R,Kn=direct(Y,K,F);out=update(K,F,np.eye(2)/2,Z,np.eye(2));assert out['terminal'] is None
 V=out['v'];errs.append(float(max(np.max(abs(V@out['y']@V.conj().T-R)),np.max(abs(V@out['k']@V.conj().T-Kn)))))
 q,_=np.linalg.qr(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)));RR,KK=direct(q.conj().T@Y@q,q.conj().T@K@q,q.conj().T@F@q)
 gau.append(float(np.max(abs(inv(RR,KK,q.conj().T@F@q)-inv(R,Kn,F)))))
assert max(errs)<1e-10 and max(gau)<1e-10 and max(cross)<1e-12
Y=np.diag([.2,.7]);F=np.diag([1.,2.]);r0,_=direct(Y,np.zeros((2,2)),F);r1,_=direct(Y,np.array([[0,.2],[.2,0.]]),F)
gap=float(np.linalg.norm(np.linalg.eigvalsh(r0)-np.linalg.eigvalsh(r1)));assert gap>1e-6
res=dict(ambient_cases=30,max_ambient_error=max(errs),max_gauge_invariant_error=max(gau),max_pauli_cross_error=max(cross),same_geometry_distinct_successor_spectrum_gap=gap,kind='synthetic mathematics/code controls',force_derived=False,holdout_accessed=False)
Path(__file__).with_name('controls.json').write_text(json.dumps(res,indent=2)+'\n');print(res)
