---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:15"
section_title: "Worked Bundle Families"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__016_worked-bundle-families.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:15 — Worked Bundle Families"
line_start: 79742
line_end: 79781
dependencies:
  - "A.16.0"
  - "A.22"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.13"
  - "C.2.1"
  - "C.2.2a"
  - "C.29"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "E.7"
  - "F.9"
  - "F.9.1"
keywords:
  - "alias discipline"
  - "engineering/management/research bundles"
  - "governance"
  - "import discipline"
  - "reusable viewpoint family"
  - "viewpoint bundle"
---

### E.17.1:15 - Worked Bundle Families

#### E.17.1:15.1 - TEVB engineering family

A TEVB engineering bundle for holons may include exact `U.ViewpointRef` members such as:

- `ref(VP.Functional)`,
- `ref(VP.Procedural)`,
- `ref(VP.AllocationResponsibility)`,
- `ref(VP.ModuleInterface)`.

Each listed reference resolves the exact viewpoint episteme P designated by the `VP.*` token inside `ref(...)`. The important point is not the vocabulary alone. The bundle states that these viewpoints are intended to recur together for one engineering family of concerns. A later description family then imports that exact engineering bundle edition and its needed references rather than re-inventing a local list of "roughly similar" viewpoints.

#### E.17.1:15.2 - Governance and risk family

A governance bundle may group exact `U.ViewpointRef` members such as:

- `ref(VP.Risk)`,
- `ref(VP.Control)`,
- `ref(VP.Compliance)`,
- `ref(VP.Operations)`.

Each listed reference resolves the exact viewpoint episteme P designated by the `VP.*` token inside `ref(...)`. This bundle is valuable precisely because the four viewpoints recur together but are not interchangeable. Keeping their exact references in one family edition makes the reuse visible while preserving each member's distinct meaning.

#### E.17.1:15.3 - Research-method family

A research-method bundle may include exact `U.ViewpointRef` members such as:

- `ref(VP.Theory)`,
- `ref(VP.Experiment)`,
- `ref(VP.Inference)`,
- `ref(VP.Limitations)`,
- and, where appropriate, `ref(VP.Reproducibility)`.

Each listed reference resolves the exact viewpoint episteme P designated by the `VP.*` token inside `ref(...)`. A local inquiry note might import only three exact references, but the import remains legible because the omitted members still belong to one reviewed source bundle edition rather than disappearing into ad hoc prose.

#### E.17.1:15.4 - Cross-family description relation positions

A serious project may use TEVB engineering viewpoints for the design family, a governance bundle for program oversight, and a publication-oriented family for public publication faces and publication forms. `E.17.1` keeps these relation positions reviewable by preserving which bundle each viewpoint came from and by preventing the final publication face or publication form from masquerading as the viewpoint library itself.

