# Runde66: Näherungspaar – ausführbarer Prüftext und Rohdaten

Präregistrierung53cfa470da80bf3b692a5d924528c5535123a06b. Auswertung25. Oktober2026. Finaler frischer lokaler PASS mit fünf Originalereignissen. Zuvor ein PASS mit denselben fünf Fällen; eine zusätzliche nichtkovariante Koordinatenabstands-Diagnose wurde entfernt und der vollständige Lauf wiederholt. Insgesamt10 Originalaufrufe, keine fehlgeschlagenen Assertions. Details und Grenzen in APPROXIMATE_WITNESS_PAIR.md.

Aus Repositorywurzel folgenden Block als r66_check.py speichern und `python r66_check.py` mit bestehenden Audit-Abhängigkeiten, NumPy und SymPy ausführen. Gegenüber dem ausgeführten Scratchskript ist nur der Audit-Importpfad an die Repositorywurzel angepasst. Originalblob wird durch audit.load_update() geprüft; empirisches main wird nicht ausgeführt. Die Regel ist nur für den dreidimensionalen R-Träger implementiert, unabhängig von der vollen Umgebungsdimension.

Frobenius-orthonormale tracelose Hermitesche Basis, positiver gemeinsamer Kommutator-Gramoperator, einfache kleinste Mode und eindeutig näherliegendes Zweiercluster. Kleine negative numerische Nullwerte im isotropen Fall sind Rundungsreste; kein negativer exakter L-Operator. Exakte Rang-/Rayleighkontrollen getrennt von Toleranz1e-10, Wurzelcutoff1e-12 und Lückenprüfung1e-8.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit

F=s.diag(1,4,9);E=s.symbols('epsilon',real=True)
R=s.Matrix([[s.Rational(3,10),s.Rational(1,5),3*E],[s.Rational(1,5),s.Rational(6,5),0],[3*E,0,s.Rational(18,5)]])
J=s.diag(1,1,0);T0=(J-s.eye(3)*s.Rational(2,3))/s.sqrt(s.Rational(2,3))
comm=lambda a,b:a*b-b*a
def lap(r,a,t):return comm(r,comm(r,t))+comm(a,comm(a,t))
rayleigh=s.simplify(s.trace(T0*lap(R,F,T0)))
assert s.trace(T0*T0)==1 and s.trace(T0)==0 and rayleigh==27*E**2
units=[]
for i in range(3):
    for j in range(3):
        b=s.zeros(3);b[i,j]=1;units.append(b)
exact_ranks=[]
for label,r,a,rank in [('zero',R.subs(E,0),F,7),('bridge',R.subs(E,s.Rational(1,100)),F,8),('isotropic',s.eye(3)*s.Rational(3,7),s.diag(1,1,3),4)]:
    m=s.Matrix.hstack(*[lap(r,a,b).reshape(9,1) for b in units]);assert m.rank()==rank
    exact_ranks.append(dict(label=label,full_operator_rank=rank,traceless_nullity=8-rank))

