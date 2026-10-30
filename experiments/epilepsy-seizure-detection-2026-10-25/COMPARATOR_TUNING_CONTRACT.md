# EP01 comparator and tuning contract

Status: preparatory design constraint; not a frozen protocol, fitted model, or
performance result. Comparator choices are statistical evaluation decisions,
not BFG-derived laws or physiological claims.

## Comparison set required before any holdout access

The frozen protocol must name an implementation, version/commit, license,
input representation and complete hyperparameter search space for every member
of all four slots below. A missing slot blocks confirmation rather than being
replaced after seeing results.

1. **Simple causal signal baseline:** a transparent causal score from the
   common prepared scalp channels, with its decision threshold calibrated only
   on development/validation data.
2. **Established non-network detector:** a conventional feature-based or other
   established seizure-detection method using the same causal input and output
   interface.
3. **Modern reference detector:** a published modern learned detector, with
   causal deployment constraints made explicit rather than assumed from an
   offline architecture.
4. **Spatial-network ablation:** the candidate network representation compared
   to an otherwise identical no-network representation. This ablation isolates
   the network feature; it does not establish a mechanism.

No particular algorithm, library, feature band, architecture, parameter count,
or BFG measurement map is selected by this document. Each remains OPEN until
the required source, code, licence, units, causal availability, and domain
checks are recorded.

## Equal-information and equal-budget rules

For a given development or validation comparison, every eligible method must
receive exactly the same record identities, causal sample prefix, channel
policy, reference/montage transform, invalid/gap mask, recording-time
denominator and event scorer. A method may not use future samples, record
identity, file order, annotations, external data, or a method-specific quality
exclusion unavailable to its rivals.

Before fitting, freeze for each slot: search-space definition, trial budget,
random seeds, early-stopping/data-use rule, maximum input history, output rate,
refractory/post-processing candidates, hardware/runtime limit and failure
handling. The numerical budget is deliberately OPEN now: choosing it requires
the final reproducible environment and must occur before any outcome-guided
search. It must then be identical across comparable slots, except where a
documented fixed implementation requirement makes equality impossible; such a
comparison is secondary and cannot support the primary claim.

All transformations fitted from data (normalisation, channel mapping,
imputation, feature scaling and calibration) are fitted within the applicable
training partition only and carried unchanged to validation/test records.
Repeated CHB-MIT sessions stay within one person partition. No external Siena
record or label is used for model selection.

## Threshold and endpoint rule

Each method supplies a timestamped causal score stream. The validation-only
threshold policy, including the candidate 90% event-sensitivity design target
if retained, must be fixed before test access. That target is a research design
choice, not a clinical norm. Test thresholds must never be retuned to restore
sensitivity. Report achieved sensitivity, false activations per 24 total
recording hours, latency, alarm occupancy, original-event denominators and
person-level distribution using the pinned SzCORE-compatible and complementary
timely endpoints already specified in this package.

Window accuracy, pooled windows, selected seizure clips, or a method-specific
subset cannot be the primary evidence. Methods failing on a record retain an
explicit failed-record receipt and do not silently disappear from a denominator.

## BFG boundary

A BFG-labelled candidate is an additional model hypothesis only after the
unchanged-kernel derivation register closes its required state/measurement,
domain, gauge, closure and unit obligations. A fitted spatial feature or a
better score cannot be renamed a BFG derivation. Until then it may appear only
as a separately labelled statistical candidate, with no biological mechanism
or clinical advantage inferred.

## Freeze gate

Before opening internal-test or Siena data, publish the filled comparator
registry, exact preprocessing/QC contract, tuning budget, threshold selection,
primary paired comparison, noninferiority margin, uncertainty procedure and
decision rule. Inadequate precision is inconclusive. This document does not
remove any of those OPEN obligations.
