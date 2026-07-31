---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__003_problem.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:2 — Problem"
line_start: 51202
line_end: 51207
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
  - "actual adverse condition"
  - "actual adverse episode"
  - "assessment and evidence separation"
  - "condition-to-predicate input rule"
  - "exact problem-for entity and use"
  - "independent criterion-applicability relation"
---

### C.22.PFR:2 - Problem

An actual Problem is neither a record nor a free-standing quality label. It depends on an actual condition and on a criterion that applies to one exact entity, scope, and interval. The relation obtains when the condition is on the adverse side of that applicable predicate.

FPF needs one identity for this dependent evaluative relation without copying values owned by `ProblemCriterionApplicabilityRelation` into additional writable PFR slots. It also needs to distinguish continuous adverse episodes from repeated episodes while refusing to infer a recovery from missing observations or evidence.

