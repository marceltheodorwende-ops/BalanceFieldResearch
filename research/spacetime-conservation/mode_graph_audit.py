"""Internal mode graphs, guessed currents and source-channel continuity."""
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
SEED=20261031

def graph(k,f,w,u):
    change=lambda a:u.conj().T@a@u
    kb,fb,wb=change(k),change(f),change(w)
    rf=fb/np.trace(fb).real
    return dict(q=np.diag(kb).real,f=np.diag(fb).real,w=np.diag(wb).real,
                aF=np.abs(rf)**2,aW=np.abs(wb)**2,b=np.abs(kb)**2,
                jF=2*np.imag(rf*kb.T),jW=2*np.imag(wb*kb.T))

def channel_flux(k,operators,u):
    kb=u.conj().T@k@u
    flux=np.zeros(kb.shape)
    for operator in operators:
        t=u.conj().T@operator@u
        comm=t@kb-kb@t
        flux+=np.real(t*comm.T)
    return flux

def hmatrix(ys,alpha):
    d=alpha+(1-alpha)*ys*ys
    return (alpha+(1-alpha)*np.outer(ys,ys))/np.sqrt(np.outer(d,d))

def exact_checks():
    alpha=pair_audit.alpha_exact([s.Rational(1,5),s.Rational(3,10)],[1,1])
    assert alpha==s.Rational(8,133)
    h=31/s.sqrt(1001)
    assert h*h==s.Rational(961,1001)
    f=s.Matrix([[1,s.I/2],[-s.I/2,1]])
    w=f/2; eye=s.eye(2); sy=s.Matrix([[0,-s.I],[s.I,0]])
    assert f.det()>0 and w.det()>0
    triangle_f=s.ones(3)/4+3*s.eye(3)/4
    triangle_k=s.Matrix([[2,-s.I,s.I],[s.I,2,-s.I],[-s.I,s.I,2]])
    assert all(triangle_f[:j,:j].det()>0 and triangle_k[:j,:j].det()>0 for j in range(1,4))
    p=[(eye+sy)/2,(eye-sy)/2]
    ts=[s.diag(s.sqrt(s.Rational(8,13)),s.sqrt(s.Rational(32,77))),
        s.diag(s.sqrt(s.Rational(5,13)),s.sqrt(s.Rational(45,77)))]
    k=eye+sy
    kp=sum((t*k*t for t in ts),s.zeros(2))
    current=sum((s.re(s.trace(p[0]*t*p[1]*(t*k-k*t))) for t in ts),s.Integer(0))
    assert s.simplify(current-(1-h))==0
    assert s.simplify(s.trace(p[0]*(kp-k))-(h-1))==0
    signs=[]
    for sign in (1,-1):
        kk=s.Matrix([[1,sign],[sign,1]])
        assert all(v>=0 for v in kk.eigenvals())
        guessed=s.simplify(2*s.im((f/2)[0,1]*kk[1,0]))
        assert guessed==s.Rational(sign,2)
        signs.append(dict(sign=sign,node_stocks=['1','1'],kernel_edge_magnitude='1',
                          guessed_edge_current=str(guessed)))
    chain=s.Matrix([[1,0],[-1,1],[0,-1]])
    triangle=s.Matrix([[1,0,-1],[-1,1,0],[0,-1,1]])
    assert chain.rank()==2 and not chain.nullspace()
    assert triangle.rank()==2 and triangle*s.ones(3,1)==s.zeros(3,1)
    return dict(alpha=str(alpha),h_squared=str(h*h),coherence_edge_loss=str(1-h*h),
                guessed_current_witnesses=signs,formation_node_flux=str(s.simplify(current)),
                formation_node_stock_changes=[str(h-1),str(1-h)],chain_cycle_dimension=0,
                triangle_cycle_dimension=len(triangle.nullspace()),triangle_circulation=['1','1','1'])

