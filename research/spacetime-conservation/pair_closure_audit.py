"""Non-scalar source exposes the hidden phase of the labelled pair reduction."""
import json
from pathlib import Path
import sympy as sp
import numpy as np
import audit
import pair_audit
from pair_family_audit import real_map,hermitian_basis

def setup():
    F=sp.diag(1,2,4); W=sp.Matrix([[1,0,0],[0,4,-1],[0,-1,4]])/9
    J=sp.zeros(3); J[1,2]=sp.I; J[2,1]=-sp.I
    L=sp.zeros(3); L[0,2]=sp.I; L[2,0]=-sp.I
    ps=[sp.diag(1,1,0),sp.Matrix([[1,0,0],[0,sp.Rational(4,5),sp.Rational(2,5)],[0,sp.Rational(2,5),sp.Rational(1,5)]]),sp.Matrix([[1,0,0],[0,sp.Rational(1,2),sp.Rational(1,2)],[0,sp.Rational(1,2),sp.Rational(1,2)]])]
    return F,W,J,L,ps

def factors(e):
    ys=[sp.Rational(1,10)-e,sp.Rational(1,10)+e,sp.Rational(3,20)]
    alpha=pair_audit.alpha_exact(ys,[sp.Rational(3,2),sp.Rational(3,2),sp.Integer(4)]); beta=1-alpha
    hs=[sp.cancel((alpha+beta*y*ys[2])**2/((alpha+beta*y*y)*(alpha+beta*ys[2]**2))) for y in ys[:2]]
    return ys,alpha,hs

def symbolic():
    F,W,J,L,ps=setup(); assert sp.I*(F*W-W*F)==sp.Rational(2,9)*J
    mapping=real_map(ps); row=sp.Matrix([[sp.trace(sp.I*(F*W-W*F)*h) for h in hermitian_basis()]])
    assert mapping.rank()==8 and mapping.col_join(row).rank()==9
    for sign in (-1,1):assert sp.trace(sp.I*(F*W-W*F)*(sp.eye(3)/3+sign*J/12))==sign*sp.Rational(1,27)
    ys,alpha,hs=factors(sp.Rational(1,100)); assert hs[1]-hs[0]>0
    hm,hp=sp.symbols('hm hp',real=True); phi=(hp-hm)*L/2+(hp+hm)*J/2
    difference=ps[2]*phi*ps[2]/6
    assert sp.simplify(sp.trace(difference*difference)-(hp-hm)**2/144)==0
    return dict(exact_alpha=str(alpha),h_plus_squared_minus_h_minus_squared=str(sp.cancel(hs[1]-hs[0])),source_hidden_phase='Phi(J)=(h_plus-h_minus)J13/2+(h_plus+h_minus)J23/2',output_W_image_distance='(h_plus-h_minus)/12 >0',native_completion='i[F,W]=(2/9)J; tr(i[F,W]K±)=±1/27',initial_image_rank=8,completed_image_rank=9)

def source():
    update=audit.load_update(); rng=np.random.default_rng(20261127); F,W,J,L,ps=setup()
    F,W,J,L=map(lambda x:np.array(x,dtype=complex),(F,W,J,L)); ps=[np.array(p,dtype=complex) for p in ps]
    calls=0; kr=0.; ir=0.; fr=0.; gr=0.; initial=0.; rows=[]
    for ev in (sp.Rational(1,200),sp.Rational(1,100),sp.Rational(1,50)):
        e=float(ev); Y=np.array([[.1,e,0],[e,.1,0],[0,0,.15]],complex); ys,alpha,hs=factors(ev); hm,hp=[float(sp.sqrt(h)) for h in hs]
        assert float(ys[0])>=2*float(ys[-1])**2 and all(float(y)>0 for y in ys)
        phi=(hp-hm)*L/2+(hp+hm)*J/2; outputs=[]
        for sign in (-1,1):
            K=np.eye(3)/3+sign*J/12; assert np.linalg.eigvalsh(K).min()>0
            for p in ps:initial=max(initial,float(np.linalg.norm(p@(K-np.eye(3)/3)@p)))
            out=pair_audit.source_aligned(update,K,F,W,Y); calls+=1; outputs.append(out)
            kr=max(kr,float(np.linalg.norm(out['k']-(np.eye(3)/3+sign*phi/12))))
            fr=max(fr,float(np.linalg.norm(out['f']-F)),float(np.linalg.norm(out['w']-W)))
            if ev==sp.Rational(1,100):
                g=audit.complex_unitary(rng,3); conj=lambda z:g@z@g.conj().T
                gout=pair_audit.source_aligned(update,conj(K),conj(F),conj(W),conj(Y)); calls+=1
                gr=max(gr,float(np.linalg.norm(gout['k']-conj(out['k']))),float(np.linalg.norm(gout['y']-conj(out['y']))))
                for p in ps:gr=max(gr,float(np.linalg.norm(conj(p)@gout['k']@conj(p)-conj(p@out['k']@p))))
        difference=outputs[1]['k']-outputs[0]['k']; observed=float(np.linalg.norm(ps[2]@difference@ps[2])); expected=(hp-hm)/12
        assert expected>0 and observed>expected/2
        ir=max(ir,abs(observed-expected)); fr=max(fr,float(np.linalg.norm(outputs[0]['y']-outputs[1]['y'])))
        rows.append(dict(load_coupling=e,h_minus=hm,h_plus=hp,initial_labelled_images_equal=True,output_W_image_distance=observed,exact_prediction=expected,commutator_completion_values=[-1/27,1/27]))
    assert calls==8 and max(kr,ir,fr,gr,initial)<1e-10
    return dict(calls=calls,kernel_residual=kr,image_separation_residual=ir,field_residual=fr,gauge_residual=gr,initial_fibre_residual=initial,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS: labelled pair reduction fails non-scalar fibre closure; native full-kernel completion identified',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261127,symbolic=symbolic(),source=source(),scope='Counterexample for this rank-eight pair-image reduction, not every reduction or BFG. Adding one native commutator scalar restores nine real kernel coordinates in this example, not a four-dimensional physical carrier.')
    Path(__file__).with_name('pair_closure_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
