"""One-record causal execution primitive; no filter design or BFG dynamics."""
from collections import deque
from fractions import Fraction
import numpy as np

class RecordStream:
    def __init__(self,record_id,sample_count,sampling_hz,channels,coefficients):
        if not isinstance(record_id,str) or not record_id:
            raise ValueError('Named recording required')
        if any(isinstance(v,bool) or not isinstance(v,int) or v<=0 for v in (sample_count,channels)):
            raise ValueError('Positive integer count/channel dimensions required')
        if isinstance(sampling_hz,bool):raise ValueError('Invalid sampling rate')
        self.fs=Fraction(sampling_hz)
        if self.fs<=0:raise ValueError('Positive sampling rate required')
        if np.iscomplexobj(coefficients):raise ValueError('Real FIR coefficients required')
        self.h=np.array(coefficients,dtype=float,copy=True)
        if self.h.ndim!=1 or not len(self.h) or not np.isfinite(self.h).all() or not np.isfinite(np.abs(self.h).sum()):
            raise ValueError('Finite nonempty fixed FIR required')
        self.h.setflags(write=False)
        self.record_id=record_id;self.total=sample_count;self.channels=channels
        self.history=deque(maxlen=len(self.h));self.seen=0;self.ready_count=0;self.invalid_count=0
        self.finished=False;self.failed=False

    def feed(self,start_index,values,valid=None):
        if self.finished or self.failed:raise ValueError('Recording closed or failed')
        if isinstance(start_index,bool) or not isinstance(start_index,int) or start_index!=self.seen:
            raise ValueError('Gap/overlap/duplicate chunk; no implicit repair')
        if np.iscomplexobj(values):raise ValueError('Real voltage samples required')
        x=np.asarray(values,dtype=float)
        if x.ndim!=2 or x.shape[1]!=self.channels or self.seen+len(x)>self.total:
            raise ValueError('Channel/count/record-boundary mismatch')
        if valid is None:mask=np.ones(len(x),dtype=bool)
        else:
            mask=np.asarray(valid)
            if mask.dtype!=np.bool_ or mask.shape!=(len(x),):raise ValueError('Explicit boolean QC mask required')
        mask=mask & np.isfinite(x).all(axis=1)
        out=np.full(x.shape,np.nan);ready=np.zeros(len(x),dtype=bool)
        indices=np.arange(self.seen,self.seen+len(x),dtype=np.int64)
        for i,row in enumerate(x):
            if not mask[i]:
                self.history.clear();self.invalid_count+=1
            else:
                self.history.append(row.copy())
                if len(self.history)==len(self.h):
                    try:
                        with np.errstate(over='raise',invalid='raise'):
                            out[i]=self.h@np.array(list(self.history)[::-1])
                    except FloatingPointError as error:
                        self.failed=True;raise ValueError('Numerical overflow; record failed') from error
                    ready[i]=True;self.ready_count+=1
            self.seen+=1
        return dict(values=out,ready=ready,invalid=~mask,sample_indices=indices,
                    availability_sample_end=indices+1,sampling_hz=str(self.fs))

    def coverage(self):
        return dict(record_id=self.record_id,observed_samples=self.seen,declared_samples=self.total,
            ready_samples=self.ready_count,invalid_samples=self.invalid_count,
            warmup_samples=self.seen-self.ready_count-self.invalid_count,
            observed_seconds=str(Fraction(self.seen)/self.fs),declared_seconds=str(Fraction(self.total)/self.fs),
            complete=self.seen==self.total and not self.failed,failed=self.failed)

    def finish(self):
        if self.failed or self.seen!=self.total:raise ValueError('Failed or truncated record; no silent exclusion')
        self.finished=True
        return self.coverage()
