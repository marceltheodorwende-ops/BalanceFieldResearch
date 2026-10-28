# Runde63: Witness-Zweimodenträger und Pauli-Kegel

Aus Repositorywurzel mit bestehenden audit-Abhängigkeiten, NumPy und SymPy ausführen. Ein frischer lokaler Lauf PASS, fünf Originalereignisse, keine Fehlvorläufe/Korrektur; empirisches main wird nicht ausgeführt. Rang1-Nullkontrolle verwendet das gegebene volle Zweimoden-Umgebungspaar, keine intrinsische Rang2-Supportbehauptung. Symbolische Identitäten und zusätzliche physikalische Vergleichskriterien getrennt in WITNESS_TWO_MODE_CARRIER.md.

```python
import sys,json
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
pauli=[s.eye(2),s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
t,x,y,z=s.symbols('t x y z',real=True);X=sum((v*a for v,a in zip([t,x,y,z],pauli)),s.zeros(2))/2
assert s.expand(X.det()-(t*t-x*x-y*y-z*z)/4)==0
assert pauli[1]*pauli[2]-pauli[2]*pauli[1]==2*s.I*pauli[3]
A=s.diag(s.sqrt(2),1/s.sqrt(2));boost=A*(s.eye(2)/2)*A.T
assert A.det()==1 and boost.det()==s.Rational(1,4) and s.trace(boost)==s.Rational(5,4)
ps=[np.array(a.tolist(),complex) for a in pauli]
def root(a):
    e,u=np.linalg.eigh((a+a.conj().T)/2);assert min(e)>-1e-10
    return (u*np.sqrt(np.where(e>1e-12,e,0)))@u.conj().T
def rho(f,w):
    sf=root(f);return sf@w@sf
coords=lambda a:np.array([np.trace(b@a).real for b in ps])
update=audit.load_update();calls=0
def run(label,k,f,w,y,p,frame):
    global calls
    r0=rho(f,w);a0=frame.conj().T@r0@frame;c0=coords(a0)
    o=update(k,f,w,y,p);calls+=1;assert o['terminal'] is None
    v=o['t4']@p;zf=v@frame;r1=rho(o['f'],o['w']);a1=zf.conj().T@r1@zf;c1=coords(a1)
    transport=float(np.linalg.norm(r1-v@r0@v.conj().T));support=float(np.linalg.norm(r1-zf@a1@zf.conj().T))
    coord=float(np.max(np.abs(c1-c0)));det0=float(np.linalg.det(a0).real);det1=float(np.linalg.det(a1).real)
    mink=float(c1[0]**2-c1[1:]@c1[1:]);assert max(transport,support,coord,abs(mink-4*det1),abs(det1-det0))<1e-10
    assert c1[0]>0 and mink>-1e-10
    row=dict(label=label,active_output_rank=int(round(np.trace(o['p']).real)),density_rank=int(sum(np.linalg.eigvalsh(r1)>1e-10)),source_transport_residual=transport,density_support_residual=support,coordinates_before=c0.tolist(),coordinates_after=c1.tolist(),coordinate_residual=coord,determinant_before=det0,determinant_after=det1,minkowski_quadratic_form=mink)
    return o,zf,row
rows=[];ni=np.eye(2);f=np.diag([1.,3.]);yy=np.diag([.2,.3])
for label,w in [('full_positive',np.array([[.5,.25],[.25,.5]])),('full_null',np.ones((2,2))/2)]:
    _,_,r=run(label,-ni,f,w,yy,ni,ni);rows.append(r)
p=np.diag([1.,1.,0.]);f=np.diag([1.,.42,0.]);w=np.array([[.6,.1j,0],[-.1j,.4,0],[0,0,0]],complex)
yy=np.array([[.25,0,.1],[0,.5,.1],[.1,.1,.5]]);k=-np.diag([1.,2.,3.]);frame=np.eye(3)[:,:2]
o,zf,r=run('seed_pair',k,f,w,yy,p,frame);rows.append(r);assert r['active_output_rank']==3 and r['density_rank']==2
_,_,r=run('retained_pair',o['k'],o['f'],o['w'],o['y'],o['p'],zf);rows.append(r)
rng=np.random.default_rng(20261113);g=audit.complex_unitary(rng,3);conj=lambda a:g@a@g.conj().T
_,_,r=run('seed_pair_gauge',conj(k),conj(f),conj(w),conj(yy),conj(p),g@frame);rows.append(r)
gauge=float(np.max(np.abs(np.array(rows[-1]['coordinates_after'])-rows[2]['coordinates_after'])));assert gauge<1e-10
result=dict(status='PASS',calls=calls,source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261113,sqrt_cutoff=1e-12,symbolic_determinant='(t^2-x^2-y^2-z^2)/4',pauli_xy_commutator='2 i sigma_z',boost_energy_before='1',boost_energy_after='5/4',boost_determinant_before_after='1/4',gauge_coordinate_residual=gauge,cases=rows,scope='Rank2 positive witness-formation support is a covariant transported two-mode carrier, not a derived physical local space. Pauli cone is exact; direct Pauli momentum identification fails commuting-translation criterion.')

print(json.dumps(result,indent=2))

```

