# Runde72: Mess-/Konditionierungstypen – Reproduktion

Präregistrierung413728e291d06db773ab7d9a81a4196c2fb8358e; Auswertung25. Oktober2026. Ein frischer lokaler PASS ohne Fehlvorlauf/Korrektur mit fünf Originalereignissen. Quellenstatus und genaue hypothetische Observable-/Witnessinterpretation in MEASUREMENT_ENERGY_BALANCE_TYPES.md; keine physikalische Energieidentifikation daraus.

Python-Block als r72_check.py in der Repositorywurzel speichern und `python r72_check.py` mit bestehenden Audit-Abhängigkeiten, NumPy/SymPy ausführen. Gegenüber dem ausgeführten Scratchskript ist nur der Audit-Importpfad an die Repositorywurzel angepasst. Pinned Originalblob geprüft, kein empirisches main. Alle tatsächlichen BFG-Q-Selektionen besitzen Masse1; Labelabfragen werden als separate mathematische Readouts mittransportiert und nicht als tatsächliche Quellereignisausgänge ausgegeben.

Symbolische Verfeinerungs-/Mischungsgegenzeugen und Zustandsbrückenvergleich sind vorab spezifiziert. Präparationen A/B/M besitzen identische nicht-W-Felder; der Witnesskanal dieses festen Ereignisses ist affin, während die ungewichtete bedingte Summenablesung nicht affin ist. Toleranz1e-10, strikt positive Konditionierungsmassen.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit

F=s.diag(1,1,3,3)
A=s.diag(s.Rational(4,5),s.Rational(1,50),s.Rational(1,10),s.Rational(2,25))
B=s.diag(s.Rational(1,50),s.Rational(2,5),s.Rational(2,25),s.Rational(1,2))
M=(A+B)/2
cover=[s.diag(1,0,1,0),s.diag(0,1,0,1)]
def exact(f,w,cover):
    rows=[]
    for e in cover:
        p=s.trace(e*w);assert p>0
        q=s.trace(e*w*e*f);rows.append((p,q,s.simplify(q/p)))
    return rows,s.simplify(sum(a[1] for a in rows)),s.simplify(sum(a[2] for a in rows))
exactmix=[exact(F,w,cover) for w in [A,B,M]]
weighted=[a[1] for a in exactmix];unweighted=[a[2] for a in exactmix]
assert weighted==[s.Rational(34,25),s.Rational(54,25),s.Rational(44,25)]
assert weighted[2]==(weighted[0]+weighted[1])/2
defect=s.simplify(unweighted[2]-(unweighted[0]+unweighted[1])/2)
assert defect==-s.Rational(56,75)
F2=s.diag(1,3);W2=s.Matrix([[s.Rational(1,2),s.Rational(1,4)],[s.Rational(1,4),s.Rational(1,2)]])
F8=s.kronecker_product(F2,s.eye(4)/4);W8=s.kronecker_product(W2,s.eye(4)/4)
groupsets=[[[0,1,2,3]],[[0,1],[2,3]],[[0],[1],[2],[3]]]
partitions=[]
for groups,expected in zip(groupsets,[s.Rational(1,2),s.Integer(1),s.Integer(2)]):
    cv=[s.kronecker_product(s.eye(2),s.diag(*[int(j in g) for j in range(4)])) for g in groups]
    _,q,u=exact(F8,W8,cv);assert q==s.Rational(1,2) and u==expected
    partitions.append(dict(groups=groups,weighted=str(q),unweighted=str(u)))
sourceW=s.diag(s.Rational(3,4),s.Rational(1,4))
assert s.trace(sourceW*F2)==s.Rational(3,2)
assert s.trace(F2*F2)/s.trace(F2)==s.Rational(5,2)

arr=lambda a:np.array(a.tolist(),complex)
update=audit.load_update();calls=0
def read(f,w,cover):
    rows=[]
    for e in cover:
        p=float(np.trace(e@w).real);q=float(np.trace(e@w@e@f).real)
        assert p>0
        assert np.linalg.norm(e@f-f@e)<1e-10
        rows.append(dict(mass=p,raw=q,conditional=q/p))
    return dict(rows=rows,weighted=sum(a['raw'] for a in rows),unweighted=sum(a['conditional'] for a in rows),
                fixed_observable=float(np.trace(w@f).real))
def run(label,f,w,y,cover):
    global calls
    before=read(f,w,cover);eye=np.eye(len(f));o=update(-eye,f,w,y,eye);calls+=1
    assert o['terminal'] is None and abs(o['msel']-1)<1e-10
    aftercover=[o['t4']@e@o['t4'].conj().T for e in cover]
    after=read(o['f'],o['w'],aftercover)
    res=max(abs(before[key]-after[key]) for key in ['weighted','unweighted','fixed_observable'])
    pres=max(abs(a[key]-b[key]) for a,b in zip(before['rows'],after['rows']) for key in a)
    effect=float(np.linalg.norm(o['t4'].conj().T@o['t4']-eye))
    assert max(res,pres,effect,abs(after['weighted']-after['fixed_observable']))<1e-10
    return o,dict(label=label,before=before,after=after,readout_transport_residual=max(res,pres),
                  actual_source_selection_mass=float(o['msel']),actual_R4_identity_effect_residual=effect)
