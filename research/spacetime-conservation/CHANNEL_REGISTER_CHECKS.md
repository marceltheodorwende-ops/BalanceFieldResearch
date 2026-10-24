# Kontrollen des C/B-Kanalregisters

Als Python-Datei vom Repository-Wurzelverzeichnis ausführen; vorhandene Auditabhängigkeiten. Gepinnter Originalupdate wird nur importiert. Hypothesen, Darstellung/Quelltrennung und Beweise in CHANNEL_REGISTER_ENERGY.md.

```python
import json,sys
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit,pair_audit
R=s.Rational;I=s.eye(2)
sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-s.I],[s.I,0]])
tc=s.diag(s.sqrt(R(8,13)),s.sqrt(R(32,77)))
tb=s.diag(s.sqrt(R(5,13)),s.sqrt(R(45,77)))
ops=[tc,tb];h=31/s.sqrt(1001)
assert tc*tc+tb*tb==I
def gamma(w):return s.Matrix(2,2,lambda a,b:s.simplify(s.trace(ops[a]*w*ops[b])))
common=gamma(I/2)
for axis in (sx,sy):
    assert gamma((I+axis/2)/2)==common and gamma((I-axis/2)/2)==common
    k=2*I+axis;pk=sum((t*k*t for t in ops),s.zeros(2))
    assert all(s.simplify(x)==0 for x in pk-(2*I+h*axis))
r0,r1,r2,r3=s.symbols('r0 r1 r2 r3',real=True)
rr=s.Matrix([[r0,r2+s.I*r3],[r2-s.I*r3,r1]])
pull=sum((rr[a,b]*ops[a]*ops[b] for a in range(2) for b in range(2)),s.zeros(2))
assert pull[0,1]==0 and pull[1,0]==0 and 1-h!=0
update=audit.load_update();nf=np.eye(2);ny=np.diag([.2,.3]);nt=[np.array(t,float) for t in ops]
gammas=[];rows=[]
for label,axis in (('x',np.array(sx,complex)),('y',np.array(sy,complex))):
    k=2*nf+axis
    for sign in (-1,1):
        w=(nf+sign*axis/2)/2
        out=pair_audit.source_aligned(update,k,nf,w,ny)
        g=np.array([[np.trace(a@w@b) for b in nt] for a in nt]);gammas.append(g)
        before=float(np.trace(w@k).real);after=float(np.trace(out['w']@out['k']).real)
        prediction=sign*(float(h)-1)/2
        assert abs(after-before-prediction)<1e-12 and np.linalg.norm(out['w']-w)<1e-12
        assert np.linalg.norm(out['k']-sum(t@k@t for t in nt))<1e-12
        rows.append(dict(axis=label,witness_sign=sign,energy_before=before,energy_after=after,energy_defect=after-before))
gd=max(float(np.linalg.norm(g-gammas[0])) for g in gammas)
assert gd<1e-12
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=4,symbolic=dict(h=str(h),register_density=[[str(x) for x in row] for row in common.tolist()],register_energy_pullback_offdiagonals=['0','0'],system_defect_offdiagonal='1-31/sqrt(1001)'),register_density_real=gammas[0].real.tolist(),register_density_imag=gammas[0].imag.tolist(),register_equality_residual=gd,cases=rows,scope='Canonical mathematical C/B complement cannot alone carry the coherence-dependent energy deficit by additive register-local energy; not a physical environment or general interaction-energy no-go.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 4,
  "symbolic": {
    "h": "31*sqrt(1001)/1001",
    "register_density": [
      [
        "516/1001",
        "155*sqrt(10)/1001"
      ],
      [
        "155*sqrt(10)/1001",
        "485/1001"
      ]
    ],
    "register_energy_pullback_offdiagonals": [
      "0",
      "0"
    ],
    "system_defect_offdiagonal": "1-31/sqrt(1001)"
  },
  "register_density_real": [
    [
      0.5154845154845155,
      0.48966337395214665
    ],
    [
      0.48966337395214665,
      0.48451548451548454
    ]
  ],
  "register_density_imag": [
    [
      0,
      0
    ],
    [
      0,
      0
    ]
  ],
  "register_equality_residual": 0,
  "cases": [
    {
      "axis": "x",
      "witness_sign": -1,
      "energy_before": 1.5,
      "energy_after": 1.5100918555382141,
      "energy_defect": 0.010091855538214123
    },
    {
      "axis": "x",
      "witness_sign": 1,
      "energy_before": 2.5,
      "energy_after": 2.489908144461786,
      "energy_defect": -0.010091855538214123
    },
    {
      "axis": "y",
      "witness_sign": -1,
      "energy_before": 1.5,
      "energy_after": 1.5100918555382141,
      "energy_defect": 0.010091855538214123
    },
    {
      "axis": "y",
      "witness_sign": 1,
      "energy_before": 2.5,
      "energy_after": 2.489908144461786,
      "energy_defect": -0.010091855538214123
    }
  ],
  "scope": "Canonical mathematical C/B complement cannot alone carry the coherence-dependent energy deficit by additive register-local energy; not a physical environment or general interaction-energy no-go."
}
```
