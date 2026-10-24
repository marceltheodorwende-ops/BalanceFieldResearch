"""Source-derived relational pair frames, not physical spatial transport."""
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
SEED=20261028

def frame(y,reference):
    eig,vec=np.linalg.eigh(y)
    p=[np.outer(vec[:,i],vec[:,i].conj()) for i in (0,1)]
    identity=p[0]+p[1]; z=p[0]-p[1]
    off=p[0]@reference@p[1]+p[1]@reference@p[0]
    amplitude=float(np.linalg.norm(off)/np.sqrt(2))
    if amplitude<1e-12:
        raise ValueError('Reference chart undefined or below audit resolution')
    x=off/amplitude
    return [identity,x,-1j*z@x,z],eig[:2],amplitude

def coordinates(basis,k):
    return np.array([np.trace(e@k).real/2 for e in basis])

def frame_residual(basis):
    eye,x,y,z=basis
    residuals=[np.linalg.norm(e-e.conj().T) for e in basis]
    for i in range(4):
        for j in range(4):
            residuals.append(abs(np.trace(basis[i]@basis[j])-2*(i==j)))
    for e in (x,y,z): residuals.append(np.linalg.norm(e@e-eye))
    for a,b,c in ((x,y,z),(y,z,x),(z,x,y)):
        residuals.append(np.linalg.norm(a@b-1j*c))
    return float(max(residuals))

def exact_checks():
    eye=s.eye(2); z=s.diag(1,-1)
    f=s.Matrix([[1,(3+4*s.I)/10],[(3-4*s.I)/10,1]])
    w=s.Matrix([[s.Rational(1,3),(1-2*s.I)/30],[(1+2*s.I)/30,s.Rational(1,3)]])
    k=s.Matrix([[2,1-2*s.I],[1+2*s.I,-1]])
    def exact_basis(reference):
        off=reference-s.diag(reference[0,0],reference[1,1])
        a=s.simplify(s.sqrt(s.trace(off*off)/2))
        x=off/a
        return [eye,x,-s.I*z*x,z],a
    ef,af=exact_basis(f); ew,aw=exact_basis(w)
    for basis in (ef,ew):
        for e in basis: assert s.simplify(e-e.conjugate().T)==s.zeros(2)
        for e in basis[1:]: assert s.simplify(e*e-eye)==s.zeros(2)
        assert s.simplify(basis[1]*basis[2]-s.I*z)==s.zeros(2)
    pf=[s.simplify(s.trace(e*k)/2) for e in ef]
    pw=[s.simplify(s.trace(e*k)/2) for e in ew]
    assert pf==[s.Rational(1,2),-1,2,s.Rational(3,2)]
    assert pw==[s.Rational(1,2),s.sqrt(5),0,s.Rational(3,2)]
    phase=s.simplify(f[0,1]*w[1,0]/(af*aw))
    c=s.simplify(s.re(phase)); sn=s.simplify(s.im(phase))
    assert s.simplify(c*c+sn*sn-1)==0
    assert s.simplify(ew[1]-c*ef[1]-sn*ef[2])==s.zeros(2)
    assert s.simplify(ew[2]+sn*ef[1]-c*ef[2])==s.zeros(2)
    assert min(f.eigenvals())>0 and all(v>0 for v in w.eigenvals())
    ys=[s.Rational(1,5),s.Rational(1,4),s.Rational(3,10)]
    alpha=pair_audit.alpha_exact(ys,[1,1,1]); beta=1-alpha
    h2=s.cancel((alpha+beta*ys[0]*ys[1])**2/
                ((alpha+beta*ys[0]**2)*(alpha+beta*ys[1]**2)))
    assert alpha==s.Rational(119,1993) and h2==s.Rational(9048258,9159761)
    # Both phase paths have the same diagonal limit but different normalized frames.
    a=s.Rational(1,10); b=s.Rational(1,1000)
    path_frames=[]
    for epsilon in (a,b):
        real,_=exact_basis(s.Matrix([[1,epsilon],[epsilon,1]]))
        imag,_=exact_basis(s.Matrix([[1,s.I*epsilon],[-s.I*epsilon,1]]))
        assert s.trace((real[1]-imag[1])**2)==4
        path_frames.append(dict(epsilon=str(epsilon),squared_frame_distance='4'))
    return dict(formation_amplitude=str(af),witness_amplitude=str(aw),
                formation_coordinates=list(map(str,pf)),witness_coordinates=list(map(str,pw)),
                relative_phase=str(phase),relative_rotation_cos=str(c),relative_rotation_sin=str(sn),
                alpha=str(alpha),h_squared=str(h2),phase_boundary_paths=path_frames)

