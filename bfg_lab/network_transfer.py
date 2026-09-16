"""New small-network cases using independent closed-form trajectories."""
import hashlib,json
from collections import Counter
from decimal import Decimal,localcontext
from pathlib import Path
from .certified import assess_family
from .certified_exact import assess_exact_pair

STAGE=Path(__file__).resolve().parents[1]/'research/network-transfer-2026-09-16'


def catalogue():
    cases=[]
    with localcontext() as ctx:
        ctx.prec=80
        for graph,n in [('path3',3),('complete4',4)]:
            lo=[[0 for _ in range(n)] for _ in range(n)]
            hi=[[0 for _ in range(n)] for _ in range(n)]
            for i in range(n):
                for j in range(i+1,n):
                    if graph=='complete4' or j==i+1:
                        lo[i][j]=lo[j][i]='.7'; hi[i][j]=hi[j][i]='1.3'
            for sensors in (list(range(n)),[0]):
                for weight,kind in [(w,k) for w in ('.8','1.2') for k in ('intact','isolated')]+[('1','constant_cut')]:
                    initial=['.25']*n if kind=='constant_cut' else [1]+[0]*(n-1)
                    data=[]
                    for k,t in enumerate(('0','.25','1')):
                        u=Decimal(weight)*Decimal(t); one=Decimal(1)
                        if kind=='constant_cut':
                            values=[Decimal('.25')]*n
                        elif kind=='isolated':
                            values=[one]+[Decimal(0)]*(n-1)
                        elif graph=='complete4':
                            e=(-4*u).exp(); values=[one/4+3*e/4]+[one/4-e/4]*3
                        else:
                            e=(-u).exp(); e3=(-3*u).exp()
                            values=[one/3+e/2+e3/6,one/3-e3/3,one/3-e/2+e3/6]
                        data.append([str(values[i]+Decimal('1e-7')*(1 if (k+i)%2 else -1)) for i in sensors])
                    cases.append(dict(id=f'{graph}_{len(sensors)}s_{weight}_{kind}',graph=graph,
                        condition=kind,weight=weight,input=dict(weight_lower=lo,weight_upper=hi,
                        initial=initial,samples=data,times=[0,'.25',1],sensors=sensors,sensor_error='1e-6')))
    return cases


def run():
    cases=catalogue(); rows=[]
    for c in cases:
        baseline=assess_family(**c['input'])
        result=assess_exact_pair(**c['input'],max_boxes=31,max_depth=12,max_candidates=27)
        rows.append(dict(id=c['id'],graph=c['graph'],condition=c['condition'],
            sensor_count=len(c['input']['sensors']),baseline=baseline['status'],
            status=result['status'],visited_boxes=result.get('visited_boxes'),
            candidate_checks=result.get('candidate_checks'),witness=result.get('witness'),
            certificate=result.get('certificate'),reason=result.get('reason')))
    return dict(cases=cases,rows=rows,
        case_sha256=hashlib.sha256(json.dumps(cases,sort_keys=True).encode()).hexdigest(),
        protocol_sha256=hashlib.sha256((STAGE/'protocol.md').read_bytes()).hexdigest(),
        counts={key:dict(Counter(r[key] for r in rows)) for key in ('baseline','status')},
        false_exclusions=[r['id'] for r in rows if r['condition']!='isolated' and r['status']=='healthy_family_excluded'])


if __name__=='__main__':
    r=run(); (STAGE/'results.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(counts=r['counts'],false_exclusions=r['false_exclusions'])))
