# Prüfungen der manuskriptinternen Energieerwartungskandidaten

Als Python-Datei vom Repository-Wurzelverzeichnis ausführen; vorhandene Auditabhängigkeiten. Nur Import des gepinnten Originalupdates. Hypothesen/Beweise in QUANTUM_ENERGY_READOUT.md.

```python
import json,sys
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit,pair_audit
R=s.Rational
alpha=pair_audit.alpha_exact([R(1,5),R(3,10)],[1,1]);beta=1-alpha
h=s.simplify((alpha+beta*R(1,5)*R(3,10))/s.sqrt((alpha+beta*R(1,5)**2)*(alpha+beta*R(3,10)**2)))
assert alpha==R(8,133) and h==31/s.sqrt(1001) and h**2<1
a,u,v=s.symbols('a u v',positive=True);b=1-a
assert s.factor((a+b*u*u)*(a+b*v*v)-(a+b*u*v)**2-a*b*(u-v)**2)==0
update=audit.load_update();I=np.eye(2);sx=np.array([[0.,1.],[1.,0.]])
f=I.copy();y=np.diag([.2,.3]);w=(I+.5*sx)/2
rows=[];outplus=None
def control(label,k,f,w,y,expected):
    out=pair_audit.source_aligned(update,k,f,w,y)
    before=float(np.trace(w@k).real);after=float(np.trace(out['w']@out['k']).real)
    ef=float(np.trace((out['f']/np.trace(out['f']))@out['k']).real)
    fixed=max(float(np.linalg.norm(out['w']-w)),float(np.linalg.norm(out['f']-f)))
    assert abs(after-expected)<1e-12 and abs(np.trace(out['k']).real-4)<1e-12 and abs(ef-2)<1e-12 and fixed<1e-12
    rows.append(dict(label=label,witness_energy_before=before,witness_energy_after=after,witness_defect=after-before,formation_energy_after=ef,kernel_trace=float(np.trace(out['k']).real),fixed_field_residual=fixed))
    return out
for sign in (-1,1):
    out=control('Ksign'+str(sign),2*I+sign*sx,f,w,y,2+sign*float(h)/2)
    if sign==1:outplus=out
control('commuting_W',2*I+sx,f,I/2,y,2.)
rng=np.random.default_rng(20261029);g=audit.complex_unitary(rng,2);conj=lambda x:g@x@g.conj().T
gout=control('gauge_plus',conj(2*I+sx),conj(f),conj(w),conj(y),2+float(h)/2)
gauge=max(float(np.linalg.norm(gout[key]-conj(outplus[key]))) for key in ('k','f','w','y'))
assert gauge<1e-12
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=4,seed=20261029,symbolic=dict(alpha=str(alpha),h=str(h),witness_defect_plus=str((h-1)/2),witness_defect_minus=str((1-h)/2),formation_defect='0',fixed_expectation_condition='[rho,Y]=0 for conservation for every Hermitian K at fixed full-persistence geometry'),gauge_residual=gauge,cases=rows,scope='Conditional rho_Q=W or F/trF, H proportional to K energy-readout audit; no physical calibration or general open-system no-go.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 4,
  "seed": 20261029,
  "symbolic": {
    "alpha": "8/133",
    "h": "31*sqrt(1001)/1001",
    "witness_defect_plus": "-1/2 + 31*sqrt(1001)/2002",
    "witness_defect_minus": "1/2 - 31*sqrt(1001)/2002",
    "formation_defect": "0",
    "fixed_expectation_condition": "[rho,Y]=0 for conservation for every Hermitian K at fixed full-persistence geometry"
  },
  "gauge_residual": 2.0859727843219497e-15,
  "cases": [
    {
      "label": "Ksign-1",
      "witness_energy_before": 1.5,
      "witness_energy_after": 1.5100918555382141,
      "witness_defect": 0.010091855538214123,
      "formation_energy_after": 2,
      "kernel_trace": 4,
      "fixed_field_residual": 0
    },
    {
      "label": "Ksign1",
      "witness_energy_before": 2.5,
      "witness_energy_after": 2.489908144461786,
      "witness_defect": -0.010091855538214123,
      "formation_energy_after": 2,
      "kernel_trace": 4,
      "fixed_field_residual": 0
    },
    {
      "label": "commuting_W",
      "witness_energy_before": 2,
      "witness_energy_after": 2,
      "witness_defect": 0,
      "formation_energy_after": 2,
      "kernel_trace": 4,
      "fixed_field_residual": 0
    },
    {
      "label": "gauge_plus",
      "witness_energy_before": 2.4999999999999996,
      "witness_energy_after": 2.4899081444617845,
      "witness_defect": -0.010091855538215011,
      "formation_energy_after": 1.9999999999999987,
      "kernel_trace": 3.9999999999999973,
      "fixed_field_residual": 9.111136944271803e-16
    }
  ],
  "scope": "Conditional rho_Q=W or F/trF, H proportional to K energy-readout audit; no physical calibration or general open-system no-go."
}
```
