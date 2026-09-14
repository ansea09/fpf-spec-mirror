---
chunk_kind: "child"
pattern_id: "C.29.AV"
pattern_title: "Derive a Condition from an Admissible Variation"
section_id: "C.29.AV:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.AV/C.29.AV__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "f965ffb27d69ec5e4ae94f1bb0092c15fa13c991"
heading_path:
  - "C.29.AV — Derive a Condition from an Admissible Variation"
  - "C.29.AV:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 64784
line_end: 64794
dependencies:
  - "B.5.MPC"
  - "B.5.RR"
  - "C.29"
  - "C.29.2"
keywords:
---

### C.29.AV:8 - Common Anti-Patterns and How to Avoid Them

| Observed or text-invited mistake | Repair |
| --- | --- |
| Vary each allocation independently while retaining a fixed-total claim. | Couple the changes so the total remains fixed and derive their allowed range. |
| Use a tangent displacement as a finite feasible move on a curved constraint. | Construct a feasible curve or retain only the first-order conclusion supported by the tangent argument. |
| Accept a zero derivative as a minimum. | Determine the remaining change or use a sufficiency theorem with its hypotheses. |
| Reject a boundary optimum because its unrestricted derivative is nonzero. | Test the available one-sided or constrained changes. |
| Apply a small-step sign to an arbitrarily large step. | Calculate the finite difference or bound the remainder over that step. |
| Declare global optimality after testing one restricted family. | Supply the missing coverage or limit the conclusion to that family. |

