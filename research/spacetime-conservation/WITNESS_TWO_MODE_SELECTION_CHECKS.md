# Runde64: Auswahl und Spektralrest des Witness-Zweimodenträgers

Präregistrierung846988cb56773f2d1e52bfdb6457acec5be5534e; Auswertung25. Oktober2026. Ein frischer lokaler Lauf PASS, fünf nichtterminale Originalereignisse ohne fehlgeschlagenen numerischen Vorlauf. Die frühere technische Freigabeunterbrechung fand vor Skripterstellung und vor Originalaufrufen statt; siehe WITNESS_TWO_MODE_SELECTION.md. Allgemeine exakte Beweise und Geltungsgrenzen dort getrennt von den numerischen Kontrollen.

Reproduktion: folgenden Python-Block als r64_check.py in der Repositorywurzel speichern und mit `python r64_check.py` ausführen; bestehende Audit-Abhängigkeiten einschließlich NumPy/SymPy werden benötigt. Gegenüber dem ausgeführten Scratchskript ist ausschließlich der Audit-Importpfad auf die Repositorywurzel angepasst. Ausgabe zusätzlich als r64_check.json neben dem Skript. `audit.load_update()` prüft den gepinnten Quell-Blob und importiert nur update; kein empirisches main. Keine Änderung am ursprünglichen Update.

Das Skript verwendet seine Eingaben mit n>=2; bei einem zweidimensionalen Ausgang wird lambda3=0 für die ausgegebene Schnittlücke ergänzt. Im isotropen Fall wird die zufällig von eigh gelieferte Zweierbasis nur zur Normberechnung verwendet, nicht als kanonische Auswahl behauptet. Toleranz1e-10, Wurzelcutoff1e-12; keine Aussage über robuste Rangentscheidungen an beliebig nahen Schwellen.

