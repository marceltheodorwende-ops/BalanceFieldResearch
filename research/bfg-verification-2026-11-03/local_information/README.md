# Local admissible profiles and information-operator reconstruction

Date: 3 November 2026. Continuation of the BFG-Engine source synthesis; no new paper, physical law or initialization default.

## 1. Result

For the plugin's existing relation `I[s]=s* J s`, a Hermitian information operator on a **specified finite complex Hilbert carrier** is uniquely determined by its functional values in any open neighborhood of a unit formed profile. Large departures from the formed profile are not mathematically necessary. We give an explicit n^2-profile construction arbitrarily close to that profile.

This result needs both admissible access to those profiles and their information-functional values. It does not generate the values from the one formed minimum. Nor does it automatically promote a real formation carrier into a complex Hilbert sector. Real-only profiles leave complex imaginary components invisible.

The source balance formula gives a second conditional route: exact balance on such an open profile neighborhood can fix J from the other supplied operators in the appropriate Hermitian sector. A finite balance tolerance generally gives a family rather than a unique J.

## 2. Constructive local reconstruction

Choose an orthonormal frame with formed unit vector e_0, and let t>0. Use the following **normalized** profiles:

```math
e_0;\quad
\frac{e_0\pm t e_j}{\sqrt{1+t^2}},\quad
\frac{e_0+\mathrm i t e_j}{\sqrt{1+t^2}}\quad(1\le j<n);
```

and for every 1<=j<k<n,

```math
\frac{e_0+t(e_j+e_k)}{\sqrt{1+2t^2}},\qquad
\frac{e_0+t e_j+\mathrm i t e_k}{\sqrt{1+2t^2}}.
```

Their number is `1+3(n-1)+(n-1)(n-2)=n^2`. Every profile lies at Hilbert-norm distance at most sqrt(2)t from e_0: for a transverse w, the squared normalized-profile distance is `2-2/sqrt(1+||w||^2)<=||w||^2`, and ||w||<=sqrt(2)t. Thus the entire family fits inside any prescribed open neighborhood by taking t small enough. This is a coordinate construction; a unitary change of frame transforms J and the profiles together.

Write q(s)=I[s] and recover unnormalized evaluations by

```math
r(w)=(1+\|w\|^2)q((e_0+w)/\sqrt{1+\|w\|^2})=q(e_0+w).
```

Set a=q(e_0), r_j^+=r(t e_j), r_j^-=r(-t e_j), r_j^i=r(i t e_j). Then

```math
J_{00}=a,\qquad
J_{jj}=\frac{r_j^++r_j^--2a}{2t^2},
```

```math
\operatorname{Re}J_{0j}=\frac{r_j^+-r_j^-}{4t},\qquad
\operatorname{Im}J_{0j}=\frac{(r_j^++r_j^-)/2-r_j^i}{2t}.
```

For a transverse pair j<k, define r_jk^+=r(t(e_j+e_k)) and r_jk^i=r(t e_j+i t e_k). Expansion gives

```math
\operatorname{Re}J_{jk}
=\frac{r_{jk}^+-a-2t(\operatorname{Re}J_{0j}+\operatorname{Re}J_{0k})-t^2(J_{jj}+J_{kk})}{2t^2},
```

```math
\operatorname{Im}J_{jk}
=\frac{a+2t\operatorname{Re}J_{0j}-2t\operatorname{Im}J_{0k}+t^2(J_{jj}+J_{kk})-r_{jk}^i}{2t^2}.
```

Together with Hermitian symmetry these formulas recover every entry. They prove that the associated profile projectors span Herm(n), and therefore prove the open-neighborhood identifiability claim. No quantum measurement postulate or new BFG law is used. The frame directions and evaluable functional are assumed available; their physical accessibility is not inferred from the algebra.

## 3. Real versus complex admissibility

If only real profiles are allowed, a Hermitian J=A+iB has real symmetric A and real skew-symmetric B, and

```math
s^*Js=s^T A s\quad(s\in\mathbb R^n).
```

All of B is invisible. An open real profile set can determine A but leaves n(n-1)/2 real imaginary parameters unresolved in the general complex Hermitian problem. If the intended category is genuinely real symmetric, there is no missing imaginary sector and local real reconstruction is sufficient for that category.

For n=2, `J_a=I` and `J_b=I+(1/2)[[0,i],[-i,0]]` are different positive definite Hermitian operators with the same functional value on **every real unit profile**. They differ on complex profiles. The September formation source's real finite profile sector cannot silently be used to claim full complex operator identification without a justified complex-sector bridge.

If profiles occupy only a complex subspace V of dimension r<n, only the compression P_V J P_V is identifiable from all profiles in V. Its observable dimension is r^2, leaving n^2-r^2 real Hermitian directions invisible, including cross-block terms. This differs from the dimension of operators annihilating V in a vector residual cost; functional compression and full vector action are distinct observations.

## 4. What BFG admissibility does and does not grant

