# BFG empirical research program

Authorization: the repository owner requested continued background research,
completion reports and subsequent experiments, prioritizing real measurements
and extending beyond EEG into physics, chemistry or biology.

## Current experiment

Real EEG covariance prediction, branch experiment/real-eeg-covariance-2026-10-07.
Protocol freeze: 37f31b1b8aae878418fe2510a55b7896bb114579.
Paper: The Balance Field Equation as a Recursive World Formula, source commit
76d9e87b4275ec41b3dcd84434e2ee3791a8d076.
Initial run 37674587952 passed six numerical controls but failed during data
download with a connection timeout. No empirical evaluation was performed.
Transport repair uses the official AWS mirror with official SHA256 verification.
Keep the scientific protocol fixed and report negative results as fully as positive ones.

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
