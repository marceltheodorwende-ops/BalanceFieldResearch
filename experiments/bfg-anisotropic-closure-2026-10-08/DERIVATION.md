# Anisotropic observables: exact spectral and coherence closure
Active source: Dynamic Order, SHA2561ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba. Canonical sections84.1–84.4 equations(129)–(138), factor criterion89(161), compatible full-persistence structure90.1; dependence P39 exact natural-frame representative. No added mechanical generator or older paper is used.

## Premises and completion criterion
Fixed finite carrier, P=I,0<Y<I,F positive definite,K Hermitian,W density. We construct sufficient gauge-invariant observables and prove their successor is determined by them. This is a factor, not necessarily a full reconstruction of every canonical component. Full persistence has no seed, all loads positive, and successor R is positive with eigenvalues strictly below1. Therefore canonical terminality is constant (nonterminal) on these fibers. This does not extend to partial selection, seeds, singular formation or physical clock identification.

## 1. Exact closed geometric observable
Let Y=sum_a y_a Pi_a use DISTINCT eigenvalues and their full spectral projectors, including multiplicities. Define weights p_a=tr(F Pi_a)/tr(F)>0, sum p_a=1, and probability measure mu=sum p_a delta_y_a. These are invariant under simultaneous unitary transformation of all operators. F need not commute with Y.
Since C,B are functions of Y, the canonical loads are

    lc=tr(F) sum_a p_a/(1+y_a),
    lb=tr(F) sum_a p_a y_a²/(1+y_a),
    alpha=lb/(lc+lb), beta=1-alpha.

Their overall formation scale cancels in alpha. The natural-frame P39 result is Y+=r_alpha(Y), r_alpha(y)=[alpha+beta y²]/(1+y)², and F+=F. Thus mu+=r_alpha pushforward(mu). If different y_a map to the same r, add their weights. The successor spectral projector at that r is the sum of the original projectors in that group. Both alpha and the resulting measure depend only on mu: the section89 fiber criterion is satisfied. This proof covers exact eigenvalue collisions, not only a simple-spectrum chart. Positivity0<r<1 follows because r is a convex combination of C_eigen² and B_eigen², each strictly between0 and1.
The measure forgets K,W, offdiagonal F, multiplicities and formation scale; it closes geometrical evolution, not physical pendulum dynamics. For two distinct atoms and a fixed weight preparation the eigenvalue pair gives two evolving internal coordinates, but this does not identify them with signed angle/velocity or seconds. Ordered atoms can swap; weights must follow their atoms. Equal eigenvalues merge and reduce this geometric observable's information.

## 2. Insufficient observables: two concrete witnesses
With Y=diag(.2,.7), F_A=diag(.8,.2), F_B=diag(.2,.8), K=diag(1,0), both states have identical geometry eigenvalues but different formation weights. The resulting successor spectra differ (control Euclidean gap .1201573). Hence eigenvalues WITHOUT weights fail the factor criterion.
With the same Y and F=[[1,.3],[.3,1]], take K_A=diag(1,0) and K_B=[[.4,1],[1,0]]. Both have tr(FK)=1 and identical mu. Diagonal contributions are1 and.4, offdiagonal contributions0 and.6. P39 preserves the diagonal kernel entries and attenuates the offdiagonal ones by gamma<1, hence the successor aggregates are1 and.4+.6gamma, unequal (control gap .0967905). Thus even (mu,tr(FK)) is insufficient. A signed kernel readout cannot be declared closed by simply attaching one trace to the geometry measure.

## 3. Closed coherence observable, including collisions
For distinct spectral projectors define

    nu_ab=tr(Pi_a K Pi_b F),
    nu=sum_ab nu_ab delta_(y_a,y_b).

This is a complex measure, not a probability; nu_ba=conjugate(nu_ab), diagonal entries real. It carries kernel times formation units, not joules. Gauge invariance follows by trace cyclicity and joint projector covariance. It exists for repeated eigenspaces without choosing individual eigenvectors.
In the natural frame, C,B,R commute with Pi_a. P39 implies

    Pi_a K+ Pi_b=gamma_ab Pi_a K Pi_b,
    gamma_ab=[alpha c_a c_b+beta b_a b_b]/sqrt(r_a r_b),
    c_a=1/(1+y_a), b_a=y_a/(1+y_a).

Therefore the successor coherence coefficient for output groups A,B is

    nu+_AB=sum_(a in A,b in B) gamma_ab nu_ab.

Equivalently nu+ is the product-map pushforward of gamma*nu. F remains unchanged in this representative. All needed coefficients and groups come from mu and nu. Thus Pi=(mu,nu) is an EXACT closed canonical observable factor on the stated full-persistence domain, including noncommuting K,F and eigenvalue collisions. This does not require silently adding instrument dynamics to canonical Xi. Scalar aggregate tr(KF)=sum_ab nu_ab is recovered but cannot be updated correctly unless the discarded coherences are retained.
For a two-atom simple-spectrum chart one can keep the sum of diagonal nu entries s and the complex offdiagonal z; then s+=s,z+=gamma12 z, with z conjugated when the sorted atoms exchange order. This smaller chart fails at a collision. The measure factor above handles that case by summing ALL diagonal and offdiagonal contributions into the merged coefficient. After geometry becomes isotropic, gamma=1 within that single block and that aggregate is preserved.

## 4. Collision and numerical policy
For Y=diag(.2,.7), the positive formation F=diag(w,1-w) with w approximately .13784556720686372 gives equal successor eigenvalues. The full canonical update is nonterminal. This refutes labeling a simple-spectrum readout exit as a canonical terminal. The global measure factor remains defined.
The exact proof groups EXACTLY equal output eigenvalues. Implementation groups gaps<=1e-12 as an explicit floating-point convention; this is not an exact-rank or exact-equality theorem for near-degenerate distinct states. No empirical states are grouped here, and no universal numerical robustness claim is made. Gap-based spectral projectors become ill-conditioned near collisions, whereas the merged exact measure uses the full eigenspace. Controls compare to independent complete Ambient computation and include two output order reversals, a collision witness and unitary changes.

## 5. Status and limits of this completed step
Completed: sufficient internal anisotropic geometric/coherence observables, exact successor laws, inadequate-readout counterexamples, collision-safe mathematical construction, executable code and independent controls.100 complex preparations match Ambient factor predictions to7.11e-15;100 unitary changes agree within3.41e-13; collision measure residual2.78e-17. Fixed criterion1e-10 passed. Synthetic mathematical/code controls only, no physical data, refit, new empirical experiment or holdout access.
Still open: physical identification of these observables, a calibrated clock, a regular two-dimensional physical reduction and internally selected pendulum force. The exact factor retains attenuation, not automatically oscillation. The next necessary step is to test whether a proposed signed two-observable physical reduction of this CLOSED factor retains enough information and satisfies the full nonlinear transition; no external sine flow is inserted as its own proof. Restricted factor closure is not renamed as completion of the physical claim.
