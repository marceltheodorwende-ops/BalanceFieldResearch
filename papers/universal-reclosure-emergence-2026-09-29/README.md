# Universal BFG Reclosure and the Conditions for Irreducible Emergence

Preprint intake: 29 September 2026. Author: **Marcel Theodor Wende**, BalanceFeld Gleichung (BFG), Independent Researcher. ORCID: 0009-0007-4028-2208.

- [Read the revised ten-page preprint (PDF)](BFG_Universal_Reclosure_and_Emergence_Preprint_2026-09-29.pdf)
- [Download the editable preprint (DOCX)](BFG_Universal_Reclosure_and_Emergence_Preprint_2026-09-29.docx)
- [Run the exploratory synthetic pilot](bfg_relational_ablation_pilot.py) and [inspect its frozen JSON output](BFG_relational_ablation_results_2026-09-29.json)
- [Read the constructive test protocol](CONSTRUCTIVE_TEST_PROTOCOL.md), [run the constructive witness](bfg_constructive_emergence_witness.py), and [inspect its frozen results](BFG_constructive_emergence_results_2026-09-29.json)
- [Verify file hashes](SHA256SUMS.txt)

## Exact claim and proof boundary

The preprint combines the generator-level BFG closure grammar with the finite five-object reclosure candidate. It restates and proves, on the declared neutral-compatible persistent stratum, the exact inheritance–novelty identity: `[Y_P,K_P]=0` if and only if `K_+=K_P`; noncommutation produces a strictly changed second spectral moment. It also proves that invertible recodings of a hidden mediator generate identical observed paths under corresponding initial states and inputs. An exact dynamical clone therefore cannot be a rival that the original model must strictly outperform.

The conditional criterion for *irreducible higher closure* additionally requires surviving source closures, a separately specified higher channel, a generating-relation removal and restoration, and discrimination against mechanistically different rivals under fixed rules. **The paper does not prove that every admissible BFG successor is emergent or that a natural carrier satisfies these requirements.** For `Y_P=λI`, the displayed finite formation step has `K_+=K_P`; even strict internal novelty is not automatic. The earlier qualitative Level-0 statements do not uniquely entail the later exact quadratic neutral completion.

The synthetic pilot shows a mediator-versus-removal effect in the constructed dynamics. Its direct-dyad control performs better on the chosen recovery endpoint, and its exact clone reproduces all trajectories. The pilot is not a run of the complete canonical five-object BFG operator and provides no empirical confirmation of universal BFG emergence.

The corrected preprint adds a separate, deliberately constructed two-stage synthetic witness. Its source, removal, and restoration gates pass in 1,000 seeded realizations. A direct source-history control with **matched effective memory** reproduces the full, removed, and restored paths (maximum difference `6.661e-16`) and passes the mixed contrast and temporal impulse signature. The one-pole direct baseline fails the temporal signature because it lacks that memory; it is a diagnostic, not a decisive rival. Thus specific mediation is **not established** by this synthetic example. The correction supersedes the initial restricted-rival pass assertion, retained in the repository's version history. Neither synthetic test derives the generator from Level 0, executes the full finite BFG map, or validates natural emergence.

## Reproduction

With Python and NumPy installed, run from this directory:

```sh
python bfg_relational_ablation_pilot.py > fresh_results.json
diff -u BFG_relational_ablation_results_2026-09-29.json fresh_results.json
python bfg_constructive_emergence_witness.py > fresh_constructive_results.json
diff -u BFG_constructive_emergence_results_2026-09-29.json fresh_constructive_results.json
sha256sum -c SHA256SUMS.txt
```

The pilot uses NumPy PCG64 with seed `20260929`, 1,000 synthetic realizations of 240 steps, and a fixed perturbation at step 120. Its reported resampling intervals are exploratory. The mathematical theorems do not depend on this simulation. Checksums establish byte identity, not independent experimental validation.

## Relationship to earlier sources

This is a new dated synthesis following the [27 September Universal Emergent Closure intake](../universal-emergent-closure-2026-09-27/README.md), the [22 September canonical papers](../canonical-2026-09-22/README.md), and the [26 September proof-chain audit](../../research/proof-chain-audit-2026-09-26/README.md). Earlier source files are preserved. The repository [LICENSE](../../LICENSE) and the original paper rights remain in force; this intake adds no new license grant.
