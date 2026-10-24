# Runde56: exakter Ergänzungsraum und Mehrschrittprüfung

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Vollständiger lokaler Lauf mit6 Originalereignissen PASS; anschließend neuer I-H-Positivitätsguard und dessen kompletter rationaler/Rekonstruktionspräfix separat frisch PASS,0 weitere Originalaufrufe. Keine Fehler oder Fehlvorläufe. Zusammengeführte Rohdaten unten enthalten diesen Guard. Empirisches main wird nicht ausgeführt. Zukunftsbeweis und genaue Minimalitätsklasse: WITNESS_OBSERVABLE_COMPLETION.md.

```python
import sys,json
from pathlib import Path
import sympy as s
import numpy as np
sys.path.insert(0,'research/spacetime-conservation')
import audit
I=s.eye(4);P=s.diag(1,1,1,0);Z=I[:,:3]
Y=s.Matrix([[20,3,1,8],[3,35,2,7],[1,2,55,6],[8,7,6,70]])/100
G=I+Y;C=G.inv();B=Y*C;PG=Z*(Z.T*G*Z).inv()*Z.T*G
lc=s.trace(G*PG*C*P*C*PG.T);lb=s.trace(G*PG*B*P*B*PG.T);alpha=s.cancel(lb/(lc+lb))
H=alpha*C*PG.T*PG*C+(1-alpha)*B*PG.T*PG*B
upper_minors=[s.factor((I-H)[:j,:j].det()) for j in range(1,5)]
assert all(x>0 for x in upper_minors)
basis=[]
for i in range(3):
    a=s.zeros(4);a[i,i]=1;basis.append(a)
for i in range(3):
    for j in range(i+1,3):
        a=s.zeros(4);a[i,j]=a[j,i]=1;basis.append(a)
coords=lambda a:s.Matrix([[s.trace(a*b) for b in basis]])
observables=[P*(Y**j)*P for j in range(4)];labels=['Y^'+str(j) for j in range(4)]
M=s.Matrix.vstack(*[coords(a) for a in observables]);ranks=[M.rank()]
for j in range(1,4):
    a=P*(H**j)*P;candidate=M.col_join(coords(a));r=candidate.rank();ranks.append(r)
    if r>M.rank():observables.append(a);labels.append('H^'+str(j));M=candidate
assert M.rank()==6 and len(observables)==6
det=s.factor(M.det());assert det!=0
representations={}
for j in range(4):
    a=P*(H**j)*P;coeff=M.T.inv()*coords(a).T
    assert sum((t*b for t,b in zip(coeff,observables)),s.zeros(4))==a
    representations[str(j)]=list(map(str,coeff))
to_np=lambda a:np.array(a.tolist(),dtype=float)
O=list(map(to_np,observables));S=list(map(to_np,basis));mn=to_np(M)
rng=np.random.default_rng(20261106);pp=to_np(P);w=pp@audit.pos(rng,4)@pp;w=w/np.trace(w).real
q=np.array([np.trace(w@a).real for a in O]);reconstructed=sum(t*b for t,b in zip(np.linalg.solve(mn,q),S))
recon=float(np.linalg.norm(reconstructed-w.real));assert recon<1e-9
he,hu=np.linalg.eigh(to_np(H));weights=np.array([np.vdot(hu[:,j],reconstructed@hu[:,j]).real for j in range(4)])
assert min(weights)>-1e-10 and abs(sum(weights)-1)<1e-10
update=audit.load_update();calls=0
def trajectory(g):
    global calls
    conj=lambda a:g@a@g.conj().T
    k=-np.eye(4);f=conj(pp);ww=conj(w);y=conj(to_np(Y));p=conj(pp);values=he.copy();rows=[]
    for step in range(3):
        o=update(k,f,ww,y,p);calls+=1;assert o['terminal'] is None
        assert np.linalg.norm(o['f']-np.eye(4))<1e-10 and np.linalg.norm(o['p']-np.eye(4))<1e-10
        if step:values=(o['alpha']+(1-o['alpha'])*values**2)/(1+values)**2
        got=np.array([np.trace(o['w']@np.linalg.matrix_power(o['y'],j)).real for j in range(4)])
        predicted=np.array([np.sum(weights*values**j) for j in range(4)])
        resid=float(np.max(np.abs(got-predicted)));assert resid<1e-10
        rows.append(dict(event=step+1,alpha=o['alpha'],moments=got.tolist(),prediction=predicted.tolist(),moment_residual=resid))
        k,f,ww,y,p=[o[x] for x in ['k','f','w','y','p']]
    return rows
real=trajectory(np.eye(4));g=audit.complex_unitary(rng,4);gauged=trajectory(g)
gauge=max(float(np.max(np.abs(np.array(a['moments'])-b['moments']))) for a,b in zip(real,gauged));assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261106,positive_I_minus_H_minors=list(map(str,upper_minors)),rank_sequence=ranks,selected_observables=labels,exact_basis_determinant=str(det),output_moment_representations=representations,reconstruction_residual=recon,discarded_imaginary_norm=float(np.linalg.norm(w.imag)),minimum_active_witness_eigenvalue=float(np.linalg.eigvalsh(w[:3,:3]).min()),initial_output_spectral_weights=weights.tolist(),gauge_moment_residual=gauge,trajectory=real,gauge_trajectory=gauged,scope='Exact rank6 joint input/future real observable space at fixed real background; two extra affine readouts beyond rank4 input population space. Not universal physical momentum or spacetime dimension.')

print(json.dumps(result,indent=2))

```

