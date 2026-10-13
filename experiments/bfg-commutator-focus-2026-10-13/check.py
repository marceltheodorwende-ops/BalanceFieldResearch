"""P80 finite synthetic implementation controls; thresholds in PROTOCOL.md."""
import json
from pathlib import Path
import numpy as np
import mpmath as mp
import sympy as sp
from scipy.linalg import expm
mp.mp.dps=120
I=np.eye(2,dtype=complex)
A=np.array([[0,1],[1,0]],complex)
C=np.array([[0,-1j],[1j,0]],complex)
L=np.diag([1.,-1.]).astype(complex)
a=mp.mpf(16)/135; lam=mp.mpf(224)/675; d=mp.mpf(29)/90; ys=mp.mpf(8)/45

def step(s,u,v,t):
    z=mp.mpc(u,v)*(1-2j*t); r=abs(z); x=s+d
    xp,xm=x+r,x-r
    assert 0<xm<=xp<1
    alpha=(xp*xp/(1+xp)+xm*xm/(1+xm))/((1+xp*xp)/(1+xp)+(1+xm*xm)/(1+xm))
    def g(x): return (alpha+(1-alpha)*x*x)/(1+x)**2
    gp,gm=g(xp),g(xm)
    eta=(gp-gm)/(2*r) if r else 2*(x-alpha)/(1+x)**3
    zn=eta*z
    return (gp+gm)/2,zn.real,zn.imag

def limit(s,u,v,t,n):
    b=a*(1-2j*t)
    for _ in range(n): s,u,v=step(s,u,v,t)
    return mp.mpc(u,v)/b**n

tail=mp.mpf(0); closure=mp.mpf(0); cases=0
for tt in ['.9','1','1.1']:
    t=mp.mpf(tt); rho=a*mp.sqrt(1+4*t*t)
    assert lam<mp.mpf('.4') and mp.mpf('.16')<rho<lam
    for off in ['-.001','0','.001']:
        for uv in [('.0001','.0002'),('.001','-.002'),('-.003','.002')]:
            s=ys+mp.mpf(off);u,v=map(mp.mpf,uv)
            z60=limit(s,u,v,t,60);z80=limit(s,u,v,t,80)
            tail=max(tail,abs(z60-z80))
            sn,un,vn=step(s,u,v,t)
            closure=max(closure,abs(limit(sn,un,vn,t,80)-a*(1-2j*t)*z80));cases+=1
assert tail<mp.mpf('1e-20') and closure<mp.mpf('1e-20')

def ambient(Y,K,L,t,svd=False):
    X=Y+float(d)*I+1j*t*(L@Y-Y@L)
    c=np.linalg.inv(I+X);b=X@c
    alpha=(np.trace(X@X@c)/np.trace((I+X@X)@c)).real
    analysis=np.vstack([np.sqrt(alpha)*c,np.sqrt(1-alpha)*b])
    if svd:
        U,s,Vh=np.linalg.svd(analysis,full_matrices=False);V=Vh.conj().T
        kp=U.conj().T@np.block([[K,np.zeros_like(K)],[np.zeros_like(K),K]])@U
        return V@np.diag(s*s)@Vh,V@kp@Vh
    M=analysis.conj().T@analysis
    e,V=np.linalg.eigh(M);hi=(V/np.sqrt(e))@V.conj().T
    tc=np.sqrt(alpha)*c@hi;tb=np.sqrt(1-alpha)*b@hi
    return M,tc@K@tc+tb@K@tb

rng=np.random.default_rng(80);gauge=svderr=spectral=fd=0.;kchange=0.
for j in range(30):
    t=[.9,1.,1.1][j%3];s=float(ys)+rng.uniform(-.001,.001);u,v=rng.uniform(-.003,.003,2)
    Y=s*I+u*A+v*C;K=L+.3*A
    out=ambient(Y,K,L,t);sout=ambient(Y,K,L,t,True)
    svderr=max(svderr,*(np.max(abs(x-y)) for x,y in zip(out,sout)))
    sn,un,vn=step(mp.mpf(s),mp.mpf(u),mp.mpf(v),mp.mpf(t))
    spectral=max(spectral,np.max(abs(out[0]-(float(sn)*I+float(un)*A+float(vn)*C))))
    raw=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2));Q,_=np.linalg.qr(raw)
    gout=ambient(Q@Y@Q.conj().T,Q@K@Q.conj().T,Q@L@Q.conj().T,t,True)
    gauge=max(gauge,*(np.max(abs(gout[i]-Q@out[i]@Q.conj().T)) for i in range(2)))
    kchange=max(kchange,np.max(abs(out[1]-K)))
    for E,want in [(I,float(lam)*I),(A,float(a)*(A-2*t*C)),(C,float(a)*(2*t*A+C))]:
        h=1e-6;yp=ambient(float(ys)*I+h*E,K,L,t)[0];ym=ambient(float(ys)*I-h*E,K,L,t)[0]
        fd=max(fd,np.max(abs((yp-ym)/(2*h)-want)))
