---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:15"
section_title: "Worked Bundle Families"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__016_worked-bundle-families.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:15 — Worked Bundle Families"
line_start: 59068
line_end: 59107
dependencies:
  - "A.16.0"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.2.2a"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.7"
  - "F.9"
  - "F.9.1"
  - "U.MultiViewDescribing"
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

A TEVB engineering bundle for holons may include viewpoints such as:

- `VP.Functional`,
- `VP.Procedural`,
- `VP.RoleEnactor`,
- `VP.ModuleInterface`.

The important point is not the vocabulary alone. The bundle states that these viewpoints are intended to recur together for one engineering family of concerns. A later description family then imports that engineering bundle rather than re-inventing a local list of "roughly similar" viewpoints.

#### E.17.1:15.2 - Governance and risk family

A governance bundle may group viewpoints such as:

- `VP.Risk`,
- `VP.Control`,
- `VP.Compliance`,
- `VP.Operations`.

This bundle is valuable precisely because the four viewpoints recur together but are not interchangeable. Keeping them as one family id makes the reuse visible while still preserving the distinct member meanings.

#### E.17.1:15.3 - Research-method family

A research-method bundle may include viewpoints such as:

- `VP.Theory`,
- `VP.Experiment`,
- `VP.Inference`,
- `VP.Limitations`,
- and, where appropriate, `VP.Reproducibility`.

A local inquiry note might import only three of these viewpoints, but the import remains legible because the omitted ones still belong to a reviewed family rather than disappearing into ad hoc prose.

#### E.17.1:15.4 - Cross-family description stack

A serious project may use TEVB engineering viewpoints for the design family, a governance bundle for program oversight, and a publication-oriented family for public surfaces. `E.17.1` makes this stack lawful by preserving which bundle each viewpoint came from and by preventing the final publication surface from masquerading as the viewpoint library itself.

