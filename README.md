# SFV/dSB Gravitational O(4)/CDL Completion — public v1.0.0

This repository is the **curated GitHub mirror** of the published SFV/dSB gravitational O(4)/Coleman–De Luccia work.

**Manuscript:** *Gravitational Completion of the Corrected SFV/dSB O(4) Bounce: A Conditional Two-Field Coleman–De Luccia Theory*  
**Author:** Steven Hoffmann  
**Public version:** v1.0.0  
**Publication date:** 2026-08-23  
**Zenodo DOI:** `10.5281/zenodo.22070942`

## Authoritative publication and provenance

The full immutable public v1.0.0 artifact is the Zenodo record above. It contains:

- the standalone manuscript PDF;
- the complete publication ZIP with manuscript source and figures;
- gravitational checkpoint derivations;
- numerical scripts and machine-readable outputs;
- the corrected flat-O(4) hostile-validation package under `reference/o4/`;
- `SHA256SUMS.txt` covering the publication package.

The public v1.0.0 package was curated from the completed **internal GCDL running archive v1.11.0**. The GitHub `main` branch is maintained as a readable/code-facing mirror and may omit large archival binaries or profiles that remain preserved in the Zenodo release.

For the complete lineage, see `PROVENANCE_AND_ARCHIVE_MAP.md`.

## Main result

The corrected flat two-field O(4) bounce is promoted to a self-consistent leading scalar–tensor Coleman–De Luccia theory **conditional on supplied gravitational coefficients**.

Formal classification:

> **G-C — COMPLETE CONDITIONAL GRAVITATIONAL O(4)/CDL THEORY / ABSOLUTE NORMALIZATION NO-PASS**

The current corrected flat anchor is

- `B_flat = 1074.028378518535`;
- `R_peak = 5.860197706763`;
- `w_FWHM = 1.751789986342`.

The gravitational completion supports:

- exact coupled O(4) Einstein–scalar equations and Hamiltonian constraint;
- independent numerical reproduction of regular gravitating branches;
- tested compact/noncompact action ordering;
- CDL/Hawking–Moss merger with `kappa_HM = 4067.441310613605` on the minimal `C=xi_P=xi_q=0` diagnostic slice;
- one resolved physical tunneling negative mode under the declared Hamiltonian/Dirac (KLT-class) reduced contour;
- positive tested higher-angular sectors and the exact internal `U(1)_Phi` phase zero mode;
- Lorentzian continuation to an open-FRW interior and a complementary thick `dS3` wall worldvolume.

## Claim boundary

This work does **not** derive a unique physical value of

`{kappa = M_*^2/F^2, C, xi_P, xi_q}`

and retains one discrete gravity-source-law choice. It does not claim an absolute dark-energy prediction, and the Euclidean-gravity contour/formulation caveat is retained. See `CLAIM_BOUNDARY.md`.

## Historical O(4) record

Zenodo record `10.5281/zenodo.17187486` preserves an earlier 2025 O(4) repository (`cosmologicalModel.zip`) whose executable benchmark is approximately `B = 1424.5651`. That record is **historical and superseded as the current numerical authority**. It is retained for provenance and should not be substituted for the corrected `B_flat = 1074.0283785` anchor.

## Reproducibility

Use `REPRODUCIBILITY.md` for the reproduction sequence. For a complete clean-room reproduction, download the publication ZIP from Zenodo DOI `10.5281/zenodo.22070942`; the GitHub mirror is intentionally lighter than the archival package.

## Relationship to Phase B2 flavor

The separately published Phase B2 flavor construction uses the corrected O(4) scalar-wall background. The historical flavor DOI cited by the v1.0.0 gravitational release is `10.5281/zenodo.22059294`. Later flavor publication/version mapping is maintained separately and should be checked before outreach.

## Citation

Citation metadata are provided in `CITATION.cff`. Please cite the Zenodo DOI and manuscript when using this work.
