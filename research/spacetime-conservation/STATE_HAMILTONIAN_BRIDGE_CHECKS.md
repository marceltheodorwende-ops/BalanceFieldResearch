# Runde73 – vollständige lokale Reproduktion

Vorabprotokoll ccf72051459c8852049c6b3fd85e6083ebc32ab2. Ein frischer PASS,3 Originalaufrufe, keine Fehlvorläufe/Korrektur. Ausführen mit Python/NumPy/SymPy und unverändertem audit.py im relativen bfg-review-Forschungspfad wie bisherige Reproduktionen. Prüfcode ist hier Dokumenttext, nicht automatisch Bestandteil der CI.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,str(Path(__file__).parent/'bfg-review/research/spacetime-conservation'))
import audit
f,z=s.symbols('f z', positive=True)
assert s.simplify(f/(f+z)+z/(f+z))==1
F=s.diag(1,3);W=s.diag(s.Rational(3,4),s.Rational(1,4));S=s.diag(1,0)
assert s.trace(S*W)==s.Rational(3,4)
assert s.trace(S*F)/s.trace(F)==s.Rational(1,4)
update=audit.load_update()
o=update(-np.eye(2),np.diag([1.,3.]),np.diag([.75,.25]),np.diag([.5,2.]),np.eye(2))
assert o['terminal'] is None and abs(o['msel']-.75)<1e-10
p=np.diag([1.,1.,0.,0.]);ff=np.diag([1.,2.,0.,0.]);w=np.zeros((4,4));w[:2,:2]=.5
k=-np.diag([1.,2.,3.,4.]);y=np.array([[.25,.03,.02,.01],[.03,.35,.03,.04],[.02,.03,.45,.03],[.01,.04,.03,.55]])
rows=[]
g=audit.complex_unitary(np.random.default_rng(20261123),4)
for name,u in [('base',np.eye(4)),('complex_gauge',g)]:
    kk,fi,wi,yi,pi=[u@a@u.conj().T for a in [k,ff,w,y,p]]
    out=update(kk,fi,wi,yi,pi)
    assert out['terminal'] is None and abs(out['msel']-1)<1e-10
    v=out['t4']@pi;seed=out['p']-v@pi@v.conj().T
    strength=float(np.trace(out['f']-v@fi@v.conj().T).real)
    stock=float(np.trace(fi).real);rho=out['f']/np.trace(out['f'])
    expected=(v@fi@v.conj().T+strength*seed)/(stock+strength)
    residual=float(np.linalg.norm(rho-expected))
    aw=float(np.trace(seed@out['w']).real);bw=float(np.trace(seed@rho).real)
    assert strength>0 and abs(np.trace(seed).real-1)<1e-10
    assert max(residual,abs(aw),abs(bw-strength/(stock+strength)))<1e-10
    rows.append(dict(label=name,seed_strength=strength,formation_seed_probability=bw,witness_seed_probability=aw,normalization_residual=residual))
assert abs(rows[0]['formation_seed_probability']-rows[1]['formation_seed_probability'])<1e-10
result=dict(status='PASS',original_calls=3,source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=1e-10,actual_selection_mass=float(o['msel']),formation_comparison_mass='1/4',witness_comparison_mass='3/4',seed_controls=rows,scope='Internal conditioning and formation injection differ; no physical instrument/state/Hamiltonian identification assumed.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

```json
{
  "status": "PASS",
  "original_calls": 3,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "tolerance": 1e-10,
  "actual_selection_mass": 0.75,
  "formation_comparison_mass": "1/4",
  "witness_comparison_mass": "3/4",
  "seed_controls": [
    {
      "label": "base",
      "seed_strength": 1.9992016499278686,
      "formation_seed_probability": 0.39990418269219347,
      "witness_seed_probability": -3.0527754325482176e-17,
      "normalization_residual": 1.065011082121043e-16
    },
    {
      "label": "complex_gauge",
      "seed_strength": 1.9992016499278729,
      "formation_seed_probability": 0.3999041826921945,
      "witness_seed_probability": -2.3451970617219264e-16,
      "normalization_residual": 5.649230453031742e-16
    }
  ],
  "scope": "Internal conditioning and formation injection differ; no physical instrument/state/Hamiltonian identification assumed."
}
```
