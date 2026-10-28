# Prüfungen K-allein-Energieoperatoren

Als Python-Datei im Repository-Wurzelverzeichnis ausführen; bestehende Auditabhängigkeiten. Originalupdate wird nur importiert. Voraussetzungen, Klassifikationsbeweis und Solverkorrektur in K_ONLY_ENERGY_CLASSIFICATION.md.

```python
import json,sys
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit,pair_audit
I=s.eye(2);sx=s.Matrix([[0,1],[1,0]]);sy=s.Matrix([[0,-s.I],[s.I,0]]);sz=s.diag(1,-1);h=31/s.sqrt(1001)
pred=2*I+(1-h)*sx/2+(1+h)*sz/2
a0,ax,ay,az=s.symbols('a0 ax ay az',real=True);hh=a0*I+ax*sx+ay*sy+az*sz
sol_z=s.linsolve(list(hh*sz-sz*hh),(a0,ax,ay,az));assert sol_z==s.FiniteSet((a0,0,0,az))
entry=s.simplify((hh*pred-pred*hh).subs({ax:0,ay:0})[0,1])
assert h**2<1 and s.simplify(entry/(1-h))==az
sol=s.linsolve([ax,ay,s.simplify(entry/(1-h))],(a0,ax,ay,az));assert sol==s.FiniteSet((a0,0,0,0))
assert s.simplify((sz*pred-pred*sz)[0,1])==1-h
update=audit.load_update();ni=np.eye(2);nx=np.array(sx,float);nz=np.array(sz,float)
theta=np.pi/8;u=np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
y=u@np.diag([.2,.3])@u.T;k=2*ni+nz;w=(ni+.5*nx)/2
out=pair_audit.source_aligned(update,k,ni,w,y)
prediction=np.array(pred,float);prediction_res=float(np.linalg.norm(out['k']-prediction));assert prediction_res<1e-12
comm=float(np.linalg.norm(k@out['k']-out['k']@k));assert comm>1e-3
def normalized(x):
    z=x-np.trace(x)*ni/2
    return z/np.sqrt(np.trace(z@z).real/2)
funcs={'K':lambda x:x,'K_squared':lambda x:x@x,'normalized_traceless':normalized,'trace_scalar':lambda x:np.trace(x)*ni}
changes={}
for label,fun in funcs.items():
    before=fun(k);after=fun(out['k']);difference=float(np.linalg.norm(after-before));energy=float(np.trace(out['w']@after).real-np.trace(w@before).real)
    changes[label]=dict(operator_change=difference,witness_energy_change=energy)
    if label=='trace_scalar':assert difference<1e-12
    else:assert difference>1e-3
trans=pair_audit.source_aligned(update,2*ni+nx,ni,w,np.diag([.2,.3]))
radius=float(np.sqrt(np.trace((trans['k']-2*ni)@(trans['k']-2*ni)).real/2));assert abs(radius-float(h))<1e-12
rng=np.random.default_rng(20261101);g=audit.complex_unitary(rng,2);conj=lambda x:g@x@g.conj().T
gout=pair_audit.source_aligned(update,conj(k),conj(ni),conj(w),conj(y))
gauge=max(float(np.linalg.norm(gout[key]-conj(out[key]))) for key in ('k','f','w','y'));assert gauge<1e-12
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=3,seed=20261101,symbolic=dict(h=str(h),common_hermitian_commutant=str(sol),noncommuting_entry='1-31/sqrt(1001)'),prediction_residual=prediction_res,K_output_commutator_norm=comm,illustrative_readouts=changes,transverse_output_radius=radius,gauge_residual=gauge,scope='Continuous U(2)-covariant K-only universally conserved readouts are scalar functions of trace on positive qubit domain; no claim for full-state/history energy maps or open systems.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 3,
  "seed": 20261101,
  "symbolic": {
    "h": "31*sqrt(1001)/1001",
    "common_hermitian_commutant": "{(a0, 0, 0, 0)}",
    "noncommuting_entry": "1-31/sqrt(1001)"
  },
  "prediction_residual": 1.491236750938252e-15,
  "K_output_commutator_norm": 0.028544077943305157,
  "illustrative_readouts": {
    "K": {
      "operator_change": 0.020183711076428672,
      "witness_energy_change": 0.005045927769105951
    },
    "K_squared": {
      "operator_change": 0.08553664408820669,
      "witness_energy_change": 0.00020369109640405725
    },
    "normalized_traceless": {
      "operator_change": 0.014416976806831424,
      "witness_energy_change": 0.005097104816540521
    },
    "trace_scalar": {
      "operator_change": 2.5121479338940403e-15,
      "witness_energy_change": -2.6645352591003757e-15
    }
  },
  "transverse_output_radius": 0.9798162889235715,
  "gauge_residual": 2.9961143025726952e-15,
  "scope": "Continuous U(2)-covariant K-only universally conserved readouts are scalar functions of trace on positive qubit domain; no claim for full-state/history energy maps or open systems."
}
```
