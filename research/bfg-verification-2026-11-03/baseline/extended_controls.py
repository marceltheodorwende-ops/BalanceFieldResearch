"""Independent controls for the closed finite event and new mathematical results.
No empirical claims. Run in a copy of the reproducibility directory.
"""
from pathlib import Path
import json,platform
import numpy as np
import mpmath as mp
import sympy as sp
from fractions import Fraction as F
OUT=Path(__file__).resolve().parent
SEED=20261103
def herm(a):return (a+a.conj().T)/2
def polar(a,tol=1e-11):
    u,s,v=np.linalg.svd(a,full_matrices=False);keep=s>tol
    return u[:,keep]@v[keep,:]
def event(state,tol=1e-10):
    k,f,w,y,p=state;n=len(y);ev,z=np.linalg.eigh(y);q=(z*(ev<1))@z.conj().T
    ts=polar(q@p);ps=herm(ts@ts.conj().T);ss=herm(ts.conj().T@ts)
    mass=float(np.trace(ss@w).real)
    if mass<=tol:return None,dict(terminal='selection')
    fs=herm(ts@f@ts.conj().T);ws=herm(ts@w@ts.conj().T/mass)
    vals,zz=np.linalg.eigh(ps);z=zz[:,vals>.5];pc=z.shape[1]
    if not pc:return None,dict(terminal='empty')
    g=np.eye(n)+y;cn=np.linalg.inv(g);bn=y@cn;d=z.conj().T@g@z;pg=z@np.linalg.solve(d,z.conj().T@g)
    lc=float(np.trace(g@pg@cn@fs@cn@pg.conj().T).real)
    lb=float(np.trace(g@pg@bn@fs@bn@pg.conj().T).real)
    if min(lc,lb)<=tol:return None,dict(terminal='load',lc=lc,lb=lb)
    a=np.vstack([np.sqrt(lb/(lc+lb))*pg@cn,np.sqrt(lc/(lc+lb))*pg@bn])
    u,s,vh=np.linalg.svd(a,full_matrices=False);keep=s>tol;u=u[:,keep];s=s[keep];v=vh[keep,:].conj().T;r=len(s)
    yn=np.diag(s*s);kn=herm(u.conj().T@np.kron(np.eye(2),k)@u)
    t4=polar(v.conj().T@ps);pinh=herm(t4@t4.conj().T);fn=herm(t4@fs@t4.conj().T);wn=herm(t4@ws@t4.conj().T)
    ee,ez=np.linalg.eigh(np.eye(r)-pinh);basis=ez[:,ee>.5];seed=0.
    pn=pinh
    if basis.shape[1]:
        lam,b=np.linalg.eigh(herm(basis.conj().T@kn@basis))
        if lam[0]>=-tol or (len(lam)>1 and lam[1]-lam[0]<tol):return None,dict(terminal='seed',n=n,p=pc,r=r)
        vec=basis@b[:,0];proj=np.outer(vec,vec.conj());seed=float(-lam[0]);fn=herm(fn+seed*proj);pn=herm(pinh+proj)
    info=dict(n=n,p=pc,r=r,p_next=int(round(np.trace(pn).real)),defect_next=int(round(r-np.trace(pn).real)),mass=mass,seed=seed,gram_max=float(max(s*s)),formation=float(np.trace(fn).real),k_norm=float(np.linalg.norm(kn,2)))
    return (kn,fn,wn,yn,pn),info
