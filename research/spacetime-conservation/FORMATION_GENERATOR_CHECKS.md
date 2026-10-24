# Runde57: F-Generator-/Endpointkontrolle

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Ein lokaler Lauf PASS, drei Originalereignisse, keine Fehler oder Korrekturen. Symbolische Irrationalitätskontrolle steht getrennt von den Gleitkomma-Ansatzdefekten. Physikalische Zusatzannahmen und Grenzen: FORMATION_GENERATOR_COMPATIBILITY.md. Empirisches main wird nicht ausgeführt.

```python
import sys,json
from pathlib import Path
import sympy as s
import numpy as np
sys.path.insert(0,'research/spacetime-conservation')
import audit
x=s.symbols('x');ratio=(s.sqrt(3)-1)/(s.sqrt(2)-1);poly=s.Poly(s.minpoly(ratio,x),x)
assert poly.degree()==4 and poly.is_irreducible
F=s.diag(1,s.sqrt(2),s.sqrt(3));W=s.eye(3)/3+(s.ones(3)-s.eye(3))/12
assert sorted(W.eigenvals().keys())==[s.Rational(1,4),s.Rational(1,2)] and F*W!=W*F
comm=s.simplify(F*W-W*F)
update=audit.load_update();calls=0
def unitary(f,sigma):
    e,u=np.linalg.eigh(f);return (u*np.exp(-1j*sigma*e))@u.conj().T
def run(f,w,y,sigma):
    global calls
    n=len(f);o=update(-np.eye(n),f,w,y,np.eye(n));calls+=1;assert o['terminal'] is None
    v=o['t4'];u=unitary(f,sigma);prediction=v@u@w@u.conj().T@v.conj().T
    source=float(np.linalg.norm(o['w']-v@w@v.conj().T));fr=float(np.linalg.norm(o['f']-v@f@v.conj().T))
    defect=float(np.linalg.norm(o['w']-prediction));energy=float(np.trace(w@f).real);energy_out=float(np.trace(o['w']@o['f']).real)
    assert max(source,fr,abs(energy-energy_out))<1e-10
    return dict(source_witness_transport_residual=source,formation_transport_residual=fr,conditional_unitary_defect=defect,energy=energy,energy_out=energy_out,minimum_witness_eigenvalue=float(np.linalg.eigvalsh(w).min()))
f=np.array(F.tolist(),float);w=np.array(W.tolist(),float);y=np.diag([.2,.3,.4])
row=run(f,w,y,.7);assert row['conditional_unitary_defect']>1e-3
rng=np.random.default_rng(20261107);g=audit.complex_unitary(rng,3);conj=lambda a:g@a@g.conj().T
gauged=run(conj(f),conj(w),conj(y),.7);gauge=abs(gauged['conditional_unitary_defect']-row['conditional_unitary_defect']);assert gauge<1e-10
fq=np.diag([1.,3.]);wq=np.array([[.5,.25],[.25,.5]],complex)
qubit=run(fq,wq,np.diag([.2,.3]),np.pi);assert qubit['conditional_unitary_defect']<1e-10
anti=unitary(fq,np.pi/2);antidefect=float(np.linalg.norm(wq-anti@wq@anti.conj().T));assert antidefect>.5
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261107,gap_ratio_minimal_polynomial=str(poly.as_expr()),gap_ratio_degree=poly.degree(),symbolic_commutator=[[str(z) for z in row] for row in comm.tolist()],n3_sigma=.7,n3=row,gauge_case=gauged,gauge_defect_residual=gauge,qubit_resonance_sigma='pi',qubit=qubit,qubit_pi_over_2_defect=antidefect,scope='Conditional unitary F-generator fails at every nonzero duration for the exact n3 witness under source R4 connection. Conservation alone does not identify a physical Hamiltonian; general instruments/connections remain open.')

print(json.dumps(result,indent=2))

```

Rohdaten:

```json
{
  "status": "PASS",
  "calls": 3,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261107,
  "gap_ratio_minimal_polynomial": "x**4 + 4*x**3 - 16*x**2 + 8*x + 4",
  "gap_ratio_degree": 4,
  "symbolic_commutator": [
    [
      "0",
      "1/12 - sqrt(2)/12",
      "1/12 - sqrt(3)/12"
    ],
    [
      "-1/12 + sqrt(2)/12",
      "0",
      "-sqrt(3)/12 + sqrt(2)/12"
    ],
    [
      "-1/12 + sqrt(3)/12",
      "-sqrt(2)/12 + sqrt(3)/12",
      "0"
    ]
  ],
  "n3_sigma": 0.7,
  "n3": {
    "source_witness_transport_residual": 0,
    "formation_transport_residual": 0,
    "conditional_unitary_defect": 0.07356721246162591,
    "energy": 1.3820881233139908,
    "energy_out": 1.3820881233139908,
    "minimum_witness_eigenvalue": 0.25000000000000006
  },
  "gauge_case": {
    "source_witness_transport_residual": 3.802725945530395e-16,
    "formation_transport_residual": 1.1604538332693262e-15,
    "conditional_unitary_defect": 0.07356721246162583,
    "energy": 1.3820881233139901,
    "energy_out": 1.3820881233139897,
    "minimum_witness_eigenvalue": 0.2499999999999999
  },
  "gauge_defect_residual": 8.326672684688674e-17,
  "qubit_resonance_sigma": "pi",
  "qubit": {
    "source_witness_transport_residual": 0,
    "formation_transport_residual": 0,
    "conditional_unitary_defect": 8.659560562354932e-17,
    "energy": 2,
    "energy_out": 2,
    "minimum_witness_eigenvalue": 0.25
  },
  "qubit_pi_over_2_defect": 0.7071067811865476,
  "scope": "Conditional unitary F-generator fails at every nonzero duration for the exact n3 witness under source R4 connection. Conservation alone does not identify a physical Hamiltonian; general instruments/connections remain open."
}
```
