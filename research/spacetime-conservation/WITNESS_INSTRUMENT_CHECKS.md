# Runde58: Witness-Instrumentkontrollen

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Ein frischer lokaler Lauf PASS, fünf Originalereignisse, keine Fehlvorläufe/Korrektur. Empirisches main wird nicht ausgeführt. Allgemeiner Rang1-Instrumentsatz und Zusatzannahmen in WITNESS_INSTRUMENT_INFORMATION.md. Numerische Pinchingkontrollen verwenden einfache positive aktive F-Eigenwerte; ein beliebiger entarteter F-Block wäre als ganzer Spektralprojektor zu behandeln, nicht als numerisch gewählte Basisprojektoren.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
F=s.diag(1,3);W=s.Matrix([[s.Rational(1,2),s.Rational(1,4)],[s.Rational(1,4),s.Rational(1,2)]])
D=s.diag(*W.diagonal());delta=W-D
assert s.trace(F*W)==s.trace(F*D)==2 and s.trace(delta.T*delta)==s.Rational(1,8)
update=audit.load_update();calls=0
def run(label,k,f,w,y,p):
    global calls
    o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
    e,z=np.linalg.eigh(p);z=z[:,e>.5];r=z.shape[1];v=o['t4']@p;j=v@z
    iso=float(np.linalg.norm(j.conj().T@j-np.eye(r)))
    vec=j.reshape(-1,order='F');choi=np.outer(vec,vec.conj());ce=np.linalg.eigvalsh(choi)
    spectrum=float(np.linalg.norm(ce-np.array([0.]*(len(ce)-1)+[float(r)])))
    pred=v@w@v.conj().T;source=float(np.linalg.norm(pred-o['w']))
    random=sum((np.sqrt(a)*v)@w@(np.sqrt(a)*v).conj().T for a in [.3,.7])
    random_res=float(np.linalg.norm(random-o['w']))
    probabilities=[float(np.trace((np.sqrt(a)*v)@w@(np.sqrt(a)*v).conj().T).real) for a in [.3,.7]]
    fe,fu=np.linalg.eigh(f);wf=np.zeros_like(w,dtype=complex);fp=[]
    for idx in range(len(fe)):
        if fe[idx]<1e-10:continue
        proj=np.outer(fu[:,idx],fu[:,idx].conj());wf+=proj@w@proj;fp.append(float(np.trace(proj@w).real))
    pinched=v@wf@v.conj().T;disturbance=float(np.linalg.norm(pinched-o['w']))
    ep=float(np.trace(wf@f).real);ew=float(np.trace(w@f).real)
    assert max(iso,spectrum,source,random_res,abs(ep-ew))<1e-10
    return dict(label=label,input_rank=r,output_dimension=len(o['k']),output_rank=int(round(np.trace(o['p']).real)),isometry_residual=iso,choi_rank=int(sum(ce>1e-10)),choi_spectrum_residual=spectrum,source_witness_residual=source,random_instrument_residual=random_res,random_label_probabilities=probabilities,formation_measurement_probabilities=fp,formation_pinching_disturbance=disturbance,energy=ew,pinched_energy=ep)
rows=[];ni=np.eye(2);f=np.diag([1.,3.]);y=np.diag([.2,.3])
for label,w in [('coherent',np.array(W.tolist(),float)),('diagonal_A',np.diag([.75,.25])),('diagonal_B',np.diag([.25,.75]))]:
    rows.append(run(label,-ni,f,w,y,ni))
assert abs(rows[0]['formation_pinching_disturbance']-np.sqrt(1/8))<1e-10
assert max(rows[i]['formation_pinching_disturbance'] for i in [1,2])<1e-10
p=np.diag([1.,1.,0.]);f=np.diag([1.,.42,0.]);w=np.array([[.6,.1j,0],[-.1j,.4,0],[0,0,0]],complex)
y=np.array([[.25,0,.1],[0,.5,.1],[.1,.1,.5]]);k=-np.diag([1.,2.,3.])
rows.append(run('seed',k,f,w,y,p))
rng=np.random.default_rng(20261108);g=audit.complex_unitary(rng,3);conj=lambda a:g@a@g.conj().T
rows.append(run('seed_gauge',conj(k),conj(f),conj(w),conj(y),conj(p)))
gauge=abs(rows[-1]['formation_pinching_disturbance']-rows[-2]['formation_pinching_disturbance']);assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261108,symbolic_pinching_defect_squared='1/8',symbolic_energy_before_after='2',gauge_pinching_residual=gauge,cases=rows,scope='Any CP instrument of the universal unchanged isometric Witness channel has state-independent outcomes at fixed other BFG data. Energy-conserving pinching disturbs coherent W; restricted diagonal preparations remain compatible.')