def run():
    rng=np.random.default_rng(SEED);records=[];defect_paths=[];max_mass_error=0.;max_norm_excess=0.;max_schur=0.
    for case in range(120):
        n=int(rng.integers(3,10));p0=int(rng.integers(1,n));q=np.linalg.qr(rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)))[0];p=q[:,:p0]@q[:,:p0].conj().T
        yy=rng.uniform(.08,.9 if case%2 else 1.8,n);yy[:2]=rng.uniform(.08,.9,2)
        y=np.diag(yy);a=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));k=-np.eye(n)-.1*herm(a)/np.linalg.norm(herm(a),2)
        f=np.eye(n);w=np.eye(n)/n;state=(k,f,w,y,p);initial_kn=np.linalg.norm(k,2);trace0=np.trace(f).real;seeds=0;path=[n-p0];full_at=None
        for step in range(n):
            new,info=event(state)
            assert new is not None,(case,step,info)
            if step>0:
                max_mass_error=max(max_mass_error,abs(info['mass']-1))
                assert info['defect_next']<path[-1] or path[-1]==0
            assert info['r']<=len(state[0]);assert info['gram_max']<1
            seeds+=bool(info['seed']);max_norm_excess=max(max_norm_excess,info['k_norm']-initial_kn)
            assert info['formation']<=trace0+(n-1)*initial_kn+1e-8
            state=new;path.append(info['defect_next'])
            if info['defect_next']==0:full_at=step+1;break
        assert full_at is not None and full_at<=n
        assert seeds<=n-1
        defect_paths.append(path);records.append(dict(case=case,n=n,p_initial=p0,full_at=full_at,path=path,seeds=int(seeds)))
        # Independent Schur expression against the ambient SVD compression.
        k,f,w,y,p=state
        # Cross-check the formula on a fresh regular full-support state. The
        # completed orbit can already have loads below the binary64 rank gate.
        y=np.diag(rng.uniform(.08,.9,len(y)));p=np.eye(len(y));state=(k,f,w,y,p)
        diag,vec=np.linalg.eigh(y);kg=vec.conj().T@k@vec;fg=vec.conj().T@f@vec
        a=float(np.sum(np.diag(fg).real*diag**2/(1+diag))/np.sum(np.diag(fg).real*(1+diag**2)/(1+diag)))
        chi=(a+(1-a)*diag[:,None]*diag[None,:])/np.sqrt((a+(1-a)*diag**2)[:,None]*(a+(1-a)*diag**2)[None,:])
        expected=chi*kg
        nxt,ii=event(state);assert nxt is not None
        # Full-support output V is recovered independently from A's Gram eigenspaces.
        cn=np.linalg.inv(np.eye(len(y))+y);bn=y@cn;aa=np.vstack([np.sqrt(a)*cn,np.sqrt(1-a)*bn]);u,sv,vh=np.linalg.svd(aa,full_matrices=False)
        back=vec.conj().T@vh.conj().T@nxt[0]@vh@vec
        max_schur=max(max_schur,float(np.linalg.norm(back-expected)))
    assert max_mass_error<1e-10 and max_norm_excess<1e-10 and max_schur<1e-9
    # A seed gate failure is an exact mathematical possibility, not a claimed integration error.
    n=6;p=np.diag([1.,1.,1.,0.,0.,0.]);rot=np.linalg.qr(rng.normal(size=(n,n)))[0];y=rot@np.diag(np.linspace(.1,.8,n))@rot.T
    stopped,why=event((np.eye(n),p,p/3,y,p));assert stopped is None and why['terminal']=='seed'
    stopped,whydeg=event((-np.eye(n),p,p/3,y,p));assert stopped is None and whydeg['terminal']=='seed'
    # High-precision closed-sector controls avoid interpreting binary64 underflow as exact termination.
    mp.mp.dps=90;full=[]
    for case in range(40):
        n=int(rng.integers(2,8));ys=[mp.mpf(str(x)) for x in rng.uniform(.001,.999,n)];weights=[mp.mpf(str(x)) for x in rng.uniform(.1,1,n)];ms=[max(ys)]
        for step in range(14):
            alpha=sum(w*t*t/(1+t) for w,t in zip(weights,ys))/sum(w*(1+t*t)/(1+t) for w,t in zip(weights,ys))
            new=[(alpha+(1-alpha)*t*t)/(1+t)**2 for t in ys];m=max(ys);mn=max(new)
            assert all(t>0 for t in new) and mn<m
            assert mn<=2*m*m/(1+m*m)*(1+mp.mpf('1e-80'))
            if step==0:assert mn<mp.mpf('.5')
            if step>=1:assert mn<=mp.mpf('.5')*mp.mpf('.8')**(2**(step-1))*(1+mp.mpf('1e-75'))
            ys=new;ms.append(mn)
        full.append(dict(case=case,log10_max=[float(mp.log10(t)) for t in ms],last_positive=str(ms[-1])))
    # Exact rational cases, including a rank-one formation density whose largest
    # load mode carries zero formation weight. These check the bound without roundoff.
    rational_cases=0
    for yc,wc in [([F(1,1000),F(999,1000),F(1,2)],[F(1),F(0),F(0)])]+[([F(j,11),F(10-j,11)],[F(1),F(2)]) for j in range(1,9)]:
        for step in range(4):
            a=sum(w*t*t/(1+t) for w,t in zip(wc,yc))/sum(w*(1+t*t)/(1+t) for w,t in zip(wc,yc))
            nn=[(a+(1-a)*t*t)/(1+t)**2 for t in yc];mm=max(yc);mn=max(nn)
            assert 0<mn<mm and mn<=2*mm*mm/(1+mm*mm)
            if step==0:assert mn<F(1,2)
            if step>=1:assert mn<=F(1,2)*F(4,5)**(2**(step-1))
            yc=nn
        rational_cases+=1
    # Exact observability compression example with one invisible hidden coordinate.
    c=sp.diag(sp.Rational(1,2),sp.Rational(1,3),sp.Rational(1,4));b=sp.Matrix([[1,1,0]]);obs=sp.Matrix.vstack(b,b*c,b*c*c)
    assert obs.rank()==2 and obs.nullspace()==[sp.Matrix([0,0,1])]
    # Strong lumpability: two blocks, equal block sums; perturbation destroys it.
    tr=sp.Matrix([[sp.Rational(1,5),sp.Rational(3,10),sp.Rational(1,2)],[sp.Rational(2,5),sp.Rational(1,10),sp.Rational(1,2)],[0,0,1]])
    assert sum(tr[0,j] for j in [0,1])==sum(tr[1,j] for j in [0,1])==sp.Rational(1,2)
    # Conformal example g=exp(2*a*x1)*eta. Constant connection coefficients.
    aa=sp.symbols('a',real=True);eta=sp.diag(-1,1,1,1);omega=[0,aa,0,0]
    gam=lambda a,b,c:sp.KroneckerDelta(a,b)*omega[c]+sp.KroneckerDelta(a,c)*omega[b]-eta[b,c]*sum(eta[a,e]*omega[e] for e in range(4))
    curv=sum(gam(0,0,e)*gam(e,2,2)-gam(0,2,e)*gam(e,0,2) for e in range(4))
    assert sp.simplify(curv+aa**2)==0
    result=dict(seed=SEED,python=platform.python_version(),numpy=np.__version__,mpmath=mp.__version__,sympy=sp.__version__,status='PASS',random_full_event_cases=len(records),high_precision_full_sector_cases=len(full),high_precision_steps_per_case=14,exact_rational_cases=rational_cases,exact_steps_per_case=4,max_witness_mass_error=max_mass_error,max_kernel_norm_excess=max_norm_excess,max_schur_crosscheck_error=max_schur,finite_completion_examples=records,collapse_examples=full,seed_terminal_control=why,degenerate_negative_seed_terminal_control=whydeg,observability_rank=int(obs.rank()),conformal_component=str(curv),scope='Implementation controls for stated finite model; no empirical data, no novelty-priority or physical validation; numerical rank tolerance only in random branch controls')
    (OUT/'extended_verification.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ['finite_completion_examples','collapse_examples']},indent=2))
    return result
def figures(r):
    import matplotlib;matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    dest=OUT.parent/'figures';dest.mkdir(exist_ok=True)
    fig,ax=plt.subplots(1,2,figsize=(9,3.6))
    for ex in sorted(r['finite_completion_examples'],key=lambda e:len(e['path']),reverse=True)[:5]:ax[0].step(range(len(ex['path'])),ex['path'],where='post',marker='o',label=f"n={ex['n']}, p={ex['p_initial']}")
    ax[0].set(xlabel='successful event',ylabel='carrier dimension minus persistence rank',title='Finite completion of actual ambient events');ax[0].legend(fontsize=7)
    for ex in r['collapse_examples'][:4]:ax[1].semilogy(range(15),[-v for v in ex['log10_max']],marker='.',linewidth=1)
    ax[1].set(xlabel='event in the full-persistence sector',ylabel='minus log10 of maximum load',title='Positive loads approach zero rapidly')
    fig.tight_layout();fig.savefig(dest/'figure4_longtime.pdf');fig.savefig(dest/'figure4_longtime.png',dpi=180);plt.close(fig)
if __name__=='__main__':figures(run())
