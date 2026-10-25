"""Exact record-local annotation validation; no cross-record clock inference."""
from fractions import Fraction
import re


def exact(value):
    # No binary floats, NaN, implicit rounding or bool-as-integer times.
    if isinstance(value, bool) or not isinstance(value, (str, int, Fraction)):
        raise ValueError('Time must be an exact rational string, integer or Fraction')
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise ValueError('Invalid exact time') from error


def reconcile(duration, events, sampling_hz):
    """Validate original half-open events against one recording, without repair.

    Off-grid annotations are retained as exact seconds but sample conversion is
    unavailable. No event is dropped, clipped, merged or sorted into compliance.
    """
    duration, fs = exact(duration), exact(sampling_hz)
    if duration <= 0 or fs <= 0 or (duration * fs).denominator != 1:
        raise ValueError('Invalid duration/rate or nonintegral declared sample count')
    checked = []
    previous_end = Fraction(0)
    seizure_seconds = Fraction(0)
    for event in events:
        if len(event) != 2:
            raise ValueError('Event must contain start and end')
        start, end = map(exact, event)
        if not 0 <= start < end <= duration or start < previous_end:
            raise ValueError('Out-of-bounds, unordered or overlapping event')
        indices = (start * fs, end * fs)
        on_grid = all(x.denominator == 1 for x in indices)
        checked.append(dict(start=str(start), end=str(end), on_sample_grid=on_grid,
                            sample_interval=[int(x) for x in indices] if on_grid else None))
        previous_end = end
        seizure_seconds += end - start
    return dict(duration_seconds=str(duration), sampling_hz=str(fs),
                sample_count=int(duration * fs), events=checked,
                seizure_seconds=str(seizure_seconds),
                nonseizure_seconds=str(duration - seizure_seconds),
                inter_record_gap_seconds=None,
                cross_record_continuity='UNRESOLVED: no dated clock relation supplied')


def clock_seconds(text):
    """Parse source clock notation, allowing hour24; never infer dates."""
    match = re.fullmatch(r'(\d{1,2}):([0-5]\d):([0-5]\d)', text)
    if not match or int(match[1]) > 24:
        raise ValueError('Unsupported clock notation')
    return 3600 * int(match[1]) + 60 * int(match[2]) + int(match[3])
