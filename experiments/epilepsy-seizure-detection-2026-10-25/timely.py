"""Supplementary fresh-activation endpoint. See TIMELY_ENDPOINT.md, not SzCORE."""
import math

def _number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError('Expected finite real seconds')
    try:
        result = float(value)
    except OverflowError as error:
        raise ValueError('Seconds outside floating-point range') from error
    if not math.isfinite(result):
        raise ValueError('Expected finite real seconds')
    return result

def _intervals(items, duration, alarms=False):
    result = []
    for pair in items:
        if len(pair) != 2:
            raise ValueError('Interval must have two endpoints')
        start, end = map(_number, pair)
        if not 0 <= start < end <= duration:
            raise ValueError('Interval outside recording or empty')
        if result and (start < result[-1][1] or (alarms and start == result[-1][1])):
            raise ValueError('Unordered, overlapping or adjacent alarm intervals')
        result.append((start, end))
    return result

def score_timely(references, alarms, duration, deadline):
    """Pure scoring; callers must provide actual causal activation timestamps.

    Returns JSON-safe sufficient statistics; undefined sensitivity is None.
    No reference merging/splitting, smoothing, tolerance or refractory suppression.
    """
    duration, deadline = _number(duration), _number(deadline)
    if duration <= 0 or deadline < 0:
        raise ValueError('Positive duration and nonnegative deadline required')
    refs = _intervals(references, duration)
    active = _intervals(alarms, duration, alarms=True)
    first = [None] * len(refs)
    outside = late_activations = 0
    i = 0
    for activation, _ in active:
        while i < len(refs) and refs[i][1] <= activation:
            i += 1
        if i < len(refs) and refs[i][0] <= activation:
            latency = activation - refs[i][0]
            if first[i] is None:
                first[i] = latency
            if latency > deadline:
                late_activations += 1
        else:
            outside += 1
    timely = sum(x is not None and x <= deadline for x in first)
    late_events = sum(x is not None and x > deadline for x in first)
    alarm_seconds = math.fsum(end-start for start, end in active)
    def daily_rate(count):
        if count == 0:
            return 0.0
        rate = (count / duration) * 86400
        if not math.isfinite(rate):
            raise ValueError('Daily rate outside floating-point range')
        return rate
    return dict(recording_seconds=duration, deadline_seconds=deadline,
        reference_events=len(refs), timely_events=timely,
        late_events=late_events, events_without_fresh_activation=sum(x is None for x in first),
        first_activation_latencies=first,
        sensitivity=timely/len(refs) if refs else None,
        false_activations=outside, false_activations_per_24h=daily_rate(outside),
        late_ictal_activations=late_activations, alarm_activations=len(active),
        alarm_activations_per_24h=daily_rate(len(active)),
        alarm_seconds=alarm_seconds, alarm_fraction=alarm_seconds/duration)
