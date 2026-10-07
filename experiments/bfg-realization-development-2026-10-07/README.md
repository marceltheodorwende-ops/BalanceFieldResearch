# Development-only realization audit: damped pendulum

**Status: exploratory analysis completed locally; confirmation gate not passed.**
No attempt-2 or attempt-3 measurement file was downloaded or inspected.
The earlier scalar holdout protocol is deferred.

Question: is the proposed linear energy / scalar BFG mapping feasible enough
to justify a frozen physical realization? Answer for this candidate: no.

15 real development recordings (five lengths, three damping settings, attempt 1),
1,364 eligible consecutive extrema, zero rejected pairs.
Source: EnzeXu/Damped_Pendulum_Dataset, commit
cbf82673641ecd65e902ad5c38a048387649a2a0.
Xu et al., TMLR 2026, https://openreview.net/forum?id=xvQYvYEGhj.

| Development diagnostic | Mean per-record relative L2 error |
|---|---:|
| Scalar BFG energy hypothesis | 0.712943 |
| Persistence | 0.065288 |
| Per-record fitted decay | 0.054072 |

The decay comparator is fit and scored on these same development pairs.
These are descriptive in-sample errors, not holdout estimates.
For 311 pairs with both angles <=0.2 rad, median measured next/current
energy was 0.967392, versus predicted 0.061545.
Separate medians summarize distributions, not a median paired difference.

Scale stress: scale factors 0.1 and 0.5 reduce mean recording coverage to
40.4% and 94.0%; factors 1,2,10 retain full coverage but yield errors
0.713,0.796,0.945. Errors with incomplete coverage are on valid pairs only.
Scale fitting alone is not a BFG derivation.

Thirty fixed-seed uniform perturbations of angles by half a rounding unit
(+/-0.0005 rad), with annotations and scale fixed, yield mean BFG errors
0.712922 to 0.712971. This limited rounding stress does not repair the failure;
it is not a sensor uncertainty model or confidence interval.

## What was established and what remains open

The scalar formula matches the existing full ambient BFG implementation on
1,000 scalar inputs, maximum residual 1.6653345369377348e-16.
Five standalone controls passed, including forbidden holdout filenames,
known scalar value, contraction, energy calibration and rejected-pair handling.
All 15 downloaded files match upstream Git blob SHA1; derived provenance also
records SHA256. A patch-added newline was detected and removed before analysis
to restore exact source bytes.

REALIZATION_DOSSIER.md separates the internally derived update from added
energy, preparation and clock hypotheses. It documents a conditional closure
obstruction, nonidentifiability, measurement information and intervention gaps.
The scalar preparation reset is not evidence for a complete BFG trajectory.
Baffle settings have no derived BFG intervention operator. Extrema annotations
use future samples, so this is a retrospective event diagnostic.

The next task is a derivation and identifiability audit of candidate carriers
retaining angle/velocity, still on development data only. No physically derived
matrix/operator map is claimed. If none can be justified, the correct result
is a documented open bridge requirement.

## Reproduce

Requires Python 3.12 or newer, standard library only.

    python -m unittest -v test_explore.py
    python fetch_development.py
    python explore.py .
    python noise_stress.py
    python compress_pairs.py
    python structural_bound.py

The downloader has a development-only allowlist and pinned Git blob verification.
Do not clone or download a complete archive of the primary dataset.
Source files stay out of Git; derived pairs, recording statistics, scale/noise
diagnostics, parameters and provenance are in results/.
SHA256SUMS.txt covers this published audit's code, documentation and results.
A bounded GitHub Actions workflow independently reproduces the development
pipeline and uploads its outputs. Check the actual run before claiming remote
verification completed.

Scientific limitations: same apparatus, cleaned and rounded measurements,
upstream offline peaks, potential-only peak energy, in-sample comparison,
no population uncertainty, no causal intervention identification and no holdout
evidence. Failure concerns this added scalar energy mapping, not all BFG
realizations. Original paper and main branch are unchanged.


INTERNAL_MATH.md proves a scale-independent maximum retention of 35.63% for
this scalar linear-energy bridge. All 1,364 development transitions retained
more than 50%, so changing the reference scale cannot repair this mapping.
