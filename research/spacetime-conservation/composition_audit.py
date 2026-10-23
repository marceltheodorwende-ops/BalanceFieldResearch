"""Exact fixed-spectral-frame composition checked against pinned BFG update."""
import json
from pathlib import Path
import numpy as np
import audit
import pair_audit

TOL=1e-10

def run():
    update=audit.load_update(); rng=np.random.default_rng(20261104)
    maxima={key:0. for key in ('source','words','population','stochastic','symmetry','gauge')}
    rows=[]; calls=0
    for n in (3,4,5,6):
        y=np.eye(n)/4+(np.eye(n,k=1)+np.eye(n,k=-1))/40
        f=np.diag(np.arange(1,n+1,dtype=float)); w=np.eye(n)/n
        _,u=np.linalg.eigh(y)
        point=np.zeros((n,n)); point[0,0]=1
        z=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n))
        generic=z@z.conj().T; generic/=np.trace(generic)
        initial=[point.copy(),generic.copy()]; current=[point,generic]
        htotal=np.ones((n,n)); words=[np.eye(n)]; markov=np.eye(n)
        for event in range(3):
            a=audit.aligned(current[0],f,y)
            ops=[a['tc'],a['tb']]
            spectral=[u.conj().T@t@u for t in ops]
            h=sum(np.outer(np.diag(t),np.diag(t).conj()) for t in spectral).real
            htotal*=h
            words=[t@l for t in ops for l in words]
            one=sum(abs(t)**2 for t in ops); markov=one@markov
            effective=np.empty((n,n))
            for i in range(n):
                for j in range(n):
                    v=u[i,:]*u[j,:].conj()
                    effective[i,j]=(v@htotal@v.conj()).real
            pw=sum(abs(l)**2 for l in words)
            maxima['words']=max(maxima['words'],float(np.linalg.norm(effective-pw)))
            maxima['stochastic']=max(maxima['stochastic'],float(np.linalg.norm(effective.sum(0)-1)),float(np.linalg.norm(effective.sum(1)-1)))
            maxima['symmetry']=max(maxima['symmetry'],float(np.linalg.norm(effective-effective.T)))
            assert np.linalg.eigvalsh(htotal)[0]>=-TOL and effective.min()>=-TOL
            outputs=[]
            for index,k in enumerate(current):
                out=pair_audit.source_aligned(update,k,f,w,y); calls+=1
                predicted=u@(htotal*(u.conj().T@initial[index]@u))@u.conj().T
                direct=sum(l@initial[index]@l.conj().T for l in words)
                maxima['source']=max(maxima['source'],float(np.linalg.norm(out['k']-predicted)),float(np.linalg.norm(out['k']-direct)))
                outputs.append(out)
            maxima['population']=max(maxima['population'],float(np.linalg.norm(np.diag(outputs[0]['k']).real-effective[:,0])))
            if event==0:
                g=audit.complex_unitary(rng,n); conj=lambda x:g@x@g.conj().T
                gout=pair_audit.source_aligned(update,conj(current[1]),conj(f),conj(w),conj(y)); calls+=1
                maxima['gauge']=max(maxima['gauge'],float(np.linalg.norm(gout['k']-conj(outputs[1]['k']))))
            rows.append(dict(n=n,event=event+1,kraus_words=len(words),minimum_gram_eigenvalue=float(np.linalg.eigvalsh(htotal)[0]),markov_matrix_difference=float(np.linalg.norm(effective-markov)),endpoint_population=float(effective[-1,0])))
            current=[out['k'] for out in outputs]
            f,w,y=outputs[0]['f'],outputs[0]['w'],outputs[0]['y']
    assert calls==28 and max(maxima.values())<TOL
    return dict(status='PASS; finite-horizon internal composition, physical transport OPEN',source_blob=audit.EXPECTED_SOURCE_BLOB,seed=20261104,tolerance=TOL,full_source_calls=calls,maximum_residuals=maxima,cases=rows)

if __name__=='__main__':
    result=run()
    Path(__file__).with_name('composition_results.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
