# Runde70: quellenbedingte Retention des selektierten historischen Trägers

Präregistrierungf8e5ca4e46507af1749580bc6e564bbb2100011b; Auswertung25. Oktober2026. Ein frischer lokaler PASS mit sieben Originalereignissen ohne Fehlvorlauf/Korrektur. Vorhandener Quell-Gramsatz und neue Historienkombination sind in SOURCE_ENFORCED_HISTORY_RETENTION.md getrennt ausgewiesen.

Python-Block als r70_check.py in der Repositorywurzel speichern und `python r70_check.py` mit bestehenden Audit-Abhängigkeiten, NumPy/SymPy ausführen. Gegenüber dem ausgeführten Scratchskript ist nur der Audit-Importpfad an die Repositorywurzel angepasst. Pinned Originalblob vor Import geprüft, kein empirisches main. Das erste historische Paar ist der tatsächliche geerbte R4-Träger nach Quellselektion; anfänglicher P hat Rang3. Die verwendete Basis dient nur der covarianten Kontrollrechnung und wird nicht als physikalische Pauli-Achse ausgegeben.

Sieben vorab bestimmte Ereignisse, Terminalität würde als PARTIAL dokumentiert. Positivität/Gramobergrenzen, spätere Masse1, historische Originalmasse und Nullpaartransport werden frisch geprüft. Toleranz1e-10,Wurzelcutoff1e-12; keine unendliche numerische Fortsetzung zertifiziert.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit

e1=s.eye(4)[:,0];e4=s.eye(4)[:,3];vv=(s.eye(4)[:,1]+s.eye(4)[:,2])/s.sqrt(2)
J=e1*e1.T+vv*vv.T;P=J+e4*e4.T;F=e1*e1.T+2*vv*vv.T+3*e4*e4.T
Q=s.diag(1,1,1,0);u=(e1+vv)/s.sqrt(2);p=s.symbols('p',positive=True)
W=p*u*u.T+(1-p)*e4*e4.T
assert J*J==J and P*P==P and Q*P==J and J.rank()==2 and P.rank()==3
assert s.simplify(s.trace(J*W))==p
assert s.simplify(s.trace(J*W*J*F)/p)==s.Rational(3,2)
assert s.simplify(s.trace(W*F))==3-s.Rational(3,2)*p

