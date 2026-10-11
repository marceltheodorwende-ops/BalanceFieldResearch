"""Bounded archived case-47 native boundary diagnostic; does not mutate results."""
import csv,json,time,sys,faulthandler
from pathlib import Path
from fractions import Fraction as F
import core
faulthandler.enable()
r=Path(__file__).resolve().parent
idx=46  # Archived first missing case; stable after completion of all 120 cases.
name=sorted(f'len{l}_cond{c}_1.csv' for l in range(1,6) for c in range(1,4))[idx//8]
N,ew,B=[(N,F(str(ew)),F(B)) for N in [2000,4000] for ew in [.0005,.2] for B in [0,2]][idx%8]
print(json.dumps({'case':idx+1,'file':name,'N':N,'ew':float(ew),'B':int(B),'method':sys.argv[1] if len(sys.argv)>1 else 'highs'}),flush=True)
with (Path('/workspace/bfg-instrument-audit/data')/name).open() as f: rows=list(csv.DictReader(f))
t=[F(x['time']) for x in rows];q=[F(x['angle']) for x in rows];w=[F(x['angular_velocity']) for x in rows]
e,A,_=core.parameters(q[0],w[0],list(map(F,['.236','.330','.426','.518','.607']))[int(name[3])-1],N,ew,B)
base=core.linprog
method=sys.argv[1] if len(sys.argv)>1 else 'highs'
def solver(*args,**kw):kw['method']=method;return base(*args,**kw)
core.linprog=solver
for kind in ['outer','inner']:
 print('build '+kind,flush=True);s=core.System(t,list(range(0,6000,5))+[5999],kind)
 print('native enter '+kind,flush=True);started=time.monotonic();z=s.solve(q,w,e[kind=='outer'],ew,A[kind=='outer'])
 print(json.dumps({'kind':kind,'status':z.status,'success':z.success,'elapsed':time.monotonic()-started}),flush=True)
print('diagnostic completed',flush=True)
