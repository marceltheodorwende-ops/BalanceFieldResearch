from pathlib import Path
import numpy as np, json,csv,hashlib,math
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import pypdfium2 as pdfium

OUT=Path(__file__).resolve().parent.parent if Path(__file__).resolve().parent.name=='numerical_supplement' else Path('outputs/BFG_DNA_Damage_Response_Preprint_2026-10-01'); SIM=OUT/'numerical_supplement';SIM.mkdir(exist_ok=True)
FIG=OUT/'figures';FIG.mkdir(exist_ok=True)
params=dict(sP=.05,kD=2.,KD=.5,dP=.4,kM=1.,sM=.02,kP=1.2,dM=.4,sQ=.02,kQ=.8,dQ=.15,h=4.,K=1.)
def hill(p):return p**4/(1+p**4)
lo,hi=0.,1.
for _ in range(80):
 p=(lo+hi)/2; f=.05-(.4+(.02+1.2*hill(p))/.4)*p
 if f>0:lo=p
 else:hi=p
pb=(lo+hi)/2; baseline=np.array([0,pb,(.02+1.2*hill(pb))/.4,(.02+.8*hill(pb))/.15])
def run(tau,r,dt):
 t=np.arange(round(80/dt)+1)*dt; z=np.empty((len(t),4));z[0]=baseline;z[0,0]=2.
 def rhs(tt,x,k):
  if tau==0:delay=x[1]
  else:
   u=(tt-tau)/dt
   if u<=0:delay=pb
   else:
    j=min(int(u),k); w=u-j
    delay=z[j,1] if j==k else (1-w)*z[j,1]+w*z[j+1,1]
  D,P,M,Q=x
  return np.array([-r*D,.05+2*D/(.5+D)-.4*P-M*P,.02+1.2*hill(delay)-.4*M,.02+.8*hill(P)-.15*Q])
 for k in range(len(t)-1):
  x=z[k];a=rhs(t[k],x,k);b=rhs(t[k]+dt/2,x+dt*a/2,k);c=rhs(t[k]+dt/2,x+dt*b/2,k);d=rhs(t[k]+dt,x+dt*c,k)
  z[k+1]=x+dt*(a+2*b+2*c+d)/6
 assert np.isfinite(z).all() and z.min()>=0
 return t,z
cases=[('A',0.,.12),('B',2.,.12),('C',0.,.03),('D',2.,.03)]
traces={};stats=[]
for name,tau,r in cases:
 t,z=run(tau,r,.01);tf,zf=run(tau,r,.005)
 err=float(np.max(np.abs(z-zf[::2])));derr=float(np.max(np.abs(z[:,0]-2*np.exp(-r*t))))
 assert err<1e-4 and derr<1e-10
 row=dict(case=name,delay=tau,repair_rate=r,max_p53=float(z[:,1].max()),time_max_p53=float(t[z[:,1].argmax()]),max_p21=float(z[:,3].max()),damage_at_80=float(z[-1,0]),step_halving_max_error=err,exact_damage_max_error=derr)
 stats.append(row);traces[name]=(t,z)
 with (SIM/f'case_{name}.csv').open('w',newline='') as f:
  w=csv.writer(f);w.writerow(['time','damage_D','p53_P','MDM2_M','p21_Q','Phi','I','IB'])
  I=(1+z[:,1])/(1+pb);phi=(1+z[:,0])*I*(1+baseline[3])/(1+z[:,3]);product=phi*I
  ib=np.gradient(product,t,edge_order=2)
  w.writerows(zip(t,*z.T,phi,I,ib))

def entropy(rho):
 e=np.linalg.eigvalsh(rho);e=e[e>1e-15];return float(-np.sum(e*np.log2(e)))
