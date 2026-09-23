# BFG Formation Robustness and Bifurcation Theorem

## 1. Scope

This theorem quantifies how far an active finite formation operator lies from a
change of formation status.

The formation gate uses two strict inequalities:

\[
\lambda_0(K_+)<-\varepsilon_{\rm sign},
\]

and

\[
\lambda_1(K_+)-\lambda_0(K_+)
>
\varepsilon_{\rm simple}.
\]

The result below is exact in the Hermitian operator \(2\)-norm of \(K_+\).

It is not yet a theorem giving the same radius directly in a parent-state norm
on \((K,Y,R,\rho)\), because perturbing a parent state can also rotate the
active packet subspace.

---

## 2. Signed gate clearances

Let

\[
\lambda_0\le\lambda_1\le\cdots
\]

be the eigenvalues of \(K_+\), and define

\[
s
=
-\varepsilon_{\rm sign}-\lambda_0,
\]

\[
g
=
(\lambda_1-\lambda_0)-\varepsilon_{\rm simple}.
\]

For a one-dimensional active support, set \(g=+\infty\).

Formation is admissible exactly when

\[
s>0
\qquad\text{and}\qquad
g>0.
\]

The two bifurcation surfaces are therefore

\[
s=0
\]

and

\[
g=0.
\]

---

## 3. Eligible-state robustness radius

Assume

\[
s>0,\qquad g>0.
\]

For any Hermitian perturbation \(E\), Weyl's inequality gives

\[
|\lambda_j(K_++E)-\lambda_j(K_+)|
\le
\|E\|_2.
\]

Hence the sign condition remains satisfied whenever

\[
\|E\|_2<s.
\]

For the ground-state gap,

\[
(\lambda_1'-\lambda_0')
\ge
(\lambda_1-\lambda_0)-2\|E\|_2,
\]

so the simplicity condition remains satisfied whenever

\[
\|E\|_2<\frac{g}{2}.
\]

Therefore every perturbation satisfying

\[
\|E\|_2
<
\min\left(s,\frac{g}{2}\right)
\]

preserves formation eligibility.

Both bounds are sharp:

- the sign boundary is reached by raising the ground eigendirection;
- the gap boundary is reached by raising the ground eigendirection and lowering
  the first excited eigendirection by equal amounts.

Thus

\[
\boxed{
d_{\rm form}
=
\min\left(
s,\frac{g}{2}
\right)
}
\]

is the exact Hermitian operator-norm distance from an eligible \(K_+\) to the
non-eligible set.

---

## 4. Ineligible-state distance to formation

Now assume at least one gate inequality fails.

Define the violations

\[
v_s=(-s)_+,
\]

\[
v_g=(-g)_+.
\]

Any perturbation entering the eligible set must change the ground eigenvalue by
at least \(v_s\), and must increase the ground gap by at least \(v_g\).

Since one operator-norm perturbation can change the two eigenvalues defining the
gap in opposite directions, the least possible norm needed to repair the gap is

\[
\frac{v_g}{2}.
\]

Therefore the infimum distance from an ineligible active operator to the
eligible set is

\[
\boxed{
d_{\bot\to{\rm form}}
=
\max\left(
v_s,\frac{v_g}{2}
\right).
}
\]

This lower bound is attained in the limit by perturbations aligned with the
lowest two eigendirections.

---

## 5. Signed formation margin

Define

\[
\boxed{
\mathfrak m_F(K_+)
=
\begin{cases}
\min(s,g/2), & s>0,\ g>0,\\[4pt]
-\max((-s)_+,(-g)_+/2), & \text{otherwise}.
\end{cases}
}
\]

Then

\[
\mathfrak m_F>0
\]

means formation is admissible, while

\[
\mathfrak m_F<0
\]

means the state is on the terminal side of the bifurcation surface.

Moreover,

\[
|\mathfrak m_F|
\]

is the exact active-operator distance to a formation-status change, interpreted
as distance to the complementary set for eligible states and infimum distance
to the eligible set for terminal states.

This gives the finite master runtime a quantitative formation stability
coordinate rather than only a binary gate.

---

## 6. Relation to Formation Eligibility

The previous Formation Eligibility Theorem gives the exact active spectrum
through the generalized pair

\[
\left(
V_r^\dagger A^\dagger(K\oplus K)AV_r,\,
V_r^\dagger A^\dagger A V_r
\right).
\]

The present theorem acts on that spectrum.

Thus the finite sequence is now

\[
(K,Y,R,\rho)
\to
A
\to
\sigma(K_+)
\to
\mathfrak m_F
\to
\text{robust formation / robust terminal / boundary}.
\]

No carrier-specific threshold is introduced.

---

## 7. Current four-carrier audit

The margin audit was applied to all current first-step states:

\[
\boxed{1409/1409}
\]

reached the active formation operator.

For every state, a perturbation with norm \(0.99\) times the exact boundary
distance preserved the original formation status:

\[
\boxed{1409/1409}.
\]

A matching adversarial perturbation placed just beyond the nearest exact
boundary and changed the status in

\[
\boxed{1409/1409}.
\]

This is an executable check of the sharpness construction, not the source of the
theorem.

### Time-series carriers

All current first-step states remain eligible.

Their median active-operator formation margins are approximately:

\[
0.79345
\]

for annual Sunspots,

\[
0.80968
\]

for Mauna Loa CO2,

and

\[
0.75833
\]

for ENSO Pacific SST.

For all three time-series carriers the nearest bifurcation surface is the
simplicity surface rather than the sign surface.

### Relational network

The relational carrier has:

\[
13
\]

eligible probes and

\[
21
\]

terminal probes.

The nearest eligible network state has margin

\[
\boxed{
+0.0166927689
}
\]

and the nearest terminal network state has margin

\[
\boxed{
-0.0183398303.
}
\]

Across all 34 probes:

- 31 are sign-surface limited;
- 3 are simplicity-surface limited.

The successful network margins range from approximately

\[
0.01669
\]

to

\[
0.37860,
\]

while terminal margins range from approximately

\[
-0.13488
\]

to

\[
-0.01834.
\]

Thus the earlier `13/21` split now has not only an exact eligibility
explanation, but a quantitative robustness distance for every probe.

---

## 8. Claim boundary

The following is theorem-level for the adopted finite active formation operator:

\[
\boxed{
d_{\rm eligible\to terminal}
=
\min\left(
-\varepsilon_{\rm sign}-\lambda_0,\,
\frac{\lambda_1-\lambda_0-\varepsilon_{\rm simple}}{2}
\right)
}
\]

whenever the state is eligible.

The corresponding ineligible-to-eligible infimum is

\[
\boxed{
d_{\rm terminal\to eligible}
=
\max\left(
(\lambda_0+\varepsilon_{\rm sign})_+,\,
\frac{
(\varepsilon_{\rm simple}-(\lambda_1-\lambda_0))_+
}{2}
\right).
}
\]

The theorem does **not** yet claim an identical radius in a norm of the parent
variables \((K,Y,R,\rho)\). Such a result additionally requires perturbation
control of the packet subspace \(U_r\), or equivalently the state-to-active-space
map.

That parent-state transport bound is the next mathematical extension.
