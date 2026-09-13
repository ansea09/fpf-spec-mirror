---
chunk_kind: "child"
pattern_id: "C.29.SC"
pattern_title: "Derive a Consequence from a Symmetry"
section_id: "C.29.SC:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.SC/C.29.SC__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "bbfb5347013400e9a895fa4b0f66992e931c0ece"
heading_path:
  - "C.29.SC — Derive a Consequence from a Symmetry"
  - "C.29.SC:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 64994
line_end: 65004
dependencies:
  - "A.3.3.TR"
  - "C.29.1"
  - "C.29.2"
  - "C.29.AV"
keywords:
---

### C.29.SC:8 - Common Anti-Patterns and How to Avoid Them

| Text-invited mistake | Repair |
| --- | --- |
| Swap components but ignore their different costs. | Apply the transformation to the complete criterion and identify whether the data remain fixed. |
| Infer a symmetric individual solution from a symmetric solution set. | Establish uniqueness or retain the whole transformed family of solutions. |
| Rotate a law while silently keeping changed initial data as the same problem. | Track the transformed initial or boundary values. |
| Demand an invariant output when the task needs an equivariant position or direction. | Specify and apply the output action. |
| Normalize an input and lose the original coordinate relation. | Retain the transformation needed to return the answer or expose the remaining ambiguity. |
| Infer physical conservation from an equivariant update alone. | Derive the quantity's change along the actual dynamics or numerical step. |

