"""Identity/timestamp validation adapter; not a detector or causal-proof engine."""
from fractions import Fraction
import math
from recording_time import exact
from availability_audit import audit_availability
from timely import score_timely


def float_exact(value):
    value=exact(value)
    try: result=float(value)
    except OverflowError as error:raise ValueError('Unrepresentable scoring time') from error
    if not math.isfinite(result) or Fraction.from_float(result)!=value:
        raise ValueError('Scorer conversion would round exact time')
    return result


def score_record(record_id, annotation_record_id, mask_record_id, decision_record_id,
                 duration, events, sampling_hz, ready, invalid, decisions, deadline):
    if not isinstance(record_id,str) or not record_id or any(
        x!=record_id for x in (annotation_record_id,mask_record_id,decision_record_id)):
        raise ValueError('Explicit matching record identities required')
    coverage=audit_availability(duration,events,sampling_hz,ready,invalid)
    fs=exact(sampling_hz);n=len(ready);alarms=[]
    for d in decisions:
        if set(d)!={'onset_sample_end','offset_sample_end','evidence_sample_end'}:
            raise ValueError('Explicit onset, offset and evidence-end receipt required')
        onset,offset,evidence=(d[k] for k in ('onset_sample_end','offset_sample_end','evidence_sample_end'))
        if any(isinstance(v,bool) or not isinstance(v,int) for v in (onset,offset,evidence)):
            raise ValueError('Integer sample-end indices required')
        if not 1<=evidence<=onset<offset<=n:
            raise ValueError('Future evidence or invalid record-end indices')
        if not ready[onset-1]:
            raise ValueError('Alarm activation without a ready output')
        alarms.append([float_exact(Fraction(onset)/fs),float_exact(Fraction(offset)/fs)])
    refs=[[float_exact(e['start']),float_exact(e['end'])] for e in coverage['original_events']]
    scores=score_timely(refs,alarms,float_exact(duration),float_exact(deadline))
    return dict(record_id=record_id,coverage=coverage,timely=scores,
                validated_alarm_intervals=alarms,
                causality_status='Declared evidence bounds checked; actual model information use NOT proven',
                clinical_result=False)
