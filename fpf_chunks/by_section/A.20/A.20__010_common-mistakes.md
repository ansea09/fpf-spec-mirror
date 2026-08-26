---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:8"
section_title: "Common mistakes"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__010_common-mistakes.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:8 — Common mistakes"
line_start: 33649
line_end: 33659
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "A.6.1"
  - "A.6.4"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "E.17"
  - "E.18"
  - "E.20"
  - "F.9"
  - "G.11"
keywords:
---

### A.20:8 - Common mistakes

| Mistake | Why it fails | Repair |
| --- | --- | --- |
| Class label as truth | `LipschitzBounds` or `TypeDomainRange` does not identify the constraint application. | Name the constraint, edition, case, test, and result. |
| `abstain` for everything missing | Not applicable, not run, unknown, and policy consequence require different actions. | Keep applicability, evaluation state, outcome, and gate consequence separate. |
| Missing required result joins to pass | A neutral element erases incompleteness. | Use the complete required-set summary rule. |
| Constraint failure suppresses GateFit | Independent repair information disappears and results depend on evaluation order. | Preserve each applicable result; let A.21 combine them. |
| A.20 becomes a package architecture | Publication, paths, refresh, and gate fields are copied into a local result. | Keep only the result and cite the consumer's pattern. |
| Entity reference becomes bridge | Retargeting and semantic correspondence are confused. | Use A.6.4; add F.9 only for a separate cross-semantic claim. |

