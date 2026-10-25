# Runde75 – lokale vollständige Reproduktion

Präregistrierung c9326f52aa477bc168e761d204a2fad9101a6628. Ein frischer PASS,4 Originalaufrufe, keine Fehlvorläufe/Korrektur. Python/NumPy, unverändertes audit.py im bisherigen relativen bfg-review-Forschungspfad. Dieser Dokumenttext wird von der bestehenden CI nicht automatisch ausgeführt.

```python
import sys,json
from pathlib import Path
import numpy as np
sys.path.insert(0,str(Path(__file__).parent/'bfg-review/research/spacetime-conservation'))
import audit
update=audit.load_update()
e=np.eye(4);a=e[:,0];b=e[:,3];v=(e[:,1]+e[:,2])/np.sqrt(2);u=(a+v)/np.sqrt(2)
outer=lambda x:np.outer(x,x.conj())
j=outer(a)+outer(v);p=j+outer(b);f=outer(a)+2*outer(v)+3*outer(b)
k=-np.diag([1.,2.,3.,4.]);y=np.diag([.2,.4,.7,2.])
ws=[.6*outer(u)+.4*outer(b),.3*j/2+.7*outer(b)]
trajectories=[];calls=0
for w in ws:
    fields=[k.copy(),f.copy(),w.copy(),y.copy(),p.copy()];out=[]
    for step in range(2):
        o=update(*fields);calls+=1
        assert o['terminal'] is None
        out.append(o);fields=[o[n] for n in ['k','f','w','y','p']]
    trajectories.append(out)
rows=[]
for step,(a,b) in enumerate(zip(*trajectories)):
    structural=max(np.linalg.norm(a[n]-b[n]) for n in ['k','f','y','p','t4','psel','a'])
    load=max(abs(a[n]-b[n]) for n in ['lc','lb','alpha'])
    distance=float(np.linalg.norm(a['w']-b['w']))
    purities=[float(np.trace(o['w']@o['w']).real) for o in [a,b]]
    assert max(structural,load,abs(distance-1/np.sqrt(2)),abs(purities[0]-1),abs(purities[1]-.5))<1e-10
    expected=[.6,.3] if step==0 else [1.,1.]
    assert max(abs(o['msel']-z) for o,z in zip([a,b],expected))<1e-10
    if step==0:
        inherited=a['t4']@a['psel']@a['t4'].conj().T
        seed=a['p']-inherited
        assert abs(np.trace(seed).real-1)<1e-10
    rows.append(dict(step=step+1,masses=[float(o['msel']) for o in [a,b]],structural_residual=float(structural),load_residual=float(load),witness_HS_distance=distance,purities=purities,active_rank=int(round(np.trace(a['p']).real))))
result=dict(status='PASS',original_calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=1e-10,rows=rows,scope='Actual lossy selection and seed fix structural dynamics without selecting a unique initial/conditional Witness; no physical Hamiltonian identified.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
```

```json
{
  "status": "PASS",
  "original_calls": 4,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "tolerance": 1e-10,
  "rows": [
    {
      "step": 1,
      "masses": [
        0.5999999999999999,
        0.3
      ],
      "structural_residual": 0.0,
      "load_residual": 0.0,
      "witness_HS_distance": 0.7071067811865476,
      "purities": [
        1.0,
        0.5
      ],
      "active_rank": 3
    },
    {
      "step": 2,
      "masses": [
        1.0,
        1.0
      ],
      "structural_residual": 0.0,
      "load_residual": 0.0,
      "witness_HS_distance": 0.7071067811865476,
      "purities": [
        1.0,
        0.5
      ],
      "active_rank": 3
    }
  ],
  "scope": "Actual lossy selection and seed fix structural dynamics without selecting a unique initial/conditional Witness; no physical Hamiltonian identified."
}
```
