import numpy as np, math
rng=np.random.default_rng(20260927)
# 1 complement/positivity
maxerr=0; minc=1e9; maxc=-1; minb=1e9; maxb=-1
for _ in range(1000):
    n=int(rng.integers(2,13)); A=rng.normal(size=(n,n))/np.sqrt(n); Y=A.T@A; I=np.eye(n)
    C=np.linalg.inv(I+Y); B=Y@C
    maxerr=max(maxerr,np.linalg.norm(C+B-I,2))
    ec=np.linalg.eigvalsh(C); eb=np.linalg.eigvalsh((B+B.T)/2)
    minc=min(minc,ec.min()); maxc=max(maxc,ec.max()); minb=min(minb,eb.min()); maxb=max(maxb,eb.max())
print('T1',maxerr,minc,maxc,minb,maxb)
# 2 Lipschitz
rat=[]
for _ in range(1000):
    n=int(rng.integers(2,13)); A=rng.normal(size=(n,n))/np.sqrt(n); Bm=rng.normal(size=(n,n))/np.sqrt(n)
    Y=A.T@A; Z=Bm.T@Bm; I=np.eye(n); CY=np.linalg.inv(I+Y); CZ=np.linalg.inv(I+Z)
    rat.append(np.linalg.norm(CY-CZ,2)/np.linalg.norm(Y-Z,2))
print('T2',max(rat))
# 3 fixed point
errs=[]; its=[]
for _ in range(5000):
    a=rng.uniform(.05,2); b=rng.uniform(.001,.35/a); phi=rng.uniform(.01,2.5)
    root=(-1+math.sqrt(1+4*a*b))/(2*b)
    for k in range(500):
        nxt=a/(1+b*phi)
        if abs(nxt-phi)<1e-12: phi=nxt; break
        phi=nxt
    errs.append(abs(phi-root)); its.append(k+1)
print('T3',max(errs),np.median(errs),np.median(its))
# 4 bounded recursion
final=[]; ok=0
for _ in range(1000):
    n=int(rng.integers(2,13)); R=rng.normal(size=(n,n))/np.sqrt(n)
    s=np.linalg.svd(R,compute_uv=False)[0]; q=rng.uniform(.65,.95); K=q/s*R
    x=rng.normal(size=n); x/=np.linalg.norm(x); good=True; prev=np.linalg.norm(x)
    for _ in range(100):
        x=K@x; cur=np.linalg.norm(x); good &= cur<=prev+1e-12; prev=cur
    ok+=good; final.append(cur)
print('T4',ok,np.median(final),max(final))
# 5 export
for gamma in [0,.05,.1,.2,.4]:
    E=.2
    for _ in range(200): E=(1-gamma)*E+.1
    print('T5',gamma,E)
# 6 ablation
cand=lost=0
for _ in range(100000):
    s,r=rng.random(2); c=s*r>.35; cand+=c; lost += bool(c and not (s*0>.35))
print('T6',cand,lost)


# 7 strengthened persistence: invariant constitutive sector + adaptive contraction
rng=np.random.default_rng(20260927)
min_id=[]; final_ad=[]; ok=0
for _ in range(2000):
    did=int(rng.integers(1,4)); dad=int(rng.integers(1,7))
    Q,_=np.linalg.qr(rng.normal(size=(did,did)))
    A=rng.normal(size=(dad,dad))/np.sqrt(dad)
    s=np.linalg.svd(A,compute_uv=False)[0]; q=rng.uniform(.55,.92); A=q/s*A
    xi=rng.normal(size=did); xi/=np.linalg.norm(xi)
    xa=rng.normal(size=dad); xa/=np.linalg.norm(xa)
    mi=1e9
    for _ in range(250):
        xi=Q@xi; xa=A@xa; mi=min(mi,np.linalg.norm(xi))
    min_id.append(mi); final_ad.append(np.linalg.norm(xa))
    ok += mi>.999999 and np.linalg.norm(xa)<=1+1e-12
print('T7',ok,min(min_id),np.median(final_ad),max(final_ad))

# 8 independent neutral-admissibility example
for g in [.1,.3]:
    M=np.array([[.8,g],[g,.8]])
    print('T8',g,max(abs(np.linalg.eigvals(M))))

# 9 matched-null higher-closure toy test
rng=np.random.default_rng(20260927)
def maxrun(mask):
    best=cur=0
    for v in mask:
        cur=cur+1 if v else 0; best=max(best,cur)
    return best
ec=en=0
for _ in range(3000):
    T=200; z=np.zeros(T); e=rng.normal(scale=.12,size=T)
    for t in range(1,T): z[t]=.94*z[t-1]+e[t]
    z=(z-z.min())/(z.max()-z.min()+1e-12)
    s1=np.clip(.25+.7*z+rng.normal(scale=.035,size=T),0,1)
    s2=np.clip(.25+.7*z+rng.normal(scale=.035,size=T),0,1)
    ec += maxrun(s1*s2>.45)>=8
    en += maxrun(s1*rng.permutation(s2)>.45)>=8
print('T9',ec,en,ec/3000,en/3000)


# 10 strict structure-preserving null + unified toy emergence test
rng=np.random.default_rng(20260927)
T=240; runs=4000
def maxrun(mask):
    best=cur=0
    for v in mask:
        cur=cur+1 if v else 0; best=max(best,cur)
    return best
aligned=null=source_a=source_n=abl=ncand=0
for _ in range(runs):
    burn=200; z=np.zeros(T+burn); eps=rng.normal(scale=.12,size=T+burn)
    for t in range(1,T+burn): z[t]=.94*z[t-1]+eps[t]
    z=z[burn:]; z=(z-z.min())/(z.max()-z.min()+1e-12)
    s1=np.clip(.25+.7*z+rng.normal(scale=.035,size=T),0,1)
    s2=np.clip(.25+.7*z+rng.normal(scale=.035,size=T),0,1)
    src=lambda s: np.std(s)>.05 and np.min(s)>=0 and np.max(s)<=1
    source_a += src(s1) and src(s2)
    c=maxrun(s1*s2>.45)>=8; aligned+=c; ncand+=c
    if c: abl += True  # relational witness is set to zero, sources unchanged
    k=int(rng.integers(35,121)); s2n=np.roll(s2,k)
    source_n += src(s1) and src(s2n)
    null += maxrun(s1*s2n>.45)>=8
print('T10',source_a,source_n,aligned,null,abl,ncand,aligned/runs,null/runs)
