# Balance Field Framework

## Mathematical amendment — 23 September 2026

The [finite repair stage](research/finite-repair-2026-09-23/README.md) supplies a corrected persistence definition, distinguishes spectral and metric projectors, and proves the real/complex formation alternatives with real-structure transport conditions. The full reconstruction law remains open; its completion contract is explicit.

## Author-supplied simulation data

The [emergence dataset and reproducible analysis](research/emergence-data-2026-09-22/README.md) contain 9,993 successful cases from the architecture paper's reported 10,000 trials. Their spectral-novelty summaries and correlation agree with the paper. The seven terminated trials and separate control streams are not included.

### Canonical reclosure and structural novelty

Research by **Marcel Theodor Wende**. The current reading entry is the pair of consolidated mathematical preprints supplied on **22 September 2026**.

## Read the current papers

| Paper | Focus |
| --- | --- |
| [Canonical Universal Reclosure Architecture](papers/canonical-2026-09-22/BFG_Canonical_Universal_Reclosure_Architecture_Preprint_2026-09-22_FINAL.pdf) | Formation, neutral resolution, persistence, reciprocal order, transport, reconstruction and the proposed universal architecture. |
| [Canonical Reclosure and Structural Novelty](papers/canonical-2026-09-22/BFG_Canonical_Reclosure_and_Structural_Novelty_Preprint_2026-09-22.pdf) | An exact finite-dimensional inheritance–novelty criterion on a neutral-compatible persistent support. |

The original PDFs are preserved byte-for-byte. [Source manifest](papers/canonical-2026-09-22/manifest.json) · [Source chronology and V3 clarification](docs/SOURCE_HISTORY.md).

## Mathematical contribution

For a finite-dimensional inherited support with self-adjoint nonnegative load `Y_P`, Hermitian formation operator `K_P`, an orthogonal persistence projector commuting with `Y`, and positive fixed weights `alpha, beta`, the two-channel polar reclosure has the exact form

```math
K_+=R^{-1}(\alpha K_P+\beta Y_PK_PY_P)R^{-1},\qquad R=(\alpha I+\beta Y_P^2)^{1/2}.
```

In a neutral-load eigenbasis this is a correlation-matrix Schur multiplier. Under these assumptions,

```math
[Y_P,K_P]=0\ \Longleftrightarrow\ K_+=K_P\ \Longleftrightarrow\ \sigma(K_+)=\sigma(K_P).
```

Noncommutation therefore gives a strict change in the formation spectrum. A successful formation gate is an additional condition. This theorem is a concrete mathematical advance over treating recursion or support reduction alone as novelty.

## Current verification

The [consolidation review](research/canonical-consolidation-2026-09-22/REVIEW.md) checks the new sources against the three BFG audit documents. A fresh bounded audit checks **512 random cases, 128 commuting controls and 128 ambient-support cases**. [Code and results](research/canonical-consolidation-2026-09-22/README.md).

The review also records the work needed to complete the architecture: the printed persistence-span definition still admits decaying directions; the general Gram-factor and recursive-transport rebuilds need explicit functions; and the two-polarity formation statement needs a real profile restriction. The new operator theorem remains useful independently of those broader obligations. Neither paper supplies empirical validation of natural systems.

## Navigate the project

- [Current claim register](docs/CLAIMS.md) and [mathematical status](docs/MATHEMATICAL_STATUS.md)
- [Next mathematical steps](docs/RESEARCH_PLAN.md)
- [Current consolidation stage](research/canonical-consolidation-2026-09-22/README.md)
- [All research stages](research/README.md), including conditional CTC models, reconstruction audits, and the exploratory RLC study
- [Source library](papers/README.md), including historical originals
- [Earlier network laboratory documentation](docs/LEGACY_LAB.md)

## Reproduce the new audit

From the repository root, with Python 3.11+ and NumPy:

```sh
python -m pip install -r requirements.txt
python research/canonical-consolidation-2026-09-22/audit.py
```

The new script checks the isolated operator theorem; it is not an implementation of the entire universal state map. Existing `bfg_lab` modules remain research models with their original stated assumptions.

## Publication and provenance

Current primary sources are author-supplied theoretical preprints. Repository reviews are AI-assisted mathematical checks, not independent peer review. Earlier stages and negative findings remain available in their dated folders and Git history. The superseded V3 nonexistence erratum has been withdrawn at the author's request; V3 is not a prerequisite file for using the consolidated sources. Original authorship and rights remain with the respective authors.
## Copyright and permissions

Copyright (c) 2026 Marcel Theodor Wende. All rights reserved for his original protected contributions throughout this repository. See [LICENSE](LICENSE) for the repository-wide rights reservation, third-party exclusions and applicable-law/GitHub exceptions. This is not an open-source license and does not revoke existing file-specific permissions.

## Experimental Emergence Studio

The [author-supplied Emergence Studio](research/emergence-studio-2026-09-23/README.md) contains Python models, examples, tests and archived results. It is preserved as a separate experimental snapshot with an intake review; its full runtime suite has not yet been independently rerun here.

## Explicit finite conditional completion

The [finite closure model](research/finite-closure-model-2026-09-23/README.md) defines and proves a reduced-state update with explicit intrinsic-Gram and unitary-recursion choices. Fifteen focused checks pass. This is a conditional mathematical completion, not a proof that the original BFG axioms uniquely force those choices or close the general unbounded case.

## Current BFG Emergence Studio

The [integrated Studio version](research/emergence-studio-integrated-2026-09-23/README.md) includes 314 original files, the adopted reduced finite closure profile, recursive-stability and exact-certificate modules, and documented results of 107 tests and nine benchmarks. The earlier Studio snapshot remains available; this import performs no new code execution.

## Latest BFG Emergence Studio — revision 3

The [current 404-file Studio version](research/emergence-studio-2026-09-23-r3/README.md) adds formation robustness, small-load contraction, stratum-transition geometry and an exploratory relational network carrier. Its documented results include 142 passed tests. Original files and results are preserved unchanged; this import does not rerun tests. Earlier versions remain available.
