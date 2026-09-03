---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:13"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__017_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:13 — Common Anti-Patterns and How to Avoid Them"
line_start: 99452
line_end: 99467
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.1"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.LRN"
  - "E.10.MOVE"
  - "E.11"
  - "E.17.0"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
---

### F.17:13 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Why it fails | Repair |
| --- | --- | --- |
| Global glossary row | Removes the exact governed value, scheme, and local-sense claim. | Recover the exact value and one scheme-based cell; keep local wording local when that suffices. |
| One row for system-role kind and status | Fuses a work-facing system-role kind with a state-family value. | Split the rows and use the pattern that defines or constrains each value. |
| Evidence-role bucket | Turns evidence use, source use, assurance, and Work into one pseudo-kind. | Recover each claim under A.10, B.3, E.10.D2, or the pattern that defines or tests the source or Work claim. |
| Automatic card-cell-row chain | Treats the presence of one naming object as need for the next. | Apply F.14 separately at each gate and stop at the lightest sufficient object. |
| Merged viewpoint/view/conformance row | A dependent kind, another dependent kind, and their direct relation are treated as one naming result. | Keep separate `U.Viewpoint`, `U.View`, and `EpistemeViewpointConformanceRelation` rows and use E.17.0 for every membership or obtaining claim. |
| Spelling or suffix identity | Lets a familiar label, stable id, or `...@Context` form create or merge values. | Resolve the value under the pattern that defines or constrains it and treat only tokens fixed there as lineage. |
| Borrowed locality label as Tech name | Imports one tradition's commitments into the row and hides the effective interpretation basis. | Recover the governed value and scheme-based cell; select the designation under F.18 and cite an actual F.9 Bridge only when its separate predicate and use conditions hold. |
| Basis by source title | Replaces the exact cell and actual basis relation with a file or citation. | Recover the cell and two-participant basis relation; keep source-unit and publication facts separate. |
| Row as publication | Treats table presence, rendering, upload, form, or carrier as availability. | Use E.24.PUB for the selected row edition, audience, bounded use, form, and carrier. |
| Block as ontology or completeness proof | Treats navigation as subtype structure or row count as value evidence. | Keep blocks optional and judge the exact row use through reader recovery and blocked-use avoidance. |
| Row without its defining or constraining pattern | Lets F.17 govern the named object. | Point to the pattern that defines or constrains the value or stop the public-row path. |

