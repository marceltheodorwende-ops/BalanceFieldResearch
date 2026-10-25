# Runde79 – vollständige lokale Reproduktion

Vorabcommit14df7e7b28942b1e3734f48273cc72840e2fd206. Ein frischer PASS,8 Originalaufrufe, keine Fehlvorläufe/Korrektur. Python/NumPy/SymPy und unverändertes audit.py im bisherigen relativen bfg-review-Forschungspfad. Dokumenttext wird von bestehender CI nicht automatisch ausgeführt.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,str(Path(__file__).parent/'bfg-review/research/spacetime-conservation'))
import audit
wf=s.diag(s.Rational(2,5),s.Rational(1,10),s.Rational(1,5),s.Rational(3,10));wc=wf.copy();wc[0,2]=wc[2,0]=s.Rational(1,10)
ff=s.diag(1,2,3,4);fc=ff.copy();fc[0,2]=fc[2,0]=s.Rational(1,5)
for a in [wf,wc,ff,fc]:assert all(a[:i,:i].det()>0 for i in range(1,5))
assert s.trace(wf)==s.trace(wc)==1 and wf!=ff/s.trace(ff)
arr=lambda a:np.array(a.tolist(),complex)
update=audit.load_update();calls=0;rows=[]
z0=np.diag([1.,1.,-1.,-1.]);y0=np.diag([.2,.2,.6,.6]);k0=np.ones((4,4))
def run(label,f0,w0,g=None):
    global calls
    g=np.eye(4) if g is None else g;cj=lambda a:g@a@g.conj().T
    k,f,w,y,z=[cj(a) for a in [k0,f0,w0,y0,z0]];h=np.eye(4,dtype=complex);gamma_sum=0.;initial_k=k.copy();initial_z=z.copy();out=[]
    off=lambda a,zz:(a-zz@a@zz)/2
    for step in range(2):
        e1=(np.eye(4)+z)/2;e2=(np.eye(4)-z)/2
        ys=[float(np.trace(e@y).real/2) for e in [e1,e2]]
        o=update(k,f,w,y,np.eye(4));calls+=1;assert o['terminal'] is None and abs(o['msel']-1)<1e-10
        v=o['t4'];alpha=float(o['alpha']);beta=1-alpha
        c=(alpha+beta*ys[0]*ys[1])/np.sqrt((alpha+beta*ys[0]**2)*(alpha+beta*ys[1]**2));assert 0<c<1
        gamma=-np.log(c);gamma_sum+=gamma
        phi=lambda a:a+(c-1)*off(a,z)
        kernel=float(np.linalg.norm(o['k']-v@phi(k)@v.conj().T))
        source=max(np.linalg.norm(o['w']-v@w@v.conj().T),np.linalg.norm(o['f']-v@f@v.conj().T))
        defects={};balances={}
        for name,a in [('W',w),('F',f)]:
            field='w' if name=='W' else 'f'
            defect=float(np.linalg.norm(o[field]-v@phi(a)@v.conj().T));pred=(1-c)*np.linalg.norm(off(a,z))
            assert abs(defect-pred)<1e-10
            delta=float((np.trace(o[field]@o['k'])-np.trace(a@k)).real)
            expected=float(((c-1)*np.trace(off(a,z)@off(k,z))).real)
            assert abs(delta-expected)<1e-10
            defects[name]=defect;balances[name]=dict(delta=delta,prediction=expected)
        h=v@h;history_expected=initial_k+(np.exp(-gamma_sum)-1)*off(initial_k,initial_z)
        history=float(np.linalg.norm(h.conj().T@o['k']@h-history_expected))
        assert max(kernel,source,history)<1e-10
        out.append(dict(step=step+1,c=float(c),gamma=float(gamma),gamma_sum=float(gamma_sum),kernel_endpoint_residual=kernel,source_transport_residual=float(source),history_residual=history,common_channel_defects=defects,kernel_weighted_balances=balances))
        k,f,w,y=[o[n] for n in ['k','f','w','y']];z=v@z@v.conj().T
    rows.append(dict(label=label,events=out))
run('compatible',arr(ff),arr(wf))
run('witness_coherence',arr(ff),arr(wc))
run('formation_coherence',arr(fc),arr(wf))
g=audit.complex_unitary(np.random.default_rng(20261127),4);run('complex_compatible',arr(ff),arr(wf),g)
for row in rows:
    for event in row['events']:
        ds=event['common_channel_defects']
        if row['label'] in ['compatible','complex_compatible']:assert max(ds.values())<1e-10
        elif row['label']=='witness_coherence':assert ds['W']>1e-5 and ds['F']<1e-10
        else:assert ds['F']>1e-5 and ds['W']<1e-10
