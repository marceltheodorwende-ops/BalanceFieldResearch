# Interior candidate search protocol

Fixed before implementation evaluation. Continue from bbc0406 and its eight
unresolved intact-network cases. Follow the three BFG audit documents identified
by hashes in ../../docs/BOUNDARY_PROTOCOL.md. Known-case exploratory engineering,
not independent preregistration or empirical BFG validation.

Change: an optional fallback proposing interior edge/initial parameters from
all observations using bounded numerical least squares. Search in normalized
box coordinates, midpoint start, finite-difference Jacobian and projected
Gauss–Newton steps with backtracking. At most 256 numerical trajectory calls.
Numerical residuals never certify compatibility or family exclusion. Convert
the final candidate to exact rationals in the original box, then apply the
existing 64-term rigorous whole-history certifier. Candidate failure, numerical
failure and budget exhaustion may retain unresolved, never create an alarm.

Primary endpoint: resolve additional compatible histories in the unchanged
20-case network-transfer catalogue without reversing any existing certificate.
Secondary control: repeat the prior 39-case catalogue. Keep physical bounds,
measurements, times and sensor subsets unchanged. Earlier solvers unmodified.

Compare the existing 31-box/27-candidate search with the added numeric fallback.
Also run the old solver with 256 boxes/27 candidates as a search-budget control.
Report computation counts separately: a rational box evaluation and a floating
trajectory evaluation have different costs; no equal-runtime superiority claim.
Failure: false exclusion, out-of-box witness, accepting only a small floating
residual, changed data/thresholds, or no additional certified histories.
No optimizer tuning after seeing this stage's results without an explicit new
protocol amendment. Preserve negative outcomes and the complete input hashes.
