# EP01 pre-freeze readiness ledger

Status: **NOT READY TO FREEZE** (31 October 2026). This is a public
bookkeeping ledger, not a confirmatory protocol, model result, clinical claim,
or BFG derivation. A row marked `SUPPORTED` only means that the named
preparatory evidence exists; it never substitutes for the still-required
frozen decision. `OPEN` means no replacement rule may be improvised after
test access.

## Scope and release rule

The only permitted empirical source before a published freeze is the CHB-MIT
development allowlist: 449 train and 116 validation records, grouped by
person. Internal CHB test cases and every Siena subject-level object remain
sealed. A change from this ledger to `READY` requires every gate below to be
closed in one versioned publication, followed by an independent check of the
published bytes. It does **not** itself authorize a data download, model run,
or test opening.

| Gate | Current evidence | Status | Required before `READY` |
|---|---|---|---|
| Scope, prior exposure, and split | `DATA_AND_SCORING_AUDIT.md`; `contract.py`; `check_contract.py` reject CHB person leakage and all EEG/test access | SUPPORTED | Preserve the explicit development allowlist and log any newly discovered prior access; otherwise reclassify affected material as development. |
| Primary-source data/version/license/annotation audit | CHB-MIT pinned-source records, provenance and annotation audits; public Siena landing-page receipt only | PARTIAL | Re-check the exact source version, license and annotation semantics at permitted acquisition time without opening sealed Siena subject data. |
| Development full-header feasibility | `FULL_HEADER_INVENTORY_CONTRACT.md` and preflight define 565 bounded header requests; synthetic controls pass | BLOCKED | Execute the finite, externally supervised, development-only header inventory once; retain every success/failure receipt and do not fill missing records. |
| Measurement/preprocessing/QC | `CHANNEL_POLICY.md`, `STREAMING_CONTRACT.md`, `AVAILABILITY_CONTRACT.md`, `RECORD_SCORING_CONTRACT.md` establish boundaries only | OPEN | Freeze units, reference/montage mapping, channel eligibility, sampling conversion, causal filters, artifact/bad-channel thresholds, gaps/resets and failed-record handling. No item may be called BFG-derived without its separate derivation gate. |
| Scoring | pinned source audit plus `TIMELY_ENDPOINT.md` and record-scoring controls | PARTIAL | Pin exact SzCORE-compatible scorer/version/configuration and complementary timely endpoint: matching, merge/split, tolerance, refractory/held-alarm treatment, deadline and recording-time denominator. These are scoring definitions, not natural laws. |
| Comparator registry and tuning | `COMPARATOR_TUNING_CONTRACT.md` fixes four required slots and equal-information constraints | OPEN | Publish an implementation/version/license/input/search-space/seed/trial-budget/failure-policy registry for all four slots. Select no method or budget from test outcomes. |
| Threshold policy | validation-only rule and optional 90% design target documented | OPEN | Freeze the target (if retained), feasible selection algorithm, tie handling, calibration partition and unchanged test application. The target is a design choice, not a clinical norm. |
| Primary comparison and inference | patient-comparison and precision audits prove limits/controls | OPEN | State estimand, primary paired contrast, noninferiority margin and its clinical justification, interval/resampling method, seed/replications, multiplicity rule, adequacy criterion and decision rule. Inadequate precision must yield `INCONCLUSIVE`. |
| Robustness/domain reporting | pediatric/adult and acquisition separation required in plan | OPEN | Freeze strata, minimum reportable denominators and sensitivity analyses for montage, artifact, gap and domain shift; do not pool incompatible contexts into an unqualified claim. |
| BFG claim boundary | `BFG_DERIVATION_REGISTER.md` and source hash review; no EEG mapping activated | OPEN | Close every state/measurement/domain/gauge/closure/unit obligation from the unchanged active core, with independent counterchecks. Otherwise label a candidate statistical only. |
| Reproducibility/publication review | package checks and SHA manifest exist | PARTIAL | Freeze code/environment/dependencies/configuration and all decision files; run independent leakage/scoring checks; publish and verify the exact frozen bytes before any internal-test or Siena opening. |

## Non-negotiable stop conditions

Do not label an outcome confirmatory, external, or clinically useful if any
row remains `OPEN`, `PARTIAL`, or `BLOCKED`. Do not compensate for a blocked
header inventory with a subset, inferred header, whole archive, hidden
exclusion, data-dependent parameter, or a post-test adjustment. A failed or
missing record stays in the complete-accounting receipt; it is not converted
to a non-seizure true negative, a silent detector, or a dropped denominator.

This ledger deliberately contains no detector, algorithm selection, threshold,
clinical margin, biological mechanism, new dynamical term, or seizure
performance value. P81 remains OPEN/deferred; the historical covariance
experiment remains negative and is not seizure detection.
