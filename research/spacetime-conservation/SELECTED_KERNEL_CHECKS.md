# Kontrollen der ausgewählten Kernelreduktion

Als Python-Datei vom Repository-Wurzelverzeichnis ausführen; vorhandene Auditabhängigkeiten. Nur Import des gepinnten Originalupdates. Beweis und Geltungsbereiche in SELECTED_KERNEL_QUOTIENT.md.

```python
import json,sys
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
update=audit.load_update()
v=s.Matrix([1,1])/s.sqrt(2);P=v*v.T;Q=s.diag(1,0);L=s.diag(1,-1)
assert P*L*P==s.zeros(2) and Q*L*Q==Q
alpha=s.Rational(1,4)/(1+s.Rational(1,4))
assert alpha==s.Rational(1,5)
assert 2*s.Rational(1,2)**2/((1+s.Rational(1,2))**2*(1+s.Rational(1,2)**2))==s.Rational(8,45)
v=np.ones(2)/np.sqrt(2);p=np.outer(v,v);y=np.diag([.5,2.]);k0=-2*np.eye(2)
outs=[];records=[]
for sign in (-1,1):
    k=k0+sign*np.diag([1.,-1.]);o=update(k,p,p,y,p);assert o['terminal'] is None
    assert abs(o['k'][0,0]-(-2+sign))<1e-12
    assert abs(o['y'][0,0]-8/45)<1e-12
    outs.append(o);records.append(dict(sign=sign,original_active=float(np.trace(p@k)),ambient=float(np.trace(k)),selected=float(k[0,0]),output=float(o['k'][0,0]),alpha=o['alpha'],output_load=float(o['y'][0,0])))
h=np.array([[0,.2],[.2,.4]])
a=update(k0,p,p,y,p);b=update(k0+h,p,p,y,p)
assert a['terminal'] is None and b['terminal'] is None
same=max(float(np.linalg.norm(a[key]-b[key])) for key in ('k','f','w','y','p'))
assert same<1e-12
rng=np.random.default_rng(20261027);n=4
z=audit.complex_unitary(rng,n);p=z[:,:2]@z[:,:2].conj().T
f=p@audit.pos(rng,n)@p;w=p/2;y=np.diag([.2,.4,.7,1.4]);k=-audit.pos(rng,n)
o=update(k,f,w,y,p);random=dict(terminal=o['terminal'])
if o['terminal'] is None:
    ps=o['psel'];e,j=np.linalg.eigh(ps);j=j[:,e>.5];r=j.shape[1];m=len(o['k'])
    yp=j.conj().T@y@j;hp=np.eye(r)+yp;vs=o['v']@np.diag(o['s'])
    zz=j.conj().T@vs@o['k']@vs.conj().T@j;mm=hp@zz@hp
    mu,z=np.linalg.eigh(yp);den=o['alpha']+(1-o['alpha'])*mu[:,None]*mu[None,:]
    rec=z@((z.conj().T@mm@z)/den)@z.conj().T
    rr=float(np.linalg.norm(rec-j.conj().T@k@j))
    ops=[o['u'][:n],o['u'][n:]]
    support=max(float(np.linalg.norm(ps@t-t)) for t in ops)
    unital=float(np.linalg.norm(sum(t.conj().T@ps@t for t in ops)-np.eye(m)))
    assert max(rr,support,unital)<1e-10
    random.update(input_rank=int(round(np.trace(p).real)),selected_rank=r,output_dimension=m,reconstruction_residual=rr,support_residual=support,unital_residual=unital,selected_original_projector_distance=float(np.linalg.norm(ps-p)))
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,calls=5,symbolic=dict(original_PLP='0',selected_QLQ='Q',alpha='1/5',output_load='8/45'),counterexample=records,same_selected_successor_residual=same,random_case=random,scope='Actual selected kernel block suffices across initial Q!=I; original active block can fail. No transported-kernel convention substituted.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "calls": 5,
  "symbolic": {
    "original_PLP": "0",
    "selected_QLQ": "Q",
    "alpha": "1/5",
    "output_load": "8/45"
  },
  "counterexample": [
    {
      "sign": -1,
      "original_active": -1.9999999999999996,
      "ambient": -4,
      "selected": -3,
      "output": -2.9999999999999987,
      "alpha": 0.2,
      "output_load": 0.17777777777777778
    },
    {
      "sign": 1,
      "original_active": -1.9999999999999996,
      "ambient": -4,
      "selected": -1,
      "output": -0.9999999999999996,
      "alpha": 0.2,
      "output_load": 0.17777777777777778
    }
  ],
  "same_selected_successor_residual": 0,
  "random_case": {
    "terminal": null,
    "input_rank": 2,
    "selected_rank": 2,
    "output_dimension": 3,
    "reconstruction_residual": 1.8099701721069553e-14,
    "support_residual": 9.55213790351541e-16,
    "unital_residual": 1.1369878428188828e-15,
    "selected_original_projector_distance": 0.5879532154901501
  },
  "scope": "Actual selected kernel block suffices across initial Q!=I; original active block can fail. No transported-kernel convention substituted."
}
```
