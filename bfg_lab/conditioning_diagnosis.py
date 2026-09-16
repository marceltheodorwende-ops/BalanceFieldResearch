"""Inspect midpoint Jacobians without changing the candidate search."""
import json
from pathlib import Path
import numpy as np
from .network_transfer import catalogue

STAGE=Path(__file__).resolve().parents[1]/'research/conditioned-search-2026-09-16'


def run():
    rows=[]
    for c in catalogue():
        if c['condition']!='intact': continue
        p=c['input']; n=len(p['initial'])
        edges=[(i,j) for i in range(n) for j in range(i+1,n) if p['weight_upper'][i][j]]
        def residual(z):
            a=np.zeros((n,n))
            for (i,j),v in zip(edges,z): a[i,j]=a[j][i]=.7+.6*v
            lam,v=np.linalg.eigh(np.diag(a.sum(axis=1))-a)
            coeff=v.T@np.array(p['initial'],dtype=float)
            pred=np.array([v@(np.exp(-float(t)*np.maximum(lam,0))*coeff) for t in p['times']])[:,p['sensors']]
            return (pred-np.array(p['samples'],dtype=float)).ravel()
        z=np.full(len(edges),.5); cols=[]
        for j in range(len(z)):
            delta=np.zeros(len(z)); delta[j]=1e-5
            cols.append((residual(z+delta)-residual(z-delta))/(2e-5))
        jac=np.array(cols).T; s=np.linalg.svd(jac,compute_uv=False)
        step=np.linalg.lstsq(jac,-residual(z),rcond=None)[0]
        rows.append(dict(id=c['id'],singular_values=s.tolist(),relative_singular_values=(s/s[0]).tolist(),
                         max_abs_default_step=float(np.max(np.abs(step)))))
    return dict(numpy=np.__version__,rows=rows)


if __name__=='__main__':
    r=run(); STAGE.mkdir(parents=True,exist_ok=True)
    (STAGE/'diagnosis.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r))
