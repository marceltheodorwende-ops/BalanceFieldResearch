# Annual Sunspot BFG Carrier — Frozen Held-Out Result

Calibration: **1700–1899**

Held-out evaluation: **1900–2008**

Mapping fingerprint:

`8345c50579367c4fcd09d6c1b2e6bcf22d909650e36e1b8e6bfb11f827f7aecc`

Plan fingerprint:

`59faa343efb8604f6d88e831995480fa71155a0473aef0d56bc1df6224d90247`

## Preregistered success criterion

BFG held-out RMSE had to be at least 1% below the frozen matched adaptive null,
and at least 90% of held-out mapped states had to pass canonical BFG reclosure.

## Result

Primary statement: **FAIL**

- BFG RMSE: `18.142522`
- matched-null RMSE: `18.262712`
- improvement vs matched null: `0.658%`
- AR(12) RMSE: `17.691890`
- persistence RMSE: `28.605886`
- held-out reclosure success: `100.0%`
- held-out novelty among successful reclosures:
  `100.0%`

The BFG adaptive correction improved on its preregistered matched ordinary-feature
null, but only by about 0.658%, below the required 1% margin. The stronger AR(12)
baseline also had lower RMSE than both adaptive corrections.

No held-out retuning is permitted. This benchmark remains permanently recorded
as a negative primary result.

The structural result (100% reclosure and 100% novelty among successful held-out
states) is reported separately and must not be substituted for the failed primary
forecast criterion.
