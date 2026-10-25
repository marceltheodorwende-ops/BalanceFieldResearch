"""Synthetic EDF fixture and access/range controls; no network or patient signals."""
from fractions import Fraction
import json
from pathlib import Path
from unittest.mock import patch
import edf_header as e

checks=[]
def check(name,value):
    if not value:raise AssertionError(name)
    checks.append(name)

def field(value,width):return str(value).encode().ljust(width,b' ')
def fixture(labels=('FP1-F7','TEMP'),units=('uV','degreeC'),samples=(128,1)):
    n=len(labels)
    head=b''.join([field('0',8),field('PRIVATE PATIENT',80),field('PRIVATE RECORD',80),
        field('01.01.00',8),field('00.00.00',8),field(256*(n+1),8),field('',44),field(2,8),field('.5',8),field(n,4)])
    values=[labels,['sensor']*n,units,[-100]*n,[100]*n,[-1000]*n,[1000]*n,['HP:0.1Hz']*n,samples,['']*n]
    return head+b''.join(field(v,w) for vals,w in zip(values,(16,80,8,8,8,8,8,80,8,32)) for v in vals)

data=fixture();parsed=e.parse_header(data)
check('exact fixture length and duration',parsed['header_bytes']==768 and parsed['recording_seconds']=='1')
check('different signal rates preserved', [c['sampling_hz'] for c in parsed['channels']]==['256','2'])
check('hand-calculated gain',parsed['channels'][0]['volts_per_digital_step']=='1/10000000')
check('calibration min midpoint max', [e.to_volts(parsed['channels'][0],d) for d in (-1000,0,1000)]==[Fraction(-1,10000),Fraction(0),Fraction(1,10000)])
check('intermediate digital500 is50microvolts',e.to_volts(parsed['channels'][0],500)==Fraction(1,20000))
check('unknown auxiliary unit is flagged',parsed['channels'][1]['volts_per_digital_step'] is None)
try:e.to_volts(parsed['channels'][1],0)
except ValueError:checks.append('unknown unit never silently converted')
else:raise AssertionError('unknown unit accepted')
check('no private identity fields emitted','PRIVATE' not in json.dumps(parsed))
dup=e.parse_header(fixture(labels=('T8-P8','T8-P8'),units=('uV','uV')))
check('duplicate channel not arbitrarily selected',e.candidate_channels(dup['channels'])['T8-P8']['status']=='duplicate_unresolved')
check('missing target explicitly flagged',e.candidate_channels(parsed['channels'])['CZ-PZ']['status']=='missing')
invalid=[data[:255],data[:-1],data[:184]+field(0,8)+data[192:],
         data[:244]+field(0,8)+data[252:],data[:236]+field(-2,8)+data[244:],
         data[:252]+field(513,4)+data[256:],fixture(samples=(0,1))]
for b in invalid:
    try:e.parse_header(b)
    except (ValueError,ZeroDivisionError):pass
    else:raise AssertionError('invalid EDF accepted')
checks.append('7 malformed/truncated/oversize/zero-rate headers rejected')
for start,value in ((256+16*2+80*2+8*2+8*2,'-100'),
                    (256+16*2+80*2+8*2+8*2+8*2,'40000')):
    bad=data[:start]+field(value,8)+data[start+8:]
    try:e.parse_header(bad)
    except ValueError:pass
    else:raise AssertionError('invalid calibration accepted')
checks.append('nonordered physical and out-of-int16 digital limits rejected')
for status,cr in ((200,None),(206,'bytes 1-256/1000'),(206,'bytes 0-255/*'),(206,'bytes 0-255/255')):
    try:e.validate_range(status,cr,0,255)
    except ValueError:pass
    else:raise AssertionError('bad range accepted')
checks.append('4 range/status mismatches rejected')
check('correct Content-Range accepted',e.validate_range(206,'bytes 0-255/1000',0,255)==1000)

class Response:
    def __init__(self,status=206):self.status=status;self.headers={'Content-Range':'bytes 0-3/100'};self.calls=[]
    def __enter__(self):return self
    def __exit__(self,*args):pass
    def read(self,n):self.calls.append(n);return b'abcd'
class Opener:
    def __init__(self,response):self.response=response
    def open(self,*args,**kwargs):return self.response
resp=Response()
with patch.object(e.urllib.request,'build_opener',return_value=Opener(resp)):
    got,total=e.read_range('https://physionet.org/fake-control',0,3)
check('reader requests only exact bounded bytes',got==b'abcd' and resp.calls==[4] and total==100)
resp=Response(status=200)
with patch.object(e.urllib.request,'build_opener',return_value=Opener(resp)):
    try:e.read_range('https://physionet.org/fake-control',0,3)
    except ValueError:pass
    else:raise AssertionError('ignored range read')
