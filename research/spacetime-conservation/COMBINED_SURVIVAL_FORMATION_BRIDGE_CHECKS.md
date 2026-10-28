# Runde77 – vollständige lokale Reproduktion

Vorabcommit c01cb4619e653b64c26ce90b11beb0c22a3e4353. Ein frischer PASS,4 Originalaufrufe, keine Fehlvorläufe/Korrektur. Python/NumPy/SymPy, unverändertes audit.py im bisherigen relativen bfg-review-Forschungspfad. Nur Dokumenttext, keine automatische CI-Ausführung.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,str(Path(__file__).parent/'bfg-review/research/spacetime-conservation'))
import audit
F=s.diag(1,2,3);S=s.eye(3)-s.ones(3)/3;t=s.symbols('t')
assert s.factor((S*F*S).charpoly(t).as_expr())==t*(3*t*t-12*t+11)/3
assert s.solve(3*t*t-12*t+11,t)==[2-s.sqrt(3)/3,2+s.sqrt(3)/3]
update=audit.load_update();rows=[];calls=0
def run(label,k,f,w,y,p,expected=None):
    global calls
    o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
    ey,uy=np.linalg.eigh(y);q=uy[:,ey<1]@uy[:,ey<1].conj().T
    uu,ss,vh=np.linalg.svd(q@p);mask=ss>1e-12*max(1.,ss[0]);tsel=uu[:,mask]@vh[mask]
    v=o['t4']@tsel;support=v.conj().T@v
    ev,z=np.linalg.eigh(o['f']);effects=[];out=[]
    for value in ev:
        if any(abs(value-a['formation_value'])<1e-8 for a in out):continue
        zz=z[:,abs(ev-value)<1e-8];projector=zz@zz.conj().T
        effect=v.conj().T@projector@v;effects.append(effect)
        before=float(np.trace(w@effect).real);after=float(o['msel']*np.trace(o['w']@projector).real)
        assert min(np.linalg.eigvalsh(effect))>-1e-10 and abs(before-after)<1e-10
        out.append(dict(formation_value=float(value),original_mass_weight=before,duality_residual=abs(before-after)))
    res=float(np.linalg.norm(sum(effects)-support));assert res<1e-10
    assert abs(sum(a['original_mass_weight'] for a in out)-o['msel'])<1e-10
    inherited=o['t4']@o['psel']@o['t4'].conj().T;seed=o['p']-inherited
    seedpull=float(np.linalg.norm(v.conj().T@seed@v));assert seedpull<1e-10
    if expected is not None:
        assert np.max(np.abs(np.sort(ev)-expected))<1e-10
        assert max(abs(a['original_mass_weight']-1/3) for a in out)<1e-10
    rows.append(dict(label=label,selection_mass=float(o['msel']),query_sum_residual=res,seed_pullback_residual=seedpull,seed_rank=int(round(np.trace(seed).real)),spectral_queries=out))
f=np.diag([1.,2.,3.]);w=np.eye(3)/3;p=np.eye(3);k=-p;oblique=p-np.ones((3,3))/3
y=.5*oblique+2*(p-oblique)
run('noncommuting_selection',k,f,w,y,p,np.array([2-1/np.sqrt(3),2+1/np.sqrt(3)]))
aligned=np.diag([1.,1.,0.]);run('commuting_selection',k,f,w,.5*aligned+2*(p-aligned),p,np.array([1.,2.]))
g=audit.complex_unitary(np.random.default_rng(20261125),3);cj=lambda a:g@a@g.conj().T
run('complex_noncommuting',cj(k),cj(f),cj(w),cj(y),cj(p),np.array([2-1/np.sqrt(3),2+1/np.sqrt(3)]))
ps=np.diag([1.,1.,0.,0.]);fs=np.diag([1.,2.,0.,0.]);ws=np.zeros((4,4));ws[:2,:2]=.5
ys=np.array([[.25,.03,.02,.01],[.03,.35,.03,.04],[.02,.03,.45,.03],[.01,.04,.03,.55]])
run('actual_seed',-np.diag([1.,2.,3.,4.]),fs,ws,ys,ps)
assert rows[-1]['seed_rank']==1
result=dict(status='PASS',original_calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=1e-10,spectral_cluster=1e-8,exact_compressed_spectrum=['2-1/sqrt(3)','2+1/sqrt(3)'],rows=rows,scope='Source-selected retained CP branch and positive formation queries, not an assumed physical measurement or Hamiltonian. Noncommuting selection prevents a universal classical same-value formation transport.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
```

```json
{
  "status": "PASS",
  "original_calls": 4,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "tolerance": 1e-10,
  "spectral_cluster": 1e-08,
  "exact_compressed_spectrum": [
    "2-1/sqrt(3)",
    "2+1/sqrt(3)"
  ],
  "rows": [
    {
      "label": "noncommuting_selection",
      "selection_mass": 0.6666666666666665,
      "query_sum_residual": 2.0770370905276122e-16,
      "seed_pullback_residual": 2.228719833105708e-16,
      "seed_rank": 0,
      "spectral_queries": [
        {
          "formation_value": 1.4226497308103738,
          "original_mass_weight": 0.3333333333333332,
          "duality_residual": 5.551115123125783e-17
        },
        {
          "formation_value": 2.577350269189626,
          "original_mass_weight": 0.33333333333333337,
          "duality_residual": 5.551115123125783e-17
        }
      ]
    },
    {
      "label": "commuting_selection",
      "selection_mass": 0.6666666666666666,
      "query_sum_residual": 0.0,
      "seed_pullback_residual": 0.0,
      "seed_rank": 0,
      "spectral_queries": [
        {
          "formation_value": 1.0,
          "original_mass_weight": 0.3333333333333333,
          "duality_residual": 0.0
        },
        {
          "formation_value": 2.0,
          "original_mass_weight": 0.3333333333333333,
          "duality_residual": 0.0
        }
      ]
    },
    {
      "label": "complex_noncommuting",
      "selection_mass": 0.6666666666666667,
      "query_sum_residual": 4.574410218352451e-16,
      "seed_pullback_residual": 2.363302104836152e-16,
      "seed_rank": 0,
      "spectral_queries": [
        {
          "formation_value": 1.4226497308103752,
          "original_mass_weight": 0.3333333333333335,
          "duality_residual": 5.551115123125783e-17
        },
        {
          "formation_value": 2.5773502691896266,
          "original_mass_weight": 0.33333333333333337,
          "duality_residual": 0.0
        }
      ]
    },
    {
      "label": "actual_seed",
      "selection_mass": 0.9999999999999998,
      "query_sum_residual": 5.520433871604776e-16,
      "seed_pullback_residual": 2.982854675986194e-16,
      "seed_rank": 1,
      "spectral_queries": [
        {
          "formation_value": -4.9954615097269617e-17,
          "original_mass_weight": -1.430970109580329e-19,
          "duality_residual": 3.4279391250687555e-20
        },
        {
          "formation_value": 0.9999999999999991,
          "original_mass_weight": 0.4999999999999996,
          "duality_residual": 2.220446049250313e-16
        },
        {
          "formation_value": 1.9992016499278698,
          "original_mass_weight": -1.4419321074257444e-19,
          "duality_residual": 3.834670378768577e-19
        },
        {
          "formation_value": 2.0000000000000004,
          "original_mass_weight": 0.5000000000000004,
          "duality_residual": 1.1102230246251565e-16
        }
      ]
    }
  ],
  "scope": "Source-selected retained CP branch and positive formation queries, not an assumed physical measurement or Hamiltonian. Noncommuting selection prevents a universal classical same-value formation transport."
}
```
