---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__004_problem.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:2 — Problem"
line_start: 34928
line_end: 34938
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

### A.20:2 - Problem

How can FPF report internal constraint validity without:

- inventing a world-side `FlowConstraintValidity` relation whose participants are unspecified;
- using one status value for not applicable, not run, unknown, policy degradation, and gate blocking;
- requiring every specialist constraint for every transformation;
- suppressing independently useful gate-fit results after one local failure;
- copying publication, path, refresh, gate, or retargeting architecture into A.20; or
- treating an entity reference as a semantic bridge or requiring every retargeting to be reversible?

