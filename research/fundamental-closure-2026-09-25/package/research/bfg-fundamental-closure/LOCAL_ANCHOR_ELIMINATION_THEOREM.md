# Local Anchor Elimination and the Memory-Branch Criterion

## 1. Source alignment

The full BFG state already contains recursive phase \(\Omega\) and memory persistence
\(M\). The AGC specialization also introduces a phase-sensitive Closure Phase Operator
and a Recursive Persistence Channel of the form

\[
M_{\rm geo}(t+\Delta t)
=
F(M_{\rm geo}(t),C_{\rm geo}(t),\text{boundary state},\text{internal phase}),
\]

with \(M_{\rm geo}\) explicitly described as the channel that retains information about
the prior admissible state.

The source gives the **role** of phase and memory, but it does not provide a universal
closed form for \(F\).

This document determines exactly when the explicit committed anchor introduced in the
previous suspension can be eliminated mathematically.

---

## 2. General suspension setting

Let

\[
\mathcal U:\mathcal X\to\mathcal X
\]

be the committed discrete BFG update on one no-event stratum.

Let

\[
\mathcal I_\omega:\mathcal X\to\mathcal X,
\qquad
0\le\omega\le1,
\]

be a chosen within-step suspension satisfying

\[
\mathcal I_0(X)=X,
\]

\[
\mathcal I_1(X)=\mathcal U(X).
\]

The previous anchor formulation used

\[
X_{\rm read}
=
\mathcal I_\omega(X_\star).
\]

The question is whether \(X_\star\) must be carried as an independent state variable.

---

## 3. Local anchor-elimination theorem

Fix a phase

\[
\omega\in[0,1).
\]

Suppose the anchor-to-readout map

\[
X_\star\mapsto\mathcal I_\omega(X_\star)
\]

is locally invertible at the current anchor.

Equivalently, in finite coordinates,

\[
\boxed{
\det D_{X_\star}\mathcal I_\omega\ne0.
}
\]

Then by the inverse function theorem there is a local reconstruction map

\[
\boxed{
\mathcal R_\omega
=
\mathcal I_\omega^{-1}
}
\]

on a neighborhood of the current readout.

Therefore

\[
X_\star
=
\mathcal R_\omega(X)
\]

can be recovered from the instantaneous pair

\[
(X,\omega).
\]

The explicit anchor is not a fundamental state variable on this chart.

---

## 4. Anchor-free local vector field

Let recursive phase advance at the declared rate

\[
\boxed{
\dot\omega
=
\nu
=
\frac1{\log2}.
}
\]

Along one suspension step,

\[
X(\tau)=\mathcal I_{\omega(\tau)}(X_\star).
\]

The anchor is constant between commit events.

Differentiate:

\[
\dot X
=
\nu\,
\partial_\omega
\mathcal I_\omega(X_\star).
\]

Using local anchor reconstruction,

\[
X_\star=\mathcal R_\omega(X),
\]

we obtain the anchor-free local equation

\[
\boxed{
\dot X
=
\frac1{\log2}
\,
\partial_\omega
\mathcal I_\omega
\left(
\mathcal R_\omega(X)
\right),
}
\]

\[
\boxed{
\dot\omega
=
\frac1{\log2}.
}
\]

This is a genuine local state law on the phase-extended chart

\[
(X,\omega).
\]

No separately stored anchor is required there.

---

## 5. Scalar/isotropic BFG theorem

For the selected scalar closure-depth variable

\[
h=-\log y,
\qquad
h\ge0,
\]

let the committed discrete update be

\[
F_H(h)
=
2h-\log2
+
2\log(1+e^{-h})
+
\log(1+e^{-2h}).
\]

The adopted closure-depth suspension is

\[
\boxed{
G_\omega(a)
=
(1-\omega)a
+
\omega F_H(a),
}
\]

where \(a\) is the step anchor.

The derivative is

\[
\frac{\partial G_\omega}{\partial a}
=
(1-\omega)
+
\omega F_H'(a),
\]

with

\[
F_H'(a)
=
2
-
\frac2{e^a+1}
-
\frac2{e^{2a}+1}.
\]

For

\[
a>0,
\]

\[
F_H'(a)>0.
\]

At

\[
a=0,
\]

\[
F_H'(0)=0.
\]

Hence for every

\[
0\le\omega<1,
\]

\[
\boxed{
\frac{\partial G_\omega}{\partial a}
\ge1-\omega>0.
}
\]

