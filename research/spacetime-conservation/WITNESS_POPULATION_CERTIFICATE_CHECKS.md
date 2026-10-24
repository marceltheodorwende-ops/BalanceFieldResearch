# Runde55: exaktes Populationsfaser-Zertifikat

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Exakter rationaler Abschnitt läuft vor den vier Originalereignissen und benötigt keine Gleitkomma-Eigenprojektoren. Code konstruiert ein rationales Witness-Paar, verschieden vom numerischen Paar aus Runde54. Ein frischer lokaler Lauf PASS ohne Fehlvorlauf/Korrektur. Empirisches main wird nicht ausgeführt.

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
lc=s.trace(G*PG*C*P*C*PG.T);lb=s.trace(G*PG*B*P*B*PG.T)
alpha=s.cancel(lb/(lc+lb));assert alpha==s.Rational(4019981,31875481) and lc>0 and lb>0
H=alpha*C*PG.T*PG*C+(1-alpha)*B*PG.T*PG*B
assert H==H.T
minors=lambda a:[s.factor(a[:j,:j].det()) for j in range(1,5)]
cert={name:minors(a) for name,a in [('Y',Y),('I-Y',I-Y),('H',H)]}
assert all(x>0 for row in cert.values() for x in row)
basis=[]
for i in range(3):
    a=s.zeros(4);a[i,i]=1;basis.append(a)
for i in range(3):
    for j in range(i+1,3):
        a=s.zeros(4);a[i,j]=a[j,i]=1;basis.append(a)
M=s.Matrix([[s.trace(b*P*(Y**j)*P) for b in basis] for j in range(4)])
assert M.rank()==4
L=None
for v in M.nullspace():
    a=sum((t*b for t,b in zip(v,basis)),s.zeros(4))
    if s.trace(a*H)!=0:
        L=a;break
assert L is not None
if s.trace(L*H)<0:L=-L
rowbound=max(sum(abs(L[i,j]) for j in range(4)) for i in range(4));L=L/rowbound
assert max(sum(abs(L[i,j]) for j in range(4)) for i in range(4))==1
moments=[s.factor(s.trace(L*P*(Y**j)*P)) for j in range(4)];assert moments==[0]*4
ws=[P/3+L/6,P/3-L/6];gap=s.factor(s.trace(L*H)/3);assert gap>0
cp=Y.charpoly().as_poly();assert s.gcd(cp,cp.diff()).degree()==0
to_np=lambda a:np.array(a.tolist(),dtype=float)
update=audit.load_update();calls=0;rows=[]
def pops(a,w):
    e,u=np.linalg.eigh(a);return np.array([np.vdot(u[:,j],w@u[:,j]).real for j in range(4)])
def run(k,f,w,y,p):
    global calls
    o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
    assert np.linalg.norm(o['f']-np.eye(4))<1e-10
    q=pops(y,w);qo=pops(o['y'],o['w']);moment=float(np.trace(o['w']@o['y']).real)
    predicted=float(np.trace(w@to_np(H)).real) if np.linalg.norm(y-to_np(Y))<1e-10 else None
    if predicted is not None:assert abs(moment-predicted)<1e-10
    return dict(input_population=q.tolist(),output_population=qo.tolist(),output_moment=moment,predicted_moment=predicted,formation_identity_residual=float(np.linalg.norm(o['f']-np.eye(4)))),q,qo
for w in ws:
    row,qi,qo=run(-np.eye(4),to_np(P),to_np(w),to_np(Y),to_np(P));rows.append(row)
