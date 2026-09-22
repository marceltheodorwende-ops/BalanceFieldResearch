# Author-supplied emergence data — 22 September 2026

This stage preserves Marcel Theodor Wende's supplied [CSV](bfg_emergence_mc.csv) unchanged and independently recomputes its scalar summaries. It follows the BFG audit distinction between source evidence, numerical checks and mathematical claims.

## Source reconciliation

The file contains **9,993 data rows**, plus a header, with nine numeric columns. This matches the successful subset of the **10,000 emergence trials** reported in Section 14 / Table 6 of the [canonical architecture paper](../../papers/canonical-2026-09-22/BFG_Canonical_Universal_Reclosure_Architecture_Preprint_2026-09-22_FINAL.pdf). The seven reported terminated trials are absent; their behavior cannot be checked from this file.

| Quantity | Recomputed | Paper |
| --- | ---: | ---: |
| Successful-case rows | 9,993 | 9,993 |
| Minimum spectral novelty | 0.0361596834703 | 0.0362 |
| Median spectral novelty | 0.269771011679 | 0.2698 |
| Maximum spectral novelty | 0.824761550954 | 0.8248 |
| Pearson correlation: spectral_novel, commP | 0.781376571853 | approximately 0.781 |

All reported rounded summaries above agree. All rows are finite and numerically distinct. Every stored lamplus is negative and gapplus positive. The largest weight-sum residual is 2.22e-16; ampplus equals sqrt(max(0,-lamplus)) at the parsed floating-point precision.

## Columns and interpretation

The CSV supplies names but no separate data dictionary. The following distinguishes observed identities from interpretation; it does not assign undocumented normalizations.

| Column | Interpretation / evidence |
| --- | --- |
| spectral_novel | Spectral novelty diagnostic; its distribution matches the paper's reported witness. Its underlying spectra are not supplied. |
| commP | Commutator diagnostic identified by the matching reported correlation; raw matrices and normalization cannot be reconstructed. |
| commY | Additional commutator diagnostic; exact operator pair and normalization remain undocumented in the CSV. |
| ratio | Stored ratio diagnostic; its exact numerator and denominator are not supplied. |
| wk, wu | Positive complementary weights: their sum is one to rounding precision. Derivation from original loads cannot be checked. |
| lamplus | Consistent with a next-step minimum eigenvalue; all entries are negative. |
| gapplus | Consistent with a next-step spectral gap; all entries are positive. |
| ampplus | Exactly consistent with the stored formation-amplitude identity. |

## Scope of verification

This dataset makes the successful emergence summary inspectable. It does not contain the architecture paper's commuting controls or separate consistency stream, nor the novelty paper's 20,000-case stream and its two 5,000-case control streams. Accordingly, it is not a complete numerical archive for both papers.

Trial identifiers, sampled matrices, dimensions and original simulation code are absent. The analysis verifies stored scalar diagnostics and paper-summary agreement, not regeneration of the ensemble, the full operator formation gate or a complete universal iteration. Seven missing terminated cases are paper-reported, not newly observed here. These simulations are not empirical measurements of nature. Existing negative findings in the [mathematical review](../canonical-consolidation-2026-09-22/REVIEW.md) remain applicable.

## Reproduce

From the repository root, using Python and NumPy:

```sh
python research/emergence-data-2026-09-22/analyze.py
```

This writes [RESULTS.json](RESULTS.json), including every column's minimum, median and maximum. [SOURCE.json](SOURCE.json) records the immutable source checksum. No source CSV rows are altered, filtered or imputed.
