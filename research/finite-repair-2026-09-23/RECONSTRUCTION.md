# Reconstruction: remaining selection problem and completion contract

## 1. What is determined now

Given finite power-bounded R, Y>=0 and the declared capacities, the amended persistent subspace and its two projectors are unique. Given an analysis operator A, its polar partial isometry with zero action on the kernel is unique. Given the compressed K with a simple negative ground eigenvalue, its minimizer orbit and rho=(-lambda_0)Pi_0 are unique. A specified compatible conjugation identifies the real polarity pair.

These are conditional constructions from supplied operators. None supplies a function assigning the next Gram factors or next recursive operator from the state.

## 2. Why the repaired ingredients still do not select a load

For a nonzero formed vector p, write Pi_p=pp*/||p||^2. For every fixed c>0, the law

```math
Y_c(p)=I+c\Pi_p
```

is positive definite, phase-invariant, unitarily equivariant and continuous for p!=0. It preserves any real structure fixing the line of p. Distinct c give distinct loads from the same p. These properties, including the formation repair, therefore do not select c. If an independently fixed scale or trace is required, it must be written into the input contract; it is not supplied by positivity or equivariance. This example tests just these stated conditions, not every unformulated BFG axiom.

Each law has a positive Gram representation: choose W=I, L=I, B=Y_c^(1/2), giving B*WB=Y_c. Thus writing a Gram factorization does not eliminate the ambiguity. Conversely, if Y is fixed, its positive square root is unique, but choosing that gauge does not determine the previously unknown Y.

If B_C=D_K F is required by a chosen BFG source, the types and laws for D_K and F must be supplied and checked. A product identity without those laws is not a selection principle: even with an invertible fixed D_K, each candidate B corresponds to F=D_K^(-1)B. Further restrictions on F may distinguish them; they must be proved or declared. This note neither discards that identity nor claims compatibility with restrictions not yet specified.

## 3. Required next-state contract

Declare a typed state S, including its field, inner product, optional conjugation, capacities, load, recursion and any active profile/orbit. Supply single-valued functions

```math
B_+(S),\quad W_+(S),\quad L_+(S),\quad R_+(S),
\qquad H_+=B_+^*W_+B_+,\quad Y_+=L_+^*H_+L_+.
```

Acceptance obligations:

1. State domains/codomains and all dependencies. No unstated external scale, eigenvector sign, stage label or fitted parameter may enter a claim of internal uniqueness.
2. Prove W_+>=0, self-adjoint capacities and well-defined products. In finite dimension this establishes Gram positivity, not uniqueness of the laws.
3. Prove R_+ power bounded, or declare an exact admissibility/termination rule for its failure. Rejecting everything is a total map but is not a nontrivial persistence theorem; give a nonterminal example.
4. Prove the next peripheral support reduces Y_+ if the existing neutral-compatible novelty theorem is to be reused. General nonnormal persistence alone does not establish this.
5. Preserve the conjugation and its intertwining identities if real polarity formation is claimed.
6. Use the minimizer orbit only when all downstream laws descend to it. If an actual vector is needed, include and justify orientation data.
7. Prove the output lies in the same declared state category or in an explicit terminal state. Only then define repeated U and prove quotient congruence where claimed.

This contract is the next research target. The current sources have not supplied enough information to derive a unique choice for all these functions. Selecting one admissible family would produce a conditional completion, whose additional assumptions must be visible. No passing count from the CSV resolves that selection problem.

## 4. Audit disposition

Finite persistence definition: repaired. Real/complex formation and conditional real-structure transport: repaired. Full reconstruction, invariant iteration and general infinite-dimensional realization: open. The [previous review](../canonical-consolidation-2026-09-22/REVIEW.md) remains the failure ledger; this stage supplies amendments rather than deleting its findings.
