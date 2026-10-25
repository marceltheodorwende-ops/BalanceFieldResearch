# Runde69: gerichtete Quellhistorie – Reproduktion und Rohdaten

Präregistrierung91e872835deb167f073902e676f75c8adeaaa46f; Auswertung25. Oktober2026. Ein frischer lokaler PASS ohne Fehlvorlauf/Korrektur mit acht Originalereignissen. Vorhandene Quellenregeln und allgemeine Beweise/Grenzen SOURCE_TRANSPORT_HISTORY.md.

Python-Block als r69_check.py in der Repositorywurzel speichern und `python r69_check.py` mit bestehenden Audit-Abhängigkeiten, NumPy/SymPy ausführen. Gegenüber dem ausgeführten Scratchskript ist nur der Audit-Importpfad auf die Repositorywurzel angepasst. Pinned Originalblob wird vor Import geprüft, empirisches main nicht ausgeführt. Die gerichtete Historie ist eine explizite Trajektorienaufzeichnung, kein zusätzliches dynamisches Grundgesetz oder verborgenes sechstes Xi-Feld.

Die drei Folgeereignisse sind vorab festgelegt. Terminalität oder Verlassen des Retentionsbereichs würde als PARTIAL erfasst, nicht durch neue Eingaben ersetzt; im ausgeführten Lauf sind alle acht Originalereignisse nichtterminal. Historische Anfangs- und Seedträger werden mit tatsächlichem Quell-T4 transportiert; nicht bloß aus willkürlichen aktuellen Eigenvektoren rekonstruiert. Toleranz1e-10,Wurzelcutoff1e-12, theoretische Nullpaar-Determinanten und Seed-Witnessgewichte können Rundungsreste beider Vorzeichen enthalten.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit

