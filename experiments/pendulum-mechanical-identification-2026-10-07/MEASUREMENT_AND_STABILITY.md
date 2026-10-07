# Measurement consistency and estimation stability

Exploratory checkpoint, 15 existing attempt-1 recordings only.
All reserved attempt-2/3 data remain unopened. No new confirmation.

## Verified preceding run

GitHub Action 37686204956 completed successfully, including four controls,
15 development-file downloads with source verification, model evaluation and
artifact upload. Logs reproduce local model scores exactly.
Artifact 11512175109: Development-mechanical-identification.
The previous immediate analysis is now remotely reproduced.

## Primary-source sensor information

PASCO's PS-3220 product documentation states angular resolution 0.18 degrees
and 2,000 encoder divisions per revolution. Its reference guide likewise
describes 0.18-degree resolution. Sources checked on 2026-10-07:
https://www.pasco.com/products/sensors/wireless/wireless-rotary-motion-sensor
https://cdn.pasco.com/product_document/013-15949A_PS-3220_WI_RMS_REF_GUIDE_11-28-18.pdf

0.18 degrees is pi/1000, approximately 0.003142 radians.
The CSV's three decimal places do not establish a 0.001-radian sensor accuracy.
Resolution, display rounding, absolute accuracy, bias and velocity processing
are distinct quantities. Actual sensor zero, software filtering and measurement
uncertainty for these recordings are not supplied by the materials read here.

## Angle/velocity consistency

Check delta(theta)=integral(w dt) over nonoverlapping 0.1-second blocks.
Use trapezoidal integration of the measured 0.01-second samples.
Mean recording relative displacement-balance RMSE: 0.010657 (about 1.07%).

A rounding-only bound, 0.001 rad for two endpoint angles plus integrated
velocity rounding, is exceeded by a mean 36.65% of blocks. This is not evidence
that the physical equation theta_dot=w fails: it omitted encoder effects,
quadrature error, velocity derivation and calibration uncertainty.

Illustrative sensitivity: add half an encoder step for each angle endpoint.
Then bound=0.001+pi/1000+0.0005*duration radians.
Only 0.0223% of blocks exceed that assumed bound, averaged over recordings.
This is a plausible resolution-based envelope, not a manufacturer-certified
accuracy or a fitted statistical uncertainty model. It does not validate the
assumed velocity-error bound or eliminate sensor bias.
Most apparent small inconsistencies can thus be compatible with the instrument
resolution; use a measurement-aware latent state, not exact cleaned values.

The earlier constant-retention audit remains a rounding-only diagnostic.
Its limitation was explicit; this instrument finding motivates a richer error
model rather than rewriting its negative result.

## Window and forecast-horizon stability

Fit integral balances using the first 20,30 or40 seconds.
Evaluate all fits on the common development interval 40<=t<60.
Forecast horizons: 0.05,0.1,0.2,0.5 seconds.
Five rivals across 15 recordings produce 900 model/configuration rows.
These are exploratory sensitivity settings, not independent experiments or
a procedure for choosing a final model using test data.

For 30-second fitting, mean error relative to velocity persistence:

| Horizon | Gravity | Viscous | Quadratic | Mixed |
|---|---:|---:|---:|---:|
| 0.05 s | 0.4018 | 0.4013 | 0.3999 | 0.3999 |
| 0.10 s | 0.2608 | 0.2602 | 0.2586 | 0.2586 |
| 0.20 s | 0.1379 | 0.1373 | 0.1364 | 0.1364 |
| 0.50 s | 0.0859 | 0.0857 | 0.0857 | 0.0859 |

Changing the fitting window has relatively little effect on these aggregate
scores, but small friction-model differences and ranking changes preclude a
strong claim about the true damping mechanism.
Horizon-dependent normalized scores have different persistence denominators;
decreasing scores do not mean absolute forecast error decreases with horizon.
The 0.1-second score differs from the previous report because validation now
uses only seconds40–60 rather than30–60. No old metric is overwritten.

## Implications for BFG realization

A richer carrier should retain angle and velocity with explicit instrument
uncertainty. The large improvement over persistence mostly follows the
mechanical gravity dynamics; it is not evidence of BFG superiority.
Friction ratios and physical projection must be checked for identifiability.
The free absolute mass/inertia/energy scale remains unresolved by angular data.
Do not equate device resolution with a complete physically justified observable.

Next: assess latent-state/noise and offset models, identify shared constraints
across lengths and damping conditions, and derive a typed carrier/projection
candidate with those constraints. Confirmation remains sealed.

## Reproduce

    python diagnostics.py ../bfg-realization-development-2026-10-07/data results

Requires the identification package's pinned NumPy/SciPy.
Tables: measurement_consistency.csv, window_horizon_sensitivity.csv;
aggregate results: diagnostic_summary.json.
Four existing numerical controls remain passing. The diagnostic uses the same
fit/forecast seams and checks the development filename allowlist.
A bounded workflow reproduces this checkpoint after publication.

