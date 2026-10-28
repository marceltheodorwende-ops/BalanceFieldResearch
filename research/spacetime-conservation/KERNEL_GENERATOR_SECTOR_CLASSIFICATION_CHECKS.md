# Runde78 – vollständige lokale Reproduktion

Ursprünglicher Plan 4611a37b79e3b952b7e1a0af16a03555c8ac5881, vor Auswertung korrigiert 458dc5559059fcb3d3c7ec1f8584833a0abd7a6c. Erst danach4 Originalaufrufe in einem frischen PASS, keine fehlgeschlagenen Auswertungen/Korrekturen am ausgeführten Prüfcode. Alter Interpolationsaudit nicht wiederholt. Python/NumPy/SymPy, unverändertes audit.py im bisherigen relativen bfg-review-Forschungspfad; Dokumenttext nicht automatisch durch CI ausgeführt.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,str(Path(__file__).parent/'bfg-review/research/spacetime-conservation'))
import audit
x=s.symbols('x',positive=True);g=-s.log(s.cos(x));d=s.sqrt(g)
assert s.simplify(s.diff(d,x,2)-(2*g-s.sin(x)**2)/(4*s.cos(x)**2*g**s.Rational(3,2)))==0
update=audit.load_update();rows=[];calls=0
def run(label,ys,fs,groups,basis=None):
    global calls
    n=len(ys);basis=np.eye(n) if basis is None else basis
    cj=lambda a:basis@a@basis.conj().T
    y=cj(np.diag(ys));f=cj(np.diag(fs));k=cj(np.ones((n,n)));w=np.eye(n)/n
    o=update(k,f,w,y,np.eye(n));calls+=1;assert o['terminal'] is None
    alpha=float(o['alpha']);beta=1-alpha;t=np.sqrt(beta/alpha)*np.array(ys)
    h=(1+np.outer(t,t))/np.sqrt(np.outer(1+t*t,1+t*t))
    aligned=o['v']@o['k']@o['v'].conj().T
    endpoint=float(np.linalg.norm(aligned-cj(h)))
    assert endpoint<1e-10 and min(np.linalg.eigvalsh(h))>-1e-10
    half=np.sqrt(h);minimum=float(np.linalg.eigvalsh(half)[0])
    row=dict(label=label,sectors=groups,alpha=alpha,endpoint_residual=endpoint,half_power_minimum=minimum)
    if groups==2:
        c=float(h[0,-1]);gamma=-np.log(c);z=np.diag([1,1,-1,-1]);generator=lambda a:gamma/2*(z@a@z-a)
        even=(np.ones((n,n))+z@np.ones((n,n))@z)/2;odd=(np.ones((n,n))-z@np.ones((n,n))@z)/2
        exact=even+np.exp(-gamma)*odd
        residual=float(np.linalg.norm(exact-h));composition=float(np.linalg.norm(half*half-h))
        assert minimum>-1e-10 and max(residual,composition)<1e-10
        row.update(gamma=gamma,generator_endpoint_residual=residual,semigroup_composition_residual=composition,generator_nonzero_norm=float(np.linalg.norm(generator(np.ones((n,n))))))
    elif groups==3:
        angles=np.arctan(t);dist=lambda z:np.sqrt(-np.log(np.cos(z)))
        gap=float(dist(angles[2]-angles[0])-dist(angles[1]-angles[0])-dist(angles[2]-angles[1]))
        assert minimum < -1e-7 and gap>0
        row.update(distance_triangle_violation=gap)
    else:assert np.linalg.norm(h-np.ones((n,n)))<1e-10
    rows.append(row)
run('two_spectral_sectors',[.2,.2,.6,.6],[1.,2.,3.,4.],2)
u=audit.complex_unitary(np.random.default_rng(20261126),4)
run('complex_two_sectors',[.2,.2,.6,.6],[1.,2.,3.,4.],2,u)
run('three_distinct_positive_formation',[1/14,1/4,1/2],[.001,.001,1.],3)
run('scalar_geometry',[.3,.3,.3],[1.,1.,1.],1)
result=dict(status='PASS',original_calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=1e-10,seed=20261126,rows=rows,scope='Frozen real Schur-power CP semigroup classification; no physical time, Hamiltonian or general non-Schur embedding exclusion. Existing interpolation audit not rerun.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
```

```json
{
  "status": "PASS",
  "original_calls": 4,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "tolerance": 1e-10,
  "seed": 20261126,
  "rows": [
    {
      "label": "two_spectral_sectors",
      "sectors": 2,
      "alpha": 0.19590643274853803,
      "endpoint_residual": 9.930136612989092e-16,
      "half_power_minimum": -7.242708929594885e-18,
      "gamma": 0.12917812153497618,
      "generator_endpoint_residual": 0.0,
      "semigroup_composition_residual": 0.0,
      "generator_nonzero_norm": 0.3653709028732866
    },
    {
      "label": "complex_two_sectors",
      "sectors": 2,
      "alpha": 0.19590643274853797,
      "endpoint_residual": 3.426580229471826e-15,
      "half_power_minimum": -7.242708929594885e-18,
      "gamma": 0.12917812153497618,
      "generator_endpoint_residual": 0.0,
      "semigroup_composition_residual": 0.0,
      "generator_nonzero_norm": 0.3653709028732866
    },
    {
      "label": "three_distinct_positive_formation",
      "sectors": 3,
      "alpha": 0.19963734957277388,
      "endpoint_residual": 8.455206652451151e-16,
      "half_power_minimum": -0.0010179374228606853,
      "distance_triangle_violation": 0.013364777391610183
    },
    {
      "label": "scalar_geometry",
      "sectors": 1,
      "alpha": 0.0825688073394496,
      "endpoint_residual": 1.3322676295501878e-15,
      "half_power_minimum": -5.624168597199657e-16
    }
  ],
  "scope": "Frozen real Schur-power CP semigroup classification; no physical time, Hamiltonian or general non-Schur embedding exclusion. Existing interpolation audit not rerun."
}
```
