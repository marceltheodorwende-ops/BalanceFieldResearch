# Zertifikat gleicher Bestände und gleicher Seeds

Vom Repository-Wurzelverzeichnis als Python-Datei ausführen. Die rationale Q_r-Matrix ist hier vollständig eingebettet; keine lokale Datei aus Runde40 wird benötigt. Importiert ausschließlich den gepinnten Originalupdate. Herleitung und exakte Zustandsdefinition in SEED_STOCK_CLOSURE.md.

```python
import json,sys
from pathlib import Path
import numpy as np
import sympy as s
sys.path.insert(0,'research/spacetime-conservation')
import audit
R=s.Rational
P=s.diag(1,1,0)
Y=s.Matrix([[R(1,4),0,R(1,10)],[0,R(1,2),R(1,10)],[R(1,10),R(1,10),R(1,2)]])
F=s.diag(1,R(21,50),0)
ac=s.diag(R(4,5),R(2,3),0);ab=3*ac*Y
H=ac.T*ac+ab.T*ab
Q=s.Matrix([[R(x) for x in row] for row in [["5343558218181183583791637149542206871659090807511/5000000000000000000000000000000000000000000000000","84386358080972687166970608861337399720610445273/1250000000000000000000000000000000000000000000000","-52440823149311122733465607222640732613486950608539/100000000000000000000000000000000000000000000000000"],["84386358080972687166970608861337399720610445273/1250000000000000000000000000000000000000000000000","44923780947022630394381483738120505954677769322593/50000000000000000000000000000000000000000000000000","-3249896174905900898283540613673097549849593393519/6250000000000000000000000000000000000000000000000"],["-52440823149311122733465607222640732613486950608539/100000000000000000000000000000000000000000000000000","-3249896174905900898283540613673097549849593393519/6250000000000000000000000000000000000000000000000","2224382923874851696898291968408817753344394891637/500000000000000000000000000000000000000000000000"]]])
assert all((Q-s.eye(3)/10)[:i,:i].det()>0 for i in (1,2,3))
abssum=lambda m:sum(abs(x) for x in m)
eq=10*abssum(Q*Q-H.inv())
eb=(sum(x*x for x in ac)+sum(x*x for x in ab))*(2*abssum(Q)*eq+eq**2)
Bq=ac*Q*P*Q*ac.T+ab*Q*P*Q*ab.T
D=ac*H.inv()*ac.T+ab*H.inv()*ab.T
assert s.trace(D)==3 and P*D*P==D
Z0=D-R(3,2)*P;Xq=Bq-P
wq=Xq[0,0]*Z0[0,1]-Xq[0,1]*Z0[0,0]
ew=(abs(Z0[0,1])+abs(Z0[0,0]))*eb
lower=R(s.floor(wq*10**15)-1,10**15);upper=R(s.floor(wq*10**15)+2,10**15)
assert lower<wq-ew and wq+ew<upper
assert lower*upper>0 and abs(wq)>R(1,10**8)
Zq=D-Bq-P/2
z1=(Zq[0,0]-Zq[1,1])/2;z2=Zq[0,1]
Lq=s.Matrix([[z2,-z1,0],[-z1,-z2,0],[0,0,0]])
arr=lambda m:np.array(m,float)
update=audit.load_update();cases=[];outs=[]
for sign in (-1,1):
    k=-2*np.eye(3)+sign*arr(Lq)
    out=update(k,arr(F),arr(P)/2,arr(Y),arr(P));assert out['terminal'] is None
    msel=out['v'].conj().T@arr(P)@out['v'];ee,ev=np.linalg.eigh(np.eye(3)-msel);z=ev[:,ee>.5]
    seed=float((z.conj().T@out['k']@z)[0,0].real)
    gain=float(np.trace(out['f']).real-np.trace(arr(F)).real)
    delta=float(np.trace(out['p']@out['k']+out['f']).real-np.trace(arr(P)@k+arr(F)).real)
    assert abs(seed+2)<1e-12 and abs(gain-2)<1e-12
    assert abs(delta-sign*2*float(wq))<1e-12
    cases.append(dict(sign=sign,active_input=float(np.trace(arr(P)@k)),ambient_input=float(np.trace(k)),seed=seed,formation_gain=gain,total_defect=delta,active_output=float(np.trace(out['p']@out['k']).real)))
    outs.append(out)
field_res=max(float(np.linalg.norm(outs[0][key]-outs[1][key])) for key in ('f','w','y','p'))
assert field_res<1e-12 and cases[0]['active_input']==cases[1]['active_input']
result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,D=[[str(x) for x in row] for row in D.tolist()],Q=[[str(x) for x in row] for row in Q.tolist()],wedge_lower=str(lower),wedge_upper=str(upper),wedge_approx=str(s.N(wq,35)),wedge_error_bound=str(s.N(ew,20)),L_approx=arr(Lq).tolist(),source_calls=2,cases=cases,nonkernel_field_residual=field_res,scope='Same input kernel traces, geometry and seed amount; different output stock. Exact algebraic construction with rational nonzero-wedge certificate.')

print(json.dumps(result,indent=2))

```

Frische Ausgabe:

```json
{
  "status": "PASS",
  "source_blob": "ff8b0a7ec922ccfeacae5bc9ce6c104b79286498",
  "D": [
    [
      "4369/2497",
      "1020/2497",
      "0"
    ],
    [
      "1020/2497",
      "3122/2497",
      "0"
    ],
    [
      "0",
      "0",
      "0"
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
  "wedge_lower": "6541042265093/1000000000000000",
  "wedge_upper": "817630283137/125000000000000",
  "wedge_approx": "0.0065410422650943530038405032291251828",
  "wedge_error_bound": "4.0013015783129557430e-47",
  "L_approx": [
    [
      0.42388964860156064,
      -0.2431002091834632,
      0
    ],
    [
      -0.2431002091834632,
      -0.42388964860156064,
      0
    ],
    [
      0,
      0,
      0
    ]
  ],
  "source_calls": 2,
  "cases": [
    {
      "sign": -1,
      "active_input": -4,
      "ambient_input": -6,
      "seed": -1.9999999999999996,
      "formation_gain": 2,
      "total_defect": -0.01308208453018711,
      "active_output": -6.013082084530187
    },
    {
      "sign": 1,
      "active_input": -4,
      "ambient_input": -6,
      "seed": -1.9999999999999993,
      "formation_gain": 1.9999999999999991,
      "total_defect": 0.013082084530188887,
      "active_output": -5.98691791546981
    }
  ],
  "nonkernel_field_residual": 4.613712248324544e-16,
  "scope": "Same input kernel traces, geometry and seed amount; different output stock. Exact algebraic construction with rational nonzero-wedge certificate."
}
```
