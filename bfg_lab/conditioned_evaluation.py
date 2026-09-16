"""Ablation of numerical rank cutoff with unchanged exact acceptance."""
import hashlib,json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from .network_transfer import catalogue
from .certified_comparison import catalogue as old_catalogue
from .certified_interior import assess_interior

ROOT=Path(__file__).resolve().parents[1]
STAGE=ROOT/'research/conditioned-search-2026-09-16'


def summary(r):
    return {k:r[k] for k in ('status','witness','symbolic_witness','fit_evaluations',
                            'fit_stop','fit_rcond','fit_certificate_status') if k in r}


def run():
    cases=catalogue(); rows=[]
    for c in cases:
        p=c['input']; options=dict(max_boxes=31,max_depth=12,max_candidates=27)
        old=assess_interior(**p,**options)
        new=assess_interior(**p,**options,fit_rcond=1e-8)
        assert old['status']=='unresolved' or old['status']==new['status']
        if c['condition']!='isolated': assert new['status']!='healthy_family_excluded'
        if 'witness' in new:
            w=new['witness']
            for i,v in enumerate(w['initial']):
                assert abs(F(v)-F(p['initial'][i]))<=F(p.get('initial_error',0))
                for j,value in enumerate(w['weights'][i]):
                    assert F(p['weight_lower'][i][j])<=F(value)<=F(p['weight_upper'][i][j])
        rows.append(dict(id=c['id'],old=summary(old),conditioned=summary(new)))
    historical=json.loads((ROOT/'research/exact-pair-2026-09-16/results.json').read_text())
    oldcases=old_catalogue(); regression=[]
    for c,expected in zip(oldcases,historical['rows']):
        r=assess_interior(**c['input'],fit_rcond=1e-8)
        assert c['id']==expected['id'] and r['status']==expected['result']['status']
        regression.append(dict(id=c['id'],status=r['status']))
    return dict(case_sha256=hashlib.sha256(json.dumps(cases,sort_keys=True).encode()).hexdigest(),
        historical_case_sha256=hashlib.sha256(json.dumps(oldcases,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        protocol_sha256=hashlib.sha256((STAGE/'protocol.md').read_bytes()).hexdigest(),
        counts={k:dict(Counter(r[k]['status'] for r in rows)) for k in ('old','conditioned')},
        rows=rows,historical_regression=regression)


if __name__=='__main__':
    r=run(); (STAGE/'results.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r['counts']))