S=s.ones(2)/2;J=s.diag(1,0);H=S*J*S
assert H*H!=H and s.trace((H*H-H).T*(H*H-H))==s.Rational(1,16)
F=s.diag(1,2);SF=s.diag(1,s.sqrt(2));X=SF*(s.ones(2)/2)*SF
assert X.det()==0 and s.trace(X)==s.Rational(3,2)
def root(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2);assert min(e)>-1e-10
    return (u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T
def density(f,w):
    sf=root(f);return sf@w@sf

update=audit.load_update();calls=0
p0=np.diag([1.,1.,0.,0.]);f0=np.diag([1.,2.,0.,0.]);w0=np.zeros((4,4));w0[:2,:2]=.5
k0=-np.diag([1.,2.,3.,4.])
y0=np.array([[.25,.03,.02,.01],[.03,.35,.03,.04],[.02,.03,.45,.03],[.01,.04,.03,.55]])
def trajectory(label,fields,z0):
    global calls
    k,f,w,y,p=[a.copy() for a in fields];initial_f=f.copy();initial_p=p.copy()
    comp=p.copy();ancestor=p.copy();births=[];strengths=[];z=z0.copy();rows=[]
    for step in range(3):
        if np.max(np.linalg.eigvalsh(y))>=1-1e-10:
            rows.append(dict(step=step,status='RETENTION_SCOPE_EXIT'));break
        o=update(k,f,w,y,p);calls+=1
        if o['terminal'] is not None:
            rows.append(dict(step=step,status='TERMINAL',terminal=o['terminal']));break
        assert np.linalg.norm(o['psel']-p)<1e-10
        v=o['t4']@p;iso=float(np.linalg.norm(v.conj().T@v-p));assert iso<1e-10
        comp=v@comp;z=v@z;ancestor=v@ancestor@v.conj().T
        births=[v@b@v.conj().T for b in births]
        seed=o['p']-v@p@v.conj().T;sr=int(round(np.trace(seed).real))
        added=o['f']-v@f@v.conj().T;strength=float(np.trace(added).real)
        assert sr in [0,1]
        if sr:
            assert strength>0 and np.linalg.norm(added-strength*seed)<1e-10
            births.append(seed);strengths.append(strength)
        else:assert np.linalg.norm(added)<1e-10
        components=[ancestor]+births
        orth=max([float(np.linalg.norm(a@b)) for i,a in enumerate(components) for b in components[i+1:]]+[0.])
        pres=float(np.linalg.norm(sum(components)-o['p']))
        fres=float(np.linalg.norm(comp@initial_f@comp.conj().T+sum((a*b for a,b in zip(strengths,births)),np.zeros_like(o['f']))-o['f']))
        qres=float(np.linalg.norm(ancestor-comp@initial_p@comp.conj().T))
        r=density(o['f'],o['w']);xp=z.conj().T@r@z
        pairres=float(np.linalg.norm(xp-np.array([[.5,np.sqrt(2)/2],[np.sqrt(2)/2,1.]])))
        bw=max([abs(np.trace(b@o['w'])) for b in births]+[0.])
        br=max([abs(np.trace(b@r)) for b in births]+[0.])
        assert max(orth,pres,fres,qres,pairres,float(bw),float(br))<1e-10
        assert abs(np.trace(ancestor).real-2)<1e-10 and np.linalg.norm(ancestor@ancestor-ancestor)<1e-10
        row=dict(step=step,status='PASS',active_rank=int(round(np.trace(o['p']).real)),ancestral_rank=2,
                 density_rank=int(sum(np.linalg.eigvalsh(r)>1e-10)),seed_count=len(births),new_seed_rank=sr,
                 seed_strengths=strengths.copy(),seed_witness_weight=float(bw),seed_density_weight=float(br),
                 pair_trace=float(np.trace(xp).real),pair_determinant=float(np.linalg.det(xp).real),
                 formation_stock=float(np.trace(o['f']).real),isometry_residual=iso,
                 orthogonality_residual=orth,carrier_decomposition_residual=pres,
                 formation_decomposition_residual=fres,ancestral_composition_residual=qres,
                 historical_pair_compression_residual=pairres)
        if len(births)==2:
            born=births[0]+births[1]
            assert abs(np.trace(born).real-2)<1e-10 and np.linalg.norm(born@born-born)<1e-10
            row.update(total_birth_carrier_rank=2,birth_formation_stock=float(np.trace(born@o['f']).real))
        rows.append(row);k,f,w,y,p=[o[n] for n in ['k','f','w','y','p']]
    return dict(label=label,rows=rows)

base=trajectory('source_history',[k0,f0,w0,y0,p0],np.eye(4)[:,:2])
rng=np.random.default_rng(20261119);g=audit.complex_unitary(rng,4);cj=lambda a:g@a@g.conj().T
gauge=trajectory('complex_history',[cj(a) for a in [k0,f0,w0,y0,p0]],g@np.eye(4)[:,:2])
complete=all(len(t['rows'])==3 and all(r['status']=='PASS' for r in t['rows']) for t in [base,gauge])
gauge_error=None
if complete:
    assert [r['active_rank'] for r in base['rows']]==[3,4,4]
    assert [r['seed_count'] for r in base['rows']]==[1,2,2]
    gauge_error=max(abs(a[key]-b[key]) for a,b in zip(base['rows'],gauge['rows']) for key in ['pair_trace','pair_determinant','formation_stock'])
    assert gauge_error<1e-10
massrows=[];outs=[]
for mass in [.25,.75]:
    o=update(-np.eye(2),np.eye(2),np.diag([mass,1-mass]),np.diag([.5,2.]),np.eye(2));calls+=1
    assert o['terminal'] is None and abs(o['msel']-mass)<1e-10
    outs.append(o);massrows.append(dict(initial_mass=1.,selection_mass=float(o['msel']),historical_mass=mass,witness_trace=float(np.trace(o['w']).real)))
same=float(max(np.linalg.norm(outs[0][key]-outs[1][key]) for key in ['k','f','w','y','p']));assert same<1e-10
result=dict(status='PASS' if complete else 'PARTIAL',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,
            seed=20261119,tolerance=1e-10,sqrt_cutoff=1e-12,exact_null_pair_trace='3/2',
            exact_null_pair_determinant='0',exact_partial_transport_projector_defect_squared='1/16',
            histories=[base,gauge],history_gauge_invariant_residual=gauge_error,
            historical_mass_examples=massrows,same_normalized_successor_residual=same,
            scope='Source transport history carries the given ancestral P0 and canonical seed lineages. Rank2 history carriers exist conditionally; no universal physical pair selection or spontaneous copy-symmetry breaking is added.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Vollständige lokale Ausgabe

```json
{
  "status": "PASS",
  "calls": 8,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261119,
  "tolerance": 1e-10,
  "sqrt_cutoff": 1e-12,
  "exact_null_pair_trace": "3/2",
  "exact_null_pair_determinant": "0",
  "exact_partial_transport_projector_defect_squared": "1/16",
  "histories": [
    {
      "label": "source_history",
      "rows": [
        {
          "step": 0,
          "status": "PASS",
          "active_rank": 3,
          "ancestral_rank": 2,
          "density_rank": 1,
          "seed_count": 1,
          "new_seed_rank": 1,
          "seed_strengths": [
            1.9992016499278686
          ],
          "seed_witness_weight": 3.0527754325482176e-17,
          "seed_density_weight": 5.5126644437207786e-17,
          "pair_trace": 1.4999999999999996,
          "pair_determinant": 0.0,
          "formation_stock": 4.999201649927869,
          "isometry_residual": 4.441008767200651e-16,
          "orthogonality_residual": 2.256211463751002e-16,
          "carrier_decomposition_residual": 0.0,
          "formation_decomposition_residual": 4.2785469637951477e-16,
          "ancestral_composition_residual": 0.0,
          "historical_pair_compression_residual": 6.866350197783356e-16
        },
        {
          "step": 1,
          "status": "PASS",
          "active_rank": 4,
          "ancestral_rank": 2,
          "density_rank": 1,
          "seed_count": 2,
          "new_seed_rank": 1,
          "seed_strengths": [
            1.9992016499278686,
            1.573947650791332
          ],
          "seed_witness_weight": 3.3249318224498836e-16,
          "seed_density_weight": 8.467158988306727e-16,
          "pair_trace": 1.5,
          "pair_determinant": -7.850462293418873e-17,
          "formation_stock": 6.573149300719202,
          "isometry_residual": 4.057595016893607e-16,
          "orthogonality_residual": 1.35664055583115e-15,
          "carrier_decomposition_residual": 1.1299417011127559e-16,
          "formation_decomposition_residual": 4.739127581997937e-15,
          "ancestral_composition_residual": 5.578051591462222e-17,
          "historical_pair_compression_residual": 3.1066412952436776e-15,
          "total_birth_carrier_rank": 2,
          "birth_formation_stock": 3.5731493007192014
        },
        {
          "step": 2,
          "status": "PASS",
          "active_rank": 4,
          "ancestral_rank": 2,
          "density_rank": 1,
          "seed_count": 2,
          "new_seed_rank": 0,
          "seed_strengths": [
            1.9992016499278686,
            1.573947650791332
          ],
          "seed_witness_weight": 3.327678403398448e-16,
          "seed_density_weight": 8.468897220778797e-16,
          "pair_trace": 1.4999999999999996,
          "pair_determinant": 1.5700924586837776e-16,
          "formation_stock": 6.573149300719202,
          "isometry_residual": 8.719727356635672e-16,
          "orthogonality_residual": 1.3817915725621857e-15,
          "carrier_decomposition_residual": 1.4913023045161965e-15,
          "formation_decomposition_residual": 5.062221845624173e-15,
          "ancestral_composition_residual": 1.4146097463297683e-16,
          "historical_pair_compression_residual": 3.4488466675883937e-15,
          "total_birth_carrier_rank": 2,
          "birth_formation_stock": 3.5731493007192006
        }
      ]
    },
    {
      "label": "complex_history",
      "rows": [
        {
          "step": 0,
          "status": "PASS",
          "active_rank": 3,
          "ancestral_rank": 2,
          "density_rank": 1,
          "seed_count": 1,
          "new_seed_rank": 1,
          "seed_strengths": [
            1.999201649927867
          ],
          "seed_witness_weight": 3.254591548957103e-16,
          "seed_density_weight": 5.281029376417454e-16,
          "pair_trace": 1.5000000000000022,
          "pair_determinant": 3.140184917367557e-16,
          "formation_stock": 4.999201649927867,
          "isometry_residual": 5.436082006757408e-16,
          "orthogonality_residual": 6.818913625417641e-16,
          "carrier_decomposition_residual": 4.9065389333867974e-18,
          "formation_decomposition_residual": 1.1700282574501315e-15,
          "ancestral_composition_residual": 3.878070153137744e-16,
          "historical_pair_compression_residual": 2.2356594981512175e-15
        },
        {
          "step": 1,
          "status": "PASS",
          "active_rank": 4,
          "ancestral_rank": 2,
          "density_rank": 1,
          "seed_count": 2,
          "new_seed_rank": 1,
          "seed_strengths": [
            1.999201649927867,
            1.5739476507913537
          ],
          "seed_witness_weight": 8.406395988791183e-16,
          "seed_density_weight": 1.5198318151950338e-15,
          "pair_trace": 1.5000000000000029,
          "pair_determinant": 5.577648753618008e-32,
          "formation_stock": 6.573149300719221,
          "isometry_residual": 1.2108843111447025e-15,
          "orthogonality_residual": 1.5808222972456855e-15,
          "carrier_decomposition_residual": 2.388415924255228e-16,
          "formation_decomposition_residual": 1.8719915937658614e-15,
          "ancestral_composition_residual": 5.92922717341484e-16,
          "historical_pair_compression_residual": 3.033368243768708e-15,
          "total_birth_carrier_rank": 2,
          "birth_formation_stock": 3.573149300719218
        },
        {
          "step": 2,
          "status": "PASS",
          "active_rank": 4,
          "ancestral_rank": 2,
          "density_rank": 1,
          "seed_count": 2,
          "new_seed_rank": 0,
          "seed_strengths": [
            1.999201649927867,
            1.5739476507913537
          ],
          "seed_witness_weight": 8.406559875140078e-16,
          "seed_density_weight": 1.5196562620976439e-15,
          "pair_trace": 1.5000000000000022,
          "pair_determinant": -1.5700924586837697e-16,
          "formation_stock": 6.573149300719219,
          "isometry_residual": 1.7189038613245723e-15,
          "orthogonality_residual": 1.595336706485526e-15,
          "carrier_decomposition_residual": 3.2151339437481814e-15,
          "formation_decomposition_residual": 5.1969551966810634e-15,
          "ancestral_composition_residual": 6.464080939641015e-16,
          "historical_pair_compression_residual": 3.036541157591698e-15,
          "total_birth_carrier_rank": 2,
          "birth_formation_stock": 3.5731493007192148
        }
      ]
    }
  ],
  "history_gauge_invariant_residual": 1.865174681370263e-14,
  "historical_mass_examples": [
    {
      "initial_mass": 1.0,
      "selection_mass": 0.25,
      "historical_mass": 0.25,
      "witness_trace": 1.0
    },
    {
      "initial_mass": 1.0,
      "selection_mass": 0.75,
      "historical_mass": 0.75,
      "witness_trace": 1.0
    }
  ],
  "same_normalized_successor_residual": 0.0,
  "scope": "Source transport history carries the given ancestral P0 and canonical seed lineages. Rank2 history carriers exist conditionally; no universal physical pair selection or spontaneous copy-symmetry breaking is added."
}
```

Neue eingebettete Reproduktion ist lokale Evidenz und wird durch die unveränderte GitHub-Pipeline nicht automatisch ausgeführt. Richtungsmarkierungen durch skalare Historie, universelle Anfangspräparation oder physikalische Raum-/Uhr-/Impulsrollen werden nicht ergänzt.
