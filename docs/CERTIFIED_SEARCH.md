# Bounded certified family search

`refine_family` in `bfg_lab.certified_search` extends the existing exact-rational
classifier without changing its historical results. Its measurement assumptions
and trajectory enclosures are those in [CERTIFIED_FAMILY.md](CERTIFIED_FAMILY.md).

```sh
python -m bfg_lab.certified_search --input examples/certified_search.json
python -m unittest discover -s tests -p test_certified_search.py -v
```

The API accepts the same arguments as `assess_family`, plus `max_boxes=256` and
`max_depth=20`. The CLI writes `results/certified_search.json` by default.
The example has an interior witness missed by the original midpoint candidate.

## Coverage argument

Represent every independent upper-triangle edge and every initial component by
a closed rational interval. Choose the widest coordinate (ties: upper-triangle
row order, then initial component order) and bisect it exactly. The two closed
children cover their parent, sharing only the split boundary. Mirror edge bounds
to maintain symmetry. Traverse breadth first. Width ordering is an efficiency
heuristic, sensitive to coordinate units; it has no role in certificate validity.

At each box, use its initial midpoint and the largest component half-width as
the uniform initial error passed to `assess_family`. This can enlarge an
anisotropic initial box but cannot omit any of its states. Consequently a leaf
exclusion certificate excludes the entire leaf. The tested midpoint itself is
inside the original box, so a verified witness is valid for the original family.
The same weights and initial state must satisfy ALL observation times.

By induction on bisections, excluding every terminal leaf excludes the original
family. Any pending or unresolved leaf prevents that conclusion. Results include
binary leaf paths and exact exclusion bounds; replay the deterministic splits
from the original input to reconstruct each leaf. Preserve the input alongside
the output. Witness results provide the actual rational parameters and bounds.

## Limits and validation

Budget exhaustion, a depth limit, an unsplittable box, or an insufficient series
budget leaves the answer `unresolved`. The method does not automatically increase
the series budget. Exact noiseless equality, parameter ambiguity, or high
dimension can still prevent resolution. It is not a complete decision algorithm.
Larger budgets may cost substantially more rational arithmetic and memory.

Seven regression tests cover an interior weight witness, an initial-state
witness, incompatible observations at different times requiring whole-family
exclusion, box/depth/series limits, malformed budgets, and a healthy parameter
grid including boundary points. The exclusion test also checks that certified
leaf paths cover total dyadic volume one. The published suite passes 70 tests
(2026-09-15). An unrelated local observation prototype is not in this publication
or this test count.

These are software and synthetic mathematical checks, not empirical evidence
for BFG, a new theorem of physics, or identification of a particular fault.
Original papers and prior negative results remain unchanged.