def source_witnesses(update):
    y=np.diag([.2,.3]); f=np.array([[1,.5j],[-.5j,1]]); w=f/2
    graphs=[]; outputs=[]; rows=[]
    for sign in (1,-1):
        k=np.array([[1.,sign],[sign,1.]])
        before=graph(k,f,w,np.eye(2)); out=pair_audit.source_aligned(update,k,f,w,y)
        after=graph(out['k'],out['f'],out['w'],np.eye(2))
        assert np.linalg.norm(after['q']-before['q'])<TOL
        assert np.linalg.norm(after['b']-hmatrix(np.array([.2,.3]),8/133)**2*before['b'])<TOL
        defect=after['q']-before['q']+before['jF'].sum(axis=1)
        assert np.linalg.norm(defect-np.array([sign/2,-sign/2]))<TOL
        graphs.append(before); outputs.append(after)
        rows.append(dict(sign=sign,guessed_current=before['jF'].tolist(),continuity_defect=defect.tolist()))
    keys=('q','f','w','aF','aW','b')
    fiber_before=max(float(np.linalg.norm(graphs[0][key]-graphs[1][key])) for key in keys)
    fiber_after=max(float(np.linalg.norm(outputs[0][key]-outputs[1][key])) for key in keys)
    assert max(fiber_before,fiber_after)<TOL
    sy=audit.pauli()[2]; k=np.eye(2)+sy
    model=audit.aligned(k,f,y); out=pair_audit.source_aligned(update,k,f,w,y)
    _,v=np.linalg.eigh(f)
    flux=channel_flux(k,[model['tc'],model['tb']],v)
    stock=np.diag(v.conj().T@(out['k']-k)@v).real
    assert np.linalg.norm(stock+flux.sum(axis=1))<TOL
    assert abs(flux[0,1]-(1-31/np.sqrt(1001)))<TOL
    # The initially circulating guessed triangle current is not retained as divergence free.
    yt=np.diag([.2,.25,.3]); ft=np.full((3,3),.25); np.fill_diagonal(ft,1.)
    wt=np.eye(3)/3
    kt=np.array([[2,-1j,1j],[1j,2,-1j],[-1j,1j,2]],complex)
    triangle=[]
    for event in range(2):
        before=graph(kt,ft,wt,np.eye(3)); out=pair_audit.source_aligned(update,kt,ft,wt,yt)
        divergence=before['jF'].sum(axis=1)
        if event==0: assert np.linalg.norm(divergence)<TOL and np.linalg.norm(before['jF'])>1e-3
        else: assert np.linalg.norm(divergence)>1e-5
        assert np.linalg.norm(np.diag(out['k']-kt))<TOL
        triangle.append(dict(event=event+1,guessed_current_divergence=divergence.tolist()))
        kt,ft,wt,yt=out['k'],out['f'],out['w'],out['y']
    return dict(full_source_calls=5,guessed_current_examples=rows,
                graph_fiber_input_residual=fiber_before,graph_fiber_output_residual=fiber_after,
                channel_formation_flux=flux.tolist(),channel_formation_stock_change=stock.tolist(),
                channel_formation_continuity_residual=float(np.linalg.norm(stock+flux.sum(axis=1))),
                triangle=triangle)

