# Finite-budget geometric input audit

P49 continues the exact actuator's resource dependency. See DERIVATION.md for proof, hypotheses, same-cost counterexample and preserved numerical failure. No joule/force calibration or universal impossibility claimed.

Run with numpy installed and the existing Ambient experiment.py importable:

    PYTHONPATH=<Ambient module directory> python check.py

Controls are synthetic mathematics/code checks only. No empirical files or holdout used. results/controls.json records finite reproducible checks; the general tail statement is proved separately.
