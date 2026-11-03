"""Exact predictive quotient and observable-origin non-identifiability checks."""
from pathlib import Path
import itertools,json,hashlib

OUT=Path(__file__).resolve().parent
def canonical(values):
    seen={};labels=[]
    for x in values:
        if x not in seen:seen[x]=len(seen)
        labels.append(seen[x])
    return tuple(labels)
def quotient(transition,output):
    n=len(transition);colors=canonical(output);initial=len(set(colors));rounds=0
    while True:
        new=canonical((colors[x],colors[transition[x]]) for x in range(n))
        if new==colors:break
        colors=new;rounds+=1
        assert rounds<=n-initial
    blocks=[[x for x in range(n) if colors[x]==j] for j in range(len(set(colors)))]
    qt=[];qo=[]
    for block in blocks:
        assert len({output[x] for x in block})==1
        assert len({colors[transition[x]] for x in block})==1
        qt.append(colors[transition[block[0]]]);qo.append(output[block[0]])
    return colors,blocks,tuple(qt),tuple(qo),rounds
def same_future(transition,output,x,y):
    seen=set()
    while (x,y) not in seen:
        if output[x]!=output[y]:return False
        seen.add((x,y));x,y=transition[x],transition[y]
    return True
def partitions(n):
    def extend(prefix):
        if len(prefix)==n:
            yield tuple(prefix);return
        for label in range(max(prefix)+2):yield from extend(prefix+[label])
    yield from extend([0])

models=pairs=0;max_refinements=0;by_dimension=[]
for n in range(1,5):
    count=0
    for part in partitions(n):
        sizes={c:part.count(c) for c in set(part)}
        # Equality of these labels is equality of the tested balance/log-count pair.
        output=tuple((1,sizes[part[x]]) for x in range(n))
        for transition in itertools.product(range(n),repeat=n):
            colors,blocks,qt,qo,rounds=quotient(transition,output)
            for x,y in itertools.product(range(n),repeat=2):
                assert (colors[x]==colors[y])==same_future(transition,output,x,y)
                pairs+=1
            for a,b in itertools.combinations(range(len(blocks)),2):
                assert not same_future(qt,qo,a,b)
            max_refinements=max(max_refinements,rounds);models+=1;count+=1
    by_dimension.append({'labels':n,'models':count})
assert models==3984 and pairs==62688
# Positive-count delayed distinction: exact future disambiguates equal current values.
delay_t=(1,2,3,3,3);delay_o=((1,3),(1,3),(1,3),(1,2),(1,2))
colors,blocks,qt,qo,rounds=quotient(delay_t,delay_o)
assert blocks==[[0],[1],[2],[3,4]] and rounds==2
# Two nonisomorphic source packets have the same complete observation-stream set.
a_t=(1,0);b_t=(1,2,3,0);a_o=((1,2),)*2;b_o=((1,2),)*4
joined_t=a_t+tuple(2+x for x in b_t);joined_o=a_o+b_o
assert same_future(joined_t,joined_o,0,2)
assert len(quotient(a_t,a_o)[1])==len(quotient(b_t,b_o)[1])==1
assert a_o[0][1]==2 and len(quotient(a_t,a_o)[1])==1  # log(2) is not log(1)
# General copy construction on the delayed positive-information model.
copy_cases=0;copy_root_pairs=0;base_n=len(delay_t);copies=3
for sigma in itertools.product(range(copies),repeat=copies):
    lifted_t=tuple(sigma[a]*base_n+delay_t[x] for a in range(copies) for x in range(base_n))
    lifted_o=tuple(delay_o[x] for a in range(copies) for x in range(base_n))
    total_t=delay_t+tuple(base_n+j for j in lifted_t);total_o=delay_o+lifted_o
    for a in range(copies):
        for x in range(base_n):
            assert same_future(total_t,total_o,x,base_n+a*base_n+x)
            copy_root_pairs+=1
    assert len(quotient(lifted_t,lifted_o)[1])==len(blocks)
    copy_cases+=1
assert copy_cases==27 and copy_root_pairs==405
baseline=OUT.parent/'baseline/extended_controls.py'
assert hashlib.sha256(baseline.read_bytes()).hexdigest()=='f445aea3784bb2dcd2af1a6878dfb8dd4b377543ea729a73de718d6a6f880f86'
report={'status':'PASS','date':'2026-11-03','exhaustive_finite_models':models,
 'models_by_dimension':by_dimension,'independent_ordered_pair_checks':pairs,
 'maximum_proper_refinements_in_exhaustive_cases':max_refinements,
 'delayed_positive_information_example':{'transition':delay_t,'count_sizes':[3,3,3,2,2],'predictive_classes':blocks,'quotient_transition':qt,'quotient_observations':qo,'proper_refinements':rounds},
 'two_cycle_vs_four_cycle_same_tested_future':True,
 'replication_maps_checked':copy_cases,'replication_state_pairs_checked':copy_root_pairs,
 'minimal_observable_model_unique_given_complete_behavior':True,
 'full_balance_count_future_fixes_microscopic_model':False,
 'tested_observations_equal_full_source_canonical_datum':False,
 'inherited_quotient_information':'log(2), despite a one-state predictive quotient',
 'unique_fundamental_initializer_derived':False,'new_physical_rule_adopted':False,'event_rule_modified':False,
 'scope':'Finite predictive equivalence and exact relative observation non-identifiability; no full-source independence, complete BFG admissibility or empirical claim'}
(OUT/'results.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
print(json.dumps(report,indent=2))
