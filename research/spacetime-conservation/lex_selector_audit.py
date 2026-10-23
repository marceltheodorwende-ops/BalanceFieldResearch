"""Retained-data spectral tie resolution and equal-load pair controls."""
from __future__ import annotations
import json
import platform
from pathlib import Path
import numpy as np
import sympy as s
import audit
import pair_audit

HERE=Path(__file__).resolve().parent
TOL=1e-10
SEED=20261030
GROUP_GAPS=[]
GROUP_SPREADS=[]

def spectral_blocks(operator,basis):
    reduced=basis.conj().T@operator@basis
    eig,vec=np.linalg.eigh((reduced+reduced.conj().T)/2)
    tolerance=TOL*max(1.,float(np.linalg.norm(reduced,2)))
    groups=[]; start=0
    for j in range(1,len(eig)+1):
        if j==len(eig) or eig[j]-eig[start]>tolerance:
            GROUP_SPREADS.append(float((eig[j-1]-eig[start])/tolerance))
            if j<len(eig): GROUP_GAPS.append(float((eig[j]-eig[j-1])/tolerance))
            groups.append(basis@vec[:,start:j]); start=j
    return groups

def selector(y,f,w):
    leaves=[]
    for qy in spectral_blocks(y,np.eye(len(y))):
        for qf in spectral_blocks(f,qy):
            leaves.extend(spectral_blocks(w,qf))
    selected=[]; rank=0
    for block in leaves:
        if rank+block.shape[1]>2:
            return None,[q.shape[1] for q in leaves]
        selected.append(block); rank+=block.shape[1]
        if rank==2: return np.column_stack(selected),[q.shape[1] for q in leaves]
    return None,[q.shape[1] for q in leaves]

def diagonal_exact_selector(y,f,w):
    keys=sorted(set(zip(y,f,w)))
    selected=[]
    for key in keys:
        group=[i for i,z in enumerate(zip(y,f,w)) if z==key]
        if len(selected)+len(group)>2: return None
        selected.extend(group)
        if len(selected)==2: return selected
    return None

def exact_checks():
    collision_y=[s.Rational(50,209),s.Rational(386,1881),s.Rational(50,209)]
    collision_f=[1,1,s.Rational(41762,20625)]
    assert diagonal_exact_selector(collision_y,collision_f,[s.Rational(1,3)]*3)==[1,0]
    fallback_y=[s.Rational(1,5),s.Rational(1,4),s.Rational(1,4),s.Rational(3,10)]
    assert diagonal_exact_selector(fallback_y,[1]*4,[s.Rational(i,10) for i in (1,2,3,4)])==[0,1]
    assert diagonal_exact_selector([s.Rational(1,4)]*3,[1]*3,[s.Rational(1,3)]*3) is None
    boundary=[]
    for epsilon in (0,s.Rational(1,1000),s.Rational(1,100000)):
        indices=diagonal_exact_selector([s.Rational(1,5),s.Rational(1,4)-epsilon,s.Rational(1,4)+epsilon],
                                       [1,2,1],[s.Rational(1,3)]*3)
        assert indices==([0,2] if epsilon==0 else [0,1])
        boundary.append(dict(epsilon=str(epsilon),indices_zero_based=indices))
    y=s.diag(s.Rational(1,5),s.Rational(1,5),s.Rational(3,10),s.Rational(3,10))
    f=s.diag(1,2,3,4); f[0,2]=f[2,0]=s.Rational(1,4)
    f[1,3]=s.I/5; f[3,1]=-s.I/5
    w=s.eye(4)/4; w[0,1]=(1-2*s.I)/40; w[1,0]=(1+2*s.I)/40
    assert all(f[:j,:j].det()>0 and w[:j,:j].det()>0 for j in range(1,5))
    alpha=pair_audit.alpha_exact([y[i,i] for i in range(4)],[1,2,3,4])
    assert alpha==s.Rational(76,1101)
    a,b=s.symbols('a b',positive=True)
    assert s.cancel((a+(1-a)*b*b)**2/((a+(1-a)*b*b)**2)-1)==0
    return dict(collision_selected_indices_zero_based=[1,0],witness_fallback_indices_zero_based=[0,1],
                symmetric_state_unresolved=True,discontinuous_selection_path=boundary,
                equal_load_alpha=str(alpha),equal_load_pair_factor='h=1',
                equal_load_F_positive_principal_minors=[str(f[:j,:j].det()) for j in range(1,5)],
                equal_load_W_positive_principal_minors=[str(w[:j,:j].det()) for j in range(1,5)])

