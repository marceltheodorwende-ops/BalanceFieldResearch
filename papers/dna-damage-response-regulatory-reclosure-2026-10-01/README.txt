DNA DAMAGE RESPONSE AND REGULATORY RECLOSURE
Preprint draft v0.1 - 1 October 2026

CONTENTS
The PDF is the reviewed reading version. The .tex file is editable manuscript source.
figures/: three plots, each as vector PDF and high-resolution PNG.
numerical_supplement/: four synthetic response CSVs, operator audit, frozen results,
reproduction code and dependencies.
source_manifest.json: BFG source filenames, SHA-256 hashes and used locations.
bibliographic_records.json: checked external scholarly records.

REPRODUCE
Install the listed dependencies into a suitable Python environment. Run:
  python numerical_supplement/reproduce.py
The script resolves outputs relative to itself, regenerates the synthetic CSV files,
results and figures, and checks trajectory positivity, step-halving agreement,
the exact damage solution, and the operator identities. No network access is used.
Parameters are deliberately illustrative, dimensionless and not fitted to cell data.
Model time is not calibrated to hours. No biological fate counts are generated.

LATEX
Compile the .tex file from this directory with the accompanying figures directory.
The supplied PDF was generated independently with ReportLab and visually checked.
The native editor compiler could not run because its standard platform directories
were unavailable; successful LaTeX compilation is not claimed for this package.

SCIENTIFIC STATUS
This is a theoretical preprint with conditional proofs and synthetic simulations,
not an empirical validation or a published/final author-approved version.
No external biological raw dataset is included. Author approval and final
submission declarations remain necessary before submission.
