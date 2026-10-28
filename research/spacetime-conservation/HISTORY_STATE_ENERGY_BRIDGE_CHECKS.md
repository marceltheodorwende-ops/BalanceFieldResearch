# Runde74 – vollständige lokale Reproduktion

Vorabcommit b74ac163b4c9266435435e0ed308038357df4d55. Ein frischer PASS,6 Originalaufrufe, keine Fehlvorläufe/Korrektur. Python/NumPy/SymPy, unverändertes audit.py im bisherigen relativen bfg-review-Forschungspfad. Dokumenttext wird nicht automatisch von CI ausgeführt.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,str(Path(__file__).parent/'bfg-review/research/spacetime-conservation'))
import audit
f=s.diag(1,2);w=s.ones(2)/2;d=w-f/3
assert d*d==s.eye(2)*s.Rational(5,18)
assert s.trace(w*f)==s.Rational(3,2)
update=audit.load_update()
p=np.diag([1.,1.,0.,0.]);ff=np.diag([1.,2.,0.,0.]);ww=np.zeros((4,4));ww[:2,:2]=.5
k=-np.diag([1.,2.,3.,4.]);y=np.array([[.25,.03,.02,.01],[.03,.35,.03,.04],[.02,.03,.45,.03],[.01,.04,.03,.55]])
g=audit.complex_unitary(np.random.default_rng(20261124),4)
rows=[];calls=0
for name,u in [('base',np.eye(4)),('complex_gauge',g)]:
    ki,fi,wi,yi,pi=[u@a@u.conj().T for a in [k,ff,ww,y,p]]
    ancestor=fi.copy();carrier=pi.copy();seed_total=np.zeros_like(fi)
    for step in range(3):
        o=update(ki,fi,wi,yi,pi);calls+=1
        assert o['terminal'] is None and abs(o['msel']-1)<1e-10
        v=o['t4']@pi
        ancestor=v@ancestor@v.conj().T;carrier=v@carrier@v.conj().T
        seed_total=v@seed_total@v.conj().T+o['f']-v@fi@v.conj().T
        rho=ancestor/3
        distance=float(sum(abs(np.linalg.eigvalsh(o['w']-rho)))/2)
        e1=float(np.trace(o['w']@ancestor).real)
        e2=float(np.trace(o['w']@(2*ancestor+carrier)).real)
        residual=max(abs(distance-np.sqrt(10)/6),abs(e1-1.5),abs(e2-4),abs(np.trace(rho)-1),np.linalg.norm(o['f']-ancestor-seed_total),np.linalg.norm(seed_total@rho),np.linalg.norm(seed_total@o['w']),np.linalg.norm(carrier@rho-rho))
        assert min(np.linalg.eigvalsh(rho))>-1e-10 and residual<1e-10
        rows.append(dict(label=name,step=step+1,trace_distance=distance,history_expectation=e1,alternative_expectation=e2,formation_stock=float(np.trace(o['f']).real),residual=float(residual)))
        ki,fi,wi,yi,pi=[o[n] for n in ['k','f','w','y','p']]
result=dict(status='PASS',original_calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261124,tolerance=1e-10,exact_distance='sqrt(10)/6',exact_expectations=['3/2','4'],rows=rows,max_residual=max(r['residual'] for r in rows),scope='Historical inherited formation supplies a distinct transported density and many internal conserved observables; no physical state or Hamiltonian chosen.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

```json
{
  "status": "PASS",
  "original_calls": 6,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261124,
  "tolerance": 1e-10,
  "exact_distance": "sqrt(10)/6",
  "exact_expectations": [
    "3/2",
    "4"
  ],
  "rows": [
    {
      "label": "base",
      "step": 1,
      "trace_distance": 0.5270462766947299,
      "history_expectation": 1.5000000000000004,
      "alternative_expectation": 4.000000000000001,
      "formation_stock": 4.999201649927869,
      "residual": 8.881784197001252e-16
    },
    {
      "label": "base",
      "step": 2,
      "trace_distance": 0.52704627669473,
      "history_expectation": 1.5000000000000013,
      "alternative_expectation": 4.000000000000003,
      "formation_stock": 6.573149300719202,
      "residual": 2.6645352591003757e-15
    },
    {
      "label": "base",
      "step": 3,
      "trace_distance": 0.52704627669473,
      "history_expectation": 1.5000000000000004,
      "alternative_expectation": 4.0,
      "formation_stock": 6.573149300719202,
      "residual": 1.5841363461219332e-15
    },
    {
      "label": "complex_gauge",
      "step": 1,
      "trace_distance": 0.5270462766947299,
      "history_expectation": 1.5000000000000024,
      "alternative_expectation": 4.000000000000006,
      "formation_stock": 4.999201649927871,
      "residual": 6.217248937900877e-15
    },
    {
      "label": "complex_gauge",
      "step": 2,
      "trace_distance": 0.5270462766947297,
      "history_expectation": 1.5000000000000022,
      "alternative_expectation": 4.000000000000006,
      "formation_stock": 6.5731493007192245,
      "residual": 6.217248937900877e-15
    },
    {
      "label": "complex_gauge",
      "step": 3,
      "trace_distance": 0.5270462766947298,
      "history_expectation": 1.5000000000000027,
      "alternative_expectation": 4.000000000000007,
      "formation_stock": 6.573149300719224,
      "residual": 7.105427357601002e-15
    }
  ],
  "max_residual": 7.105427357601002e-15,
  "scope": "Historical inherited formation supplies a distinct transported density and many internal conserved observables; no physical state or Hamiltonian chosen."
}
```
