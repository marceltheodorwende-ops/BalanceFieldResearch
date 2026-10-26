"""Paired patient-level exact statistics and resampling; no inferential decision."""
from fractions import Fraction
from cohort_coverage import coverage_report, count
from recording_time import exact


def aggregate_pairs(expected, receipts_a, receipts_b):
    if not coverage_report(expected,receipts_a)['complete'] or not coverage_report(expected,receipts_b)['complete']:
        raise ValueError('Both methods require the same complete expected records')
    patients={};deadlines=set()
    for row in expected:
        p=patients.setdefault(row['person'],dict(seconds=Fraction(),events=0,a_tp=0,b_tp=0,a_fp=0,b_fp=0))
        p['seconds']+=exact(row['seconds']);p['events']+=count(row['events'])
        for label,receipts in [('a',receipts_a),('b',receipts_b)]:
            s=receipts[row['record_id']]['result']['timely']
            tp=count(s['timely_events']);fp=count(s['false_activations'])
            if tp>row['events']:raise ValueError('Impossible detected reference count')
            p[label+'_tp']+=tp;p[label+'_fp']+=fp
            deadlines.add(Fraction(s['deadline_seconds']))
    if len(deadlines)!=1:raise ValueError('Mixed event deadline conventions')
    return [dict(person=k,**{name:str(v) if name=='seconds' else v for name,v in value.items()}) for k,value in sorted(patients.items())]


def paired_statistic(patients, indices):
    seconds=sum((exact(patients[i]['seconds']) for i in indices),Fraction())
    events=sum(patients[i]['events'] for i in indices)
    tp=sum(patients[i]['a_tp']-patients[i]['b_tp'] for i in indices)
    fp=sum(patients[i]['a_fp']-patients[i]['b_fp'] for i in indices)
    return dict(sensitivity_difference=str(Fraction(tp,events)) if events else None,
                false_activations_per24h_difference=str(86400*fp/seconds),
                seconds=str(seconds),events=events)


def paired_resamples(patients, draws):
    n=len(patients)
    if n<2 or len({p['person'] for p in patients})!=n:
        raise ValueError('At least two distinct already-aggregated people required')
    results=[]
    for draw in draws:
        if len(draw)!=n or any(isinstance(i,bool) or not isinstance(i,int) or not 0<=i<n for i in draw):
            raise ValueError('Each paired draw must contain n patient indices')
        results.append(paired_statistic(patients,draw))
    if not results:raise ValueError('Explicit resampling draws required')
    return dict(point=paired_statistic(patients,range(n)),resamples=results,
                undefined_sensitivity_draws=sum(r['sensitivity_difference'] is None for r in results),
                confidence_interval=None,decision='UNSPECIFIED: inferential rule and precision not frozen')