def source_witnesses(update,exact):
    y=np.diag([.2,.25,.3]); f=np.eye(3,dtype=complex)
    f[0,1]=.3+.4j; f[1,0]=.3-.4j
    w=np.eye(3,dtype=complex)/3; w[0,1]=(1-2j)/30; w[1,0]=(1+2j)/30
    k=np.diag([2.,-1.,0.]).astype(complex); k[0,1]=1-2j; k[1,0]=1+2j
    rows=[]
    for fallback in (False,True):
        formation=np.eye(3) if fallback else f
        reference=w if fallback else formation
        basis,_,_=frame(y,reference)
        out=pair_audit.source_aligned(update,k,formation,w,y)
        next_basis,_,_=frame(out['y'],out['w'] if fallback else out['f'])
        p=coordinates(basis,k); pp=coordinates(next_basis,out['k'])
        h=np.sqrt(float(s.Rational(exact['h_squared'])))
        residual=float(np.linalg.norm(pp-p*np.array([1,h,h,1])))
        assert residual<TOL
        if fallback:
            try: frame(y,formation)
            except ValueError: pass
            else: raise AssertionError('Diagonal formation must not define a transverse chart')
        rows.append(dict(witness_fallback=fallback,input_coordinates=p.tolist(),
                         successor_coordinates=pp.tolist(),component_residual=residual))
    return dict(full_source_calls=2,cases=rows)

def complex_controls(update):
    rng=np.random.default_rng(SEED)
    maxima=dict(pauli=0.,frame_transport=0.,component_update=0.,reference_coordinates=0.,
                gauge_frame=0.,gauge_components=0.,reference_rotation=0.)
    minimum_amplitude=float('inf'); rows=[]; gauge_calls=0
    for n in (3,4,5,6):
        for case in range(3):
            u=audit.complex_unitary(rng,n)
            y=(u*np.linspace(.2,.3,n))@u.conj().T
            f=audit.pos(rng,n); w=audit.pos(rng,n); w/=np.trace(w).real
            raw=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)); k=(raw+raw.conj().T)/2
            for event in range(2):
                basis,ys,amplitude=frame(y,f); wbasis,_,wa=frame(y,w)
                minimum_amplitude=min(minimum_amplitude,amplitude)
                p=coordinates(basis,k); wf=coordinates(basis,w)
                c,sn=wf[1]/wa,wf[2]/wa
                rotation=max(np.linalg.norm(wbasis[1]-c*basis[1]-sn*basis[2]),
                             np.linalg.norm(wbasis[2]+sn*basis[1]-c*basis[2]))
                out=update(k,f,w,y,np.eye(n))
                assert out['terminal'] is None
                next_basis,_,next_amp=frame(out['y'],out['f'])
                pnext=coordinates(next_basis,out['k'])
                alpha=out['alpha']; beta=1-alpha
                h=(alpha+beta*ys[0]*ys[1])/np.sqrt((alpha+beta*ys[0]**2)*(alpha+beta*ys[1]**2))
                v=out['v']
                transport=max(np.linalg.norm(next_basis[i]-v.conj().T@basis[i]@v) for i in range(4))
                reference=max(np.linalg.norm(coordinates(next_basis,out['f'])-coordinates(basis,f)),
                              np.linalg.norm(coordinates(next_basis,out['w'])-wf),abs(next_amp-amplitude))
                component=np.linalg.norm(pnext-p*np.array([1,h,h,1]))
                maxima['pauli']=max(maxima['pauli'],frame_residual(basis),frame_residual(next_basis))
                maxima['frame_transport']=max(maxima['frame_transport'],float(transport))
                maxima['component_update']=max(maxima['component_update'],float(component))
                maxima['reference_coordinates']=max(maxima['reference_coordinates'],float(reference))
                maxima['reference_rotation']=max(maxima['reference_rotation'],float(rotation))
                if case==0:
                    g=audit.complex_unitary(rng,n); conjugate=lambda x:g@x@g.conj().T
                    gbasis,_,_=frame(conjugate(y),conjugate(f))
                    gauge_frame=max(np.linalg.norm(gbasis[i]-conjugate(basis[i])) for i in range(4))
                    gout=update(conjugate(k),conjugate(f),conjugate(w),conjugate(y),np.eye(n))
                    assert gout['terminal'] is None
                    obasis,_,_=frame(gout['y'],gout['f'])
                    gauge_component=np.linalg.norm(coordinates(obasis,gout['k'])-pnext)
                    maxima['gauge_frame']=max(maxima['gauge_frame'],float(gauge_frame))
                    maxima['gauge_components']=max(maxima['gauge_components'],float(gauge_component))
                    gauge_calls+=1
                rows.append(dict(n=n,case=case,event=event+1,formation_amplitude=amplitude,
                                 frame_transport_residual=float(transport),component_residual=float(component)))
                k,f,w,y=out['k'],out['f'],out['w'],out['y']
    assert max(maxima.values())<TOL
    return dict(preparations=12,source_events=len(rows),additional_gauge_source_calls=gauge_calls,
                full_source_calls=len(rows)+gauge_calls,minimum_formation_amplitude=minimum_amplitude,
                maximum_residuals=maxima,cases=rows)

def run():
    update=audit.load_update(); exact=exact_checks()
    return dict(scope='Stable spectral pair with nonzero formation or witness reference; internal frame only',
                source_blob=audit.EXPECTED_SOURCE_BLOB,seed=SEED,tolerance=TOL,
                runtime=dict(python=platform.python_version(),numpy=np.__version__,sympy=s.__version__),
                exact=exact,source_witnesses=source_witnesses(update,exact),full_source=complex_controls(update),
                status='PASS for relational frame and internal transport; physical space/current/Einstein OPEN')

if __name__=='__main__':
    result=run()
    (HERE/'relational_frame_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:({a:b for a,b in v.items() if a!='cases'} if isinstance(v,dict) else v)
                      for k,v in result.items()},indent=2))
