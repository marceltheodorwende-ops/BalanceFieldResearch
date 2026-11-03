# Focused dependency audit of the finite-event classification

Reference: DOI 10.5281/zenodo.23897937, version 1.0. This is a new internal review of the written proof chain, not a claim to have independently formalized every theorem.

## Contract and protected assumptions

The event is exactly Section 12: finite ambient input space; Hermitian K; positive densities with normalized witness; positive semidefinite Y; orthogonal P; selector threshold [0,1); positive-load gates; ambient reduced SVD; lossless R4; simple negative rank-one seed or absorbing terminal. No forcing, carrier expansion, renormalization or changed seed rule is inserted. Exact ranks in a theorem are not numerical rank cutoffs.

| Claim | Required dependency | Focused audit and remaining boundary |
|---|---|---|
| 13.1 Ambient invariants | Positive selected load; selected range inside Q; ambient domain of A | The first channel puts Ran(P_s) inside Ran(A*), making V*P_s a partial isometry and R4 lossless. D>=I and spectral separation below 1 give norm(A)<1. Repeated positive singular values rotate all successor data together. No certified floating rank test follows. |
| 26.1 Lossless later selection | 13.1 and density support after seed | Successful output has 0<Y<I, so Q=I next time. Both compressed channels are injective on the persisted support, hence positive formation gives positive loads. A later positive-defect branch may still fail its seed gate. |
| 26.2 Finite completion or absorption | 26.1; ambient range identity; rank-one seed | Ran(A*)=Ran(P)+Y Ran(P). The added dimension is q=rank((I-P)YP). Successful positive q gives d_next=q-1<=d-1. For q=0, dimension reduction gives full persistence without a seed. First-attempt bookkeeping gives at most n0 attempts. This includes failures; it does not promise initial survival. |
| 26.3 Finite seed budget | 26.2 and isometric K compression | After first selected rank s>=1, total seeds <=e+d1=n1-s<=n0-1. Norm(K) cannot grow under isometric compression; each seed contributes at most norm(K0). Only first selection can reduce historical witness mass. |
| 26.4 Load collapse | Full persistence; fixed compatible gauge; nonzero positive formation | The load ratio a is a positive weighted mean of y_i^2/(1+y_i^2), including singular formation densities. The maximum inequality gives strict decrease, first successor below 1/2, and a uniform double-exponential bound. It is not a physical energy statement. |
| 26.5 Kernel convergence | 26.2, 26.4 and positive Schur factors | Every fixed matrix entry is its initial complex value times a decreasing nonnegative scalar product. Finite dimension upgrades entrywise convergence to Frobenius convergence. Off-diagonal vanishing is not required. Y=0 fails the positive B-load gate only at the limit. |
| 26.6 Renewal limit | 26.2-26.5 and four-mode Vandermonde chart | Finite seed budget excludes indefinite endogenous seeding. Shrinking load bounds absolute spectral gaps and chart determinant; this alone does not establish relative ill-conditioning. |

## Independent safeguards

The proof distinguishes the first selection from post-success inputs, q=0 from q>0, zero formation weights from zero total formation, exact positivity from underflow, and finite-time continuation from a terminal limit. Within these assumptions this focused review found no contradiction in this chain. That is a bounded review conclusion, not a new external correctness certification.

## Fresh implementation replay

The preserved extended-controls implementation was rerun for this stage. It checks 120 random finite-event prefixes, 40 high-precision full-sector cases over 14 steps, nine exact rational cases over four steps, Schur-versus-SVD correspondence and two seed-terminal controls. See baseline/extended_verification.json and baseline/execution_log.txt. The script is preserved from the published supplement; rerunning it is fresh execution, not independent implementation. Numerical rank decisions remain tolerance dependent.

## Open implementation obligations

1. Rank-changing inputs need certified decision procedures or explicitly unresolved outcomes, rather than arbitrary tolerance-based physical claims.
2. Very small positive loads need scaled or high-precision arithmetic to avoid false terminal labels.
3. The full operator proof has not been checked by a proof assistant.
4. The historical uniqueness of the adopted event rules and a general physical correspondence are not established by this chain.
