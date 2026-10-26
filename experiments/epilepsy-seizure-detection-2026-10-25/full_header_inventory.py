"""Finite development-only header inventory. CLI requires explicit execution."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import os
from development_manifest import build_manifest, parse_checksums, PINS
from annotation_import import parse_summary, join_header
from annotation_reconciliation import reconcile_summary
from channel_policy import compile_map
from edf_header import probe
from contract import TRAIN, VALIDATION


def load_records(binary_path):
    root=Path(__file__).resolve().parent
    raw=(root/'source_metadata/CHB_SHA256SUMS.txt').read_bytes()
    if hashlib.sha256(raw).hexdigest()!=PINS['CHB_SHA256SUMS.txt']:raise ValueError('Master checksum mismatch')
    pins=parse_checksums(raw);records={}
    for case in TRAIN+VALIDATION:
        data=(root/'source_metadata'/f'{case}-summary.txt').read_bytes()
        if hashlib.sha256(data).hexdigest()!=pins[f'{case}/{case}-summary.txt']:raise ValueError('Summary hash mismatch')
        if case=='chb09':
            data,_=reconcile_summary(data,case,'chb09/chb09_08.edf',Path(binary_path).read_bytes(),[(2,'End',1)])
        records.update(parse_summary(data.decode('ascii'),case,numbered_events=True,channel_sections=True,extended_clock_tokens=True,event_value_spacing=True))
    return records


def atomic_json(path,value):
    temporary=path.with_suffix('.pending')
    temporary.write_text(json.dumps(value,indent=2)+'\n')
    os.replace(temporary,path)


def run_inventory(records, output, *, workers=4, probe_fn=probe):
    manifest,_=build_manifest();paths=sorted(r['path'] for r in manifest)
    if set(records)!=set(paths):raise ValueError('Exact full development manifest required before acquisition')
    if isinstance(workers,bool) or not isinstance(workers,int) or not 1<=workers<=4:raise ValueError('One to four workers required')
    # Do not overwrite a previous run or silently reuse stale receipts.
    output=Path(output);output.mkdir(parents=True,exist_ok=False)
    atomic_json(output/'selection.json',dict(paths=paths,count=len(paths),mode='validated header ranges only',waveform_access=False))
    def one(path):
        try:
            header=probe_fn(path,retain_invalid_calibration=True)
            if header['path']!=path or header['waveform_bytes_read']!=0:raise ValueError('Wrong header identity or sample access')
            mapping=compile_map(header['metadata'])
            joined=join_header(records[path],header,256)
            return dict(path=path,status='eligible' if mapping['eligible'] else 'metadata_ineligible',
                header_sha256=header['header_sha256'],header_bytes=header['header_bytes_read'],
                full_EDF_hash_verified=False,reasons=mapping['reasons'],record=joined)
        except Exception as error:
            return dict(path=path,status='failed',error_type=type(error).__name__,error=str(error))
    results=[]
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures={executor.submit(one,path):path for path in paths}
        for future in as_completed(futures):
            receipt=future.result();key=hashlib.sha256(receipt['path'].encode()).hexdigest()
            atomic_json(output/(key+'.json'),receipt);results.append(receipt)
    results.sort(key=lambda x:x['path'])
    failed=sum(r['status']=='failed' for r in results)
    seconds=sum((Fraction(r['record']['duration_seconds']) for r in results if r['status']!='failed'),Fraction())
    summary=dict(expected_files=len(paths),attempted_files=len(results),failed_files=failed,
        metadata_ineligible_files=sum(r['status']=='metadata_ineligible' for r in results),
        eligible_files=sum(r['status']=='eligible' for r in results),
        all_files_attempted=len(results)==len(paths),all_metadata_eligible=all(r['status']=='eligible' for r in results),
        successfully_joined_seconds=str(seconds),full_cohort_recorded_seconds=str(seconds) if not failed else None,
        waveform_access_enabled=False,clinical_result=False)
    atomic_json(output/'summary.json',summary)
    return summary


if __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--execute',action='store_true',required=True)
    parser.add_argument('--binary-companion',required=True)
    parser.add_argument('--output',required=True)
    args=parser.parse_args()
    print(json.dumps(run_inventory(load_records(args.binary_companion),args.output),indent=2))