rng=np.random.default_rng(20261001);maxpol=maxid=maxclone=0.;minent=1.;mint=1.;audit=[]
for k in range(1000):
 X=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));rho=X@X.conj().T;rho/=np.trace(rho)
 y=rng.uniform(0,4,3);a=rng.uniform(.1,.9);b=1-a;den=a+b*y*y
 chi=(a+b*y[:,None]*y[None,:])/np.sqrt(den[:,None]*den[None,:]);sch=chi*rho
 C=np.diag(1/(1+y));B=np.diag(y/(1+y));A=np.vstack([np.sqrt(a)*C,np.sqrt(b)*B]);Q=np.diag(np.sqrt(a*np.diag(C)**2+b*np.diag(B)**2));J=A@np.linalg.inv(Q)
 pol=J.conj().T@np.block([[rho,np.zeros((3,3))],[np.zeros((3,3)),rho]])@J
 rhs=np.sum(a*b*(y[:,None]-y[None,:])**2*np.abs(rho)**2/(den[:,None]*den[None,:]))
 lhs=np.trace(rho@rho).real-np.trace(sch@sch).real
 pe=float(np.max(np.abs(pol-sch)));ie=float(abs(lhs-rhs));se=entropy(sch)-entropy(rho);te=float(abs(np.trace(sch)-1))
 maxpol=max(maxpol,pe);maxid=max(maxid,ie);maxclone=max(maxclone,pe);minent=min(minent,se);mint=min(mint,float(np.linalg.eigvalsh(sch).min()))
 audit.append([k,pe,ie,se,te])
