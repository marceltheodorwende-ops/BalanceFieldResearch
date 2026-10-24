# Runde53: Reproduktion der Präparations-/Lokalitätsprüfung

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Gepinnte Originaldynamik nur importiert und fünfmal aufgerufen; empirisches main nicht ausgeführt. Ein lokaler Lauf ohne Fehler/Korrektur. Allgemeine Sätze stehen in PREPARATION_LOCALITY.md, diese Stichproben ersetzen deren Beweise nicht.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
I=s.eye(2); X=s.Matrix([[0,1],[1,0]]); E=s.diag(1,0)
wp=(I+X)/2;wm=(I-X)/2;w0=I/2;fd=s.diag(1,3)
roots=[wp,wm,I/s.sqrt(2)]
rw=[s.simplify(s.trace(E*r*fd*r)) for r in roots]
sf=s.diag(1,s.sqrt(3));rf=[s.trace(E*sf*w*sf) for w in [wp,wm,w0]]
assert rw==[1,1,s.Rational(1,2)] and rf==[s.Rational(1,2)]*3
f=2*I+X; a=(s.sqrt(3)+1)/2;b=(s.sqrt(3)-1)/2;sf=a*I+b*X
he=s.simplify(sf*E*sf)
assert s.simplify(sf*sf-f)==s.zeros(2)
assert he[1,1]==1-s.sqrt(3)/2 and he[0,1]==s.Rational(1,2)
energies=[s.trace(w*f) for w in [wp,wm]];assert energies==[3,1]
assert E*wp*E==E*wm*E
update=audit.load_update();rows=[]
def root(m):
    e,u=np.linalg.eigh((m+m.conj().T)/2)
    assert min(e)>-1e-10
    return (u*np.sqrt(np.maximum(e,0)))@u.conj().T
ni=np.eye(2);nx=np.array(X,float);ne=np.diag([1.,0.])
for name,f,states in [('mixture',np.diag([1.,3.]),[(ni+nx)/2,(ni-nx)/2,ni/2]),('coherence',2*ni+nx,[(ni+nx)/2,(ni-nx)/2])]:
    for j,w in enumerate(states):
        o=update(-ni,f,w,np.diag([.2,.3]),ni);assert o['terminal'] is None
        v=o['t4'];eout=v@ne@v.conj().T
        h=root(f)@ne@root(f);hout=root(o['f'])@eout@root(o['f'])
        resid=float(np.linalg.norm(hout-v@h@v.conj().T))
        q=float(np.trace(w@h).real);qo=float(np.trace(o['w']@hout).real)
        qrw=float(np.trace(ne@root(w)@f@root(w)).real)
        assert resid<1e-10 and abs(q-qo)<1e-10
        rows.append(dict(case=name,preparation=j,q_RF=q,q_RW=qrw,energy=float(np.trace(w@f).real),energy_out=float(np.trace(o['w']@o['f']).real),observable_transport_residual=resid,expectation_residual=abs(q-qo)))
result=dict(status='PASS',calls=len(rows),source_blob=audit.EXPECTED_SOURCE_BLOB,symbolic_RW=list(map(str,rw)),symbolic_RF=list(map(str,rf)),symbolic_local_observable=[[str(x) for x in row] for row in he.tolist()],coherence_energies=list(map(str,energies)),cases=rows,scope='Affineness is an additional operational criterion; strict orthogonal-block localization requires block diagonal F. No physical spatial bridge proved.')

print(json.dumps(result,indent=2))

```

Rohresultat:

```json
{
  "status": "PASS",
  "calls": 5,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "symbolic_RW": [
    "1",
    "1",
    "1/2"
  ],
  "symbolic_RF": [
    "1/2",
    "1/2",
    "1/2"
  ],
  "symbolic_local_observable": [
    [
      "sqrt(3)/2 + 1",
      "1/2"
    ],
    [
      "1/2",
      "1 - sqrt(3)/2"
    ]
  ],
  "coherence_energies": [
    "3",
    "1"
  ],
  "cases": [
    {
      "case": "mixture",
      "preparation": 0,
      "q_RF": 0.5,
      "q_RW": 0.9999999999999996,
      "energy": 2,
      "energy_out": 2,
      "observable_transport_residual": 0,
      "expectation_residual": 0
    },
    {
      "case": "mixture",
      "preparation": 1,
      "q_RF": 0.5,
      "q_RW": 0.9999999999999996,
      "energy": 2,
      "energy_out": 2,
      "observable_transport_residual": 0,
      "expectation_residual": 0
    },
    {
      "case": "mixture",
      "preparation": 2,
      "q_RF": 0.5,
      "q_RW": 0.5000000000000001,
      "energy": 2,
      "energy_out": 2,
      "observable_transport_residual": 0,
      "expectation_residual": 0
    },
    {
      "case": "coherence",
      "preparation": 0,
      "q_RF": 1.4999999999999996,
      "q_RW": 1.4999999999999993,
      "energy": 3,
      "energy_out": 3,
      "observable_transport_residual": 0,
      "expectation_residual": 0
    },
    {
      "case": "coherence",
      "preparation": 1,
      "q_RF": 0.49999999999999983,
      "q_RW": 0.4999999999999998,
      "energy": 1,
      "energy_out": 1,
      "observable_transport_residual": 0,
      "expectation_residual": 0
    }
  ],
  "scope": "Affineness is an additional operational criterion; strict orthogonal-block localization requires block diagonal F. No physical spatial bridge proved."
}
```
