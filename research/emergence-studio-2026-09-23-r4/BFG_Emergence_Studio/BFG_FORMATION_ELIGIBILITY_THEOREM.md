# BFG Formation Eligibility Theorem

## 1. Purpose

The finite master runtime admits formation only when the active successor
formation operator has a **simple negative lowest eigenvalue**.

The relational fourth carrier exposed a useful distinction:

- all 34 parent formation operators already possess a negative ground mode;
- only 13 of the 34 probes pass the active formation gate.

Therefore parent negativity alone is not the eligibility condition.

The missing object is the transport of the parent formation geometry through the
neutral/persistent packet.

---

## 2. Active packet

For a finite reduced master state define

\[
C=(I+Y)^{-1},
\qquad
B=Y(I+Y)^{-1},
\]

the \(G\)-orthogonal persistent projector \(P\), reciprocal weights
\(\alpha,\beta\), and

\[
A=
\begin{bmatrix}
\sqrt{\alpha}\,PC\\
\sqrt{\beta}\,PB
\end{bmatrix}.
\]

Let

\[
H=K\oplus K.
\]

Take the thin singular-value decomposition on the active support,

\[
A=U_r\Sigma_rV_r^\dagger,
\]

where every singular value in \(\Sigma_r\) is strictly positive.

The adopted finite master law forms

\[
\boxed{
K_+=U_r^\dagger H U_r.
}
\]

---

## 3. Exact generalized-eigenvalue criterion

Define on the active right support

\[
M
=
V_r^\dagger A^\dagger H A V_r,
\]

\[
N
=
V_r^\dagger A^\dagger A V_r.
\]

Using the SVD,

\[
M
=
\Sigma_r
U_r^\dagger H U_r
\Sigma_r
=
\Sigma_r K_+\Sigma_r,
\]

while

\[
N=\Sigma_r^2.
\]

Because \(\Sigma_r\) is invertible on the active support,

\[
Mx=\lambda Nx
\]

is equivalent, after setting \(y=\Sigma_r x\), to

\[
K_+y=\lambda y.
\]

Therefore

\[
\boxed{
\sigma_{\rm gen}(M,N)=\sigma(K_+).
}
\]

This is exact in finite dimension.

### Formation Eligibility Theorem

Let

\[
\lambda_0^{\rm gen}\le\lambda_1^{\rm gen}\le\cdots
\]

be the finite generalized eigenvalues of \((M,N)\).

Then the master formation gate is admissible exactly when

\[
\boxed{
\lambda_0^{\rm gen}<-\varepsilon_{\rm sign}
}
\]

and

\[
\boxed{
\lambda_1^{\rm gen}-\lambda_0^{\rm gen}
>
\varepsilon_{\rm simple}.
}
\]

For a one-dimensional active support, the gap is interpreted as infinite.

Thus formation eligibility can be certified directly from the parent state and
its neutral/persistent packet before committing a successor.

---

## 4. Parent-ground transport witness

Let \(u_-\) be a normalized lowest eigenvector of the parent operator \(K\),

\[
Ku_-=\kappa_-u_-.
\]

Assume

\[
Au_-\neq0.
\]

Define the transported parent-ground Rayleigh witness

\[
\boxed{
\chi_-
=
\frac{
\langle Au_-,\,H Au_-\rangle
}{
\langle Au_-,Au_-\rangle
}.
}
\]

Because

\[
\frac{Au_-}{\|Au_-\|}
\in
\operatorname{ran}A,
\]

the min-max principle gives

\[
\lambda_{\min}(K_+)
\le
\chi_-.
\]

Hence

\[
\boxed{
\chi_-<0
\quad\Longrightarrow\quad
\lambda_{\min}(K_+)<0.
}
\]

This is a carrier-independent **sufficient negativity witness**.

It is not a general necessity theorem: another vector in the active packet
subspace can in principle provide the negative Rayleigh direction even if the
transported parent ground vector does not.

The exact generalized-eigenvalue criterion remains the necessary-and-sufficient
finite gate test.

---

## 5. Interpretation

The theorem separates two different facts:

\[
\text{parent negative mode}
\]

and

\[
\text{active negative mode after neutral/persistent transport}.
\]

