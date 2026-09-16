"""Fixed interior-search evaluation with historical input hashes."""
import hashlib,json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from .network_transfer import catalogue
from .certified_comparison import catalogue as old_catalogue
from .certified_exact import assess_exact_pair
from .certified_interior import assess_interior

ROOT=Path(__file__).resolve().parents[1]
STAGE=ROOT/'research/interior-search-2026-09-16'


def summarize(r):
    return {k:r[k] for k in ('status','witness','symbolic_witness','fit_evaluations',
        'fit_stop','fit_certificate_status','visited_boxes','candidate_checks') if k in r}


def run():
    cases=catalogue(); rows=[]
    for c in cases:
        p=c['input']; a=assess_exact_pair(**p,max_boxes=31,max_depth=12,max_candidates=27)
        b=assess_exact_pair(**p,max_boxes=256,max_depth=12,max_candidates=27)
        r=assess_interior(**p,max_boxes=31,max_depth=12,max_candidates=27)
        assert a['status']=='unresolved' or a['status']==r['status']
        if c['condition']!='isolated': assert r['status']!='healthy_family_excluded'
        if 'witness' in r:
            w=r['witness']; ex=F(p.get('initial_error',0))
            for i,x in enumerate(w['initial']):
                assert abs(F(x)-F(p['initial'][i]))<=ex
                for j,value in enumerate(w['weights'][i]):
                    assert F(p['weight_lower'][i][j])<=F(value)<=F(p['weight_upper'][i][j])
        rows.append(dict(id=c['id'],baseline=summarize(a),more_boxes=summarize(b),interior=summarize(r)))
    historic=json.loads((ROOT/'research/exact-pair-2026-09-16/results.json').read_text())
    oldcases=old_catalogue(); regression=[]
    for c,old in zip(oldcases,historic['rows']):
        r=assess_interior(**c['input']); assert c['id']==old['id']
        assert r['status']==old['result']['status']
        regression.append(dict(id=c['id'],status=r['status']))
    return dict(case_sha256=hashlib.sha256(json.dumps(cases,sort_keys=True).encode()).hexdigest(),
        old_case_sha256=hashlib.sha256(json.dumps(oldcases,sort_keys=True,separators=(',',':')).encode()).hexdigest(),
        protocol_sha256=hashlib.sha256((STAGE/'protocol.md').read_bytes()).hexdigest(),
        counts={k:dict(Counter(row[k]['status'] for row in rows)) for k in ('baseline','more_boxes','interior')},
        rows=rows,historical_regression=regression)


if __name__=='__main__':
    r=run(); (STAGE/'results.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r['counts']))
