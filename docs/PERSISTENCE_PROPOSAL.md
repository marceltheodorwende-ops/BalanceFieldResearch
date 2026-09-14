# Proposed finite-dimensional persistence correction

Status: research proposal, 14 September 2026. This note does not edit or replace
the five original source files. It is not a claim of empirical validation.

## Definition

For a finite-dimensional power-bounded linear map R, define

W_per = direct sum over |lambda|=1 of ker(R-lambda I).

Define E_s as the sum of generalized eigenspaces with |lambda|<1. Power
boundedness excludes growing eigenvalues and nontrivial Jordan blocks at unit
modulus. Hence H = W_per direct-sum E_s. On E_s, R^n tends to zero; on W_per,
R is diagonalizable with unit-modulus eigenvalues. Every nonzero vector of W_per
has bounded iterates bounded away from zero, by equivalence of norms in an
eigenbasis. If no peripheral eigenvalue exists, W_per is the zero subspace.

This definition replaces the invalid span of all bounded nondecaying forward
vectors in Eq. 27 of Canonical Closure/V4. For diag(1,1/2), (1,0) and (1,1)
both survive, but their difference decays. The old span therefore includes E_s.

## Spectral and metric projections are different

The spectral projection onto W_per along E_s is a Riesz projector and commutes
with R. A separate positive graph metric G=I+Y defines the G-orthogonal projector
W(W^dagger G W)^-1 W^dagger G. For nonnormal R these need not coincide. Even for
normal R, the graph-metric projector need not commute with R if G does not.
The split uses the metric projector; it must not be substituted for the spectral
projector in a dynamical proof without additional assumptions.

## Numerical implementation boundary

The current lab supports normal, finite, power-bounded R only. It uses absolute
tolerance 1e-10 for normality and the unit circle. Classification near the circle
is tolerance-dependent; a near-unit decaying mode may be classified persistent.
The exact mathematical definition has no such tolerance. General nonnormal
numerical extraction and infinite-dimensional extensions are outside this patch.

## Capacity transport and formation

The polar factor J determines Ran(J). An orthonormal basis U of that range gives
the reduced capacity U^dagger(A direct-sum A)U. Different orthonormal bases give
unitarily equivalent capacities and the same spectrum. Kernel zero modes from
J^dagger(A direct-sum A)J on the unreduced input space must not be counted as
physical formation modes.

The gate checks positive dual loads, positive persistence gap, and a negative,
simple isolated minimum of K=c+N-D. In one dimension isolation is vacuous:
formation_gap is null, not a fabricated second eigenvalue. For a wholly
peripheral spectrum the empty stable-complement convention gives gamma=1.
These edge conventions are explicit implementation choices.

`formation_admitted` means only that these candidate conditions pass. It is not
a generated next state: the Gram rebuild and updated recursive transport are
still unspecified. Invalid shapes, nonfinite inputs and unsupported nonnormal
operators raise errors rather than being presented as physical terminal events.
