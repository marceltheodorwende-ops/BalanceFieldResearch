# Runde71: deklarierte räumliche Hierarchie – Reproduktion

Präregistrierungc8a4a90a5d43a1ffa50d6fc997a2f763f4690468; Auswertung25. Oktober2026. Ein frischer lokaler PASS ohne Fehlvorlauf/Korrektur, fünf Originalereignisse. Algebraische Bilanzen, physikalische Grenzen und die ausdrücklich zusätzlichen Label-/Einbettungsdaten in DECLARED_SPATIAL_HIERARCHY.md.

Python-Block als r71_check.py in der Repositorywurzel speichern und `python r71_check.py` mit bestehenden Audit-Abhängigkeiten, NumPy/SymPy ausführen. Gegenüber dem ausgeführten Scratchskript ist nur der Audit-Importpfad auf die Repositorywurzel angepasst. Originalblob vor Import geprüft, kein empirisches main.

Die erste Quellselektion erzeugt die historische Basis; die anschließenden vollständigen Updates laufen auf Dimensionen3,12,48. Die bestehenden unabhängigen Vollpersistenzformeln aus audit.aligned prüfen vollständige zurückausgerichtete Tensor-Nachfolger. Die deklarierte geometrische Koordinatenkontrolle bis64 Labels ist separat und keine Raumzeit-/Uhrsimulation. Bei Eichung werden Zustandsfelder und Labelsektoren gemeinsam transformiert. Bedingte Witnessnormalisierung dient nur dem vorab getrennten mathematischen Readout, nicht einer neuen BFG-Q-Selektion oder einem behaupteten physikalischen Messinstrument.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit

