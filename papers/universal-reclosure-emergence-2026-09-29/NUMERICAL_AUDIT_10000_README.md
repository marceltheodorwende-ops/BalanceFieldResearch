# Adapted 10,000-case numerical audit of the 29 September BFG preprint

**Run date:** 29 September 2026. **Source:** [numerical_audit_10000.py](numerical_audit_10000.py). **Frozen output:** [NUMERICAL_AUDIT_10000_RESULTS.json](NUMERICAL_AUDIT_10000_RESULTS.json). NumPy 2.3.5, Python 3.12.14; PCG64 seed `20260929`, complex and real dimensions 2–8. Absolute numerical tolerance is `1e-9`, fixed in the script before the run.

This adapts the algebraic **classes** of the earlier [10,000-instance canonical architecture audit](../canonical-2026-09-22/BFG_Canonical_Universal_Reclosure_Architecture_Preprint_2026-09-22_FINAL.pdf), Section 14 and Appendix C, to the equations of the [new universal reclosure and emergence preprint](BFG_Universal_Reclosure_and_Emergence_Preprint_2026-09-29.pdf). The historical original generator, its random matrices, and its seven terminated cases are unavailable; this is a **fresh ensemble**, not a replay of its 9,993/7 outcome. The [earlier supplied CSV](../../research/emergence-data-2026-09-22/README.md) only stores the 9,993 successful scalar rows.

| Audit class | Fresh trials | Independent observable and outcome |
| --- | ---: | --- |
| Neutral load, resolvent/contrast, graph projector, reciprocal weights, compact packet, polar support, positivity and non-expansion | 10,000 | All finite consistency residuals below `1e-9`; largest packet gain `0.631352 < 1/√2`. The smallest compressed positive eigenvalue was `−2.56e-14`, consistent with floating-point roundoff. |
| Level-0 formed branch, Hesse positivity, exact quartic remainder, whitening and direct neutral minimization versus Gram resolvent | 10,000 | All checks passed; maximum difference of direct and Gram minima `7.11e-14`. This tests Appendix C's **declared tangent-sector interface**. |
| Schur-factor defect and independent second spectral moment for the neutral-compatible persistent stratum of Theorem 1 | 10,000 | All 10,000 random noncommuting cases had positive internal novelty; maximum moment-identity residual `1.47e-14`. |
| Formation gate on the Schur stratum | 10,000 | 9,861 passed; 139 terminated under the sampled inputs. These counts are diagnostic properties of this ensemble. |
| Commuting inheritance and scalar-load controls | 1,000 and 100 | All returned inherited formation up to roundoff. |

The complete results file records every maximum residual, lower eigenvalue and gate count. To reproduce from this directory:

```sh
python3 numerical_audit_10000.py > fresh_audit.json
diff -u NUMERICAL_AUDIT_10000_RESULTS.json fresh_audit.json
sha256sum -c SHA256SUMS.txt
```

**Interpretation.** These are finite-dimensional consistency tests of equations, not an independent proof of the theorems. The Schur-stratum update used for Theorem 1 is not a numerical execution of the complete five-object canonical successor with endogenous persistence reconstruction. A spectral change establishes internal formation novelty under the stated hypotheses; it does not by itself meet the paper's independent-source, higher-channel, generative-removal, restoration and rival-exclusion criterion for irreducible emergence. The role and metric of a physical neutral mediator are not inferred from 10,000 trials. Existing 1,000-realization synthetic removal tests are separately archived with the paper, and their matched-memory direct rival ties.
