# Prüfungen momentan kommutierender Energieablesungen

Als Python-Datei aus dem Repository-Wurzelverzeichnis ausführen; bestehende Auditabhängigkeiten. Gepinnter Originalupdate wird nur importiert. Die exakte Kollisionspartition wird symbolisch bewiesen und dann explizit ausgewertet. Hypothesen/Beweise in COMMUTING_ENERGY_READOUT.md.

```python
import json,sys
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit,pair_audit
R=s.Rational;ys=[R(1,5),R(4,5)];a=pair_audit.alpha_exact(ys,[1,3])
assert a==R(11,36)
assert pair_audit.g(ys[0],a)==pair_audit.g(ys[1],a)==R(25,108)
h=s.simplify((a+(1-a)*ys[0]*ys[1])/s.sqrt((a+(1-a)*ys[0]**2)*(a+(1-a)*ys[1]**2)))
assert h==R(5,6)
update=audit.load_update();I=np.eye(2);sx=np.array([[0.,1.],[1.,0.]])
k=2*I+sx;w=(I+.5*sx)/2
def pinch(z,k,scalar=False):
    if scalar:
        assert np.linalg.norm(z-np.trace(z)*I/2)<1e-12
        return k.copy()
    vals,u=np.linalg.eigh(z);assert abs(vals[1]-vals[0])>1e-8
    return sum(np.outer(u[:,j],u[:,j].conj())@k@np.outer(u[:,j],u[:,j].conj()) for j in (0,1))
f=np.diag([1.,3.]);y=np.diag([.2,.8]);o=pair_audit.source_aligned(update,k,f,w,y)
hy0=pinch(y,k);hy1=pinch(o['y'],o['k'],True)
assert np.linalg.norm(hy0-2*I)<1e-12 and np.linalg.norm(hy1-(2*I+5*sx/6))<1e-12
collision=dict(alpha=o['alpha'],output_load=o['y'].real.tolist(),H_before=hy0.real.tolist(),H_after=hy1.real.tolist(),energy_before=float(np.trace(w@hy0).real),energy_after=float(np.trace(o['w']@hy1).real))
assert abs(collision['energy_after']-29/12)<1e-12
low=np.diag([.2,.3]);p=pair_audit.source_aligned(update,k,I,w,low)
positive_res=float(np.linalg.norm(pinch(p['y'],p['k'])-pinch(low,k)))
assert positive_res<1e-12
ff=I+.5*sx;q=pair_audit.source_aligned(update,k,ff,w,low)
hf0=pinch(ff,k);hf1=pinch(q['f'],q['k'])
formation=dict(field_residual=float(np.linalg.norm(q['f']-ff)),H_change=float(np.linalg.norm(hf1-hf0)),energy_before=float(np.trace(w@hf0).real),energy_after=float(np.trace(q['w']@hf1).real))
assert formation['H_change']>1e-3 and formation['field_residual']<1e-12
rng=np.random.default_rng(20261031);g=audit.complex_unitary(rng,2);conj=lambda x:g@x@g.conj().T
go=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y))
gh0=pinch(conj(y),conj(k));gh1=pinch(go['y'],go['k'],True)
gauge=max(float(np.linalg.norm(gh0-conj(hy0))),float(np.linalg.norm(gh1-conj(hy1))))
assert gauge<1e-12
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=4,seed=20261031,symbolic=dict(alpha='11/36',collision_load='25/108',h='5/6',collision_energy_change='5/12'),collision=collision,no_collision_HY_residual=positive_res,formation_pinning=formation,gauge_residual=gauge,scope='Instantaneous Y-commutant pinching is invariant without new spectral mergers but can fail at an exact collision; F pinching is not a general replacement. No physical Hamiltonian selected.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 4,
  "seed": 20261031,
  "symbolic": {
    "alpha": "11/36",
    "collision_load": "25/108",
    "h": "5/6",
    "collision_energy_change": "5/12"
  },
  "collision": {
    "alpha": 0.3055555555555555,
    "output_load": [
      [
        0.23148148148148143,
        0
      ],
      [
        0,
        0.23148148148148148
      ]
    ],
    "H_before": [
      [
        2,
        0
      ],
      [
        0,
        2
      ]
    ],
    "H_after": [
      [
        2,
        0.8333333333333335
      ],
      [
        0.8333333333333335,
        2.0000000000000004
      ]
    ],
    "energy_before": 2,
    "energy_after": 2.416666666666667
  },
  "no_collision_HY_residual": 6.280369834735101e-16,
  "formation_pinning": {
    "field_residual": 0,
    "H_change": 0.028544077943305043,
    "energy_before": 2.499999999999999,
    "energy_after": 2.4899081444617845
  },
  "gauge_residual": 9.985997127080695e-16,
  "scope": "Instantaneous Y-commutant pinching is invariant without new spectral mergers but can fail at an exact collision; F pinching is not a general replacement. No physical Hamiltonian selected."
}
```
