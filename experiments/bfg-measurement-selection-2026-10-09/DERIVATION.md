# P64 — Measurement selection, aliasing and conditional force resolution

## Active statement and prerequisites
Determine what additional between-event observations can identify the P63
interpolation freedoms. Prove finite-measurement counterexamples, exact
functional selection criteria and a finite-dimensional reconstruction with
conditioning and acceleration-error bounds. Verify code/algebra and publish
with verified register/ledgers. This closes this observation-identifiability
investigation; no physical calibration or sine-force selection is claimed.

Sole source: Dynamic Order,8 October2026,144 pages,SHA256
1ad084a50c91a0827dd735d7cb8f666dc9e0c2552ed06b616cef28975babbdba.
Sources: Part I22–23(87)–(91),62–64,73.1(clock calibration procedure);
83(121)–(123),84–85(124)–(143),86(144)–(150),87(152),
88.3(157)–(158),88.4(159),89(161)–(162),90(163)–(164).
Dependencies: P60–P63; fix one actual P62 carrier T and one P63 reference
Abel coordinate N and phase cocycle b, not arbitrary replacement dynamics.
The declared commutator preparation stays additional. P63's reference
flow, dimensionless time lambda, and relative phase phi remain as defined.
Here u=N(x), and a phase-interpolation rival is b_h=b+h(N), with h
smooth and one-periodic. A constant h does not change the flow; fix its
mean to zero when identifying coefficients. No SI clock, inertia or data.

## Exact measurement equation
For a known dimensionless lag a>0 and a known initial u, compare the lifted
phase increment to the reference increment in the SAME observed coordinate:

 D_a h(u) = phi_h(a)-phi_ref(a) = h(u+a)-h(u).             (1)

This is exact for the full nonlinear P63 flow since u advances linearly;
it does not linearize P(x). The initial coordinate and the lag must be
independently identified; no measured radial dynamics or clock is supplied
by the canonical event alone. If phase is measured only modulo2pi,
unwrapping or a separately justified residual bound <pi is required.
Equation(1) otherwise has additional integer ambiguity.

## Any finite measurement set leaves smooth alternatives
Consider finitely many exact observations (u_i,a_i). Include in the finite
set S on R/Z every u_i and u_i+a_i, and every coordinate where finitely
many velocity/acceleration derivatives are measured. Its complement
contains an open interval. Choose a nonzero C-infinity bump supported
inside that interval and extend periodically. Subtract its mean if needed;
this changes neither (1) nor any derivative. The bump and all its derivatives
vanish at every node, up to the harmless common constant after mean removal.
Thus D_ai h(u_i)=0 and all sampled derivatives agree with the reference,
while h' and h'' are nonzero elsewhere. For any prescribed small phase
tolerance scale the bump, preserving exact agreement at the nodes.

Therefore no finite exact list of these observations uniquely determines
an unrestricted smooth between-event angular velocity/acceleration. This
includes finitely sampled real development recordings; their reuse does
not supply independent confirmation. It is not a universal BFG impossibility
claim: it identifies the observational limit of this unrestricted family.
No sample count is silently converted into a smoothness/bandwidth theorem.

## Functional lag selection and its precise scope
Suppose the FULL function D_a h(u) is known to vanish for every u on a
complete unit interval, not just finitely many u. Periodicity extends this
identity everywhere. If a is irrational, continuity and density of rotations
{n a mod1} imply h is constant: h(u+n a)=h(u), and every target phase is
approached by such a sequence. Then h'=h''=0 and this phase freedom is
eliminated. If a=p/q in lowest terms, h(u)=sin(2pi q u) is a concrete
nonconstant invisible rival; rational lags do not remove all frequencies.

