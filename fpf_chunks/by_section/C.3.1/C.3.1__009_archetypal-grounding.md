---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:7"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__009_archetypal-grounding.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:7 — Archetypal Grounding"
line_start: 40282
line_end: 40289
dependencies:
  - "A.1"
  - "A.11"
  - "A.2.6"
  - "A.8"
  - "C.2.3"
  - "C.3"
  - "C.3.2"
  - "C.3.3"
  - "E.24.UK"
  - "F.5"
  - "F.8"
keywords:
  - "kind"
  - "partial order"
  - "subkind"
  - "type hierarchy"
---

### C.3.1:7 - Archetypal Grounding

| Situation | C.3.1 move | Boundary |
| --- | --- | --- |
| "Cooling pump is a pump." | Declare a context-local `U.SubkindOf(CoolingPumpKind, PumpKind)` relation. | Do not infer a durable `U.CoolingPump` root kind. |
| "WorkPlan depends on Work." | Use the governing work or E.24.UK relation. | Do not encode dependency as `U.SubkindOf` unless a real kind partial order is being claimed. |
| "Safety-critical function is a kind of function." | Use a local `U.Kind` and subkind order for the current claim. | Membership and intent detail go to C.3.2; public FPF naming goes to Part F after U-kind admission. |

