# Runde52: lokale Reproduktion

Aus Repositorywurzel mit Python, NumPy, SymPy und den bestehenden audit-Abhängigkeiten ausführen. audit.load_update prüft die gepinnte Quelle; empirisches main wird nicht ausgeführt. Reihenfolge der Dichten im JSON: R_F, R_W. Eichprüfung vergleicht rücktransformierte Operatoren; rohe Koordinatenbeiträge werden bei der Eichkontrolle nicht als invariant behauptet.

```python
import json,sys
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
I=s.eye(2);sx=s.Matrix([[0,1],[1,0]]);F=s.diag(1,3);W=(I+sx/2)/2
sf=s.diag(1,s.sqrt(3));sw=(s.sqrt(3)+1)*I/4+(s.sqrt(3)-1)*sx/4
rf=sf*W*sf;rw=s.simplify(sw*F*sw)
assert s.trace(rf)==s.trace(rw)==2 and rf.det()==rw.det()==s.Rational(9,16)
assert rw[0,0]==1-s.sqrt(3)/4 and rf[0,0]==s.Rational(1,2)
ff=s.diag(1,9);ww=(I+s.Rational(9,10)*sx)/2;jordan=(ww*ff+ff*ww)/2
assert jordan.det()==-s.Rational(45,16)
update=audit.load_update();calls=0
def root(m):
    m=(m+m.conj().T)/2;e,u=np.linalg.eigh(m)
    assert min(e)>-1e-10
    active=e[e>1e-12];assert len(active)>0 and min(active)>1e-8
    q=(u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T
    return q,float(np.linalg.norm(q@q-m)/max(1.,np.linalg.norm(m))),float(min(active))
def densities(f,w):
    sf,rf,gf=root(f);sw,rw,gw=root(w)
    return [sf@w@sf,sw@f@sw],max(rf,rw),min(gf,gw)
def run(label,k,f,w,y,p):
    global calls
    o=update(k,f,w,y,p);calls+=1
    assert o['terminal'] is None
    old,root0,gap0=densities(f,w);new,root1,gap1=densities(o['f'],o['w'])
    v=o['t4']@p;s4=o['t4']@o['t4'].conj().T;seed=o['p']-s4;unused=np.eye(len(o['k']))-o['p']
    effects=[]
    for j in range(len(k)):
        e=np.zeros_like(p);e[j,j]=1;effects.append(p@e@p)
    cover=sum(v@e@v.conj().T for e in effects)+seed+unused
    cover_res=float(np.linalg.norm(cover-np.eye(len(o['k']))))
    records=[];backs=[]
    for a,b in zip(old,new):
        transport=float(np.linalg.norm(b-v@a@v.conj().T)/max(1.,np.linalg.norm(b)))
        qi=np.array([np.trace(e@a).real for e in effects]);qo=np.array([np.trace(v@e@v.conj().T@b).real for e in effects])
        co=float(np.linalg.norm(qo-qi)/max(1.,np.linalg.norm(qi)))
        seedq=float(np.trace(seed@b).real);unusedq=float(np.trace(unused@b).real)
        assert min(qi)>-1e-10 and min(qo)>-1e-10 and min(np.linalg.eigvalsh(b))>-1e-10
        assert max(transport,co,abs(seedq),abs(unusedq),cover_res)<1e-10
        records.append(dict(trace_before=float(np.trace(a).real),trace_after=float(np.trace(b).real),coordinate_input_energy=np.diag(a).real.tolist(),transport_residual=transport,comoving_effect_residual=co,seed_energy=seedq,unused_energy=unusedq))
        backs.append(o['v']@b@o['v'].conj().T)
    return dict(label=label,input_dimension=len(k),output_dimension=len(o['k']),output_rank=int(round(np.trace(o['p']).real)),square_root_residual=max(root0,root1),minimum_retained_eigenvalue=min(gap0,gap1),cover_residual=cover_res,densities=records),backs
ni=np.eye(2);nx=np.array(sx,float);rows=[]
r,_=run('full_ambiguity',2*ni+np.diag([1.,-1.]),np.diag([1.,3.]),(ni+.5*nx)/2,np.diag([.2,.3]),ni);rows.append(r)
p=np.diag([1.,1.,0.]);w=np.array([[.6,.1j,0],[-.1j,.4,0],[0,0,0]],complex)
r,_=run('noncommuting_seed',-np.diag([1.,2.,3.]),np.diag([1.,.42,0.]),w,np.array([[.25,0,.1],[0,.5,.1],[.1,.1,.5]]),p);rows.append(r)
rng=np.random.default_rng(20261103);n=4;z=audit.complex_unitary(rng,n);p=z[:,:2]@z[:,:2].conj().T
f=p@audit.pos(rng,n)@p;w=p@audit.pos(rng,n)@p;w=w/np.trace(w).real
z=audit.complex_unitary(rng,n);y=(z*np.array([.15,.3,.5,.7]))@z.conj().T;k=-audit.pos(rng,n)
r,back=run('complex_seed',k,f,w,y,p);rows.append(r)
g=audit.complex_unitary(rng,n);conj=lambda x:g@x@g.conj().T
r,gback=run('complex_gauge',conj(k),conj(f),conj(w),conj(y),conj(p));rows.append(r)
gauge=max(float(np.linalg.norm(b-conj(a))/max(1.,np.linalg.norm(a))) for a,b in zip(back,gback));assert gauge<1e-10
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=calls,seed=20261103,sqrt_cutoff=1e-12,symbolic=dict(RF=[[str(x) for x in row] for row in rf.tolist()],RW=[[str(x) for x in row] for row in rw.tolist()],common_trace='2',common_determinant='9/16',jordan_counterexample_determinant='-45/16'),gauge_density_residual=gauge,cases=rows,scope='Two positive energy-density candidates share exact isometric transport and global invariant but disagree locally. Effects are not spatial regions without a bridge.')

print(json.dumps(result,indent=2))

```

