"""Extra-level tangent sensitivity of the BFG two-level sector."""
import json
from pathlib import Path
import numpy as np
import sympy as sp
import audit
import pair_audit

TOL=1e-10

def symbolic():
    s,r,e=sp.symbols('s r e',positive=True)
    a=sp.diag(1,1,-1,-1); bp=sp.diag(1,-1,0,0); bm=sp.diag(0,0,1,-1)
    for sign,b in ((1,bp),(-1,bm)):
        z=sp.eye(4)+r*a+e*b; mu=sp.trace(z*z)/4
        derivative=((mu*sp.eye(4)+z*z)/(2*mu)).diff(e).subs(e,0)
        assert (derivative-(1+sign*r)*b/(1+r*r)).applyfunc(sp.cancel)==sp.zeros(4)
    ym=s*(1-r); yp=s*(1+r)
    alpha=pair_audit.alpha_exact([ym,yp],[sp.Integer(1),sp.Integer(1)])
    gm=pair_audit.g(ym,alpha); gp=pair_audit.g(yp,alpha)
    rows={}; funcs={}; bounds={s:sp.Rational(1,100),r:sp.Rational(1,4)}
    for name,sign,y in (('plus',1,yp),('minus',-1,ym)):
        derivative=2*((1-alpha)*y-alpha)/(1+y)**3
        h=sp.cancel(2*s*r*derivative/(gp-gm))
        assert sp.cancel(h.subs(s,0)-(1+sign*r))==0
        expression=sp.cancel(sp.diff(h,s)/h)
        num,den=map(sp.Poly,sp.fraction(expression))
        def mass(poly):
            return sum(abs(c)*sp.prod(bounds[v]**power for v,power in zip(poly.gens,mon)) for mon,c in poly.terms())
        lower=2*abs(den.eval({v:0 for v in den.gens}))-mass(den); upper=mass(num)
        assert lower>0
        bound=sp.cancel(upper/lower)
        rows[name]=dict(exact_relative_tangent=str(h),numerator_mass=str(upper),denominator_lower=str(lower),rational_log_s_derivative_bound=str(bound),integer_bound=int(sp.ceiling(bound)))
        funcs[name]=sp.lambdify((s,r),h,'numpy')
    return rows,funcs

def growth():
    target=np.sqrt(2)-1; rows=[]
    for index,epsilon in enumerate((.1,.05,.025,.0125)):
        r=epsilon; plus=0.; minus=0.; count=50*4**index
        for _ in range(count):
            plus+=np.log1p(r); minus+=np.log1p(-r); r/=1+r*r
        rows.append(dict(epsilon=epsilon,boundary_steps=count,scaled_log_plus=epsilon*plus,scaled_log_minus=epsilon*minus,plus_error=abs(epsilon*plus-target),minus_error=abs(epsilon*minus+target),log_plus=plus,log_minus=minus))
    for key in ('plus_error','minus_error'):
        assert rows[-1][key]<.02 and rows[-1][key]<.4*rows[0][key]
    return dict(limit_magnitude=float(target),cases=rows)

def source_controls(funcs):
    update=audit.load_update(); rng=np.random.default_rng(20261113)
    u=audit.complex_unitary(rng,4); a=u@np.diag([1,1,-1,-1])@u.conj().T
    bs={'plus':u@np.diag([1,-1,0,0])@u.conj().T,'minus':u@np.diag([0,0,1,-1])@u.conj().T}
    cross=np.zeros((4,4),complex); block=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
    cross[:2,2:]=block; cross[2:,:2]=block.conj().T; cross*=.1/np.linalg.norm(cross,2)
    f=u@(np.eye(4)+cross)@u.conj().T; w=np.eye(4)/4
    z=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); k=z@z.conj().T; k/=np.trace(k)
    mean=lambda m:float(np.trace(f@m).real/np.trace(f).real)
    calls=0; residual=0.; gauge=0.; rows=[]
    for r in (.1,.05):
        for scale in (.001,.0001):
            load=scale*(np.eye(4)+r*a); base=pair_audit.source_aligned(update,k,f,w,load); calls+=1
            aligned=audit.aligned(k,f,load)
            residual=max(residual,float(np.linalg.norm(base['k']-aligned['k'])),float(np.linalg.norm(base['y']-aligned['y'])))
            normalized=base['y']/mean(base['y']); rp=float(np.trace(a@normalized).real/4)
            if r==.1:
                g=audit.complex_unitary(rng,4); conj=lambda x:g@x@g.conj().T
                out=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(load)); calls+=1
                gauge=max(gauge,float(np.linalg.norm(out['y']-conj(base['y']))))
            for name,b in bs.items():
                factor=float(funcs[name](scale,r))
                assert factor>1 if name=='plus' else 0<factor<1
                errors=[]
                for eta in (1e-4,1e-5):
                    outputs=[]
                    for sign in (1,-1):
                        out=pair_audit.source_aligned(update,k,f,w,load+sign*scale*eta*b); calls+=1
                        outputs.append(out['y']/mean(out['y']))
                    derivative=(outputs[0]-outputs[1])/(2*eta)
                    error=float(np.linalg.norm((r/rp)*derivative-factor*b)); errors.append(dict(eta=eta,relative_tangent_error=error))
                assert min(row['relative_tangent_error'] for row in errors)<1e-6
                rows.append(dict(r=r,s=scale,block=name,exact_relative_factor=factor,finite_difference=errors))
    assert calls==38 and max(residual,gauge)<TOL
    return dict(full_source_calls=calls,maximum_base_identity_residual=residual,maximum_gauge_load_residual=gauge,cases=rows)

def run():
    cert,funcs=symbolic()
    return dict(status='PASS: upper-block tangent amplification and lower-block contraction; nonlinear stability OPEN',source_blob=audit.EXPECTED_SOURCE_BLOB,tolerance=TOL,seed=20261113,certificates=cert,boundary_growth=growth(),source=source_controls(funcs),scope='Infinitesimal within-block load directions; no finite-perturbation nonlinear escape claim')

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('extra_level_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
