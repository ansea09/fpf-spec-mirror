---
chunk_kind: "child"
pattern_id: "C.29.AV"
pattern_title: "Derive a Condition from an Admissible Variation"
section_id: "C.29.AV:10"
section_title: "Architectural Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.AV/C.29.AV__011_architectural-rationale.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "C.29.AV — Derive a Condition from an Admissible Variation"
  - "C.29.AV:10 — Architectural Rationale"
line_start: 64801
line_end: 64808
dependencies:
  - "B.5.MPC"
  - "B.5.RR"
  - "C.29"
  - "C.29.2"
keywords:
---

### C.29.AV:10 - Architectural Rationale

The admissible family, change calculation and conclusion are separated because each can fail independently. A correct difference can describe impossible candidates. An admissible comparison can yield only a necessary condition. A strong mathematical result can still use a criterion that does not answer the practitioner's question.

Finite differences provide the direct comparison whenever they are manageable. Derivatives expose local structure economically, and sufficiency theorems can extend that information under additional hypotheses. Keeping these routes connected lets the reader use the least machinery that obtains the needed result.

The same construction spans a resource allocation and a continuous history. What carries across is the preservation of conditions and reasoning from the resulting change. The cost model and the physical action retain their different origins and uses.

