"""Guarded implication bookkeeping; not a theorem prover or new model law."""
from pathlib import Path
import json,hashlib

OUT=Path(__file__).resolve().parent
g=json.loads((OUT/'dependency_graph.json').read_text(encoding='utf-8'))
ids={x['id'] for x in g['nodes']};sources={x['id'] for x in g['sources']}
assert len(ids)==len(g['nodes'])==38
assert len({r['id'] for r in g['rules']})==16
for source in g['sources']:
    assert (OUT/source['record']).is_file(),source
for r in g['rules']:
    assert r['source'] in sources and r['requires'] and r['produces']
    assert set(r['requires']+r['produces'])<=ids

def closure(given):
    known=set(given);trace=[]
    assert known<=ids
    while True:
        changed=False
        for r in g['rules']:
            new=set(r['produces'])-known
            if new and set(r['requires'])<=known:
                known.update(new);trace.append({'rule':r['id'],'added':sorted(new)})
                changed=True
        if not changed:return known,trace

scenario_results=[]
for case in g['scenarios']:
    known,trace=closure(case['given'])
    assert set(case['expect_present'])<=known,case['id']
    assert not set(case['expect_absent'])&known,case['id']
    scenario_results.append({'id':case['id'],'hypothetical_only':case.get('hypothetical_only',False),'given':case['given'],'closure':sorted(known),'trace':trace})
# Find strongly connected components of the underlying guarded-rule dependency graph.
# Edges alone do not discharge guards; forward closure above requires every guard.
adj={x:set() for x in ids}
for r in g['rules']:
    for a in r['requires']:adj[a].update(r['produces'])
def reachable(start):
    seen=set();pending=[start]
    while pending:
        x=pending.pop()
        if x not in seen:seen.add(x);pending.extend(adj[x]-seen)
    return seen
reach={x:reachable(x) for x in ids};pending=set(ids);components=[]
while pending:
    x=min(pending);comp={y for y in pending if y in reach[x] and x in reach[y]}
    pending-=comp
    if len(comp)>1:components.append(sorted(comp))
assert sorted(components)==sorted([sorted(x) for x in g['expected_cyclic_components']])
for item in g['prohibited_shortcuts']:
    assert item['from'] in ids and item['to'] in ids
    # The isolated source does not derive the claimed target through accepted guards.
    known,_=closure([item['from']])
    assert item['to'] not in known,item['id']
baseline=OUT.parent/'baseline/extended_controls.py'
expected='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()==expected
report={'status':'PASS','date':'2026-11-03','node_count':len(ids),'rule_count':len(g['rules']),
 'source_records_checked':len(sources),'scenario_count':len(scenario_results),
 'guarded_cyclic_components':sorted(components),'prohibited_shortcuts_checked':len(g['prohibited_shortcuts']),
 'scenarios':scenario_results,
 'complete_event_closed_from_supplied_input':True,
 'unique_origin_closed_from_reviewed_formation_packet':False,
 'full_historical_impossibility_or_independence_theorem':False,
 'new_physical_rule_adopted':False,'event_rule_modified':False,
 'scope':'Dependency bookkeeping, source-record existence, guarded forward closure and cycle diagnostics; not a formal proof of attached mathematical theorems'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='scenarios'},indent=2))
