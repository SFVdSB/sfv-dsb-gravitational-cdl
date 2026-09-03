# O(4) / gravitational-CDL provenance and archive map

**Status:** Gate-A1 provenance map  
**Last audited:** 2026-09-03

This file distinguishes scientific lineage from package/version labels. In particular, **internal GCDL running versions and public publication versions use different version namespaces**.

| Layer | Identifier | Classification | Numerical/physical role |
|---|---|---|---|
| Historical executable O(4) | Zenodo `10.5281/zenodo.17187486` / `cosmologicalModel.zip` | Historical; superseded as current authority | Negative-branch benchmark `B ≈ 1424.5651` at the older parameter point |
| Mixed historical local bundle | `OriginalO(4).zip` | Historical mixed bundle; not authoritative | Combines old 1424-era executable material with a later manuscript state; preserve only for provenance |
| Corrected flat O(4) | hostile-validation package under internal `reference/o4/` | **Current flat-space authority** | `B_flat = 1074.028378518535`, `R_peak = 5.860197706763`, `w_FWHM = 1.751789986342` |
| Gravitational working archive | internal `sfv-dsb-gravitational-cdl-running-v1.11.0` | **Current internal gravitational parent** | Completed GCDL checkpoint chain and final G-C verdict |
| Public archival release | Zenodo `10.5281/zenodo.22070942`, public `v1.0.0` | **Current authoritative public O(4)/CDL artifact** | Standalone PDF + complete publication ZIP curated from internal v1.11.0 |
| GitHub mirror | `SFVdSB/sfv-dsb-gravitational-cdl` | Current curated public mirror | Readable/code-facing mirror; full immutable archive remains Zenodo |

## Verified relationship between internal v1.11.0 and public v1.0.0

The Zenodo publication ZIP contains 160 files excluding directory entries. Comparing it with internal GCDL running v1.11.0:

- 132 paths occur under the same relative names;
- 131 of those 132 are byte-identical;
- the sole same-path difference is `SHA256SUMS.txt`, expected because the package contents differ;
- all 16 documents moved into publication `derivation/` are byte-identical to their corresponding internal checkpoint/root source files;
- publication-only additions are principally publication metadata, the manuscript source/PDF, and generated figure PDFs;
- internal-only omissions are working-control, prompt, provenance, DE-quarantine, and other internal program-management material not required in the curated publication release.

This supports the classification:

> **public GCDL v1.0.0 = faithful curated publication extraction of completed internal GCDL v1.11.0.**

## Zenodo 22070942 integrity

The record contains the standalone manuscript PDF and the complete publication ZIP. The standalone PDF and the PDF inside the ZIP have the same SHA-256:

`5a0f991f92fcdc890d62fba12d64b3f1730dba9897ed12c66c873ddb53380078`

All 159 files listed by the ZIP's `SHA256SUMS.txt` verified successfully during Gate A1.

## Historical record 17187486

The record contains only `cosmologicalModel.zip`. Its README/config/result files identify the older benchmark with approximately:

- `v = 9.0e-5`;
- `lambda = 1.3e-4`;
- `lambdaPhi = 0.1`;
- `g_portal = 2.0`;
- final `B = 1424.5651`.

That result is **not the current corrected O(4) anchor**. Keep the record for provenance; when editing Zenodo metadata, label it clearly as historical/superseded and point readers to DOI `10.5281/zenodo.22070942`.

## Version naming rule

Never use bare `v1.0.0` in cross-repository discussion. Use one of:

- **internal GCDL running v1.0.0** (early gravitational work stage), or
- **public GCDL publication v1.0.0** (completed release curated from internal v1.11.0).

## Authority rule for outreach

For Volkas/publication-readiness work:

1. use corrected flat O(4) `B_flat = 1074.028378518535` as the flat numerical authority;
2. use internal GCDL v1.11.0 for complete internal provenance/audit history;
3. cite Zenodo `10.5281/zenodo.22070942` as the authoritative public gravitational release;
4. treat Zenodo `17187486` and the mixed `OriginalO(4).zip` only as historical provenance.
