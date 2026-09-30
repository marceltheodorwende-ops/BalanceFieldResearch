# Proposed Level-0 neutral-capacity source law

**Working mathematical amendment, 30 September 2026. Status: PROPOSED, not adopted as a historical BFG theorem.** This document formulates a new constitutive rule for the BalanceFeld Gleichung. It is not attributed to the 7–8 September Level-0 papers, and it does not retroactively prove their §3.2 from §3.1. It narrows the class of admissible neutral completions. Scientific adoption and the interpretation of the neutral capacity remain decisions for the author.

## 1. Historical data and the missing arrow

The [8 September source](../../papers/BFG_Strong_Universal_Reclosure_Whitepaper_2026-09-08.pdf), §3.1, declares a finite real Hilbert carrier \(V_0\), three capacity roles \(\mathfrak D_0,\mathfrak c_0,\aleph_0\), their combination \(K_0=\mathfrak c_0+\aleph_0-\mathfrak D_0\), and

\[
F_0(\delta)=\tfrac12\langle\delta,K_0\delta\rangle+\tfrac14\|\delta\|^4.
\]

For this amendment, take the operator representatives of the three capacities to be self-adjoint in the specified real Hilbert metric; in particular \(K_0\) is self-adjoint. This typing is an explicit domain condition for the proposed rule. Assume its lowest eigenvalue \(\lambda_0<0\) is simple and separated by a positive gap. At either minimum \(\delta_*=\pm\sqrt{-\lambda_0}e_0\), the Hessian is

\[
H_*:=D^2F_0(\delta_*)=K_0-\lambda_0I-2\lambda_0e_0e_0^*>0.
\tag{1}
\]

Section 3.2 separately states the exact quadratic neutral functional \(J_A(d,\nu)=\tfrac12\|d-A^*\nu\|^2+\tfrac12\|\nu\|^2\). Its channel \(A\) and the correspondence between its coordinates and the formed branch are not fixed by (1). The [previous bridge](../completion-boundary-2026-09-29/LEVEL0_NEUTRAL_TANGENT_BRIDGE.md) makes this gap explicit. A scalar countermodel with the same entire §3.1 triple and different couplings can be built because §3.1 imposes no equation on that coupling.

## 2. New source law L0–NC

**L0–NC (neutral-capacity tangent coupling; proposed axiom).** For a formed branch as above, identify the neutral tangent carrier with a second copy of \(V_0\) using the *same derived Hessian metric* \(H_*\). In the exact quadratic tangent sector, identify the mixed source–neutral Hessian with the already declared neutral-capacity operator \(-\aleph_0\) in the original carrier coordinates. The neutral cost after completion of the source square has intrinsic metric \(H_*\), with no independent fit parameter. Equivalently, the single prescribed functional is

\[
\boxed{\mathcal J_{\rm NC}(D,\eta)
=\tfrac12\|D-H_*^{-1}\aleph_0\eta\|_{H_*}^2
+\tfrac12\|\eta\|_{H_*}^2.}
\tag{2}
\]

This is a **new choice of channel and metric**, expressed entirely with existing Level-0 operators. It does not assert that the finite-displacement quartic parent energy equals (2). A distinct physical neutral carrier requires its own identification test; (2) is a formal same-carrier-copy rule. For source data where this identification is inappropriate, L0–NC does not apply.

The two clauses matter independently. Fixing only the cross-Hessian \(-\aleph_0\) leaves the intrinsic neutral metric free; fixing only the metric \(H_*\) leaves the coupling free. The proposed axiom fixes both.

## 3. Exact consequences

**Theorem 1 (uniqueness inside the extended Level-0 rule).** With (1) and L0–NC, the unnormalized neutral map and metric are uniquely

\[
L=H_*^{-1}\aleph_0,\qquad M=H_*.
\tag{3}
\]

Writing \(d=H_*^{1/2}D\), \(\nu=H_*^{1/2}\eta\), the §3.2 channel is the self-adjoint dimensionless operator

\[
A^*=A=H_*^{-1/2}\aleph_0H_*^{-1/2},\qquad
Y=A^*A=A^2\succeq0.
\tag{4}
\]

The minimizer and reduced energy are

\[
\eta_*=(H_*+\aleph_0H_*^{-1}\aleph_0)^{-1}\aleph_0D,
\tag{5}
\]

\[
\min_\eta\mathcal J_{\rm NC}(D,\eta)
=\tfrac12\langle D,H_*^{1/2}(I+Y)^{-1}H_*^{1/2}D\rangle.
\tag{6}
\]

Consequently \(C_N=(I+Y)^{-1}\), \(B_N=Y(I+Y)^{-1}\), \(C_N+B_N=I\), \(0<C_N\le I\), and \(0\le B_N<I\) are exact in this tangent sector. The construction is orthogonally covariant and adds no numerical constant.

*Proof.* The source Hessian of (2) in \(D\) is \(H_*\); its mixed Hessian is \(-\aleph_0\). Because \(H_*>0\), the first identity in (3) is forced by \(-H_*L=-\aleph_0\). The same-carrier-copy clause fixes \(M\). Whitening gives \(\mathcal J_{\rm NC}=\tfrac12\|d-A\nu\|^2+\tfrac12\|\nu\|^2\), proving (4). Expanding (2) in \(\eta\) gives Hessian \(S=H_*+\aleph_0H_*^{-1}\aleph_0>0\) and linear term \(-\langle\eta,\aleph_0D\rangle\); stationarity proves (5). Completing the square, or applying the Woodbury identity, gives (6). Positive functional calculus proves the remaining bounds. Under an orthogonal source change \(U\), \(H_*\mapsto UH_*U^*\) and \(\aleph_0\mapsto U\aleph_0U^*\); their square roots and (2)–(6) transform together. ∎

