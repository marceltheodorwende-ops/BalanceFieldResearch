"""Sparse global outer/inner systems; exact rational certificate arithmetic."""
from fractions import Fraction as F
from math import isqrt
import numpy as np
from scipy.sparse import coo_matrix,hstack
from scipy.optimize import linprog

def atan_bounds(z,n=32):
    v=sum(((-1)**j*z**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    nxt=z**(2*n+1)/F(2*n+1)
    return (v,v+nxt) if n%2==0 else (v-nxt,v)
a,b=atan_bounds(F(1,5));c,d=atan_bounds(F(1,239));PI=(16*a-4*d,16*b-4*c)
def sqrt_bounds(x,p=30):
    assert x>=0
    scale=10**p;n=isqrt(x.numerator*scale*scale//x.denominator)
    return F(n,scale),F(n+1,scale)
def cos_bounds(x):
    assert 0<=x<=1
    lo=sum(((-1)**j*x**(2*j)/F(__import__('math').factorial(2*j)) for j in range(32)),F(0))
    return lo,lo+x**64/F(__import__('math').factorial(64))
def parameters(q0,w0,L,N,ew,B):
    e=(PI[0]/N+F(1,2000),PI[1]/N+F(1,2000));k=F('9.799')/L;km=F('9.799')*L/(L*L+F('.02'))
    qlo=abs(q0)+e[0];qhi=abs(q0)+e[1]
    plo=1-cos_bounds(qlo)[1];phi=1-cos_bounds(qhi)[0]
    ulo=abs(w0)+ew
    vlo=sqrt_bounds(ulo*ulo+2*k*plo)[0];vhi=sqrt_bounds(ulo*ulo+2*k*phi)[1]
    klo,khi=sqrt_bounds(k)
    alo=k+2*klo*vlo+B*vlo*vlo;ahi=k+2*khi*vhi+B*vhi*vhi
    corridor=qhi<PI[0] and phi+ulo*ulo/(2*km)<2
    return e,(alo,ahi),bool(corridor)

class System:
 def __init__(self,t,knots,kind):
    self.t=[F(str(x)) for x in t];self.knots=np.asarray(knots);self.kind=kind;self.K=len(knots)
    self.rows=[];self.info=[]
    def add(co,kind,idx,sign,extra=F(0)):
        self.rows.append([(j,c*sign) for j,c in co.items() if c]);self.info.append((kind,idx,sign,extra))
    for i,ti in enumerate(self.t):
        j=int(np.searchsorted(knots,i,side='right')-1);j=min(j,self.K-2)
        h=self.t[knots[j+1]]-self.t[knots[j]];s=ti-self.t[knots[j]];u=s/h
        if kind=='outer':
            cq={j:1-u,j+1:u};cw={self.K+j:1-u,self.K+j+1:u}
            eq=s*(h-s)/2;ev=2*s*(h-s)/h
        else:
            cq={j:2*u**3-3*u*u+1,j+1:-2*u**3+3*u*u,self.K+j:h*(u**3-2*u*u+u),self.K+j+1:h*(u**3-u*u)}
            cw={j:(6*u*u-6*u)/h,j+1:(-6*u*u+6*u)/h,self.K+j:3*u*u-4*u+1,self.K+j+1:3*u*u-2*u}
            eq=ev=F(0)
        for sign in [1,-1]:add(cq,'q',i,sign,eq);add(cw,'w',i,sign,ev)
    for j in range(self.K-1):
        h=self.t[knots[j+1]]-self.t[knots[j]]
        if kind=='outer':
            cs=[({self.K+j+1:F(1),self.K+j:F(-1)},h),({j+1:F(1),j:F(-1),self.K+j:-h/2,self.K+j+1:-h/2},h*h/4)]
        else:
            cs=[({j:-6/h**2,j+1:6/h**2,self.K+j:-4/h,self.K+j+1:-2/h},F(1)),
                ({j:6/h**2,j+1:-6/h**2,self.K+j:2/h,self.K+j+1:4/h},F(1))]
        for co,fac in cs:
            for sign in [1,-1]:add(co,'a',j,sign,fac)
    ii=[];jj=[];vv=[]
    for i,row in enumerate(self.rows):
        for j,v in row:ii.append(i);jj.append(j);vv.append(float(v))
    self.G=coo_matrix((vv,(ii,jj)),shape=(len(self.rows),2*self.K)).tocsr()
 def rhs(self,q,w,e,ew,A):
    b=[];sc=[]
    for typ,i,sign,extra in self.info:
        if typ=='q':width=e+A*extra;center=sign*q[i]
        elif typ=='w':width=ew+A*extra;center=sign*w[i]
        else:width=A*extra;center=F(0)
        b.append(center+width);sc.append(width)
    return b,sc
 def solve(self,q,w,e,ew,A):
    b,sc=self.rhs(q,w,e,ew,A);bfloat=np.array([float(z) for z in b]);scale=np.array([float(z) for z in sc])
    if self.kind=='outer':
        bounds=[(float(q[i]-e),float(q[i]+e)) for i in self.knots]+[(float(w[i]-ew),float(w[i]+ew)) for i in self.knots]+[(0,None)]
        c=np.r_[np.zeros(2*self.K),1.];M=hstack([self.G,-scale[:,None]],format='csr')
    else:
        bounds=[(None,None)]*(2*self.K)+[(0,1)]
        c=np.r_[np.zeros(2*self.K),-1.];M=hstack([self.G,scale[:,None]],format='csr')
    result=linprog(c,A_ub=M,b_ub=bfloat,bounds=bounds,method='highs',options={'time_limit':5.,'threads':1,'dual_feasibility_tolerance':1e-9,'primal_feasibility_tolerance':1e-9})
    return result
 def outer_certificate(self,result,q,w,e,ew,A):
    if not result.success:return None
    weights=np.maximum(0,-result.ineqlin.marginals);active=np.flatnonzero(weights>1e-12)
    if len(active)==0:return None
    b,_=self.rhs(q,w,e,ew,A);c=[F(0)]*(2*self.K);rhs=F(0);terms=[]
    for i in active:
        lam=F(str(float(weights[i])));rhs+=lam*b[i]
        for j,g in self.rows[i]:c[j]+=lam*g
        terms.append([int(i),str(lam)])
    lo=[q[i]-e for i in self.knots]+[w[i]-ew for i in self.knots]
    hi=[q[i]+e for i in self.knots]+[w[i]+ew for i in self.knots]
    m=sum((cc*(l if cc>=0 else u) for cc,l,u in zip(c,lo,hi)),F(0))-rhs
    return {'margin':float(m),'positive':m>0,'active_rows':len(active),'weights':terms,'exact_margin':str(m)}
 def inner_certificate(self,result,q,w,e,ew,A):
    if not result.success or result.x[-1]<=1e-6:return None
    xx=[F(str(float(v))) for v in result.x[:-1]];b,sc=self.rhs(q,w,e,ew,A);minimum=None
    for row,bval,scale in zip(self.rows,b,sc):
        margin=(bval-sum((v*xx[j] for j,v in row),F(0)))/scale
        minimum=margin if minimum is None else min(minimum,margin)
    if minimum<=F(1,10**8):return None
    return {'minimum_normalized_margin':float(minimum),'positive':True,'states':[str(v) for v in xx],
            'exact_normalized_margin':str(minimum),'solver_sigma':float(result.x[-1])}
