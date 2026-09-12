---
chunk_kind: "child"
pattern_id: "C.29.2"
pattern_title: "Computational Formulation"
section_id: "C.29.2:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.2/C.29.2__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.2 — Computational Formulation"
  - "C.29.2:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 60455
line_end: 60468
dependencies:
  - "A.10"
  - "A.3.1"
  - "A.3.3"
  - "A.6.1"
  - "A.6.3.RT"
  - "B.1.5"
  - "B.1.6"
  - "B.3"
  - "B.5"
  - "C.16"
  - "C.2.1"
  - "C.29.1"
  - "C.29.3"
  - "C.39"
  - "C.40"
keywords:
---

### C.29.2:8 - Common Anti-Patterns and How to Avoid Them

| Misuse | Repair |
| --- | --- |
| “Solve the constraints” is the algorithm | Supply an applicable solver or construct the search/update procedure, with its input class and result guarantee. |
| Store only the current answer estimate | Recover the control position, bounds, pending work or other information the next operation actually needs. |
| A branch chooses an exactly known sign of an arbitrary real value | Explain how that sign is obtainable from the available representation; use a justified enclosure or return the unresolved comparison. |
| The invariant holds, so the loop finishes | Supply the separate progress argument or state the continuing behavior actually intended. |
| A tiny equation residual proves a tiny answer error | Connect residual to output error under the applicable conditioning or other subject argument. |
| One matrix operation costs one step | Expand the operation count and storage for the actual matrix dimensions and representation. |
| The dense array fails, so no simulation is possible | Retain the dense-allocation rejection; examine the needed output and an applicable alternative algorithm. |
| A smaller numeric type is an exact compression | State the changed precision and establish the error consequence. |
| A reference simulator defines what the physical system did | Retain the computational result and use C.29.3 for preparation, execution and result-reading correspondence. |

