# Mathematical amendment: persistence, polarity and transport

## 1. Scope and replacement definition

Work on a finite-dimensional complex Hilbert space H, with a linear operator R satisfying sup(n>=0)||R^n|| < infinity. Let G=I+Y with Y self-adjoint and nonnegative. Real spaces can be treated by complexification and restriction back to the real invariant space. All adjoints below refer to the original Hilbert metric.

Replace architecture Eq. (23), rather than asserting equivalence with its witness-span construction, by

```math
W_{per}=\bigoplus_{|\lambda|=1}\ker(R-\lambda I),\qquad
E_s=\bigoplus_{|\lambda|<1}\ker(R-\lambda I)^{\dim H}. \tag{1}
```

Power boundedness excludes eigenvalues outside the unit disk and nontrivial Jordan blocks on its boundary: either would make powers unbounded. Hence H=W_per direct-sum E_s, and R^n restricted to E_s tends to zero. On W_per, diagonalization with unimodular eigenvalues gives bounded positive and negative powers. This includes stable Jordan blocks and nonnormal R.

**Intrinsic characterization.** W_per is exactly the set of x_0 belonging to a bounded bilateral orbit (x_n) indexed by all integers with x_(n+1)=R x_n. For x_0 in W_per use its unique backward iterates within W_per. Conversely let E be the projection onto W_per along E_s. For every positive m,

```math
(I-E)x_0=R_s^m(I-E)x_{-m}\longrightarrow0, \qquad R_s=R|_{E_s}. \tag{2}
```

The right-hand side tends to zero because the orbit is bounded and ||R_s^m|| tends to zero. Thus x_0 is peripheral. In particular this is the unique largest R-invariant subspace on which R is invertible with uniformly bounded positive and negative powers.

This supplies a precise reversible-persistence interpretation. Requiring bounded bilateral persistence is an explicit strengthening of the old forward nondecay wording, not a consequence that rescues its span. For R=diag(1,1/2), e1 and e1+e2 both satisfy forward nondecay, but their difference e2 decays. Their span is therefore the wrong object.

## 2. Two canonical projectors with different roles

The spectral projector E is the peripheral Riesz projector, equivalently the projection along E_s. It satisfies E^2=E and ER=RE. For a full-column-rank basis matrix Z of W_per define

```math
P_G=Z(Z^*GZ)^{-1}Z^*G. \tag{3}
```

This is independent of the chosen basis Z. It satisfies P_G^2=P_G, Ran(P_G)=W_per and P_G^*G=GP_G; these identities follow by direct multiplication. It is the unique G-orthogonal projector onto W_per and is contractive in the G norm. For W_per={0}, define both projectors to be zero. For W_per=H, both equal I.

E encodes the dynamical decomposition. P_G encodes the metric splitting used in dual channels. No commutation of P_G with R is inferred.

**Exact nonnormal example:** R=[[1,-1/2],[0,1/2]], G=I. Then E=[[1,-1],[0,0]], while P_G=diag(1,0). E commutes with R; P_G does not. The powers of R are bounded, so the example meets the hypotheses.

**Bridge to the novelty theorem.** Require additionally that W_per reduce Y (equivalently, in finite dimension for self-adjoint Y, that Y W_per is contained in W_per). Its ordinary orthogonal projector P then commutes with Y. Both G and its inverse preserve the orthogonal blocks, so their G-orthogonal and ordinary complements agree, giving P_G=P. This recovers the orthogonal, neutral-compatible support hypothesis of the novelty theorem. The spectral repair alone does not imply this additional condition.

No floating-point unit-circle tolerance is part of (1). Finite precision cannot uniformly distinguish a unit eigenvalue from a sufficiently close decaying one. A numerical implementation must report ambiguity or use a declared separation certificate; it must not promote tolerance membership to an exact theorem.

## 3. Formation theorem with the correct field

For self-adjoint K let its lowest eigenvalue lambda_0<0 be simple and consider

```math
F(z)=\tfrac12\langle z,Kz\rangle+\tfrac14\|z\|^4.
\quad
F(z)\geq\tfrac14(\|z\|^2+\lambda_0)^2-\tfrac14\lambda_0^2. \tag{4}
```

Equality holds precisely when z is in the lowest eigenspace and ||z||^2=-lambda_0. Therefore:

- On a real space, the minimizer set is {+sqrt(-lambda_0)e_0,-sqrt(-lambda_0)e_0}.
- On a complex space, it is {sqrt(-lambda_0) exp(i theta)e_0 : theta real}.

The minimum value is -lambda_0^2/4 in both cases. Spectral simplicity gives a line over the declared field, not a preferred vector on that line. If the lowest eigenvalue is multiple, the corresponding sphere of minimizers replaces these conclusions; if lambda_0>=0, zero is the unique global minimizer.

For complex H, a real profile sector must be supplied by a **conjugation** C: an antilinear isometric involution. The real sector is Fix(C). Require CK=KC. The simple ground eigenspace then has a C-real unit eigenvector: if Ce=a e, |a|=1, choose a phase b satisfying b/conjugate(b)=a; C(be)=be. Restricting (4) to Fix(C) yields exactly two minima.

## 4. Preservation of the real sector by polar transport

Let C_in and C_out be specified conjugations, and let the analysis operator A obey A C_in=C_out A. Then A* intertwines in the reverse direction; A*A commutes with C_in. Its positive square root Q and Moore-Penrose inverse Q^+ do too, by finite spectral calculus. Thus

```math
J=AQ^+,\qquad J C_{in}=C_{out}J. \tag{5}
```

Both active support and Ran(J) are invariant under their conjugations. If the capacity operator on the output space commutes with C_out, its compression to Ran(J) also commutes with the restricted conjugation. The next formation operator therefore has an inherited real sector.

For the BFG two-channel A, sufficient input conditions are: C_in commutes with Y and P, the weights are real, and C_out=C_in direct-sum C_in; require every transported capacity to commute with the corresponding conjugation as well. If C_in also commutes with R and G, (1) is conjugation-invariant and the uniqueness of (3) implies that P_G commutes with C_in. A rebuilt next load must separately preserve that real structure; its positivity alone is insufficient.

This is a conditional preservation theorem, not a canonical choice of conjugation for arbitrary complex input data. A coordinate-dependent conjugation selected after seeing the eigenvectors is not automatically compatible with all other state operators.

## 5. Canonical formation output and the next-state boundary

The unordered minimizer set is uniquely determined. An individual signed or phased minimizer is not. A basis-free alternative output is the rank-one operator

```math
\rho_+=(-\lambda_0)\Pi_0, \tag{6}
```

where Pi_0 is the ground spectral projector. This is invariant under sign/phase and determines the minimizer orbit. It may be used instead of a vector only if every downstream law factors through that orbit (is phase-invariant), or if an equivariant quotient update is proved well-defined. Otherwise additional orientation data are required.

There cannot be a universally unitary-equivariant selection of a nonzero eigenvector from K alone: -I leaves K unchanged, whereas equivariance would require the selected vector to equal its negative. This obstruction does not exclude an orientation supplied by other state data. It prevents calling an arbitrary eigenvector-sign convention an intrinsic rule.

## 6. What this amendment closes

Equations (1)-(3) repair finite persistence under declared power boundedness. Equations (4)-(5) repair the real/complex formation statement and its transport compatibility. They do not determine the next Gram factors, next recursion, or invariant admissible category. Those obligations are made explicit in [RECONSTRUCTION.md](RECONSTRUCTION.md). No infinite-dimensional bilateral characterization or domain theorem is asserted here.
