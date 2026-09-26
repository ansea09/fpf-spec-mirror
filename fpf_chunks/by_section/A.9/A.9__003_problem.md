---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Choose and Check an Aggregation Law for the Intended Result"
section_id: "A.9:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__003_problem.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "A.9 — Choose and Check an Aggregation Law for the Intended Result"
  - "A.9:2 — Problem"
line_start: 23995
line_end: 24003
dependencies:
  - "A.19.CN"
  - "A.19.ULSAM"
  - "B.1"
  - "B.2"
  - "C.29"
keywords:
  - "aggregation law"
  - "bounds"
  - "cross-scale consistency"
  - "dependency model"
  - "intended result"
  - "ordered composition"
  - "singleton identity"
---

### A.9:2 - Problem

| Failure | Practical consequence |
|---|---|
| An operation is chosen from the numbers alone. | A sum, minimum or product answers a different question from the one the receiver needs. |
| A roll-up hides dependence, overlap or interaction. | Repeated evidence is counted as independent, or component claims are promoted to an unsupported whole claim. |
| Reordering or repartitioning is assumed harmless. | Ordered Methods or numerical computation return a different result. |
| Failure of an aggregation model is treated as a new whole. | A repairable model premise is confused with the independent identity question. |

