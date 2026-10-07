# BFG empirical research program

Authorization: the repository owner requested continued background research,
completion reports and subsequent experiments, prioritizing real measurements
and extending beyond EEG into physics, chemistry or biology.

## Completed EEG experiment

Branch: experiment/real-eeg-covariance-2026-10-07.
Protocol freeze: 37f31b1b8aae878418fe2510a55b7896bb114579.
Paper source: 76d9e87b4275ec41b3dcd84434e2ee3791a8d076.
Successful completed workflow: 37681346583.
Published results commit: d1e4a2d8bb02de4ea2cbc97c7fd6d590d23c40b9.
GitHub report: experiments/real-eeg-covariance-2026-10-07/README.md.

69 held-out people, 3,685 prediction pairs; 100% model coverage;
28 rejected windows in the entire cohort, zero excluded recordings.
Mean relative Frobenius error: BFG 0.8674, persistence 0.5864,
linear 0.6655, frozen geometry 1.2206.
Paired BFG-minus-persistence 0.2810, 95% CI [0.2193,0.3299];
BFG-minus-linear 0.2019 [0.0428,0.3134];
BFG-minus-frozen -0.3532 [-0.8150,-0.0539].
Frozen practical success criterion failed. This tests the additional EEG
bridge, not a general rejection of the abstract BFG construction.
Seven code controls passed. Independent spectral calculation reproduced all
3,685 held-out losses (max absolute residual 7.105427357601002e-15);
subject bootstrap and artifact checksums independently verified.
MATHEMATICAL_ASSESSMENT.md documents derivation and conditional bridge theorem.

Initial run 37674587952 failed downloading before empirical evaluation.
Official AWS mirror plus official SHA256 verification repaired transport.
Run 37680650640 had invalid YAML; 37680964493 produced identical empirical
results but publication failed because of root gitignore; corrected publication
completed in 37681346583. Do not repeat or announce those as new findings.
Reporting record: completed negative EEG result, independent verification and
next frozen pendulum protocol are included in the current user-facing completion
report on 2026-10-07. Do not send a duplicate EEG completion notification.

## Current priority: exploratory realization

Strategy changed by the user on 2026-10-07. Prioritize the two-stage realization
below before additional confirmatory experiments. The previous pendulum protocol
25855b7d44417ea7c23da62630a63290cf25a3d3 remains an immutable historical proposal;
its holdout evaluation is deferred and must not be launched automatically.

### Stage 1: development-only exploration

Use the current architecture only on development observations. Test feasibility,
stress the carrier map and find failure modes. Track each mapping proposal and
whether its structure is derived from BFG, independently motivated measurement
assumptions, or a fitted convenience. Changing a bridge is allowed here but all
results remain exploratory. Performance alone does not establish derivation.

For the existing pendulum candidate on experiment/real-pendulum-decay-2026-10-07,
only attempt 1 (15 recordings) may be downloaded or inspected. Attempts 2 and 3
(30 recordings) remain sealed. Primary source and pinned commit:
EnzeXu/Damped_Pendulum_Dataset, cbf82673641ecd65e902ad5c38a048387649a2a0.
The linear energy bridge is a hypothesis, not an established BFG realization.
Check carrier-state identifiability, preparation, units/scale, basis invariance,
rank/gates/terminal behavior, clock, observables, noise robustness and forecast
information availability. Report failures and missing physical identifications.

Specify intervention logic and falsifiable response predictions, including what
interventions the real dataset actually supports. Passive recordings cannot
establish causal intervention effects. If intervention evidence is absent,
document the missing dataset or design instead of claiming causal confirmation.

Already inspected EEG holdout subjects cannot confirm any revised hypothesis.

### Stage 2: frozen confirmatory realization

Proceed only when a derivation dossier and reproducible implementation fully
specify the claimed BFG-derived structure, with all additional empirical
assumptions explicitly separated. Freeze carrier map, preparation, state update,
observables and clock, intervention logic, rivals, preprocessing, exclusions,
sample/split, uncertainty procedure and decision rule in a commit before
accessing untouched subjects/data. Include strong physical/statistical rivals.
If no testable bridge exists, document the open requirement and remain in Stage 1.
Confirmatory claims are limited to the frozen realization and supported tests;
prediction and intervention claims must be distinguished.

Preserve independent test observations and prohibit development downloads that
include holdout files. Do not tune scientific criteria using held-out outcomes.
Current task: assemble the development-only realization/derivation dossier,
then run bounded exploratory analyses; do not resume the old pendulum holdout
instruction. Prefer mathematically justified conclusions over positive scores.
Strategy update is reported to the user; no empirical result claimed.

## Rules for subsequent experiments

Use real open measurement datasets as primary evidence. Synthetic inputs are
permitted for implementation controls, not as substitutes for empirical results.
After finishing the current experiment, select a justified non-EEG experiment
in physics, chemistry or biology. State precisely which additional preparation,
clock, observable or transition bridge is being tested; the paper does not
already supply these physical identifications. If a predictive bridge cannot be
specified, record that obstacle rather than inventing a derived physical law.

Freeze each question, preparation, preprocessing, model, baseline, split and
loss before held-out evaluation. Never tune to a previously inspected holdout
and present it as independent confirmation; use genuinely new test observations
for revised hypotheses. Keep at most one new empirical experiment active.
Use dedicated branches and bounded GitHub Actions runs (at most 45 minutes per
run). Do not merge into main, rewrite papers, use paid services, contact third
parties or access restricted data without separate authorization.

Publish code, provenance, exclusions, sufficient statistics, uncertainty,
results and limitations. Verify GitHub upload and the actual run outcome before
claiming completion. Maintain this ledger with current branch/run, completed
experiments and already-reported outcomes to avoid duplicate reports.

## Reporting

On each completion report what was tested, how it finished, sample size,
comparison results, uncertainty, limitations and GitHub links. If blocked, say
what failed and whether any results exist. Continue with one justified next
experiment after a completed result; avoid indefinite loops of identical retries.