The Neutral Interface supplies approximate balance/interface bands and a quadratic information functional. The recursive-stability module additionally requires bounded iterates and Lyapunov control. Strict margins in finitely many continuous state inequalities give a neighborhood **within their already specified state domain**. They do not remove exact equality constraints, create missing state directions or prove dynamical reachability.

For a concrete source-type residual, take fixed `R=Pi+q(I-Pi)` with 0<q<1, N=I and e_0 spanning Pi. A normalized local profile e_0+w has residual

```math
\|(R-I)s\|^2=(1-q)^2\frac{\|w\|^2}{1+\|w\|^2}.
```

If the other Lyapunov terms have slack and the available residual-cost budget is L>0, all local probes above satisfy this part of the source corridor whenever

```math
2\lambda_R(1-q)^2t^2\le L.
```

This is an instantaneous, exact residual bound, not proof that the complete BFG evolution produces every probe or that the full action principle is minimized there. Any additional source terms and domain constraints must be checked separately. No new dynamics is inserted to make the profiles accessible.

There is also a spectral restriction. For fixed R, let `V_b={s:sup_m ||R^m s||<infinity}`. This is a linear subspace. If it contains an open unit-sphere neighborhood, it contains n independent vectors. Each has bounded iterates; expanding arbitrary unit vectors in that basis gives a finite uniform bound on ||R^m||. Hence R must be power bounded on the whole finite carrier. Conversely a power-bounded R imposes no further state exclusion through this boundedness test alone.

For `R=diag(1,2)`, V_b is only span(e_0). There is no full-carrier open admissible neighborhood, so the local reconstruction cannot use transverse profiles. For `R=diag(1,1/2)`, boundedness alone permits every direction, although other constraints may still restrict them. If admissibility is limited to the exact quartic minimizers +/-sqrt(-lambda_0)e_0, their normalized projectors span only one real dimension. Allowing admissible perturbations is a substantive domain condition, not a consequence of having a unique minimum.

## 5. A source-based exact-balance alternative

The source ratio is

```math
\Phi[s,N]=\frac{s^* E J s}{s^* B_{op} N s}.
```

In a sector where the two quadratic forms are Hermitian and the denominator is nonzero, exact Phi=1 on an open complex profile neighborhood implies `EJ=B_op N` by the same local identifiability theorem. If E is invertible, this forces

```math
J=E^{-1}B_{op}N.
```

The candidate must still be Hermitian/positive and satisfy all other specified constraints; arbitrary noncommuting products need not pass those checks. E, B_op and N remain supplied or separately derived inputs. This is a consequence of an **open set of exact balance**, not of balance at a single formed state.

Approximate balance is different. With E=B_op=N=I and `0<epsilon<1`, the requirement `|Phi(s)-1|<=epsilon` on every unit profile is equivalent, for Hermitian J, to

```math
(1-\epsilon)I\le J\le(1+\epsilon)I.
```

The Rayleigh-quotient bounds prove this equivalence. This contains infinitely many positive operators; the band alone does not specify their functional values. Thus even full-domain admissibility is not identical to knowing the information functional.

## 6. Exact uniqueness versus numerical sensitivity

For n=2 the normalized local measurement matrix in Hermitian coordinates has determinant

```math
\frac{8t^4}{(1+t^2)^3}>0\quad(t>0).
```

It is invertible for every nonzero t, but becomes poorly conditioned as probes approach the formed line. If each normalized information value has independent absolute error at most eta, the displayed reconstruction obeys

```math
|\Delta J_{11}|\le\frac{2+t^2}{t^2}\eta,\quad
|\Delta\operatorname{Re}J_{01}|\le\frac{1+t^2}{2t}\eta,\quad
|\Delta\operatorname{Im}J_{01}|\le\frac{1+t^2}{t}\eta.
```

The diagonal bound is attained by choosing both real-perturbed observation errors +eta and the central observation error -eta. For eta=10^-6, its bound is 0.000201 at t=1/10 but 0.020001 at t=1/100. These are arithmetic sensitivity examples, not empirical datasets. Arbitrarily local exact identifiability does not imply uniformly accurate reconstruction from noisy or finite-precision inputs.

## 7. Outcome for the origin program

The operator-reconstruction route no longer requires distant test profiles. It requires a sufficiently rich **allowed domain** and specified information-functional values, or the stronger exact-balance operator identity with independently given E/B_op/N. We have not established that the original first formation supplies either complete data packet.

The next missing implication is precise: does the source origin admit an open complex family and determine I[s] on it, or does it enforce exact balance on that family with all remaining operators fixed? A real-only or lower-dimensional domain gives only the corresponding compressed information. A tolerance corridor alone gives inequalities, not a unique operator. These are source obligations, not new physical rules adopted here.

The plugin's global module context and 20-reference inventory remain in the [synthesis](../plugin_synthesis/README.md). This step reuses that context and checks the specific information/admissibility clauses; it does not claim a new full audit of every bundled page. [SOURCES.json](SOURCES.json) pins its scope. Run `python local_information/check_local_information.py`; [results.json](results.json) records exact reconstructions, rank limits, residual bounds and error amplification. No paper, runtime or finite event is modified.