def root(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2);assert min(e)>-1e-10
    return (u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T

def select(f,w):
    sf=root(f);r=sf@w@sf;e,u=np.linalg.eigh((r+r.conj().T)/2);z=u[:,e>1e-10]
    assert z.shape[1]==3
    q=z@z.conj().T;rr=z.conj().T@r@z;aa=z.conj().T@f@z
    hs=[np.diag([1.,-1.,0.])/np.sqrt(2),np.diag([1.,1.,-2.])/np.sqrt(6)]
    for i in range(3):
        for j in range(i+1,3):
            b=np.zeros((3,3),complex);b[i,j]=b[j,i]=1/np.sqrt(2);hs.append(b)
            b=np.zeros((3,3),complex);b[i,j]=1j/np.sqrt(2);b[j,i]=-1j/np.sqrt(2);hs.append(b)
    cs=[np.r_[(rr@b-b@rr).reshape(-1),(aa@b-b@aa).reshape(-1)] for b in hs]
    l=np.array([[np.vdot(a,b).real for b in cs] for a in cs]);ev,v=np.linalg.eigh(l)
    assert min(ev)>-1e-10
    data=dict(r=r,a=q@f@q,lap_eigenvalues=ev.tolist(),mode_gap=float(ev[1]-ev[0]),projector=None)
    if ev[1]-ev[0]<=1e-8:return data
    t=sum((c*b for c,b in zip(v[:,0],hs)),np.zeros((3,3),complex));te,tv=np.linalg.eigh(t)
    gaps=np.diff(te)
    if abs(gaps[0]-gaps[1])<=1e-8:return data
    ix=[0,1] if gaps[0]<gaps[1] else [1,2];other=({0,1,2}-set(ix)).pop()
    g=min(abs(te[i]-te[other]) for i in ix);assert g>1e-8
    b=z@tv[:,ix];j=b@b.conj().T
    cost=float(np.linalg.norm(r@j-j@r)**2+np.linalg.norm(data['a']@j-j@data['a'])**2)
    bound=float(ev[0]/g**2);assert cost<=bound+1e-10
    data.update(projector=j,cost=cost,bound=bound,lambda_min=float(ev[0]),cluster_gap=float(g),
                cluster_choice_gap=float(abs(gaps[0]-gaps[1])),pair_energy=float(np.trace(j@r).real))
    return data

f=np.diag([1.,4.,9.]);w0=np.array([[.3,.1,0],[.1,.3,0],[0,0,.4]])
zero=select(f,w0);assert np.linalg.norm(zero['projector']-np.diag([1,1,0]))<1e-10
w=w0.copy();w[0,2]=w[2,0]=.01
y=np.array([[.25,.03,.02],[.03,.35,.04],[.02,.04,.45]])
y4=np.array([[.25,.03,.02,.04],[.03,.35,.04,.03],[.02,.04,.45,.02],[.04,.03,.02,.55]])
update=audit.load_update();calls=0;rows=[]
def run(label,k,f,w,y,p,defined):
    global calls
    before=select(f,w);o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
    after=select(o['f'],o['w']);v=o['t4']@p
    eigres=float(np.max(np.abs(np.array(after['lap_eigenvalues'])-before['lap_eigenvalues'])))
    assert eigres<1e-10
    row=dict(label=label,defined=defined,lap_eigenvalues=after['lap_eigenvalues'],
             mode_gap=after['mode_gap'],spectrum_transport_residual=eigres,
             active_output_rank=int(round(np.trace(o['p']).real)))
    if defined:
        assert before['projector'] is not None and after['projector'] is not None
        pr=float(np.linalg.norm(after['projector']-v@before['projector']@v.conj().T))
        errs={key:abs(after[key]-before[key]) for key in ['cost','bound','lambda_min','cluster_gap','pair_energy']}
        assert max([pr]+list(errs.values()))<1e-10
        assert before['lambda_min']>0 and after['cost']>0
        row.update({key:after[key] for key in ['cost','bound','lambda_min','cluster_gap','cluster_choice_gap','pair_energy']})
        row.update(projector_transport_residual=pr,invariant_residuals=errs)
    else:assert before['projector'] is None and after['projector'] is None
    rows.append(row);return o

p=np.eye(3);o=run('bridge',-p,f,w,y,p,True)
run('bridge_successor',o['k'],o['f'],o['w'],o['y'],o['p'],True)
f4=np.zeros((4,4),complex);f4[:3,:3]=f;w4=np.zeros((4,4),complex);w4[:3,:3]=w
p4=np.diag([1.,1.,1.,0.]);run('seed_bridge',-np.eye(4),f4,w4,y4,p4,True)
assert rows[-1]['active_output_rank']==4
rng=np.random.default_rng(20261116);g=audit.complex_unitary(rng,4);cj=lambda a:g@a@g.conj().T
run('seed_bridge_gauge',-np.eye(4),cj(f4),cj(w4),cj(y4),cj(p4),True)
run('isotropic_ambiguous',-p,np.diag([1.,1.,3.]),np.diag([3/7,3/7,1/7]),y,p,False)
assert rows[0]['lambda_min']<=.0027+1e-10
gauge=max(abs(rows[2][key]-rows[3][key]) for key in ['cost','lambda_min','pair_energy']);assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261116,
            exact_rayleigh=str(rayleigh),exact_operator_ranks=exact_ranks,
            zero_bridge_cost=zero['cost'],zero_bridge_mode_gap=zero['mode_gap'],
            gauge_invariant_residual=gauge,tolerance=1e-10,sqrt_cutoff=1e-12,gap_cutoff=1e-8,cases=rows,
            scope='Gap-defined approximate pair is covariant and transported; commutator error is bounded but conserved, not dynamically reduced. Equal Laplacian weights are an explicit candidate choice, not a BFG law.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Vollständige finale lokale Ausgabe

```json
{
  "status": "PASS",
  "calls": 5,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261116,
  "exact_rayleigh": "27*epsilon**2",
  "exact_operator_ranks": [
    {
      "label": "zero",
      "full_operator_rank": 7,
      "traceless_nullity": 1
    },
    {
      "label": "bridge",
      "full_operator_rank": 8,
      "traceless_nullity": 0
    },
    {
      "label": "isotropic",
      "full_operator_rank": 4,
      "traceless_nullity": 4
    }
  ],
  "zero_bridge_cost": 6.458300786649208e-33,
  "zero_bridge_mode_gap": 0.1465885871497039,
  "gauge_invariant_residual": 1.252296877307657e-14,
  "tolerance": 1e-10,
  "sqrt_cutoff": 1e-12,
  "gap_cutoff": 1e-08,
  "cases": [
    {
      "label": "bridge",
      "defined": true,
      "lap_eigenvalues": [
        0.0022934867503124775,
        0.14735848087962702,
        9.824217863233546,
        9.970799065292374,
        30.771567359255382,
        30.77157374136396,
        74.95995642777238,
        74.96303357545204
      ],
      "mode_gap": 0.14506499412931453,
      "spectrum_transport_residual": 1.2079226507921703e-13,
      "active_output_rank": 3,
      "cost": 0.0015370738776649539,
      "bound": 0.00154538897444387,
      "lambda_min": 0.0022934867503124775,
      "cluster_gap": 1.2182297835761264,
      "cluster_choice_gap": 1.2053019551222057,
      "pair_energy": 1.4999267201042445,
      "projector_transport_residual": 1.4350598961151936e-15,
      "invariant_residuals": {
        "cost": 3.686287386450715e-18,
        "bound": 1.0256118870843878e-14,
        "lambda_min": 1.5188371393914935e-14,
        "cluster_gap": 8.659739592076221e-15,
        "pair_energy": 2.886579864025407e-15
      }
    },
    {
      "label": "bridge_successor",
      "defined": true,
      "lap_eigenvalues": [
        0.002293486750315849,
        0.14735848087962694,
        9.824217863233544,
        9.970799065292356,
        30.7715673592554,
        30.77157374136396,
        74.95995642777243,
        74.96303357545206
      ],
      "mode_gap": 0.1450649941293111,
      "spectrum_transport_residual": 4.263256414560601e-14,
      "active_output_rank": 3,
      "cost": 0.001537073877664901,
      "bound": 0.0015453889744461433,
      "lambda_min": 0.002293486750315849,
      "cluster_gap": 1.2182297835761258,
      "cluster_choice_gap": 1.2053019551222037,
      "pair_energy": 1.4999267201042468,
      "projector_transport_residual": 1.3245201644731972e-15,
      "invariant_residuals": {
        "cost": 5.2909066017292616e-17,
        "bound": 2.2733551152676057e-15,
        "lambda_min": 3.3714350755609246e-15,
        "cluster_gap": 6.661338147750939e-16,
        "pair_energy": 2.220446049250313e-15
      }
    },
    {
      "label": "seed_bridge",
      "defined": true,
      "lap_eigenvalues": [
        0.002293486750295048,
        0.14735848087962652,
        9.824217863233498,
        9.970799065292315,
        30.771567359255577,
        30.77157374136412,
        74.95995642777257,
        74.96303357545219
      ],
      "mode_gap": 0.14506499412933146,
      "spectrum_transport_residual": 1.2789769243681803e-13,
      "active_output_rank": 4,
      "cost": 0.0015370738776648663,
      "bound": 0.0015453889744321272,
      "lambda_min": 0.002293486750295048,
      "cluster_gap": 1.2182297835761258,
      "cluster_choice_gap": 1.2053019551222017,
      "pair_energy": 1.4999267201042434,
      "projector_transport_residual": 2.737663106286999e-15,
      "invariant_residuals": {
        "cost": 8.391724815037804e-17,
        "bound": 1.4866580189121237e-15,
        "lambda_min": 2.2412627309620348e-15,
        "cluster_gap": 9.325873406851315e-15,
        "pair_energy": 1.7763568394002505e-15
      }
    },
    {
      "label": "seed_bridge_gauge",
      "defined": true,
      "lap_eigenvalues": [
        0.002293486750307571,
        0.1473584808796286,
        9.82421786323353,
        9.970799065292358,
        30.771567359255545,
        30.771573741364104,
        74.95995642777254,
        74.9630335754523
      ],
      "mode_gap": 0.14506499412932103,
      "spectrum_transport_residual": 1.5631940186722204e-13,
      "active_output_rank": 4,
      "cost": 0.0015370738776648851,
      "bound": 0.0015453889744405215,
      "lambda_min": 0.002293486750307571,
      "cluster_gap": 1.218229783576143,
      "cluster_choice_gap": 1.205301955122255,
      "pair_energy": 1.4999267201042437,
      "projector_transport_residual": 1.902717864990209e-15,
      "invariant_residuals": {
        "cost": 6.591949208711867e-17,
        "bound": 2.2111219105669377e-15,
        "lambda_min": 3.193625919273302e-15,
        "cluster_gap": 2.3314683517128287e-14,
        "pair_energy": 8.881784197001252e-16
      }
    },
    {
      "label": "isotropic_ambiguous",
      "defined": false,
      "lap_eigenvalues": [
        -4.853713303415115e-16,
        -8.323142354298488e-17,
        1.245134980045242e-16,
        9.71445146547012e-16,
        3.9999999999999925,
        3.999999999999993,
        4.0,
        4.000000000000001
      ],
      "mode_gap": 4.021399067985266e-16,
      "spectrum_transport_residual": 6.661338147750939e-15,
      "active_output_rank": 3
    }
  ],
  "scope": "Gap-defined approximate pair is covariant and transported; commutator error is bounded but conserved, not dynamically reduced. Equal Laplacian weights are an explicit candidate choice, not a BFG law."
}
```

Neue Reproduktion ist Dokumenttext und lokale Evidenz, kein automatisch von der unveränderten GitHub-Pipeline ausgeführter Audit.
