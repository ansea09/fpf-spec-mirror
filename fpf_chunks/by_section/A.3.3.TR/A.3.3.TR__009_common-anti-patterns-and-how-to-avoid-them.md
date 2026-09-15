---
chunk_kind: "child"
pattern_id: "A.3.3.TR"
pattern_title: "Construct a Rule for State Change"
section_id: "A.3.3.TR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.TR/A.3.3.TR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "98777b284b6a41fa3481a1230a16182d0f323c2a"
heading_path:
  - "A.3.3.TR — Construct a Rule for State Change"
  - "A.3.3.TR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 10022
line_end: 10032
dependencies:
  - "A.22.CGUS"
  - "A.3.3"
  - "A.3.3.CC"
  - "B.5.FM"
  - "B.5.MPC"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.TR:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Why it changes the result | Repair |
| --- | --- | --- |
| Replace saved-value updates with updates of the current value | Interference between read and write disappears from the model. | Retain the saved value and instruction position, or justify an atomic operation. |
| Conjoin alternative actions | The model demands incompatible changes at once and can lose legitimate executions. | State the alternatives and the condition enabling each one. |
| Leave a local action's other state values free | A model can introduce changes no participant performs. | State the unchanged values or the joint action that changes them. |
| Filter away violations of the property being investigated | The model excludes the failure instead of explaining whether the implementation prevents it. | Model the behavior or derive the prevention rule, then test the property. |
| Infer progress from preservation | An invariant can hold in a cycle with no useful completion. | Supply a decreasing measure, scheduling condition or other relevant progress argument. |
| Repair a missing interaction law by changing a numerical setting | The computation still lacks the relation needed to determine the modeled change. | Repair the subject account and then select a computation for it. |

