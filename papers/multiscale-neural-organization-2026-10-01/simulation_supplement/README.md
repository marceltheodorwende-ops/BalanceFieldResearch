# Simulation data reconstructed from the preprint

This is a new computational supplement derived from PDF pages 7-11, equations 11-24, Table 3 and Appendix B. It is not the original accompanying script or archive.

- table3_transcribed.csv preserves the six rounded rows printed in Table 3 (page 9).
- recomputed_summary.csv contains freshly calculated values from the stated matrices and parameters.
- Six trajectory CSVs contain the initial impulse state and all 60 updates, in coordinate order w1,s1,w2,s2,w3,s3.
- results.json contains parameters, results and fresh verification evidence.
- reconstruct_simulations.py regenerates all CSV and JSON files using Python and NumPy.

Run `python -m pip install numpy==2.3.5`, then `python reconstruct_simulations.py`.

All six summary rows agree with the precision printed in Table 3. The full spectrum formula was checked in 1,485 cases, including parameter values outside the positive-eigenvalue domain. The disconnected transfer is zero, the matched-radius comparison holds, and the driven clone has zero discrepancy over 128 updates. Alternative factorization residual is within floating-point precision. The random seed follows the paper; normal inputs and the alternative diagonal gains are explicit reconstruction choices because their original specifications are unavailable.

These are dimensionless synthetic model data. They are not patient data or empirical EEG. This supplement does not recover the original six-source manuscript hashes, original source code or original figure-generation files. Figure graphics are already present in the unchanged PDF.