Therefore \(G_\omega\) is strictly increasing and globally invertible on
\([0,\infty)\).

The anchor is uniquely reconstructible from the current pair

\[
(h,\omega).
\]

So the scalar/isotropic phase-extended BFG continuum is **globally anchor-free inside
each open step**.

---

## 6. Explicit scalar local law

Let

\[
a
=
G_\omega^{-1}(h).
\]

Then

\[
h(\tau)
=
G_{\omega(\tau)}(a).
\]

Therefore

\[
\boxed{
\dot h
=
\frac{
F_H(a)-a
}{
\log2
},
}
\]

\[
\boxed{
\dot\omega
=
\frac1{\log2}.
}
\]

In the original load variable

\[
y=e^{-h},
\]

\[
\boxed{
\dot y
=
-
\frac y{\log2}
\left[
F_H(a)-a
\right].
}
\]

The anchor \(a\) is not stored: it is reconstructed from \((h,\omega)\).

The implementation performs this reconstruction by monotone bisection.

---

## 7. Why phase \(\Omega\) is genuinely required

If phase is omitted, the same current closure depth can lie on different suspension
steps at different within-step phases.

Take a fixed current value \(h\) and two phases

\[
\omega_1\ne\omega_2.
\]

Because each \(G_{\omega_i}\) is invertible, there are unique anchors

\[
a_i=G_{\omega_i}^{-1}(h).
\]

Generically,

\[
a_1\ne a_2.
\]

Their tangent velocities are

\[
v_i
=
\frac{
F_H(a_i)-a_i
}{
\log2
}.
\]

Generically,

\[
\boxed{
v_1\ne v_2.
}
\]

Thus the reduced scalar value \(h\) alone does not determine a unique future tangent.

The recursive phase coordinate is therefore not optional bookkeeping in the continuum
description.

It is the minimal variable that resolves this ambiguity in the scalar stratum.

---

## 8. General memory-branch criterion

The inverse-function theorem gives a local criterion.

### Anchor-free chart

If

\[
D_{X_\star}\mathcal I_\omega
\]

is invertible, then

\[
(X,\omega)
\]

is locally sufficient.

No independent memory branch is mathematically necessary.

### Singular or non-injective chart

Suppose two distinct anchors satisfy

\[
X_\star^{(1)}\ne X_\star^{(2)},
\]

but

\[
\mathcal I_\omega(X_\star^{(1)})
=
\mathcal I_\omega(X_\star^{(2)})
=
X,
\]

while

\[
\partial_\omega
\mathcal I_\omega(X_\star^{(1)})
\ne
\partial_\omega
\mathcal I_\omega(X_\star^{(2)}).
\]

Then no single-valued vector field

\[
\dot X=V(X,\omega)
\]

can reproduce both histories.

Therefore some additional branch variable is required.

This is precisely the mathematical role that BFG's memory-persistence coordinate
\(M\) is capable of carrying.

The minimum requirement is not that \(M\) store the whole historical state. It need
only distinguish the equivalence classes of anchors that are collapsed by the
readout map.

---

## 9. Memory quotient

At fixed \((X,\omega)\), define an equivalence relation on anchors by