**Dependence, not circularity.** The first half of (1) uses only historical §3.1. Equation (2) is the new L0–NC source law. Equations (3)–(6) follow from those premises. They do **not** show that §3.1 selected (2). The historical §3.2 has a general channel \(A\); L0–NC restricts that channel to (4), rather than proving that every historically admissible \(A\) had that form.

## 4. Compatibility and exclusion checks

**Scalar branch.** Take \(K_0=-1\), \(\mathfrak c_0=0\), \(\aleph_0=2\), and \(\mathfrak D_0=3\). The formed minimum is \(\delta_*=1\), \(H_*=2\), and L0–NC forces \(L=1\), \(M=2\), \(A=1\), and \(Y=1\). Hence \(\mathcal J_{\rm NC}(D,\eta)=(D-\eta)^2+\eta^2\) and its minimum is \(D^2/2\). The alternative \(L=2\), \(M=2\) from the old countermodel has the same historical §3.1 data but violates the *new* mixed-Hessian clause. This is exactly how the amendment excludes it, without rewriting history.

**Why both clauses are needed.** Keep these same scalar capacities and \(L=1\) but choose \(M=4\). Then the mixed Hessian remains \(-2=-\aleph_0\), whereas \(\min_\eta[(D-\eta)^2+2\eta^2]=2D^2/3\). Thus the mixed-Hessian clause alone does not recover the proposed response; the neutral-metric clause is an additional premise.

**Nontrivial neutral spectrum and novelty remain possible.** On \(\mathbb R^2\), choose

\[
K_0=\begin{pmatrix}-1&0\\0&2\end{pmatrix},\quad
\aleph_0=\begin{pmatrix}1&1/4\\1/4&1\end{pmatrix},\quad
\mathfrak c_0=\begin{pmatrix}0&0\\0&3\end{pmatrix},\quad
\mathfrak D_0=\begin{pmatrix}2&1/4\\1/4&2\end{pmatrix}.
\tag{7}
\]

All three capacities in this example are positive semidefinite and \(K_0=\mathfrak c_0+\aleph_0-\mathfrak D_0\). At \(\delta_*=e_1\), \(H_*=\operatorname{diag}(2,3)\), and

\[
A=\begin{pmatrix}1/2&1/(4\sqrt6)\\1/(4\sqrt6)&1/3\end{pmatrix},
\quad 0<A<I,
\quad Y_{12}=\frac5{24\sqrt6}>0.
\tag{8}
\]

Since \([K_0,Y]_{12}=-5/(8\sqrt6)\ne0\), the existing BFG finite novelty theorem permits strict second-moment change on the compatible full persistent support with positive reciprocal loads. The amendment therefore does not algebraically force \(Y\) to be scalar or erase every novelty channel. It also does not guarantee that *every* source has novelty or passes every later gate.

**No global quartic equality.** For the scalar branch, the exact parent perturbation energy is \(f(z)=z^2+z^3+z^4/4\). The same-branch two-piece minimum at \(D\ge0\) is \(D^2/2+D^3/4+D^4/32\). Formula (6) gives only its quadratic term \(D^2/2\). This is a consistent Hessian-sector interpretation, not a claim that the cubic and quartic remainder vanishes.

## 5. What this amendment does not settle

1. **Authorial source choice.** L0–NC is a proposal. Its identification of the neutral capacity with a mixed Hessian is mathematically precise but not inferred from the earlier source. The author must decide whether this is the intended Level-0 meaning and whether the same-carrier-copy restriction suits BFG's target domains.
2. **Other finite completion rules.** The later intrinsic-Gram successor load, strict-sign selection, transverse recursion/projection order, formation seed and gates retain the declared or conditional status documented in [the G/S/R audit](../proof-chain-audit-2026-09-26/PROOF_CHAINS.md). L0–NC fixes the *initial tangent channel* in its domain, not all successor laws at every level.
3. **Narrower model class.** Historical §3.2 admitted arbitrary specified channels. L0–NC rejects channels not equal to (4). This is a consistent sector restriction and a substantive new empirical/mathematical commitment, not a conservative claim that the original allowed-model class is unchanged.
4. **Physical identification and emergence.** The same-carrier-copy rule does not identify an independently measured mediator, entail a natural carrier, or exclude a matched-memory direct representation. The [current emergence preprint](../../papers/universal-reclosure-emergence-2026-09-29/README.md) retains those limits.

## 6. Dependency ledger and acceptance criteria

| Claim | Status after proposed adoption | Decisive check |
| --- | --- | --- |
| Positive formed Hessian \(H_*\) | Derived from historical §3.1 | Simple negative ground eigenvalue and gap. |
| Mixed Hessian \(-\aleph_0\) and neutral metric \(H_*\) | New source law L0–NC | Must be stated as a new axiom, not cited as §3.1's theorem. |
| Unique \(L,M,A,Y\) for fixed full Level-0 triple | Theorem 1 under L0–NC | Equations (3)–(4); old \(L=2\) countermodel excluded. |
| Exact neutral resolvent | Derived in quadratic tangent sector | Equations (5)–(6); quartic remainder retained. |
| Nontrivial novelty possibility | Consistent example, not universal | Equations (7)–(8) and \([K_0,Y]\ne0\). |
| Complete finite successor and physical emergence | Separate conditional/open results | G/S/R source-status audit; full-state gates; real intervention evidence. |

**Decision point.** If adopted, cite L0–NC as a new dated Level-0 axiom and revise only subsequent BFG claims that explicitly choose this same-carrier tangent sector. If not adopted, retain the existing conditional bridge and the countermodel. Do not silently substitute this proposal into earlier papers.