Rohdaten:

```json
{
  "status": "PASS",
  "calls": 5,
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "seed": 20261113,
  "sqrt_cutoff": 1e-12,
  "symbolic_determinant": "(t^2-x^2-y^2-z^2)/4",
  "pauli_xy_commutator": "2 i sigma_z",
  "boost_energy_before": "1",
  "boost_energy_after": "5/4",
  "boost_determinant_before_after": "1/4",
  "gauge_coordinate_residual": 1.2212453270876722e-15,
  "cases": [
    {
      "label": "full_positive",
      "active_output_rank": 2,
      "density_rank": 2,
      "source_transport_residual": 0,
      "density_support_residual": 0,
      "coordinates_before": [
        1.9999999999999998,
        0.8660254037844386,
        0,
        -0.9999999999999998
      ],
      "coordinates_after": [
        1.9999999999999998,
        0.8660254037844386,
        0,
        -0.9999999999999998
      ],
      "coordinate_residual": 0,
      "determinant_before": 0.5624999999999999,
      "determinant_after": 0.5624999999999999,
      "minkowski_quadratic_form": 2.2499999999999996
    },
    {
      "label": "full_null",
      "active_output_rank": 2,
      "density_rank": 1,
      "source_transport_residual": 0,
      "density_support_residual": 0,
      "coordinates_before": [
        1.9999999999999998,
        1.7320508075688772,
        0,
        -0.9999999999999998
      ],
      "coordinates_after": [
        1.9999999999999998,
        1.7320508075688772,
        0,
        -0.9999999999999998
      ],
      "coordinate_residual": 0,
      "determinant_before": 0,
      "determinant_after": 0,
      "minkowski_quadratic_form": 0
    },
    {
      "label": "seed_pair",
      "active_output_rank": 3,
      "density_rank": 2,
      "source_transport_residual": 6.335708625836367e-16,
      "density_support_residual": 7.038471360066578e-16,
      "coordinates_before": [
        0.7679999999999999,
        0,
        -0.1296148139681572,
        0.43200000000000005
      ],
      "coordinates_after": [
        0.7680000000000015,
        7.99996883980906e-16,
        -0.1296148139681575,
        0.4320000000000005
      ],
      "coordinate_residual": 1.5543122344752192e-15,
      "determinant_before": 0.09659999999999996,
      "determinant_after": 0.09660000000000044,
      "minkowski_quadratic_form": 0.38640000000000174
    },
    {
      "label": "retained_pair",
      "active_output_rank": 3,
      "density_rank": 2,
      "source_transport_residual": 1.672631615674469e-15,
      "density_support_residual": 2.33302869752235e-15,
      "coordinates_before": [
        0.7680000000000015,
        7.99996883980906e-16,
        -0.1296148139681575,
        0.4320000000000005
      ],
      "coordinates_after": [
        0.7680000000000012,
        1.2349590311497613e-15,
        -0.1296148139681576,
        0.4319999999999996
      ],
      "coordinate_residual": 8.881784197001252e-16,
      "determinant_before": 0.09660000000000044,
      "determinant_after": 0.09660000000000052,
      "minkowski_quadratic_form": 0.3864000000000022
    },
    {
      "label": "seed_pair_gauge",
      "active_output_rank": 3,
      "density_rank": 2,
      "source_transport_residual": 3.9495156629567436e-16,
      "density_support_residual": 8.471473480114719e-16,
      "coordinates_before": [
        0.768,
        5.169475958410885e-16,
        -0.12961481396815772,
        0.43199999999999955
      ],
      "coordinates_after": [
        0.7680000000000002,
        1.1657341758564144e-15,
        -0.129614813968158,
        0.4319999999999997
      ],
      "coordinate_residual": 6.487865800153259e-16,
      "determinant_before": 0.09660000000000005,
      "determinant_after": 0.0966000000000001,
      "minkowski_quadratic_form": 0.3864000000000004
    }
  ],
  "scope": "Rank2 positive witness-formation support is a covariant transported two-mode carrier, not a derived physical local space. Pauli cone is exact; direct Pauli momentum identification fails commuting-translation criterion."
}
```
