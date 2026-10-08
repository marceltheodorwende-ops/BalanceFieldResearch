import json
import numpy as np
from pathlib import Path
rng=np.random.default_rng(50)
F=np.diag([1.,2.]);Y=np.diag([.2,.7]);K=np.diag([-.4,.3]);D=np.array([[0,.01],[.01,0.]])
L=np.diag([1.,-1.]);assert np.array_equal(L@F@L,F) and np.array_equal(L@Y@L,Y)
assert np.linalg.norm(L@D@L-D)>.02
# A covariant additional policy using existing noncommuting K and a fixed unit factor.
K=np.array([[0,.2],[.2,0.]])
policy=lambda f,y,k:1j*(y@k-k@y)*.01
errs=[]
for _ in range(20):
 q,_=np.linalg.qr(rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)))
 errs.append(float(np.max(abs(policy(q.conj().T@F@q,q.conj().T@Y@q,q.conj().T@K@q)-q.conj().T@policy(F,Y,K)@q))))
assert max(errs)<1e-12
assert np.allclose(policy(F,Y,K),policy(F,Y,K).conj().T)
for sign in [-1,1]:
 assert min(np.linalg.eigvalsh(Y+sign*policy(F,Y,K)))>0 and max(np.linalg.eigvalsh(Y+sign*policy(F,Y,K)))<1
result=dict(gauge_controls=20,max_residual=max(errs),forbidden_offdiagonal_stabilizer_defect=float(np.linalg.norm(L@D@L-D)),admissible_signed_commutator_norm=float(np.linalg.norm(policy(F,Y,K),2)),kind='synthetic math controls',physical_force_selected=False)
Path(__file__).with_name('controls.json').write_text(json.dumps(result,indent=2)+'\n');print(result)
