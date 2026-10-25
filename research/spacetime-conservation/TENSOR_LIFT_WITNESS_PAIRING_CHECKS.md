# Runde67: Quell-Tensorlift und Witness-Formationspaarung – Reproduktion

Präregistrierung296c4c3dac4466147a3b7eb3feab4ffa8cf5e400. Ein frischer lokaler PASS mit sieben Originalereignissen, keine fehlgeschlagenen Kontrollläufe. BFG-Quellgleichungen163/164 und Theorem8, PDF-Seite80; vollständige Herleitung/Grenzen TENSOR_LIFT_WITNESS_PAIRING.md.

Folgenden Block als r67_check.py in der Repositorywurzel speichern und `python r67_check.py` mit bestehenden Audit-Abhängigkeiten, NumPy/SymPy ausführen. Gegenüber dem ausgeführten Scratchskript ist nur der Audit-Importpfad auf die Repositorywurzel angepasst. Output zusätzlich als JSON neben dem Skript. Pinned Originalblob wird vor Import geprüft, kein empirisches main. Die zurückausgerichteten Originalfelder sind v @ field_out @ v†; im Vollpersistenzzweig ist v quadratisch unitär, weshalb keine willkürliche SVD-Rahmenzuordnung nötig ist. Auch theoretische Nullräume des reinen tau bzw. Rang1-W werden unter dem vorab festgelegten Cutoff behandelt.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit

F=s.diag(1,3);sf=s.diag(1,s.sqrt(3));W=s.Matrix([[s.Rational(1,2),s.Rational(1,4)],[s.Rational(1,4),s.Rational(1,2)]])
R=sf*W*sf
taus=[s.eye(2)/2,s.diag(s.Rational(3,4),s.Rational(1,4)),s.diag(1,0)]
for t,purity in zip(taus,[s.Rational(1,2),s.Rational(5,8),s.Integer(1)]):
    assert s.trace(t)==1 and s.trace(t*t)==purity
    assert s.trace(s.kronecker_product(W,t)*s.kronecker_product(F,t))==s.trace(W*F)*purity
    assert s.kronecker_product(R,t*t).rank()==R.rank()*t.rank()
u=s.Matrix([1,s.sqrt(3)])/2;N=s.ones(2)/2;RN=sf*N*sf
assert u.T*u==s.ones(1) and RN*u==2*u
z=s.kronecker_product(u,s.eye(2));x=s.simplify(z.T*s.kronecker_product(RN,s.eye(2)/4)*z)
assert x==s.eye(2)/2 and x.det()==s.Rational(1,4)

