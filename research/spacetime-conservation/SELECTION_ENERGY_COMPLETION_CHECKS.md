# Runde61: Vergleichsergänzung der Auswahlenergie

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Ein frischer lokaler Lauf PASS, vier Originalaufrufe nur für die behaltene Quelle, keine Fehlvorläufe/Korrektur. Der komplementäre Zweig ist eine ausdrücklich hypothetische mathematische Vergleichskompression und wird nicht als BFG-Nachfolger ausgeführt oder ausgegeben. Empirisches main wird nicht ausgeführt; Beweis/Grenzen in SELECTION_ENERGY_COMPLETION.md.

```python
import sys,json
from pathlib import Path
import sympy as s
import numpy as np
sys.path.insert(0,'research/spacetime-conservation')
import audit
I=s.eye(3);F=s.diag(1,2,3);W=F**2/14;S=I-s.ones(3)/3;S0=s.diag(1,1,0)
def exact(q,w):
    r=I-q;m=s.trace(q*w);es=s.simplify(s.trace(w*q*F*q)/m);er=s.simplify(s.trace(w*r*F*r)/(1-m))
    total=s.simplify(m*es+(1-m)*er);cross=s.simplify(s.trace(w*(q*F*r+r*F*q)));before=s.trace(w*F)
    assert s.simplify(total-before+cross)==0
    return dict(selected_mass=m,rejected_mass=1-m,selected_energy=es,rejected_energy=er,weighted_energy=total,input_energy=before,cross=cross)
sym=[exact(S,W),exact(S0,W),exact(S,I/3)]
assert sym[0]['cross']==s.Rational(8,21) and sym[0]['weighted_energy']==s.Rational(46,21)
assert sym[1]['cross']==sym[2]['cross']==0
update=audit.load_update();calls=0
arr=lambda a:np.array(a.tolist(),float)
def run(label,f,w,q):
    global calls
    n=len(f);r=np.eye(n)-q;y=q/2+2*r
    o=update(-np.eye(n),f,w,y,np.eye(n));calls+=1;assert o['terminal'] is None
    m=float(np.trace(q@w).real);mr=float(np.trace(r@w).real)
    es=float(np.trace(w@q@f@q).real/m);er=float(np.trace(w@r@f@r).real/mr)
    cross=float(np.trace(w@(q@f@r+r@f@q)).real);before=float(np.trace(w@f).real);total=m*es+mr*er
    source=float(np.trace(o['w']@o['f']).real)
    assert m>0 and mr>0 and max(abs(m+mr-1),abs(total-before+cross),abs(source-es),abs(o['msel']-m))<1e-10
    return dict(label=label,selected_mass=m,rejected_comparison_mass=mr,source_selected_energy=source,comparison_rejected_energy=er,comparison_weighted_energy=total,input_energy=before,cross=cross,balance_residual=abs(total-before+cross),selected_energy_residual=abs(source-es))
rows=[run('oblique',arr(F),arr(W),arr(S)),run('protected',arr(F),arr(W),arr(S0)),run('oblique_mixed',arr(F),np.eye(3)/3,arr(S))]
rng=np.random.default_rng(20261111);g=audit.complex_unitary(rng,3);conj=lambda a:g@a@g.conj().T
rows.append(run('oblique_gauge',conj(arr(F)),conj(arr(W)),conj(arr(S))))
gauge=abs(rows[0]['cross']-rows[-1]['cross']);assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261111,exact_cases=[{k:str(v) for k,v in row.items()} for row in sym],gauge_cross_residual=gauge,cases=rows,scope='Binary LÃ¼ders completion is an explicit mathematical comparison, not a source-specified rejected physical branch. Weighted energies require an interference cross term; universal preservation iff selection commutes with F.')

print(json.dumps(result,indent=2))

```

Rohdaten:

```json
{
  "status": "PASS",
  "calls": 4,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261111,
  "exact_cases": [
    {
      "selected_mass": "2/3",
      "rejected_mass": "1/3",
      "selected_energy": "16/7",
      "rejected_energy": "2",
      "weighted_energy": "46/21",
      "input_energy": "18/7",
      "cross": "8/21"
    },
    {
      "selected_mass": "5/14",
      "rejected_mass": "9/14",
      "selected_energy": "9/5",
      "rejected_energy": "3",
      "weighted_energy": "18/7",
      "input_energy": "18/7",
      "cross": "0"
    },
    {
      "selected_mass": "2/3",
      "rejected_mass": "1/3",
      "selected_energy": "2",
      "rejected_energy": "2",
      "weighted_energy": "2",
      "input_energy": "2",
      "cross": "0"
    }
  ],
  "gauge_cross_residual": 2.220446049250313e-16,
  "cases": [
    {
      "label": "oblique",
      "selected_mass": 0.6666666666666667,
      "rejected_comparison_mass": 0.33333333333333337,
      "source_selected_energy": 2.285714285714286,
      "comparison_rejected_energy": 2,
      "comparison_weighted_energy": 2.1904761904761902,
      "input_energy": 2.5714285714285716,
      "cross": 0.3809523809523811,
      "balance_residual": 2.7755575615628914e-16,
      "selected_energy_residual": 8.881784197001252e-16
    },
    {
      "label": "protected",
      "selected_mass": 0.3571428571428571,
      "rejected_comparison_mass": 0.6428571428571429,
      "source_selected_energy": 1.8,
      "comparison_rejected_energy": 3,
      "comparison_weighted_energy": 2.5714285714285716,
      "input_energy": 2.5714285714285716,
      "cross": 0,
      "balance_residual": 0,
      "selected_energy_residual": 0
    },
    {
      "label": "oblique_mixed",
      "selected_mass": 0.6666666666666666,
      "rejected_comparison_mass": 0.33333333333333337,
      "source_selected_energy": 2.0000000000000004,
      "comparison_rejected_energy": 1.9999999999999998,
      "comparison_weighted_energy": 1.9999999999999996,
      "input_energy": 2,
      "cross": 1.1102230246251565e-16,
      "balance_residual": 3.3306690738754696e-16,
      "selected_energy_residual": 8.881784197001252e-16
    },
    {
      "label": "oblique_gauge",
      "selected_mass": 0.6666666666666666,
      "rejected_comparison_mass": 0.33333333333333337,
      "source_selected_energy": 2.2857142857142856,
      "comparison_rejected_energy": 1.9999999999999993,
      "comparison_weighted_energy": 2.1904761904761902,
      "input_energy": 2.571428571428572,
      "cross": 0.3809523809523813,
      "balance_residual": 4.996003610813204e-16,
      "selected_energy_residual": 0
    }
  ],
  "scope": "Binary Lüders completion is an explicit mathematical comparison, not a source-specified rejected physical branch. Weighted energies require an interference cross term; universal preservation iff selection commutes with F."
}
```
