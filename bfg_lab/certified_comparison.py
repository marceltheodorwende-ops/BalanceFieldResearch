"""Replay the existing certified regression cases under fixed search budgets."""
import hashlib
import json
from collections import Counter
from decimal import Decimal, localcontext
from pathlib import Path
from .certified import assess_family
from .certified_search import refine_family


def catalogue():
    cases = []
    def add(name, p, source):
        cases.append(dict(id=name, source=source, input=p))
    def pair(lo=0, hi=2, samples=None, times=None, **kwargs):
        return dict(weight_lower=[[0,lo],[lo,0]], weight_upper=[[0,hi],[hi,0]],
                    initial=[1,0], samples=samples, times=times, sensors=[0,1], **kwargs)
    source = 'tests/test_certified.py'
    add('exact_overlap', pair(samples=[[1,0],['.7','.3']], times=[0,1]), source)
    add('series_limit', pair(1,1,[[1,0],['.5','.5']],[0,100],terms=2), source)
    add('inconsistent_narrow', pair('.9','1.1',
        [[1,0],['.582649444','.417350556'],['.506138670','.493861330']],
        [0,1,2],sensor_error='.000000001'), source)
    add('midpoint_control', pair('.9','1.1',[[1,0],['.56766764','.43233236']],
        [0,1],sensor_error='.000001'), source)
    add('exclusion_control', pair('.9','1.1',[[1,0],[3,0]],[0,1],sensor_error='.001'), source)
    p = pair('.9','1.1',[['.5','.5'],['.5','.5']],[0,1]); p['initial']=['.5','.5']
    add('constant_control', p, source)
    with localcontext() as ctx:
        ctx.prec = 90
        for w in (Decimal('.9'), Decimal('1'), Decimal('1.1')):
            for e0 in (Decimal('-.001'),Decimal('.001')):
                for e1 in (Decimal('-.001'),Decimal('.001')):
                    for noise in (Decimal('-.0001'),Decimal('.0001')):
                        x0=Decimal(1)+e0; x1=e1; samples=[]
                        for t in (Decimal(0),Decimal('.1'),Decimal(1),Decimal(3)):
                            diff=(x0-x1)*(-2*w*t).exp()/2; mean=(x0+x1)/2
                            samples.append([str(mean+diff+noise),str(mean-diff-noise)])
                        add(f'corner_{w}_{e0}_{e1}_{noise}', pair('.9','1.1',samples,[0,'.1',1,3],
                            initial_error='.001',sensor_error='.000100000000000000000000000001'), source)
    source = 'tests/test_certified_search.py'
    with localcontext() as ctx:
        ctx.prec = 60
        for name, weights in [(f'grid_{w}',[w]) for w in ('0','0.125','0.5','0.9','1','1.75','2')] + [
                ('inconsistent_wide',['0.9','1.1'])]:
            samples=[['1','0']]
            for t,w in enumerate(weights,1):
                y=(1+(-2*Decimal(w)*t).exp())/2
                samples.append([str(y),str(1-y)])
            add(name, pair(samples=samples,times=list(range(len(samples))),sensor_error='.000001'), source)
    add('initial_witness',dict(weight_lower=[[0]],weight_upper=[[0]],initial=['0.5'],
        samples=[['0.25']],times=[0],sensors=[0],initial_error='0.5'),source)
    return cases


def compact(result):
    return dict(status=result['status'], reason=result.get('reason'),
                visited_boxes=result.get('visited_boxes',1),
                excluded_leaves=len(result.get('excluded_leaves',[])),
                pending_leaves=len(result.get('pending_paths',[])),
                unresolved_leaf_reasons=dict(Counter(r['reason'] for r in result.get('unresolved_leaves',[]))))


def run():
    cases=catalogue(); rows=[]
    for case in cases:
        p=case['input']
        baseline=compact(assess_family(**p))
        small=compact(refine_family(**p,max_boxes=31,max_depth=20))
        large=compact(refine_family(**p,max_boxes=255,max_depth=20))
        rows.append(dict(id=case['id'],baseline=baseline,search_31=small,search_255=large))
    # Diagnostic witnesses use known synthetic generating parameters. They are
    # not available to a blind detector and are not counted as search successes.
    diagnostics=[]
    for case,row in zip(cases,rows):
        if row['search_255']['status'] != 'unresolved':
            continue
        name=case['id']; p=case['input']
        if name.startswith('corner_'):
            _,w,e0,e1,_=name.split('_')
            initial=[str(Decimal(1)+Decimal(e0)),e1]
            a=[[0,w],[w,0]]
            witness=assess_family(a,a,initial,p['samples'],p['times'],p['sensors'],
                                  sensor_error=p['sensor_error'],terms=64)
            diagnostics.append(dict(id=name,kind='synthetic_generating_witness',
                result=compact(witness),weights=a,initial=initial,terms=64))
        elif name=='grid_2':
            diagnostics.append(dict(id=name,kind='box_budget_only_increase',
                max_boxes=1023,max_depth=20,result=compact(refine_family(**p,max_boxes=1023,max_depth=20))))
        elif name=='series_limit':
            q=dict(p,terms=128)
            diagnostics.append(dict(id=name,kind='series_budget_only_increase',
                terms=128,result=compact(refine_family(**q,max_boxes=255,max_depth=20))))
    encoded=json.dumps(cases,sort_keys=True,separators=(',',':')).encode()
    return dict(case_sha256=hashlib.sha256(encoded).hexdigest(),cases=cases,
                settings=dict(box_budgets=[31,255],max_depth=20,terms='unchanged per input; default 24'),
                counts={method:dict(Counter(row[method]['status'] for row in rows))
                        for method in ('baseline','search_31','search_255')},rows=rows,diagnostics=diagnostics)


if __name__=='__main__':
    result=run(); path=Path('results/certified_comparison.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result['counts'],indent=2))
