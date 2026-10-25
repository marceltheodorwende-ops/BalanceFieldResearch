# Runde80 – vollständige lokale Reproduktion

Vorabcommit7c64c8b950d0eda022deac130a05e41fefedf89f. Ein frischer PASS,5 Originalaufrufe, keine Fehlvorläufe/Korrektur. Python/NumPy/SymPy und unverändertes audit.py im bisherigen relativen bfg-review-Forschungspfad. Dokumenttext wird nicht automatisch durch bestehende CI ausgeführt.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,str(Path(__file__).parent/'bfg-review/research/spacetime-conservation'))
import audit
v=s.Matrix([s.sqrt(3)/2,s.Rational(1,2)]);P=v*v.T;Y=s.diag(s.Rational(1,4),s.Rational(1,2));G=s.eye(2)+Y;C=G.inv();B=s.eye(2)-C
pg=v*(v.T*G*v).inv()*v.T*G
lc=s.simplify(s.trace(G*pg*C*P*C*pg.T));lb=s.simplify(s.trace(G*pg*B*P*B*pg.T));alpha=s.simplify(lb/(lc+lb))
M=s.simplify(alpha*C*pg.T*pg*C+(1-alpha)*B*pg.T*pg*B)
comm=P*M-M*P;norm2=s.simplify(s.trace(comm.T*comm));assert norm2>0
assert s.simplify((s.Rational(5,4)*s.eye(2)-P/4)*P-P*(s.Rational(5,4)*s.eye(2)-P/4))==s.zeros(2)
arr=lambda a:np.array(a.tolist(),complex)
update=audit.load_update();calls=0;rows=[]
fields=[-np.diag([1.,2.]),arr(P),arr(P),arr(Y),arr(P)]
def run(label,g,steps):
    global calls
    k,f,w,y,p=[g@a@g.conj().T for a in fields];events=[];z=None;initial_off=None
    for step in range(steps):
        o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
        if step==0:
            assert np.linalg.norm(o['p']-np.eye(2))<1e-10
            assert np.linalg.norm(o['f']-(1.25*np.eye(2)-.25*o['w']))<1e-10
            value=float(np.linalg.norm(o['w']@o['y']-o['y']@o['w'])**2)
            assert abs(value-float(norm2))<1e-10
            ey,u=np.linalg.eigh(o['y']);z=u@np.diag([1.,-1.])@u.conj().T
            initial_off=[np.linalg.norm((o[n]-z@o[n]@z)/2) for n in ['w','f']]
            defects=None
        else:
            e1=(np.eye(2)+z)/2;e2=(np.eye(2)-z)/2;ys=[float(np.trace(e@y).real) for e in [e1,e2]]
            a=float(o['alpha']);b=1-a;c=(a+b*ys[0]*ys[1])/np.sqrt((a+b*ys[0]**2)*(a+b*ys[1]**2));assert c<1
            defects={}
            for n,A in [('w',w),('f',f)]:
                phi=A+(c-1)*(A-z@A@z)/2
                defect=float(np.linalg.norm(o[n]-o['t4']@phi@o['t4'].conj().T));assert defect>1e-7
                defects[n]=defect
            z=o['t4']@z@o['t4'].conj().T
        offs=[float(np.linalg.norm((o[n]-z@o[n]@z)/2)) for n in ['w','f']]
        retention=max(abs(a-b) for a,b in zip(offs,initial_off));assert retention<1e-10
        mutual=float(np.linalg.norm(o['w']@o['f']-o['f']@o['w']));assert mutual<1e-10
        gap=float(np.ptp(np.linalg.eigvalsh(o['y'])));assert gap>1e-8
        events.append(dict(step=step+1,formation_witness_commutator=mutual,history_off_norms=offs,off_retention_residual=retention,current_y_gap=gap,common_channel_defects=defects))
        k,f,w,y,p=[o[n] for n in ['k','f','w','y','p']]
    rows.append(dict(label=label,events=events))
run('actual_seed_history',np.eye(2),3)
run('complex_seed_history',audit.complex_unitary(np.random.default_rng(20261128),2),2)
result=dict(status='PASS',original_calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=1e-10,seed=20261128,exact_alpha=str(alpha),exact_seed_output_WY_commutator_norm_squared=str(norm2),rows=rows,scope='Source seed can produce W/F commuting with each other but outside the common two-sector generator class; historical cross-block coherence is retained, not autonomously removed.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
```

```json
{
  "status": "PASS",
  "original_calls": 5,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "tolerance": 1e-10,
  "seed": 20261128,
  "exact_alpha": "25/281",
  "exact_seed_output_WY_commutator_norm_squared": "3276800/5118804747",
  "rows": [
    {
      "label": "actual_seed_history",
      "events": [
        {
          "step": 1,
          "formation_witness_commutator": 6.245004513516506e-17,
          "history_off_norms": [
            0.24450925301648918,
            0.061127313254122365
          ],
          "off_retention_residual": 0.0,
          "current_y_gap": 0.10347737107706542,
          "common_channel_defects": null
        },
        {
          "step": 2,
          "formation_witness_commutator": 6.245004513516506e-17,
          "history_off_norms": [
            0.24450925301648924,
            0.061127313254122385
          ],
          "off_retention_residual": 5.551115123125783e-17,
          "current_y_gap": 0.008359710011466943,
          "common_channel_defects": {
            "w": 0.10232050639641906,
            "f": 0.025580126599104795
          }
        },
        {
          "step": 3,
          "formation_witness_commutator": 6.245004513516506e-17,
          "history_off_norms": [
            0.24450925301648924,
            0.061127313254122385
          ],
          "off_retention_residual": 5.551115123125783e-17,
          "current_y_gap": 0.00014389776959741816,
          "common_channel_defects": {
            "w": 0.027584475261939412,
            "f": 0.0068961188154848625
          }
        }
      ]
    },
    {
      "label": "complex_seed_history",
      "events": [
        {
          "step": 1,
          "formation_witness_commutator": 8.025088416794598e-17,
          "history_off_norms": [
            0.244509253016489,
            0.06112731325412205
          ],
          "off_retention_residual": 0.0,
          "current_y_gap": 0.10347737107706559,
          "common_channel_defects": null
        },
        {
          "step": 2,
          "formation_witness_commutator": 1.8223784084739278e-16,
          "history_off_norms": [
            0.2445092530164891,
            0.06112731325412208
          ],
          "off_retention_residual": 1.1102230246251565e-16,
          "current_y_gap": 0.008359710011466941,
          "common_channel_defects": {
            "w": 0.10232050639641913,
            "f": 0.0255801265991047
          }
        }
      ]
    }
  ],
  "scope": "Source seed can produce W/F commuting with each other but outside the common two-sector generator class; historical cross-block coherence is retained, not autonomously removed."
}
```
