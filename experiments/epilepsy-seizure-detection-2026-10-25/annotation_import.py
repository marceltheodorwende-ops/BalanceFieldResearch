"""Offline CHB summary dialect import; no acquisition or clock-gap inference."""
import hashlib
import re
from pathlib import Path
from development_manifest import development_entry, PINS
from contract import TRAIN, VALIDATION
from recording_time import clock_seconds, reconcile


def parse_summary(text, case, *, numbered_events=False, channel_sections=False, extended_clock_tokens=False):
    if case not in TRAIN + VALIDATION:
        raise ValueError('Only development/validation cases are accepted')
    parts = text.split('File Name: ')
    if len(parts) < 2 or 'Seizure' in parts[0]:
        raise ValueError('Missing file blocks or orphan event metadata')
    records = {}
    for block in parts[1:]:
        lines = [s.strip() for s in block.splitlines() if s.strip()]
        if len(lines) < 4:
            raise ValueError('Incomplete file block')
        name = lines[0]
        row = development_entry(case+'/'+name)
        if row['path'] in records:
            raise ValueError('Duplicate file annotation block')
        clocks = []
        for line, prefix in zip(lines[1:3], ('File Start Time: ', 'File End Time: ')):
            if not line.startswith(prefix):
                raise ValueError('Missing or reordered file clock')
            value = line[len(prefix):]
            if extended_clock_tokens:
                if re.fullmatch(r'(\d{1,2}):([0-5]\d):([0-5]\d)', value) is None:
                    raise ValueError('Unsupported extended clock token')
            else:
                clock_seconds(value)
            clocks.append(value)
        count = re.fullmatch(r'Number of Seizures in File: (\d+)', lines[3])
        if count is None:
            raise ValueError('Missing event count')
        count = int(count[1])
        boundary = 4 + 2*count
        changes = []
        if len(lines) < boundary:
            raise ValueError('Event count/line mismatch or unsupported metadata')
        tail = lines[boundary:]
        if tail and not channel_sections:
            raise ValueError('Event count/line mismatch or unsupported metadata')
        while tail:
            if len(tail) < 3 or tail[0] != 'Channels changed:' or set(tail[1]) != {'*'}:
                raise ValueError('Unknown or incomplete channel-change section')
            tail = tail[2:]
            channels = []
            while tail and tail[0] != 'Channels changed:':
                match = re.fullmatch(r'Channel (\d+): (.+)', tail[0])
                if match is None or int(match[1]) != len(channels)+1:
                    raise ValueError('Invalid channel-change index or unknown line')
                channels.append(dict(index=int(match[1]), label=match[2]))
                tail = tail[1:]
            if not channels:
                raise ValueError('Empty channel-change section')
            changes.append(dict(channels=channels, scope='between_file_blocks_unassigned'))
        events = []
        numbered_block = None
        previous_end = 0
        for i in range(count):
            pair = []
            for line, kind in zip(lines[4+2*i:6+2*i], ('Start', 'End')):
                pattern = r'Seizure(?: (\d+))? '+kind+r' Time: (\d+) seconds'
                match = re.fullmatch(pattern, line)
                if match is None:
                    raise ValueError('Unsupported or incomplete event pair')
                indexed = match[1] is not None
                if indexed and not numbered_events:
                    raise ValueError('Numbered-event mode must be explicitly enabled')
                if numbered_block is None:
                    numbered_block = indexed
                if indexed != numbered_block or (indexed and int(match[1]) != i+1):
                    raise ValueError('Mixed, mismatched or nonconsecutive event numbering')
                pair.append(int(match[2]))
            if not previous_end <= pair[0] < pair[1]:
                raise ValueError('Unordered, overlapping or empty source event')
            previous_end = pair[1]
            events.append(pair)
        records[row['path']] = dict(path=row['path'],person=row['person'],split=row['split'],
            source_start_clock=clocks[0],source_end_clock=clocks[1],events=events,
            declared_event_count=count,duration_verified=False)
        if changes:
            records[row['path']]['following_channel_change_sections'] = changes
    return records


def load_pinned_chb01():
    data = Path(__file__).with_name('source_metadata').joinpath('chb01-summary.txt').read_bytes()
    if hashlib.sha256(data).hexdigest() != PINS['chb01-summary.txt']:
        raise ValueError('Source summary hash mismatch')
    return parse_summary(data.decode('ascii'), 'chb01')


def join_header(record, header, sampling_hz):
    """Join by exact path, then validate source events against EDF duration.

    sampling_hz is an explicit target-channel rate, not inferred from clocks.
    """
    if record['path'] != header['path']:
        raise ValueError('Annotation/header path mismatch')
    development_entry(record['path'])
    metadata = header['metadata']
    if metadata.get('discontinuous') or metadata.get('recording_seconds') is None:
        raise ValueError('Continuous, known EDF duration required')
    return reconcile(metadata['recording_seconds'], record['events'], sampling_hz)
