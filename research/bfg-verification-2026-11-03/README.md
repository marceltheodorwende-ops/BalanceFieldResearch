# BFG verification and RC feasibility — 3 November 2026

Research stage for **The Balance Field Gleichung: Finite Dynamics and Physical Correspondence in RC Models**, DOI [10.5281/zenodo.23897937](https://doi.org/10.5281/zenodo.23897937). [Published paper](../../papers/finite-dynamics-rc-models-2026-11-02/README.md).

## Results of the first milestone

- An indexed register of 48 numbered statements, with original statement text, available adjacent proofs, labels and PDF pages. Seven central dependencies received a focused analytic review; the remaining rows are explicitly pending detailed adversarial review. Definitions and limitations are indexed but are not treated as positive theorems.
- A written scalar proof gives the stronger scalar-only bound `y_k < 2^(-1-2^(k-1))` for k>=1 and 0<y0<1. Five symbolic identities and 816 exact rational steps passed. No priority claim or proof-assistant certificate is made.
- The published finite-event control implementation was freshly replayed: 120 random cases, 40 high-precision cases and nine rational cases passed. This is a replay of existing code, not an independent reimplementation.
- A new synthetic three-node RC pilot explores component mismatch and finite measurement resolution in 1,000 tolerance cases. Its classical null and designed BFG clock are observationally identical in the ideal common mode, so this pilot cannot independently confirm a BFG natural law.
- A prospective protocol records hardware-readiness gates, finite event resolution and the inability of the assumed millivolt detector to resolve the predicted nanovolt thermal scale.
- Proof-assistant verification and actual hardware work remain incomplete. No laboratory data are included.

## Files

| File | Purpose |
|---|---|
| [claims.json](claims.json), [claims.csv](claims.csv) | Indexed claims and review status |
| [PROOF_AUDIT.md](PROOF_AUDIT.md) | Central dependency audit and unresolved rank issues |
| [SCALAR_PROOF.md](SCALAR_PROOF.md) | Analytic scalar proof, assumptions and boundary controls |
| [scalar_controls.py](scalar_controls.py), [scalar_results.json](scalar_results.json) | Exact symbolic and rational checks |
| [baseline/](baseline/) | Preserved published implementation and fresh execution results |
| [rc_pilot.py](rc_pilot.py), [rc_pilot_results.json](rc_pilot_results.json) | Synthetic feasibility study |
| [synthetic_fixed_time_trace.csv](synthetic_fixed_time_trace.csv) | Explicitly synthetic acquisition trace |
| [EXPERIMENT_PROTOCOL.md](EXPERIMENT_PROTOCOL.md) | Prospective protocol and discrimination boundary |
| [FORMALIZATION_PLAN.md](FORMALIZATION_PLAN.md) | Formal proof acceptance criteria; not completed |
| [SOURCE.json](SOURCE.json), [reference_main.tex](reference_main.tex) | Frozen source reference and hashes |

## Reproduce

Use Python 3.12, NumPy 2.5.4, SymPy 1.14.0 and mpmath 1.3.0. Matplotlib 3.11.2 is also needed to import the preserved baseline script. Run from this folder:

```sh
python scalar_controls.py
python rc_pilot.py
python -c "import runpy; m=runpy.run_path('baseline/extended_controls.py'); m['run']()"
```

The last command intentionally replays checks without regenerating manuscript figures. Exact rational iteration can be slower than floating point because numerator and denominator sizes grow rapidly. Output paths are relative to each script, not the current working directory.

## Status and next steps

### Follow-up: foundation-to-event derivation audit

[Open the derivation audit](foundation_audit/README.md) and its [status ledger](foundation_audit/DERIVATION_STATUS.md). Six historical text extractions, including the April 2025 sources, were traced separately from the November event definitions. An exact, parameter-free successor witness shows nonuniqueness relative to an explicitly listed structural packet: the same input yields loads 8/45 and 8/53. The stronger exact Gram identification excludes the witness, so the result does not refute the defined event. Source-local checks also expose the limits of a monotone-descent balance argument and the telescoping process-time definition. All controls passed. No new physical law, paper or experimental claim was introduced. Earlier September G/S/R findings are credited.

Reproduce this follow-up with `python foundation_audit/verify_foundations.py` (SymPy required). See its source manifest for extraction hashes and the explicit limit on any claim about all historical axioms.

**Existing derivation reconciled with the program:** the [19-step crosswalk](foundation_audit/DERIVATION_PROGRAM_CROSSWALK.md) confirms the prior BFG-internal conditional Gram derivation and its correct active-target coordinates. The 8/45-versus-8/53 witness fails the full same-completion premise and does not refute that derivation. Exact complex rectangular-channel, selector, weight, seed and capacity-transport checks passed. Run `python foundation_audit/verify_crosswalk.py`. Source versions are pinned, and remaining role/ordering obligations are separated from already derived algebra. No program rule or published PDF is changed.

This stage found no contradiction in the focused central finite-model proof chain. It does not certify all 48 statements, establish historical uniqueness of the model, or validate a universal physical law. Next: execute the scalar proof-assistant pilot; certify ambiguous rank decisions; complete adversarial reviews of the other claims; identify a physically discriminating prediction before presenting hardware as a natural-law test.

The original publication remains unchanged. This dated research stage is an internal AI-assisted analytic/computational review, not external peer review. No background scheduler was created. Repository-wide rights remain in force for new materials; the original publication retains its existing file-specific published terms.
