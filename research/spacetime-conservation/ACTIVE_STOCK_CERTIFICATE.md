# Rationales Zertifikat – kombinierter aktiver Bestand

Reproduktion: Python-Datei aus dem folgenden Codeblock im Repository-Wurzelverzeichnis ausführen; vorhandene Auditabhängigkeiten genügen. Originalupdate wird ausschließlich importiert. Die Näherungserzeugung wird vollständig durch die anschließenden exakten Bruchtests geprüft. Ausgabe des frisch erfolgreichen Laufs:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "alpha": "1/10",
  "H": [
    [
      "1",
      "0",
      "18/125"
    ],
    [
      "0",
      "13/9",
      "1/5"
    ],
    [
      "18/125",
      "1/5",
      "61/625"
    ]
  ],
  "Q": [
    [
      "5343558218181183583791637149542206871659090807511/5000000000000000000000000000000000000000000000000",
      "84386358080972687166970608861337399720610445273/1250000000000000000000000000000000000000000000000",
      "-52440823149311122733465607222640732613486950608539/100000000000000000000000000000000000000000000000000"
    ],
    [
      "84386358080972687166970608861337399720610445273/1250000000000000000000000000000000000000000000000",
      "44923780947022630394381483738120505954677769322593/50000000000000000000000000000000000000000000000000",
      "-3249896174905900898283540613673097549849593393519/6250000000000000000000000000000000000000000000000"
    ],
    [
      "-52440823149311122733465607222640732613486950608539/100000000000000000000000000000000000000000000000000",
      "-3249896174905900898283540613673097549849593393519/6250000000000000000000000000000000000000000000000",
      "2224382923874851696898291968408817753344394891637/500000000000000000000000000000000000000000000000"
    ]
  ],
  "inverse_sqrt_error_bound": "1.3839983778025934512e-48",
  "stock_error_bound": "3.6475509733060360780e-46",
  "certified_lower": "6599430384017/1000000000000000",
  "certified_upper": "6599430384019/1000000000000000",
  "center": "0.0065994303840177635158542230734271716821124427581797",
  "source_calls": 2,
  "source_defect": 0.006599430384018223,
  "gauge_defect": 0.006599430384016225,
  "gauge_residual": 1.9984014443252818e-15,
  "balance_residual": 4.172009959724221e-16,
  "seed_formation_gain": 1.2568997908165365
}
```

```python
import json, sys
from pathlib import Path
import sympy as s
import mpmath as mp
import numpy as np
sys.path.insert(0, 'research/spacetime-conservation')
import audit
R=s.Rational
P=s.diag(1,1,0); K=-s.diag(1,2,3)
F=s.diag(1,R(21,50),0)
Y=s.Matrix([[R(1,4),0,R(1,10)],[0,R(1,2),R(1,10)],[R(1,10),R(1,10),R(1,2)]])
G=s.eye(3)+Y
ac=s.diag(R(4,5),R(2,3),0)
ab=3*ac*Y
H=ac.T*ac+ab.T*ab
assert H.det()>0
assert s.trace(F*s.diag(R(4,5),R(2,3),0)*Y*P*Y)/s.trace(F*s.diag(R(4,5),R(2,3),0)) == R(1,9)
mp.mp.dps=100
hm=mp.matrix([[mp.mpf(str(H[i,j].p))/mp.mpf(str(H[i,j].q)) for j in range(3)] for i in range(3)])
e,v=mp.eigsy(hm)
qm=v*mp.diag([1/mp.sqrt(x) for x in e])*v.T
Q=s.Matrix(3,3,lambda i,j:R(str(mp.nstr(qm[min(i,j),max(i,j)],50))))
assert all((Q-s.eye(3)/10)[:i,:i].det()>0 for i in (1,2,3))
res=Q*Q-H.inv()
absum=lambda m:sum(abs(x) for x in m)
errq=10*absum(res)
bound=6*(sum(x*x for x in ac)+sum(x*x for x in ab))*(2*absum(Q)*errq+errq**2)
Bq=ac*Q*P*Q*ac.T+ab*Q*P*Q*ab.T
center=s.trace(K*(Bq-P))
lo=R(6599430384017,10**15); hi=R(6599430384019,10**15)
assert center-bound>lo and center+bound<hi
assert errq<R(1,10**45) and bound<R(1,10**43)
update=audit.load_update()
arr=lambda m:np.array(m,float)
def run(k,f,w,y,p):
    out=update(k,f,w,y,p)
    assert out['terminal'] is None
    d=float(np.trace(out['p']@out['k']+out['f']).real-np.trace(p@k+f).real)
    u=out['u']; ss=out['t4']@out['t4'].conj().T
    b=sum(t@ss@t.conj().T for t in (u[:3],u[3:]))
    predicted=float(np.trace(k@(b-p)).real)
    assert abs(d-predicted)<1e-12 and abs(d-float(center))<1e-12
    return out,d,abs(d-predicted)
out,d,residual=run(arr(K),arr(F),arr(P)/2,arr(Y),arr(P))
rng=np.random.default_rng(20261025); gauge=audit.complex_unitary(rng,3)
conj=lambda m:gauge@arr(m)@gauge.conj().T
gout,gd,gres=run(conj(K),conj(F),conj(P)/2,conj(Y),conj(P))
assert abs(d-gd)<1e-12
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,alpha='1/10',H=[[str(x) for x in row] for row in H.tolist()],Q=[[str(x) for x in row] for row in Q.tolist()],inverse_sqrt_error_bound=str(s.N(errq,20)),stock_error_bound=str(s.N(bound,20)),certified_lower=str(lo),certified_upper=str(hi),center=str(s.N(center,50)),source_calls=2,source_defect=d,gauge_defect=gd,gauge_residual=abs(d-gd),balance_residual=max(residual,gres),seed_formation_gain=float(np.trace(out['f']).real-np.trace(arr(F)).real))

print(json.dumps(result,indent=2))

```
