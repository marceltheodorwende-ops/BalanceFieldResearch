# The Balance Field Equation as a Recursive World Formula

A finite operator model with geometric self feedback and explicit physical bridge requirements.

**Marcel Theodor Wende · Preprint dated 6 October 2026**

[Read the original PDF](BFG_Balance_Field_Equation_Preprint.pdf) · [Model and emergence sequence](docs/MODEL.md) · [Claim and proof status](docs/CLAIM_STATUS.md) · [32 illustrated panels](docs/FIGURES.md) · [References](docs/REFERENCES.md)

The paper defines a finite recursive state on unitary equivalence classes, with spectral selection, polar transport, endogenous geometry and weights, ambient reduced SVD, R4 realignment, and an explicit seed or terminal rule. Its central state is $\Xi=(K,\rho_F,\rho_W,Y,P)$.

Geometric feedback is part of the update: the current load geometry shapes the metric and analysis operator, whose singular values determine the next load geometry. Scalar damping is established on a declared control branch. This does not establish universal contraction of the complete endogenous state or a physical theory of every system.

Physical information, time in seconds, spacetime, gravitation, particle observables, atoms, molecules, biology, and experience require separately specified measurement and transition bridges. The package preserves the manuscript's distinction between mathematical consequences, constitutive assumptions, and open physical transitions.

## Contents

| Path | Contents |
| --- | --- |
| `BFG_Balance_Field_Equation_Preprint.pdf` | User-supplied PDF, preserved byte for byte; 68 pages |
| `docs/MODEL.md` | State types, update order, feedback and later transitions |
| `docs/CLAIM_STATUS.md` | Conditional results, assumptions and open obligations |
| `docs/FIGURES.md` | English captions and all 32 original figure assets |
| `docs/REFERENCES.md` | Bibliography transcribed from the supplied paper |
| `docs/PREPRINT_TEXT.txt` | Searchable page-wise PDF text extraction; the PDF controls formula typography |
| `figures/` | PNG panels prepared for this paper |
| `data/` | Matching synthetic grids and figure manifest |
| `SHA256SUMS.txt` | Integrity hashes of package files |

## Numerical panels

The `.npz` files contain the numerical grids used for the computational illustrations. Inspect a file with NumPy: `np.load("data/figure_01.npz", allow_pickle=False)`. These are synthetic illustration/control data, not measurements from natural systems. Schematic and conventional physical-model panels are explicitly labelled in the figure guide. No standalone complete-kernel simulator is claimed by this package.

## Source and rights

The supplied PDF is the authoritative publication artifact. Documentation summarizes it and does not replace its assumptions or proofs. The repository [rights notice](../../LICENSE) applies; this package introduces no new license. The PDF's author/contact/ORCID information is retained in the original document.
