# Fixed-Dimension Memory Tameness Theorem

## 1. Purpose

Two earlier results must be combined correctly:

1. across increasing finite mode dimension, the current continuum completion admits at
   least
   \[
   3^{d-1}
   \]
   continuation branches for suitable \(d\)-mode strata;

2. along one exact orbit starting from a finite carrier,
   \[
   d_{n+1}\le d_n\le d_0.
   \]

The remaining question is:

> At one fixed finite dimension \(d\), can the number of discrete continuation
> branches become arbitrarily large as state, phase, and readout vary?

For the finite-fiber part of the current commuting suspension family, standard
o-minimal mathematics says no.

---

## 2. Definability of the commuting suspension

In closure-depth coordinates

\[
h_i>0,
\qquad
y_i=e^{-h_i},
\]

the reciprocal loads are

\[
\Lambda_C
=
\sum_i\frac{r_i}{1+e^{-h_i}},
\]

\[
\Lambda_B
=
\sum_i
\frac{r_i e^{-2h_i}}{1+e^{-h_i}}.
\]

Then

\[
\alpha
=
\frac{\Lambda_B}
{\Lambda_C+\Lambda_B},
\qquad
\beta=1-\alpha,
\]

and

\[
y_i^+
=
\frac{
\alpha+\beta e^{-2h_i}
}{
(1+e^{-h_i})^2
}.
\]

The endpoint depth is

\[
H_{+,i}
=
-\log y_i^+.
\]

For phase

\[
0<\omega<1,
\]

the declared continuum readout is

\[
F_{d,i}(h;r,\omega)
=
(1-\omega)h_i
+
\omega H_{+,i}(h;r).
\]

Every operation appearing here is built from:

- field operations;
- order;
- exponentiation;
- logarithm on the positive reals, which is definable as the inverse of exponentiation.

Therefore the graph of

\[
F_d
\]

is definable in the real exponential field

\[
\mathbb R_{\exp}.
\]

---

## 3. Known mathematical input

Wilkie's theorem states that the real exponential field is o-minimal.

A standard consequence of o-minimal cell decomposition is uniform control of fibers:
for a fixed definable map/family, the number of connected components of every fiber is
bounded by one finite constant depending only on the definable family.

In particular, if all fibers under consideration are finite, their cardinalities have
one uniform finite upper bound.

These are **known mathematical theorems**, not new BFG results.

---

## 4. Uniform finite-branch theorem at fixed dimension

Fix one finite dimension \(d\).

Consider the definable family of anchor fibers

\[
\mathcal F_{r,\omega,x}
=
\left\{
h\in(0,\infty)^d:
F_d(h;r,\omega)=x
\right\},
\]

with parameters

\[
r_i>0,
\qquad
0<\omega<1,
\qquad
x\in\mathbb R^d.
\]

Restrict attention to parameter values for which the anchor fiber is finite.

Uniform finiteness gives a number

\[
\boxed{
B_d<\infty
}
\]

such that

\[
\boxed{
|\mathcal F_{r,\omega,x}|
\le B_d
}
\]

for every finite fiber in this \(d\)-mode family.

No explicit sharp value of \(B_d\) is obtained from the general o-minimal theorem.

---

## 5. Compatibility with the exponential lower bound

The constructive global-memory theorem already gives finite fibers with at least

\[
3^{d-1}
\]

points.

Therefore any valid uniform upper bound must satisfy

\[
\boxed{
B_d\ge3^{d-1}.
}
\]

So fixed-dimensional branch memory is finite on finite fibers, but its worst-case bound
grows at least exponentially with dimension.

There is no contradiction:

- fixed \(d\): finite uniform bound;
- variable \(d\): no dimension-independent finite bound.

---

## 6. Consequence for one finite initial orbit

Let the initial carrier dimension be

\[
d_0<\infty.
\]

Carrier monotonicity gives

\[
d_n\le d_0.
\]

