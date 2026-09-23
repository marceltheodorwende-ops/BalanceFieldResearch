# Multidimensional Small-Load Contraction

**Development/calibration data only. No held-out target is opened.**

## Sufficient theorem

For a finite reduced master state with `Y >= 0`, rank-one positive `rho`, positive keep load `lambda_keep >= eta > 0`, and `||Y||_2 <= delta`,

\[
\|Y_+\|_2 \le C(\delta,\mu,\eta)\,\|Y\|_2^2,
\]

where

\[
C=\|P\|_2^2\left(1+\frac{\mu}{\eta}\right),
\qquad \mu=\operatorname{tr}\rho.
\]

The bound is sufficient and intentionally conservative.

If additionally

\[
q=C\|Y_0\|_2<1,
\]

then repeated application with the same uniform `C` gives

\[
\|Y_n\|_2 \le C^{-1}q^{2^n}.
\]

This is double-exponential decay in recursive depth.

## Current audit

Certificates evaluated: `3816`

Explicit bound satisfied: `3816/3816` (`100.000%`)

Already inside the strict local condition `C||Y||<1`: `2665/3816` (`69.838%`)

## By recursive depth

| Depth | Certificates | Bound pass | Local C||Y||<1 | Median actual ||Y+||/||Y||² | Median C||Y|| |
|---:|---:|---:|---:|---:|---:|
| 1 | 1375 | 1375 | 16.291% | 0.0662911 | 1.131 |
| 2 | 1375 | 1375 | 100.000% | 1.17931 | 0.030485 |
| 3 | 1066 | 1066 | 100.000% | 1.17227 | 0.000800161 |
| 4 | 0 | 0 | 0.000% |  |  |

## Interpretation

The theorem explains the observed near-quadratic recursive load contraction without fitting the exponent. The carrier data are used only to test whether the sufficient finite-dimensional inequality is respected by the current implemented states.

A failed strict-local condition `C||Y||<1` does not refute one-step quadratic boundedness; it only means the conservative uniform iteration bound is not yet strong enough at that state.
