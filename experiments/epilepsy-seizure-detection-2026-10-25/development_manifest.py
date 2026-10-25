"""Offline, pinned-source manifest builder. No download or test authorization."""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
from contract import TRAIN, VALIDATION, INTERNAL_TEST, person, validate_split

ROOT = Path(__file__).resolve().parent
PINS = {
    'CHB_RECORDS': '72b640d6a3fef4b40de255933d1403823d1655c56f93d69761105a653798fc08',
    'CHB_SHA256SUMS.txt': 'f1698efeb9fef887e55cedf6eda13386d9a888db663aec48b2aa194b7b753d2b',
    'chb01-summary.txt': '77e86183845192d147c88a9bb4263c2b4a32e936c6236029770f86ca2ea023db',
    'SIENA_LICENSE.txt': '9a78e7f22742dde9f66ae235ec793ba2212019dc4d0ced75c4da09ced0b35fb2',
}
URLS = {
    'CHB_RECORDS': 'https://physionet.org/files/chbmit/1.0.0/RECORDS',
    'CHB_SHA256SUMS.txt': 'https://physionet.org/files/chbmit/1.0.0/SHA256SUMS.txt',
    'chb01-summary.txt': 'https://physionet.org/files/chbmit/1.0.0/chb01/chb01-summary.txt',
    'SIENA_LICENSE.txt': 'https://physionet.org/files/siena-scalp-eeg/1.0.0/LICENSE.txt',
}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def parse_records(data):
    records = data.decode('ascii').splitlines()
    if not records or len(records) != len(set(records)):
        raise ValueError('Empty or duplicate RECORDS')
    for path in records:
        if not re.fullmatch(r'chb(0[1-9]|1[0-9]|2[0-4])/chb\1[a-c]?_[0-9]+\+?\.edf', path):
            raise ValueError('Invalid or cross-case RECORDS path')
    return records

def parse_checksums(data):
    checks = {}
    for line in data.decode('ascii').splitlines():
        parts = line.split()
        if len(parts) != 2 or not re.fullmatch('[0-9a-f]{64}', parts[0]) or parts[1] in checks:
            raise ValueError('Malformed or duplicate source checksum')
        checks[parts[1]] = parts[0]
    if not checks:
        raise ValueError('Empty checksums')
    return checks

def select_development(records, checks):
    rows = []
    for path in records:
        case = path.split('/')[0]
        if case not in TRAIN + VALIDATION:
            continue
        if path not in checks or not re.fullmatch('[0-9a-f]{64}', checks[path]):
            raise ValueError('Missing or invalid development waveform checksum')
        rows.append(dict(dataset='chbmit', version='1.0.0', case=case,
            person=person(case), split='train' if case in TRAIN else 'validation',
            path=path, sha256=checks[path],
            url='https://physionet.org/files/chbmit/1.0.0/'+path))
    return sorted(rows, key=lambda r:r['path'])

def build_manifest():
    validate_split()
    data = {name:(ROOT/'source_metadata'/name).read_bytes() for name in PINS}
    if any(digest(data[name]) != expected for name, expected in PINS.items()):
        raise ValueError('Pinned metadata changed')
    checks = parse_checksums(data['CHB_SHA256SUMS.txt'])
    for name, source_name in [('CHB_RECORDS','RECORDS'),('chb01-summary.txt','chb01/chb01-summary.txt')]:
        if checks.get(source_name) != digest(data[name]):
            raise ValueError('Original source metadata checksum mismatch')
    records = parse_records(data['CHB_RECORDS'])
    if any(path not in checks for path in records):
        raise ValueError('RECORDS entry missing original checksum')
    rows = select_development(records, checks)
    return rows, dict(record_entries=len(records), development_entries=len(rows),
        train_entries=sum(r['split']=='train' for r in rows),
        validation_entries=sum(r['split']=='validation' for r in rows),
        sealed_internal_entries=sum(p.split('/')[0] in INTERNAL_TEST for p in records),
        acquired=[dict(path='source_metadata/'+name,url=URLS[name],sha256=PINS[name],bytes=len(data[name])) for name in PINS],
        exposure='chb01 development summary contains event annotations; no test annotations or waveforms fetched',
        waveform_download_enabled=False,confirmatory_freeze=False)

def development_entry(relative):
    rows, _ = build_manifest()  # Reconstruct from pinned sources; never trust a caller-supplied table.
    match = next((r for r in rows if r['path'] == relative), None)
    if match is None:
        raise ValueError('Not an exact development allowlist member')
    return match

def verify_development_bytes(relative, data):
    row = development_entry(relative)
    if digest(data) != row['sha256']:
        raise ValueError('Waveform byte hash mismatch')
    return row

if __name__ == '__main__':
    rows, summary = build_manifest()
    with (ROOT/'development_files.csv').open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]),lineterminator='\n')
        writer.writeheader();writer.writerows(rows)
    (ROOT/'development_manifest_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))