\[
X_\star\sim_\omega X_\star'
\iff
\mathcal I_\omega(X_\star)
=
\mathcal I_\omega(X_\star').
\]

If all representatives of one equivalence class also have the same phase derivative,
then the class causes no dynamical ambiguity.

If a class contains different derivatives, define the **continuation branches**

\[
[X_\star]_{\omega,\dot X}.
\]

A minimal memory variable need only label these distinct continuation branches.

Thus one may write schematically

\[
\boxed{
M
=
\text{continuation-branch label}
}
\]

rather than

\[
M=X_\star
\]

as a full anchor copy.

This is a strictly smaller conceptual role.

---

## 10. Local state equation with memory only when necessary

The phase-extended local BFG continuum therefore takes the stratified form

\[
\boxed{
\dot X
=
\mathcal V_{\rm BFG}(X,\Omega,M),
}
\]

\[
\boxed{
\dot\Omega
=
\frac1{\log2}.
}
\]

On an injective chart,

\[
M
\]

is dynamically redundant and may be omitted or kept constant.

On a non-injective chart, \(M\) selects the admissible continuation branch.

At an exact BFG event surface, the discrete event map updates the stratum and may also
update/reset the memory branch.

---

## 11. What the source does and does not provide

The source BFG architecture already treats:

- \(\Omega\) as recursive phase;
- \(M\) as memory persistence;
- process-sensitive closure as a legitimate BFG layer;
- \(M_{\rm geo}\) as a function of prior persistence, closure, boundary state and
  internal phase.

But the source leaves the function

\[
F
\]

in

\[
M_{\rm geo}(t+\Delta t)
=
F(M_{\rm geo}(t),C_{\rm geo}(t),\text{boundary},\text{phase})
\]

unspecified.

Therefore the source supports the **need and role** of a memory channel but does not
uniquely determine the branch-update law required by the present continuum completion.

---

## 12. Current conclusion

The explicit committed anchor is not generally fundamental.

The sharper result is

\[
\boxed{
\text{anchor can be eliminated exactly on every locally invertible suspension chart}.
}
\]

The true continuum state requirement is

\[
\boxed{
(X,\Omega)
}
\]

where the suspension is invertible, and

\[
\boxed{
(X,\Omega,M)
}
\]

only where continuation branches remain dynamically distinct.

For the scalar/isotropic selected BFG sector, \((Y,\Omega)\) is already sufficient.

For the full noncommuting rank-preserving state, local invertibility must now be
tested stratum by stratum.

Rank-changing events remain outside the smooth chart and are handled by the exact BFG
event map.


## 13. Constructive two-mode memory-branch counterexample

The coupled commuting multi-mode suspension is not globally invertible.

Take formation weights

\[
r=(0.11560491,\ 0.81916805)
\]

and phase

\[
\boxed{\omega=0.86}.
\]

The following three distinct selected closure-depth anchors are:

\[
a^{(1)}
=
(0.5477780109900522,\ 0.10675283802139944),
\]

\[
a^{(2)}
=
(1.292136408510817,\ 0.09571786689741645),
\]

\[
a^{(3)}
=
(2.7981030718815405,\ 0.08968102378697691).
\]

Their load coordinates are all strictly selected:

\[
e^{-a_i^{(k)}}\in(0,1).
\]

Under the coupled BFG endpoint rule and the adopted closure-depth suspension, all
three map at the same phase to

\[
\boxed{
h_{\rm read}
\approx
(1.27649265340182,\ 1.21855180171112).
}
\]

But their recursive-time tangents are respectively

\[
v^{(1)}
\approx
(1.22245698,\ 1.86510099),
\]

\[
v^{(2)}
\approx
(-0.02624322,\ 1.88361273),
\]

\[
v^{(3)}
\approx
(-2.55258117,\ 1.89373985).
\]

Therefore

\[
\boxed{
(h_{\rm read},\omega)
}
\]

does not determine a unique tangent.

This is a constructive BFG-internal memory-branch no-go.

No deterministic local law

\[
\dot h=V(h,\omega)
\]

can reproduce all three continuations.

A branch variable is mathematically required.

---

## 14. Fold surface

The same example contains a singular anchor-to-readout Jacobian.

At

\[
a
=
(1.2921364085108027,\ 0.09571786689741542)
\]

the Jacobian determinant changes sign near

\[
\boxed{
\omega_{\rm fold}
\approx
0.8283584507952344.
}
\]

A finite-difference singular-value audit gives one singular value of order

\[
10^{-11}
\]

at the located fold.

Thus the three-branch behavior is not an arbitrary numerical coincidence. It is
associated with an actual fold of the chosen suspension map.

The exact numerical values are internal mathematical diagnostics, not empirical data.

---

## 15. Minimal memory law

The fold result changes the state requirement.

A full stored anchor is excessive, but \((X,\Omega)\) is globally insufficient.

The minimal continuation state is

\[
\boxed{
(X,\Omega,M_b),
}
\]

where

\[
M_b
\]

is a **continuation-branch label**.

On each locally invertible branch,

\[
X_\star
=
\mathcal R_{\Omega,M_b}(X).
\]

Then

\[
\boxed{
\dot X
=
\frac1{\log2}
\partial_\Omega
\mathcal I_\Omega
\left(
\mathcal R_{\Omega,M_b}(X)
\right).
}
\]

Between branch events, the minimal persistence rule is

\[
\boxed{
\dot M_b=0,
}
\]

meaning: continue on the same admissible sheet.

A branch switch is permitted only when the current sheet ceases to be admissibly
continuable or an exact BFG event map requires a change.

This **branch-continuity rule** is a new BFG continuum completion principle. It is
motivated by the source role of memory persistence but is not already fixed by the
source's generic \(M\)-update equation.
