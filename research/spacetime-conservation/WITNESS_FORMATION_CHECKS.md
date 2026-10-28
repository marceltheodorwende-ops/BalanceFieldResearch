# Kontrollen der Witness-gewichteten Formation

Als Python-Datei vom Repository-Wurzelverzeichnis ausführen; bestehende Auditabhängigkeiten. Originalupdate wird nur importiert. Gemeinsame F/W-Retention und Anfangskonditionierung werden ausdrücklich unterschieden. Beweis, physikalische Hypothese und Prüfverlauf in WITNESS_FORMATION_ENERGY.md.

```python
import json,sys
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
update=audit.load_update();calls=0
def run(label,k,f,w,y,p):
    global calls
    out=update(k,f,w,y,p);calls+=1
    if out['terminal'] is not None:return dict(label=label,terminal=out['terminal'])
    ev,z=np.linalg.eigh(y);q=z[:,ev<1]@z[:,ev<1].conj().T
    u,sv,vh=np.linalg.svd(q@p);mask=sv>1e-12*max(1.,sv[0]);tsel=u[:,mask]@vh[mask]
    S=tsel.conj().T@tsel;mass=float(np.trace(S@w).real)
    fs=tsel@f@tsel.conj().T;f4=out['t4']@fs@out['t4'].conj().T;seed=out['f']-f4
    ortho=float(np.linalg.norm(out['w']@seed)/max(1.,np.linalg.norm(seed)))
    common_support=bool(np.linalg.norm(S@f@S-f)/max(1.,np.linalg.norm(f))<1e-10 and np.linalg.norm(S@w@S-w)<1e-10)
    moments=[];res=0.
    for power in (1,2,3):
        old=float(np.trace(w@np.linalg.matrix_power(f,power)).real)
        new=float(np.trace(out['w']@np.linalg.matrix_power(out['f'],power)).real)
        pred=float(np.trace(S@w@S@np.linalg.matrix_power(S@f@S,power)).real/mass)
        rr=abs(new-pred)/max(1.,abs(new),abs(pred));res=max(res,rr)
        moments.append(dict(power=power,before=old,after=new,selection_prediction=pred))
        if common_support:assert abs(new-old)/max(1.,abs(new),abs(old))<1e-10
    assert max(res,ortho)<1e-10
    purity=float(np.trace(w@w).real);seedgain=float(np.trace(seed).real)
    altold=float(np.trace(f).real*purity);altnew=float(np.trace(out['f']).real*np.trace(out['w']@out['w']).real)
    if common_support:assert abs(altnew-altold-seedgain*purity)/max(1.,abs(altnew))<1e-10
    return dict(label=label,terminal=None,selection_mass=mass,common_support=common_support,input_dimension=len(k),output_dimension=len(out['k']),input_rank=int(round(np.trace(p).real)),output_rank=int(round(np.trace(out['p']).real)),seed_formation=seedgain,seed_witness_overlap=ortho,moment_residual=res,moments=moments,alternative_MW_energy_before=altold,alternative_MW_energy_after=altnew,formation_density_energy_before=float(np.trace(f@f).real/np.trace(f).real),formation_density_energy_after=float(np.trace(out['f']@out['f']).real/np.trace(out['f']).real))
p=np.diag([1.,1.,0.]);f=np.diag([1.,.42,0.]);y=np.array([[.25,0,.1],[0,.5,.1],[.1,.1,.5]])
rows=[run('rank2_seed',-np.diag([1.,2.,3.]),f,p/2,y,p)]
rows.append(run('initial_rank_loss',-np.eye(2),np.diag([1.,3.]),np.eye(2)/2,np.diag([.5,2.]),np.eye(2)))
assert abs(rows[-1]['moments'][0]['before']-2)<1e-12 and abs(rows[-1]['moments'][0]['after']-1)<1e-12
sx=np.array([[0.,1.],[1.,0.]]);ff=np.diag([1.,3.]);ww=(np.eye(2)+.5*sx)/2
rows.append(run('full_positive',2*np.eye(2)+np.diag([1.,-1.]),ff,ww,np.diag([.2,.3]),np.eye(2)))
assert abs(rows[-1]['moments'][0]['after']-2)<1e-12 and abs(rows[-1]['alternative_MW_energy_after']-2.5)<1e-12
rng=np.random.default_rng(20261102);n=4;z=audit.complex_unitary(rng,n);p=z[:,:2]@z[:,:2].conj().T
f=p@audit.pos(rng,n)@p;w=p/2;z=audit.complex_unitary(rng,n);y=(z*np.array([.15,.3,.5,.7]))@z.conj().T;k=-audit.pos(rng,n)
rows.append(run('complex_seed',k,f,w,y,p))
g=audit.complex_unitary(rng,n);conj=lambda x:g@x@g.conj().T
rows.append(run('complex_gauge',conj(k),conj(f),conj(w),conj(y),conj(p)))
gauge=max(abs(a['after']-b['after'])/max(1.,abs(a['after']),abs(b['after'])) for a,b in zip(rows[-2]['moments'],rows[-1]['moments']))
assert gauge<1e-10
SWF=s.Rational(1,2);mass=s.Rational(1,2);assert SWF/mass==1
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=calls,seed=20261102,gauge_moment_residual=gauge,cases=rows,scope='Witness-weighted formation spectrum is invariant under lossless selection, R4 and orthogonal seed; initial selection conditioning and other quantum/H candidates separated. No physical energy identification asserted.')

print(json.dumps(result,indent=2))

```

