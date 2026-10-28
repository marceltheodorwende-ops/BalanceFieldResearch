# Frische Originalkontrollen fester Bestandsgewichte

Code als Python-Datei vom Repository-Wurzelverzeichnis ausführen; vorhandene Auditabhängigkeiten. Nur Import des gepinnten Originalupdates. Beweise und Geltungsbereiche in LINEAR_STOCK_LIMIT.md.

```python
import sys,json
from pathlib import Path
import numpy as np
sys.path.insert(0,'research/spacetime-conservation')
import audit
update=audit.load_update()
rows=[]
def check(label,k,f,w,y,p):
    o=update(k,f,w,y,p)
    assert o['terminal'] is None
    n=len(k); s4=o['t4']@o['t4'].conj().T
    b4=sum(t@s4@t.conj().T for t in (o['u'][:n],o['u'][n:]))
    x=b4-p
    da=float(np.trace(o['p']@o['k']).real-np.trace(p@k).real)
    df=float(np.trace(o['f']).real-np.trace(f).real)
    prediction=float(np.trace(k@x).real)
    assert abs(da+df-prediction)<1e-12
    assert abs(np.trace(x))<1e-12 and np.linalg.norm(p@x@p-x)<1e-12
    assert np.min(np.linalg.eigvalsh(b4))>-1e-12
    assert np.min(np.linalg.eigvalsh(2*p-b4))>-1e-12
    rows.append(dict(label=label,input_rank=int(round(np.trace(p))),output_rank=int(round(np.trace(o['p']))),alpha=o['alpha'],delta_active=da,delta_formation=df,combined_defect=da+df,predicted_defect=prediction,X=x.real.tolist(),trace_X=float(np.trace(x).real),X_eigenvalues=np.linalg.eigvalsh(x).tolist()))
    return x,da,df
v=np.array([np.sqrt(3)/2,.5,0.]);p=np.outer(v,v)
x,da,df=check('rank1',-np.diag([2.,3.,5.]),p,p,np.diag([.2,.4,.6]),p)
assert abs(da+2.25)<1e-12 and abs(df-2.25)<1e-12 and np.linalg.norm(x)<1e-12
p=np.diag([1.,1.,0.]);f=np.diag([1.,.42,0.]);w=p/2;y=np.array([[.25,0,.1],[0,.5,.1],[.1,.1,.5]])
x,da,df=check('rank2_base',-np.diag([1.,2.,3.]),f,w,y,p)
d=da+df
xx,da,df=check('rank2_swapped',-np.diag([2.,1.,3.]),f,w,y,p)
assert np.linalg.norm(x-xx)<1e-12 and abs(da+df+d)<1e-12
xx,da,df=check('rank2_scalar',-np.eye(3),f,w,y,p)
assert np.linalg.norm(x-xx)<1e-12 and abs(da+df)<1e-12
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=4,cases=rows,scope='Fixed linear stock coefficients; rank1/scalar special conservation and sign reversal, not general physical energy impossibility.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 4,
  "cases": [
    {
      "label": "rank1",
      "input_rank": 1,
      "output_rank": 2,
      "alpha": 0.05882352941176469,
      "delta_active": -2.2499999999999982,
      "delta_formation": 2.249999999999999,
      "combined_defect": 8.881784197001252e-16,
      "predicted_defect": 2.220446049250313e-16,
      "X": [
        [
          -1.1102230246251565e-16,
          -5.551115123125783e-17,
          0
        ],
        [
          -1.1102230246251565e-16,
          0,
          0
        ],
        [
          0,
          0,
          0
        ]
      ],
      "trace_X": -1.1102230246251565e-16,
      "X_eigenvalues": [
        -1.7963785889362148e-16,
        0,
        6.861555643110582e-17
      ]
    },
    {
      "label": "rank2_base",
      "input_rank": 2,
      "output_rank": 3,
      "alpha": 0.1,
      "delta_active": -1.2503003604325187,
      "delta_formation": 1.2568997908165365,
      "combined_defect": 0.006599430384017779,
      "predicted_defect": 0.006599430384018001,
      "X": [
        [
          0.006599430384017557,
          -0.01539946037568922,
          -4.85023479271675e-18
        ],
        [
          -0.01539946037568922,
          -0.006599430384017779,
          1.0808096224738149e-16
        ],
        [
          -4.85023479271675e-18,
          1.0808096224738149e-16,
          1.1777884948761404e-32
        ]
      ],
      "trace_X": -2.220446049250313e-16,
      "X_eigenvalues": [
        -0.016753980460055506,
        2.2834897614194288e-31,
        0.01675398046005528
      ]
    },
    {
      "label": "rank2_swapped",
      "input_rank": 2,
      "output_rank": 3,
      "alpha": 0.1,
      "delta_active": -1.7496996395674795,
      "delta_formation": 1.7431002091834626,
      "combined_defect": -0.006599430384016891,
      "predicted_defect": -0.006599430384017335,
      "X": [
        [
          0.006599430384017557,
          -0.01539946037568922,
          -4.85023479271675e-18
        ],
        [
          -0.01539946037568922,
          -0.006599430384017779,
          1.0808096224738149e-16
        ],
        [
          -4.85023479271675e-18,
          1.0808096224738149e-16,
          1.1777884948761404e-32
        ]
      ],
      "trace_X": -2.220446049250313e-16,
      "X_eigenvalues": [
        -0.016753980460055506,
        2.2834897614194288e-31,
        0.01675398046005528
      ]
    },
    {
      "label": "rank2_scalar",
      "input_rank": 2,
      "output_rank": 3,
      "alpha": 0.1,
      "delta_active": -0.9999999999999991,
      "delta_formation": 1,
      "combined_defect": 8.881784197001252e-16,
      "predicted_defect": 2.220446049250313e-16,
      "X": [
        [
          0.006599430384017557,
          -0.01539946037568922,
          -4.85023479271675e-18
        ],
        [
          -0.01539946037568922,
          -0.006599430384017779,
          1.0808096224738149e-16
        ],
        [
          -4.85023479271675e-18,
          1.0808096224738149e-16,
          1.1777884948761404e-32
        ]
      ],
      "trace_X": -2.220446049250313e-16,
      "X_eigenvalues": [
        -0.016753980460055506,
        2.2834897614194288e-31,
        0.01675398046005528
      ]
    }
  ],
  "scope": "Fixed linear stock coefficients; rank1/scalar special conservation and sign reversal, not general physical energy impossibility."
}
```
