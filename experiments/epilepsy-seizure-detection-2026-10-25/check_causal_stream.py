"""Independent causal/coverage controls, synthetic voltages only."""
import json
from pathlib import Path
import numpy as np
from causal_stream import RecordStream

checks=[]
def check(n,x):
    if not x:raise AssertionError(n)
    checks.append(n)

def process(x,h,parts,valid=None):
    s=RecordStream('synthetic',len(x),256,x.shape[1],h);out=[];ready=[];offset=0
    for size in parts:
        r=s.feed(offset,x[offset:offset+size],None if valid is None else valid[offset:offset+size])
        assert np.array_equal(r['availability_sample_end'],np.arange(offset+1,offset+size+1))
        offset+=size;out.append(r['values']);ready.append(r['ready'])
    return np.concatenate(out),np.concatenate(ready),s.finish()

x=np.array([[1.],[2.],[3.],[4.]])
y,ready,cov=process(x,[.5,.5],[1,3])
check('hand causal convolution and no zero padding',np.isnan(y[0,0]) and np.array_equal(y[1:,0],[1.5,2.5,3.5]))
check('all observed samples retained in duration',cov['observed_samples']==4 and cov['warmup_samples']==1 and cov['ready_samples']==3 and cov['observed_seconds']=='1/64')
timing=RecordStream('timing',2,4,1,[1.]).feed(0,[[1.],[2.]])
check('availability timestamps use sample ends',np.array_equal(timing['availability_sample_end'],[1,2]) and timing['sampling_hz']=='4')
rng=np.random.default_rng(20261025);oracle_cases=0;max_error=0.
for length in (1,2,5):
    h=rng.uniform(-1,1,length)
    for _ in range(30):
        x=rng.normal(size=(40,3));valid=rng.random(40)>.15
        y,ready,cov=process(x,h,[40],valid)
        oracle=np.full_like(x,np.nan);expected=np.zeros(40,dtype=bool)
        # Independent direct-window oracle; no stateful streaming implementation.
        for n in range(length-1,40):
            if valid[n-length+1:n+1].all():
                expected[n]=True
                oracle[n]=sum(h[j]*x[n-j] for j in range(length))
        assert np.array_equal(ready,expected)
        np.testing.assert_allclose(y,oracle,atol=1e-12,rtol=1e-12,equal_nan=True)
        if ready.any():max_error=max(max_error,float(np.max(abs(y[ready]-oracle[ready]))))
        for parts in ([1]*40,[3,7,11,19]):
            yy,rr,cc=process(x,h,parts,valid)
            np.testing.assert_array_equal(yy,y);assert np.array_equal(rr,ready) and cc==cov
        altered=x.copy();altered[20:]+=1000
        yy,rr,_=process(altered,h,[40],valid)
        np.testing.assert_array_equal(yy[:20],y[:20]);assert np.array_equal(rr[:20],ready[:20])
        assert cov['ready_samples']+cov['invalid_samples']+cov['warmup_samples']==40
        oracle_cases+=1
checks.append('90 independent window-oracle/chunk/future/coverage cases')
check('oracle numerical discrepancy bounded',max_error<1e-12)
x=np.array([[1.],[np.nan],[2.],[3.]])
y,ready,cov=process(x,[.5,.5],[4])
check('nonfinite input resets and preserves invalid duration',np.array_equal(ready,[False,False,False,True]) and cov['invalid_samples']==1 and cov['warmup_samples']==2)
s=RecordStream('A',2,256,1,[.5,.5]);s.feed(0,[[1.],[2.]]);s.finish()
t=RecordStream('B',2,256,1,[.5,.5]);z=t.feed(0,[[100.],[200.]])
check('fresh file has fresh warmup state',not z['ready'][0] and z['values'][1,0]==150)
for start,values in ((2,[[3.]]),(0,[[3.]])):
    try:s.feed(start,values)
    except ValueError:pass
    else:raise AssertionError('closed record reused')
checks.append('closed recording cannot concatenate another file')
s=RecordStream('A',4,256,1,[1.]);s.feed(0,[[1.]])
for start,values in ((2,[[2.]]),(0,[[2.]]),(1,[[2.],[3.],[4.],[5.]]),(1,[[1.,2.]])):
    try:s.feed(start,values)
    except ValueError:pass
    else:raise AssertionError('bad chunk accepted')
check('4 gap/overlap/overrun/channel failures are state preserving',s.seen==1)
try:s.finish()
except ValueError:checks.append('truncated recording fails explicitly')
else:raise AssertionError('truncation accepted')
for h in ([],[float('nan')],[float('inf')],[[1.]]):
    try:RecordStream('A',2,256,1,h)
    except ValueError:pass
    else:raise AssertionError('invalid FIR accepted')
checks.append('4 invalid coefficient definitions rejected')
h=np.array([1.]);s=RecordStream('A',1,256,1,h);h[0]=2.
check('caller cannot mutate supplied coefficient array',s.feed(0,[[3.]])['values'][0,0]==3)
x=np.zeros((3,1));h=[.25,-.5,.25];noise=np.array([[.01],[-.01],[.01]])
y,r,_=process(x,h,[3]);yn,rn,_=process(x+noise,h,[3])
check('conditional error bound L1(h)*delta attained',abs(abs(yn[2,0]-y[2,0])-sum(abs(v) for v in h)*.01)<1e-15)
s=RecordStream('overflow',1,256,1,[2.])
try:s.feed(0,[[np.finfo(float).max]])
except ValueError:pass
else:raise AssertionError('overflow accepted')
check('overflow poisons record before continuation',s.failed)
try:RecordStream('complex',1,256,1,np.array([1+1j]))
except ValueError:checks.append('complex coefficients not silently truncated')
else:raise AssertionError('complex coefficient accepted')
result=dict(status='PASS',control_groups=len(checks),checks=checks,independent_oracle_cases=oracle_cases,
    max_oracle_error=max_error,no_waveform_or_annotation_access=True,scientific_filter_selected=False,
    BFG_or_physiological_law=False,empirical_result=False,confirmatory_freeze=False)
Path(__file__).with_name('causal_stream_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
