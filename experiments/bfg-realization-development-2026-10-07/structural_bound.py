import csv,gzip,io,json
from pathlib import Path
r=Path(__file__).parent
p=list(csv.DictReader(io.StringIO(gzip.decompress((r/'results/pairs.csv.gz').read_bytes()).decode())))
lo,hi=0.,1.
for _ in range(100):
    y=(lo+hi)/2
    if 1-y-y*y-3*y**3>0: lo=y
    else: hi=y
m=(lo+hi)/2
ratio=2*m/((1+m)**2*(1+m*m))
out=dict(kind='post-development structural bound, not confirmation',max_scalar_energy_retention=ratio,maximizing_y=m,pairs_observed_retention_above_half=sum(float(x['observed_ratio'])>.5 for x in p),pairs_observed_retention_above_exact_max=sum(float(x['observed_ratio'])>ratio for x in p),pairs=len(p),fraction_above_exact_max=sum(float(x['observed_ratio'])>ratio for x in p)/len(p))
(r/'results/structural_bound.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