f=arr(F);y=np.diag([.2,.25,.3,.35]);cv=list(map(arr,cover));rows=[];outs=[]
for label,w in [('prep_A',A),('prep_B',B),('prep_M',M)]:
    o,row=run(label,f,arr(w),y,cv);rows.append(row);outs.append(o)
mixres=float(np.linalg.norm(outs[2]['w']-(outs[0]['w']+outs[1]['w'])/2));assert mixres<1e-10
assert abs(rows[2]['after']['unweighted']-(rows[0]['after']['unweighted']+rows[1]['after']['unweighted'])/2-float(defect))<1e-10
fine=[np.kron(np.eye(2),np.diag([int(j==i) for j in range(4)])) for i in range(4)]
o,row=run('uniform_hierarchy_labels',arr(F8),arr(W8),np.kron(np.diag([.2,.3]),np.eye(4)),fine);rows.append(row)
refine=[]
for groups in groupsets:
    cc=[np.kron(np.eye(2),np.diag([int(j in g) for j in range(4)])) for g in groups]
    oo=[o['t4']@e@o['t4'].conj().T for e in cc];r=read(o['f'],o['w'],oo)
    assert abs(r['weighted']-.5)<1e-10 and abs(r['unweighted']-len(groups)/2)<1e-10
    refine.append(dict(groups=groups,readout=r))
rng=np.random.default_rng(20261122);g=audit.complex_unitary(rng,4);cj=lambda a:g@a@g.conj().T
_,row=run('prep_A_complex_gauge',cj(f),cj(arr(A)),cj(y),[cj(e) for e in cv]);rows.append(row)
gauge=max(abs(rows[-1]['after'][key]-rows[0]['after'][key]) for key in ['weighted','unweighted','fixed_observable']);assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261122,tolerance=1e-10,
            exact_weighted_mixture=list(map(str,weighted)),exact_unweighted_mixture=list(map(str,unweighted)),
            exact_unweighted_affinity_defect=str(defect),exact_partitions=partitions,
            exact_source_state_bridges_F_readouts=['3/2','5/2'],source_witness_output_mixture_residual=mixres,
            gauge_readout_residual=gauge,cases=rows,refinement_after_source_update=refine,
            scope='Weighted conditional expectation is the fixed-observable unconditional type under the stated witness interpretation; unweighted conditional sums fail affinity/refinement invariance. Physical state/Hamiltonian/calibration are not selected by these identities.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Vollständige lokale Ausgabe