The radial freedom also has a functional criterion. Write P63's alternative
Abel coordinate f(u)=u+d(u), f'>0, d one-periodic. Its fractional radial
map advances u to f^-1(f(u)+a). Equality to the reference map for EVERY
u means f(u+a)=f(u)+a, equivalently d(u+a)=d(u). An irrational lag forces
d constant by the same proof, so the radial path is unchanged. Radial
and phase functional comparisons together eliminate these TWO explicit
P63 freedoms within the fixed carrier/clock class. They do not prove
uniqueness among all possible BFG realizations, select T, identify seconds,
or identify the phase with a physical pendulum angle. Finite recordings
cannot establish exact functional equality without additional regularity.

## Conditional finite reconstruction with declared bandwidth
A falsifiable EXTRA model assumption is that the unknown h is a real
zero-mean trigonometric polynomial of degree <=H, H>=1:

 h(u)=sum_{0<|k|<=H} c_k exp(2pi i k u), c_-k=conj(c_k).

This is a restriction of interpolation uncertainty, not a BFG axiom or a
new dynamical term justified solely by fit improvement. It must be fixed
and defended on development evidence, with larger-bandwidth and unrestricted
smooth rivals retained. Do not impose h=0 by convention as physical selection.
For u_j=j/J, J>=2H+1, measure (1) at one known lag a. Then

 d_j=sum c_k m_k exp(2pi i k j/J), m_k=exp(2pi i k a)-1.  (2)

Distinct Fourier columns are orthonormal under the discrete norm
||d||_J²=J^-1 sum|d_j|², since no difference of retained k equals J.
The normalized measurement matrix therefore has singular values

 |m_k|=2|sin(pi k a)|, sigma_min=min_{1<=k<=H}|m_k|.      (3)

It is injective exactly when k a is not an integer for 1<=k<=H. In
particular a=p/q with q>H suffices in this FINITE model, although it failed
the unrestricted model. Recover

 c_k = [J^-1 sum_j d_j exp(-2pi i k j/J)]/m_k.            (4)

For a half-event lag, every even k is invisible; more samples at that same
lag do not recover those modes. Irrational a ensures exact finite rank,
but does not guarantee good conditioning as H increases: rational
approximations make some sin(pi k a) arbitrarily small. Uniform
unrestricted force stability does not follow from exact injectivity.

## Error bounds, units and prespecified perturbations
Define robustness as perturbation of reconstruction in this fixed-H model,
fixed sampling grid and known reference/clock, with total residual error
||e||_J<=E. This is inverse-problem robustness, not full-state dynamical
Lyapunov stability or empirical prediction confirmation. For sigma_min>0,
Parseval and (4) give

 ||h_hat-h||_L2<=E/sigma_min,
 ||h_hat''-h''||_L2<=(2pi H)² E/sigma_min.                (5)

If a physical duration c seconds were independently calibrated, divide
the acceleration bound by c². A calibrated inertia J_phys plus the
additionally assumed mechanical angle/torque law would multiply it by
J_phys to give a torque-error bound. None of these calibrations or physical
identifications is currently established. The h'' term is the actual
P63 between-event acceleration difference; this derives a conditional
resolution bound without postulating a sine torque in the readout.

For bounded perturbations |delta u_j|<=rho_u, |delta a_j|<=rho_a,
the mean-value theorem bounds the error in D_a h by
||h'||_infinity*(2rho_u+rho_a). If ||h||_L2<=R in this finite model,
Cauchy–Schwarz gives ||h'||_infinity<=2pi H sqrt(2H) R.
Hence a sufficient total E is phase-residual error plus
2pi H sqrt(2H) R*(2rho_u+rho_a). This does not cover uncertainty in
the reference b or preparation T: those require a separate validated
bound, added to E. No value of R, measurement noise, jitter or inertia
is fabricated. The given inequalities specify what must be measured.

Multiple lags a_l with their residual blocks can be combined with normalized
mean square over l. The singular values become
sqrt(L^-1 sum_l |exp(2pi i k a_l)-1|²). This is an explicitly typed
combination of observation operators, not a tensor lift of the kernel.
It can remove a finite-model nullspace but finitely many lag/coordinate
nodes still fail the unrestricted smooth family by the bump proof.