N,E,FS=s.symbols('N E F',positive=True)
assert s.simplify(4*FS/(4*N)-FS/N)==0
assert s.simplify(4*E/(4*N)**2-E/(4*N**2))==0
assert s.simplify((E/N**2)/(1/N)-E/N)==0
assert s.simplify(4*E/(4*N)-E/N)==0
update=audit.load_update();calls=0
def root(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2);assert min(e)>-1e-10
    return (u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T
def rho(f,w):
    a=root(f);return a@w@a
e=np.eye(4);v=(e[:,1]+e[:,2])/np.sqrt(2);u=(e[:,0]+v)/np.sqrt(2)
j=np.outer(e[:,0],e[:,0])+np.outer(v,v);p=j+np.outer(e[:,3],e[:,3])
f=np.outer(e[:,0],e[:,0])+2*np.outer(v,v)+3*np.outer(e[:,3],e[:,3])
w=.6*np.outer(u,u)+.4*np.outer(e[:,3],e[:,3])
prep=update(-np.diag([1.,2.,3.,4.]),f,w,np.diag([.2,.4,.7,2.]),p);calls+=1
assert prep['terminal'] is None and len(prep['f'])==3
base={key:prep[key] for key in ['k','f','w','y','p']}
c=prep['t4']@prep['psel']@prep['t4'].conj().T
E0=float(np.trace(rho(base['f'],base['w'])).real);F0=float(np.trace(base['f']).real)
CF0=float(np.trace(c@base['f']).real)
assert abs(E0-1.5)<1e-10 and abs(F0-5.5)<1e-10 and abs(CF0-3)<1e-10

def cover(count):
    cells=[];pairs=[]
    for a in range(count):
        z=np.zeros((count,count));z[a,a]=1
        cells.append(np.kron(np.eye(3),z));pairs.append(np.kron(c,z))
    return cells,pairs
def readouts(fields,cells,pairs):
    f,w=fields['f'],fields['w'];r=rho(f,w);rows=[]
    for cell,pair in zip(cells,pairs):
        mass=float(np.trace(cell@w).real);assert mass>0
        fw=cell@f@cell;wc=cell@w@cell/mass
        rows.append(dict(formation=float(np.trace(fw).real),pair_formation=float(np.trace(pair@f).real),
                         mass=mass,raw=float(np.trace(cell@r).real),pair_raw=float(np.trace(pair@r).real),
                         conditional=float(np.trace(wc@fw).real),pair_rank=float(np.trace(pair).real)))
    return rows

fields={key:a.copy() for key,a in base.items()};reference={key:a.copy() for key,a in base.items()}
stages=[];stage1_input=None
for level in range(3):
    count=4**level;cells,pairs=cover(count);before=readouts(fields,cells,pairs)
    for row in before:
        expected=dict(formation=F0/count,pair_formation=CF0/count,mass=1/count,
                      raw=E0/count**2,pair_raw=E0/count**2,conditional=E0/count,pair_rank=2)
        assert max(abs(row[key]-value) for key,value in expected.items())<1e-10
    if level==1:stage1_input=({key:a.copy() for key,a in fields.items()},cells,pairs,before)
    o=update(*[fields[key] for key in ['k','f','w','y','p']]);calls+=1;assert o['terminal'] is None
    back={key:o['v']@o[key]@o['v'].conj().T for key in fields}
    ca=[o['t4']@a@o['t4'].conj().T for a in cells];pa=[o['t4']@a@o['t4'].conj().T for a in pairs]
    after=readouts(o,ca,pa)
    readres=max(abs(a[key]-b[key]) for a,b in zip(before,after) for key in a)
    assert readres<1e-10
    aligned=audit.aligned(reference['k'],reference['f'],reference['y'])
    reference.update(k=aligned['k'],y=aligned['y'])
    expected={key:np.kron(reference[key],np.eye(count)/count if key in ['f','w'] else np.eye(count)) for key in fields}
    fullres=max(float(np.linalg.norm(back[key]-expected[key])) for key in fields)
    assert max(fullres,abs(o['alpha']-aligned['alpha']))<1e-10
    stages.append(dict(level=level,label_count=count,dimension=len(fields['f']),local_before=before,local_after=after,
                       total_formation=sum(a['formation'] for a in after),raw_total=sum(a['raw'] for a in after),
                       conditional_total=sum(a['conditional'] for a in after),readout_transport_residual=readres,
                       full_tensor_update_residual=fullres,alpha=float(o['alpha'])))
    fields={key:np.kron(a,np.eye(4)/4 if key in ['f','w'] else np.eye(4)) for key,a in back.items()}

edges=[]
for parent,child in zip(stages,stages[1:]):
    errs=[]
    for i,pr in enumerate(parent['local_after']):
        cs=child['local_before'][4*i:4*i+4]
        vals=dict(formation=sum(a['formation'] for a in cs)-pr['formation'],
                  raw=sum(a['raw'] for a in cs)-pr['raw']/4,
                  conditional=sum(a['conditional'] for a in cs)-pr['conditional'])
        errs.extend(map(abs,vals.values()))
    assert max(errs)<1e-10;edges.append(dict(parent_level=parent['level'],max_balance_residual=max(errs),raw_child_sum_factor=.25))

fields,cells,pairs,before=stage1_input;rng=np.random.default_rng(20261121);g=audit.complex_unitary(rng,12)
cj=lambda a:g@a@g.conj().T;gf={key:cj(a) for key,a in fields.items()}
o=update(*[gf[key] for key in ['k','f','w','y','p']]);calls+=1;assert o['terminal'] is None
gc=[o['t4']@cj(a)@o['t4'].conj().T for a in cells];gp=[o['t4']@cj(a)@o['t4'].conj().T for a in pairs]
ga=readouts(o,gc,gp);gres=max(abs(a[key]-b[key]) for a,b in zip(before,ga) for key in a);assert gres<1e-10

vertices=np.array([[1,1,1],[1,-1,-1],[-1,1,-1],[-1,-1,1]],float)/np.sqrt(3)
points=np.zeros((1,3));geometry=[]
for level in range(4):
    count=len(points);centroid=float(np.linalg.norm(points.mean(axis=0)))
    second=float(np.mean(np.sum(points*points,axis=1)))
    assert count==4**level and centroid<1e-10 and abs(second-(1-4**(-level))/3)<1e-10
    geometry.append(dict(level=level,labels=count,centroid_residual=centroid,second_moment=second,
                         formation_per_label=F0/count,total_formation=F0))
    points=((points[:,None,:]+vertices[None,:,:])/2).reshape(-1,3)
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261121,
            exact_local_formation='F0/N',exact_local_mass='1/N',exact_local_raw='E0/N^2',
            exact_local_conditional='E0/N',raw_child_sum_factor='1/4',tolerance=1e-10,sqrt_cutoff=1e-12,
            preparation=dict(dimension=3,historical_pair_rank=2,formation=F0,ancestor_formation=CF0,energy=E0),
            stages=stages,edge_controls=edges,gauge_readout_residual=gres,declared_geometry=geometry,
            scope='Declared source IFS labels supply a conditional extended spatial hierarchy. Formation and unweighted label-conditioned readouts have node balances; raw witness pairing does not. No autonomous spacetime, physical instrument or four-current derived.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Vollständige lokale Ausgabe

```json
{
  "status": "PASS",
  "calls": 5,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261121,
  "exact_local_formation": "F0/N",
  "exact_local_mass": "1/N",
  "exact_local_raw": "E0/N^2",
  "exact_local_conditional": "E0/N",
  "raw_child_sum_factor": "1/4",
  "tolerance": 1e-10,
  "sqrt_cutoff": 1e-12,
  "preparation": {
    "dimension": 3,
    "historical_pair_rank": 2,
    "formation": 5.499999999999997,
    "ancestor_formation": 3.000000000000001,
    "energy": 1.5
  },
  "stages": [
    {
      "level": 0,
      "label_count": 1,
      "dimension": 3,
      "local_before": [
        {
          "formation": 5.499999999999997,
          "pair_formation": 3.000000000000001,
          "mass": 1.0,
          "raw": 1.5,
          "pair_raw": 1.5000000000000004,
          "conditional": 1.5,
          "pair_rank": 2.0000000000000004
        }
      ],
      "local_after": [
        {
          "formation": 5.499999999999997,
          "pair_formation": 3.000000000000001,
          "mass": 1.0,
          "raw": 1.5,
          "pair_raw": 1.5000000000000004,
          "conditional": 1.5,
          "pair_rank": 2.0000000000000004
        }
      ],
      "total_formation": 5.499999999999997,
      "raw_total": 1.5,
      "conditional_total": 1.5,
      "readout_transport_residual": 0.0,
      "full_tensor_update_residual": 1.1102230246251565e-16,
      "alpha": 0.013942826673411405
    },
    {
      "level": 1,
      "label_count": 4,
      "dimension": 12,
      "local_before": [
        {
          "formation": 1.3749999999999993,
          "pair_formation": 0.7500000000000002,
          "mass": 0.25,
          "raw": 0.09375000000000003,
          "pair_raw": 0.09375000000000006,
          "conditional": 0.375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 1.3749999999999993,
          "pair_formation": 0.7500000000000002,
          "mass": 0.25,
          "raw": 0.09375,
          "pair_raw": 0.09375000000000003,
          "conditional": 0.375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 1.3749999999999993,
          "pair_formation": 0.7500000000000002,
          "mass": 0.25,
          "raw": 0.09375000000000003,
          "pair_raw": 0.09375000000000006,
          "conditional": 0.375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 1.3749999999999993,
          "pair_formation": 0.7500000000000002,
          "mass": 0.25,
          "raw": 0.09375,
          "pair_raw": 0.09375000000000003,
          "conditional": 0.375,
          "pair_rank": 2.0000000000000004
        }
      ],
      "local_after": [
        {
          "formation": 1.3749999999999993,
          "pair_formation": 0.7500000000000002,
          "mass": 0.25000000000000006,
          "raw": 0.09375000000000006,
          "pair_raw": 0.09375000000000007,
          "conditional": 0.375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 1.3749999999999993,
          "pair_formation": 0.7500000000000002,
          "mass": 0.25000000000000006,
          "raw": 0.09375000000000001,
          "pair_raw": 0.09375000000000003,
          "conditional": 0.375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 1.3749999999999993,
          "pair_formation": 0.7500000000000002,
          "mass": 0.25000000000000006,
          "raw": 0.09375000000000006,
          "pair_raw": 0.09375000000000007,
          "conditional": 0.375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 1.3749999999999993,
          "pair_formation": 0.7500000000000002,
          "mass": 0.25000000000000006,
          "raw": 0.09375000000000001,
          "pair_raw": 0.09375000000000003,
          "conditional": 0.375,
          "pair_rank": 2.0000000000000004
        }
      ],
      "total_formation": 5.499999999999997,
      "raw_total": 0.3750000000000001,
      "conditional_total": 1.5,
      "readout_transport_residual": 5.551115123125783e-17,
      "full_tensor_update_residual": 2.6645352591003757e-15,
      "alpha": 0.0005931751859338272
    },
    {
      "level": 2,
      "label_count": 16,
      "dimension": 48,
      "local_before": [
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375000000009,
          "pair_raw": 0.00585937500000001,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375000000005,
          "pair_raw": 0.005859375000000007,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375000000006,
          "pair_raw": 0.005859375000000008,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859374999999993,
          "pair_raw": 0.005859374999999994,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859374999999994,
          "pair_raw": 0.005859374999999996,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375,
          "pair_raw": 0.005859375000000002,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375000000008,
          "pair_raw": 0.0058593750000000095,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375000000002,
          "pair_raw": 0.0058593750000000035,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375,
          "pair_raw": 0.005859375000000002,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859374999999997,
          "pair_raw": 0.005859374999999998,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375000000002,
          "pair_raw": 0.0058593750000000035,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375,
          "pair_raw": 0.005859375000000002,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859374999999997,
          "pair_raw": 0.005859374999999999,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375,
          "pair_raw": 0.005859375000000001,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.005859375000000003,
          "pair_raw": 0.0058593750000000035,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.06250000000000001,
          "raw": 0.0058593750000000035,
          "pair_raw": 0.005859375000000005,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        }
      ],
      "local_after": [
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859375000000008,
          "pair_raw": 0.0058593750000000095,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859375000000005,
          "pair_raw": 0.005859375000000007,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859375000000005,
          "pair_raw": 0.005859375000000007,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859374999999991,
          "pair_raw": 0.005859374999999993,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859374999999992,
          "pair_raw": 0.005859374999999994,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859374999999999,
          "pair_raw": 0.005859375,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859375000000007,
          "pair_raw": 0.005859375000000009,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859375000000001,
          "pair_raw": 0.005859375000000003,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859374999999999,
          "pair_raw": 0.005859375000000002,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859374999999996,
          "pair_raw": 0.005859374999999997,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859375000000002,
          "pair_raw": 0.005859375000000003,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859374999999999,
          "pair_raw": 0.005859375,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859374999999996,
          "pair_raw": 0.005859374999999998,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859374999999998,
          "pair_raw": 0.005859375,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859375000000002,
          "pair_raw": 0.005859375000000003,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        },
        {
          "formation": 0.34374999999999983,
          "pair_formation": 0.18750000000000006,
          "mass": 0.0625,
          "raw": 0.005859375000000003,
          "pair_raw": 0.0058593750000000035,
          "conditional": 0.09375,
          "pair_rank": 2.0000000000000004
        }
      ],
      "total_formation": 5.499999999999997,
      "raw_total": 0.09375,
      "conditional_total": 1.5,
      "readout_transport_residual": 1.3877787807814457e-17,
      "full_tensor_update_residual": 6.217248937900877e-15,
      "alpha": 1.4078728779574573e-06
    }
  ],
  "edge_controls": [
    {
      "parent_level": 0,
      "max_balance_residual": 5.551115123125783e-17,
      "raw_child_sum_factor": 0.25
    },
    {
      "parent_level": 1,
      "max_balance_residual": 1.3877787807814457e-17,
      "raw_child_sum_factor": 0.25
    }
  ],
  "gauge_readout_residual": 1.5543122344752192e-15,
  "declared_geometry": [
    {
      "level": 0,
      "labels": 1,
      "centroid_residual": 0.0,
      "second_moment": 0.0,
      "formation_per_label": 5.499999999999997,
      "total_formation": 5.499999999999997
    },
    {
      "level": 1,
      "labels": 4,
      "centroid_residual": 0.0,
      "second_moment": 0.25000000000000006,
      "formation_per_label": 1.3749999999999993,
      "total_formation": 5.499999999999997
    },
    {
      "level": 2,
      "labels": 16,
      "centroid_residual": 6.938893903907228e-18,
      "second_moment": 0.3125000000000001,
      "formation_per_label": 0.34374999999999983,
      "total_formation": 5.499999999999997
    },
    {
      "level": 3,
      "labels": 64,
      "centroid_residual": 1.5515838457795457e-17,
      "second_moment": 0.3281250000000001,
      "formation_per_label": 0.08593749999999996,
      "total_formation": 5.499999999999997
    }
  ],
  "scope": "Declared source IFS labels supply a conditional extended spatial hierarchy. Formation and unweighted label-conditioned readouts have node balances; raw witness pairing does not. No autonomous spacetime, physical instrument or four-current derived."
}
```

Neue eingebettete Kontrolle ist lokale Evidenz und wird von der unveränderten GitHub-Pipeline nicht automatisch ausgeführt. Toleranz1e-10,Wurzelcutoff1e-12; keine allgemeine Nahschwellen- oder physikalische Identifikationsbehauptung.
