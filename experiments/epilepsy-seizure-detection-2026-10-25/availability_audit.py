"""Full-record availability accounting only; not alarm/event matching."""
from fractions import Fraction
import numpy as np
from recording_time import reconcile, exact


def audit_availability(duration, events, sampling_hz, ready, invalid):
    base=reconcile(duration, events, sampling_hz)
    n=base['sample_count'];fs=exact(sampling_hz)
    ready=np.asarray(ready);invalid=np.asarray(invalid)
    if any(x.dtype!=np.bool_ or x.shape!=(n,) for x in (ready,invalid)):
        raise ValueError('Complete one-record boolean masks required')
    if np.any(ready & invalid):
        raise ValueError('Invalid samples cannot be ready')
    intervals=[(Fraction(e['start']),Fraction(e['end'])) for e in base['events']]
    per_event=[]
    for a,b in intervals:
        # Bound loop by intersecting sample cells; support fractional annotations.
        start=int(a*fs);end=-(-(b*fs).numerator//(b*fs).denominator)
        overlap=Fraction(0)
        for i in range(start,min(end,n)):
            if ready[i]:
                overlap+=max(Fraction(0),min(b,Fraction(i+1)/fs)-max(a,Fraction(i)/fs))
        per_event.append(dict(start=str(a),end=str(b),ready_overlap_seconds=str(overlap),
                              unavailable_overlap_seconds=str(b-a-overlap)))
    ready_seconds=Fraction(int(ready.sum()))/fs
    invalid_seconds=Fraction(int(invalid.sum()))/fs
    warmup_seconds=Fraction(n-int(ready.sum())-int(invalid.sum()))/fs
    return dict(recorded_seconds=base['duration_seconds'],
        original_event_count=len(intervals),original_events=base['events'],
        ready_seconds=str(ready_seconds),invalid_seconds=str(invalid_seconds),
        warmup_seconds=str(warmup_seconds),
        unavailable_seconds=str(invalid_seconds+warmup_seconds),
        per_event=per_event,
        full_record_rate_denominator_seconds=base['duration_seconds'],
        original_sensitivity_denominator=len(intervals),
        alarm_matching_performed=False,
        limitation='Readiness is retrospective cell accounting, not an alarm timestamp; preserve sample-end availability for causal detection')
