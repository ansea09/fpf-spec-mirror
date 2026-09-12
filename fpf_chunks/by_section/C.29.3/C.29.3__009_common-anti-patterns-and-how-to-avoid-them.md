---
chunk_kind: "child"
pattern_id: "C.29.3"
pattern_title: "Computational Realization"
section_id: "C.29.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.3/C.29.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.3 — Computational Realization"
  - "C.29.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 60793
line_end: 60803
dependencies:
  - "A.3.3"
  - "A.6.1"
  - "B.5.MPC"
  - "C.16"
  - "C.29.2"
keywords:
---

### C.29.3:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Why it fails here | Repair |
| --- | --- | --- |
| Send an unrepresentable answer | A signed field wraps or rejects a value that is valid in the calculation. | Change the encoding or realization, or restrict the admitted input. |
| Split a command without recovering composition | Two absolute targets do not add like relative increments. | Explain the state and rule connecting the completed commands. |
| Read the carrier by its familiar scale | The circuit's physical average uses a different decoding from its inputs. | Derive and use the receiving scale. |
| Infer exact occupancy from unavailable cards | Some assigned cards are outside during reservation or return. | Use the four-state account or retain the upper bound. |
| Treat one successful run as every required run | An untested endpoint or interleaving can change the result. | Supply the argument or evidence that covers the declared use. |
| Require a new trial for an adequate conditional design | The trial may leave the design decision unchanged. | Finish with the sufficient conditional consequence; obtain further information when its use warrants it. |