Rohdaten:

```json
{
  "status": "PASS",
  "calls": 6,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261106,
  "rank_sequence": [
    4,
    5,
    6,
    6
  ],
  "selected_observables": [
    "Y^0",
    "Y^1",
    "Y^2",
    "Y^3",
    "H^1",
    "H^2"
  ],
  "exact_basis_determinant": "50039509481554182681062527277403475/17825502216487046980221686777068840575409321698",
  "output_moment_representations": {
    "0": [
      "1",
      "0",
      "0",
      "0",
      "0",
      "0"
    ],
    "1": [
      "0",
      "0",
      "0",
      "0",
      "1",
      "0"
    ],
    "2": [
      "0",
      "0",
      "0",
      "0",
      "0",
      "1"
    ],
    "3": [
      "-5695351982955401192225081350067210734203955764937587500/3369241113532036263240109492541844380020679809310583147579",
      "-1795973324707056355349233360286609066040233634687500000/3369241113532036263240109492541844380020679809310583147579",
      "-85443624851908168104425000000000/16989907324170160301401150383809547",
      "46564655997122875000000000/13543159650068162800508848047",
      "-175109079562774540777186164156161353710203686325/105700086958124216642883271080422108140758089558259",
      "14245305399283376644/50164763677853954481"
    ]
  },
  "reconstruction_residual": 6.144579600556882e-14,
  "discarded_imaginary_norm": 0.3458745175489046,
  "minimum_active_witness_eigenvalue": 0.14074619985148715,
  "initial_output_spectral_weights": [
    0.006912597972285998,
    0.362449477372212,
    0.2653607824476618,
    0.36527714220784047
  ],
  "gauge_moment_residual": 2.220446049250313e-16,
  "trajectory": [
    {
      "event": 1,
      "alpha": 0.12611514787808234,
      "moments": [
        1,
        0.135079854709242,
        0.01887692714677235,
        0.002709244285696726
      ],
      "prediction": [
        1.0000000000000002,
        0.1350798547092419,
        0.01887692714677231,
        0.0027092442856967176
      ],
      "moment_residual": 2.220446049250313e-16
    },
    {
      "event": 2,
      "alpha": 0.013389634661315819,
      "moments": [
        1.0000000000000002,
        0.024667399749481275,
        0.0006236430304890718,
        0.00001614259661312697
      ],
      "prediction": [
        1.0000000000000002,
        0.02466739974948127,
        0.0006236430304890715,
        0.000016142596613126953
      ],
      "moment_residual": 6.938893903907228e-18
    },
    {
      "event": 3,
      "alpha": 0.0005071671298157842,
      "moments": [
        1.0000000000000002,
        0.0010753572781915669,
        0.0000011878589030013322,
        1.3468154171213835e-9
      ],
      "prediction": [
        1.0000000000000002,
        0.0010753572781915654,
        0.000001187858903001329,
        1.346815417121378e-9
      ],
      "moment_residual": 1.5178830414797062e-18
    }
  ],
  "gauge_trajectory": [
    {
      "event": 1,
      "alpha": 0.1261151478780823,
      "moments": [
        1,
        0.13507985470924191,
        0.018876927146772318,
        0.0027092442856967197
      ],
      "prediction": [
        1.0000000000000002,
        0.1350798547092419,
        0.01887692714677231,
        0.0027092442856967176
      ],
      "moment_residual": 2.220446049250313e-16
    },
    {
      "event": 2,
      "alpha": 0.01338963466131581,
      "moments": [
        1,
        0.024667399749481254,
        0.0006236430304890709,
        0.000016142596613126936
      ],
      "prediction": [
        1.0000000000000002,
        0.02466739974948126,
        0.0006236430304890712,
        0.000016142596613126943
      ],
      "moment_residual": 2.220446049250313e-16
    },
    {
      "event": 3,
      "alpha": 0.0005071671298157841,
      "moments": [
        1,
        0.0010753572781915667,
        0.0000011878589030013317,
        1.3468154171213825e-9
      ],
      "prediction": [
        1.0000000000000002,
        0.0010753572781915651,
        0.0000011878589030013283,
        1.3468154171213763e-9
      ],
      "moment_residual": 2.220446049250313e-16
    }
  ],
  "scope": "Exact rank6 joint input/future real observable space at fixed real background; two extra affine readouts beyond rank4 input population space. Not universal physical momentum or spacetime dimension.",
  "positive_I_minus_H_minors": [
    "44537236603506321481/50164763677853954481",
    "112509145577783343442205851/145365997407538531530361851",
    "33035232232348575645954411604419641/50969721972510480904203451151428641",
    "182733395181710495417136258194792092705316912270500244/284098228608545376382081876325204531726744450503743369"
  ]
}
```
