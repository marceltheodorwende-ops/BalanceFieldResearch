# Runde59: stabiler kommutierender F-Sektor

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Ein frischer lokaler Lauf PASS,6 Originalereignisse, keine Fehlvorläufe/Korrektur. Empirisches main wird nicht ausgeführt. Ganze numerisch geclusterte F-Spektralräume statt beliebiger Basislinien; die allgemeine Identität inklusive exakter Entartung/Seedkollision ist in COMMUTING_FORMATION_SECTOR.md bewiesen und nicht von der Clustertoleranz abhängig.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
fs=s.diag(1,3);ws=s.Matrix([[s.Rational(1,2),s.Rational(1,4)],[s.Rational(1,4),s.Rational(1,2)]])
cs=ws*fs-fs*ws;assert s.trace(cs.conjugate().T*cs)==s.Rational(1,2)
update=audit.load_update();calls=0
comm=lambda w,f:w@f-f@w
def projectors(f):
    e,u=np.linalg.eigh((f+f.conj().T)/2);clusters=[]
    for j,x in enumerate(e):
        if not clusters or abs(x-e[clusters[-1][0]])>1e-9:clusters.append([j])
        else:clusters[-1].append(j)
    return [u[:,idx]@u[:,idx].conj().T for idx in clusters]
def run(label,k,f,w,y,p):
    global calls
    rows=[]
    for step in range(2):
        c0=comm(w,f);n0=float(np.linalg.norm(c0)**2)
        pi=projectors(f);pinched=sum(a@w@a for a in pi)
        moments0=np.array([np.trace(w@np.linalg.matrix_power(f,j)).real for j in [1,2,3]])
        o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
        v=o['t4']@p;c1=comm(o['w'],o['f']);n1=float(np.linalg.norm(c1)**2)
        resid=float(np.linalg.norm(c1-v@c0@v.conj().T))
        measured=v@pinched@v.conj().T;dist=float(np.linalg.norm(measured-o['w']))
        moments1=np.array([np.trace(o['w']@np.linalg.matrix_power(o['f'],j)).real for j in [1,2,3]])
        mr=float(np.max(np.abs(moments1-moments0)))
        assert max(resid,abs(n1-n0),mr)<1e-10
        if label=='commuting':assert dist<1e-10 and n1<1e-20
        else:assert dist>.1 and n1>1e-4
        rows.append(dict(event=step+1,input_commutator_squared=n0,output_commutator_squared=n1,commutator_transport_residual=resid,measurement_source_defect=dist,moments_before=moments0.tolist(),moments_after=moments1.tolist(),moment_residual=mr,output_rank=int(round(np.trace(o['p']).real))))
        k,f,w,y,p=[o[x] for x in ['k','f','w','y','p']]
    return rows
p=np.diag([1.,1.,0.]);f=np.diag([1.,.42,0.]);k=-np.diag([1.,2.,3.]);y=np.array([[.25,0,.1],[0,.5,.1],[.1,.1,.5]])
w0=np.diag([.6,.4,0.]);w1=np.array([[.6,.1j,0],[-.1j,.4,0],[0,0,0]],complex)
rows0=run('commuting',k,f,w0,y,p);rows1=run('coherent',k,f,w1,y,p)
rng=np.random.default_rng(20261109);g=audit.complex_unitary(rng,3);conj=lambda a:g@a@g.conj().T
rowsg=run('coherent_gauge',conj(k),conj(f),conj(w1),conj(y),conj(p))
gauge=max(abs(a['output_commutator_squared']-b['output_commutator_squared']) for a,b in zip(rows1,rowsg));assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261109,symbolic_qubit_commutator_squared='1/2',numerical_spectral_cluster_tolerance=1e-9,gauge_commutator_squared_residual=gauge,commuting=rows0,coherent=rows1,gauge=rowsg,scope='Joint-retention commutation sector invariant, commutator norm not dissipated; formation spectral instrument agrees with source on commuting preparations only. No physical sector selection or clock derived.')

