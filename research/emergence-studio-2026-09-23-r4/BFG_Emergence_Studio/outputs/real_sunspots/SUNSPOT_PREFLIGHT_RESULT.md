# Annual Sunspot Carrier — Readiness-First Refresh

Status: **READY_FOR_VALIDATION**

This is the active annual-sunspot result under the same readiness-first policy
used for the Mauna Loa CO2 carrier.

The previous 1900–2008 confirmatory result is preserved separately in the audit
history. Because those years have already been opened, they are treated as
development data for this new hypothesis and are **not** reused as blind held-out
data.

Development data: **1700–2008**

Prospective held-out target: **2009–2025**

Held-out metrics evaluated: **NO**

Mapping fingerprint:

`a0b3673cca890c5090f472fa07fe1fec813f6663773025da07038b26132ca156`

Plan fingerprint:

`0d79fbd248229b50a5a3d2a2d5babbd1b7c4bae843e98308d6ff9517239af0d9`

## Readiness rule

The same portfolio readiness rule used for CO2 is applied:

- BFG wins at least 2 of 3 temporal folds.
- Mean relative RMSE improvement is positive.
- Worst fold is no worse than -2% versus the matched null.
- Canonical BFG reclosure succeeds on at least 95% of evaluation states.

## Rolling temporal preflight

- Fold 1 (1860–1909): BFG RMSE `15.136760`, null RMSE `15.895379`, relative improvement `+4.773%`, reclosure `100.0%`
- Fold 2 (1910–1959): BFG RMSE `18.682428`, null RMSE `18.979922`, relative improvement `+1.567%`, reclosure `100.0%`
- Fold 3 (1960–2008): BFG RMSE `17.088313`, null RMSE `17.168818`, relative improvement `+0.469%`, reclosure `100.0%`

Summary:

- fold wins: `3/3`
- mean relative improvement: `+2.270%`
- worst fold: `+0.469%`
- minimum evaluation reclosure: `100.0%`

## Full development fit

- selected BFG feature: `neutral_retention`
- selected matched-null feature: `absolute_slope`
- BFG RMSE: `14.786536`
- matched-null RMSE: `14.821988`
- AR(12) RMSE: `14.941540`
- relative improvement: `+0.239%`
- canonical reclosure: `100.0%`
- novelty among successful reclosures:
  `100.0%`

## Interpretation

The refreshed carrier is **READY_FOR_VALIDATION** under the updated portfolio
criteria.

That is a readiness result, not a confirmatory empirical pass. A genuinely new
annual-sunspot continuation for 2009–2025 must be supplied later under the
Blind-Heldout Guard. No confirmation permit is generated during this refresh.
