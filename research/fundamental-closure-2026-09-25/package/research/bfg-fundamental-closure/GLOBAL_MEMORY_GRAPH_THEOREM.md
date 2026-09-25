# Global Memory-Graph Theorem and Exponential Branch Growth

## 1. Question

Local continuum memory is now understood:

- injective suspension chart: no memory branch is required;
- isolated simple fold: one local sheet bit is sufficient;
- overlapping folds: a larger branch/chart identifier is required.

The remaining global question is whether the number of admissible continuation
branches is nevertheless bounded by one universal finite number.

For the current coupled commuting BFG suspension, the answer is **no** if arbitrary
finite mode dimension is admitted.

The branch multiplicity has a constructive exponential lower bound.

---

## 2. Fixed-alpha one-mode three-root witness

Freeze the reciprocal retained weight at

\[
\boxed{\alpha=0.3},
\qquad
\beta=0.7,
\]

and choose phase

\[
\boxed{\omega=0.94}.
\]

For one closure-depth coordinate \(h>0\), define

\[
y=e^{-h},
\]

\[
y_+
=
\frac{\alpha+\beta y^2}{(1+y)^2},
\]

\[
H_+(h)=-\log y_+,
\]

and the declared phase suspension

\[
G(h)
=
(1-\omega)h+\omega H_+(h).
\]

For target

\[
\boxed{G(h)=1.45},
\]

there are three distinct selected roots:

\[
\boxed{
h_1\approx0.41456487258,
}
\]

\[
\boxed{
h_2\approx2.01177462800,
}
\]

\[
\boxed{
h_3\approx5.11882415753.
}
\]

Their derivatives are numerically approximately

\[
0.26064,\qquad -0.08646,\qquad 0.04898,
\]

so all three roots are nondegenerate.

This is the elementary three-sheet building block.

---

## 3. Dominant-mode decoupling construction

Consider an \(n\)-mode commuting selected stratum.

Choose formation weights in the limiting form

\[
r^{(0)}
=
(1,0,\ldots,0).
\]

Only the first mode determines the global reciprocal weights.

For one weighted mode,

\[
\alpha
=
\frac{y_1^2}{1+y_1^2}.
\]

Choose

\[
\alpha_0=0.3.
\]

Then

\[
y_1
=
\sqrt{\frac{\alpha_0}{1-\alpha_0}},
\]

and therefore

\[
\boxed{
h_1^\star
=
-\frac12
\log\frac{\alpha_0}{1-\alpha_0}
\approx0.42364893019.
}
\]

At this anchor the global reciprocal weight is exactly \(\alpha_0\).

The first coordinate target is chosen as its exact BFG phase readout.

For every secondary coordinate \(i=2,\ldots,n\), choose the common target

\[
h_{{\rm read},i}=1.45.
\]

Because the secondary zero-weight modes do not alter \(\alpha_0\), each secondary
coordinate independently admits the three roots listed above.

Hence the full decoupled system has exactly the Cartesian-product family

\[
\boxed{
3^{\,n-1}
}
\]

of distinct anchor solutions.

---

## 4. Nondegeneracy of every product branch

At the zero-secondary-weight construction the anchor Jacobian is triangular.

The first diagonal derivative is numerically

\[
\boxed{
\partial_{h_1}F_1
\approx0.63219\ne0.
}
\]

Every secondary diagonal derivative is one of

\[
0.26064,\qquad -0.08646,\qquad 0.04898,
\]

all nonzero.

Therefore the full Jacobian determinant is nonzero at **every** one of the

\[
3^{n-1}
\]

product branches.

Each branch is an isolated regular preimage.

---

## 5. Positive-coupling persistence theorem

Replace the limiting weights by

\[
\boxed{
r^{(\varepsilon)}
=
(1,\varepsilon,\ldots,\varepsilon),
\qquad
\varepsilon>0.
}
\]

The coupled BFG readout depends smoothly on \(\varepsilon\).

Since every \(\varepsilon=0\) product solution has invertible Jacobian, the implicit
function theorem gives, for every fixed finite \(n\), an \(\varepsilon_n>0\) such that
for

\[
0<\varepsilon<\varepsilon_n
\]

all

\[
\boxed{
3^{\,n-1}
}
\]

branches persist as distinct smooth solutions.

Thus the exponential multiplicity does **not** rely on exactly zero formation weight.

It occurs for strictly positive formation weights.

This is the main global branch-growth theorem.

---

## 6. Deterministic finite verification

The implementation verifies the construction at

\[
\varepsilon=10^{-6}
\]

for:

\[
n=2:\quad 3\text{ branches},
\]

\[
n=3:\quad 9\text{ branches},
\]

\[
n=4:\quad 27\text{ branches},
\]

\[
n=5:\quad 81\text{ branches}.
\]

These are internal mathematical checks of the constructive theorem, not empirical
observations.

