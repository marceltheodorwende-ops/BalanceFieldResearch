# RC pilot: prospective protocol and identifiability gate

Status: simulation and prospective design only. No hardware was purchased and no laboratory measurements were made. This is not a preregistration in an external registry; revise and freeze the protocol before collecting data.

## Question and comparison

Can a calibrated passive three-node RC network reproduce the predicted common-mode exponential and a finite sequence of designed BFG threshold events within a justified measurement budget?

Classical null: C x_dot=-Lx with the measured components, probe loading and initial state. Event implementation: apply the prescribed thresholds f(y) to that same trajectory. In the ideal common mode these predict identical event values and times. There is no BFG-versus-classical discrimination in this design. A test of a natural BFG law requires an additional independently specified physical prediction and a competing model with differing observables. That requirement is currently open.

## Nominal model and simulated acquisition

Three nodes each have a 10 microfarad capacitor and 100 kilohm resistor to ground. Two additional 100 kilohm resistors join node 1 to the middle and the middle to node 2. Thus L=10^-5 [[2,-1,0],[-1,3,-1],[0,-1,2]] siemens and C=10^-5 I farads. The common-voltage time constant is one second. Prepare all nodes at 0.8 V relative to a fixed 1 V reference; remove the charging source at t=0. Synthetic traces use 100 samples per second for five seconds. This rescaling changes physical times relative to the paper's nominal circuit, not the dimensionless recursion.

The pilot assumes 1 mV detector standard deviation and 1 mV quantization step. Its 1,000 tolerance cases vary each conductance and capacitance independently by a uniform +/-1%. These are exploratory design assumptions, not measurements or guaranteed hardware specifications. Tolerances and detector noise are separate streams. The saved trace is synthetic.

## Practical result and resolution boundary

Starting at 0.8 V, ideal successor thresholds are approximately 0.240891 V, 0.0712373 V, 0.00879984 V, 0.000152173 V and 0.0000000462989 V. Only the first three successors exceed a nominal 1 mV floor. Being above that floor does not guarantee reliable detection: noise tails, timing error, node mismatch and calibration must also be included. The fixed five-second trace covers those first three ideal events only; later tabulated events are analytical extrapolations, not recorded samples.

The equilibrium thermal voltage scale sqrt(k_B T/C) at 300 K is about 20.4 nV per mode for these capacitors, far below the assumed detector noise. This prototype cannot test the microscopic thermal residual theorem at that resolution. Do not interpret added millivolt detector noise as the capacitor's thermal bath or apply an ideal unfiltered residual formula directly to noisy sampled voltages.

## Hardware-readiness gates

Before a physical run, identify the actual acquisition device, input impedance, bandwidth, synchronization, voltage calibration, capacitor leakage and dielectric behavior. Include measurement loading in the fitted circuit; the ideal nonperturbing-detector assumption cannot simply be declared satisfied. Specify a common ground and isolated low-voltage preparation, with no mains-connected improvised circuit.

Calibrate component values and measurement errors on separate data. Fix allowed parameter ranges before held-out validation. Record three node voltages, not only their mean, to detect loss of the common mode. Fit or independently measure the actual L and C; do not retune them separately for every validation trajectory.

For each held-out run compute x_pred(t)=C^-1/2 exp(-Ht) C^1/2 x0 with H=C^-1/2 L C^-1/2. Reject the stated implementation if the measured trajectory or events exceed a predeclared simultaneous uncertainty region after accounting for model discrepancy. Numerical thresholds for this rule remain unset until the real instrument and calibration data exist. A failed ideal-circuit test may reject its calibration, preparation or approximation; it does not by itself falsify every BFG formulation.

Use fixed observation windows for stochastic residual checks. Random threshold stopping needs a separately justified stopped-process analysis. Preserve raw measurements and calibration records if hardware work proceeds. Do not discard failed preparations without recording a predetermined exclusion reason.

Measurement-uncertainty reference: [BIPM/JCGM guides](https://www.bipm.org/en/web/guest/publications/guides), particularly JCGM 100:2008, https://doi.org/10.59161/JCGM100-2008E.
