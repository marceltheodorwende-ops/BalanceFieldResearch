"""Replay the frozen 39 cases through the exact-pair fallback."""
import hashlib,json
from collections import Counter
from pathlib import Path
from .certified_comparison import catalogue
from .certified_exact import assess_exact_pair


def run():
    cases=catalogue(); rows=[]
    for c in cases:
        r=assess_exact_pair(**c['input'])
        if c['id'].startswith(('corner_','grid_')):
            assert r['status']!='healthy_family_excluded'
        rows.append(dict(id=c['id'],result=r))
    encoded=json.dumps(cases,sort_keys=True,separators=(',',':')).encode()
    return dict(case_sha256=hashlib.sha256(encoded).hexdigest(),
                protocol_sha256=hashlib.sha256((Path(__file__).resolve().parents[1]/
                    'research/exact-pair-2026-09-16/protocol.md').read_bytes()).hexdigest(),
                counts=dict(Counter(r['result']['status'] for r in rows)),rows=rows)


if __name__=='__main__':
    r=run(); path=Path('research/exact-pair-2026-09-16/results.json'); path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(r['counts']))
