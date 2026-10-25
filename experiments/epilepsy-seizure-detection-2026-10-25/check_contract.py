"""Independent edge controls; synthetic event times are not patient evidence."""
import csv
import io
import json
import sys
from pathlib import Path
import numpy as np
from contract import *
sys.path.insert(0, str(Path(__file__).parent / 'vendor'))
from timescoring.annotations import Annotation
from timescoring.scoring import EventScoring

checks = []
def check(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

check('23 real persons / 24 cases split 14,4,5', validate_split() == [14,4,5])
check('repeat session aliases same person', person('chb01') == person('chb21'))
try:
    validate_split(tuple(x for x in TRAIN if x != 'chb21'), VALIDATION + ('chb21',), INTERNAL_TEST)
except ValueError:
    checks.append('adversarial repeat-session leakage rejected')
else:
    raise AssertionError('leakage accepted')
check('development summary allowed', permit_metadata('chbmit', 'chb01/chb01-summary.txt'))
for path in ('chb19/chb19-summary.txt', '../RECORDS', '/RECORDS', 'x/../RECORDS',
             'chb01/chb01_01.edf', 'chb01/chb01_01.edf.seizures', 'all.zip'):
    check('metadata denied: ' + path, not permit_metadata('chbmit', path))
check('external annotations sealed', not permit_metadata('siena-scalp-eeg', 'PN00/Seizures-list-PN00.txt'))
check('all EEG sealed before exact allowlist', not permit_eeg('chbmit', 'chb01/chb01_01.edf'))

def score(ref, hyp, duration=300, strict=False):
    # Integer decisecond boundary cases with analytically known counts.
    p = EventScoring.Parameters(toleranceStart=0, toleranceEnd=0,
          minDurationBetweenEvents=0) if strict else EventScoring.Parameters()
    return EventScoring(Annotation(ref, 10, duration*10), Annotation(hyp, 10, duration*10), p)

default = score([(100,110)], [(150,151)])
strict = score([(100,110)], [(150,151)], strict=True)
check('default postictal-only alarm counted true', default.tp == 1 and default.fp == 0)
check('strict postictal-only alarm rejected', strict.tp == 0 and strict.fp == 1)
merged = score([(100,110),(180,190)], [])
check('default changes reference event denominator', merged.refTrue == 1)
check('strict preserves these two references', score([(100,110),(180,190)], [], strict=True).refTrue == 2)
empty = score([], [])
check('no seizures => sensitivity undefined', np.isnan(empty.sensitivity) and empty.fpRate == 0)
check('one false alarm in 300s => 288/day', score([],[(10,11)]).fpRate == 288)
check('exact endpoint contact not overlap strict', score([(100,110)],[(110,111)],strict=True).tp == 0)
check('long reference split into scoring units', score([(0,601)],[],duration=900,strict=True).refTrue == 3)
check('perfect strict match', score([(100,110)],[(100,110)],strict=True).sensitivity == 1)

manifest = Path(__file__).parent / 'audit_sources/data_manifest.csv'
rows = list(csv.DictReader(io.StringIO(manifest.read_text())))
check('prior data exactly 109 persons x 2 runs', len(rows) == 218 and
      {int(r['subject']) for r in rows} == set(range(1,110)) and
      all({int(r['run']) for r in rows if int(r['subject']) == i} == {1,2} for i in range(1,110)))
check('prior provenance only eegmmidb', all('/eegmmidb/1.0.0/' in r['url'] for r in rows))
result = dict(status='PASS', controls=len(checks), checks=checks, numpy=np.__version__,
    split_person_counts=validate_split(), prior_measurement_files=len(rows),
    counterexample=dict(reference=[[100,110]], alarm=[[150,151]],
      default_tp=int(default.tp), default_fp=int(default.fp), strict_tp=int(strict.tp), strict_fp=int(strict.fp)),
    empirical_result=False, confirmatory_freeze=False)
Path(__file__).with_name('contract_checks.json').write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps(result, indent=2))
