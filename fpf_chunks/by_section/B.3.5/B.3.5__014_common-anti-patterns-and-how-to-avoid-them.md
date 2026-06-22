---
chunk_kind: "child"
pattern_id: "B.3.5"
pattern_title: "Working-Model Relations & Grounding (CT2R-LOG)"
section_id: "B.3.5:12"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.5/B.3.5__014_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "B.3.5 — Working-Model Relations & Grounding (CT2R-LOG)"
  - "B.3.5:12 — Common Anti-Patterns and How to Avoid Them"
line_start: 34536
line_end: 34544
dependencies:
  - "B.3"
  - "C.13"
  - "E.14"
keywords:
  - "CT2R"
  - "Compose-CAL"
  - "assurance layer"
  - "constructive trace"
  - "grounding"
  - "working model"
---

### B.3.5:12 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What goes wrong | Repair |
| --- | --- | --- |
| Constructive-trace replacement | A `Gamma_m` trace is treated as the public relation, so engineers lose the readable Working-Model edge. | Keep the Working-Model relation canonical and attach the trace only as grounding. |
| Unchecked relation label | A familiar part-whole label is published without naming the intended relation kind or validation mode. | Declare the Working-Model relation, `validationMode`, and the grounding or evidence relation that makes the edge reviewable. |
| Order/time leakage | Assembly sequence, phase, or parallel work is encoded as a part-whole edge. | Keep order, method, and temporal claims adjacent to the structural edge; do not turn them into mereology. |
| Assurance by notation | A diagram, graph display, or data format is treated as if it made the relation true. | Treat representations as publication forms; keep the relation claim, grounding relation, and validation mode explicit. |

