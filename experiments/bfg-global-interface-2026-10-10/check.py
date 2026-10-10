"""Synthetic independent feasibility and canonical spectral controls."""
import json,random
from pathlib import Path
import numpy as np
import sympy as s
from fractions import Fraction as F
from core import System
rng=random.Random(74)
t=np.arange(11)*.01;knots=[0,5,10];outer=System(t,knots,'outer');inner=System(t,knots,'inner')
for _ in range(40):
 a=F(str(rng.uniform(-1,1)));v=F(str(rng.uniform(-1,1)));q0=F(str(rng.uniform(-1,1)))
 tt=outer.t;q=[q0+v*z+a*z*z/2 for z in tt];w=[v+a*z for z in tt]
 xx=[q[i] for i in knots]+[w[i] for i in knots]
 for system in [outer,inner]:
  b,_=system.rhs(q,w,F('.001'),F('.002'),F(2))
  assert all(sum((c*xx[j] for j,c in row),F(0))<=bb for row,bb in zip(system.rows,b))
# Four-point local-pass/global-fail example; arbitrary finite velocity boxes.
sy=System([0,1,2,3],[0,1,2,3],'outer');q=[F(0),F(0),F(1),F(1)];w=[F(0)]*4
res=sy.solve(q,w,F(0),F(100),F(1));cert=sy.outer_certificate(res,q,w,F(0),F(100),F(1));assert res.success and res.x[-1]<1e-8 and not(cert and cert['positive'])
# The deliberately weaker linear relaxation passes this impossible exact path.
si=System([0,1,2,3],[0,1,2,3],'inner');ri=si.solve(q,w,F(0),F(100),F(1));assert not ri.success
bad=System([0,1],[0,1],'outer');bq=[F(0),F(10)];bw=[F(0),F(0)]
br=bad.solve(bq,bw,F(0),F('.001'),F(1));bc=bad.outer_certificate(br,bq,bw,F(0),F('.001'),F(1));assert bc and bc['positive']
x,y,f1,f2=s.symbols('x y f1 f2',positive=True);LC=f1/(1+x)+f2/(1+y);LB=f1*x*x/(1+x)+f2*y*y/(1+y);alpha=LB/(LC+LB)
g=s.Matrix([(alpha+(1-alpha)*z*z)/(1+z)**2 for z in [x,y]]);J=g.jacobian([x,y])
for i,j in [(0,1),(1,0)]:
 target=(1-[x,y][i]**2)/(1+[x,y][i])**2*s.diff(alpha,[x,y][j]);assert s.simplify(J[i,j]-target)==0
jfun=s.lambdify((x,y,f1,f2),J,'numpy');gfun=s.lambdify((x,y,f1,f2),g,'numpy');maxerr=0;mindisc=1e10;minoff=1e10;maxsvd=0
for _ in range(400):
 z=np.array([rng.uniform(.02,.95),rng.uniform(.02,.95)]);weights=[rng.uniform(.1,3),rng.uniform(.1,3)];jj=np.asarray(jfun(*z,*weights));
 assert jj[0,1]>0 and jj[1,0]>0
 disc=(jj[0,0]-jj[1,1])**2+4*jj[0,1]*jj[1,0];assert disc>0
 dh=1e-6;fd=np.column_stack([(np.asarray(gfun(*(z+dh*np.eye(2)[i]),*weights)).ravel()-np.asarray(gfun(*(z-dh*np.eye(2)[i]),*weights)).ravel())/(2*dh) for i in range(2)])
 maxerr=max(maxerr,float(abs(fd-jj).max()));mindisc=min(mindisc,float(disc));minoff=min(minoff,float(min(jj[0,1],jj[1,0])))
 lc=sum(np.asarray(weights)/(1+z));lb=sum(np.asarray(weights)*z*z/(1+z));aa=lb/(lc+lb)
 ambient=np.vstack([np.diag(np.sqrt(aa)/(1+z)),np.diag(np.sqrt(1-aa)*z/(1+z))])
 eig=np.linalg.svd(ambient,compute_uv=False)**2;gg=np.asarray(gfun(*z,*weights)).ravel();maxsvd=max(maxsvd,float(abs(np.sort(eig)-np.sort(gg)).max()))
assert maxerr<1e-7
xx=s.symbols('xx',positive=True);f=2*xx**2/((1+xx)**2*(1+xx**2));lt=2*xx*(1-xx)/((1+xx)**3*(1+xx**2))
assert s.simplify(s.diff(f,xx)/lt-2*(1+xx+xx**2)/(1+xx**2))==0
out={'status':'passed','quadratic_outer_inner_controls':40,'canonical_controls':400,'max_tangent_fd_error':maxerr,'min_discriminant':mindisc,'min_offdiagonal':minoff,
'global_fourpoint_outer_passes_inner_fails':True,'max_ambient_svd_error':maxsvd,'symmetric_eigenvalue_ratio_identity':True,'known_impossible_exact_certificate':bc}
Path(__file__).with_name('controls.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='global_fourpoint_exact_certificate'}))
