import json
from pathlib import Path
import numpy as np
from experiment import update
rng=np.random.default_rng(4908);records=[];res=[]
for n in (2,3,5):
 Y=np.diag(rng.uniform(.1,.4,n));raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));F=raw@raw.conj().T+np.eye(n)
 ms=[float(np.linalg.norm(Y,2))];ds=[]
 for k in range(4):
  raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));D=(raw+raw.conj().T)/2
  D*=min(np.linalg.eigvalsh(Y))*.1/np.linalg.norm(D,2)
  z=Y+D;assert min(np.linalg.eigvalsh(z))>0 and max(np.linalg.eigvalsh(z))<1
  out=update(np.eye(n),F,np.eye(n)/n,z,np.eye(n));assert out['terminal'] is None
  Y=out['v']@out['y']@out['v'].conj().T
  ds.append(float(np.linalg.norm(D,2)));ms.append(float(np.linalg.norm(Y,2)))
  assert ms[-1]<=.5*(ms[-2]+ds[-1])+1e-12
 lower=2*ms[-1]-ms[0]+sum(ms[1:-1]);assert sum(ds)>=lower-1e-12
 upper=2**(-4)*ms[0]+sum(2**(-(4-j))*d for j,d in enumerate(ds))
 assert ms[-1]<=upper+1e-12
 records.append(dict(n=n,events=4,total_input_norm=sum(ds),telescoping_lower=lower,terminal_norm=ms[-1],convolution_upper=upper))
# Same preparation cost and identical initial state, distinct canonical successors.
z=np.array([.2,.7]);d=np.array([.01,0.]);outs=[]
for sign in (-1,1):
 out=update(np.eye(2),np.diag([1.,2.]),np.eye(2)/2,np.diag(z+sign*d),np.eye(2));outs.append((out['v']@out['y']@out['v'].conj().T).real.diagonal())
gap=float(np.linalg.norm(outs[1]-outs[0]));assert gap>1e-4
# Scalar positive-reserve example: finite budget drains exactly as declared.
y=.05596219;d=.15;B=.6;cost=.15;steps=0
while B>=cost-1e-14:
 x=y+d;y=2*x*x/((1+x)**2*(1+x*x));B-=cost;steps+=1
assert steps==4 and abs(B)<1e-14
vals=[.05596219]
for _ in range(100):
 x=vals[-1]+.15;vals.append(2*x*x/((1+x)**2*(1+x*x)))
m=min(vals);lower=101*m-vals[0];assert 15>=lower and lower>5
result=dict(reserve_control=dict(events=100,minimum_norm=m,total_input=15,required_lower=lower),kind='synthetic mathematics/code controls only',matrix_controls=records,same_cost_opposite_input_successor_gap=gap,scalar_budget_events=steps,scalar_remaining_budget=B,resource_units='abstract; no joule calibration',force_selected=False,holdout_accessed=False)
Path(__file__).with_name('results').joinpath('controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
