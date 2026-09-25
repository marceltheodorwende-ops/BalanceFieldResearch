# Simple-Fold Memory Theorem and Branch-Continuity Rule

## 1. Question

The coupled two-mode suspension already provides a constructive memory-branch
counterexample: distinct anchors can produce the same current readout and recursive
phase while requiring different tangents.

The next question is local:

> Is the first singularity a generic simple fold, and if so how much memory is
> minimally required near it?

The answer is yes: the deterministic fold previously identified is a generic
corank-one Whitney fold to numerical certification.

---

## 2. Fold map

Fix the two-mode formation weights

\[
r=(0.11560491,\ 0.81916805)
\]

and use the closure-depth suspension

\[
F(a,\omega)
=
(1-\omega)a
+
\omega H_+(a),
\]

where \(H_+(a)\) is the coupled commuting BFG endpoint in closure-depth coordinates.

At

\[
a_f
=
(1.2921364085108027,\ 0.09571786689741542)
\]

and

\[
\omega_f
\approx0.8283584507952344,
\]

the anchor Jacobian

\[
D_aF(a_f,\omega_f)
\]

has singular values approximately

\[
\boxed{
(0.84798398,\ 1.6\times10^{-11})
}.
\]

Thus the rank drops by exactly one.

---

## 3. Simple-fold nondegeneracy

Let \(v\) be the right null direction and \(\ell\) the left null direction of
\(D_aF\).

Numerically,

\[
v
\approx
(-0.99996956,\ 0.00780292),
\]

\[
\ell
\approx
(-0.41986534,\ 0.90758641).
\]

The projected quadratic curvature is

\[
\boxed{
\ell^T D_a^2F[v,v]
\approx
8.59\times10^{-3}
\ne0.
}
\]

This is the standard nondegeneracy condition for a simple fold.

The recursive phase also unfolds the singularity transversely:

\[
\boxed{
\ell^T\partial_\omega F
\approx1.1926
\ne0,
}
\]

and the determinant crosses zero with

\[
\boxed{
\frac d{d\omega}
\det D_aF
\approx-0.437
\ne0.
}
\]

Therefore this is not a higher-order cusp or an accidental flat singularity.

---

## 4. Local Whitney normal form

By the standard fold theorem, after smooth local coordinate changes the map is
equivalent to the normal form

\[
\boxed{
(u,z)\mapsto(u,z^2)
}
\]

at fixed phase, with the recursive phase providing a transverse unfolding parameter.

Consequently, sufficiently near the fold:

- on one side of the fold image there are two local inverse sheets;
- on the fold they coalesce;
- on the other side there is no inverse in that local chart.

Thus a **single binary branch label is locally sufficient** to distinguish the two
nearby inverse sheets.

---

## 5. Local memory bit

Let \(v\) be the fold null direction. Define the signed sheet coordinate

\[
\mu
=
v^T(a-a_f).
\]

Then locally

\[
M_{\rm bit}
=
\begin{cases}
+1,&\mu>0,\\
-1,&\mu<0.
\end{cases}
\]

At

\[
\mu=0
\]

the two local sheets meet and the bit is observationally degenerate.

The bit is a local chart label. It is not a new physical binary degree of freedom.

---

## 6. The fold is not a BFG terminal event

The fold is a singularity of the **inverse anchor reconstruction**.

The original suspension

\[
F(a,\omega)
\]

remains smooth and well defined at the fold.

Therefore

\[
\boxed{
\text{fold}\not\Rightarrow\bot.
}
\]

No BFG terminal condition follows merely from

\[
\det D_aF=0.
\]

Exact terminality remains controlled by the previously declared BFG gates:
zero dual load, witness annihilation, no-choice formation failure, loss of selected
support, and related structural conditions.

---

## 7. No spontaneous branch switching

Because the full anchor-phase trajectory remains continuous through the fold, a
reduced memory description must preserve the incoming continuation sheet.

Thus the living continuum rule is:

\[
\boxed{
\text{follow the continuous lifted sheet; do not switch sheets merely because a fold is reached.}
}
\]

A branch change is allowed only when:

1. an exact BFG event map changes the stratum; or
2. the currently lifted branch loses admissibility and another continuation is
   uniquely selected by the declared no-choice rules.

This is the local operational content of the Memory-Continuity Principle.

---

## 8. Why one bit is only local

The earlier deterministic example at

\[
\omega=0.86
\]

has **three distinct anchors** mapping to one readout.

Therefore a single global binary bit cannot label all continuation histories at that
point.

A fixed binary code for three branches requires at least

\[
\boxed{
\lceil\log_2 3\rceil=2
}
\]

bits.

More invariantly, global memory must carry a branch/chart identifier

\[
M_b\in\mathcal B(X,\Omega)
\]

rather than one universal bit.

Near an isolated simple fold,

\[
|\mathcal B|=2
\]

and one bit is enough.

Across a larger state space, multiple folds can overlap in the same readout image, so
the number of continuation branches can exceed two.

---

## 9. Minimal global memory structure

The current minimal continuum memory is therefore not

\[
M=X_\star
\]

and not one universal binary variable.

It is

\[
\boxed{
M=(\text{branch chart},\text{local sheet label})
}
\]

with the chart information needed only where multiple local fold structures overlap.

On injective charts, \(M\) is redundant.

Near one simple fold, it reduces to one bit.

At multi-branch overlaps, the branch label must distinguish all dynamically distinct
continuations.

---

## 10. Current result

The continuum memory problem now has a precise hierarchy:

### Injective region

\[
(X,\Omega)
\]

is sufficient.

### Simple-fold neighborhood

\[
(X,\Omega,M_{\rm bit})
\]

is sufficient locally.

### Multi-fold / multi-branch region

\[
(X,\Omega,M_b)
\]

with a finite or countable branch label is required.

### Exact BFG event surface

Apply the discrete Selection/R4/formation/terminal event map; do not infer an event
from inverse-coordinate singularity alone.

This provides a continuity-preserving role for BFG memory \(M\) without inflating it
into storage of the complete historical state.
