# BFG Recursive Stability Audit

Audit: **PASS**

This is a numerical audit of the hypotheses of the finite-dimensional recursive stability theorem. It is not the theorem itself.

Development/carrier operators checked: `1375`

Spectral criterion satisfied: `1375/1375`

| Carrier | Operators | Pass fraction | Max rho | Min stable gap |
|---|---:|---:|---:|---:|
| annual-sunspots | 297 | 1.000000 | 1 | 0.24 |
| mauna-loa-co2 | 370 | 1.000000 | 1 | 0.24 |
| enso-pacific-sst | 708 | 1.000000 | 1 | 0.24 |

Control behavior:

- semisimple unit-circle control accepted: `True`
- unit-circle Jordan block rejected: `True`
- supercritical eigenvalue rejected: `True`
- small outward unit-circle perturbation rejected: `True`
- tangential unit-circle perturbation remains admissible: `True`

Interpretation guard: a PASS means the current finite-dimensional operators satisfy the theorem's numerical spectral hypotheses. It does not prove every possible BFG carrier or an infinite-dimensional extension.
