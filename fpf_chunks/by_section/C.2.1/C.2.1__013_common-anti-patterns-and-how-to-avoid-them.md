---
chunk_kind: "child"
pattern_id: "C.2.1"
pattern_title: "U.Episteme - Epistemes and their slot relation"
section_id: "C.2.1:12"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.1/C.2.1__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "C.2.1 — U.Episteme - Epistemes and their slot relation"
  - "C.2.1:12 — Common Anti-Patterns and How to Avoid Them"
line_start: 37114
line_end: 37122
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.6.5"
  - "A.7"
  - "B.1.3"
  - "C.2"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0-E.17.2"
  - "E.18"
keywords:
---

### C.2.1:12 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Carrier-as-episteme | A PDF, diagram, dashboard, repository, or database row is treated as the episteme itself. | Separate `U.Episteme`, `U.EpistemePublication`, publication face, carrier, and source relation. |
| EntityOfConcern drift | The thing being described changes while the same episteme label is kept. | Name the `EntityOfConcernSlot` value and any `EntityOfConcernChangeMode` explicitly. |
| View and viewpoint collapse | A view is treated as the stakeholder concern, or the viewpoint is treated as the view content. | Keep `ViewpointSlot` and `ViewSlot` distinct and use E.17 for multi-view publication. |
| Triangle-as-ontology | Symbol-Concept-Object is used as the normative episteme model. | Treat the triangle only as a didactic projection of `U.EpistemeSlotRelation`. |