with (SIM/'operator_audit.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['trial','polar_schur_error','moment_identity_error','entropy_change_bits','trace_error']);w.writerows(audit)
assert maxpol<1e-12 and maxid<1e-12 and minent>=-1e-12 and mint>=-1e-12
rho=np.array([[.5,.45],[.45,.5]]);chi=1/np.sqrt(5);n=np.arange(21);ent=[entropy(np.array([[.5,.45*chi**k],[.45*chi**k,.5]])) for k in n]
mem=[]
for a,b,s in [(.5,.25,.1),(.6,.35,.1),(1.,1.,0.)]:
 q=[1.,1.]
 for k in range(2,21):q.append(a*q[-1]+b*q[-2]+s)
 mem.append(q)
results=dict(seed=20261001,units='dimensionless; arbitrary model time, not hours',parameters=params,baseline=baseline.tolist(),dt=.01,verification_dt=.005,horizon=80,cases=stats,operator_audit=dict(trials=1000,alpha_range=[.1,.9],load_range=[0,4],max_polar_schur_error=maxpol,max_moment_identity_error=maxid,min_entropy_change_bits=minent,min_output_eigenvalue=mint),two_state_example=dict(loads=[0,2],alpha=.5,c=.45,chi=chi,entropy_before=ent[0],entropy_after=ent[1],purity_before=float(np.trace(rho@rho)),purity_after=.5+2*(.45*chi)**2),memory_examples=dict(coefficients=[[.5,.25,.1],[.6,.35,.1],[1,1,0]],trajectories=mem))
(SIM/'results.json').write_text(json.dumps(results,indent=2)+'\n')

# Static scientific plots: native vector PDF and high-resolution PNG exports.
palette=['#176B87','#C55A11','#48854A','#8356A0']
def start(name,title,w=560,h=380):
 c=canvas.Canvas(str(FIG/(name+'.pdf')),pagesize=(w,h));c.setTitle(title);c.setFont('Helvetica-Bold',13);c.drawString(24,h-27,title);return c,w,h
def finish(c,name):
 c.save();d=pdfium.PdfDocument(FIG/(name+'.pdf'));d[0].render(scale=2.5).to_pil().save(FIG/(name+'.png'))
def proj(x,y,z):return (280+140*(x-y),75+70*(x+y)+135*z)
def path(c,pts,stroke=1,fill=0):
 p=c.beginPath();p.moveTo(*pts[0]);
 for q in pts[1:]:p.lineTo(*q)
 c.drawPath(p,stroke=stroke,fill=fill)
def axes3(c,labels,ranges):
 c.setStrokeColor(colors.HexColor('#666666'));c.setLineWidth(.6);o=proj(0,0,0)
 for i,label in enumerate(labels):
  e=[0,0,0];e[i]=1;end=proj(*e);c.line(*o,*end);c.setFillColor(colors.black);c.setFont('Helvetica',9)
  dx,dy=[(0,-17),(-52,-10),(8,2)][i];c.drawString(end[0]+dx,end[1]+dy,label)
  for f in [0,.5,1]:
   q=[0,0,0];q[i]=f;p=proj(*q);c.circle(*p,1.2,fill=1);c.drawString(p[0]+3,p[1]-9,f'{ranges[i][0]+f*(ranges[i][1]-ranges[i][0]):.2g}')
c,w,h=start('figure_1_entropy_surface','1  Spectral entropy increase under neutral reclosure')
axis=np.linspace(0,4,33);baseent=ent[0];surf=[]
for i in range(32):
 for j in range(32):
  verts=[];vals=[]
  for ii,jj in [(i,j),(i+1,j),(i+1,j+1),(i,j+1),(i,j)]:
   x,y=axis[ii],axis[jj];ch=(1+x*y)/np.sqrt((1+x*x)*(1+y*y));s=entropy(np.array([[.5,.45*ch],[.45*ch,.5]]))-baseent;vals.append(s);verts.append(proj(x/4,y/4,s/.72))
  surf.append((i+j,verts,np.mean(vals)))
for _,verts,s in sorted(surf,reverse=True):
 f=min(s/.65,1);c.setFillColor(colors.Color(.12+.68*f,.5+.2*f,.75-.45*f));c.setStrokeColor(colors.Color(.7,.75,.8));c.setLineWidth(.12);path(c,verts,1,1)
axes3(c,['load y1','load y2','entropy gain (bits)'],[(0,4),(0,4),(0,.72)])
c.setFont('Helvetica',9);c.drawString(24,345,'alpha = beta = 0.5; input off-diagonal c = 0.45; 33 x 33 grid')
c.drawString(24,24,'Zero gain on y1 = y2. Spectral mixing is not a gain in predictive information.');finish(c,'figure_1_entropy_surface')
c,w,h=start('figure_2_phase_trajectories','2  Synthetic DNA-response trajectories: damage, p53 and p21')
maxP=max(z[:,1].max() for t,z in traces.values());maxQ=max(z[:,3].max() for t,z in traces.values());axes3(c,['damage D','p53 P','p21 Q'],[(0,2),(0,maxP),(0,maxQ)])
for i,(name,tau,r) in enumerate(cases):
 t,z=traces[name];pts=[proj(a/2,b/maxP,d/maxQ) for a,b,_,d in z[::15]];c.setStrokeColor(colors.HexColor(palette[i]));c.setLineWidth(1.5);path(c,pts)
 c.setFillColor(colors.HexColor(palette[i]));c.circle(*pts[0],3,fill=1);c.rect(pts[-1][0]-2,pts[-1][1]-2,4,4,fill=1)
 c.setFont('Helvetica',9);c.drawString(24,345-i*14,f'{name}: delay {tau:g}, repair r = {r:g}')
c.setFillColor(colors.black);c.drawString(24,24,'Circles: t = 0. Squares: t = 80. Arbitrary model units; no patient or cell data.');finish(c,'figure_2_phase_trajectories')
def panel(c,x,y,w,h,title,lines,xmax,ymin,ymax):
 c.setFillColor(colors.black);c.setFont('Helvetica-Bold',10);c.drawString(x,y+h+12,title);c.setStrokeColor(colors.HexColor('#cccccc'));c.setLineWidth(.5)
 for f in [0,.5,1]:
  c.line(x,y+f*h,x+w,y+f*h);c.setFont('Helvetica',8);c.drawRightString(x-5,y+f*h-3,f'{ymin+f*(ymax-ymin):.2g}');c.drawCentredString(x+f*w,y-13,f'{f*xmax:g}')
 c.setStrokeColor(colors.black);c.line(x,y,x+w,y);c.line(x,y,x,y+h)
 for xs,ys,col in lines:
  pts=[(x+xx/xmax*w,y+(yy-ymin)/(ymax-ymin)*h) for xx,yy in zip(xs,ys)];c.setStrokeColor(colors.HexColor(col));c.setLineWidth(1.2);path(c,pts)
c,w,h=start('figure_3_temporal_responses','3  Model response histories and bounded recursive inheritance',560,430)
for ix,(state,title) in enumerate([(1,'A  p53 activity P'),(3,'B  p21 activity Q')]):
 lines=[(t[::20],z[::20,state],palette[i]) for i,(t,z) in enumerate(traces.values())];panel(c,50+ix*265,230,210,130,title,lines,80,0,max(v[1].max() for v in lines)*1.05)
panel(c,50,55,210,110,'C  Repeated reclosure: entropy (bits)',[(n,np.array(ent),palette[0])],20,0,1)
panel(c,315,55,210,110,'D  Bounded two-step scalar witnesses',[(n,np.array(mem[i]),palette[i]) for i in range(2)],20,0,2.1)
c.setFillColor(colors.black);c.setFont('Helvetica',8);c.drawString(24,396,'Response colors: A blue, B orange, C green, D purple (cases as in Figure 2).');c.drawString(24,25,'Horizontal axes: model time in A-B; iteration n in C-D. Neither scalar witness is Shannon information.');finish(c,'figure_3_temporal_responses')
print(json.dumps(results,indent=2))