Ein Lauf, vier Originalaufrufe, keine Fehlvorläufe. Rohresultat:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 4,
  "seed": 20261103,
  "sqrt_cutoff": 1e-12,
  "symbolic": {
    "RF": [
      [
        "1/2",
        "sqrt(3)/4"
      ],
      [
        "sqrt(3)/4",
        "3/2"
      ]
    ],
    "RW": [
      [
        "1 - sqrt(3)/4",
        "1/2"
      ],
      [
        "1/2",
        "sqrt(3)/4 + 1"
      ]
    ],
    "common_trace": "2",
    "common_determinant": "9/16",
    "jordan_counterexample_determinant": "-45/16"
  },
  "gauge_density_residual": 3.0275068114561745e-15,
  "cases": [
    {
      "label": "full_ambiguity",
      "input_dimension": 2,
      "output_dimension": 2,
      "output_rank": 2,
      "square_root_residual": 2.633125101432526e-16,
      "minimum_retained_eigenvalue": 0.25,
      "cover_residual": 0,
      "densities": [
        {
          "trace_before": 1.9999999999999998,
          "trace_after": 1.9999999999999998,
          "coordinate_input_energy": [
            0.5,
            1.4999999999999998
          ],
          "transport_residual": 0,
          "comoving_effect_residual": 0,
          "seed_energy": 0,
          "unused_energy": 0
        },
        {
          "trace_before": 1.9999999999999991,
          "trace_after": 1.9999999999999991,
          "coordinate_input_energy": [
            0.5669872981077805,
            1.4330127018922187
          ],
          "transport_residual": 0,
          "comoving_effect_residual": 0,
          "seed_energy": 0,
          "unused_energy": 0
        }
      ]
    },
    {
      "label": "noncommuting_seed",
      "input_dimension": 3,
      "output_dimension": 3,
      "output_rank": 3,
      "square_root_residual": 1.8777378735113004e-15,
      "minimum_retained_eigenvalue": 0.35857864376269055,
      "cover_residual": 0,
      "densities": [
        {
          "trace_before": 0.7679999999999999,
          "trace_after": 0.7680000000000011,
          "coordinate_input_energy": [
            0.6,
            0.16799999999999995,
            0
          ],
          "transport_residual": 6.335708625836367e-16,
          "comoving_effect_residual": 1.1298258127427696e-15,
          "seed_energy": -1.191005925783608e-18,
          "unused_energy": -3.6858526558657513e-16
        },
        {
          "trace_before": 0.768,
          "trace_after": 0.7679999999999995,
          "coordinate_input_energy": [
            0.5970395570880345,
            0.1709604429119656,
            0
          ],
          "transport_residual": 1.1381050439451533e-15,
          "comoving_effect_residual": 6.77599954797753e-16,
          "seed_energy": -6.57972727391966e-18,
          "unused_energy": -3.6997665914062835e-16
        }
      ]
    },
    {
      "label": "complex_seed",
      "input_dimension": 4,
      "output_dimension": 4,
      "output_rank": 3,
      "square_root_residual": 9.794564632252288e-16,
      "minimum_retained_eigenvalue": 0.2868568384516175,
      "cover_residual": 1.306427772957477e-15,
      "densities": [
        {
          "trace_before": 8.125079671122128,
          "trace_after": 8.125079671122123,
          "coordinate_input_energy": [
            0.5252493049012741,
            1.53908224019631,
            1.517832766531369,
            4.542915359493175
          ],
          "transport_residual": 2.1784662872475345e-15,
          "comoving_effect_residual": 2.238313800635153e-16,
          "seed_energy": 7.26415455565288e-17,
          "unused_energy": -3.772156198511567e-15
        },
        {
          "trace_before": 8.125079671122133,
          "trace_after": 8.125079671122135,
          "coordinate_input_energy": [
            0.590672869745903,
            1.6419324481132704,
            1.6542389154082018,
            4.238235437854758
          ],
          "transport_residual": 1.1698963068602774e-15,
          "comoving_effect_residual": 1.1795078727558717e-15,
          "seed_energy": 6.765421556309548e-17,
          "unused_energy": -3.7539416020138106e-15
        }
      ]
    },
    {
      "label": "complex_gauge",
      "input_dimension": 4,
      "output_dimension": 4,
      "output_rank": 3,
      "square_root_residual": 1.0609417515258182e-15,
      "minimum_retained_eigenvalue": 0.2868568384516175,
      "cover_residual": 1.82825707489979e-15,
      "densities": [
        {
          "trace_before": 8.125079671122133,
          "trace_after": 8.125079671122137,
          "coordinate_input_energy": [
            2.1482054474176047,
            2.3403790128602777,
            2.4150587219389177,
            1.221436488905332
          ],
          "transport_residual": 8.491696736394161e-16,
          "comoving_effect_residual": 1.0760203531583145e-15,
          "seed_energy": -1.4333152720258369e-16,
          "unused_energy": 1.1232334506949826e-16
        },
        {
          "trace_before": 8.125079671122133,
          "trace_after": 8.125079671122132,
          "coordinate_input_energy": [
            1.8597653628780475,
            2.1163314692837516,
            2.6607807685274847,
            1.48820207043285
          ],
          "transport_residual": 9.853695149814207e-16,
          "comoving_effect_residual": 3.705884844559322e-16,
          "seed_energy": -1.4983674023749671e-16,
          "unused_energy": 5.338611497318624e-16
        }
      ]
    }
  ],
  "scope": "Two positive energy-density candidates share exact isometric transport and global invariant but disagree locally. Effects are not spatial regions without a bridge."
}
```