---

## 7. Memory information lower bound

To distinguish \(N\) simultaneous continuation branches using a fixed binary code
requires at least

\[
\lceil\log_2N\rceil
\]

bits.

With

\[
N_n\ge3^{n-1},
\]

the BFG continuation memory therefore satisfies the constructive lower bound

\[
\boxed{
b_n
\ge
\left\lceil
(n-1)\log_2 3
\right\rceil.
}
\]

So the required branch information grows at least linearly with mode dimension in
this family.

Examples:

\[
n=2:\ b_n\ge2,
\]

\[
n=3:\ b_n\ge4,
\]

\[
n=4:\ b_n\ge5,
\]

\[
n=5:\ b_n\ge7.
\]

---

## 8. Memory graph

At fixed finite dimension and away from singular values, the inverse continuation
structure can be represented as a finite branch graph.

### Nodes

A node is a locally invertible continuation sheet

\[
\mathcal B_k.
\]

### Fold edges

At a simple fold, two local sheets meet.

The lifted forward trajectory does not randomly switch; the incoming sheet continues
through the fold in the anchor representation.

### Event edges

Selection, R4 rank change, formation seeding, or terminal gates induce exact BFG
cross-stratum edges.

### Readout collisions

Different graph nodes may have the same reduced pair

\[
(X,\Omega).
\]

The memory coordinate \(M_b\) identifies the node.

Thus the local continuum state is

\[
\boxed{
(X,\Omega,M_b).
}
\]

---

## 9. Finite per finite regular chart, not uniformly finite globally

For a fixed finite mode dimension and a fixed regular readout, the observed branch set
is finite on the regular branch charts considered here.

The theorem above proves something different and stronger globally:

\[
\boxed{
\text{there is no dimension-independent finite upper bound on branch multiplicity.}
}
\]

For every proposed finite branch-label set of size \(N\), choose \(n\) large enough
that

\[
3^{n-1}>N.
\]

Then the constructive BFG commuting stratum contains a readout requiring more than
\(N\) continuation labels.

Therefore \(M\) cannot be a universal finite-state automaton with a fixed number of
states if the BFG state space admits unbounded finite mode dimension.

---

## 10. Relation to finite BFG orbit dimension

The sharper carrier theorem gives

\[
\boxed{
d_{k+1}\le d_k,
\qquad
p_k\le d_k\le d_0.
}
\]

Hence every orbit starting from a finite carrier has a uniform carrier and persistence
rank bound fixed by the initial dimension.

Therefore the exponential branch lower bound across **different dimensions** does not
imply unbounded branch-memory growth along one fixed finite-carrier orbit.

For fixed dimension, the later o-minimal analysis establishes a uniform bound on every
finite inverse fiber, while the reciprocal-alpha reduction shows that any
positive-dimensional full-persistent commuting load fiber is at most one-dimensional.

See `CARRIER_DIMENSION_MONOTONICITY_THEOREM.md`,
`FIXED_DIMENSION_MEMORY_TAMENESS.md`, and
`RECIPROCAL_ALPHA_FIBER_REDUCTION.md`.

---

## 11. Current memory classification

The mathematically justified hierarchy is now:

### Scalar/isotropic chart

No branch memory beyond \(\Omega\).

### Isolated simple fold

One local bit.

### Finite-dimensional multi-fold chart

A finite branch/chart identifier for each regular readout.

### Arbitrary finite dimension

No universal finite branch-state bound; the constructive lower bound is exponential:

\[
N_n\ge3^{n-1}.
\]

### One exact orbit from finite initial carrier

Carrier dimension and persistent rank are uniformly bounded by the initial carrier.

For every **finite** inverse fiber, the discrete continuation-branch count is uniformly
bounded at fixed dimension by the later o-minimal tameness theorem.

In the full-persistent commuting load sector, any positive-dimensional inverse fiber is
at most one-dimensional and can be represented by reciprocal \(lpha\) plus a finite
sheet label.

Thus unbounded discrete branch-count memory is not supported along one fixed finite
orbit. The remaining open issue is whether dynamically inequivalent
positive-dimensional fibers actually occur, and how the corresponding continuous
memory coordinate generalizes beyond the commuting locked sector.

---

## 12. Consequence

BFG memory persistence should not be modeled as a fixed universal finite-state switch.

The current mathematics instead supports a variable-complexity continuation memory:

\[
\boxed{
M_b\in\mathcal B(X,\Omega),
}
\]

where the branch set depends on the current stratum.

The global branch-growth theorem therefore constrains memory across **families of
increasing finite dimension**, while the later carrier/tameness results control one
fixed finite orbit.

The remaining memory problem is no longer unlimited discrete branch growth. It is the
existence and dynamical relevance of positive-dimensional continuation fibers and their
extension beyond the full-persistent commuting sector.
