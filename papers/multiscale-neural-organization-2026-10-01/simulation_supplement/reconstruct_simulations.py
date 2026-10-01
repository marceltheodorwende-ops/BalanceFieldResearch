"""New reconstruction from preprint equations 11-24; not the original simulate.py."""
from pathlib import Path
import csv, json, hashlib
import numpy as np

ROOT=Path(__file__).resolve().parent
L=np.array([[1.,-1.,0.],[-1.,2.,-1.],[0.,-1.,1.]])
J=np.array([[0.,1.],[1.,0.]])
C=np.ones(6)/np.sqrt(6)
D=np.tile([1.,-1.],3)/np.sqrt(6)
CASES={
 'reference':(.12,.10,[1.,1.,1.]),
 'weak_mediation':(.12,.10,[.65,.65,.65]),
 'disconnected_levels':(0.,.10,[1.,1.,1.]),
 'contrast_suppression':(.12,.32,[.92/1.14]*3),
 'middle_interface_reduced':(.12,.10,[1.,.35,1.]),
 'linear_instability':(.12,.10,[1.12]*3),
}
REPORTED=[(.9200,.189,.0014,.5727),(.5980,3.42e-5,2.54e-7,.0125),
 (.9200,.189,.0014,0.),(.9200,.189,1.31e-8,.5438),
 (.8174,.016,6.97e-5,.0613),(1.0304,1.82,.0135,2.6301)]

def matrix(kappa,eta,gains):
    R=.82*np.eye(6)-kappa*np.kron(L,np.eye(2))+eta*np.kron(np.eye(3),J)
    M=np.diag(np.sqrt(np.repeat(gains,2)))
    return M@R@M,R,M

def write_csv(path,header,rows):
    with path.open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f); w.writerow(header); w.writerows(rows)

def main():
    rows=[]; results={}; table_errors={}
    for (name,(k,e,g)),expected in zip(CASES.items(),REPORTED):
        A,R,M=matrix(k,e,g)
        x=np.eye(6)[0].copy(); trajectory=[]
        for t in range(61):
            trajectory.append([t,*x,np.linalg.norm(x),*[(x[2*j]+x[2*j+1])/np.sqrt(2) for j in range(3)]])
            x=A@x
        write_csv(ROOT/(name+'_trajectory.csv'),['step','w1','s1','w2','s2','w3','s3','norm','level1_common','level2_common','level3_common'],trajectory)
        A20=np.linalg.matrix_power(A,20)
        actual=np.array([max(abs(np.linalg.eigvalsh(A))),np.linalg.norm(A20@C),np.linalg.norm(A20@D),sum(r[6] for r in trajectory[:21])])
        # Independent reference: rounded numbers transcribed from Table 3, PDF page 9.
        d_tol={'reference':5.1e-5,'disconnected_levels':5.1e-5,'linear_instability':5.1e-5,'weak_mediation':5.1e-10,'contrast_suppression':5.1e-11,'middle_interface_reduced':5.1e-8}[name]
        tolerances=np.array([.000051,.0051 if name=='linear_instability' else .00051,d_tol,.000051])
        assert np.all(abs(actual-np.array(expected))<=tolerances),(name,actual,expected)
        rows.append([name,.82,k,e,*g,*actual])
        results[name]=dict(a=.82,kappa=k,eta=e,gains=g,spectral_radius=actual[0],C20=actual[1],D20=actual[2],G20=actual[3])
        table_errors[name]=(actual-np.array(expected)).tolist()
    write_csv(ROOT/'recomputed_summary.csv',['case','a','kappa','eta','n1','n2','n3','spectral_radius','C20','D20','G20'],rows)
    write_csv(ROOT/'table3_transcribed.csv',['case','spectral_radius','C20','D20','G20'],[[name,*v] for name,v in zip(CASES,REPORTED)])
    errors=[]
    for k in np.linspace(0,.25,11):
        for e in np.linspace(0,.35,15):
            for n in np.linspace(.5,1.3,9):
                A,_,_=matrix(k,e,[n]*3)
                exact=np.sort([n*(.82-k*l+s*e) for l in [0,1,3] for s in [-1,1]])
                errors.append(float(max(abs(np.linalg.eigvalsh(A)-exact))))
    assert max(errors)<1e-12
    assert results['disconnected_levels']['G20']==0
    assert abs(results['reference']['spectral_radius']-results['contrast_suppression']['spectral_radius'])<1e-12
    A,R,M=matrix(*CASES['reference'])
    rng=np.random.default_rng(20261001); x=np.zeros(6); z=x.copy(); clone_error=0.
    for _ in range(128):
        u=rng.normal(size=6); x=M@R@M@x+u; z=A@z+u
        clone_error=max(clone_error,float(max(abs(x-z))))
    assert clone_error<1e-12
    alt=np.diag(np.sqrt(np.repeat([.8,1.2,.7],2))); inv=np.linalg.inv(alt)
    factor_error=float(np.max(abs(alt@(inv@A@inv)@alt-A)))
    assert factor_error<1e-12
    results['verification']=dict(spectrum_cases=len(errors),max_spectrum_error=max(errors),rounded_table3_residuals=table_errors,clone_max_error=clone_error,alternative_factorization_residual=factor_error,numpy_version=np.__version__,seed=20261001,driven_input_note='Normal inputs chosen for this reconstruction; original distribution was not supplied.')
    (ROOT/'results.json').write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(results['verification'],indent=2))

if __name__=='__main__': main()