print(json.dumps(result,indent=2))

```

Rohdaten:

```json
{
  "status": "PASS",
  "calls": 6,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261109,
  "symbolic_qubit_commutator_squared": "1/2",
  "numerical_spectral_cluster_tolerance": 1e-9,
  "gauge_commutator_squared_residual": 6.938893903907228e-18,
  "commuting": [
    {
      "event": 1,
      "input_commutator_squared": 0,
      "output_commutator_squared": 1.0561318332533505e-31,
      "commutator_transport_residual": 3.249818199920344e-16,
      "measurement_source_defect": 5.939767439154817e-16,
      "moments_before": [
        0.768,
        0.6705599999999999,
        0.6296352
      ],
      "moments_after": [
        0.7680000000000002,
        0.6705600000000004,
        0.6296352000000006
      ],
      "moment_residual": 6.661338147750939e-16,
      "output_rank": 3
    },
    {
      "event": 2,
      "input_commutator_squared": 1.0561318332533505e-31,
      "output_commutator_squared": 9.527334693640607e-32,
      "commutator_transport_residual": 2.3785329957008082e-17,
      "measurement_source_defect": 1.890526499251144e-15,
      "moments_before": [
        0.7680000000000002,
        0.6705600000000004,
        0.6296352000000006
      ],
      "moments_after": [
        0.7680000000000001,
        0.6705600000000002,
        0.6296352000000004
      ],
      "moment_residual": 2.220446049250313e-16,
      "output_rank": 3
    }
  ],
  "coherent": [
    {
      "event": 1,
      "input_commutator_squared": 0.0067280000000000005,
      "output_commutator_squared": 0.006727999999999998,
      "commutator_transport_residual": 3.480620635922988e-16,
      "measurement_source_defect": 0.1414213562373095,
      "moments_before": [
        0.768,
        0.6705599999999999,
        0.6296352
      ],
      "moments_after": [
        0.7680000000000002,
        0.6705600000000004,
        0.6296352000000006
      ],
      "moment_residual": 6.661338147750939e-16,
      "output_rank": 3
    },
    {
      "event": 2,
      "input_commutator_squared": 0.006727999999999998,
      "output_commutator_squared": 0.006727999999999998,
      "commutator_transport_residual": 1.3755069186866033e-16,
      "measurement_source_defect": 0.14142135623730953,
      "moments_before": [
        0.7680000000000002,
        0.6705600000000004,
        0.6296352000000006
      ],
      "moments_after": [
        0.7680000000000001,
        0.6705600000000002,
        0.6296352000000004
      ],
      "moment_residual": 2.220446049250313e-16,
      "output_rank": 3
    }
  ],
  "gauge": [
    {
      "event": 1,
      "input_commutator_squared": 0.006727999999999995,
      "output_commutator_squared": 0.006728000000000005,
      "commutator_transport_residual": 4.1006097466758646e-16,
      "measurement_source_defect": 0.1414213562373097,
      "moments_before": [
        0.7679999999999998,
        0.6705599999999997,
        0.6296351999999996
      ],
      "moments_after": [
        0.7679999999999995,
        0.6705599999999989,
        0.6296351999999984
      ],
      "moment_residual": 1.2212453270876722e-15,
      "output_rank": 3
    },
    {
      "event": 2,
      "input_commutator_squared": 0.006728000000000005,
      "output_commutator_squared": 0.0067280000000000005,
      "commutator_transport_residual": 3.5092527034393185e-16,
      "measurement_source_defect": 0.14142135623730906,
      "moments_before": [
        0.7679999999999995,
        0.6705599999999989,
        0.6296351999999984
      ],
      "moments_after": [
        0.7679999999999991,
        0.6705599999999984,
        0.6296351999999976
      ],
      "moment_residual": 7.771561172376096e-16,
      "output_rank": 3
    }
  ],
  "scope": "Joint-retention commutation sector invariant, commutator norm not dissipated; formation spectral instrument agrees with source on commuting preparations only. No physical sector selection or clock derived."
}
```
