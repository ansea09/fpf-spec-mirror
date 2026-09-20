---
chunk_kind: "child"
pattern_id: "A.1.RI"
pattern_title: "Reidentifying an Object across Observations"
section_id: "A.1.RI:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.RI/A.1.RI__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "1fa007d1110d961d54ced2fa58e08177663c401f"
heading_path:
  - "A.1.RI — Reidentifying an Object across Observations"
  - "A.1.RI:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 2146
line_end: 2155
dependencies:
  - "A.1"
  - "A.3.3.PI"
  - "A.3.3.TR"
  - "B.5.RR"
  - "B.5.TC"
  - "B.5.TU"
  - "C.11.DUA"
  - "C.16.IR"
  - "C.16.MR"
  - "C.2.1"
keywords:
---

### A.1.RI:8 - Common Anti-Patterns and How to Avoid Them

| Failure in these situations | Consequence | Repair |
| --- | --- | --- |
| Treat a reused label as uninterrupted object continuity | Resource totals or actions can be assigned to another run or object. | Apply the relevant lifecycle or continuity rule to the available observations. |
| Accept a plausible pair without its shared constraints | Another object loses its only possible observation. | Compare the complete associations that must hold together. |
| Report the best-ranked connection as the only possible one | A scoring preference becomes an unsupported identification. | Keep the ranking assumption and test alternatives when uniqueness matters. |
| Require identity resolution for an invariant aggregate | Additional observation delays a result already determined. | Evaluate the receiving quantity across the surviving associations. |
| Treat a failed model as evidence that one convenient association is true | Contradictory observations or rules remain hidden in later reasoning. | Locate the incompatible premise or observation and repair that contribution. |

