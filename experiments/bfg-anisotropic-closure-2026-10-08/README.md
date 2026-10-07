# Completed internal anisotropic observable-closure step
The canonical full-persistence matrix sector admits an exact gauge-invariant factor consisting of a formation-weighted spectral probability measure and a kernel/formation coherence measure. It works even when geometry eigenvalues merge. See DERIVATION.md for the full proof, source equations, units, discarded information and physical limits.

Eigenvalues alone and even (weighted geometry,aggregate kernel trace) fail closure; both explicit counterexamples are retained. The compact simple-spectrum chart remains available, but its exit is not a canonical terminal. The fuller measure construction resolves that mathematical chart limitation.

Local controls:100 complete Ambient comparisons,100 unitary changes, two ordering reversals, both insufficient-readout witnesses and collision handling. Maximum factor residual7.11e-15; gauge residual3.41e-13; collision residual2.78e-17; criterion1e-10 passed. No real-data evaluation, new forecast improvement, physical intervention, holdout access or workflow launched. Numerical grouping tolerance1e-12 is an implementation convention, not a general near-collision guarantee. Results/controls.json preserves outcomes.

Reproduce from this directory in the research repository (numpy, scipy):

    python verify.py results

This imports ../bfg-matrix-tangent-2026-10-08/control.py and ../real-eeg-covariance-2026-10-07/experiment.py for independent comparison without executing their main/download routines. Source is exclusively Dynamic Order.

This step closes an INTERNAL observable-factor obligation. It does not establish the physical angle/velocity map, gravity, friction or seconds from BFG. Those remain explicitly open in the register. Next: test a proposed regular two-observable physical reduction of this derived factor, preserving the coherence information shown necessary by the counterexample.
