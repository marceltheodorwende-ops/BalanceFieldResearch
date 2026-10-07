import gzip
from pathlib import Path
r=Path(__file__).parent/'results'
p=r/'pairs.csv'
(r/'pairs.csv.gz').write_bytes(gzip.compress(p.read_bytes(),mtime=0))
p.unlink()