print(json.dumps(result,indent=2))

```

Rohdaten:

```json
{
  "status": "PASS",
  "calls": 5,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261108,
  "symbolic_pinching_defect_squared": "1/8",
  "symbolic_energy_before_after": "2",
  "gauge_pinching_residual": 1.1102230246251565e-16,
  "cases": [
    {
      "label": "coherent",
      "input_rank": 2,
      "output_dimension": 2,
      "output_rank": 2,
      "isometry_residual": 0,
      "choi_rank": 1,
      "choi_spectrum_residual": 0,
      "source_witness_residual": 0,
      "random_instrument_residual": 0,
      "random_label_probabilities": [
        0.29999999999999993,
        0.7000000000000001
      ],
      "formation_measurement_probabilities": [
        0.5,
        0.5
      ],
      "formation_pinching_disturbance": 0.3535533905932738,
      "energy": 2,
      "pinched_energy": 2
    },
    {
      "label": "diagonal_A",
      "input_rank": 2,
      "output_dimension": 2,
      "output_rank": 2,
      "isometry_residual": 0,
      "choi_rank": 1,
      "choi_spectrum_residual": 0,
      "source_witness_residual": 0,
      "random_instrument_residual": 0,
      "random_label_probabilities": [
        0.29999999999999993,
        0.7000000000000001
      ],
      "formation_measurement_probabilities": [
        0.75,
        0.25
      ],
      "formation_pinching_disturbance": 0,
      "energy": 1.5,
      "pinched_energy": 1.5
    },
    {
      "label": "diagonal_B",
      "input_rank": 2,
      "output_dimension": 2,
      "output_rank": 2,
      "isometry_residual": 0,
      "choi_rank": 1,
      "choi_spectrum_residual": 0,
      "source_witness_residual": 0,
      "random_instrument_residual": 0,
      "random_label_probabilities": [
        0.29999999999999993,
        0.7000000000000001
      ],
      "formation_measurement_probabilities": [
        0.25,
        0.75
      ],
      "formation_pinching_disturbance": 0,
      "energy": 2.5,
      "pinched_energy": 2.5
    },
    {
      "label": "seed",
      "input_rank": 2,
      "output_dimension": 3,
      "output_rank": 3,
      "isometry_residual": 1.1760980339788589e-15,
      "choi_rank": 1,
      "choi_spectrum_residual": 1.4138407905592051e-15,
      "source_witness_residual": 6.023330909306101e-16,
      "random_instrument_residual": 4.997395469570963e-16,
      "random_label_probabilities": [
        0.30000000000000004,
        0.7000000000000003
      ],
      "formation_measurement_probabilities": [
        0.4,
        0.6
      ],
      "formation_pinching_disturbance": 0.1414213562373095,
      "energy": 0.768,
      "pinched_energy": 0.768
    },
    {
      "label": "seed_gauge",
      "input_rank": 2,
      "output_dimension": 3,
      "output_rank": 3,
      "isometry_residual": 9.965469260517931e-16,
      "choi_rank": 1,
      "choi_spectrum_residual": 1.3455658882875059e-15,
      "source_witness_residual": 5.654799424776986e-16,
      "random_instrument_residual": 5.568219589256643e-16,
      "random_label_probabilities": [
        0.3000000000000001,
        0.7000000000000006
      ],
      "formation_measurement_probabilities": [
        0.3999999999999999,
        0.6000000000000009
      ],
      "formation_pinching_disturbance": 0.1414213562373094,
      "energy": 0.7680000000000001,
      "pinched_energy": 0.7680000000000018
    }
  ],
  "scope": "Any CP instrument of the universal unchanged isometric Witness channel has state-independent outcomes at fixed other BFG data. Energy-conserving pinching disturbs coherent W; restricted diagonal preparations remain compatible."
}
```
