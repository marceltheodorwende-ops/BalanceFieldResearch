# Real EEG one step covariance prediction protocol

Frozen 7 October 2026 before measurement files were downloaded or evaluated.
Source paper: The Balance Field Equation as a Recursive World Formula,
6 October 2026, BalanceFieldResearch commit
76d9e87b4275ec41b3dcd84434e2ee3791a8d076, sections 4–14, 17, 42, 67, 69, 72.

## Question

Does the canonical finite BFG update, with the explicit preparation and readout
below, predict the next measured EEG covariance better than persistence, a
development-fitted linear model and a frozen-geometry control? This is a test of
this additional EEG bridge hypothesis, not empirical validation of the world
formula, consciousness, gravity or the Born rule. No task classification is claimed.

## Data and separation

PhysioNet EEG Motor Movement/Imagery v1.0.0, DOI 10.13026/C28G6P.
Use all 109 numbered subjects, runs R01 (eyes open) and R02 (eyes closed).
Subjects 001–040 are development, 041–109 are held out. No tuning after held-out
evaluation. All recordings and rejected recordings must be listed. Missing files
or invalid headers/channels are exclusions, not replacements. Require at least
30 development and 50 held-out subjects with both runs for a completed evaluation.

Choose FC3, FC4, C3, C4, CP3, CP4, Cz, Pz before download. Preserve EDF amplitude
calibration, report volts. Subtract the instantaneous eight-channel mean. Apply a
causal fourth-order 1–40 Hz Butterworth bandpass at 160 Hz, reset each recording,
discard its first four seconds. Partition into nonoverlapping two-second windows,
demean per window and compute sample covariance. Use fixed 5 percent isotropic
shrinkage: F=0.95*C+0.05*trace(C)*I/8. Reject nonfinite data, zero-power windows,
windows with any absolute referenced input above 500 microvolts, or clipped raw
chosen-channel samples. Reject pairs touching a rejected window; do not bridge gaps.

## Explicit additional bridge

For each current window reset a one-step preparation on eight measured channels:
K=-I, rho_F=F, rho_W=F/trace(F), P=I, Y=F/s. The formation unit is squared volts;
K=-s*I in that matched unit (its value has no effect on the no-complement branch).
s is the 95th percentile of eigenvalues of accepted development-window F only.
This is a constitutive preparation, not a reconstruction derived in the paper.
Perform the ambient canonical update, including selection, positive loads,
reduced SVD, R4, seed gates. Read out the next physical covariance as
C_pred=s*V*Y_next*V_dagger, with zeros in discarded ambient directions. Compare
against the next measured shrunk F. No post-hoc rescaling of BFG predictions.
The two-second measurement horizon is a proposed clock bridge; it is not derived
from recursion count. Each window is independently prepared; this is not an
unforced many-step BFG orbit.

## Comparators

Persistence predicts F_next=F_current. The linear comparator fits the 36 unique
covariance entries (divided by s) with an intercept and ridge penalty 1e-3 times
the number of development pairs, without penalizing the intercept. Symmetrize
and project its prediction onto the positive semidefinite cone. All parameters
are development-only. Frozen geometry uses Y=mean(F_development)/s in every
preparation and uses current F for loads, keeping all other rules and the readout.
It is an ablation model, not the canonical BFG recursion.

## Endpoints and uncertainty

Primary loss: ||C_pred-F_next||_F/||F_next||_F. Secondary: relative sorted-eigenvalue
error in eight-dimensional ambient coordinates. Average pairs within each run,
then runs within subjects, then subjects equally. Report each condition separately.
Report canonical and control terminal rates against all eligible pairs. Primary
paired comparisons use the common nonterminal subset, and coverage is mandatory;
do not present selected coverage as universal prediction. Report comparator
performance on all eligible pairs too. No fallback prediction for terminals.
Bootstrap held-out subject means 10,000 times, seed 20261007, percentile 95 percent
intervals for model losses and BFG-minus-comparator differences. Comparisons are
exploratory and unadjusted; no confirmatory significance claims. A practical
success target is lower mean loss than every comparator, upper paired interval
below zero and at least 95 percent coverage; no threshold is fitted to results.

## Numerical controls

Rank tolerance: 1e-12*max(1,largest singular value). Relative tolerance 1e-10 on
well-conditioned controls. Compare scalar update against its independent closed
form. Test joint input-unitary covariance with compatible SVD frames, m4=1,
successor positivity, trace, projector and dimension. Exact-rank mathematics is
distinct from numerical rank; report rank sensitivity at 1e-10 and 1e-14 on all
held-out pairs as a secondary diagnostic. Floating-point boundary cases are
reported rather than silently clipped into a model branch.

## Publication

Publish this frozen protocol, source code, dependency versions, tests, file URL and
SHA256 manifest, window-level sufficient statistics, pair losses, subject summary,
bootstrap results, plots and limitations. Raw EDF files stay at PhysioNet and are
downloaded reproducibly; derived data retain PhysioNet attribution and ODC-By 1.0.
Repository rights for original code/documentation remain unchanged. Publish negative
and inconclusive results with the same completeness as positive results.
