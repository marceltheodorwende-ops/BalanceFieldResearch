# EP01 — Reliable seizure detection in long-term scalp EEG

Status: ACTIVE preparatory package; NOT a frozen confirmatory protocol.
Owner instruction: 25 October 2026. Epilepsy research now takes priority.
P81 remains OPEN / deferred; no mathematical or publication gate is waived.

Latest explicit constraint (25 October 2026): do not invent physical/biological laws,
free dynamics terms or post-hoc rules to make results fit. Any candidate presented
as BFG-derived must obtain its mathematical conditions from the active BFG equations,
with explicit derivation, domain and independent checks. Measurement assumptions
and statistical comparator models remain separately labelled; neither is an internal
BFG law. If a required condition is not derivable, record it as OPEN rather than
adding it silently. Protocol/scoring choices are evaluation definitions, not laws.

## Question and intended use
Can spatial EEG network features reduce false seizure alarms relative to strong conventional detectors without losing event sensitivity on unseen patients and an external dataset?
Initial use: retrospective support for specialist review in an epilepsy monitoring unit.
Detection of ongoing seizures, not pre-seizure forecasting, diagnosis, treatment selection or proven clinical benefit.

## Evidence motivating the question
- EpiCARE 2026 priorities, including diagnosis/prediction and patient outcomes: https://pubmed.ncbi.nlm.nih.gov/41489013/
- AES/NINDS priorities: https://aesnet.org/research-funding/epilepsy-research-benchmarks/plain-language-summary
- SzCORE validation framework: https://epilepsybenchmarks.com/framework/
- Candidate primary data documentation: https://physionet.org/content/chbmit/1.0.0/ and Siena via SzCORE.
Record dataset version, original license, provenance and hashes before use; inspect metadata first.
CHB-MIT repeat sessions must be grouped by actual person (not case label). Pediatric/adult and acquisition differences require separate reporting.
TUH or any other access-controlled data are not authorized without separate access review.

## Existing evidence / separation
The earlier EEG covariance forecast failed its practical criterion (BFG relative Frobenius error .8674 vs persistence .5864); see experiments/RESEARCH_PROGRAM.md on experiment/real-eeg-covariance-2026-10-07.
It was NOT a seizure detector. Previously examined subjects cannot confirm revised hypotheses.
No seizure EEG samples have been downloaded or evaluated for EP01 at initialization.

## Single active dependency: EP01 data and evaluation contract
Before modeling:
1. Inventory repository code, published EEG split manifests and all previously accessed subjects/datasets.
2. Validate access/license and event annotation semantics for CHB-MIT and Siena. Select development records explicitly and create an allowlist; no whole-dataset archives including held-out records.
3. Specify patient-disjoint development/validation/test partitions and a genuinely untouched external evaluation cohort. If prior exposure cannot be excluded, label development, not confirmation.
4. Freeze signal units, causal preprocessing, reference/montage, sampling, channel mapping, artifact handling, missing data, event matching and recording gaps.
5. Fix baseline implementations/versions and network-feature ablations using identical data and tuning budgets.
6. Specify threshold calibration using development/validation only. Candidate sensitivity target 90% is a research design choice, not a clinical standard; finalize it before any test data. A fixed validation-selected threshold is applied unchanged at test, with achieved sensitivity reported; NEVER retune test thresholds to obtain matched sensitivity.
7. Specify event-based false alarms per 24 recording hours, event sensitivity, latency, per-person results and patient-cluster uncertainty. Fix event matching/merging/tolerance/refractory rules via a pinned SzCORE-compatible scorer. Retain all non-seizure hours; report exclusions and recording duration. Window accuracy alone is insufficient.
8. Define primary comparison, sensitivity noninferiority margin, uncertainty/decision rule, sample-size feasibility and artifact/montage/domain-shift sensitivity before freeze. If precision is inadequate, report inconclusive.
9. Verify leakage controls, split validation and scoring edge cases independently, then publish the complete versioned protocol BEFORE accessing test EEG or test labels.

## Modeling after EP01 completion
Strong simple signal-feature baseline, established detector and suitable modern reference model; add spatial/network features as an ablation with matched preprocessing.
BFG is an optional, explicitly specified extra model hypothesis; demonstrate incremental predictive value separately from mechanism claims. No neural mechanism follows from curve fit or covariance forecast.
For BFG derivations only the hash-verified Dynamic Order PDF is active. Source-access failures must not block independent dataset/scoring work or be bypassed with a different paper.
No model, target sensitivity, clinical efficacy or BFG advantage is established here.

## Execution and publication
Continue the existing background task; do not create an additional automation.
Exactly one active empirical experiment, check queued/in-progress Actions first, timeout <=45 min per Actions run.
Publish code, protocols, provenance, audits, positive/negative results and uncertainties on experiment/real-eeg-covariance-2026-10-07 in marceltheodorwende-ops/BalanceFieldResearch. Keep a transition/status mirror on the historical pendulum branch when publication works.
No main merge, original paper edit, paid services, third-party contact, restricted data, invented measurements or holdout tuning.
Verify published bytes and actual workflow results before claiming success. Keep bounded failure receipts and avoid identical unproductive retries.
Completion of EP01 requires reviewed contract + independent checks + verified GitHub publication and ledger entry. Current status remains preparatory.

