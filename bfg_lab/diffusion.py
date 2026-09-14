"""Known flux-law transport and fixed diagnostic check; no BFG dynamics claim."""
import hashlib
import json
from pathlib import Path
import numpy as np
from .core import TOL, split, persistent_basis


def adjacency(family, n, weight):
    if isinstance(n,bool) or not isinstance(n,(int,np.integer)) or n < 3:
        raise ValueError('Graph size must be an integer >=3')
    if not np.isfinite(weight) or weight <= 0:
        raise ValueError('Weight must be finite and positive')
    if family == 'path':
        edges=[(i,i+1) for i in range(n-1)]
    elif family == 'cycle':
        edges=[(i,(i+1)%n) for i in range(n)]
    elif family == 'star':
        edges=[(1,i) for i in range(n) if i!=1]
    elif family == 'complete':
        edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    else:
        raise ValueError('Unknown graph family')
    a=np.zeros((n,n))
    for i,j in edges:
        a[i,j]=a[j,i]=weight
    return a


def heat_operator(a, dt):
    if np.iscomplexobj(a):
        raise ValueError('Real adjacency required')
    a=np.asarray(a,dtype=float)
    if (a.ndim!=2 or a.shape[0]!=a.shape[1] or len(a)<2 or
        not np.isfinite(a).all() or np.any(a<0) or
        not np.allclose(a,a.T,atol=TOL,rtol=0) or np.any(np.diag(a)!=0)):
        raise ValueError('Expected finite symmetric nonnegative adjacency without loops')
    if not np.isfinite(dt) or dt<=0:
        raise ValueError('Positive finite time interval required')
    lap=np.diag(a.sum(axis=1))-a
    values,vectors=np.linalg.eigh(lap)
    # A graph Laplacian is PSD; discard only floating-point negative eigenvalues.
    values=np.maximum(values,0)
    return (vectors*np.exp(-dt*values))@vectors.T, lap


def evaluate(a, x, dt=.2, horizon=20, alpha=.2):
    r,lap=heat_operator(a,dt)
    if isinstance(horizon,bool) or not isinstance(horizon,(int,np.integer)) or horizon<1:
        raise ValueError('Positive integer horizon required')
    if not np.isfinite(alpha) or alpha<=0:
        raise ValueError('Positive finite load offset required')
    if np.iscomplexobj(x):
        raise ValueError('Real initial state required')
    x=np.asarray(x,dtype=float)
    if x.shape!=(len(lap),) or not np.isfinite(x).all():
        raise ValueError('Invalid initial state')
    values,vectors=np.linalg.eigh(lap)
    if values[1]<=TOL:
        raise ValueError('This target requires a numerically connected graph')
    initial=x-x.mean()
    denom=np.linalg.norm(initial)
    if denom<=TOL:
        raise ValueError('Recovery ratio undefined for an initially constant state')
    current=x.copy()
    for _ in range(horizon):
        current=r@current
    observed=float(np.linalg.norm(current-x.mean())/denom)
    coefficients=vectors[:,1:].T@initial
    predicted=float(np.linalg.norm(np.exp(-horizon*dt*values[1:])*coefficients)/denom)
    bound=float(np.exp(-horizon*dt*values[1]))
    y=dt*lap+alpha*np.eye(len(lap))
    w=persistent_basis(r)
    if w.shape[1]!=1:
        raise ValueError('Sampling interval does not resolve the unique persistent mode at TOL')
    result=split(y,x,w)
    lk=len(x)*float(x.mean())**2/(1+alpha)
    expected=np.array([lk,alpha**2*lk])
    return dict(observed_ratio=observed,modal_prediction=predicted,gap_bound=bound,
                prediction_error=abs(observed-predicted),
                bound_violation=max(0.,observed-bound),
                mass_error=float(abs(current.sum()-x.sum())),
                load_error=float(np.max(np.abs(np.array(result['loads'])-expected))),
                loads=result['loads'],weights=result['weights'].tolist() if result['status']=='ok' else None,
                gain=result.get('gain'),split_status=result['status'],laplacian_gap=float(values[1]))


def run():
    rows=[]
    for family in ('path','cycle','star','complete'):
        for n in (4,6,8):
            for weight in (.5,1.,2.):
                a=adjacency(family,n,weight)
                for initial in ('impulse','two_impulses'):
                    x=np.zeros(n); x[0]=1
                    if initial=='two_impulses':
                        x*=.5; x[-1]=.5
                    rows.append(dict(family=family,n=n,weight=weight,initial=initial,
                                     **evaluate(a,x)))
    protocol=Path(__file__).resolve().parents[1]/'docs/DIFFUSION_PROTOCOL.md'
    summary=dict(protocol_sha256=hashlib.sha256(protocol.read_bytes()).hexdigest(),
                 numpy=np.__version__,cases=len(rows))
    for key in ('prediction_error','bound_violation','mass_error','load_error'):
        summary['max_'+key]=max(r[key] for r in rows)
    return dict(**summary,runs=rows)


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',default='results/diffusion.json')
    args=parser.parse_args()
    result=run()
    path=Path(args.output); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='runs'}))
