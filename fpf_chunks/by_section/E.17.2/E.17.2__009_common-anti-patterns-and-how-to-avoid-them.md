---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:6.1"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoints Bundle"
  - "E.17.2:6.1 — Common Anti-Patterns and How to Avoid Them"
line_start: 75301
line_end: 75309
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

### E.17.2:6.1 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Correction |
| --- | --- | --- |
| Functional view means the diagram | A functional diagram, card, or dashboard is treated as `VP.Functional` itself. | Keep `VP.Functional` as the viewpoint; model the diagram or card through Description, view, publication face, or publication form machinery. |
| Architecture framework becomes TEVB | A 4+1, UAF, NAF, SysML, or local framework is imported as the FPF viewpoint bundle. | Map it to TEVB or to a separate architecture-specific `U.ViewpointBundle` species. |
| Responsibility view becomes role assignment | A responsibility-oriented view adds `U.Role` or `U.RoleAssignment` as a Description-episteme coordinate. | Keep responsibility as viewpoint content; use `A.2`, `A.2.1`, and `A.15` when a work-facing role assignment is actually claimed. |
| Extra viewpoint by label | Information, assurance, mission, or deployment labels are added directly to `TEVB.EngBundle.viewpoints`. | Introduce a separate bundle species or keep the label as a transformation-flow family label where appropriate. |

