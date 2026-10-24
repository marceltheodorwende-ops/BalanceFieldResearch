# Originalkontrollen der aktiven Kernelreduktion

Code als Python-Datei im Repository-Wurzelverzeichnis ausführen. Vorhandene Auditabhängigkeiten; gepinnter Originalupdate wird nur importiert. Die allgemeine Herleitung steht in ACTIVE_KERNEL_QUOTIENT.md.

```python
import json,sys
from pathlib import Path
import numpy as np
sys.path.insert(0,'research/spacetime-conservation')
import audit
update=audit.load_update()
def inspect(k,f,w,y,p,out):
    if out['terminal'] is not None:return dict(terminal=out['terminal'])
    e,z=np.linalg.eigh(p);z=z[:,e>.5];r=z.shape[1];n=len(k);m=len(out['k'])
    ops=[out['u'][:n],out['u'][n:]]
    op=[z.conj().T@t for t in ops]
    yp=z.conj().T@y@z;hp=np.eye(r)+yp
    vs=out['v']@np.diag(out['s'])
    zz=z.conj().T@vs@out['k']@vs.conj().T@z
    mm=hp@zz@hp
    mu,v=np.linalg.eigh(yp);den=out['alpha']+(1-out['alpha'])*mu[:,None]*mu[None,:]
    rec=v@((v.conj().T@mm@v)/den)@v.conj().T
    target=z.conj().T@k@z
    residual=float(np.linalg.norm(rec-target))
    unital=float(np.linalg.norm(sum(t.conj().T@t for t in op)-np.eye(m)))
    support=max(float(np.linalg.norm(p@t-t)) for t in ops)
    bases=[np.eye(2),np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
    maps=[sum(t.conj().T@b@t for t in op) for b in bases]
    mat=np.column_stack([np.r_[b.real.ravel(),b.imag.ravel()] for b in maps])
    rank=int(np.linalg.matrix_rank(mat,tol=1e-10))
    assert rank==4 and min(den.ravel())>0
    assert max(residual,unital,support)<1e-10
    return dict(input_dimension=n,input_rank=r,output_dimension=m,output_active_rank=int(round(np.trace(out['p']).real)),reconstruction_residual=residual,unital_residual=unital,support_residual=support,real_map_rank=rank,min_divisor=float(np.min(den)))
p=np.diag([1.,1.,0.]);f=np.diag([1.,.42,0.]);w=p/2;y=np.array([[.25,0,.1],[0,.5,.1],[.1,.1,.5]])
k=-np.diag([1.,2.,3.]).astype(complex)
h=np.array([[0,0,.2],[0,0,.3j],[.2,-.3j,.4]])
assert np.linalg.norm(p@h@p)==0
a=update(k,f,w,y,p);b=update(k+h,f,w,y,p)
assert a['terminal'] is None and b['terminal'] is None
equal=max(float(np.linalg.norm(a[key]-b[key])) for key in ('k','f','w','y','p'))
assert equal<1e-10
cases=[inspect(k,f,w,y,p,a),inspect(k+h,f,w,y,p,b)]
rng=np.random.default_rng(20261026);n=4
z=audit.complex_unitary(rng,n);p=z[:,:2]@z[:,:2].conj().T
f=p@audit.pos(rng,n)@p;w=p/2
z=audit.complex_unitary(rng,n);y=(z*np.array([.15,.3,.5,.7]))@z.conj().T
k=-audit.pos(rng,n);out=update(k,f,w,y,p)
cases.append(inspect(k,f,w,y,p,out))
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=3,seed=20261026,identical_successor_residual=equal,discarded_kernel_norm=float(np.linalg.norm(h)),cases=cases,scope='Exact active-kernel quotient after Q=I, explicit injective full-output reconstruction, not physical four-momentum.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 3,
  "seed": 20261026,
  "identical_successor_residual": 6.982695313449726e-17,
  "discarded_kernel_norm": 0.6480740698407861,
  "cases": [
    {
      "input_dimension": 3,
      "input_rank": 2,
      "output_dimension": 3,
      "output_active_rank": 3,
      "reconstruction_residual": 3.968631777662163e-15,
      "unital_residual": 1.1356245773426213e-15,
      "support_residual": 9.737884992031863e-17,
      "real_map_rank": 4,
      "min_divisor": 0.15625
    },
    {
      "input_dimension": 3,
      "input_rank": 2,
      "output_dimension": 3,
      "output_active_rank": 3,
      "reconstruction_residual": 3.967975158773689e-15,
      "unital_residual": 1.1356245773426213e-15,
      "support_residual": 9.737884992031863e-17,
      "real_map_rank": 4,
      "min_divisor": 0.15625
    },
    {
      "input_dimension": 4,
      "input_rank": 2,
      "output_dimension": 4,
      "output_active_rank": 3,
      "reconstruction_residual": 3.219336860413571e-14,
      "unital_residual": 8.798999020591313e-16,
      "support_residual": 5.0815081593400575e-15,
      "real_map_rank": 4,
      "min_divisor": 0.23892989563706765
    }
  ],
  "scope": "Exact active-kernel quotient after Q=I, explicit injective full-output reconstruction, not physical four-momentum."
}
```