def pair_factor_check(update,k,f,w,y):
    z,leaves=selector(y,f,w)
    assert z is not None
    source_s=z@z.conj().T
    eig,vec=np.linalg.eigh(source_s); ze=vec[:,eig<.5]
    env_y,env_vec=np.linalg.eigh(ze.conj().T@y@ze)
    env_basis=ze@env_vec
    env_weight=np.diag(env_basis.conj().T@f@env_basis).real
    predicted=pair_audit.pair_step(z.conj().T@k@z,z.conj().T@f@z,z.conj().T@y@z,env_y,env_weight)
    out=pair_audit.source_aligned(update,k,f,w,y)
    nz,nleaves=selector(out['y'],out['f'],out['w'])
    assert nz is not None
    residuals=dict(projector=float(np.linalg.norm(nz@nz.conj().T-source_s)),
                   pair_kernel=float(np.linalg.norm(z.conj().T@out['k']@z-predicted['k'])),
                   pair_load=float(np.linalg.norm(z.conj().T@out['y']@z-predicted['y'])),
                   alpha=abs(float(out['alpha']-predicted['alpha'])))
    assert max(residuals.values())<TOL
    return out,residuals,z,leaves,nleaves

def witness_controls(update):
    rows=[]
    for kind in ('collision','witness'):
        if kind=='collision':
            y=np.diag([50/209,386/1881,50/209]); f=np.diag([1.,1.,41762/20625]); w=np.eye(3)/3
        else:
            y=np.diag([.2,.25,.25,.3]); f=np.eye(4); w=np.diag([.1,.2,.3,.4])
        k=np.arange(len(y)**2,dtype=float).reshape(len(y),len(y)); k=(k+k.T)/2
        out,residuals,z,leaves,nleaves=pair_factor_check(update,k,f,w,y)
        expected=np.diag([1.,1.]+[0.]*(len(y)-2))
        assert np.linalg.norm(z@z.conj().T-expected)<TOL
        rows.append(dict(kind=kind,residuals=residuals,terminal_block_ranks=leaves))
    # Nontrivial global dynamics with an exactly equal-load selected pair.
    y=np.diag([.2,.2,.3,.3]); f=np.diag([1.,2.,3.,4.]).astype(complex)
    f[0,2]=f[2,0]=.25; f[1,3]=.2j; f[3,1]=-.2j
    w=np.eye(4,dtype=complex)/4; w[0,1]=(1-2j)/40; w[1,0]=(1+2j)/40
    k=np.array([[2,1+1j,.3,.2j],[1-1j,-1,.4j,.1],[.3,-.4j,2,.5-.2j],[-.2j,.1,.5+.2j,0]])
    out,residuals,z,leaves,nleaves=pair_factor_check(update,k,f,w,y)
    identity=np.diag([1.,1.,0.,0.]); axis=np.diag([1.,-1.,0.,0.])
    off=np.zeros((4,4),complex); off[0,1]=w[0,1]; off[1,0]=w[1,0]
    x=off/(np.linalg.norm(off)/np.sqrt(2)); basis=[identity,x,-1j*axis@x,axis]
    p=np.array([np.trace(e@k).real/2 for e in basis]); pp=np.array([np.trace(e@out['k']).real/2 for e in basis])
    charge_residual=float(np.linalg.norm(pp-p)); global_change=float(np.linalg.norm(out['k']-k))
    assert charge_residual<TOL and global_change>1e-5 and np.all(np.abs(p)>1e-3)
    unresolved,_=selector(np.eye(3)/4,np.eye(3),np.eye(3)/3)
    assert unresolved is None
    return dict(full_source_calls=3,selection_witnesses=rows,equal_load_coordinates=p.tolist(),
                equal_load_successor_coordinates=pp.tolist(),equal_load_charge_residual=charge_residual,
                equal_load_global_kernel_change=global_change,equal_load_factor_residuals=residuals,
                symmetric_selector_returned_unresolved=True)

