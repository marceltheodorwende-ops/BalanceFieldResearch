# Runde65: gemeinsame Witness-/Formationsalgebra – Reproduktion

Präregistrierung fab96e7009802f62254e69e3eeb01b151170ef87; Auswertung25. Oktober2026. Ein frischer lokaler Lauf PASS ohne Fehlvorlauf/Korrektur, sechs nichtterminale Originalereignisse. Allgemeiner Isometrie-/Zentrumbeweis und Grenzen in JOINT_WITNESS_FORMATION_SELECTOR.md. Keine empirischen Daten oder physikalischen Bestätigungen.

Reproduktion: Python-Block als r65_check.py in der Repositorywurzel speichern und `python r65_check.py` mit bestehenden Audit-Abhängigkeiten, NumPy und SymPy ausführen. Gegenüber dem ausgeführten Scratchskript ist nur der Audit-Importpfad an die Repositorywurzel angepasst. JSON wird neben dem Skript geschrieben; `audit.load_update()` prüft den Originalblob und führt kein empirisches main aus.

Die exakte Algebra wird durch Produkte der hermiteschen Generatoren aufgebaut. Ihr Kommutant ist der gemeinsame lineare Kommutationsnullraum; das Zentrum wird als B' geschnitten mit (B')' bestimmt (endlichdimensionaler Bicommutantensatz). Die numerische Kontrolle verwendet dafür reelle Koeffizienten einer hermiteschen Basis. Sie implementiert die Projektorrekonstruktion nur für die hier auftretenden Zentrumdimensionen1/2 auf dem dreidimensionalen R-Träger, keinen allgemeinen Algorithmus für beliebige größere Zentren. Bei Zentrumdimension2 trennt eine nichtskalare zentrale Matrix die beiden minimalen zentralen Komponenten; nur eine eindeutige Rang2-Komponente wird genommen.

Rangtoleranz1e-10, Wurzelcutoff1e-12, Spektralcluster1e-8. Nullräume werden numerisch geprüft, nicht als beliebig kleine Kopplungen zertifiziert. Die exakte beliebig kleine nichtnull Brücke ist im Bericht separat algebraisch behandelt. Rohsingularwerte zeigen den Abstand des tatsächlich geprüften epsilon=1/100 vom Rangcutoff.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit

F=s.diag(1,4,9); sf=s.diag(1,2,3)
W=s.Matrix([[s.Rational(3,10),s.Rational(1,10),0],[s.Rational(1,10),s.Rational(3,10),0],[0,0,s.Rational(2,5)]])
WB=W.copy();WB[0,2]=WB[2,0]=s.Rational(1,100)
Y=s.Matrix([[25,3,2],[3,35,4],[2,4,45]])/100
Y4=s.Matrix([[25,3,2,4],[3,35,4,3],[2,4,45,2],[4,3,2,55]])/100
FI=s.diag(1,1,3);WI=s.diag(s.Rational(3,7),s.Rational(3,7),s.Rational(1,7))
R=sf*W*sf;RB=sf*WB*sf;RI=s.eye(3)*s.Rational(3,7)
assert FI*WI==RI
minors={}
for name,m in [('W',W),('W_bridge',WB),('Y',Y),('I-Y',s.eye(3)-Y),('Y4',Y4),('I-Y4',s.eye(4)-Y4)]:
    ds=[s.factor(m[:j,:j].det()) for j in range(1,m.rows+1)]
    assert all(v>0 for v in ds);minors[name]=list(map(str,ds))

def exact_commutant(gens,n=3):
    units=[]
    for i in range(n):
        for j in range(n):
            e=s.zeros(n);e[i,j]=1;units.append(e)
    rows=s.Matrix.vstack(*[s.Matrix.hstack(*[(e*g-g*e).reshape(n*n,1) for e in units]) for g in gens])
    return [v.reshape(n,n) for v in rows.nullspace()]

def algebra(gens,n=3):
    basis=[s.eye(n)]
    while True:
        candidates=basis+[a*g for a in basis for g in gens]
        cols=s.Matrix.hstack(*[a.reshape(n*n,1) for a in candidates]).columnspace()
        new=[c.reshape(n,n) for c in cols]
        if len(new)==len(basis):return new
        basis=new

