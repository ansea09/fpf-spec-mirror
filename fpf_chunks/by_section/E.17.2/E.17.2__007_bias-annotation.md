---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:5.1"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__007_bias-annotation.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoints Bundle"
  - "E.17.2:5.1 — Bias-Annotation"
line_start: 79445
line_end: 79454
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.2:5.1 - Bias-Annotation

| Bias | How E.17.2 prevents it |
| --- | --- |
| Viewpoint-as-publication-face bias | `VP.*` ids are engineering viewpoint ids, not publication faces, publication forms, files, cards, or carriers. |
| Architecture-framework import bias | TEVB is an engineering viewpoint bundle over holons; architecture-specific viewpoint bundles remain separate species that may import TEVB. |
| Role-coordinate leakage | `VP.AllocationResponsibility` names a viewpoint, not a new `U.Role`, `U.RoleAssignment`, or allocation-responsibility root kind inside Description episteme signatures. |
| Viewpoint proliferation bias | Assurance, information, mission, deployment, and business labels remain separate bundle species or lexical family labels unless a new `U.ViewpointBundle` species is explicitly introduced. |
| EntityOfConcern drift | TEVB-aligned descriptions keep the selected holon as `EntityOfConcernRef` unless a governed retargeting pattern changes it. |

