# Runde68: Symmetrie des vollständigen Quell-Tensorzustands

Präregistrierung68e99e4af6ecff6e4670e26dac7048bc492cc736; Auswertung25. Oktober2026. Ein frischer lokaler PASS mit sechs Originalereignissen ohne Fehlvorlauf/Korrektur. Allgemeine Stabilisator-/Projektorrangbeweise und Geltungsgrenzen in TENSOR_LIFT_FULL_STATE_SYMMETRY.md.

Python-Block als r68_check.py in der Repositorywurzel speichern und `python r68_check.py` mit bestehenden Audit-Abhängigkeiten, NumPy/SymPy ausführen. Gegenüber dem ausgeführten Scratchskript ist nur der Audit-Importpfad auf die Repositorywurzel angepasst. Originalblob vor Import geprüft, kein empirisches main. Back-Felder werden mit dem Original-v aus dem SVD-Rahmen zurückausgerichtet; Kopiensymmetrie wird für alle fünf Felder geprüft.

Die symbolischen Kopiengeneratoren umfassen sämtliche Diagonalprojektoren und verbindende Matrixeinheiten innerhalb jeder Kopiengruppe; sie erzeugen dieselbe Kopienalgebra und damit denselben Kommutanten wie die volle Gruppe. Die resultierenden Kommutantendimensionen zählen komplexe Matrixdimensionen, nicht physikalische Dimensionen. Numerische Positivbeispiele wählen ganze getrennte F-Spektralblöcke bzw. suppR; kein einzelner willkürlicher Eigenvektor wird ausgewählt. Toleranz1e-10,Wurzelcutoff1e-12,Cluster1e-8.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit

def copy_commutant_dimension(m,groups):
    n=2*m;gens=[]
    for i in range(m):
        e=s.zeros(m);e[i,i]=1;gens.append(s.kronecker_product(s.eye(2),e))
    for group in groups:
        for i,j in zip(group,group[1:]):
            e=s.zeros(m);e[i,j]=1;gens.append(s.kronecker_product(s.eye(2),e))
    units=[]
    for i in range(n):
        for j in range(n):
            e=s.zeros(n);e[i,j]=1;units.append(e)
    eq=s.Matrix.vstack(*[s.Matrix.hstack(*[(e*g-g*e).reshape(n*n,1) for e in units]) for g in gens])
    return n*n-eq.rank()
dimensions=[]
for m,groups,expected in [(2,[[0,1]],4),(3,[[0,1,2]],4),(3,[[0],[1,2]],8)]:
    value=copy_commutant_dimension(m,groups);assert value==expected
    dimensions.append(dict(m=m,blocks=groups,commutant_dimension=value))
swap=s.Matrix([[0,0,1],[0,1,0],[1,0,0]])
bad=s.kronecker_product(s.diag(1,0),s.diag(1,1,0));us=s.kronecker_product(s.eye(2),swap)
diff=us*bad*us.T-bad
assert bad.rank()==2 and s.trace(diff.T*diff)==2