igap=float(np.max(np.abs(np.array(rows[0]['input_population'])-rows[1]['input_population'])))
ogap=float(np.max(np.abs(np.array(rows[0]['output_population'])-rows[1]['output_population'])))
mgap=rows[0]['output_moment']-rows[1]['output_moment']
assert igap<1e-10 and ogap>1e-5 and abs(mgap-float(gap))<1e-10
rng=np.random.default_rng(20261105);g=audit.complex_unitary(rng,4);conj=lambda a:g@a@g.conj().T;gauge=0.
for w,ref in zip(ws,rows):
    row,qi,qo=run(-np.eye(4),conj(to_np(P)),conj(to_np(w)),conj(to_np(Y)),conj(to_np(P)))
    gauge=max(gauge,float(np.max(np.abs(qi-ref['input_population']))),float(np.max(np.abs(qo-ref['output_population']))),abs(row['output_moment']-ref['output_moment']))
assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261105,alpha=str(alpha),positive_leading_minors={k:list(map(str,v)) for k,v in cert.items()},L=[[str(x) for x in row] for row in L.tolist()],null_moments=list(map(str,moments)),input_moment_rank=4,exact_output_moment_gap=str(gap),output_moment_gap_float=float(gap),witness_lower_bound='1/6 on P',input_population_gap=igap,output_population_gap=ogap,numerical_output_moment_gap=mgap,gauge_residual=gauge,cases=rows,scope='Exact rational alternative witness certifies spectral-population nonclosure; original-update floating-point checks are separate.')

print(json.dumps(result,indent=2))

```

Rohresultat:

```json
{
  "status": "PASS",
  "calls": 4,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261105,
  "alpha": "4019981/31875481",
  "positive_leading_minors": {
    "Y": [
      "1/5",
      "691/10000",
      "18951/500000",
      "2475617/100000000"
    ],
    "I-Y": [
      "4/5",
      "5191/10000",
      "116599/500000",
      "6409917/100000000"
    ],
    "H": [
      "5627527074347633000/50164763677853954481",
      "696472259026465196750000/48455332469179510510120617",
      "119016069427670962088692000000000/50969721972510480904203451151428641",
      "2711645539429482709508411610023558938203125000000/284098228608545376382081876325204531726744450503743369"
    ]
  },
  "L": [
    [
      "-283354/2020591",
      "-21363972/38391229",
      "11643531/38391229",
      "0"
    ],
    [
      "-21363972/38391229",
      "4176682/38391229",
      "0",
      "0"
    ],
    [
      "11643531/38391229",
      "0",
      "1207044/38391229",
      "0"
    ],
    [
      "0",
      "0",
      "0",
      "0"
    ]
  ],
  "null_moments": [
    "0",
    "0",
    "0",
    "0"
  ],
  "input_moment_rank": 4,
  "exact_output_moment_gap": "432029868515685052375000/1925886930087373395035647149",
  "output_moment_gap_float": 0.00022432774311214874,
  "witness_lower_bound": "1/6 on P",
  "input_population_gap": 1.6653345369377348e-16,
  "output_population_gap": 0.05500560921891168,
  "numerical_output_moment_gap": 0.00022432774311215153,
  "gauge_residual": 9.43689570931383e-16,
  "cases": [
    {
      "input_population": [
        0.32711760838999193,
        0.3197278820811195,
        0.3023734426051525,
        0.050781066923736004
      ],
      "output_population": [
        0.006742578230764962,
        0.350865349313867,
        0.30234280791517965,
        0.34004926454018847
      ],
      "output_moment": 0.13443592621764594,
      "predicted_moment": 0.13443592621764577,
      "formation_identity_residual": 1.2411658558941093e-15
    },
    {
      "input_population": [
        0.32711760838999193,
        0.3197278820811197,
        0.3023734426051524,
        0.05078106692373599
      ],
      "output_population": [
        0.008625645775469926,
        0.31304731313322953,
        0.3573484171340913,
        0.3209786239572092
      ],
      "output_moment": 0.1342115984745338,
      "predicted_moment": 0.13421159847453362,
      "formation_identity_residual": 1.2411658558941093e-15
    }
  ],
  "scope": "Exact rational alternative witness certifies spectral-population nonclosure; original-update floating-point checks are separate."
}
```
