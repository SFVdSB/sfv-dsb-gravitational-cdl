# Reproducibility guide

## Which artifact is authoritative?

For **public v1.0.0**, the authoritative complete reproducibility artifact is the publication ZIP archived at Zenodo DOI `10.5281/zenodo.22070942`.

The GitHub `main` branch is a curated mirror. It carries claim/citation metadata and selected machine-readable checkpoints, but it is not required to duplicate the complete manuscript source, generated figures, large numerical profiles, or every checkpoint file contained in the immutable Zenodo archive.

During the Gate-A1 provenance audit on 2026-09-03:

- the standalone Zenodo manuscript PDF was byte-identical to the PDF embedded in the publication ZIP;
- every one of the 159 entries listed in the publication ZIP's `SHA256SUMS.txt` verified successfully;
- 131 of 132 same-path files shared with the internal GCDL v1.11.0 archive were byte-identical; the remaining same-path file was the checksum manifest, which necessarily differs because the package file sets differ;
- all 16 files curated into the publication `derivation/` directory were byte-identical to their corresponding v1.11 checkpoint/root sources.

## Core sequence inside the Zenodo publication ZIP

1. **Corrected flat O(4) anchor**
   - Read `reference/o4/O4_CLEAN_DERIVATION.md`.
   - Run the flat reproduction scripts under `reference/o4/scripts/`.
   - Compare with the frozen outputs under `reference/o4/results/`.

2. **Exact scalar–tensor equations**
   - Read `derivation/GCDL_1A_EXACT_COUPLED_EUCLIDEAN_EINSTEIN_SCALAR_DERIVATION.md`.
   - Run `scripts/gcdl_1a_symbolic_derivation.py`.

3. **Independent gravitating-background reproduction**
   - Read `derivation/GCDL_2A_INDEPENDENT_NUMERICAL_CDL_REPRODUCTION.md`.
   - Run `scripts/gcdl_2a_independent_numerical_reproduction.py`.

4. **Action ordering**
   - Read `derivation/GCDL_2B_GRAVITATING_ACTION_DOMINANCE_AND_COMPETING_SADDLES.md`.
   - Run `scripts/gcdl_2b_action_dominance.py`.

5. **Physical spectrum**
   - Read `derivation/GCDL_2C_PHYSICAL_SCALAR_METRIC_FLUCTUATION_SPECTRUM.md`.
   - Run `scripts/gcdl_2c_physical_fluctuation_spectrum.py`.

6. **Lorentzian continuation**
   - Read `derivation/GCDL_3A_LORENTZIAN_CONTINUATION_AND_INTERIOR_COSMOLOGICAL_BACKGROUND.md`.
   - Run `scripts/gcdl_3a_lorentzian_continuation.py`.

7. **Absolute-scale gate and final verdict**
   - Read `derivation/GCDL_3B_ABSOLUTE_SCALE_EXTRACTION_AND_DE_REOPENING_GATE.md`.
   - Read `derivation/GCDL_4_FINAL_GRAVITATIONAL_VERDICT.md`.
   - Run `scripts/gcdl_4_final_verdict.py`.

## Environment

Recommended baseline:

- Python 3.10+
- NumPy
- SciPy
- SymPy
- pandas

Some numerical scans are computationally intensive. Frozen outputs are included in the Zenodo release so they can be inspected independently of a full rerun.

## Historical benchmark warning

Do not use the executable `B ≈ 1424.5651` benchmark from Zenodo record `17187486` as the current O(4) anchor. That archive is retained as historical provenance. The corrected flat authority for this release is `B_flat = 1074.028378518535`.
