# Experimental closure M2: negative spectral transport

M2 is an explicit alternative to M1's packet projector. It is a modeling
proposal, not a consequence proved from the five source papers. It retains M1's
normalization, capacity retention and load closure. Original sources are unchanged.

## Rule and rationale

After an admitted candidate and capacity update, form
`K_next = C_next + N_next - D_next`. Let P be the orthogonal spectral projector
onto the eigenvectors with eigenvalues strictly below `-TOL`. Set
`R_next = P + rho (I-P)` with `0 <= rho < 1-TOL`.

The rationale is to preserve the entire strictly negative formation subspace,
rather than just the packet direction. A Hermitian spectral projector is
independent of eigenvector phases and choices of basis inside degenerate
eigenspaces. In exact arithmetic R is normal and power bounded, with peripheral
space Ran(P); its other directions contract by rho. Empty P is permitted and
leads to no persistent support at the next candidate test. Full P gives R=I.
The existing isolated-minimum gate still applies: multiple negative directions
are allowed, but a degenerate lowest eigenvalue fails that gate.

This definition imposes persistence using the chosen formation operator. It
does not derive a microscopic mechanism or demonstrate self-organization.
The rank can remain greater than one, but carrier dimension still cannot grow.
The state need not occupy every preserved direction. A state without any dual
support can stop even if a negative spectral space exists.

## Reproduction

`python -m bfg_lab.minimal` emits all four M1/M2 maintained/depleted histories.
Python API: `simulate(multimode_seed(), transport_rule='negative_spectrum')`.
The previous default `transport_rule='packet'` is preserved.

M2 seed: Y=I, d=(1,1,1), R=diag(1,1,0.5), D=diag(4,3,1), C=N=I.
The first candidate has formation eigenvalues -2 and -1. With retention a,
the surviving diagonal mode values follow `2-4 a^k` and `2-3 a^k` until
their directions are removed by the negative spectral rule.

| Retention | Result within 12 steps | Persistent ranks after transitions |
| --- | --- | --- |
| 1 | Step budget reached | 2 throughout |
| 0.8 | Four transitions; next candidate has no dual support | 2, 1, 1, 0 |

For a=0.8 the admitted candidate minima are -2, -1.2, -0.56, -0.048.
The next formation operator becomes positive after the fourth transition;
its transport has no peripheral space. This timing follows the explicit order:
test current candidate, update capacities, construct next transport.

## Self-check and limits

- Analytic diagonal spectra and stopping time are independent reference values.
- Twelve seeded complex unitary coordinate changes preserve spectra and stop.
- Initial perturbations +/-1e-6 preserve the depletion stop index.
- A noncommuting load/capacity example checks four transitions and PSD invariants.
  It has three persistent next directions: the two branches jointly span more
  than the incoming two-dimensional peripheral space. An initial expectation
  of rank two failed this check and was corrected. Carrier dimension remains
  three; persistent rank need not decrease monotonically in general.
- A spectrum with eigenvalue -5e-9 retains that direction at thresholds 1e-12
  and 1e-10, but loses it at 1e-8. Near zero, rank is intentionally discontinuous.

The threshold sweep tests `spectral_transport` only. The full recursive pipeline
still uses the existing absolute TOL=1e-10; no full-pipeline tolerance robustness
claim is made. Away from zero a spectral gap supports local projector stability,
but these examples do not establish robustness for arbitrary states or empirical
validity. Comparison with an independently motivated transport law remains open.