def root(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2);assert min(e)>-1e-10
    return (u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T
def density(f,w):
    q=root(f);return q@w@q
update=audit.load_update();calls=0;rows=[]
def run(label,k,f,w,y,p):
    global calls
    ri=density(f,w);o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
    v=o['v'];back={n:v@o[n]@v.conj().T for n in ['k','f','w','y','p']}
    ro=v@density(o['f'],o['w'])@v.conj().T
    residual=float(np.linalg.norm(ro-ri));assert residual<1e-10
    row=dict(label=label,dimension=len(f),formation_stock=float(np.trace(f).real),
             witness_trace=float(np.trace(w).real),energy_before=float(np.trace(ri).real),
             energy_after=float(np.trace(ro).real),density_rank=int(sum(np.linalg.eigvalsh(ri)>1e-10)),
             retained_density_residual=residual,alpha=float(o['alpha']),lc=float(o['lc']),lb=float(o['lb']))
    rows.append(row);return back,o,row
f=np.diag([1.,3.]);w=np.array([[.5,.25],[.25,.5]]);y=np.diag([.2,.3]);p=np.eye(2);k=-p
base,baseo,br=run('base_full_rank',k,f,w,y,p)
lifted=[]
for label,t in [('uniform',np.eye(2)/2),('biased',np.diag([.75,.25])),('pure',np.diag([1.,0.]))]:
    k2=np.kron(k,np.eye(2));f2=np.kron(f,t);w2=np.kron(w,t);y2=np.kron(y,np.eye(2));p2=np.eye(4)
    back,o,row=run('lift_'+label,k2,f2,w2,y2,p2)
    expected={n:np.kron(base[n],t if n in ['f','w'] else np.eye(2)) for n in base}
    fullres=max(float(np.linalg.norm(back[n]-expected[n])) for n in base)
    rdres=float(np.linalg.norm(density(f2,w2)-np.kron(density(f,w),t@t)))
    purity=float(np.trace(t@t).real)
    assert max(fullres,rdres,abs(o['lc']-baseo['lc']),abs(o['lb']-baseo['lb']),abs(o['alpha']-baseo['alpha']))<1e-10
    assert abs(row['energy_before']-br['energy_before']*purity)<1e-10
    assert row['density_rank']==br['density_rank']*int(sum(np.linalg.eigvalsh(t)>1e-10))
    row.update(purity=purity,full_lift_update_residual=fullres,density_tensor_residual=rdres)
    lifted.append((t,back,o,row))
t,biased,bo,biasedrow=lifted[1];rng=np.random.default_rng(20261117);g=audit.complex_unitary(rng,4);cj=lambda a:g@a@g.conj().T
back,o,row=run('biased_lift_gauge',cj(np.kron(k,np.eye(2))),cj(np.kron(f,t)),cj(np.kron(w,t)),cj(np.kron(y,np.eye(2))),cj(np.eye(4)))
gauge=max(float(np.linalg.norm(back[n]-cj(biased[n]))) for n in back);assert gauge<1e-10
row['full_field_gauge_residual']=gauge
n=np.ones((2,2))/2;null,no,nr=run('rank_one_base',k,f,n,y,p)
back,o,row=run('rank_one_uniform_lift',np.kron(k,p),np.kron(f,p/2),np.kron(n,p/2),np.kron(y,p),np.eye(4))
assert nr['density_rank']==1 and row['density_rank']==2
zz=np.kron(np.array([1.,np.sqrt(3)])/2,np.eye(2)).reshape(2,4).T
# Construct the support frame directly as a tensor product of the column vector.
zz=np.kron((np.array([1.,np.sqrt(3)])/2).reshape(2,1),np.eye(2))
xx=zz.conj().T@density(np.kron(f,p/2),np.kron(n,p/2))@zz
assert np.linalg.norm(xx-np.eye(2)/2)<1e-10
row.update(pair_compression_trace=float(np.trace(xx).real),pair_compression_determinant=float(np.linalg.det(xx).real))
fullres=max(float(np.linalg.norm(back[a]-np.kron(null[a],p/2 if a in ['f','w'] else p))) for a in back)
assert fullres<1e-10;row['full_lift_update_residual']=fullres
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261117,
            source_lift='II90.1 equations163/164, PDFpage80',exact_purities=['1/2','5/8','1'],
            exact_uniform_rank_one_pair='X=I2/2, trace1, determinant1/4',tolerance=1e-10,sqrt_cutoff=1e-12,
            cases=rows,scope='Source-declared tensor lift intertwines full-persistence update; trWF scales by purity across levels while formation stock is unchanged. Level parameters are declared, not autonomously selected physical laws.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Vollständige lokale Ausgabe

```json
{
  "status": "PASS",
  "calls": 7,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261117,
  "source_lift": "II90.1 equations163/164, PDFpage80",
  "exact_purities": [
    "1/2",
    "5/8",
    "1"
  ],
  "exact_uniform_rank_one_pair": "X=I2/2, trace1, determinant1/4",
  "tolerance": 1e-10,
  "sqrt_cutoff": 1e-12,
  "cases": [
    {
      "label": "base_full_rank",
      "dimension": 2,
      "formation_stock": 4.0,
      "witness_trace": 1.0,
      "energy_before": 1.9999999999999998,
      "energy_after": 1.9999999999999998,
      "density_rank": 2,
      "retained_density_residual": 0.0,
      "alpha": 0.07126611068991665,
      "lc": 3.141025641025641,
      "lb": 0.24102564102564117
    },
    {
      "label": "lift_uniform",
      "dimension": 4,
      "formation_stock": 4.0,
      "witness_trace": 1.0,
      "energy_before": 1.0,
      "energy_after": 1.0,
      "density_rank": 4,
      "retained_density_residual": 0.0,
      "alpha": 0.07126611068991665,
      "lc": 3.141025641025641,
      "lb": 0.24102564102564117,
      "purity": 0.5,
      "full_lift_update_residual": 0.0,
      "density_tensor_residual": 3.925231146709438e-17
    },
    {
      "label": "lift_biased",
      "dimension": 4,
      "formation_stock": 4.0,
      "witness_trace": 1.0,
      "energy_before": 1.25,
      "energy_after": 1.25,
      "density_rank": 4,
      "retained_density_residual": 0.0,
      "alpha": 0.07126611068991666,
      "lc": 3.1410256410256405,
      "lb": 0.24102564102564117,
      "purity": 0.625,
      "full_lift_update_residual": 0.0,
      "density_tensor_residual": 1.1443916996305594e-16
    },
    {
      "label": "lift_pure",
      "dimension": 4,
      "formation_stock": 4.0,
      "witness_trace": 1.0,
      "energy_before": 1.9999999999999998,
      "energy_after": 1.9999999999999998,
      "density_rank": 2,
      "retained_density_residual": 0.0,
      "alpha": 0.07126611068991665,
      "lc": 3.141025641025641,
      "lb": 0.24102564102564117,
      "purity": 1.0,
      "full_lift_update_residual": 0.0,
      "density_tensor_residual": 0.0
    },
    {
      "label": "biased_lift_gauge",
      "dimension": 4,
      "formation_stock": 3.9999999999999996,
      "witness_trace": 1.0,
      "energy_before": 1.2499999999999996,
      "energy_after": 1.2499999999999998,
      "density_rank": 4,
      "retained_density_residual": 1.325557033251125e-15,
      "alpha": 0.0712661106899166,
      "lc": 3.141025641025642,
      "lb": 0.24102564102564109,
      "full_field_gauge_residual": 2.958108942860096e-15
    },
    {
      "label": "rank_one_base",
      "dimension": 2,
      "formation_stock": 4.0,
      "witness_trace": 1.0,
      "energy_before": 1.9999999999999998,
      "energy_after": 1.9999999999999998,
      "density_rank": 1,
      "retained_density_residual": 0.0,
      "alpha": 0.07126611068991665,
      "lc": 3.141025641025641,
      "lb": 0.24102564102564117
    },
    {
      "label": "rank_one_uniform_lift",
      "dimension": 4,
      "formation_stock": 4.0,
      "witness_trace": 1.0,
      "energy_before": 1.0,
      "energy_after": 1.0,
      "density_rank": 2,
      "retained_density_residual": 0.0,
      "alpha": 0.07126611068991665,
      "lc": 3.141025641025641,
      "lb": 0.24102564102564117,
      "pair_compression_trace": 0.9999999999999998,
      "pair_compression_determinant": 0.2499999999999999,
      "full_lift_update_residual": 0.0
    }
  ],
  "scope": "Source-declared tensor lift intertwines full-persistence update; trWF scales by purity across levels while formation stock is unchanged. Level parameters are declared, not autonomously selected physical laws."
}
```

Die Parameter m/tau sind in der Quelle deklarierte Leveldaten, kein autonomes physikalisches Auswahlgesetz. Sieben lokale Originalkontrollen sind kein neuer Remote-CI-Pass und keine empirische Bestätigung.
