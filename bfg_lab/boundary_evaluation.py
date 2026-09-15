"""Fixed ablations for the boundary protocol; no synthetic oracle input."""
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path
from .certified_comparison import catalogue, compact
from .certified_search import refine_family
from .certified_boundary import assess_boundary


def run(mode):
    if mode not in ('old24','old64','boundary24','boundary64'):
        raise ValueError('Unknown ablation')
    cases=catalogue(); rows=[]
    for case in cases:
        p=dict(case['input'])
        if mode=='old64':
            p['terms']=64
        if mode.startswith('old'):
            r=refine_family(**p,max_boxes=255,max_depth=20)
        else:
            r=assess_boundary(**p,max_boxes=255,max_depth=20,max_candidates=81,
                              candidate_terms=64 if mode=='boundary64' else p.get('terms',24))
        witness=r.get('witness')
        if witness:
            # Check against the ORIGINAL input, independent of search bookkeeping.
            original=case['input']; ex=F(original.get('initial_error',0))
            for i,v in enumerate(witness['initial']):
                assert abs(F(v)-F(original['initial'][i]))<=ex
                for j,w in enumerate(witness['weights'][i]):
                    assert F(original['weight_lower'][i][j])<=F(w)<=F(original['weight_upper'][i][j])
        if case['id'].startswith(('corner_','grid_')):
            assert r['status']!='healthy_family_excluded'
        rows.append(dict(id=case['id'],result=compact(r),witness=witness,
                         candidate_checks=r.get('candidate_checks',0)))
    encoded=json.dumps(cases,sort_keys=True,separators=(',',':')).encode()
    return dict(mode=mode,case_sha256=hashlib.sha256(encoded).hexdigest(),
                protocol_sha256=hashlib.sha256((Path(__file__).resolve().parents[1]/
                    'docs/BOUNDARY_PROTOCOL.md').read_bytes()).hexdigest(),
                counts=dict(Counter(r['result']['status'] for r in rows)),rows=rows)


if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('mode',choices=['old24','old64','boundary24','boundary64'])
    args=p.parse_args(); r=run(args.mode)
    path=Path('results')/('boundary_'+args.mode+'.json')
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r['counts']))
