"""Finite upper splitting: stopped lower-pair coherence control."""
import json
from pathlib import Path
import sympy as sp
import numpy as np
import mpmath as mp
import audit
import pair_audit

def certificate():
    s,r,p,q,t=sp.symbols('s r p q t'); rho=1+t
    zs=[1+r+r*p,1+r-r*p,1-r+r*q,1-r-r*q]
    gs=[(rho+z*z)/(1+s*z)**2 for z in zs]
    # Factors common to all output eigenvalues cancel in q_next.
    L=sp.cancel((1-2*(gs[2]-gs[3])/(q*(gs[0]+gs[1]-gs[2]-gs[3])))/r)
    num,den=sp.fraction(sp.cancel(L-sp.Rational(1,2)))
    origin={s:0,r:0,p:0,q:0,t:0}
    if den.subs(origin)<0:num,den=-num,-den
    bounds={s:sp.Rational(1,100),r:sp.Rational(1,4),p:sp.Rational(1,2),q:sp.Rational(1,2),t:sp.Integer(1)}
    def enclose(expr):
        poly=sp.Poly(expr,s,r,p,q,t); mass=sum(abs(c)*sp.prod(bounds[v]**k for v,k in zip(poly.gens,mon)) for mon,c in poly.terms())
        return sp.cancel(2*poly.coeff_monomial(1)-mass),sp.cancel(mass)
    nl,nu=enclose(num); dl,du=enclose(den)
    row=dict(numerator_lower=str(nl),numerator_mass=str(nu),denominator_lower=str(dl),denominator_mass=str(du),rho_interval='[0,2] encloses [25/64,121/64]')
    assert nl>0 and dl>0,row
    assert sp.cancel(L.subs(s,0)-(1+(p*p-q*q)/4)/(1+r*(p*p-q*q)/4))==0
    return row

def symbolic():
    r,a,b=sp.symbols('r a b'); mu=1+r*r+(a*a+b*b)/2
    z=[1+r+a,1+r-a,1-r+b,1-r-b]; g=[mu+x*x for x in z]; total=sum(g)
    rn=(r+(a*a-b*b)/4)/mu; an=(1+r)*a/mu; bn=(1-r)*b/mu
    assert sp.cancel((g[0]+g[1]-g[2]-g[3])/total-rn)==0
    assert sp.cancel(2*(g[0]-g[1])/total-an)==0
    assert sp.cancel(2*(g[2]-g[3])/total-bn)==0
    ys=[sp.Rational(1,1000)*zv.subs({r:sp.Rational(1,10),a:sp.Rational(1,20),b:sp.Rational(1,100)}) for zv in z]
    alpha=pair_audit.alpha_exact(ys,[sp.Integer(1)]*4); exact_g=[pair_audit.g(y,alpha) for y in ys]
    upper_ratio=sp.cancel(2*(exact_g[0]-exact_g[1])/(exact_g[0]+exact_g[1]-exact_g[2]-exact_g[3]))
    assert upper_ratio>sp.Rational(1,2)
    return dict(mu=str(mu),r_next=str(rn),a_next=str(an),b_next=str(bn),positive_source_exit_witness=dict(r='1/10',p='1/2',q='1/10',s='1/1000',p_next=str(upper_ratio)),scope='boundary identities and exact positive-load exit witness')

def step(s,r,a,b):
    zs=[1+r+a,1+r-a,1-r+b,1-r-b]
    rho=sum(z*z/(1+s*z) for z in zs)/sum(1/(1+s*z) for z in zs)
    g=[(rho+z*z)/(1+s*z)**2/(1+s*s*rho) for z in zs]; total=sum(g)
    h=(rho+(1-r)**2-b*b)/mp.sqrt((rho+(1-r)**2-b*b)**2+4*rho*b*b)
    return s*s*total/4,(g[0]+g[1]-g[2]-g[3])/total,2*(g[0]-g[1])/total,2*(g[2]-g[3])/total,h

