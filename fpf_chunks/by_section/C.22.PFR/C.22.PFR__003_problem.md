---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__003_problem.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:2 — Problem"
line_start: 66041
line_end: 66046
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.22"
  - "C.22.2"
  - "E.18.1"
  - "E.23"
  - "G.11"
keywords:
---

### C.22.PFR:2 - Problem

An actual Problem depends on an actual condition and on a criterion that applies to one entity, scope, and interval. It is neither a record nor a free-standing quality label. The relation obtains when the condition is on the adverse side of that applicable predicate.

FPF needs one identity for this dependent evaluative relation without copying values defined by `ProblemCriterionApplicabilityRelation` into additional writable PFR slots. It also needs to distinguish continuous adverse episodes from repeated episodes without inferring a recovery from missing observations or evidence.

