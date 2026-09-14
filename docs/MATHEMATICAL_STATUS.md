# Mathematical status

Sources: the [five-document collection](../papers/README.md). V4 page numbers refer to the PDF. Read the [V3 erratum](ERRATUM_V3.md) and [source audit](SOURCE_AUDIT.md).

## Eq. 27: a concrete counterexample (page 7)

Let R = diag(1, 1/2), with identity metric. Both (1,0) and (1,1) have
bounded forward trajectories with positive limiting norm. Their span contains
(0,1), whose trajectory tends to zero. Thus the span in the printed definition
is the whole two-dimensional space, while the unit-modulus eigenspace has
dimension one. This is an algebraic counterexample, not a floating-point issue.

The lab uses the peripheral spectral interpretation, restricted to normal
power-bounded matrices, with tolerance 1e-10. This is an explicit implementation
choice pending a corrected definition; it is not a silent correction of the PDF.
Mixed stable/peripheral nonnormal transport is rejected in this initial version.

## Implemented identities

- Eqs. 11â€“14 and BFG-C1/C2: C=(I+Y)^-1, B=I-C, Z=C-B.
- Eq. 29: positive-metric orthogonal projection for a supplied independent basis.
- Eqs. 31â€“38: reciprocal weights, direct-sum packet, local gain bound and polar factor.
- BFG-C3: compact split, using square roots of weights as required by Eq. 37.

The local non-expansion bound does not establish contraction of the entire
state-dependent recursion with changing geometry. The numerical tolerance for
zero loads and singular values is a computational convention. A reported
`no_dual_support` is a local diagnostic, not the full Eq. 41 formation gate.

## Not implemented or established

- Complete state update for capacities, recursive transport and carrier maps.
- Concrete B_C, W_N and L_C reconstruction functions. Structural V2 sections 23–24 explicitly leave the microscopic construction open.
- Full formation gate, universal iteration, intrinsic infinite-future quotient.
- General nonnormal or infinite-dimensional implementation.
- Reproduction of every original figure or the precise 10,000-instance streams.
- Natural-theory recovery, energy identification or consciousness measurement.

The network experiment uses R=I-0.2L and Y=L+0.2I. These are declared toy
choices, not derived universal carrier laws. In connected consensus networks,
the persistent direction is the constant vector. Several projected BFG readouts
can consequently remain unchanged despite topology changes; this is an informative
limitation, not evidence of predictive power.