def root(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2);assert min(e)>-1e-10
    return (u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T
def rp(f,w):
    t=root(f);return t@w@t
def projector(a,which):
    e,u=np.linalg.eigh((a+a.conj().T)/2)
    chosen=(e>1e-10) if which=='support' else (abs(e-e[0])<1e-8)
    return u[:,chosen]@u[:,chosen].conj().T

update=audit.load_update();calls=0;rows=[]
def run(label,fields,stabilizer,good_kind=None,bad_pair=None):
    global calls
    k,f,w,y,p=fields
    o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
    back={name:o['v']@o[name]@o['v'].conj().T for name in ['k','f','w','y','p']}
    before=max(float(np.linalg.norm(stabilizer@a@stabilizer.conj().T-a)) for a in fields)
    after=max(float(np.linalg.norm(stabilizer@a@stabilizer.conj().T-a)) for a in back.values())
    assert max(before,after)<1e-10
    row=dict(label=label,dimension=len(f),symmetry_input_residual=before,symmetry_output_residual=after,
             density_rank=int(sum(np.linalg.eigvalsh(rp(f,w))>1e-10)))
    if good_kind:
        ji=projector(rp(f,w) if good_kind=='support' else f,good_kind)
        jo=projector(rp(o['f'],o['w']) if good_kind=='support' else o['f'],good_kind)
        jr=float(np.linalg.norm(o['v']@jo@o['v'].conj().T-ji))
        assert abs(np.trace(ji).real-2)<1e-10 and jr<1e-10
        row.update(positive_projector_rank=2,positive_projector_transport_residual=jr)
    if bad_pair is not None:
        b=float(np.linalg.norm(stabilizer@bad_pair@stabilizer.conj().T-bad_pair))
        assert abs(b-np.sqrt(2))<1e-10
        row['noncovariant_coordinate_pair_change']=b
    rows.append(row);return o,back

k=-np.eye(2);f=np.diag([1.,3.]);w=np.array([[.5,.25],[.25,.5]]);y=np.diag([.2,.3]);p=np.eye(2)
run('base',[k,f,w,y,p],np.eye(2))
def lift(t):return [np.kron(a,t if i in [1,2] else np.eye(len(t))) for i,a in enumerate([k,f,w,y,p])]
u2=np.array([[0.,1.],[1.,0.]])
run('uniform_m2',lift(np.eye(2)/2),np.kron(p,u2),'minimum')
u3=np.array(swap.tolist(),float);badn=np.array(bad.tolist(),float)
run('uniform_m3',lift(np.eye(3)/3),np.kron(p,u3),bad_pair=badn)
block=np.eye(3,dtype=complex);block[1:,1:]=np.array([[1.,1j],[1j,1.]])/np.sqrt(2)
run('degenerate_tau_m3',lift(np.diag([.5,.25,.25])),np.kron(p,block),'minimum')
run('pure_tau_m3',lift(np.diag([1.,0.,0.])),np.kron(p,block),'support')
rng=np.random.default_rng(20261118);g=audit.complex_unitary(rng,6);cj=lambda a:g@a@g.conj().T
run('uniform_m3_gauge',[cj(a) for a in lift(np.eye(3)/3)],cj(np.kron(p,u3)),bad_pair=cj(badn))
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261118,
            symbolic_copy_commutants=dimensions,exact_bad_pair_change_squared='2',
            necessary_uniform_m2_ranks=[0,2,4],necessary_uniform_m3_ranks=[0,3,6],
            tolerance=1e-10,sqrt_cutoff=1e-12,cases=rows,
            scope='Uniform tensor lift has a common stabilizer of every current Xi field, requiring covariant projector ranks divisible by m. Nonuniform/pure tau and explicit extra history or label data are distinct alternatives.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Vollständige lokale Ausgabe

```json
{
  "status": "PASS",
  "calls": 6,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261118,
  "symbolic_copy_commutants": [
    {
      "m": 2,
      "blocks": [
        [
          0,
          1
        ]
      ],
      "commutant_dimension": 4
    },
    {
      "m": 3,
      "blocks": [
        [
          0,
          1,
          2
        ]
      ],
      "commutant_dimension": 4
    },
    {
      "m": 3,
      "blocks": [
        [
          0
        ],
        [
          1,
          2
        ]
      ],
      "commutant_dimension": 8
    }
  ],
  "exact_bad_pair_change_squared": "2",
  "necessary_uniform_m2_ranks": [
    0,
    2,
    4
  ],
  "necessary_uniform_m3_ranks": [
    0,
    3,
    6
  ],
  "tolerance": 1e-10,
  "sqrt_cutoff": 1e-12,
  "cases": [
    {
      "label": "base",
      "dimension": 2,
      "symmetry_input_residual": 0.0,
      "symmetry_output_residual": 0.0,
      "density_rank": 2
    },
    {
      "label": "uniform_m2",
      "dimension": 4,
      "symmetry_input_residual": 0.0,
      "symmetry_output_residual": 0.0,
      "density_rank": 4,
      "positive_projector_rank": 2,
      "positive_projector_transport_residual": 0.0
    },
    {
      "label": "uniform_m3",
      "dimension": 6,
      "symmetry_input_residual": 0.0,
      "symmetry_output_residual": 0.0,
      "density_rank": 6,
      "noncovariant_coordinate_pair_change": 1.4142135623730951
    },
    {
      "label": "degenerate_tau_m3",
      "dimension": 6,
      "symmetry_input_residual": 4.452147374007132e-16,
      "symmetry_output_residual": 4.452147374007132e-16,
      "density_rank": 6,
      "positive_projector_rank": 2,
      "positive_projector_transport_residual": 0.0
    },
    {
      "label": "pure_tau_m3",
      "dimension": 6,
      "symmetry_input_residual": 4.452147374007132e-16,
      "symmetry_output_residual": 4.452147374007132e-16,
      "density_rank": 2,
      "positive_projector_rank": 2,
      "positive_projector_transport_residual": 0.0
    },
    {
      "label": "uniform_m3_gauge",
      "dimension": 6,
      "symmetry_input_residual": 1.5024197651096135e-15,
      "symmetry_output_residual": 3.378600228550355e-15,
      "density_rank": 6,
      "noncovariant_coordinate_pair_change": 1.4142135623730954
    }
  ],
  "scope": "Uniform tensor lift has a common stabilizer of every current Xi field, requiring covariant projector ranks divisible by m. Nonuniform/pure tau and explicit extra history or label data are distinct alternatives."
}
```

Dokumentierte lokale Kontrolle, keine automatisch von der unveränderten GitHub-Pipeline ausgeführte neue Audit-Datei. Notwendige Rangverträglichkeit ist keine allgemeine eindeutige physikalische Auswahlregel.