def complex_controls(update):
    rng=np.random.default_rng(SEED)
    maxima=dict(node=0.,graph_alpha=0.,graph_load=0.,formation_edges=0.,witness_edges=0.,kernel_edges=0.,guessed_current_evolution=0.,
                hilbert_schmidt_loss=0.,source_current_continuity=0.,source_current_antisymmetry=0.,gauge_graph=0.,gauge_source_current=0.)
    rows=[]; gauges=0; max_guessed_divergence=0.; max_formation_transfer=0.
    for n in (3,4,5,6):
        for case in range(3):
            u=audit.complex_unitary(rng,n); ys=np.linspace(.2,.3,n); y=(u*ys)@u.conj().T
            f=audit.pos(rng,n); w=audit.pos(rng,n); w/=np.trace(w).real
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=(raw+raw.conj().T)/2
            for event in range(2):
                before=graph(k,f,w,u); model=audit.aligned(k,f,y)
                out=pair_audit.source_aligned(update,k,f,w,y); after=graph(out['k'],out['f'],out['w'],u)
                current_ys=np.diag(u.conj().T@y@u).real
                lc=np.sum(before['f']/(1+current_ys))
                lb=np.sum(before['f']*current_ys**2/(1+current_ys))
                graph_alpha=lb/(lc+lb)
                h=hmatrix(current_ys,graph_alpha)
                values=dict(node=max(np.linalg.norm(after[key]-before[key]) for key in ('q','f','w')),
                            graph_alpha=abs(float(out['alpha']-graph_alpha)),
                            graph_load=np.linalg.norm(u.conj().T@out['y']@u-np.diag(pair_audit.g(current_ys,graph_alpha))),
                            formation_edges=np.linalg.norm(after['aF']-before['aF']),
                            witness_edges=np.linalg.norm(after['aW']-before['aW']),
                            kernel_edges=np.linalg.norm(after['b']-h*h*before['b']),
                            guessed_current_evolution=max(np.linalg.norm(after[key]-h*before[key]) for key in ('jF','jW')),
                            hilbert_schmidt_loss=abs(np.linalg.norm(k)**2-np.linalg.norm(out['k'])**2-np.sum((1-h*h)*before['b'])))
                _,vf=np.linalg.eigh(f)
                source_flux=channel_flux(k,[model['tc'],model['tb']],vf)
                stock=np.diag(vf.conj().T@(out['k']-k)@vf).real
                values['source_current_continuity']=np.linalg.norm(stock+source_flux.sum(axis=1))
                values['source_current_antisymmetry']=np.linalg.norm(source_flux+source_flux.T)
                max_formation_transfer=max(max_formation_transfer,float(np.linalg.norm(stock)))
                max_guessed_divergence=max(max_guessed_divergence,float(np.linalg.norm(before['jF'].sum(axis=1))))
                for key,value in values.items(): maxima[key]=max(maxima[key],float(value))
                if case==0 and event==0:
                    g=audit.complex_unitary(rng,n); conjugate=lambda a:g@a@g.conj().T
                    gout=pair_audit.source_aligned(update,conjugate(k),conjugate(f),conjugate(w),conjugate(y))
                    gb=graph(gout['k'],gout['f'],gout['w'],g@u)
                    gr=max(float(np.linalg.norm(gb[key]-after[key])) for key in after)
                    gm=audit.aligned(conjugate(k),conjugate(f),conjugate(y))
                    gf=channel_flux(conjugate(k),[gm['tc'],gm['tb']],g@vf)
                    maxima['gauge_source_current']=max(maxima['gauge_source_current'],float(np.linalg.norm(gf-source_flux)))
                    maxima['gauge_graph']=max(maxima['gauge_graph'],gr); gauges+=1
                rows.append(dict(n=n,case=case,event=event+1,formation_node_transfer_norm=float(np.linalg.norm(stock)),
                                 candidate_mode_current_divergence_norm=float(np.linalg.norm(before['jF'].sum(axis=1)))))
                k,f,w,y=out['k'],out['f'],out['w'],out['y']
    assert max(maxima.values())<TOL and max_formation_transfer>1e-5 and max_guessed_divergence>1e-3
    return dict(preparations=12,source_events=len(rows),additional_gauge_source_calls=gauges,
                full_source_calls=len(rows)+gauges,maximum_residuals=maxima,
                maximum_actual_formation_node_transfer=max_formation_transfer,
                maximum_failed_mode_current_divergence=max_guessed_divergence,cases=rows)

def run():
    update=audit.load_update()
    return dict(scope='Internal retained graphs and exact channel flux; no physical spatial identification',
                source_blob=audit.EXPECTED_SOURCE_BLOB,seed=SEED,tolerance=TOL,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                exact=exact_checks(),witnesses=source_witnesses(update),full_source=complex_controls(update),
                status='PASS for graph closure and source current identity; guessed mode currents fail; physical spatial current OPEN')

if __name__=='__main__':
    result=run()
    (HERE/'mode_graph_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='cases'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))
