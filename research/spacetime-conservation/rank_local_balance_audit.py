"""Local adjoint accounting through actual rectangular seed/rank events."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import audit

def symbolic():
    v=sp.Matrix([sp.sqrt(3)/2,sp.Rational(1,2),0]); P=v*v.T; Y=sp.diag(sp.Rational(1,5),sp.Rational(2,5),sp.Rational(3,5)); K=-sp.diag(2,3,5)
    assert P*P==P and sp.trace(P)==1
    assert P.col_join(P*Y).rank()==2
    D=2*P; assert sorted((sp.eye(3)-D).eigenvals())==[-1,1]
    assert sp.trace(K*(D-sp.eye(3)))==sp.Rational(11,2)
    assert sp.trace(K*(D-P))==-sp.Rational(9,4)
    return dict(local_pullback='B_a=sum U_r Eout_a U_r†; Delta q_a=tr K(B_a-Ein_a)',ambient_total='tr K(D-I)',active_total='tr K(sum U_r Pplus U_r†-P)',witness_analysis_rank=2,witness_D='2P',witness_export_eigenvalues=['-1','1','1'],witness_ambient_change='11/2',witness_active_change='-9/4')

def local(k,p,out):
    n=len(k); m=len(out['k']); ops=[out['u'][:n,:],out['u'][n:,:]]
    eig,u=np.linalg.eigh(out['f']); assert m==1 or np.min(np.diff(eig))>1e-8
    effects=[np.outer(u[:,j],u[:,j].conj()) for j in range(m)]
    D=sum(t@t.conj().T for t in ops); dp=sum(t@out['p']@t.conj().T for t in ops)
    residual=0.; ambient=[]; active=[]; pulls=[]
    norm=max(1.,float(np.linalg.norm(k)))
    for e in effects:
        B=sum(t@e@t.conj().T for t in ops); ea=out['p']@e@out['p']; Ba=sum(t@ea@t.conj().T for t in ops)
        qa=float(np.trace(e@out['k']).real); qi=float(np.trace(k).real/m)
        aa=float(np.trace(ea@out['k']).real); ai=float(np.trace(p@k).real/m)
        residual=max(residual,abs(qa-qi-np.trace(k@(B-np.eye(n)/m)).real)/norm,abs(aa-ai-np.trace(k@(Ba-p/m)).real)/norm)
        ambient.append(qa); active.append(aa); pulls.append(B)
    amb=float(np.trace(out['k']).real-np.trace(k).real); act=float(np.trace(out['p']@out['k']).real-np.trace(p@k).real)
    residual=max(residual,abs(amb-np.trace(k@(D-np.eye(n))).real)/norm,abs(act-np.trace(k@(dp-p)).real)/norm)
    return dict(residual=residual,D=D,pulls=pulls,ambient=np.array(ambient),active=np.array(active),ambient_change=amb,active_change=act,output_dimension=m,output_carrier_rank=int(round(np.trace(out['p']).real)),export_eigenvalues=np.linalg.eigvalsh(np.eye(n)-D).tolist())

def source():
    update=audit.load_update(); rng=np.random.default_rng(20261130); v=np.array([np.sqrt(3)/2,.5,0.]); p=np.outer(v,v); y=np.diag([.2,.4,.6]); k=-np.diag([2.,3.,5.])
    out=update(k,p,p,y,p); calls=1; assert out['terminal'] is None
    witness=local(k,p,out); wr=max(witness['residual'],float(np.linalg.norm(witness['D']-2*p)),abs(witness['ambient_change']-5.5),abs(witness['active_change']+2.25))
    assert witness['output_dimension']==2 and witness['output_carrier_rank']==2
    records=[]; residual=0.; gauge=0.; gauges=0
    for n in (3,4,5):
        for case in range(2):
            u=audit.complex_unitary(rng,n); rank=n//2; p=u[:,:rank]@u[:,:rank].conj().T
            q=audit.complex_unitary(rng,n); y=(q*np.linspace(.15,.7,n))@q.conj().T
            f=p@audit.pos(rng,n)@p; w=p/rank; k=-audit.pos(rng,n)
            out=update(k,f,w,y,p); calls+=1
            record=dict(n=n,case=case,input_carrier_rank=rank,terminal=out['terminal'])
            if out['terminal'] is not None:records.append(record); continue
            b=local(k,p,out); residual=max(residual,b['residual'])
            record.update(output_dimension=b['output_dimension'],output_carrier_rank=b['output_carrier_rank'],ambient_change=b['ambient_change'],active_change=b['active_change'],export_eigenvalues=b['export_eigenvalues'])
            if case==0:
                g=audit.complex_unitary(rng,n); conj=lambda z:g@z@g.conj().T
                gout=update(conj(k),conj(f),conj(w),conj(y),conj(p)); calls+=1; gauges+=1; assert gout['terminal'] is None
                gb=local(conj(k),conj(p),gout)
                gauge=max(gauge,gb['residual'],float(np.linalg.norm(gb['ambient']-b['ambient'])),float(np.linalg.norm(gb['active']-b['active'])),float(np.linalg.norm(gb['D']-conj(b['D']))))
                for x,z in zip(gb['pulls'],b['pulls']):gauge=max(gauge,float(np.linalg.norm(x-conj(z))))
            records.append(record)
    assert calls==7+gauges and any(x['terminal'] is None for x in records) and max(wr,residual,gauge)<1e-10
    return dict(calls=calls,nonterminal_random=sum(x['terminal'] is None for x in records),terminal_random=sum(x['terminal'] is not None for x in records),local_residual=residual,gauge_residual=gauge,witness_residual=wr,witness=dict(input_dimension=3,input_carrier_rank=1,output_dimension=witness['output_dimension'],output_carrier_rank=witness['output_carrier_rank'],ambient_change=witness['ambient_change'],active_change=witness['active_change'],export_eigenvalues=witness['export_eigenvalues']),cases=records)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261130,symbolic=symbolic(),source=source(),scope='Exact local rectangular pullback balances for complete nonterminal source events, distinguishing ambient kernel and active carrier. No terminal successor, positive energy reservoir, or full four-current invented.')
    Path(__file__).with_name('rank_local_balance_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