result=dict(status='PASS',original_calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=1e-10,seed=20261127,distinct_compatible_state_candidates=True,rows=rows,scope='Common internal CP generator on a stable block-diagonal W/F sector, not a uniquely selected physical state, Hamiltonian or calibrated time.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
```

```json
{
  "status": "PASS",
  "original_calls": 8,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "tolerance": 1e-10,
  "seed": 20261127,
  "distinct_compatible_state_candidates": true,
  "rows": [
    {
      "label": "compatible",
      "events": [
        {
          "step": 1,
          "c": 0.8788174152965355,
          "gamma": 0.12917812153497604,
          "gamma_sum": 0.12917812153497604,
          "kernel_endpoint_residual": 5.438959822042073e-16,
          "source_transport_residual": 0.0,
          "history_residual": 5.438959822042073e-16,
          "common_channel_defects": {
            "W": 0.0,
            "F": 0.0
          },
          "kernel_weighted_balances": {
            "W": {
              "delta": 0.0,
              "prediction": -0.0
            },
            "F": {
              "delta": 1.7763568394002505e-15,
              "prediction": -0.0
            }
          }
        },
        {
          "step": 2,
          "c": 0.995974327341904,
          "gamma": 0.0040337974908799664,
          "gamma_sum": 0.133211919025856,
          "kernel_endpoint_residual": 5.438959822042073e-16,
          "source_transport_residual": 0.0,
          "history_residual": 9.42055475210265e-16,
          "common_channel_defects": {
            "W": 0.0,
            "F": 0.0
          },
          "kernel_weighted_balances": {
            "W": {
              "delta": 2.220446049250313e-16,
              "prediction": -0.0
            },
            "F": {
              "delta": 1.7763568394002505e-15,
              "prediction": -0.0
            }
          }
        }
      ]
    },
    {
      "label": "witness_coherence",
      "events": [
        {
          "step": 1,
          "c": 0.8788174152965355,
          "gamma": 0.12917812153497604,
          "gamma_sum": 0.12917812153497604,
          "kernel_endpoint_residual": 5.438959822042073e-16,
          "source_transport_residual": 0.0,
          "history_residual": 5.438959822042073e-16,
          "common_channel_defects": {
            "W": 0.017137805481106588,
            "F": 0.0
          },
          "kernel_weighted_balances": {
            "W": {
              "delta": -0.024236516940693065,
              "prediction": -0.024236516940692912
            },
            "F": {
              "delta": 1.7763568394002505e-15,
              "prediction": -0.0
            }
          }
        },
        {
          "step": 2,
          "c": 0.995974327341904,
          "gamma": 0.0040337974908799664,
          "gamma_sum": 0.133211919025856,
          "kernel_endpoint_residual": 5.438959822042073e-16,
          "source_transport_residual": 0.0,
          "history_residual": 9.42055475210265e-16,
          "common_channel_defects": {
            "W": 0.0005693160870753757,
            "F": 0.0
          },
          "kernel_weighted_balances": {
            "W": {
              "delta": -0.0007075662480433564,
              "prediction": -0.0007075662480435628
            },
            "F": {
              "delta": 1.7763568394002505e-15,
              "prediction": -0.0
            }
          }
        }
      ]
    },
    {
      "label": "formation_coherence",
      "events": [
        {
          "step": 1,
          "c": 0.8788174152965355,
          "gamma": 0.12917812153497604,
          "gamma_sum": 0.12917812153497604,
          "kernel_endpoint_residual": 5.438959822042073e-16,
          "source_transport_residual": 0.0,
          "history_residual": 5.438959822042073e-16,
          "common_channel_defects": {
            "W": 0.0,
            "F": 0.034275610962213175
          },
          "kernel_weighted_balances": {
            "W": {
              "delta": 0.0,
              "prediction": -0.0
            },
            "F": {
              "delta": -0.04847303388138435,
              "prediction": -0.048473033881385824
            }
          }
        },
        {
          "step": 2,
          "c": 0.995974327341904,
          "gamma": 0.0040337974908799664,
          "gamma_sum": 0.133211919025856,
          "kernel_endpoint_residual": 5.438959822042073e-16,
          "source_transport_residual": 0.0,
          "history_residual": 9.42055475210265e-16,
          "common_channel_defects": {
            "W": 0.0,
            "F": 0.0011386321741507514
          },
          "kernel_weighted_balances": {
            "W": {
              "delta": 2.220446049250313e-16,
              "prediction": -0.0
            },
            "F": {
              "delta": -0.0014151324960849365,
              "prediction": -0.0014151324960871255
            }
          }
        }
      ]
    },
    {
      "label": "complex_compatible",
      "events": [
        {
          "step": 1,
          "c": 0.8788174152965355,
          "gamma": 0.12917812153497604,
          "gamma_sum": 0.12917812153497604,
          "kernel_endpoint_residual": 2.276530961992607e-15,
          "source_transport_residual": 2.2473876566261386e-15,
          "history_residual": 4.6687515698192614e-15,
          "common_channel_defects": {
            "W": 3.5177400214896307e-16,
            "F": 2.172006801790718e-15
          },
          "kernel_weighted_balances": {
            "W": {
              "delta": 0.0,
              "prediction": -1.4853317520149206e-17
            },
            "F": {
              "delta": 7.105427357601002e-15,
              "prediction": -1.6660635601312644e-16
            }
          }
        },
        {
          "step": 2,
          "c": 0.995974327341904,
          "gamma": 0.0040337974908799664,
          "gamma_sum": 0.133211919025856,
          "kernel_endpoint_residual": 8.464315638485407e-16,
          "source_transport_residual": 0.0,
          "history_residual": 5.070341132255096e-15,
          "common_channel_defects": {
            "W": 8.313324051541856e-19,
            "F": 8.424610789379428e-18
          },
          "kernel_weighted_balances": {
            "W": {
              "delta": 0.0,
              "prediction": 2.4546345924781505e-19
            },
            "F": {
              "delta": 3.552713678800501e-15,
              "prediction": 2.059625056326426e-18
            }
          }
        }
      ]
    }
  ],
  "scope": "Common internal CP generator on a stable block-diagonal W/F sector, not a uniquely selected physical state, Hamiltonian or calibrated time."
}
```
