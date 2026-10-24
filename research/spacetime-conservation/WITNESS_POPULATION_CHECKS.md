# Runde54: Populationsfaser-Reproduktion

Aus Repositorywurzel mit audit-Abhängigkeiten, NumPy und SymPy ausführen. Die ersten fünf Originalaufrufe bestanden die Faser-/Eichprüfung, endeten aber an einer falschen Vollträger-alpha-Kontrollformel; korrigierter finaler Code unten. Frischer finaler Lauf: fünf Aufrufe PASS. Insgesamt10 Aufrufe; kein empirisches main ausgeführt. Der konkrete Zeuge ist numerisch, kein Intervallzertifikat.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
update=audit.load_update();calls=0
p=np.diag([1.,1.,1.,0.]);f=p.copy();k=-np.eye(4)
y=np.array([[.2,.03,.01,.08],[.03,.35,.02,.07],[.01,.02,.55,.06],[.08,.07,.06,.7]])
def effects(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2)
    return e,[np.outer(u[:,j],u[:,j].conj()) for j in range(len(e))]
ye,ein=effects(y);assert min(ye)>0 and max(ye)<1
def run(k,f,w,y,p):
    global calls
    o=update(k,f,w,y,p);calls+=1
    assert o['terminal'] is None
    return o
o=run(k,f,p/3,y,p);yo,eout=effects(o['y']);v=o['t4']@p
basis=[]
for i in range(3):
    a=np.zeros((4,4));a[i,i]=1;basis.append(a)
for i in range(3):
    for j in range(i+1,3):
        a=np.zeros((4,4));a[i,j]=a[j,i]=1/np.sqrt(2);basis.append(a)
vec=lambda a:np.array([np.trace(b@a).real for b in basis])
mat=lambda a:sum(t*b for t,b in zip(a,basis))
A=np.array([vec(p@e@p) for e in ein]+[vec(p)])
u,sv,vh=np.linalg.svd(A,full_matrices=False);rank=int(np.sum(sv>1e-10))
projector=vh[:rank].T@vh[:rank]
B=[vec(v.conj().T@e@v) for e in eout]
res=[b-projector@b for b in B];j=int(np.argmax([np.linalg.norm(a) for a in res]))
lnorm=float(np.linalg.norm(res[j]));assert lnorm>1e-5
L=mat(res[j]/lnorm);assert np.linalg.norm(A@vec(L))<1e-10
ws=[p/3+.1*L,p/3-.1*L];assert min(np.linalg.eigvalsh(w[:3,:3]).min() for w in ws)>0
def pops(o,w,y):
    _,ee=effects(y);_,eo=effects(o['y'])
    return np.array([np.trace(e@w).real for e in ee]),np.array([np.trace(e@o['w']).real for e in eo])
rows=[];outs=[]
for w in ws:
    oo=run(k,f,w,y,p);qi,qo=pops(oo,w,y);outs.append((qi,qo))
    rows.append(dict(input_population=qi.tolist(),output_population=qo.tolist(),energy=float(np.trace(w@f).real),energy_out=float(np.trace(oo['w']@oo['f']).real),output_rank=int(round(np.trace(oo['p']).real))))
igap=float(np.max(np.abs(outs[0][0]-outs[1][0])));ogap=float(np.max(np.abs(outs[0][1]-outs[1][1])))
assert igap<1e-10 and ogap>1e-5 and abs(ogap-.2*lnorm)<1e-10
rng=np.random.default_rng(20261104);g=audit.complex_unitary(rng,4);conj=lambda a:g@a@g.conj().T
gauge=0.
for w,(qi,qo) in zip(ws,outs):
    oo=run(conj(k),conj(f),conj(w),conj(y),conj(p));gi,go=pops(oo,conj(w),conj(y))
    gauge=max(gauge,float(np.max(np.abs(gi-qi))),float(np.max(np.abs(go-qo))))
assert gauge<1e-10
Y=s.Matrix([[s.Rational(str(t)) for t in row] for row in y.tolist()]);P=s.diag(1,1,1,0);C=(s.eye(4)+Y).inv()
G=s.eye(4)+Y;Z=s.eye(4)[:,:3];PG=Z*(Z.T*G*Z).inv()*Z.T*G;B=Y*C
lc=s.trace(G*PG*C*P*C*PG.T);lb=s.trace(G*PG*B*P*B*PG.T)
alpha=s.cancel(lb/(lc+lb));assert abs(float(alpha)-o['alpha'])<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261104,alpha_exact=str(alpha),input_Y_eigenvalues=ye.tolist(),output_Y_eigenvalues=yo.tolist(),minimum_spectral_gap=float(min(np.min(np.diff(ye)),np.min(np.diff(yo)))),input_span_singular_values=sv.tolist(),input_span_rank=rank,selected_output=j,output_span_residual=lnorm,L=L.tolist(),minimum_active_witness_eigenvalue=float(min(np.linalg.eigvalsh(w[:3,:3]).min() for w in ws)),input_population_gap=igap,output_population_gap=ogap,gauge_population_residual=gauge,cases=rows,scope='Numerical witness-population nonclosure at instantaneous Y spectral covers; exact linear-span criterion separately proved. Not a spatial current identification or exact interval certificate.')

print(json.dumps(result,indent=2))

```

Finale Rohdaten:

```json
{
  "status": "PASS",
  "calls": 5,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261104,
  "alpha_exact": "4019981/31875481",
  "input_Y_eigenvalues": [
    0.18521113398285383,
    0.3375218062019368,
    0.5298440654763632,
    0.747422994338846
  ],
  "output_Y_eigenvalues": [
    0.00399615611541471,
    0.11203327155644575,
    0.1297698406169991,
    0.16428622759610909
  ],
  "minimum_spectral_gap": 0.017736569060553334,
  "input_span_singular_values": [
    1.977711289477622,
    0.9712216831456921,
    0.9264235123428464,
    0.1276258127722888,
    2.951968239460645e-16
  ],
  "input_span_rank": 4,
  "selected_output": 2,
  "output_span_residual": 0.2279948351333779,
  "L": [
    [
      0.15603113073469663,
      0.6247344047508585,
      0.015470415795295097,
      0
    ],
    [
      0.6247344047508585,
      -0.14307055506758304,
      -0.29491719643325726,
      0
    ],
    [
      0.015470415795295097,
      -0.29491719643325726,
      -0.012960575667113524,
      0
    ],
    [
      0,
      0,
      0,
      0
    ]
  ],
  "minimum_active_witness_eigenvalue": 0.2612725967923556,
  "input_population_gap": 1.1102230246251565e-16,
  "output_population_gap": 0.04559896702667571,
  "gauge_population_residual": 2.7755575615628914e-16,
  "cases": [
    {
      "input_population": [
        0.327117608389992,
        0.3197278820811197,
        0.30237344260515236,
        0.050781066923736046
      ],
      "output_population": [
        0.008372198982845797,
        0.3165585998080192,
        0.3526450960379732,
        0.3224241051711617
      ],
      "energy": 1,
      "energy_out": 0.9999999999999993,
      "output_rank": 4
    },
    {
      "input_population": [
        0.32711760838999193,
        0.31972788208111963,
        0.3023734426051525,
        0.05078106692373595
      ],
      "output_population": [
        0.006996025023389089,
        0.34735406263907737,
        0.3070461290112975,
        0.338603783326236
      ],
      "energy": 1,
      "energy_out": 0.9999999999999993,
      "output_rank": 4
    }
  ],
  "scope": "Numerical witness-population nonclosure at instantaneous Y spectral covers; exact linear-span criterion separately proved. Not a spatial current identification or exact interval certificate."
}
```
