# Level-0 coupling and the complete finite successor: proof status

29 September 2026. Mathematical supplement to the [universal reclosure and emergence preprint](BFG_Universal_Reclosure_and_Emergence_Preprint_2026-09-29.pdf). The source claims below refer to the specified published BFG rules, not to every possible unpublished premise. No natural-system emergence claim is made.

## 1. Requested claim: a unique coupling without an additional choice

The [8 September Level-0 source](../BFG_Strong_Universal_Reclosure_Whitepaper_2026-09-08.pdf) states in §3.1 a quartic formation functional and in §3.2 a *separate* quadratic neutral completion.

**Proposition 1 (source-scoped non-uniqueness).** The data of §3.1, including a formed minimum and its Hessian, do not uniquely determine the channel coupling in §3.2.

**Proof.** Fix the same complete one-dimensional §3.1 functional in every model:

\[
F_0(x)=-\tfrac12x^2+\tfrac14x^4,\qquad x_*=1,\qquad H_*=F_0''(1)=2.
\]

For each \(\ell>0\), let the neutral tangent metric be \(M=2\) and its nonzero linear coupling be \(L=\ell\). The positive two-piece completion is

\[
J_\ell(D,\eta)=(D-\ell\eta)^2+\eta^2.
\]

Its unique minimizer and exact response are

\[
\eta_*=\frac{\ell D}{1+\ell^2},\qquad
\min_\eta J_\ell(D,\eta)=\frac{D^2}{1+\ell^2}.
\]

Whitening gives \(d=\sqrt2D\), \(A^*=\ell\), and \(Y=A^*A=\ell^2\). Thus \(\ell=1\) and \(\ell=2\) have identical §3.1 data and strictly positive neutral channels, but their exact responses are respectively \(D^2/2\) and \(D^2/5\). Neither branch condition nor positivity selects one. ∎

The original §3.2 supplies a quadratic completion as a BFG rule. Its minimization and Gram resolvent are exact **once a channel has been specified**. The Hessian in §3.1 supplies a local metric; it cannot make the quartic energy exactly quadratic at finite displacement. The [direct derivation attempt](../../research/completion-boundary-2026-09-29/SOURCE_DERIVATION_ATTEMPT.md) computes the nonzero cubic and quartic remainder. A unique physical or mathematical interface therefore needs a new independent rule or an older sourced premise that excludes one of these two couplings. Calling either choice “canonical” is not such a proof.

## 2. Requested claim: the complete canonical finite successor

The [Fundamental Closure Law](../../research/fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/FUNDAMENTAL_CLOSURE_LAW.md) and [Master State](../../research/fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/MASTER_STATE.md) define the living rank-aware state

\[
\Xi=(\mathcal H,\mathfrak D,\mathfrak c,\aleph,\rho_F,\rho_W,Y,R_C).
\]

It contains the formation operator \(K=\mathfrak c+\aleph-\mathfrak D\), separate positive formation and normalized witness densities, a positive neutral load, and recursive transport. It has five conceptual roles, but the fully typed implementation retains their components separately. Its declared update is selection first, followed by witness/persistence transport, positive dual loads and reciprocal weights, selected two-channel analysis, reduced SVD, target Gram, three-capacity transport, formation and witness reconstruction with the gated seed, target persistence, and transverse recursion. Exact failed gates return the absorbing terminal value.

**Theorem 2 (complete conditional finite update).** Under the declared intrinsic-Gram successor load, neutral-contrast selection, transverse recursion, and all exact nonterminal gates, the full finite update has a unique typed target up to simultaneous active-basis unitary change. It preserves positive nonzero formation density, unit-trace witness, positive target neutral load, Hermitian capacities, and power-bounded recursion, and \(\dim\mathcal H_+=\operatorname{rank}\mathcal A\leq\dim\mathcal H\). Otherwise it terminates at the prescribed gate.

**Proof and dependencies.** The [existing full-state theorem](../../research/completion-boundary-2026-09-29/UNIFIED_FINITE_THEOREM.md) gives the detailed argument, including rank events: reduced SVD \(\mathcal A=U\Sigma V^*\) gives the positive target load \(Y_+=\Sigma^2\); polar transport of both densities preserves positivity and normalizes the surviving witness; a required seed is positive on its orthogonal support; and, for the already constructed target persistence projector \(P_+\), the declared recursion \(R_{C,+}=P_++Q_+(I+Y_+)^{-1}Q_+\) has an identity peripheral block and a strict finite-dimensional contraction on \(Q_+=I-P_+\). Exact gates cover empty persistence, vanished mass, dual zero load, zero analysis rank and unavailable unique formation seed. This is a proof of the **declared operator**, not a proof that its three completion rules are compelled by historical §3.1. ∎

**Fresh executable check.** On the package's `repeated_rank_growth_fixture`, four consecutive calls of `bfg_universal_state_update` with `tol=1e-12` and `boundary_tol=1e-10` are nonterminal. The persistent ranks are 3, 4, 4, 4 inside dimension 4; witness traces are one to floating precision, the smallest formation eigenvalue is \(-0.8\), and the smallest neutral eigenvalues are approximately 0.0028649525658471235, 0.00007940396247126099, 0.00013525074086497352 and 0.00000010256168029063261. The [execution audit](FULL_SUCCESSOR_NATURAL_EVIDENCE_AUDIT.md) gives the command and earlier record. This computation checks an implementation and fixture; it does not prove a missing source implication or irreducible emergence.

## 3. Why these two tasks cannot both be checked off in the requested absolute sense

The historical/source-only finite rules also leave the target load and recursion underdetermined. The [update derivation audit](../../research/fundamental-closure-2026-09-25/package/research/bfg-fundamental-closure/UNIVERSAL_UPDATE_DERIVATION_AUDIT.md) constructs different positive target Gram operators for the same preclosure packet, and different bounded recursions with the same persistent space. The [G/S/R proof audit](../../research/proof-chain-audit-2026-09-26/PROOF_CHAINS.md) exhibits further inequivalent Gram, selector and transverse-response choices under their explicitly weaker source conditions. These are source-scoped independence results, not claims about any unspecified stronger axiom.

| Goal | Mathematical status | What would close the remaining claim |
| --- | --- | --- |
| Level-0 quadratic tangent and exact neutral elimination | Proved from the jointly stated §§3.1–3.2 plus an identified interface | Nothing further for that conditional theorem. |
| Unique coupling from §3.1 without additional choice | Not derivable from the stated §3.1 data; Proposition 1 is a countermodel | An independently justified BFG premise selecting the coupling, with the countermodel excluded. |
| Complete typed finite successor with declared G/S/R rules | Proved conditionally; four full synthetic transitions executed | Nothing further for the stated finite operator and its exact gates. |
| Unique full successor forced by historical Level 0 alone | Not established; source-only target load and recursion admit inequivalent completions | Derive the exact G/S/R role and ordering identifications from older premises, or explicitly adopt them as new BFG axioms. |
| Irreducible emergence in a natural carrier | Open | Independently measured full state and higher reporter, selective removal and restoration, and matched mechanistic rivals. |

The precise mathematical progress is a closed, fully typed **conditional** finite successor and a proof that the requested stronger uniqueness does not follow from the enumerated older premises. No manipulation of the existing equations can make two admissible unequal responses equal.