assert max(gauge,svderr,spectral)<1e-11 and fd<1e-7 and kchange>0
# Same native planar coordinates but differing scalar preparation do not close.
one=step(ys-mp.mpf('.001'),mp.mpf('.001'),0,mp.mpf(1))
two=step(ys+mp.mpf('.001'),mp.mpf('.001'),0,mp.mpf(1))
nonclosure=abs(mp.mpc(one[1]-two[1],one[2]-two[2]));assert nonclosure>mp.mpf('1e-8')
# A single real time unit below is synthetic, never calibrated seconds.
exp_error=0;branch=[]
for m in [0,1,-1]:
    rho=float(a)*np.sqrt(5);phi=-np.arctan(2.);ell=np.log(rho);omega=phi+2*np.pi*m
    J=np.array([[0.,-1.],[1.,0.]]);G=ell*np.eye(2)+omega*J
    B=float(a)*np.array([[1.,2.],[-2.,1.]])
    S=np.array([[1.,0.],[ell,-omega]])
    H=np.array([[0.,1.],[-(ell*ell+omega*omega),2*ell]])
    exp_error=max(exp_error,np.max(abs(expm(G)-B)),np.max(abs(S@G-H@S)),np.max(abs(expm(H)-S@B@np.linalg.inv(S))))
    branch.append(dict(m=m,kappa=ell*ell+omega*omega,gamma=-2*ell,rank=int(np.linalg.matrix_rank(S))))
assert exp_error<1e-10 and len({b['kappa'] for b in branch})==3
ell,omega,theta,vel,inertia=sp.symbols('ell omega theta vel inertia',real=True)
G=sp.Matrix([[ell,-omega],[omega,ell]]);S=sp.Matrix([[1,0],[ell,-omega]])
H=sp.Matrix([[0,1],[-(ell**2+omega**2),2*ell]])
assert sp.simplify(S*G-H*S)==sp.zeros(2)
Edot=sp.expand(inertia*((ell**2+omega**2)*theta*vel+vel*(2*ell*vel-(ell**2+omega**2)*theta)))
assert sp.simplify(Edot-2*inertia*ell*vel**2)==0
assert S.det()==-omega
# Zero coupling loses kinematic observability; large coupling violates local proof hypothesis.
assert float(a)*np.sqrt(1+4*10**2)>1
result=dict(kind='synthetic_mathematical_controls_only',precision_digits=120,nonlinear_cases=cases,
 max_factor_tail=str(tail),max_factor_closure=str(closure),matrix_gauge_cases=30,max_gauge_error=gauge,
 max_svd_error=svderr,max_spectral_error=spectral,max_finite_difference_error=fd,
 observed_nonneutral_K_change=kchange,native_coordinate_nonclosure=str(nonclosure),max_expm_error=exp_error,
 synthetic_clock_branches=branch,symbolic_force_energy_checks=True,physical_calibration=False,
 empirical_confirmation=False,holdout_accessed=False)
Path(__file__).with_name('controls.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
# Independent derivative of the nonlinear factor near zero, and exact lift-image check.
z_derivative_error=mp.mpf(0)
for tt in ['.9','1','1.1']:
    t=mp.mpf(tt);h=mp.mpf('1e-12')
    for uv,target in [( (h,0),mp.mpc(1,0)),((0,h),mp.mpc(0,1))]:
        zp=limit(ys,uv[0],uv[1],t,80);zm=limit(ys,-uv[0],-uv[1],t,80)
        z_derivative_error=max(z_derivative_error,abs((zp-zm)/(2*h)-target))
assert z_derivative_error<mp.mpf('1e-18')
def generic(Y,K,R,L,t):
    n=len(Y);eye=np.eye(n);X=Y+float(d)*eye+1j*t*(L@Y-Y@L)
    cc=np.linalg.inv(eye+X);bb=X@cc
    alpha=(np.trace(R@X@X@cc)/np.trace(R@(eye+X@X)@cc)).real
    analysis=np.vstack([np.sqrt(alpha)*cc,np.sqrt(1-alpha)*bb])
    U,s,Vh=np.linalg.svd(analysis,full_matrices=False);V=Vh.conj().T
    kp=V@(U.conj().T@np.block([[K,np.zeros_like(K)],[np.zeros_like(K),K]])@U)@Vh
    return V@np.diag(s*s)@Vh,kp,alpha
lift_error=0.;balance_error=0.
for t in [.9,1.,1.1]:
    Y=float(ys)*I+.001*A-.002*C;K=L+.3*A;R=I;W=(I+A/2)/2
    base=generic(Y,K,R,L,t)
    for h in [2,3]:
        aux=np.eye(h);lift=generic(np.kron(Y,aux),np.kron(K,aux),np.kron(R,aux/h),np.kron(L,aux),t)
        lift_error=max(lift_error,np.max(abs(lift[0]-np.kron(base[0],aux))),np.max(abs(lift[1]-np.kron(base[1],aux))),abs(lift[2]-base[2]))
        wh=np.kron(W,aux/h);ah=4*h*(wh-np.eye(2*h)/(2*h))
        lift_error=max(lift_error,np.max(abs(ah-np.kron(A,aux))),abs(np.trace(ah@np.kron(Y,aux))/(2*h)-np.trace(A@Y)/2))
        balance_error=max(balance_error,abs(np.trace(np.kron(R,aux/h))-np.trace(R)),abs(np.trace(wh)-1))
assert lift_error<1e-11 and balance_error<1e-11
result.update(max_factor_derivative_error=str(z_derivative_error),tensor_image_cases=6,max_tensor_svd_error=lift_error,max_lift_stock_trace_error=balance_error)
Path(__file__).with_name('controls.json').write_text(json.dumps(result,indent=2)+'\n')
print('Additional derivative/tensor controls:',json.dumps({k:result[k] for k in ['max_factor_derivative_error','tensor_image_cases','max_tensor_svd_error','max_lift_stock_trace_error']}))
