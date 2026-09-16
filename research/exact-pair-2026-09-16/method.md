# Exact two-node fallback

API: `bfg_lab.certified_exact.assess_exact_pair`, same arguments as
`assess_boundary` plus `log_terms=64` (integer 1..256). CLI:

```sh
python -m bfg_lab.certified_exact --input your_input.json
python -m bfg_lab.exact_evaluation
```

This is an additional fallback after the existing boundary solver. Original
functions are unchanged. It applies only to two nodes, both observed (either
sensor order), exactly known initial state, zero measurement error and two
times, zero and t>0. Existing input validation remains mandatory.

## Proof and certificate contract

For a symmetric edge w>=0, heat evolution preserves the sum S=x0+x1, while
the difference D=x0-x1 obeys D(t)=D(0) exp(-2wt). This follows by adding and
subtracting the two differential equations. If D(0) is nonzero, any feasible
exact observation must have the same S and ratio r=D(t)/D(0) in (0,1].
For r=0, finite w and finite t cannot reach exact equilibrium. Negative r
or r>1 is also impossible. These tests give whole-family exclusion certificates.

Otherwise there is exactly one candidate weight w=-log(r)/(2t). Define
z=(1-r)/(1+r), so 0<=z<1. Integrating the geometric series for 1/(1-z^2)
gives w=(1/t) sum_(k>=0) z^(2k+1)/(2k+1).
After N terms, with partial sum s, the omitted terms are nonnegative and at
most z^(2N+1)/((2N+1)(1-z^2)). Divide both bounds by t. Every operation is
rational; the implementation uses no floating logarithm.

If this enclosure lies within the permitted weight interval, return a
`compatible_witness` with `certificate_kind=analytic_two_node` and a
`symbolic_witness`. The symbolic record stores the expression, exact rational
ratio and time, initial state, and rational weight enclosure. Its single edge
is shared symmetrically by both nodes. **It is not the ordinary rational
`witness.weights` format**: consumers must handle this certificate variant
explicitly and must not substitute a rounded weight for the exact expression.

Equal sums and equal differences imply equality of both observed components,
so this candidate fits the entire declared two-time history. If the weight
enclosure is disjoint from the allowed interval, uniqueness proves exclusion.
If the enclosures overlap at a boundary without containment, retain unresolved.
For a constant initial state the existing checker remains responsible.

These are sufficient certificates, not a complete rational/transcendental
decision procedure. Near r=0 the series can converge slowly; noise, uncertain
initial conditions and more observation times are outside this analytic layer.
The method neither widens tolerances nor interprets computation limits as faults.