```python
import sys, json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0, 'research/spacetime-conservation')
import audit

TOL=1e-10
lam=[s.Rational(3,5),s.Rational(39,100),s.Rational(1,100)]
assert sum(lam)==1 and sum(lam[:2])==s.Rational(99,100)
assert lam[1]-lam[2]==s.Rational(19,50)
iso=s.eye(3)/3; qa=s.diag(1,1,0); qb=s.diag(0,1,1)
assert qa!=qb and s.trace(qa*iso)==s.trace(qb*iso)==s.Rational(2,3)
update=audit.load_update(); calls=0

def root(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2)
    assert min(e)>-TOL
    return (u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T

def density(f,w):
    sf=root(f); return sf@w@sf

def summary(r):
    e,u=np.linalg.eigh((r+r.conj().T)/2);e=e[::-1];u=u[:,::-1]
    assert min(e)>-TOL
    q=u[:,:2]@u[:,:2].conj().T
    r2=q@r@q
    return dict(eigenvalues=e.tolist(),rank=int(sum(e>TOL)),energy=float(e.sum()),
                top_two_energy=float(e[:2].sum()),discarded_energy=float(e[2:].sum()),
                top_two_gap=float(e[1]-(e[2] if len(e)>2 else 0)),truncation_frobenius=float(np.linalg.norm(r-r2))),q,r2

def run(label,k,f,w,y,p,retention):
    global calls
    ri=density(f,w); si,qi,r2i=summary(ri)
    o=update(k,f,w,y,p);calls+=1
    assert o['terminal'] is None
    ro=density(o['f'],o['w']); so,qo,r2o=summary(ro)
    row=dict(label=label,before=si,after=so,selection_mass=float(o['msel']),
             active_output_rank=int(round(np.trace(o['p']).real)))
    if retention:
        v=o['t4']@p
        residual=float(np.linalg.norm(ro-v@ri@v.conj().T))
        eigres=float(np.max(np.abs(np.array(si['eigenvalues'])-so['eigenvalues'])))
        assert max(residual,eigres)<TOL
        row.update(density_transport_residual=residual,spectral_residual=eigres)
        if si['top_two_gap']>TOL:
            qres=float(np.linalg.norm(qo-v@qi@v.conj().T))
            rres=float(np.linalg.norm(r2o-v@r2i@v.conj().T))
            assert max(qres,rres)<TOL
            row.update(top_two_projector_residual=qres,truncated_density_transport_residual=rres)
    return o,row

eye=np.eye(3);f=eye.copy();w=np.diag([.6,.39,.01]);y=np.diag([.2,.3,.4]);k=-eye
rows=[]
o,row=run('full_rank_first',k,f,w,y,eye,True);rows.append(row)
_,row=run('full_rank_successor',o['k'],o['f'],o['w'],o['y'],o['p'],True);rows.append(row)
_,row=run('isotropic',k,f,eye/3,y,eye,True);rows.append(row)
assert row['after']['rank']==3 and abs(row['after']['discarded_energy']-1/3)<TOL
sel=eye-np.ones((3,3))/3;fs=np.diag([1.,2.,3.]);ws=fs@fs/14
_,row=run('actual_oblique_selection',k,fs,ws,sel/2+2*(eye-sel),eye,False);rows.append(row)
assert row['before']['rank']==3 and row['after']['rank']==2
assert abs(row['selection_mass']-2/3)<TOL and abs(row['after']['energy']-16/7)<TOL
rng=np.random.default_rng(20261114);g=audit.complex_unitary(rng,3);conj=lambda a:g@a@g.conj().T
_,row=run('full_rank_complex_gauge',conj(k),conj(f),conj(w),conj(y),conj(eye),True);rows.append(row)
gauge=float(np.max(np.abs(np.array(row['after']['eigenvalues'])-rows[0]['after']['eigenvalues'])))
assert gauge<TOL
for row in [rows[0],rows[1],rows[4]]:
    assert row['after']['rank']==3
    assert abs(row['after']['discarded_energy']-.01)<TOL
    assert abs(row['after']['top_two_gap']-.38)<TOL
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261114,
            tolerance=TOL,sqrt_cutoff=1e-12,exact_tail='1/100',exact_top_two_energy='99/100',
            exact_cutoff_gap='19/50',exact_isotropic_tail='1/3',gauge_spectral_residual=gauge,
            cases=rows,scope='Retention preserves density rank and tail. Actual selection can produce rank2; top2 truncation is conditional and not a physical local-space selection law.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Vollständige lokale Ausgabe

```json
{
  "status": "PASS",
  "calls": 5,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261114,
  "tolerance": 1e-10,
  "sqrt_cutoff": 1e-12,
  "exact_tail": "1/100",
  "exact_top_two_energy": "99/100",
  "exact_cutoff_gap": "19/50",
  "exact_isotropic_tail": "1/3",
  "gauge_spectral_residual": 2.220446049250313e-16,
  "cases": [
    {
      "label": "full_rank_first",
      "before": {
        "eigenvalues": [
          0.6,
          0.39,
          0.01
        ],
        "rank": 3,
        "energy": 1.0,
        "top_two_energy": 0.99,
        "discarded_energy": 0.01,
        "top_two_gap": 0.38,
        "truncation_frobenius": 0.01
      },
      "after": {
        "eigenvalues": [
          0.6,
          0.39,
          0.01
        ],
        "rank": 3,
        "energy": 1.0,
        "top_two_energy": 0.99,
        "discarded_energy": 0.01,
        "top_two_gap": 0.38,
        "truncation_frobenius": 0.01
      },
      "selection_mass": 1.0,
      "active_output_rank": 3,
      "density_transport_residual": 0.0,
      "spectral_residual": 0.0,
      "top_two_projector_residual": 0.0,
      "truncated_density_transport_residual": 0.0
    },
    {
      "label": "full_rank_successor",
      "before": {
        "eigenvalues": [
          0.6,
          0.39,
          0.01
        ],
        "rank": 3,
        "energy": 1.0,
        "top_two_energy": 0.99,
        "discarded_energy": 0.01,
        "top_two_gap": 0.38,
        "truncation_frobenius": 0.01
      },
      "after": {
        "eigenvalues": [
          0.6,
          0.39,
          0.01
        ],
        "rank": 3,
        "energy": 1.0,
        "top_two_energy": 0.99,
        "discarded_energy": 0.01,
        "top_two_gap": 0.38,
        "truncation_frobenius": 0.01
      },
      "selection_mass": 1.0,
      "active_output_rank": 3,
      "density_transport_residual": 0.0,
      "spectral_residual": 0.0,
      "top_two_projector_residual": 0.0,
      "truncated_density_transport_residual": 0.0
    },
    {
      "label": "isotropic",
      "before": {
        "eigenvalues": [
          0.3333333333333333,
          0.3333333333333333,
          0.3333333333333333
        ],
        "rank": 3,
        "energy": 1.0,
        "top_two_energy": 0.6666666666666666,
        "discarded_energy": 0.3333333333333333,
        "top_two_gap": 0.0,
        "truncation_frobenius": 0.3333333333333333
      },
      "after": {
        "eigenvalues": [
          0.3333333333333333,
          0.3333333333333333,
          0.3333333333333333
        ],
        "rank": 3,
        "energy": 1.0,
        "top_two_energy": 0.6666666666666666,
        "discarded_energy": 0.3333333333333333,
        "top_two_gap": 0.0,
        "truncation_frobenius": 0.3333333333333333
      },
      "selection_mass": 1.0,
      "active_output_rank": 3,
      "density_transport_residual": 0.0,
      "spectral_residual": 0.0
    },
    {
      "label": "actual_oblique_selection",
      "before": {
        "eigenvalues": [
          1.9285714285714286,
          0.5714285714285715,
          0.07142857142857142
        ],
        "rank": 3,
        "energy": 2.5714285714285716,
        "top_two_energy": 2.5,
        "discarded_energy": 0.07142857142857142,
        "top_two_gap": 0.5000000000000001,
        "truncation_frobenius": 0.07142857142857142
      },
      "after": {
        "eigenvalues": [
          1.9293826980551876,
          0.35633158765909845
        ],
        "rank": 2,
        "energy": 2.285714285714286,
        "top_two_energy": 2.285714285714286,
        "discarded_energy": 0.0,
        "top_two_gap": 0.35633158765909845,
        "truncation_frobenius": 0.0
      },
      "selection_mass": 0.6666666666666667,
      "active_output_rank": 2
    },
    {
      "label": "full_rank_complex_gauge",
      "before": {
        "eigenvalues": [
          0.6000000000000001,
          0.39,
          0.010000000000000122
        ],
        "rank": 3,
        "energy": 1.0000000000000002,
        "top_two_energy": 0.9900000000000001,
        "discarded_energy": 0.010000000000000122,
        "top_two_gap": 0.3799999999999999,
        "truncation_frobenius": 0.01000000000000008
      },
      "after": {
        "eigenvalues": [
          0.6000000000000002,
          0.3900000000000002,
          0.009999999999999976
        ],
        "rank": 3,
        "energy": 1.0000000000000004,
        "top_two_energy": 0.9900000000000004,
        "discarded_energy": 0.009999999999999976,
        "top_two_gap": 0.3800000000000002,
        "truncation_frobenius": 0.009999999999999976
      },
      "selection_mass": 0.9999999999999998,
      "active_output_rank": 3,
      "density_transport_residual": 7.170701389496695e-16,
      "spectral_residual": 1.6653345369377348e-16,
      "top_two_projector_residual": 1.6451147797018265e-15,
      "truncated_density_transport_residual": 7.925444953235957e-16
    }
  ],
  "scope": "Retention preserves density rank and tail. Actual selection can produce rank2; top2 truncation is conditional and not a physical local-space selection law."
}
```

Nur Dokumentationsänderung, kein neuer Remote-CI-Pass. Allgemeine Rang-/Stabilisator-/Spektralrestaussagen sind algebraisch bewiesen; fünf endliche Kontrollen allein wären dafür nicht ausreichend.
