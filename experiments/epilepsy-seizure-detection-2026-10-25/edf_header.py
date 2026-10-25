"""Bounded EDF header parsing and development-only HTTP range metadata probe."""
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import re
import urllib.request
from development_manifest import development_entry
from montage_audit import BIPOLAR18

ROOT=Path(__file__).resolve().parent
MAX_SIGNALS=512  # Parser allocation bound, not a physiological parameter.
UNITS={'V':Fraction(1),'mV':Fraction(1,1000),'uV':Fraction(1,1000000)}

def ascii_field(data):
    return data.decode('ascii').strip()

def fixed_header(data):
    if len(data)!=256 or ascii_field(data[:8])!='0':
        raise ValueError('Unsupported or truncated EDF fixed header')
    size=int(ascii_field(data[184:192]));ns=int(ascii_field(data[252:256]))
    records=int(ascii_field(data[236:244]));duration=Fraction(ascii_field(data[244:252]))
    if not 1<=ns<=MAX_SIGNALS or size!=256*(ns+1):
        raise ValueError('Invalid/oversized EDF header dimensions')
    if records < -1 or duration<=0:
        raise ValueError('Invalid record count/duration')
    return dict(header_bytes=size,signals=ns,records=records,record_seconds=str(duration),
                discontinuous=ascii_field(data[192:236]).startswith('EDF+D'))

def parse_header(data):
    info=fixed_header(data[:256]);ns=info['signals']
    if len(data)!=info['header_bytes']:
        raise ValueError('Full signal header length mismatch')
    fields=[];pos=256
    for width in (16,80,8,8,8,8,8,80,8,32):
        fields.append([ascii_field(data[pos+i*width:pos+(i+1)*width]) for i in range(ns)])
        pos+=width*ns
    channels=[]
    for i in range(ns):
        pmin,pmax=Fraction(fields[3][i]),Fraction(fields[4][i])
        dmin,dmax=int(fields[5][i]),int(fields[6][i]);samples=int(fields[8][i])
        if not -32768<=dmin<dmax<=32767 or pmax<=pmin or samples<=0:
            raise ValueError('Invalid signal calibration or sample count')
        unit=fields[2][i];gain=(pmax-pmin)/(dmax-dmin)
        channels.append(dict(index=i,label=fields[0][i],unit=unit,
            physical_min=str(pmin),physical_max=str(pmax),digital_min=dmin,digital_max=dmax,
            samples_per_record=samples,sampling_hz=str(Fraction(samples)/Fraction(info['record_seconds'])),
            declared_prefilter=fields[7][i],volts_per_digital_step=str(gain*UNITS[unit]) if unit in UNITS else None))
    info['channels']=channels
    info['recording_seconds']=str(info['records']*Fraction(info['record_seconds'])) if info['records']>=0 else None
    info['expected_full_file_bytes']=info['header_bytes']+2*info['records']*sum(c['samples_per_record'] for c in channels) if info['records']>=0 else None
    # Identifying patient/recording text and raw dates are deliberately not emitted.
    return info

def to_volts(channel, digital):
    if channel['unit'] not in UNITS:
        raise ValueError('Unrecognized voltage unit; no silent substitution')
    pmin=Fraction(channel['physical_min']);pmax=Fraction(channel['physical_max'])
    return (pmin+(Fraction(digital)-channel['digital_min'])*(pmax-pmin)/(channel['digital_max']-channel['digital_min']))*UNITS[channel['unit']]

def candidate_channels(channels):
    result={}
    for label in BIPOLAR18:
        matches=[c['index'] for c in channels if c['label'].strip().upper()==label]
        result[label]=dict(indices=matches,status='unique' if len(matches)==1 else 'missing' if not matches else 'duplicate_unresolved')
    return result

def validate_range(status,content_range,start,end):
    match=re.fullmatch(r'bytes ([0-9]+)-([0-9]+)/([0-9]+)',content_range or '')
    if status!=206 or match is None:
        raise ValueError('Server did not honor a bounded byte range')
    a,b,total=map(int,match.groups())
    if a!=start or b!=end or total<=end:
        raise ValueError('Content-Range mismatch')
    return total

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*args,**kwargs):
        raise ValueError('Unexpected redirect; stop metadata acquisition')

def read_range(url,start,end):
    request=urllib.request.Request(url,headers={'Range':f'bytes={start}-{end}',
        'Accept-Encoding':'identity','User-Agent':'EP01-bounded-header-metadata/1.0'})
    # Default proxy/CA handlers are retained; no alternate credentials or routes.
    with urllib.request.build_opener(NoRedirect).open(request,timeout=15) as response:
        total=validate_range(response.status,response.headers.get('Content-Range'),start,end)
        data=response.read(end-start+1)  # Never ask for bytes outside the validated range.
        if len(data)!=end-start+1:
            raise ValueError('Truncated range body')
        return data,total

def probe(relative):
    # Validate exact development membership before constructing any network request.
    row=development_entry(relative)
    first,total=read_range(row['url'],0,255);fixed=fixed_header(first)
    rest,total2=read_range(row['url'],256,fixed['header_bytes']-1)
    if total!=total2:
        raise ValueError('File total changed across range requests')
    data=first+rest;parsed=parse_header(data)
    if parsed['expected_full_file_bytes'] is not None and parsed['expected_full_file_bytes']!=total:
        raise ValueError('EDF declared structure/file total mismatch')
    return dict(dataset='chbmit',path=relative,split=row['split'],url=row['url'],
        source_full_EDF_sha256=row['sha256'],full_EDF_sha256_verified=False,
        header_sha256=hashlib.sha256(data).hexdigest(),header_bytes_read=len(data),
        waveform_bytes_read=0,HTTP_range_total_bytes=total,metadata=parsed,
        candidate18=candidate_channels(parsed['channels']),
        limitation='One development EDF header only; no signal equality, gap continuity or physiological BFG identification established')

if __name__=='__main__':
    # One explicitly declared development record; no bulk or test mode.
    result=probe('chb01/chb01_01.edf')
    (ROOT/'development_header_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:v for k,v in result.items() if k not in ('metadata','candidate18')},indent=2))