arr=lambda m:np.array(m.tolist(),complex)
f0=arr(F);p0=arr(P);j0=arr(J);z0=arr(s.Matrix.hstack(e1,vv));uf=arr(u)
k0=-np.diag([1.,2.,3.,4.]);y0=np.diag([.2,.4,.7,2.]);e4n=arr(e4)
wf=lambda mass:mass*(uf@uf.conj().T)+(1-mass)*(e4n@e4n.conj().T)
def root(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2);assert min(e)>-1e-10
    return (u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T
def density(f,w):
    a=root(f);return a@w@a
update=audit.load_update();calls=0
def run(label,mass,count,g=None):
    global calls
    cj=(lambda a:g@a@g.conj().T) if g is not None else (lambda a:a.copy())
    k,f,w,y,carrier=[cj(a) for a in [k0,f0,wf(mass),y0,p0]]
    pair=None;frame=cj(j0)@((g@z0) if g is not None else z0);original_mass=1.;rows=[];first=None
    target=np.array([[.5,np.sqrt(2)/2],[np.sqrt(2)/2,1.]])
    for step in range(count):
        yy=np.linalg.eigvalsh(y);eta=float(max(yy[yy<1]));o=update(k,f,w,y,carrier);calls+=1
        if o['terminal'] is not None:
            rows.append(dict(step=step,status='TERMINAL',terminal=o['terminal']));break
        if step==0:
            first=o;tsel=cj(j0);pair=o['t4']@o['psel']@o['t4'].conj().T
            v=o['t4']@tsel;frame=v@frame
            assert np.linalg.norm(o['psel']-cj(j0))<1e-10
            seed=o['p']-pair;assert abs(np.trace(seed).real-1)<1e-10
        else:
            assert np.all(yy<1) and abs(o['msel']-1)<1e-10
            v=o['t4']@carrier;pair=v@pair@v.conj().T;frame=v@frame;seed=np.zeros_like(o['p'])
        original_mass*=float(o['msel']*o['m4'])
        eigen=np.linalg.eigvalsh(o['y']);bound=float(o['alpha']+(1-o['alpha'])*eta**2)
        assert min(eigen)>0 and max(eigen)<=bound+1e-10 and bound<1
        r=density(o['f'],o['w']);x=frame.conj().T@r@frame
        residual=float(np.linalg.norm(x-target));pres=float(np.linalg.norm(pair@pair-pair))
        assert max(residual,pres,abs(np.trace(pair).real-2),abs(original_mass-mass))<1e-10
        assert np.linalg.norm(frame.conj().T@frame-np.eye(2))<1e-10
        if step==0:assert abs(np.trace(seed@o['w']))<1e-10 and abs(np.trace(seed@r))<1e-10
        row=dict(step=step,status='PASS',input_selection_mass=float(o['msel']),historical_original_mass=original_mass,
                 input_selected_eta=eta,gram_upper_bound=bound,min_successor_Y=float(min(eigen)),
                 max_successor_Y=float(max(eigen)),active_rank=int(round(np.trace(o['p']).real)),
                 inherited_pair_rank=2,density_rank=int(sum(np.linalg.eigvalsh(r)>1e-10)),
                 pair_trace=float(np.trace(x).real),pair_determinant=float(np.linalg.det(x).real),
                 pair_compression_residual=residual,pair_projector_residual=pres,
                 formation_stock=float(np.trace(o['f']).real))
        rows.append(row);k,f,w,y,carrier=[o[n] for n in ['k','f','w','y','p']]
    return dict(label=label,rows=rows),first

main,first=run('selection_then_autonomous_retention',.6,3)
alt,other=run('same_successor_other_original_mass',.3,1)
rng=np.random.default_rng(20261120);g=audit.complex_unitary(rng,4)
gauge,_=run('complex_selection_history',.6,3,g)
complete=all(all(x['status']=='PASS' for x in t['rows']) and len(t['rows'])==n for t,n in [(main,3),(alt,1),(gauge,3)])
same=None;gres=None
if complete:
    same=float(max(np.linalg.norm(first[n]-other[n]) for n in ['k','f','w','y','p']));assert same<1e-10
    gres=max(abs(a[n]-b[n]) for a,b in zip(main['rows'],gauge['rows']) for n in ['pair_trace','pair_determinant','formation_stock','max_successor_Y'])
    assert gres<1e-10
result=dict(status='PASS' if complete else 'PARTIAL',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261120,
            exact_selection_rank=2,exact_initial_rank=3,exact_initial_energy='3-3p/2',exact_conditional_energy='3/2',
            exact_pair_determinant='0',same_normalized_successor_residual=same,gauge_invariant_residual=gres,
            tolerance=1e-10,sqrt_cutoff=1e-12,cases=[main,alt,gauge],
            scope='Source Gram bound forces joint retention after the first successful autonomous event. The actually selected rank2 carrier persists historically despite an initial loss and seed; physical interpretation remains open.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Vollständige lokale Ausgabe

```json
{
  "status": "PASS",
  "calls": 7,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261120,
  "exact_selection_rank": 2,
  "exact_initial_rank": 3,
  "exact_initial_energy": "3-3p/2",
  "exact_conditional_energy": "3/2",
  "exact_pair_determinant": "0",
  "same_normalized_successor_residual": 0.0,
  "gauge_invariant_residual": 3.9968028886505635e-15,
  "tolerance": 1e-10,
  "sqrt_cutoff": 1e-12,
  "cases": [
    {
      "label": "selection_then_autonomous_retention",
      "rows": [
        {
          "step": 0,
          "status": "PASS",
          "input_selection_mass": 0.5999999999999999,
          "historical_original_mass": 0.5999999999999998,
          "input_selected_eta": 0.7,
          "gram_upper_bound": 0.5748205994090333,
          "min_successor_Y": 0.003019786720995685,
          "max_successor_Y": 0.1789833591859211,
          "active_rank": 3,
          "inherited_pair_rank": 2,
          "density_rank": 1,
          "pair_trace": 1.5000000000000007,
          "pair_determinant": -7.850462293418873e-17,
          "pair_compression_residual": 7.447602459741819e-16,
          "pair_projector_residual": 5.799951611264341e-16,
          "formation_stock": 5.5
        },
        {
          "step": 1,
          "status": "PASS",
          "input_selection_mass": 1.0000000000000002,
          "historical_original_mass": 0.5999999999999998,
          "input_selected_eta": 0.1789833591859211,
          "gram_upper_bound": 0.0455312104887392,
          "min_successor_Y": 0.013867935759291647,
          "max_successor_Y": 0.03275622503399515,
          "active_rank": 3,
          "inherited_pair_rank": 2,
          "density_rank": 1,
          "pair_trace": 1.5,
          "pair_determinant": -2.3551386880256565e-16,
          "pair_compression_residual": 1.2412670766236366e-16,
          "pair_projector_residual": 6.708153086820535e-16,
          "formation_stock": 5.5
        },
        {
          "step": 2,
          "status": "PASS",
          "input_selection_mass": 1.0000000000000002,
          "historical_original_mass": 0.5999999999999998,
          "input_selected_eta": 0.03275622503399515,
          "gram_upper_bound": 0.0016655090050671198,
          "min_successor_Y": 0.0007640424259901152,
          "max_successor_Y": 0.0015615336318080381,
          "active_rank": 3,
          "inherited_pair_rank": 2,
          "density_rank": 1,
          "pair_trace": 1.5,
          "pair_determinant": -2.3551386880256565e-16,
          "pair_compression_residual": 1.2412670766236366e-16,
          "pair_projector_residual": 6.708153086820535e-16,
          "formation_stock": 5.5
        }
      ]
    },
    {
      "label": "same_successor_other_original_mass",
      "rows": [
        {
          "step": 0,
          "status": "PASS",
          "input_selection_mass": 0.29999999999999993,
          "historical_original_mass": 0.2999999999999999,
          "input_selected_eta": 0.7,
          "gram_upper_bound": 0.5748205994090333,
          "min_successor_Y": 0.003019786720995685,
          "max_successor_Y": 0.1789833591859211,
          "active_rank": 3,
          "inherited_pair_rank": 2,
          "density_rank": 1,
          "pair_trace": 1.5000000000000007,
          "pair_determinant": -7.850462293418873e-17,
          "pair_compression_residual": 7.447602459741819e-16,
          "pair_projector_residual": 5.799951611264341e-16,
          "formation_stock": 5.5
        }
      ]
    },
    {
      "label": "complex_selection_history",
      "rows": [
        {
          "step": 0,
          "status": "PASS",
          "input_selection_mass": 0.6,
          "historical_original_mass": 0.5999999999999998,
          "input_selected_eta": 0.6999999999999998,
          "gram_upper_bound": 0.5748205994090331,
          "min_successor_Y": 0.003019786720995684,
          "max_successor_Y": 0.17898335918592112,
          "active_rank": 3,
          "inherited_pair_rank": 2,
          "density_rank": 1,
          "pair_trace": 1.4999999999999982,
          "pair_determinant": -7.850462293418856e-17,
          "pair_compression_residual": 4.5005133084051296e-15,
          "pair_projector_residual": 7.171514182605759e-16,
          "formation_stock": 5.4999999999999964
        },
        {
          "step": 1,
          "status": "PASS",
          "input_selection_mass": 0.9999999999999999,
          "historical_original_mass": 0.5999999999999996,
          "input_selected_eta": 0.17898335918592112,
          "gram_upper_bound": 0.04553121048873922,
          "min_successor_Y": 0.013867935759291657,
          "max_successor_Y": 0.03275622503399516,
          "active_rank": 3,
          "inherited_pair_rank": 2,
          "density_rank": 1,
          "pair_trace": 1.499999999999996,
          "pair_determinant": -7.850462293418872e-17,
          "pair_compression_residual": 7.354127706689938e-15,
          "pair_projector_residual": 2.4551967619401308e-15,
          "formation_stock": 5.499999999999998
        },
        {
          "step": 2,
          "status": "PASS",
          "input_selection_mass": 0.9999999999999999,
          "historical_original_mass": 0.5999999999999995,
          "input_selected_eta": 0.03275622503399516,
          "gram_upper_bound": 0.001665509005067121,
          "min_successor_Y": 0.0007640424259901154,
          "max_successor_Y": 0.0015615336318080385,
          "active_rank": 3,
          "inherited_pair_rank": 2,
          "density_rank": 1,
          "pair_trace": 1.4999999999999962,
          "pair_determinant": -3.140184917367547e-16,
          "pair_compression_residual": 6.942501191086319e-15,
          "pair_projector_residual": 2.9038083572871997e-15,
          "formation_stock": 5.499999999999998
        }
      ]
    }
  ],
  "scope": "Source Gram bound forces joint retention after the first successful autonomous event. The actually selected rank2 carrier persists historically despite an initial loss and seed; physical interpretation remains open."
}
```

Dokumentierte lokale Evidenz; die unveränderte GitHub-Pipeline führt diese neue eingebettete Reproduktion nicht automatisch aus. Die Quellen-Gramschranke liefert keine Vollzustandskontraktion oder physikalische Zeit.