The neutral pair, persistent projector and reciprocal packet can transport the
parent negative direction into a positive active Rayleigh direction.

Therefore

\[
\boxed{
\text{negative parent }K
\not\Rightarrow
\text{formation eligibility}.
}
\]

The relevant object is the negative geometry **after admissible packet
transport**.

---

## 6. Current four-carrier audit

The exact criterion was checked on all first-step states currently used by the
three READY time-series carriers plus the exploratory relational carrier.

Total audited states:

\[
\boxed{1409}.
\]

Maximum mismatch between the direct active spectrum and the generalized
spectrum:

\[
\boxed{
3.55\times10^{-15}.
}
\]

### Annual Sunspots

\[
297/297
\]

formation states pass.

The generalized criterion matches the runtime gate on

\[
297/297.
\]

The parent-ground witness sign also matches on

\[
297/297.
\]

Observed witness range:

\[
-1.2371\lesssim\chi_-\lesssim-1.1774.
\]

### Mauna Loa CO2

\[
370/370
\]

formation states pass.

Exact generalized criterion:

\[
370/370.
\]

Ground witness sign:

\[
370/370.
\]

Observed witness range:

\[
-1.2474\lesssim\chi_-\lesssim-1.2237.
\]

### ENSO Pacific SST

\[
708/708
\]

formation states pass.

Exact generalized criterion:

\[
708/708.
\]

Ground witness sign:

\[
708/708.
\]

Observed witness range:

\[
-1.2482\lesssim\chi_-\lesssim-1.1793.
\]

### Relational weighted network

All

\[
\boxed{34/34}
\]

parent \(K\) operators already have a negative ground mode.

All

\[
\boxed{34/34}
\]

active formation gaps exceed the simplicity threshold. The smallest observed
gap is approximately

\[
0.08388,
\]

far above the numerical simplicity tolerance.

Nevertheless only

\[
\boxed{13/34}
\]

pass the formation gate.

The exact generalized criterion matches the runtime on

\[
\boxed{34/34}.
\]

For this carrier the parent-ground witness sign also separates the two groups
exactly:

successful probes:

\[
-0.55412
\le
\chi_-
\le
-0.01602,
\]

terminal probes:

\[
0.01983
\le
\chi_-
\le
0.13599.
\]

Thus the 13/21 split is not caused by absence of parent negativity and not by
ground-state degeneracy.

It is caused by whether the negative parent geometry survives the
neutral/persistent packet as a negative active Rayleigh direction.

---

## 7. Architectural consequence

The formation layer can now be written as

\[
\boxed{
(K,Y,R,\rho)
\longrightarrow
A
\longrightarrow
(M,N)
\longrightarrow
\text{generalized active spectrum}
\longrightarrow
\text{formation / }\bot.
}
\]

This makes formation eligibility an explicit transport criterion rather than a
carrier-specific empirical rule.

The exact criterion introduces no fitted threshold beyond the already declared
sign and simplicity tolerances of the master formation gate.

---

## 8. Executable implementation

Implemented in

`bfg_studio/formation_eligibility.py`.

Main interfaces:

- `packet_formation_eligibility`
- `state_formation_eligibility`
- `run_formation_eligibility_audit`
- `write_formation_eligibility_report`

CLI:

```bash
python -m bfg_studio formation-eligibility \
  --out outputs/formation_eligibility
```

No confirmatory held-out target is opened by this audit.

---

## 9. Claim boundary

The following is theorem-level for the adopted finite master map:

\[
\boxed{
\sigma(K_+)
=
\sigma_{\rm gen}
\left(
A^\dagger(K\oplus K)A,\,
A^\dagger A
\right)
}
\]

after restriction to the active right support.

The following is theorem-level as a sufficient condition:

\[
\boxed{
\chi_-<0
\Rightarrow
\lambda_{\min}(K_+)<0.
}
\]

The following is an observed fact of the present carrier audit, not promoted to
a universal theorem:

\[
\boxed{
\operatorname{sign}\chi_-
\text{ classified every current first-step carrier state correctly.}
}
\]

In particular, the `34/34` relational separation is retained as an empirical
property of the current real graph carrier, while the generalized-spectrum
criterion itself is exact finite mathematics.
