"""Exact scalar controls using the normalized duplicated e1 direction."""
from fractions import Fraction as Q
import json

# u=(e1,e1)/sqrt(2); each duplicated contribution is divided by two.
rows=[]
for a in (Q(0), Q(1), Q(2), Q(-3,2)):
    compressed_c = (Q(1)+Q(1))/2
    tangent = Q(0)
    full_gram = (a*a+a*a)/2
    normal_gram = a*a
    assert compressed_c == 1
    assert full_gram == tangent*tangent+normal_gram
    rows.append(dict(a=str(a), compressed_c=str(compressed_c),
                     tangent=str(tangent), full_gram=str(full_gram),
                     defect=str(normal_gram)))
assert len({r['compressed_c'] for r in rows}) == 1
assert len({r['defect'] for r in rows}) > 1
weighted_full=Q(1)+Q(1,2)+Q(1,2)+Q(1)
weighted_separate=Q(1)+Q(1)
assert weighted_full==3 and weighted_separate==2
print(json.dumps(dict(exact_controls='passed', family=rows,
                     weighted_full=str(weighted_full),
                     weighted_separate=str(weighted_separate)), indent=2))
