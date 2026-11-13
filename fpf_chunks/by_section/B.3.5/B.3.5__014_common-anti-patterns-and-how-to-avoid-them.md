---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
section_id: "B.3.5:12"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__014_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "B.3.5 — Assurance Grounding for Working-Model Relation Claims (CT2R-LOG)"
  - "B.3.5:12 — Common Anti-Patterns and How to Avoid Them"
line_start: 47591
line_end: 47599
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
---

### B.3.5:12 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Trace as relation or truth-maker | A `Gamma_m` trace is treated as the public relation or the source of whole identity, or its presence or notation is treated as proof that the relation obtains. | Keep the Working-Model relation canonical; recover the relation facts and reidentification rule independently; attach the trace only as their inspectable C.2.1 account. |
| Unchecked relation label or mode | A familiar relation label or `axiomatic` flag is published as though either settled relation obtaining or identity. | State and test the relation first. When B.3.5 is elected, add the branch-specific mode and support account. Stop when a fact required by the relation's defining pattern is missing. |
| Order/time leakage | Sequence, phase labels or parallel timing are treated as sufficient evidence of parthood. | Recover each relation separately: A.15.1 for Work parts, A.14 for a proper phase of an unchanged non-Work carrier, and B.1.4 for aggregation of recovered order or temporal relations. |
| Assurance by notation | A diagram, graph display, or data format is treated as if it made the relation true. | Use the display to present the relation claim and establish its grounds under the relation rule. When this profile is elected, state its grounding relation and validation mode. |

