"""Numerical witness proposals accepted only by the exact rational certifier."""
import numpy as np
from .certified import assess_family, _number
from .certified_exact import assess_exact_pair


class _BudgetExhausted(Exception):
    pass


def assess_interior(weight_lower,weight_upper,initial,samples,times,sensors,
                    initial_error=0,sensor_error=0,fit_evaluations=256,
                    fit_terms=64,**options):
    if type(fit_evaluations)!=int or fit_evaluations<0:
        raise ValueError('Nonnegative integer fit budget required')
    if type(fit_terms)!=int or not 0<=fit_terms<=128:
        raise ValueError('Integer fit certificate budget 0..128 required')
    previous=assess_exact_pair(weight_lower,weight_upper,initial,samples,times,sensors,
                              initial_error,sensor_error,**options)
    if previous['status']!='unresolved' or fit_evaluations==0:
        return previous
    n=len(initial); edges=[(i,j) for i in range(n) for j in range(i+1,n)]
    ex=_number(initial_error); x=list(map(_number,initial))
    intervals=[(_number(weight_lower[i][j]),_number(weight_upper[i][j])) for i,j in edges]
    intervals += [(v-ex,v+ex) for v in x]
    variable=[i for i,(l,u) in enumerate(intervals) if l<u]
    if not variable:
        return previous
    count=0; candidate=None; stop='stalled'
    try:
        lower=np.array([float(l) for l,u in intervals]); width=np.array([float(u-l) for l,u in intervals])
        ts=np.array([float(_number(t)) for t in times])
        target=np.array([[float(_number(v)) for v in row] for row in samples])
        if not all(np.isfinite(a).all() for a in (lower,width,ts,target)):
            raise ValueError('Nonfinite numerical proposal input')
        def residual(z):
            nonlocal count
            if count>=fit_evaluations: raise _BudgetExhausted()
            count+=1
            values=lower.copy(); values[variable]+=width[variable]*z
            a=np.zeros((n,n))
            for (i,j),w in zip(edges,values): a[i,j]=a[j,i]=w
            lap=np.diag(a.sum(axis=1))-a
            lam,v=np.linalg.eigh(lap); lam=np.maximum(lam,0)
            coeff=v.T@values[len(edges):]
            predictions=np.array([v@(np.exp(-t*lam)*coeff) for t in ts])[:,sensors]
            r=(predictions-target).ravel()
            if not np.isfinite(r).all(): raise ValueError('Nonfinite residual')
            return r
        z=np.full(len(variable),.5); r=residual(z); candidate=z.copy()
        tolerance=float(_number(sensor_error))/2
        while True:
            if np.max(np.abs(r))<=tolerance:
                stop='small_numerical_residual'; break
            columns=[]
            for j in range(len(z)):
                zp=z.copy(); zm=z.copy(); zp[j]=min(1,z[j]+1e-5); zm[j]=max(0,z[j]-1e-5)
                columns.append((residual(zp)-residual(zm))/(zp[j]-zm[j]))
            step=np.linalg.lstsq(np.array(columns).T,-r,rcond=None)[0]
            if not np.isfinite(step).all(): raise ValueError('Nonfinite proposal step')
            accepted=False
            for k in range(12):
                trial=np.clip(z+step*(.5**k),0,1)
                if np.max(np.abs(trial-z))<1e-12: continue
                rr=residual(trial)
                if rr@rr < r@r:
                    z,r=trial,rr; candidate=z.copy(); accepted=True; break
            if not accepted: break
    except _BudgetExhausted:
        stop='numerical_budget_exhausted'
    except (ValueError,OverflowError,FloatingPointError,np.linalg.LinAlgError):
        stop='numerical_failure'
    previous['fit_evaluations']=count; previous['fit_stop']=stop
    if candidate is None: return previous
    # Convert bounded normalized coordinates to rationals, then apply ORIGINAL
    # rational bounds. Floating-point optimization cannot expand the family.
    values=[l for l,u in intervals]
    for j,index in enumerate(variable):
        l,u=intervals[index]; q=_number(format(float(candidate[j]),'.12f'))
        q=max(_number(0),min(_number(1),q)); values[index]=l+(u-l)*q
    a=[[_number(0) for _ in x] for _ in x]
    for (i,j),w in zip(edges,values): a[i][j]=a[j][i]=w
    certified=assess_family(a,a,values[len(edges):],samples,times,sensors,
                            0,sensor_error,fit_terms)
    if certified['status']=='compatible_witness':
        certified.update(witness_source='numerical_proposal_exact_certificate',
                         fit_evaluations=count,fit_stop=stop,fit_terms=fit_terms)
        return certified
    previous['fit_certificate_status']=certified['status']
    return previous


if __name__=='__main__':
    import argparse,json
    from pathlib import Path
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--input',type=Path,required=True)
    p.add_argument('--output',type=Path,default=Path('results/certified_interior.json'))
    args=p.parse_args(); r=assess_interior(**json.loads(args.input.read_text(encoding='utf-8'),parse_float=str))
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8'); print(r['status'])
