# Mauna Loa CO2 Carrier — Validation Readiness Preflight

Status: **READY_FOR_VALIDATION**

This is a calibration / rolling-origin readiness result only.

**Held-out 1991–2001 target metrics have not been evaluated.**

Mapping fingerprint:

`fd69a8b0d4f771f6effa6fbe5c2a00c79322131bbf2248a5f1ddf37ddb50fea9`

Plan fingerprint:

`653836593f729577e1f878a2212aa1d0ea53cae752f80d57ec4db41599b50a17`

## Readiness rule

The held-out block may be opened only when all of the following hold:

- BFG beats the matched ordinary-feature null in at least 2 of 3 temporal folds.
- Mean relative RMSE improvement across folds is positive.
- No temporal fold is worse than the matched null by more than 2%.
- Canonical BFG reclosure succeeds on at least 95% of evaluation states.

## Rolling preflight

- Fold 1 (1976-01-01 to 1980-12-01): BFG RMSE `0.250560`, null RMSE `0.247080`, relative difference `-1.408%`, reclosure `100.0%`
- Fold 2 (1981-01-01 to 1985-12-01): BFG RMSE `0.434993`, null RMSE `0.446175`, relative difference `+2.506%`, reclosure `100.0%`
- Fold 3 (1986-01-01 to 1990-12-01): BFG RMSE `0.421023`, null RMSE `0.423889`, relative difference `+0.676%`, reclosure `100.0%`

Summary:

- fold wins: `2/3`
- mean relative improvement: `+0.591%`
- worst fold: `-1.408%`
- minimum evaluation reclosure fraction:
  `100.0%`

## Full calibration fit

- selected BFG feature: `lambda_up`
- selected matched-null feature: `recent_level`
- BFG RMSE: `0.406321`
- matched-null RMSE: `0.406874`
- relative improvement: `+0.136%`
- canonical reclosure: `100.0%`

## Interpretation

The carrier is **ready for a confirmatory held-out test** under the frozen plan.

This is not a confirmatory pass and is not reported as empirical validation.
The held-out result remains sealed. If that test is opened later, its result must
be retained whether positive or negative; no post-held-out retuning is allowed.