```json
{
  "status": "PASS",
  "calls": 5,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261122,
  "tolerance": 1e-10,
  "exact_weighted_mixture": [
    "34/25",
    "54/25",
    "44/25"
  ],
  "exact_unweighted_mixture": [
    "172/45",
    "212/45",
    "88/25"
  ],
  "exact_unweighted_affinity_defect": "-56/75",
  "exact_partitions": [
    {
      "groups": [
        [
          0,
          1,
          2,
          3
        ]
      ],
      "weighted": "1/2",
      "unweighted": "1/2"
    },
    {
      "groups": [
        [
          0,
          1
        ],
        [
          2,
          3
        ]
      ],
      "weighted": "1/2",
      "unweighted": "1"
    },
    {
      "groups": [
        [
          0
        ],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ]
      ],
      "weighted": "1/2",
      "unweighted": "2"
    }
  ],
  "exact_source_state_bridges_F_readouts": [
    "3/2",
    "5/2"
  ],
  "source_witness_output_mixture_residual": 6.206335383118183e-17,
  "gauge_readout_residual": 3.1086244689504383e-15,
  "cases": [
    {
      "label": "prep_A",
      "before": {
        "rows": [
          {
            "mass": 0.9,
            "raw": 1.1,
            "conditional": 1.2222222222222223
          },
          {
            "mass": 0.1,
            "raw": 0.26,
            "conditional": 2.6
          }
        ],
        "weighted": 1.36,
        "unweighted": 3.8222222222222224,
        "fixed_observable": 1.36
      },
      "after": {
        "rows": [
          {
            "mass": 0.9,
            "raw": 1.1,
            "conditional": 1.2222222222222223
          },
          {
            "mass": 0.1,
            "raw": 0.26,
            "conditional": 2.6
          }
        ],
        "weighted": 1.36,
        "unweighted": 3.8222222222222224,
        "fixed_observable": 1.36
      },
      "readout_transport_residual": 0.0,
      "actual_source_selection_mass": 1.0,
      "actual_R4_identity_effect_residual": 0.0
    },
    {
      "label": "prep_B",
      "before": {
        "rows": [
          {
            "mass": 0.1,
            "raw": 0.26,
            "conditional": 2.6
          },
          {
            "mass": 0.9,
            "raw": 1.9,
            "conditional": 2.111111111111111
          }
        ],
        "weighted": 2.16,
        "unweighted": 4.711111111111111,
        "fixed_observable": 2.16
      },
      "after": {
        "rows": [
          {
            "mass": 0.1,
            "raw": 0.26,
            "conditional": 2.6
          },
          {
            "mass": 0.9,
            "raw": 1.9,
            "conditional": 2.111111111111111
          }
        ],
        "weighted": 2.16,
        "unweighted": 4.711111111111111,
        "fixed_observable": 2.16
      },
      "readout_transport_residual": 0.0,
      "actual_source_selection_mass": 1.0,
      "actual_R4_identity_effect_residual": 0.0
    },
    {
      "label": "prep_M",
      "before": {
        "rows": [
          {
            "mass": 0.5,
            "raw": 0.6799999999999999,
            "conditional": 1.3599999999999999
          },
          {
            "mass": 0.5,
            "raw": 1.0799999999999998,
            "conditional": 2.1599999999999997
          }
        ],
        "weighted": 1.7599999999999998,
        "unweighted": 3.5199999999999996,
        "fixed_observable": 1.7599999999999998
      },
      "after": {
        "rows": [
          {
            "mass": 0.5,
            "raw": 0.6799999999999999,
            "conditional": 1.3599999999999999
          },
          {
            "mass": 0.5,
            "raw": 1.0799999999999998,
            "conditional": 2.1599999999999997
          }
        ],
        "weighted": 1.7599999999999998,
        "unweighted": 3.5199999999999996,
        "fixed_observable": 1.7599999999999998
      },
      "readout_transport_residual": 0.0,
      "actual_source_selection_mass": 1.0,
      "actual_R4_identity_effect_residual": 0.0
    },
    {
      "label": "uniform_hierarchy_labels",
      "before": {
        "rows": [
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          },
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          },
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          },
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          }
        ],
        "weighted": 0.5,
        "unweighted": 2.0,
        "fixed_observable": 0.5
      },
      "after": {
        "rows": [
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          },
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          },
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          },
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          }
        ],
        "weighted": 0.5,
        "unweighted": 2.0,
        "fixed_observable": 0.5
      },
      "readout_transport_residual": 0.0,
      "actual_source_selection_mass": 1.0,
      "actual_R4_identity_effect_residual": 0.0
    },
    {
      "label": "prep_A_complex_gauge",
      "before": {
        "rows": [
          {
            "mass": 0.9000000000000001,
            "raw": 1.1000000000000005,
            "conditional": 1.2222222222222225
          },
          {
            "mass": 0.09999999999999996,
            "raw": 0.26,
            "conditional": 2.600000000000001
          }
        ],
        "weighted": 1.3600000000000005,
        "unweighted": 3.8222222222222237,
        "fixed_observable": 1.3600000000000003
      },
      "after": {
        "rows": [
          {
            "mass": 0.9000000000000001,
            "raw": 1.1,
            "conditional": 1.222222222222222
          },
          {
            "mass": 0.09999999999999987,
            "raw": 0.2599999999999994,
            "conditional": 2.5999999999999974
          }
        ],
        "weighted": 1.3599999999999994,
        "unweighted": 3.8222222222222193,
        "fixed_observable": 1.3599999999999997
      },
      "readout_transport_residual": 4.440892098500626e-15,
      "actual_source_selection_mass": 1.0,
      "actual_R4_identity_effect_residual": 1.0042237061366075e-15
    }
  ],
  "refinement_after_source_update": [
    {
      "groups": [
        [
          0,
          1,
          2,
          3
        ]
      ],
      "readout": {
        "rows": [
          {
            "mass": 1.0,
            "raw": 0.5,
            "conditional": 0.5
          }
        ],
        "weighted": 0.5,
        "unweighted": 0.5,
        "fixed_observable": 0.5
      }
    },
    {
      "groups": [
        [
          0,
          1
        ],
        [
          2,
          3
        ]
      ],
      "readout": {
        "rows": [
          {
            "mass": 0.5,
            "raw": 0.25,
            "conditional": 0.5
          },
          {
            "mass": 0.5,
            "raw": 0.25,
            "conditional": 0.5
          }
        ],
        "weighted": 0.5,
        "unweighted": 1.0,
        "fixed_observable": 0.5
      }
    },
    {
      "groups": [
        [
          0
        ],
        [
          1
        ],
        [
          2
        ],
        [
          3
        ]
      ],
      "readout": {
        "rows": [
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          },
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          },
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          },
          {
            "mass": 0.25,
            "raw": 0.125,
            "conditional": 0.5
          }
        ],
        "weighted": 0.5,
        "unweighted": 2.0,
        "fixed_observable": 0.5
      }
    }
  ],
  "scope": "Weighted conditional expectation is the fixed-observable unconditional type under the stated witness interpretation; unweighted conditional sums fail affinity/refinement invariance. Physical state/Hamiltonian/calibration are not selected by these identities."
}
```

Neue eingebettete Kontrolle ist lokale Evidenz und wird nicht automatisch von der unveränderten GitHub-Pipeline ausgeführt. Fixes mathematisches F-Observable, physikalischer Hamiltonian, kalibrierter Apparat und allgemeine Instrumentfamilie bleiben verschiedene Begriffe.
