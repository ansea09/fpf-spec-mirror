---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__012_rationale.md"
commit_sha: "c7ac61bbaa8d3c10165b1a5a4a350956c87d77c9"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:10 — Rationale"
line_start: 33664
line_end: 33667
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

### A.20:10 - Rationale

Constraint truth, knowledge about that truth, and a policy response are different. A.20 records the evaluation result. The constraint's own pattern defines the truth condition. A.21 or another consumer decides what follows. Keeping those steps separate removes evaluation-order dependence and prevents a local validity pattern from becoming a second architecture for flows, publication, refresh, and gates.