For every finite-fiber continuum chart encountered by that orbit, define

\[
B_{\le d_0}
=
\max_{1\le d\le d_0}B_d.
\]

Since this is a maximum of finitely many finite integers,

\[
\boxed{
B_{\le d_0}<\infty.
}
\]

Therefore along every portion of the orbit whose suspension fibers remain finite,

\[
\boxed{
\text{the number of discrete continuation branches is uniformly bounded.}
}
\]

Consequently a finite branch identifier requires at most

\[
\boxed{
\left\lceil
\log_2 B_{\le d_0}
\right\rceil
}
\]

binary bits on those finite-fiber charts.

The theorem is qualitative because \(B_d\) is not explicitly known.

---

## 7. What is now ruled out

For one fixed finite initial carrier, the following mechanism is ruled out:

\[
\text{iteration}
\to
\text{larger and larger carrier}
\to
\text{larger and larger finite branch set}
\to
\text{unbounded discrete memory}.
\]

Carrier growth is impossible.

The following mechanism is also ruled out on finite fibers:

\[
\text{fixed dimension}
\to
\text{arbitrarily many isolated finite preimages}.
\]

O-minimal uniform finiteness prevents it for the fixed definable family.

Thus **unbounded discrete branch-count memory is not available along a fixed finite
orbit while the relevant inverse fibers remain finite.**

---

## 8. The only remaining memory singularity

O-minimality bounds the number of **connected components** of all fibers, including
singular ones.

But a connected fiber can itself have positive dimension.

If

\[
\dim\mathcal F_{r,\omega,x}>0,
\]

then infinitely many anchors share the same readout and phase.

Two cases are possible.

### Dynamically equivalent component

If the phase derivative is constant over that component, the whole component represents
one continuation law and no continuous memory coordinate is needed.

### Dynamically inequivalent component

If

\[
\partial_\omega F_d(h;r,\omega)
\]

varies along the positive-dimensional fiber, then the current readout plus a finite
branch label cannot determine the tangent.

A continuous memory coordinate is then required.

Therefore the last route to genuinely non-finite memory is

\[
\boxed{
\text{positive-dimensional inverse fiber with dynamically distinct tangents}.
}
\]

---

## 9. Refined memory hierarchy

For a finite initial carrier, the current continuum completion now gives:

### Regular injective chart

No \(M_b\).

### Finite multi-branch chart

Finite branch label, uniformly bounded at fixed \(d_0\).

### Simple fold / finite singularity

Finite local sheet label.

### Positive-dimensional dynamically equivalent fiber

One continuation class despite infinitely many anchors.

### Positive-dimensional dynamically inequivalent fiber

A continuous memory coordinate is required.

This is the only currently unresolved route to non-finite continuation memory for one
fixed finite initial carrier.

---

## 10. Relation to full-persistence lock

If an orbit reaches

\[
P=I,
\qquad
0<Y<I,
\]

the carrier and persistence rank are locked.

The subsequent load dynamics is a fixed-dimensional definable family with fixed
formation density in the gauge-aligned full-persistent description.

Thus the long-term memory question in this locked regime is entirely an
inverse-fiber-geometry question at fixed dimension.

No further rank-growth mechanism remains.

---

## 11. Current conclusion

The memory question is now much narrower than before.

For one finite initial BFG state:

\[
\boxed{
\text{carrier dimension is uniformly bounded}
}
\]

and, on finite inverse fibers,

\[
\boxed{
\text{discrete continuation-branch count is uniformly bounded}.
}
\]

So unbounded finite-state memory growth is not supported by the current mathematics.

The only unresolved possibility is a positive-dimensional inverse fiber carrying
different continuation tangents.

The next exact task is therefore:

> Determine whether such dynamically inequivalent positive-dimensional fibers can occur
> in the admissible BFG suspension family.

If they are impossible, finite initial BFG states have finite continuation-memory
complexity under the current continuum completion.
