# Prüfungen positiver Zustandskompensation

Als Python-Datei vom Repository-Wurzelverzeichnis ausführen; bestehende Auditabhängigkeiten. Gepinnter Originalupdate wird ausschließlich importiert. Hypothesen und Beweise in ENERGY_STATE_POSITIVITY.md.

```python
import json,sys
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit,pair_audit
R=s.Rational;h=31/s.sqrt(1001)
assert R(99,100)**2>h**2 and h**2>R(1,2)**2 and h<1
sx=np.array([[0.,1.],[1.,0.]]);I=np.eye(2);k=2*I+sx;f=I.copy();y=np.diag([.2,.3])
update=audit.load_update();rows=[];ref=None
for r in (s.S.One,R(99,100),R(1,2)):
    w=(I+float(r)*sx)/2
    out=pair_audit.source_aligned(update,k,f,w,y)
    inv=(I+float(r/h)*sx)/2
    ev=np.linalg.eigvalsh(inv)
    ein=float(np.trace(w@k).real);emax=float(np.linalg.eigvalsh(out['k'])[-1]);einv=float(np.trace(inv@out['k']).real)
    assert abs(einv-ein)<1e-12 and abs(np.trace(inv)-1)<1e-12
    assert np.linalg.norm(out['w']-w)<1e-12
    if r>h:assert ev[0]<0 and ein>emax+1e-4
    else:assert ev[0]>0 and ein<emax
    rows.append(dict(r=str(r),inverse_min_eigenvalue=float(ev[0]),energy_input=ein,source_energy_output=float(np.trace(out['w']@out['k']).real),maximum_possible_positive_output_energy=emax,spectral_excess=ein-emax,inverse_energy=einv))
    if r==R(99,100):ref=(w,out)
rng=np.random.default_rng(20261030);g=audit.complex_unitary(rng,2);conj=lambda x:g@x@g.conj().T
w,original=ref;out=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(y))
gauge=max(float(np.linalg.norm(out[key]-conj(original[key]))) for key in ('k','f','w','y'))
assert gauge<1e-12
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=4,seed=20261030,symbolic=dict(h=str(h),inverse_eigenvalues='(1 +/- r/h)/2',strict_positive_input_r='99/100',strict_r_square_minus_h_square=str(s.factor(R(99,100)**2-h**2)),partial_feasible_r='1/2'),cases=rows,gauge_residual=gauge,scope='State compensation cannot universally preserve a K-proportional isolated energy while maintaining density positivity; partial mixed-state feasibility retained. Actual W update unchanged.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 4,
  "seed": 20261030,
  "symbolic": {
    "h": "31*sqrt(1001)/1001",
    "inverse_eigenvalues": "(1 +/- r/h)/2",
    "strict_positive_input_r": "99/100",
    "strict_r_square_minus_h_square": "200801/10010000",
    "partial_feasible_r": "1/2"
  },
  "cases": [
    {
      "r": "1",
      "inverse_min_eigenvalue": -0.010299742566334702,
      "energy_input": 3,
      "source_energy_output": 2.9798162889235713,
      "maximum_possible_positive_output_energy": 2.9798162889235718,
      "spectral_excess": 0.020183711076428246,
      "inverse_energy": 3
    },
    {
      "r": "99/100",
      "inverse_min_eigenvalue": -0.005196745140671366,
      "energy_input": 2.99,
      "source_energy_output": 2.970018126034336,
      "maximum_possible_positive_output_energy": 2.9798162889235718,
      "spectral_excess": 0.010183711076428459,
      "inverse_energy": 2.9899999999999998
    },
    {
      "r": "1/2",
      "inverse_min_eigenvalue": 0.24485012871683265,
      "energy_input": 2.5,
      "source_energy_output": 2.489908144461786,
      "maximum_possible_positive_output_energy": 2.9798162889235718,
      "spectral_excess": -0.47981628892357175,
      "inverse_energy": 2.5
    }
  ],
  "gauge_residual": 7.65897505568125e-16,
  "scope": "State compensation cannot universally preserve a K-proportional isolated energy while maintaining density positivity; partial mixed-state feasibility retained. Actual W update unchanged."
}
```