Finale frische Ausgabe (fünf Fälle; dokumentierte Vorläufe separat):

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 5,
  "seed": 20261102,
  "gauge_moment_residual": 3.845827966204958e-16,
  "cases": [
    {
      "label": "rank2_seed",
      "terminal": null,
      "selection_mass": 1.0000000000000002,
      "common_support": true,
      "input_dimension": 3,
      "output_dimension": 3,
      "input_rank": 2,
      "output_rank": 3,
      "seed_formation": 1.2568997908165356,
      "seed_witness_overlap": 1.7057136075561954e-16,
      "moment_residual": 5.551115123125783e-16,
      "moments": [
        {
          "power": 1,
          "before": 0.71,
          "after": 0.7100000000000003,
          "selection_prediction": 0.7100000000000003
        },
        {
          "power": 2,
          "before": 0.5882,
          "after": 0.5882000000000004,
          "selection_prediction": 0.5882000000000002
        },
        {
          "power": 3,
          "before": 0.537044,
          "after": 0.5370440000000005,
          "selection_prediction": 0.537044
        }
      ],
      "alternative_MW_energy_before": 0.71,
      "alternative_MW_energy_after": 1.338449895408268,
      "formation_density_energy_before": 0.828450704225352,
      "formation_density_energy_after": 1.0296228097929387
    },
    {
      "label": "initial_rank_loss",
      "terminal": null,
      "selection_mass": 0.5,
      "common_support": false,
      "input_dimension": 2,
      "output_dimension": 1,
      "input_rank": 2,
      "output_rank": 1,
      "seed_formation": 0,
      "seed_witness_overlap": 0,
      "moment_residual": 0,
      "moments": [
        {
          "power": 1,
          "before": 2,
          "after": 1,
          "selection_prediction": 1
        },
        {
          "power": 2,
          "before": 5,
          "after": 1,
          "selection_prediction": 1
        },
        {
          "power": 3,
          "before": 14,
          "after": 1,
          "selection_prediction": 1
        }
      ],
      "alternative_MW_energy_before": 2,
      "alternative_MW_energy_after": 1,
      "formation_density_energy_before": 2.5,
      "formation_density_energy_after": 1
    },
    {
      "label": "full_positive",
      "terminal": null,
      "selection_mass": 1,
      "common_support": true,
      "input_dimension": 2,
      "output_dimension": 2,
      "input_rank": 2,
      "output_rank": 2,
      "seed_formation": 0,
      "seed_witness_overlap": 0,
      "moment_residual": 0,
      "moments": [
        {
          "power": 1,
          "before": 2,
          "after": 2,
          "selection_prediction": 2
        },
        {
          "power": 2,
          "before": 5,
          "after": 5,
          "selection_prediction": 5
        },
        {
          "power": 3,
          "before": 14,
          "after": 14,
          "selection_prediction": 14
        }
      ],
      "alternative_MW_energy_before": 2.5,
      "alternative_MW_energy_after": 2.5,
      "formation_density_energy_before": 2.5,
      "formation_density_energy_after": 2.5
    },
    {
      "label": "complex_seed",
      "terminal": null,
      "selection_mass": 0.9999999999999996,
      "common_support": true,
      "input_dimension": 4,
      "output_dimension": 4,
      "input_rank": 2,
      "output_rank": 3,
      "seed_formation": 13.572867421344021,
      "seed_witness_overlap": 1.3359843290958452e-16,
      "moment_residual": 1.92291398310248e-15,
      "moments": [
        {
          "power": 1,
          "before": 4.941012642844755,
          "after": 4.941012642844755,
          "selection_prediction": 4.94101264284475
        },
        {
          "power": 2,
          "before": 36.218398589610445,
          "after": 36.21839858961044,
          "selection_prediction": 36.21839858961038
        },
        {
          "power": 3,
          "before": 295.61082482272764,
          "after": 295.6108248227274,
          "selection_prediction": 295.61082482272684
        }
      ],
      "alternative_MW_energy_before": 4.941012642844754,
      "alternative_MW_energy_after": 11.727446353516765,
      "formation_density_energy_before": 7.330157036141066,
      "formation_density_energy_after": 10.942686049450018
    },
    {
      "label": "complex_gauge",
      "terminal": null,
      "selection_mass": 1.0000000000000004,
      "common_support": true,
      "input_dimension": 4,
      "output_dimension": 4,
      "input_rank": 2,
      "output_rank": 3,
      "seed_formation": 13.572867421344029,
      "seed_witness_overlap": 8.039081947232602e-17,
      "moment_residual": 2.4997881780332166e-15,
      "moments": [
        {
          "power": 1,
          "before": 4.941012642844755,
          "after": 4.941012642844756,
          "selection_prediction": 4.941012642844759
        },
        {
          "power": 2,
          "before": 36.218398589610445,
          "after": 36.21839858961044,
          "selection_prediction": 36.2183985896105
        },
        {
          "power": 3,
          "before": 295.6108248227276,
          "after": 295.6108248227275,
          "selection_prediction": 295.61082482272826
        }
      ],
      "alternative_MW_energy_before": 4.941012642844754,
      "alternative_MW_energy_after": 11.727446353516768,
      "formation_density_energy_before": 7.330157036141066,
      "formation_density_energy_after": 10.94268604945002
    }
  ],
  "scope": "Witness-weighted formation spectrum is invariant under lossless selection, R4 and orthogonal seed; initial selection conditioning and other quantum/H candidates separated. No physical energy identification asserted."
}
```