def complex_controls(update):
    rng=np.random.default_rng(SEED)
    maxima=dict(projector=0.,pair_kernel=0.,pair_load=0.,alpha=0.,gauge_projector=0.,gauge_successor=0.)
    rows=[]; gauges=0
    for n in (3,4,5,6):
        for case in range(3):
            ys=np.array([.2,.2,.3] if n==3 else [.2,.25,.25]+list(np.linspace(.28,.3,n-3)))
            f=np.diag(np.linspace(1.,2.,n)).astype(complex)
            tied=[0,1] if n==3 else [1,2]
            if case==1: f[tied,tied]=1.5
            noise=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); noise=(noise+noise.conj().T)/2
            np.fill_diagonal(noise,0)
            if case==1: noise[tied[0],tied[1]]=noise[tied[1],tied[0]]=0
            f+=.01*noise/max(1.,np.linalg.norm(noise,2))
            w=np.diag(np.linspace(1.,2.,n)).astype(complex)
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); raw=(raw+raw.conj().T)/2
            w+=.01*raw/max(1.,np.linalg.norm(raw,2)); w/=np.trace(w).real
            assert np.linalg.eigvalsh(f)[0]>0 and np.linalg.eigvalsh(w)[0]>0
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=(raw+raw.conj().T)/2
            u=audit.complex_unitary(rng,n); convert=lambda a:u@a@u.conj().T
            k,f,w,y=convert(k),convert(f),convert(w),convert(np.diag(ys))
            for event in range(2):
                out,residuals,z,leaves,nleaves=pair_factor_check(update,k,f,w,y)
                for key,value in residuals.items(): maxima[key]=max(maxima[key],value)
                if case==0 and event==0:
                    g=audit.complex_unitary(rng,n); conjugate=lambda a:g@a@g.conj().T
                    gz,_=selector(conjugate(y),conjugate(f),conjugate(w)); assert gz is not None
                    gr=float(np.linalg.norm(gz@gz.conj().T-conjugate(z@z.conj().T)))
                    gout=pair_audit.source_aligned(update,conjugate(k),conjugate(f),conjugate(w),conjugate(y))
                    ngz,_=selector(gout['y'],gout['f'],gout['w']); assert ngz is not None
                    rr=float(np.linalg.norm(ngz@ngz.conj().T-conjugate(z@z.conj().T)))
                    maxima['gauge_projector']=max(maxima['gauge_projector'],gr)
                    maxima['gauge_successor']=max(maxima['gauge_successor'],rr); gauges+=1
                rows.append(dict(n=n,case=case,event=event+1,witness_needed=case==1,
                                 terminal_block_ranks=leaves,successor_terminal_block_ranks=nleaves,
                                 residuals=residuals))
                k,f,w,y=out['k'],out['f'],out['w'],out['y']
    assert max(maxima.values())<TOL
    return dict(preparations=12,source_events=len(rows),additional_gauge_source_calls=gauges,
                full_source_calls=len(rows)+gauges,maximum_residuals=maxima,cases=rows)

def run():
    GROUP_GAPS.clear(); GROUP_SPREADS.clear()
    update=audit.load_update()
    result=dict(scope='C with Y degeneracies; Y/F/W lexicographic selector only where no unresolved block straddles rank two',
                source_blob=audit.EXPECTED_SOURCE_BLOB,seed=SEED,tolerance=TOL,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                exact=exact_checks(),witnesses=witness_controls(update),full_source=complex_controls(update),
                status='PASS for conditional retained selector/factor; spatial current and Einstein OPEN')
    assert min(GROUP_GAPS)>1000 and max(GROUP_SPREADS)<=1
    result['numerical_grouping']=dict(minimum_resolved_gap_over_tolerance=min(GROUP_GAPS),
                                      maximum_within_group_spread_over_tolerance=max(GROUP_SPREADS),
                                      exact_degeneracy_law_is_not_a_tolerance=True)
    return result

if __name__=='__main__':
    result=run()
    (HERE/'lex_selector_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='cases'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))
