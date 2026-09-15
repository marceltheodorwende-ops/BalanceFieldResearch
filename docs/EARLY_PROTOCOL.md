# Early observation protocol E1 (2026-09-15)

Fixed before execution. Deterministic validation, not external preregistration.
No training, feature selection or fitted parameters.

Assume fixed undirected heat diffusion as in D1. Observe the Euclidean
disagreement norm initially and at step m=5. Predict an interval for its ratio
at H=20, with dt=0.2. Predictor inputs are only q=norm(z_m)/norm(z_0), m and H;
graph, spectrum, later states and BFG readouts are not predictor inputs.

Test the interval [q^(H/m), q]. Also test a conservative interval when the
reported q has a known absolute error at most 0.01. Error endpoints -0.01,0,
+0.01 are deterministic stress cases, not a probabilistic noise model.

New graphs: sizes 7 and 9, 20 realizations each, RNG seed 20260915. Start with
a path with independent Uniform(0.2,1.2) weights. Add every non-path edge with
probability 0.25, with a fresh Uniform(0.2,1.2) weight. Each graph uses initial
e_0 and an independent Uniform(0,1) vector normalized to sum one. Thus 40 graphs,
80 state cases. No earlier path/star examples are reused as evaluation cases.

Accept: all 80 exact intervals and all 240 error-aware intervals contain the
simulated H-step ratio within 1e-10. Report all rows, maximum violation, mean
interval widths, and compare width with the no-measurement interval [0,1].
Widths are descriptive, not statistical confidence or predictive accuracy.
The graph generator sees randomness; interval computation does not.