def prefixes():
    mp.mp.dps=500; rows=[]
    for pv in ('.1','.5'):
        for qv in ('.1','.5'):
            s=mp.mpf('.001'); r=mp.mpf('.1'); a=r*mp.mpf(pv); b=r*mp.mpf(qv); u0=(b/r)**2
            total=mp.mpf(0); product=mp.mpf(1); history=[]; exited=False
            for event in range(6):
                oldr=r; oldq=b/r; oldb=b
                assert r<=mp.mpf('.25') and a/r<=mp.mpf('.5') and b/r<=mp.mpf('.5') and s<=mp.mpf('.01')
                s,r,a,b,h=step(s,r,a,b)
                assert 0<b/r<=oldq*(1-oldr/2) and oldq**2-(b/r)**2>=2*oldb**2
                total+=oldb**2; product*=h
                assert total+(b/r)**2/2<=u0/2 and 1-product<=mp.mpf(32)/35*total
                exited=r>mp.mpf('.25') or a/r>mp.mpf('.5') or b/r>mp.mpf('.5') or s>mp.mpf('.01')
                history.append(dict(event=event+1,s=mp.nstr(s,18),r=mp.nstr(r,18),p=mp.nstr(a/r,18),q=mp.nstr(b/r,18),output_outside=bool(exited)))
                if exited:break
            rows.append(dict(p0=pv,q0=qv,precision_digits=500,history=history,exit_recorded=bool(exited),prefix_sum_b2=mp.nstr(total,18),coherence_product=mp.nstr(product,18),stopped_loss_bound=mp.nstr(mp.mpf(16)/35*u0,18),unconditional_future_bound='NOT CLAIMED'))
    assert any(x['exit_recorded'] for x in rows)
    return rows

def source():
    rng=np.random.default_rng(20261119); update=audit.load_update(); u=audit.complex_unitary(rng,4)
    cross=np.zeros((4,4),complex); x=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2)); cross[:2,2:]=x; cross[2:,:2]=x.conj().T; cross*=.1/np.linalg.norm(cross,2)
    f=u@(np.eye(4)+cross)@u.conj().T; w=np.eye(4)/4
    x=rng.normal(size=(4,4))+1j*rng.normal(size=(4,4)); kb=x@x.conj().T; kb/=np.trace(kb); k=u@kb@u.conj().T
    kr=0.; gr=0.; yr=0.; calls=0; rows=[]
    for r in (.1,.2):
        for p in (.1,.5):
            for q in (.1,.5):
                s=.001; a=r*p; b=r*q
                sn,rn,an,bn,h=map(float,step(mp.mpf(str(s)),mp.mpf(str(r)),mp.mpf(str(a)),mp.mpf(str(b))))
                load=(u*(s*np.array([1+r+a,1+r-a,1-r+b,1-r-b])))@u.conj().T
                out=pair_audit.source_aligned(update,k,f,w,load); calls+=1
                got=u.conj().T@out['k']@u; expected=kb[2:,2:].copy(); expected[0,1]*=h; expected[1,0]*=h
                kr=max(kr,float(np.linalg.norm(got[2:,2:]-expected)))
                ey=(u*np.array([1+rn+an,1+rn-an,1-rn+bn,1-rn-bn]))@u.conj().T
                yr=max(yr,float(np.linalg.norm(out['y']/(np.trace(out['y']).real/4)-ey)))
                assert bn/rn<=q*(1-r/2)
                if r==.1 and p==.1:
                    gauge=audit.complex_unitary(rng,4); conj=lambda z:gauge@z@gauge.conj().T
                    gout=pair_audit.source_aligned(update,conj(k),conj(f),conj(w),conj(load)); calls+=1; gr=max(gr,float(np.linalg.norm(gout['k']-conj(out['k']))))
                rows.append(dict(r=r,p=p,q=q,r_next=rn,p_next=an/rn,q_next=bn/rn))
    assert calls==10 and max(kr,gr)<1e-10 and yr<1e-8
    return dict(calls=calls,kernel_residual=kr,gauge_residual=gr,normalized_load_residual=yr,cases=rows)

if __name__=='__main__':
    result=dict(status='PASS',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261119,certificate=certificate(),symbolic=symbolic(),stopped_positive_load_prefixes=prefixes(),source=source(),scope='Finite upper splitting: stopped lower memory through first exit only. No invariant upper-width cone or unrestricted all-event memory theorem claimed.')
    Path(__file__).with_name('two_sided_pair_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
