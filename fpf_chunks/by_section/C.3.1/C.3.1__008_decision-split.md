---
chunk_kind: "child"
pattern_id: "C.3.1"
pattern_title: "U.Kind and U.SubkindOf Core"
section_id: "C.3.1:6"
section_title: "Decision Split"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.1/C.3.1__008_decision-split.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "C.3.1 — U.Kind and U.SubkindOf Core"
  - "C.3.1:6 — Decision Split"
line_start: 39975
line_end: 39983
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

### C.3.1:6 - Decision Split

| Source cue | C.3.1 disposition |
| --- | --- |
| "This claim ranges over cooling pumps." | Create or cite the context-local `U.Kind` for cooling pump. |
| "Cooling pump is a subkind of pump." | Declare `U.SubkindOf(CoolingPumpKind, PumpKind)` in the context. |
| "CoolingPump should become a public FPF U-kind." | Use `E.24.UK`, `A.11`, and `A.8` as needed. |
| "`U.WorkPlan` depends on `U.Work`." | Do not encode as `U.SubkindOf` unless C.3 typed reasoning actually claims a subkind order. Use the governing work or E.24.UK settlement. |

