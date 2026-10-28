# Kontrollen der endlichen aktiven Trägerfüllung

Als Python-Datei aus dem Repository-Wurzelverzeichnis ausführen; bestehende Auditabhängigkeiten. Originalupdate wird nur importiert. Beweis und Geltungsgrenzen in CARRIER_FILLING.md.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
symbolic=[]
for r,ell in ((2,0),(2,1),(2,2),(3,3)):
    n=2*r;p=s.diag(*([1]*r+[0]*r));b=s.diag(*([s.Rational(j+1,20) if j<ell else 0 for j in range(r)]))
    y=s.eye(n)/2+s.BlockMatrix([[s.zeros(r),b],[b,s.zeros(r)]]).as_explicit()
    leakage=(s.eye(n)-p)*y*p
    rank=p.col_join(p*y).rank()
    assert leakage.rank()==ell and rank==r+ell
    symbolic.append(dict(r=r,ell=ell,analysis_rank=rank))
update=audit.load_update();calls=0
def trajectory(label,k,f,w,y,p,steps):
    global calls
    rows=[]
    for step in range(steps):
        n=len(k);r=int(round(np.trace(p).real));ell=int(np.linalg.matrix_rank((np.eye(n)-p)@y@p,tol=1e-10))
        o=update(k,f,w,y,p);calls+=1
        row=dict(step=step+1,n=n,r=r,ell=ell,terminal=o['terminal'])
        if o['terminal'] is not None:rows.append(row);return dict(label=label,events=rows,filled=False)
        m=len(o['k']);rr=int(round(np.trace(o['p']).real));gap=m-rr
        assert m==r+ell and rr==r+(ell>0) and gap==max(ell-1,0)
        assert gap<=max(n-r-1,0)
        full=float(np.linalg.norm(o['p']-np.eye(m)))
        row.update(m=m,output_rank=rr,output_deficit=gap,full_projector_residual=full)
        rows.append(row)
        k,f,w,y,p=(o[key] for key in ('k','f','w','y','p'))
        if gap==0:
            assert full<1e-10
            return dict(label=label,events=rows,filled=True)
    assert False,'Declared rank-filling bound failed'
p=np.diag([1.,1.,0.,0.]);results=[trajectory('reducing_rank2',-np.diag([2.,3.,5.,7.]),p,p/2,np.diag([.2,.3,.4,.5]),p,1)]
p=np.diag([1.,1.,0.]);f=np.diag([1.,.42,0.]);y=np.array([[.25,0,.1],[0,.5,.1],[.1,.1,.5]])
results.append(trajectory('rank2_leak1',-np.diag([1.,2.,3.]),f,p/2,y,p,1))
rng=np.random.default_rng(20261028)
for n,r in ((4,2),(6,3)):
    z=audit.complex_unitary(rng,n);p=z[:,:r]@z[:,:r].conj().T
    f=p@audit.pos(rng,n)@p;w=p/r
    z=audit.complex_unitary(rng,n);y=(z*np.linspace(.15,.7,n))@z.conj().T
    k=-audit.pos(rng,n)
    results.append(trajectory('generic_rank'+str(r),k,f,w,y,p,r))
assert calls<=7
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261028,calls=calls,symbolic=symbolic,trajectories=results,scope='Exact-rank nonterminal active-carrier filling, not physical time or a selected local pair field. Finite numerical prefixes only.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261028,
  "calls": 7,
  "symbolic": [
    {
      "r": 2,
      "ell": 0,
      "analysis_rank": 2
    },
    {
      "r": 2,
      "ell": 1,
      "analysis_rank": 3
    },
    {
      "r": 2,
      "ell": 2,
      "analysis_rank": 4
    },
    {
      "r": 3,
      "ell": 3,
      "analysis_rank": 6
    }
  ],
  "trajectories": [
    {
      "label": "reducing_rank2",
      "events": [
        {
          "step": 1,
          "n": 4,
          "r": 2,
          "ell": 0,
          "terminal": null,
          "m": 2,
          "output_rank": 2,
          "output_deficit": 0,
          "full_projector_residual": 0
        }
      ],
      "filled": true
    },
    {
      "label": "rank2_leak1",
      "events": [
        {
          "step": 1,
          "n": 3,
          "r": 2,
          "ell": 1,
          "terminal": null,
          "m": 3,
          "output_rank": 3,
          "output_deficit": 0,
          "full_projector_residual": 1.2553166750354037e-15
        }
      ],
      "filled": true
    },
    {
      "label": "generic_rank2",
      "events": [
        {
          "step": 1,
          "n": 4,
          "r": 2,
          "ell": 2,
          "terminal": null,
          "m": 4,
          "output_rank": 3,
          "output_deficit": 1,
          "full_projector_residual": 0.9999999999999999
        },
        {
          "step": 2,
          "n": 4,
          "r": 3,
          "ell": 1,
          "terminal": null,
          "m": 4,
          "output_rank": 4,
          "output_deficit": 0,
          "full_projector_residual": 6.68455551633537e-16
        }
      ],
      "filled": true
    },
    {
      "label": "generic_rank3",
      "events": [
        {
          "step": 1,
          "n": 6,
          "r": 3,
          "ell": 3,
          "terminal": null,
          "m": 6,
          "output_rank": 4,
          "output_deficit": 2,
          "full_projector_residual": 1.4142135623730951
        },
        {
          "step": 2,
          "n": 6,
          "r": 4,
          "ell": 2,
          "terminal": null,
          "m": 6,
          "output_rank": 5,
          "output_deficit": 1,
          "full_projector_residual": 0.9999999999999999
        },
        {
          "step": 3,
          "n": 6,
          "r": 5,
          "ell": 1,
          "terminal": null,
          "m": 6,
          "output_rank": 6,
          "output_deficit": 0,
          "full_projector_residual": 1.2023212912475022e-15
        }
      ],
      "filled": true
    }
  ],
  "scope": "Exact-rank nonterminal active-carrier filling, not physical time or a selected local pair field. Finite numerical prefixes only."
}
```
