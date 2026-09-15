# One early observation: a conditional recovery interval

Under fixed symmetric heat diffusion, one observation of disagreement after
five steps narrows the possible disagreement after twenty steps. In 80 new
state cases on 40 weighted random connected graphs, every exact interval and
all 240 bounded-error intervals contain the simulated target. Average interval
width is 0.270342 versus 1 for the no-measurement interval [0,1]. With absolute
ratio error at most 0.01, average width across the three error cases is 0.282158.
No violation was observed. This is not a statistical coverage probability.

Verification: 39 tests in the repository publication set passed after the final
code change. Four new tests cover single-mode equality and mixtures, error
enclosure, invalid inputs and all 80 network cases. An additional pre-existing
local observation module is outside this publication; its files are preserved.
The initial focused run failed on the missing early module before implementation.

See the [fixed protocol](EARLY_PROTOCOL.md). Reproduce with
`python -m bfg_lab.early`; JSON includes every case and the protocol hash.

## Derivation and observation budget

Let z be the initial disagreement, q=||R^m z||/||z||, and p=H/m >=1.
For the symmetric heat operator, diagonalize R with eigenvalues r_j in [0,1].
Normalize squared initial modal coefficients to weights w_j summing to one.
Then q^2=sum w_j r_j^(2m). Convexity of u^p on [0,1] gives

`q^(2p) <= sum w_j (r_j^(2m))^p <= sum w_j r_j^(2m) = q^2`.

Taking square roots yields the prediction interval `[q^(H/m), q]`.
The function receives only q, m, H and an optional absolute error bound.
It never receives the graph, its spectrum or a later state. The test harness
constructs the interval before simulating the future target.

If measurement q_hat has known error <=e, intersect [q_hat-e,q_hat+e] with
[0,1], obtaining [a,b]. A conservative future interval is [a^(H/m),b].
An empty intersection is rejected as incompatible. This assumes a bound on
the normalized ratio error, not independent additive sensor noise on raw states.

## What is and is not established

The additional measurement supplies transient information discarded by the
initial projected readouts in D1. It needs access to the network-wide
disagreement norm at two times, including the initial reference. That is a
real observation cost, even though graph topology is not an input to the bound.

The interval can be wide. A single exponential attains its lower endpoint;
mixtures can share the same early ratio but have different later ratios.
Thus this does not deliver an exact point prediction, a recovery time estimate,
or an optimal interval. Equal test conditions do not imply universal usefulness.

This result is standard spectral convexity under the specified diffusion law,
not a new BFG law or a demonstration of BFG superiority. External forcing,
time-varying transport and general nonnormal dynamics are outside the proof.
The 80 cases are a validation grid with no training or fitted model, not a
held-out empirical study. Original papers and earlier experimental rules remain
unchanged. The practical result is a rigorously bounded forecast from an
explicit additional observation, with assumptions that can be checked separately.
