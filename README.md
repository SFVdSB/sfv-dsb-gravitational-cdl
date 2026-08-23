# SFV/dSB Gravitational O(4)/CDL Completion — v1.0.0

**Suggested GitHub repository:** `SFVdSB/sfv-dsb-gravitational-cdl`

This repository accompanies the standalone manuscript:

> **Gravitational Completion of the Corrected SFV/dSB O(4) Bounce: A Conditional Two-Field Coleman–De Luccia Theory**

Author: Steven Hoffmann  
Version: v1.0.0  
Date: 2026-08-23

## Main result

The corrected flat two-field O(4) bounce is promoted to a self-consistent leading scalar–tensor Coleman–De Luccia theory **conditional on supplied gravitational coefficients**.

Formal classification:

> **G-C — COMPLETE CONDITIONAL GRAVITATIONAL O(4)/CDL THEORY / ABSOLUTE NORMALIZATION NO-PASS**

The repository supports:

- corrected flat O(4) bounce: `B_flat = 1074.0283785`;
- exact coupled O(4) Einstein–scalar equations and constraint;
- independent numerical reproduction of regular gravitating branches;
- tested compact/noncompact action ordering;
- CDL/Hawking–Moss merger, with `kappa_HM = 4067.441310613605` on the minimal `C=xi_P=xi_q=0` diagnostic slice;
- one resolved physical tunneling negative mode under the declared Hamiltonian/Dirac (KLT-class) reduced contour;
- positive tested higher-angular sectors and the exact internal U(1)_Phi phase zero mode;
- Lorentzian continuation to an open-FRW interior and a complementary thick dS3 wall worldvolume.

## Explicit claim boundary

This repository **does not derive** a unique physical value of

`{kappa = M_*^2/F^2, C, xi_P, xi_q}`

and retains one discrete gravity-source-law choice. It does not claim an absolute dark-energy prediction. The general Euclidean-gravity contour ambiguity is also retained.

## Repository structure

- `paper/` — LaTeX manuscript and figures.
- `derivation/` — gravitational checkpoint derivations and final verdict.
- `scripts/` — symbolic/numerical reproduction scripts.
- `results/` — machine-readable numerical outputs.
- `reference/o4/` — corrected flat O(4) derivation and hostile-validation controls.
- `CITATION.cff` — citation metadata.
- `.zenodo.json` — Zenodo deposition metadata template.
- `REPRODUCIBILITY.md` — reproduction guide.
- `CLAIM_BOUNDARY.md` — publication claim boundary.

## Reproducing the main checkpoints

Python dependencies are intentionally lightweight: NumPy, SciPy, SymPy, and pandas are sufficient for the core scripts. Run scripts from the repository root. Individual scripts write or verify outputs under `results/`.

The authoritative derivation history is preserved in `derivation/`.

## Relationship to Phase B2 flavor

The separately published Phase B2 flavor package uses the corrected O(4) scalar-wall background:

DOI: `10.5281/zenodo.22059294`

This repository provides the standalone corrected/gravitational O(4) foundation that should be cited by later SFV/dSB cosmology papers.

## Before publishing

1. Create the GitHub repository, preferably `SFVdSB/sfv-dsb-gravitational-cdl`.
2. Upload this repository as the initial `v1.0.0` release.
3. Connect/archive the GitHub release with Zenodo.
4. Zenodo DOI for this release: `10.5281/zenodo.22070942`.
5. Choose the code/document license you want before public release. No license has been silently selected in this package.
