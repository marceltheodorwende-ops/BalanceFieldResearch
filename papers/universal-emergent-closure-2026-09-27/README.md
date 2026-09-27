# BalanceFeld-Gleichung: Universal Emergent Closure

Publication intake: 27 September 2026. Author: Marcel Theodor Wende.

- **[Read the authoritative FINAL paper (PDF)](BalanceFeld_Gleichung_Universal_Emergent_Closure_Preprint_FINAL.pdf)**
- **[Download the complete FINAL reproducibility package (ZIP)](BalanceFeld_Gleichung_Preprint_Reproducibility_FINAL.zip)**
- [Numerical script](BFG_numerical_reproducibility.py), [frozen results](BFG_numerical_results_frozen.txt), and [original environment record](BFG_numerical_environment.json)
- [Package SHA-256 manifest](BFG_RELEASE_SHA256.json) and [intake checksums, including the ZIP](UPLOAD_SHA256.json)

## Scope and interpretation

This exploratory preprint develops a proposed universal closure grammar and illustrates it with synthetic numerical examples. Reproduction of those examples does not establish empirical universality or strong BFG irreducibility. In particular, the current circular-shift comparison produces 3,984/4,000 aligned detections (0.996) and 3,344/4,000 null detections (0.836); the endpoint has low specificity. Witness removal in the evaluation is not an intervention in the generating dynamics.

This dated source supplements the [22 September canonical papers](../canonical-2026-09-22/README.md). It does not by itself close the mathematical obligations documented in the [26 September proof-chain audit](../../research/proof-chain-audit-2026-09-26/README.md).

## Version and provenance

The FINAL PDF is authoritative for this intake. Its historical shuffle result is corrected to 971/3,000 (0.3236667), consistent with the script and frozen log.

The included [RELEASE DOCX](BalanceFeld_Gleichung_Universal_Emergent_Closure_Preprint_RELEASE.docx) is an earlier editable source retained unchanged for provenance. It still contains 970/3,000 and 0.3233 and must not be used to regenerate the FINAL PDF without these corrections. See [README_FINAL.txt](README_FINAL.txt).

The complete ZIP and its seven extracted members are preserved byte-for-byte. The numerical script, frozen results, and environment record were not changed during packaging. The inner manifest covers every other extracted member; the intake manifest also covers the ZIP and this overview. Checksums establish file identity, not independent evidence of a historical creation date.

## Reproduction and audit limits

With Python and NumPy available, run from this directory:

```sh
python BFG_numerical_reproducibility.py
```

The supplied environment record specifies Python 3.13.5 and NumPy 2.3.5. The local audit ran the unchanged script successfully with Python 3.12.14 and NumPy 2.3.5. Both historical and current detection counts reproduced exactly. T1, T4 and T7 showed small floating-point differences; byte-identical output across environments is not claimed. The script is a numerical demonstrator, not an assertion-based verification of every manuscript claim or a complete figure-generation pipeline.

The FINAL PDF contains 24 pages and all eleven figures. Visual checking used rendered page overviews; it is not a character-by-character print-production certification.

## Rights

The repository [LICENSE](../../LICENSE) and any notices in the original documents apply. This intake adds no new license grant and changes no authorship credits.
