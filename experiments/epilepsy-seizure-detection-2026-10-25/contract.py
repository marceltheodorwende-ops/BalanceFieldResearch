"""EP01 preparatory access contract. No network or measurement-file access."""
from pathlib import PurePosixPath
import re

TRAIN = tuple(f'chb{i:02d}' for i in range(1, 15)) + ('chb21',)
VALIDATION = tuple(f'chb{i:02d}' for i in range(15, 19))
INTERNAL_TEST = ('chb19', 'chb20', 'chb22', 'chb23', 'chb24')
SIENA_EXTERNAL = ('PN00', 'PN01', 'PN03', 'PN05', 'PN06', 'PN07', 'PN09',
                  'PN10', 'PN11', 'PN12', 'PN13', 'PN14', 'PN16', 'PN17')

def person(case):
    if not re.fullmatch(r'chb(0[1-9]|1[0-9]|2[0-4])', case):
        raise ValueError('Unknown CHB case')
    return 'chb01' if case == 'chb21' else case

def validate_split(train=TRAIN, validation=VALIDATION, test=INTERNAL_TEST):
    groups = [set(map(person, x)) for x in (train, validation, test)]
    if any(groups[i] & groups[j] for i in range(3) for j in range(i)):
        raise ValueError('Person leakage across partitions')
    cases = tuple(train) + tuple(validation) + tuple(test)
    if len(cases) != len(set(cases)) or set(cases) != {f'chb{i:02d}' for i in range(1,25)}:
        raise ValueError('Duplicate or missing case')
    return [len(g) for g in groups]

def permit_metadata(dataset, relative):
    """Only development metadata; no test annotation files or archives."""
    p = PurePosixPath(relative)
    if p.is_absolute() or '..' in p.parts or '\\' in relative:
        return False
    if dataset == 'chbmit':
        if relative in ('RECORDS', 'SHA256SUMS.txt', 'SUBJECT-INFO'):
            return True
        return any(relative == f'{case}/{case}-summary.txt'
                   for case in TRAIN + VALIDATION)
    # Siena is sealed external, including subject-specific metadata/annotations.
    return dataset == 'siena-scalp-eeg' and relative in ('LICENSE.txt',)

def permit_eeg(dataset, relative):
    """Full waveform gate remains closed pending acquisition/preprocessing contract.

    The separate development-only EDF header probe reads validated header ranges,
    never samples. Exact manifest membership alone does not open this gate.
    """
    return False
