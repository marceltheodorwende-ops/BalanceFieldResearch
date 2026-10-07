# Real EEG covariance prediction experiment

The frozen protocol in PROTOCOL.md defines an explicit EEG bridge hypothesis for
the finite BFG kernel and a held-out comparison against persistence, linear
prediction and frozen geometry. Results have not yet been evaluated in this
branch state. The completed run replaces this file's role with README.md and
results/summary.json; do not interpret an initiated run as empirical evidence.

Source paper commit: 76d9e87b4275ec41b3dcd84434e2ee3791a8d076.
Protocol freeze commit: 37f31b1b8aae878418fe2510a55b7896bb114579.

Data: Schalk (2009), PhysioNet EEG Motor Movement/Imagery v1.0.0,
https://doi.org/10.13026/C28G6P, ODC-By 1.0. Original raw EDF files are downloaded
from PhysioNet and are not stored in Git. Measurement-derived tables retain
third-party attribution. Original code/documentation retain repository rights.

Reproduce with Python 3.12 and requirements.txt:

```
python -m unittest -v test_experiment
python experiment.py download
python experiment.py evaluate
python report.py
```

The GitHub workflow executes these commands and commits results to this dedicated
experiment branch only. It does not merge the experiment into main or change the
paper. Numerical unit controls use constructed inputs; the empirical evaluation
uses original EEG measurements. The EEG preparation and readout are additional
constitutive hypotheses, not laws derived by the source paper.
