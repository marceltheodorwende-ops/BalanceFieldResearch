"""Finite three-level boundary splitting and exact source monotonicity checks."""
import json
import math
from pathlib import Path
import numpy as np
import sympy as sp
import audit
import pair_audit

TOL=1e-10

def symbolic():
    r,b,q=sp.symbols('r b q',positive=True)
    a=sp.diag(1,1,-1,-1)
    for sign,block in ((1,sp.diag(1,-1,0,0)),(-1,sp.diag(0,0,1,-1))):
        z=sp.eye(4)+r*a+b*block; mu=sp.trace(z*z)/4
        nxt=(mu*sp.eye(4)+z*z)/(2*mu)
        assert sp.cancel(sp.trace(a@nxt)/4-(r+sign*b*b/4)/(1+r*r+b*b/2))==0
        assert sp.cancel(sp.trace(block@nxt)/2-(1+sign*r)*b/(1+r*r+b*b/2))==0
    upper=q*(1+r)/(1+q*q*r/4)
    lower=q*(1-r)/(1-q*q*r/4)
    assert sp.cancel(2-upper-(2-q)*(1-q*r/2)/(1+q*q*r/4))==0
    assert sp.cancel(q-lower-q*r*(1-q*q/4)/(1-q*q*r/4))==0
    assert sp.Rational(9,4)+sp.Rational(81,64)*sp.Rational(1,100)<sp.Rational(5,2)
    assert sp.Rational(24,65)>sp.Rational(1,3)
    return dict(mu='1+r**2+b**2/2',r_successor='(r+sigma*b**2/4)/mu',b_successor='(1+sigma*r)*b/mu',upper_relative='q*(1+r)/(1+q**2*r/4)',lower_relative='q*(1-r)/(1-q**2*r/4)',comparison_inverse_square_increment='14481/6400 < 5/2')

def step(r,b,sign):
    mu=1+r*r+b*b/2
    return (r+sign*b*b/4)/mu,(1+sign*r)*b/mu

def boundary_controls():
    rows=[]
    for index,epsilon in enumerate((.1,.05,.025,.0125)):
        q0=epsilon**2; bound=math.ceil(math.log(.5/q0)/math.log1p(epsilon/3)); horizon=200*4**index
        assert bound<=horizon
        r=epsilon; b=r*q0; event=0
        while r<.25 and b/r<.5 and event<horizon:
            q=b/r
            assert r+TOL>=epsilon/math.sqrt(1+2.5*event*epsilon**2)
            rn,bn=step(r,b,1)
            assert bn/rn+TOL>=q*(1+epsilon/3)
            r,b=rn,bn; event+=1
        assert event<=bound and (r>=.25 or b/r>=.5)
        upper=dict(exit_step=event,exit_type='relative_width' if b/r>=.5 else 'main_contrast',r=r,q=b/r)
        r=epsilon; b=r*q0
        for _ in range(horizon):
            oldq=b/r; oldr=r; r,b=step(r,b,-1)
            assert 0<r<=oldr+TOL and 0<b/r<=oldq+TOL and b/r<=q0+TOL
        rows.append(dict(epsilon=epsilon,initial_relative_width=q0,boundary_horizon=horizon,proved_exit_upper_bound=bound,upper=upper,lower=dict(r=r,q=b/r,stays_in_cone=True)))
    return rows

def source_controls():
    update=audit.load_update(); rng=np.random.default_rng(20261114)
    u=audit.complex_unitary(rng,4); av=np.array([1.,1.,-1.,-1.]); a=(u*av)@u.conj().T
    basis={1:np.array([1.,-1.,0.,0.]),-1:np.array([0.,0.,1.,-1.])}
    block={sign:(u*v)@u.conj().T for sign,v in basis.items()}
    cross=np.zeros((4,4),complex); z=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
    cross[:2,2:]=z; cross[2:,:2]=z.conj().T; cross*=.1/np.linalg.norm(cross,2)
    f=u@(np.eye(4)+cross)@u.conj().T; w=np.eye(4)/4
    z=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); k=z@z.conj().T; k/=np.trace(k)
    calls=0; maximum=0.; normalized=0.; gauge=0.; rows=[]
    for r in (.1,.05):
        for q in (.1,.5):
            for sign in (1,-1):
                b=r*q
                for scale in (.001,.0001):
                    exact_r,exact_b,exact_s=map(lambda v:sp.Rational(str(v)),(r,b,scale))
                    zv=[1+exact_r*v+exact_b*sp.Integer(int(bv)) for v,bv in zip((1,1,-1,-1),basis[sign])]
                    ys=[exact_s*v for v in zv]; alpha=pair_audit.alpha_exact(ys,[sp.Integer(1)]*4)
                    vals=[sp.cancel(pair_audit.g(v,alpha)) for v in ys]
                    expected=(u*np.array([float(v) for v in vals]))@u.conj().T
                    load=scale*(np.eye(4)+r*a+b*block[sign])
                    out=pair_audit.source_aligned(update,k,f,w,load); calls+=1
                    maximum=max(maximum,float(np.linalg.norm(out['y']-expected)))
                    source_z=out['y']/(np.trace(out['y']).real/4)
                    rn=float(np.trace(a@source_z).real/4); bn=float(np.trace(block[sign]@source_z).real/2); qn=bn/rn
                    ez=expected/(np.trace(expected).real/4)
                    normalized=max(normalized,abs(rn-float(np.trace(a@ez).real/4)),abs(bn-float(np.trace(block[sign]@ez).real/2)))
                    assert 0<qn<2 and (qn>q if sign==1 else qn<q)
                    if r==.1 and q==.1 and sign==1:
                        g=audit.complex_unitary(rng,4); conj=lambda x:g@x@g.conj().T
                        gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(load)); calls+=1
                        gauge=max(gauge,float(np.linalg.norm(gout['y']-conj(out['y']))))
                    rows.append(dict(r=r,q=q,s=scale,split_block='upper' if sign==1 else 'lower',source_relative_width=qn))
    assert calls==18 and max(maximum,gauge)<TOL and normalized<1e-8
    return dict(full_source_calls=calls,maximum_rational_source_load_residual=maximum,maximum_normalized_coordinate_residual=normalized,maximum_gauge_load_residual=gauge,cases=rows)

def run():
    return dict(status='PASS: finite nonlinear boundary exit above and invariant contraction cone below',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,normalized_tolerance=1e-8,seed=20261114,symbolic=symbolic(),boundary=boundary_controls(),source=source_controls(),scope='Nonlinear quantitative exit is a boundary theorem; positive-load monotonicity is exact, long-source exit rate OPEN')

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('finite_splitting_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
