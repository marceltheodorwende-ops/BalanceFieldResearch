# Runde60: Anfangsselektion des kommutierenden Sektors

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Ein frischer lokaler Lauf PASS, vier Originalereignisse, keine Fehlvorläufe/Korrektur. Exakte rationale Kreuzblock-/Kommutator-/Energieprüfung getrennt von der Gleitkomma-Originalzuordnung. Empirisches main wird nicht ausgeführt; Grenzen und Beweis in COMMUTING_SECTOR_SELECTION.md.

```python
import sys,json
from pathlib import Path
import sympy as s
import numpy as np
sys.path.insert(0,'research/spacetime-conservation')
import audit
I=s.eye(3);F=s.diag(1,2,3);W=F**2/14;S=I-s.ones(3)/3;S0=s.diag(1,1,0)
assert W*F-F*W==s.zeros(3)
def exact(q):
    mass=s.trace(q*W);a=q*W*q/mass;b=q*F*q;c=s.simplify(a*b-b*a)
    identity=q*(F*(I-q)*W-W*(I-q)*F)*q/mass
    assert s.simplify(c-identity)==s.zeros(3)
    return dict(mass=mass,commutator=c,norm_squared=s.simplify(s.trace(c.T*c)),energy=s.simplify(s.trace(q*W*q*F)/mass))
e=exact(S);e0=exact(S0)
assert e['mass']==s.Rational(2,3) and e['norm_squared']>0 and e0['norm_squared']==0
update=audit.load_update();calls=0
arr=lambda a:np.array(a.tolist(),dtype=float)
def run(label,k,f,w,y,p,q):
    global calls
    o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
    mass=float(np.trace(q@w).real);a=q@w@q/mass;b=q@f@q;c=a@b-b@a
    v=o['t4']@q;co=o['w']@o['f']-o['f']@o['w']
    residual=float(np.linalg.norm(co-v@c@v.conj().T));norm=float(np.linalg.norm(co)**2)
    pred_energy=float(np.trace(q@w@q@f).real/mass);energy=float(np.trace(o['w']@o['f']).real)
    assert max(residual,abs(o['msel']-mass),abs(energy-pred_energy))<1e-10
    return o,dict(label=label,input_commutator_squared=float(np.linalg.norm(w@f-f@w)**2),selection_mass=mass,output_commutator_squared=norm,commutator_transport_residual=residual,input_energy=float(np.trace(w@f).real),predicted_conditional_energy=pred_energy,output_energy=energy,output_dimension=len(o['k']),output_Y_eigenvalues=np.linalg.eigvalsh(o['y']).tolist())
f=arr(F);w=arr(W);q=arr(S);y=q/2+2*(np.eye(3)-q);k=-np.eye(3)
o,r=run('oblique_selection',k,f,w,y,np.eye(3),q)
assert abs(r['output_commutator_squared']-float(e['norm_squared']))<1e-10
assert np.linalg.norm(o['y']-np.eye(2)*8/45)<1e-10
oo,follow=run('retention_after_selection',o['k'],o['f'],o['w'],o['y'],o['p'],np.eye(2))
assert abs(follow['output_commutator_squared']-r['output_commutator_squared'])<1e-10
_,protected=run('protected_selection',k,f,w,np.diag([.5,.5,2.]),np.eye(3),arr(S0))
assert protected['output_commutator_squared']<1e-20
rng=np.random.default_rng(20261110);g=audit.complex_unitary(rng,3);conj=lambda a:g@a@g.conj().T
_,gauged=run('oblique_gauge',conj(k),conj(f),conj(w),conj(y),np.eye(3),conj(q))
gauge=abs(gauged['output_commutator_squared']-r['output_commutator_squared']);assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261110,exact_input_energy=str(s.trace(W*F)),exact_oblique={k:([[str(x) for x in row] for row in v.tolist()] if isinstance(v,s.MatrixBase) else str(v)) for k,v in e.items()},exact_protected={k:([[str(x) for x in row] for row in v.tolist()] if isinstance(v,s.MatrixBase) else str(v)) for k,v in e0.items()},gauge_commutator_squared_residual=gauge,cases=[r,follow,protected,gauged],scope='Commuting formation sector protected by joint retention but not arbitrary initial selection. Oblique source selection creates F-W noncommutation from commuting input; conditional energy not a closed total balance.')

print(json.dumps(result,indent=2))

```

Rohdaten:

```json
{
  "status": "PASS",
  "calls": 4,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261110,
  "exact_input_energy": "18/7",
  "exact_oblique": {
    "mass": "2/3",
    "commutator": [
      [
        "0",
        "1/42",
        "-1/42"
      ],
      [
        "-1/42",
        "0",
        "1/42"
      ],
      [
        "1/42",
        "-1/42",
        "0"
      ]
    ],
    "norm_squared": "1/294",
    "energy": "16/7"
  },
  "exact_protected": {
    "mass": "5/14",
    "commutator": [
      [
        "0",
        "0",
        "0"
      ],
      [
        "0",
        "0",
        "0"
      ],
      [
        "0",
        "0",
        "0"
      ]
    ],
    "norm_squared": "0",
    "energy": "9/5"
  },
  "gauge_commutator_squared_residual": 1.9949319973733282e-17,
  "cases": [
    {
      "label": "oblique_selection",
      "input_commutator_squared": 0,
      "selection_mass": 0.6666666666666667,
      "output_commutator_squared": 0.0034013605442177078,
      "commutator_transport_residual": 3.925718919352214e-17,
      "input_energy": 2.5714285714285716,
      "predicted_conditional_energy": 2.285714285714285,
      "output_energy": 2.285714285714286,
      "output_dimension": 2,
      "output_Y_eigenvalues": [
        0.17777777777777773,
        0.17777777777777778
      ]
    },
    {
      "label": "retention_after_selection",
      "input_commutator_squared": 0.0034013605442177078,
      "selection_mass": 1,
      "output_commutator_squared": 0.0034013605442177078,
      "commutator_transport_residual": 0,
      "input_energy": 2.285714285714286,
      "predicted_conditional_energy": 2.285714285714286,
      "output_energy": 2.285714285714286,
      "output_dimension": 2,
      "output_Y_eigenvalues": [
        0.04417177161353589,
        0.04417177161353589
      ]
    },
    {
      "label": "protected_selection",
      "input_commutator_squared": 0,
      "selection_mass": 0.3571428571428571,
      "output_commutator_squared": 0,
      "commutator_transport_residual": 0,
      "input_energy": 2.5714285714285716,
      "predicted_conditional_energy": 1.8,
      "output_energy": 1.8,
      "output_dimension": 2,
      "output_Y_eigenvalues": [
        0.17777777777777778,
        0.17777777777777778
      ]
    },
    {
      "label": "oblique_gauge",
      "input_commutator_squared": 4.3480877760079954e-32,
      "selection_mass": 0.6666666666666671,
      "output_commutator_squared": 0.003401360544217688,
      "commutator_transport_residual": 4.085582230950352e-16,
      "input_energy": 2.5714285714285725,
      "predicted_conditional_energy": 2.2857142857142874,
      "output_energy": 2.2857142857142874,
      "output_dimension": 2,
      "output_Y_eigenvalues": [
        0.17777777777777773,
        0.17777777777777787
      ]
    }
  ],
  "scope": "Commuting formation sector protected by joint retention but not arbitrary initial selection. Oblique source selection creates F-W noncommutation from commuting input; conditional energy not a closed total balance."
}
```
