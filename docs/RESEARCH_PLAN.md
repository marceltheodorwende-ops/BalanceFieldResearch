# Development and evaluation plan

## First application: network robustness

Question: do fixed BFG-derived measurements add held-out predictive information
about disagreement decay or recovery after perturbation beyond standard graph
and dynamical summaries?

The current demo is exploratory only. It contains no trained predictor, no
held-out evaluation, and no claim that BFG outperforms a baseline.

Before an evaluation, preregister graph families, sampling seed, train/test
separation by graph, perturbation schedules, units, numerical tolerances,
load/transport extraction, target recovery horizon and error metric. Fix these
before inspecting test outcomes. Structural recursion level is not assumed to
equal physical time.

Compare degree summaries, Laplacian gap and a capacity-matched model using the
same observations. Ablate persistence projection and reciprocal weights; shuffle
coupling while controlling graph size. Report uncertainty, all failed cases,
and negative results. Do not rename a failed metric after seeing the test set.

## Implementation milestones

- Initial lab: neutral, projection, balance, polar support, numerical tests, toy dashboard.
- Next: resolve Eq. 27; obtain and audit prior definitions needed for Eq. 40.
- Then: complete finite-dimensional state and reclosure specification with gate tests.
- Later: preregister and run a predictive network benchmark.
- Empirical domains follow only after a validated measurement map is available.