symbolic=[]
for name,r,f,expected in [('pair',R,F,(5,2,2)),('bridge',RB,F,(9,1,1)),('isotropic',RI,FI,(2,5,2))]:
    a=algebra([r,f]);c=exact_commutant([r,f]);z=exact_commutant([r,f]+c)
    dims=(len(a),len(c),len(z));assert dims==expected
    symbolic.append(dict(label=name,algebra_dimension=dims[0],commutant_dimension=dims[1],center_dimension=dims[2]))
assert s.trace(s.diag(1,1,0)*R)==s.Rational(3,2)
assert s.trace(R)==s.Rational(51,10)

def hb(n):
    out=[]
    for i in range(n):
        b=np.zeros((n,n),complex);b[i,i]=1;out.append(b)
    for i in range(n):
        for j in range(i+1,n):
            b=np.zeros((n,n),complex);b[i,j]=b[j,i]=1/np.sqrt(2);out.append(b)
            b=np.zeros((n,n),complex);b[i,j]=1j/np.sqrt(2);b[j,i]=-1j/np.sqrt(2);out.append(b)
    return out

def numerical_commutant(gens,n):
    basis=hb(n);cols=[]
    for b in basis:
        v=np.concatenate([(b@g-g@b).reshape(-1) for g in gens])
        cols.append(np.r_[v.real,v.imag])
    m=np.stack(cols,axis=1);_,sv,vh=np.linalg.svd(m,full_matrices=False)
    rank=int(sum(sv>1e-10))
    return [sum((a*b for a,b in zip(v,basis)),np.zeros((n,n),complex)) for v in vh[rank:]],sv.tolist()