## Prospective measurement bridge and unsatisfied prerequisites
The derived selection rule is concrete: declare preparation and identify
x, relative phase and u=N(x); independently calibrate a constant event
duration and phase measurement/unwrapping; fix and justify H and residual
bounds; choose J>=2H+1 and lags with a certified sigma_min; collect
development observations at the specified states/times; reconstruct via
(4), test larger-bandwidth/nonparametric rivals on the same data, and
evaluate (5) with all reference/calibration uncertainty. Failure of radial
fractional-map agreement blocks the fixed-N interpretation before fitting h.
Passive repeated observations are not causal interventions. Freeze any
complete candidate and decision rule before independent untouched holdout.

This is a prospective, conditional measurement protocol, not an executed
experiment or a frozen confirmatory physical realization. Arbitrary phase
grid preparation, an independently observed BFG state/event clock, and the
bandwidth restriction are not established for the existing pendulum files.
The next necessary dependency is to determine whether permitted real
development instrumentation can identify that state/clock and distinguish
the preparation/observable from mechanical rivals. No holdout is opened
to settle these prerequisites. A good finite reconstruction alone cannot
prove BFG-internal force, energy or universal physics.

## Accompanying whole-source and other-carrier audit
Part I22–23/73.1 and89 requires identified measurement/clock/factor bridges;
the exact equation(1) is their concrete interface for P63. 83–85 and the
62–64 differential chain define the actual quotient state and tangent;
they do not measure N or seconds. 86's balances, spectral entropy and
witness record are consistent with equal canonical endpoints of all these
rivals, so none alone eliminates h. 87's finite seed theorem cannot add
missing observations. 88.1's scalar illustration does not settle this
matrix family; 88.2's separate driven fixed point does not permit a finite
Abel clock there; 88.3 supplies viability/transverse requirements rather
than measurement rank. 88.4's mediator ODE remains an additional model.

Under the full-persistence L_m of90(163)–(164), normalized base x,phi,u
readouts have the SAME measurement equation and singular values. Replication
preserves stock/witness and multiplies ranks; it neither provides independent
measurement samples nor improves (3) without a separately justified
instrument/noise model. Projection back retains the finite-node ambiguity.
Nonreplicated inputs and seed degeneracy require new explicit rules. No
fractal architecture or metric claim is made. This compatible carrier
transfer supports the same active identification step.

## Controls and proof status
Frozen controls: symbolic rational-lag alias and periodic measurement
multiplier; explicit smooth finite-node invisible bump; Fourier matrix SVD
against (3), direct reconstruction and bounded-noise recovery; half-lag
rank failure and complementary-lag recovery; acceleration Parseval bound.
All are synthetic mathematical/code controls, not measured data. Finite
numerical irrational values do not prove irrationality; the general
functional result uses the stated exact irrational assumption.

Observed controls passed: three symbolic identities, an explicit ten-node
invisible smooth bump, and three Fourier reconstruction/noise cases. Matrix
singular values agreed with (3) to <=1.12e-15; exact reconstruction error
was <=3.45e-12, including the ill-conditioned case. At H=5 a half-event
lag had rank6 of10; combining half- and third-event lags restored rank10
with minimum singular value1.22474. A deliberately adverse perturbation in
the weakest mode attained the coefficient error bound numerically. Near
lag0.499999 the condition number was159154.94 and residual RMS7.071e-5
produced coefficient error5.627 and acceleration error888.58 in dimensionless
units. This retained negative robustness result demonstrates that full
rank alone is insufficient. The initial frequency-one noise control also
passed; the completed control targets the least observable mode explicitly.
None of these synthetic values are physical uncertainties or observations.

PROVED: finite-node nonidentifiability, functional irrational-lag selection
within the explicit P63 freedoms, and conditional finite-band measurement
rank/recovery/acceleration bounds. ADDITIONAL HYPOTHESES: bandwidth,
instrument model, preparation and state/time calibration. OPEN: actual
physical selection, pendulum observable/sine force, energy, inertia and
interventions. Publish and verify the ledgers before declaring this step done.
