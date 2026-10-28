# Runde62: allgemeine CP-Auswahlkomplemente

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Ein frischer lokaler PASS, drei Originalereignisse nur für die behaltene Quelle; Vergleichs-Failureinstrumente und kohärente Erweiterung ausschließlich mathematische Konstruktionen. Keine Fehlvorläufe/Korrektur, empirisches main wird nicht ausgeführt. Exakter allgemeiner Satz/Grenzen in GENERAL_SELECTION_COMPLETION.md.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
I=s.eye(3);F=s.diag(1,2,3);W=F**2/14;S=I-s.ones(3)/3;R=I-S
cross=S*F*R+R*F*S;crossnorm=s.factor(s.trace(cross.T*cross));assert crossnorm>0
assert s.trace(W*cross)==s.Rational(8,21)
update=audit.load_update();calls=0;rng=np.random.default_rng(20261112)
arr=lambda a:np.array(a.tolist(),float)
def run(label,f,w,q):
    global calls
    r=np.eye(3)-q;y=q/2+2*r;o=update(-np.eye(3),f,w,y,np.eye(3));calls+=1
    assert o['terminal'] is None
    v=o['t4']@q;J=np.vstack([v,r]);m=len(o['f']);state=J@w@J.conj().T
    seed=o['f']-v@f@v.conj().T
    hext=J@f@J.conj().T;hext[:m,:m]+=seed
    iso=float(np.linalg.norm(J.conj().T@J-np.eye(3)))
    selected=float(np.linalg.norm(hext[:m,:m]-o['f']))
    density=float(np.linalg.norm(state[:m,:m]/o['msel']-o['w']))
    energy=float(np.trace(state@hext).real);ein=float(np.trace(w@f).real)
    dephased=state.copy();dephased[:m,m:]=0;dephased[m:,:m]=0
    ed=float(np.trace(dephased@hext).real);x=float(np.trace(w@(q@f@r+r@f@q)).real)
    kraus=[np.sqrt(a)*audit.complex_unitary(rng,3)@r for a in [.25,.75]]
    effect=sum(k.conj().T@k for k in kraus);gr=sum(k.conj().T@np.diag([4.,5.,6.])@k for k in kraus)
    defect=f-q@f@q-gr;off=float(np.linalg.norm(q@defect@r-q@f@r))
    assert max(iso,selected,density,abs(energy-ein),abs(ein-ed-x),np.linalg.norm(effect-r),np.linalg.norm(q@gr),off)<1e-10
    assert np.linalg.eigvalsh((hext+hext.conj().T)/2).min()>-1e-10
    return dict(label=label,extended_dimension=len(hext),isometry_residual=iso,kept_energy_operator_residual=selected,kept_conditional_state_residual=density,coherent_extended_energy=energy,input_energy=ein,classically_dephased_energy=ed,cross_expectation=x,random_failure_effect_residual=float(np.linalg.norm(effect-r)),random_failure_pullback_support_residual=float(np.linalg.norm(q@gr)),unavoidable_offdiagonal_norm=float(np.linalg.norm(q@defect@r)),offdiagonal_identity_residual=off)
rows=[run('oblique',arr(F),arr(W),arr(S)),run('protected',arr(F),arr(W),np.diag([1.,1.,0.]))]
g=audit.complex_unitary(rng,3);conj=lambda a:g@a@g.conj().T
rows.append(run('oblique_gauge',conj(arr(F)),conj(arr(W)),conj(arr(S))))
gauge=abs(rows[0]['cross_expectation']-rows[-1]['cross_expectation']);assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261112,exact_cross_operator=[[str(x) for x in row] for row in cross.tolist()],exact_cross_frobenius_squared=str(crossnorm),exact_cross_expectation='8/21',gauge_cross_residual=gauge,cases=rows,scope='Any classical blockadditive CP failure completion has the same offdiagonal F obstruction. Coherent isometric energy extension exists mathematically but is not a source-selected physical environment.')

print(json.dumps(result,indent=2))

```

Rohdaten:

```json
{
  "status": "PASS",
  "calls": 3,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261112,
  "exact_cross_operator": [
    [
      "-2/3",
      "-1/3",
      "0"
    ],
    [
      "-1/3",
      "0",
      "1/3"
    ],
    [
      "0",
      "1/3",
      "2/3"
    ]
  ],
  "exact_cross_frobenius_squared": "4/3",
  "exact_cross_expectation": "8/21",
  "gauge_cross_residual": 5.551115123125783e-17,
  "cases": [
    {
      "label": "oblique",
      "extended_dimension": 5,
      "isometry_residual": 4.437999950946387e-16,
      "kept_energy_operator_residual": 0,
      "kept_conditional_state_residual": 1.415262216750919e-16,
      "coherent_extended_energy": 2.5714285714285716,
      "input_energy": 2.5714285714285716,
      "classically_dephased_energy": 2.1904761904761907,
      "cross_expectation": 0.3809523809523811,
      "random_failure_effect_residual": 9.983329836384224e-17,
      "random_failure_pullback_support_residual": 3.0632424703794725e-16,
      "unavoidable_offdiagonal_norm": 0.816496580927726,
      "offdiagonal_identity_residual": 2.1782311762897924e-16
    },
    {
      "label": "protected",
      "extended_dimension": 5,
      "isometry_residual": 0,
      "kept_energy_operator_residual": 0,
      "kept_conditional_state_residual": 0,
      "coherent_extended_energy": 2.5714285714285716,
      "input_energy": 2.5714285714285716,
      "classically_dephased_energy": 2.5714285714285716,
      "cross_expectation": 0,
      "random_failure_effect_residual": 2.220446049250313e-16,
      "random_failure_pullback_support_residual": 0,
      "unavoidable_offdiagonal_norm": 0,
      "offdiagonal_identity_residual": 0
    },
    {
      "label": "oblique_gauge",
      "extended_dimension": 5,
      "isometry_residual": 5.351534061875271e-16,
      "kept_energy_operator_residual": 0,
      "kept_conditional_state_residual": 5.296209425468139e-16,
      "coherent_extended_energy": 2.5714285714285703,
      "input_energy": 2.571428571428571,
      "classically_dephased_energy": 2.1904761904761894,
      "cross_expectation": 0.38095238095238115,
      "random_failure_effect_residual": 2.617888261996619e-16,
      "random_failure_pullback_support_residual": 9.65304838639767e-16,
      "unavoidable_offdiagonal_norm": 0.8164965809277264,
      "offdiagonal_identity_residual": 1.0596491296791377e-15
    }
  ],
  "scope": "Any classical blockadditive CP failure completion has the same offdiagonal F obstruction. Coherent isometric energy extension exists mathematically but is not a source-selected physical environment."
}
```
