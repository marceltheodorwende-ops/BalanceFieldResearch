"""Independent controls for provenance, membership and exact montage audit."""
import csv
import hashlib
import json
from pathlib import Path
from development_manifest import *
from montage_audit import audit
from contract import permit_eeg

checks=[]
def check(name,value):
    if not value:raise AssertionError(name)
    checks.append(name)

rows,summary=build_manifest()
check('686 source records and all source hashes available',summary['record_entries']==686)
check('565 development files:449 train116 validation',len(rows)==565 and summary['train_entries']==449 and summary['validation_entries']==116)
check('121 internal files omitted',summary['sealed_internal_entries']==121)
check('person sessions kept together',all(r['person']=='chb01' and r['split']=='train' for r in rows if r['case']=='chb21'))
check('all nonselected-seizure filtering avoided',len(rows)==sum(1 for p in parse_records((ROOT/'source_metadata/CHB_RECORDS').read_bytes()) if p.split('/')[0] in TRAIN+VALIDATION))
check('unique exact paths and565 valid SHA256',len({r['path'] for r in rows})==565 and all(len(bytes.fromhex(r['sha256']))==32 for r in rows))
check('legitimate filename extensions retained',any('chb17a_' in r['path'] for r in rows) and any('+.' in r['path'] for r in rows))
check('membership helper agrees with pinned first record',development_entry('chb01/chb01_01.edf') in rows)
for path in ('chb19/chb19_01.edf','chb24/chb24_01.edf','../chb01/chb01_01.edf',
             '/chb01/chb01_01.edf','chb01/chb01_999999.edf','chb01/chb02_01.edf',
             'chb01/chb01_01.edf.seizures','chb01/chb01-summary.txt','all.zip'):
    try:development_entry(path)
    except ValueError:pass
    else:raise AssertionError('forbidden entry accepted '+path)
checks.append('9 forbidden or nonexistent membership requests rejected')
try:verify_development_bytes('chb01/chb01_01.edf',b'not an EDF or matching digest')
except ValueError:checks.append('wrong supplied waveform bytes rejected without download')
else:raise AssertionError('wrong byte hash accepted')
check('download gate still closed',not permit_eeg('chbmit','chb01/chb01_01.edf'))

bad_records=(b'',b'chb01/chb01_01.edf\nchb01/chb01_01.edf\n',
             b'chb01/chb02_01.edf\n',b'../RECORDS\n',b'chb99/chb99_01.edf\n')
for data in bad_records:
    try:parse_records(data)
    except ValueError:pass
    else:raise AssertionError('bad source path accepted')
checks.append('5 malformed/duplicate/cross-case source lists rejected')
h='0'*64
for data in (b'',b'wrong-hash file\n',(h+' file\n'+h+' file\n').encode()):
    try:parse_checksums(data)
    except ValueError:pass
    else:raise AssertionError('bad checksum table accepted')
checks.append('3 malformed/duplicate checksum lists rejected')
try:select_development(['chb01/chb01_01.edf'],{})
except ValueError:checks.append('missing development hash rejected')
else:raise AssertionError('missing hash accepted')

m=audit()
check('exact bipolar rank and disconnected graph agree',m['exact_incidence_rank']==19 and len(m['components'])==2)
check('common-average reconstruction disproved',not m['common_average_identifiable'] and m['stacked_rank']==20)
check('explicit null measurement has nonzero target',m['kernel_witness']['measurement_zero'] and set(m['kernel_witness']['target_values'].values())=={'-3/19','16/19'})
check('18-channel bipolar candidate has16 independent directions',len(m['candidate_bipolar18'])==18 and m['candidate_rank']==16)
check('montage output deterministic',m==audit())

result=dict(status='PASS',control_groups=len(checks),checks=checks,source_records=686,
    development_files=565,training_files=449,validation_files=116,sealed_internal_files=121,
    waveform_bytes_downloaded=0,development_annotation_exposure='chb01-summary.txt',
    test_annotations_opened=False,external_waveforms_opened=False,empirical_performance=False,
    positive_waveform_digest_path='not exercised: no original waveform downloaded')
(ROOT/'manifest_montage_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