def root(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2);assert min(e)>-1e-10
    return (u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T

def select(f,w):
    t=root(f);r=t@w@t;e,u=np.linalg.eigh((r+r.conj().T)/2)
    z=u[:,e>1e-10];q=z@z.conj().T;n=z.shape[1]
    rr=z.conj().T@r@z;aa=z.conj().T@f@z
    comm,csv=numerical_commutant([rr,aa],n)
    center,zsv=numerical_commutant([rr,aa]+comm,n)
    projector=None;clusters=[]
    if len(center)==2:
        candidates=[b-np.trace(b)*np.eye(n)/n for b in center]
        c=max(candidates,key=np.linalg.norm);ee,vv=np.linalg.eigh(c)
        groups=[]
        for i,x in enumerate(ee):
            if not groups or abs(x-ee[groups[-1][0]])>1e-8:groups.append([i])
            else:groups[-1].append(i)
        clusters=[len(g) for g in groups]
        pairs=[g for g in groups if len(g)==2]
        if len(pairs)==1:
            b=z@vv[:,pairs[0]];projector=b@b.conj().T
    elif len(center)!=1:
        raise AssertionError('Test cases require center dimensions1 or2')
    return dict(r=r,q=q,a=q@f@q,projector=projector,comm_dim=len(comm),center_dim=len(center),
                cluster_ranks=clusters,comm_singular_values=csv,center_singular_values=zsv,
                support_rank=n)

update=audit.load_update();calls=0
arr=lambda m:np.array(m.tolist(),complex)
rows=[]
def run(label,k,f,w,y,p,expected_pair,expected_comm):
    global calls
    before=select(f,w);o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
    after=select(o['f'],o['w']);v=o['t4']@p
    rr=float(np.linalg.norm(after['r']-v@before['r']@v.conj().T))
    ar=float(np.linalg.norm(after['a']-v@before['a']@v.conj().T))
    assert max(rr,ar)<1e-10
    assert before['support_rank']==after['support_rank']==3
    assert before['comm_dim']==after['comm_dim']==expected_comm
    assert before['center_dim']==after['center_dim']==(1 if expected_pair is None else 2)
    row=dict(label=label,support_rank=after['support_rank'],active_output_rank=int(round(np.trace(o['p']).real)),
             commutant_dimension=after['comm_dim'],center_dimension=after['center_dim'],
             density_transport_residual=rr,compressed_formation_transport_residual=ar,
             cluster_ranks=after['cluster_ranks'],source_mass=float(o['msel']),
             comm_singular_values_before=before['comm_singular_values'],
             comm_singular_values_after=after['comm_singular_values'])
    if expected_pair is None:
        assert before['projector'] is None and after['projector'] is None
        row['pair_selected']=False
    else:
        qi=before['projector'];qo=after['projector'];assert qi is not None and qo is not None
        ir=float(np.linalg.norm(qi-expected_pair));pr=float(np.linalg.norm(qo-v@qi@v.conj().T))
        centerres=max(float(np.linalg.norm(qo@after[k]-after[k]@qo)) for k in ['r','a'])
        assert max(ir,pr,centerres)<1e-10
        ei=float(np.trace(qi@before['r']).real);eo=float(np.trace(qo@after['r']).real)
        assert abs(ei-eo)<1e-10
        row.update(pair_selected=True,input_projector_residual=ir,projector_transport_residual=pr,
                   reducing_commutator_residual=centerres,pair_energy_before=ei,pair_energy_after=eo,
                   total_energy=float(np.trace(after['r']).real))
    rows.append(row);return o

f=arr(F);w=arr(W);y=arr(Y);p=np.eye(3);k=-p;pair=np.diag([1.,1.,0.])
o=run('unique_joint_block',k,f,w,y,p,pair,2)
run('actual_successor',o['k'],o['f'],o['w'],o['y'],o['p'],o['t4']@pair@o['t4'].conj().T,2)
run('nonzero_bridge',k,f,arr(WB),y,p,None,1)
run('isotropic_R_extra_F',k,arr(FI),arr(WI),y,p,pair,5)
f4=np.zeros((4,4),complex);f4[:3,:3]=f
w4=np.zeros((4,4),complex);w4[:3,:3]=w
p4=np.diag([1.,1.,1.,0.]);pair4=np.diag([1.,1.,0.,0.]);k4=-np.eye(4);y4=arr(Y4)
run('seed_joint_block',k4,f4,w4,y4,p4,pair4,2)
assert rows[-1]['active_output_rank']==4
rng=np.random.default_rng(20261115);g=audit.complex_unitary(rng,4);conj=lambda a:g@a@g.conj().T
run('seed_complex_gauge',conj(k4),conj(f4),conj(w4),conj(y4),conj(p4),conj(pair4),2)
assert rows[-1]['active_output_rank']==4
gauge=abs(rows[-1]['pair_energy_after']-rows[-2]['pair_energy_after']);assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261115,
            tolerance=1e-10,sqrt_cutoff=1e-12,commutant_rank_cutoff=1e-10,spectral_cluster=1e-8,
            symbolic_dimensions=symbolic,exact_positive_minors=minors,exact_pair_energy='3/2',
            exact_total_energy='51/10',exact_isotropic_pair_energy='6/7',
            gauge_pair_energy_residual=gauge,cases=rows,
            scope='Unique minimal central rank2 block of joint R,QFQ algebra is a conditional transported selector. Nonzero bridge removes it; no autonomous full BFG pair or physical locality claimed.')
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
```

## Vollständige lokale Ausgabe

```json
{
  "status": "PASS",
  "calls": 6,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261115,
  "tolerance": 1e-10,
  "sqrt_cutoff": 1e-12,
  "commutant_rank_cutoff": 1e-10,
  "spectral_cluster": 1e-08,
  "symbolic_dimensions": [
    {
      "label": "pair",
      "algebra_dimension": 5,
      "commutant_dimension": 2,
      "center_dimension": 2
    },
    {
      "label": "bridge",
      "algebra_dimension": 9,
      "commutant_dimension": 1,
      "center_dimension": 1
    },
    {
      "label": "isotropic",
      "algebra_dimension": 2,
      "commutant_dimension": 5,
      "center_dimension": 2
    }
  ],
  "exact_positive_minors": {
    "W": [
      "3/10",
      "2/25",
      "4/125"
    ],
    "W_bridge": [
      "3/10",
      "2/25",
      "3197/100000"
    ],
    "Y": [
      "1/4",
      "433/5000",
      "19239/500000"
    ],
    "I-Y": [
      "3/4",
      "2433/5000",
      "133061/500000"
    ],
    "Y4": [
      "1/4",
      "433/5000",
      "19239/500000",
      "2082897/100000000"
    ],
    "I-Y4": [
      "3/4",
      "2433/5000",
      "133061/500000",
      "11851897/100000000"
    ]
  },
  "exact_pair_energy": "3/2",
  "exact_total_energy": "51/10",
  "exact_isotropic_pair_energy": "6/7",
  "gauge_pair_energy_residual": 1.1102230246251565e-15,
  "cases": [
    {
      "label": "unique_joint_block",
      "support_rank": 3,
      "active_output_rank": 3,
      "commutant_dimension": 2,
      "center_dimension": 2,
      "density_transport_residual": 3.1615462657659624e-15,
      "compressed_formation_transport_residual": 7.242024871923129e-15,
      "cluster_ranks": [
        1,
        2
      ],
      "source_mass": 1.0000000000000004,
      "comm_singular_values_before": [
        8.657911395242785,
        8.657911395242785,
        5.547122702097472,
        5.547122702097471,
        3.157530680769389,
        3.134232188726658,
        0.38286889028713694,
        1.123398907392673e-16,
        0.0
      ],
      "comm_singular_values_after": [
        8.65791139524278,
        8.65791139524278,
        5.547122702097462,
        5.547122702097462,
        3.15753068076939,
        3.134232188726661,
        0.3828688902871357,
        2.089652157353527e-15,
        3.1489425938217894e-17
      ],
      "pair_selected": true,
      "input_projector_residual": 2.22118482934829e-16,
      "projector_transport_residual": 4.53662527306456e-16,
      "reducing_commutator_residual": 1.8222544942413647e-15,
      "pair_energy_before": 1.5000000000000002,
      "pair_energy_after": 1.4999999999999993,
      "total_energy": 5.099999999999995
    },
    {
      "label": "actual_successor",
      "support_rank": 3,
      "active_output_rank": 3,
      "commutant_dimension": 2,
      "center_dimension": 2,
      "density_transport_residual": 4.0313320186135884e-15,
      "compressed_formation_transport_residual": 6.583163827566449e-15,
      "cluster_ranks": [
        2,
        1
      ],
      "source_mass": 1.0,
      "comm_singular_values_before": [
        8.65791139524278,
        8.65791139524278,
        5.547122702097462,
        5.547122702097462,
        3.15753068076939,
        3.134232188726661,
        0.3828688902871357,
        2.089652157353527e-15,
        3.1489425938217894e-17
      ],
      "comm_singular_values_after": [
        8.657911395242774,
        8.657911395242769,
        5.547122702097459,
        5.547122702097458,
        3.1575306807693893,
        3.134232188726659,
        0.38286889028713716,
        1.1850776772815247e-15,
        4.2734809005268815e-16
      ],
      "pair_selected": true,
      "input_projector_residual": 5.310520964736449e-16,
      "projector_transport_residual": 7.053201766002355e-16,
      "reducing_commutator_residual": 4.2812430460893755e-15,
      "pair_energy_before": 1.4999999999999993,
      "pair_energy_after": 1.5000000000000004,
      "total_energy": 5.099999999999995
    },
    {
      "label": "nonzero_bridge",
      "support_rank": 3,
      "active_output_rank": 3,
      "commutant_dimension": 1,
      "center_dimension": 1,
      "density_transport_residual": 4.269449128421432e-15,
      "compressed_formation_transport_residual": 7.12102275405283e-15,
      "cluster_ranks": [],
      "source_mass": 1.0000000000000004,
      "comm_singular_values_before": [
        8.658119517276955,
        8.657941812450145,
        5.547213150886133,
        5.5472125756325115,
        3.157657211492775,
        3.1343608380710606,
        0.38387300097770266,
        0.04789036176844534,
        7.63093075591976e-16
      ],
      "comm_singular_values_after": [
        8.658119517276951,
        8.657941812450138,
        5.547213150886132,
        5.547212575632506,
        3.1576572114927774,
        3.134360838071063,
        0.3838730009777011,
        0.0478903617684462,
        3.833836597246023e-16
      ],
      "pair_selected": false
    },
    {
      "label": "isotropic_R_extra_F",
      "support_rank": 3,
      "active_output_rank": 3,
      "commutant_dimension": 5,
      "center_dimension": 2,
      "density_transport_residual": 3.528169134584992e-16,
      "compressed_formation_transport_residual": 1.3720423550828537e-15,
      "cluster_ranks": [
        2,
        1
      ],
      "source_mass": 1.0000000000000002,
      "comm_singular_values_before": [
        1.9999999999999998,
        1.9999999999999998,
        1.9999999999999998,
        1.9999999999999998,
        0.0,
        0.0,
        0.0,
        0.0,
        0.0
      ],
      "comm_singular_values_after": [
        1.9999999999999998,
        1.9999999999999993,
        1.9999999999999984,
        1.9999999999999984,
        1.4386866943924374e-15,
        1.4226293621688087e-15,
        3.477229495919885e-16,
        1.724169449917548e-16,
        7.587959231199765e-17
      ],
      "pair_selected": true,
      "input_projector_residual": 0.0,
      "projector_transport_residual": 9.778679471283594e-16,
      "reducing_commutator_residual": 9.294648364900157e-16,
      "pair_energy_before": 0.8571428571428571,
      "pair_energy_after": 0.8571428571428568,
      "total_energy": 1.2857142857142854
    },
    {
      "label": "seed_joint_block",
      "support_rank": 3,
      "active_output_rank": 4,
      "commutant_dimension": 2,
      "center_dimension": 2,
      "density_transport_residual": 2.8419660691575563e-15,
      "compressed_formation_transport_residual": 4.837892018459422e-15,
      "cluster_ranks": [
        1,
        2
      ],
      "source_mass": 0.9999999999999999,
      "comm_singular_values_before": [
        8.657911395242785,
        8.657911395242785,
        5.547122702097472,
        5.547122702097471,
        3.157530680769389,
        3.134232188726658,
        0.38286889028713694,
        1.123398907392673e-16,
        0.0
      ],
      "comm_singular_values_after": [
        8.657911395242788,
        8.657911395242786,
        5.547122702097474,
        5.547122702097472,
        3.157530680769388,
        3.1342321887266587,
        0.3828688902871382,
        6.786555866177162e-16,
        4.617222478567233e-17
      ],
      "pair_selected": true,
      "input_projector_residual": 2.22118482934829e-16,
      "projector_transport_residual": 8.99028683335918e-16,
      "reducing_commutator_residual": 3.128519562116902e-15,
      "pair_energy_before": 1.5000000000000002,
      "pair_energy_after": 1.500000000000003,
      "total_energy": 5.100000000000004
    },
    {
      "label": "seed_complex_gauge",
      "support_rank": 3,
      "active_output_rank": 4,
      "commutant_dimension": 2,
      "center_dimension": 2,
      "density_transport_residual": 6.810899958266713e-15,
      "compressed_formation_transport_residual": 1.2874626699109445e-14,
      "cluster_ranks": [
        1,
        2
      ],
      "source_mass": 0.9999999999999997,
      "comm_singular_values_before": [
        8.657911395242772,
        8.657911395242767,
        5.547122702097462,
        5.547122702097462,
        3.157530680769388,
        3.134232188726654,
        0.38286889028713544,
        2.867195479737769e-15,
        6.935536474822385e-17
      ],
      "comm_singular_values_after": [
        8.657911395242785,
        8.65791139524278,
        5.54712270209747,
        5.547122702097464,
        3.157530680769388,
        3.134232188726658,
        0.3828688902871377,
        3.681867670543698e-15,
        1.8867745190415914e-16
      ],
      "pair_selected": true,
      "input_projector_residual": 1.5562997970466313e-15,
      "projector_transport_residual": 1.9572532324690595e-15,
      "reducing_commutator_residual": 5.0241293788344296e-15,
      "pair_energy_before": 1.4999999999999991,
      "pair_energy_after": 1.500000000000002,
      "total_energy": 5.099999999999999
    }
  ],
  "scope": "Unique minimal central rank2 block of joint R,QFQ algebra is a conditional transported selector. Nonzero bridge removes it; no autonomous full BFG pair or physical locality claimed."
}
```

Sechs neue Quellaufrufe sind lokale Evidenz. Die bestehenden grünen GitHub-Läufe am Runde64-Commit führen diese neue eingebettete Reproduktion nicht automatisch aus.