check('ignored range refused before body read',resp.calls==[])
resp=Response()
resp.read=lambda n:b'abc'
with patch.object(e.urllib.request,'build_opener',return_value=Opener(resp)):
    try:e.read_range('https://physionet.org/fake-control',0,3)
    except ValueError:pass
    else:raise AssertionError('truncated body accepted')
checks.append('truncated range body rejected')
with patch.object(e,'read_range',side_effect=AssertionError('Network must not be called')):
    for path in ('chb19/chb19_01.edf','chb24/chb24_01.edf','../chb01/chb01_01.edf','PN00/anything.edf'):
        try:e.probe(path)
        except ValueError:pass
        else:raise AssertionError('forbidden network attempt')
checks.append('4 heldout/traversal/external requests denied before network')
try:e.NoRedirect().redirect_request(None,None,None,None,None,None)
except ValueError:checks.append('redirect explicitly rejected')
else:raise AssertionError('redirect allowed')
# Retention mode preserves structural accounting; calibration is never invented.
from channel_policy import TARGET17, compile_map
labels=TARGET17+('-',);n=len(labels)
base=fixture(labels=labels,units=('uV',)*n,samples=(128,)*n)
# Digital minimum and maximum are grouped fields, offsets from EDF specification.
offset_min=256+n*(16+80+8+8+8)
offset_max=offset_min+8*n
bad=bytearray(base)
for off in (offset_min,offset_max):bad[off+8*(n-1):off+8*n]=field(0,8)
try:e.parse_header(bytes(bad))
except ValueError:checks.append('strict default still rejects unused invalid calibration')
else:raise AssertionError('strict behavior changed')
retained=e.parse_header(bytes(bad),retain_invalid_calibration=True)
check('retained placeholder has explicit invalid calibration and no invented gain',
      retained['channels'][-1]['calibration_valid'] is False and
      retained['channels'][-1]['volts_per_digital_step'] is None and
      retained['channels'][-1]['calibration_error'] is not None)
check('unused placeholder does not prevent valid target mapping',compile_map(retained)['eligible'])
check('all rows still contribute to full file size',retained['expected_full_file_bytes']==256*(n+1)+2*2*128*n)
try:e.to_volts(retained['channels'][-1],0)
except ValueError:checks.append('invalid retained channel conversion forbidden')
else:raise AssertionError('invalid channel converted')
bad_target=bytearray(base)
for off in (offset_min,offset_max):bad_target[off:off+8]=field(0,8)
target=e.parse_header(bytes(bad_target),retain_invalid_calibration=True)
check('invalid required target remains ineligible',not compile_map(target)['eligible'])
for malformed in (bytes(bad)[:-1],fixture(samples=(0,1))):
    try:e.parse_header(malformed,retain_invalid_calibration=True)
    except ValueError:pass
    else:raise AssertionError('retention bypassed structural rejection')
checks.append('retention mode still rejects truncation and zero sample count')

# Public probe integration uses the exact header ranges and unchanged allowlist.
full_size=256*(n+1)+2*2*128*n
calls=[]
def fixture_range(url,start,end):
    calls.append((start,end))
    return bytes(bad)[start:end+1],full_size
with patch.object(e,'read_range',side_effect=fixture_range):
    recovered=e.probe('chb01/chb01_01.edf',retain_invalid_calibration=True)
check('probe retention integration exact ranges and full-file accounting',
      calls==[(0,255),(256,len(bad)-1)] and recovered['HTTP_range_total_bytes']==full_size and
      recovered['header_bytes_read']==len(bad) and recovered['waveform_bytes_read']==0 and
      compile_map(recovered['metadata'])['eligible'])
with patch.object(e,'read_range',side_effect=AssertionError('No network')):
    try:e.probe('chb19/chb19_01.edf',retain_invalid_calibration=True)
    except ValueError:checks.append('retention probe cannot bypass heldout guard')
    else:raise AssertionError('retention bypassed guard')
with patch.object(e,'read_range',side_effect=lambda url,a,b:(bytes(bad)[a:b+1],full_size+2)):
    try:e.probe('chb01/chb01_01.edf',retain_invalid_calibration=True)
    except ValueError:checks.append('retention probe still rejects full-file size mismatch')
    else:raise AssertionError('bad total accepted')

result=dict(status='PASS',control_groups=len(checks),checks=checks,network_requests=0,synthetic_only=True,empirical_result=False)
Path(__file__).with_name('edf_header_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
