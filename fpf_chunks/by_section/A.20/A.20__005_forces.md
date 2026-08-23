---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__005_forces.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:3 — Forces"
line_start: 33124
line_end: 33133
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

### A.20:3 - Forces

| Need | Tension |
| --- | --- |
| Small local result | A user needs one check result, while later replay needs its constraint, case, and window. |
| Open constraint families | Different transformations carry different laws; a fixed universal checklist would create false requirements. |
| Truth and policy separation | Whether a constraint holds is not the same as what a gate does with the result. |
| Missing information | Not applicable, not run, unknown, and error lead to different next actions. |
| Reuse without fanout | A reusable result must be precise without copying every possible consumer's record and policy. |

