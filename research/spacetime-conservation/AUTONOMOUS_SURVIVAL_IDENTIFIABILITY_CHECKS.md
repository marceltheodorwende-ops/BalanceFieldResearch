# Runde76 – vollständige lokale Reproduktion

Vorabcommit 9abc7e9ef37af8bc72672995f01cd04800cfb6bd. Ein frischer PASS,4 Originalereignisse, keine Fehlvorläufe/Korrektur. Python/NumPy/SymPy, unverändertes audit.py im bisherigen relativen bfg-review-Forschungspfad. Prüftext wird durch bestehende CI nicht automatisch ausgeführt.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,str(Path(__file__).parent/'bfg-review/research/spacetime-conservation'))
import audit
S=s.diag(1,1,0);A=s.diag(s.Rational(3,5),0,s.Rational(2,5));B=s.diag(s.Rational(3,10),s.Rational(3,10),s.Rational(2,5))
assert A!=B and s.trace(A)==s.trace(B)==1 and s.trace(S*A)==s.trace(S*B)==s.Rational(3,5)
assert s.Matrix.hstack(s.eye(3).reshape(9,1),S.reshape(9,1)).rank()==2
update=audit.load_update()
e=np.eye(4);a=e[:,0];b=e[:,3];v=(e[:,1]+e[:,2])/np.sqrt(2);u=(a+v)/np.sqrt(2)
outer=lambda x:np.outer(x,x.conj())
j=outer(a)+outer(v);p=j+outer(b);f=outer(a)+2*outer(v)+3*outer(b)
k=-np.diag([1.,2.,3.,4.]);y=np.diag([.2,.4,.7,2.])
ws=[.6*outer(u)+.4*outer(b),.6*j/2+.4*outer(b)]
seq=[];calls=0
for w in ws:
    fields=[k.copy(),f.copy(),w.copy(),y.copy(),p.copy()];out=[];mass=1.
    for step in range(2):
        o=update(*fields);calls+=1
        assert o['terminal'] is None
        mass*=o['msel'];out.append((o,mass));fields=[o[n] for n in ['k','f','w','y','p']]
    seq.append(out)
rows=[]
for step,((a,ma),(b,mb)) in enumerate(zip(*seq)):
    structure=max(np.linalg.norm(a[n]-b[n]) for n in ['k','f','y','p','t4','psel','a'])
    distance=float(np.linalg.norm(a['w']-b['w']));purities=[float(np.trace(o['w']@o['w']).real) for o in [a,b]]
    residual=max(structure,abs(a['msel']-b['msel']),abs(ma-.6),abs(mb-.6),abs(distance-1/np.sqrt(2)),abs(purities[0]-1),abs(purities[1]-.5))
    assert residual<1e-10 and abs(a['msel']-(.6 if step==0 else 1))<1e-10
    rows.append(dict(step=step+1,selection_masses=[float(o['msel']) for o in [a,b]],historical_masses=[float(ma),float(mb)],purities=purities,witness_HS_distance=distance,record_residual=float(residual)))
result=dict(status='PASS',original_calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=1e-10,exact_query_span_rank=2,exact_state_real_dimension=8,rows=rows,scope='Structural plus autonomous survival records exclude stored Witness itself; identical records do not identify general Witness. Restricted preparation families and additional measurements remain open.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
```

```json
{
  "status": "PASS",
  "original_calls": 4,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "tolerance": 1e-10,
  "exact_query_span_rank": 2,
  "exact_state_real_dimension": 8,
  "rows": [
    {
      "step": 1,
      "selection_masses": [
        0.5999999999999999,
        0.6
      ],
      "historical_masses": [
        0.5999999999999999,
        0.6
      ],
      "purities": [
        1.0,
        0.5
      ],
      "witness_HS_distance": 0.7071067811865476,
      "record_residual": 1.1102230246251565e-16
    },
    {
      "step": 2,
      "selection_masses": [
        1.0,
        1.0
      ],
      "historical_masses": [
        0.5999999999999999,
        0.6
      ],
      "purities": [
        1.0,
        0.5
      ],
      "witness_HS_distance": 0.7071067811865476,
      "record_residual": 1.1102230246251565e-16
    }
  ],
  "scope": "Structural plus autonomous survival records exclude stored Witness itself; identical records do not identify general Witness. Restricted preparation families and additional measurements remain open."
}
```
