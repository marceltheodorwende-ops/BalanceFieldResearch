"""Real-linear information in labelled competing pair compressions."""
import json
from pathlib import Path
import sympy as sp
import numpy as np
import audit
import pair_audit

def hermitian_basis():
    basis=[]
    for i in range(3):
        m=sp.zeros(3); m[i,i]=1; basis.append(m)
    for i,j in ((0,1),(0,2),(1,2)):
        m=sp.zeros(3); m[i,j]=m[j,i]=1; basis.append(m)
        m=sp.zeros(3); m[i,j]=sp.I; m[j,i]=-sp.I; basis.append(m)
    return basis

def real_map(projectors):
    columns=[]
    for h in hermitian_basis():
        column=[]
        for p in projectors:
            block=p*h*p
            column.extend(sp.re(x) for x in block)
            column.extend(sp.im(x) for x in block)
        columns.append(sp.Matrix(column))
    return sp.Matrix.hstack(*columns)

def symbolic():
    pf=sp.diag(1,1,0); pw=sp.Matrix([[1,0,0],[0,sp.Rational(1,2),sp.Rational(1,2)],[0,sp.Rational(1,2),sp.Rational(1,2)]])
    p12=sp.Matrix([[1,0,0],[0,sp.Rational(4,5),sp.Rational(2,5)],[0,sp.Rational(2,5),sp.Rational(1,5)]])
    J=sp.zeros(3); J[1,2]=sp.I; J[2,1]=-sp.I
    mapping=real_map([pf,p12,pw]); null=mapping.nullspace()
    assert mapping.rank()==8 and len(null)==1
    recovered=sum((c*h for c,h in zip(null[0],hermitian_basis())),sp.zeros(3)); assert recovered==J
    coordinate=real_map([pf,sp.diag(1,0,1),sp.diag(0,1,1)]); assert coordinate.rank()==9
    for sign in (-1,1):
        K=sp.eye(3)/3+sign*J/12
        assert sorted(K.eigenvals())==[sp.Rational(1,4),sp.Rational(1,3),sp.Rational(5,12)]
    t=sp.symbols('t',nonnegative=True); p=sp.zeros(3); p[0,0]=1; p[1:3,1:3]=(sp.eye(2)+sp.Matrix([[1,t/9],[t/9,-1]])/sp.sqrt(1+t*t/81))/2
    assert sp.simplify(p*J*p)==sp.zeros(3)
    for projector in (pf,p12,pw):assert projector*J*projector==sp.zeros(3)
    return dict(candidate_family_real_rank=8,kernel_real_dimension=1,invisible_direction='i(|2><3|-|3><2|)',positive_fibre_eigenvalues=['1/4','1/3','5/12'],coordinate_pair_real_rank=9,full_labelled_family='injective on Herm(C^n), real dimension n²',trace_one_visible_dimensions=dict(candidate_family=7,all_pairs=8))

def source():
    update=audit.load_update(); rng=np.random.default_rng(20261126); F=np.diag([1.,2.,4.]); W=np.array([[1.,0,0],[0,4.,-1.],[0,-1.,4.]])/9
    J=np.zeros((3,3),complex); J[1,2]=1j; J[2,1]=-1j
    ps=[np.diag([1.,1.,0.]),np.array([[1.,0,0],[0,.8,.4],[0,.4,.2]]),np.array([[1.,0,0],[0,.5,.5],[0,.5,.5]])]
    cr=0.; hr=0.; fr=0.; gr=0.; calls=0; rows=[]
    for index,y in enumerate((.05,.1,.2)):
        outputs=[]
        for sign in (-1,1):
            K=np.eye(3)/3+sign*J/12; Y=y*np.eye(3); out=pair_audit.source_aligned(update,K,F,W,Y); calls+=1; outputs.append(out)
            assert np.linalg.eigvalsh(K).min()>0
            hr=max(hr,float(np.linalg.norm(out['k']-K)))
            fr=max(fr,float(np.linalg.norm(out['f']-F)),float(np.linalg.norm(out['w']-W)))
            for p in ps:cr=max(cr,float(np.linalg.norm(p@out['k']@p-p@(np.eye(3)/3)@p)))
            if index==0:
                g=audit.complex_unitary(rng,3); conj=lambda z:g@z@g.conj().T
                gout=pair_audit.source_aligned(update,conj(K),conj(F),conj(W),conj(Y)); calls+=1
                gr=max(gr,float(np.linalg.norm(gout['k']-conj(out['k']))))
                for p in ps:gr=max(gr,float(np.linalg.norm(conj(p)@gout['k']@conj(p)-conj(p@out['k']@p))))
        difference=outputs[1]['k']-outputs[0]['k']; hr=max(hr,float(np.linalg.norm(difference-J/6)))
        for p in ps:cr=max(cr,float(np.linalg.norm(p@difference@p)))
        rows.append(dict(input_y=y,hidden_kernel_distance=float(np.linalg.norm(difference)),predicted_distance=float(np.sqrt(2)/6),identical_labelled_images=True,original_carrier_rank=3))
    assert calls==8 and max(cr,hr,fr,gr)<1e-10
    return dict(calls=calls,compression_residual=cr,hidden_state_residual=hr,field_residual=fr,gauge_residual=gr,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261126,symbolic=symbolic(),source=source(),scope='Labelled competing sector family need not be a four-real-dimensional carrier; full labelled rank-two family retains all kernel data. The displayed invisible fibre stays closed in this scalar sector.')
    Path(__file__).with_name('pair_family_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
