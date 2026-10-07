"""Development-only rounding stress; fixed annotations and scale, not sensor model."""
import csv,json,random,statistics
from pathlib import Path
from explore import LENGTHS,allowed,pairs,scalar,loss,write_csv

root=Path(__file__).parent
s=json.loads((root/'results/summary.json').read_text())['scale_J_per_kg']
records=[]
for seed in range(30):
    rng=random.Random(20261007+seed)
    for path in sorted((root/'data').glob('*.csv')):
        if not allowed(path.name): raise ValueError('holdout forbidden')
        rows=list(csv.DictReader(path.open()))
        for row in rows:
            row['angle']=str(float(row['angle'])+rng.uniform(-.0005,.0005))
        ps,rejected,_=pairs(rows,LENGTHS[int(path.name[3])-1])
        def predict(p):
            y=scalar(p['E']/s)
            return None if y is None else s*y
        error,coverage=loss(ps,predict)
        records.append(dict(seed=seed,recording=path.name,pairs=len(ps),rejected_pairs=rejected,bfg_error=error,coverage=coverage,persistence_error=loss(ps,lambda p:p['E'])[0]))
write_csv(root/'results/rounding_stress.csv',records)
means=[statistics.mean(r['bfg_error'] for r in records if r['seed']==seed) for seed in range(30)]
result=dict(kind='exploratory uniform half-rounding-unit perturbations; not confidence intervals',seeds=30,mean_record_bfg_error_range=[min(means),max(means)],annotations_fixed=True,scale_fixed=True,holdout_accessed=False)
(root/'results/rounding_stress.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
