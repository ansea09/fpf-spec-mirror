---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "Bounded Model-Use Structure and DDD Bounded-Context Recovery"
section_id: "A.1.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__004_problem.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.1.1 — Bounded Model-Use Structure and DDD Bounded-Context Recovery"
  - "A.1.1:2 — Problem"
line_start: 1874
line_end: 1879
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.22"
  - "A.3.1"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.29"
  - "E.17.0"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
---

### A.1.1:2 - Problem

DDD bounded-context practice couples several real concerns: a model is defined and applicable within a boundary; actual systems in assigned roles use it; code and descriptions contain expressions of it; integration and maintenance work aims to keep those expressions consistent; and maps describe relationships among model uses. These are practical prompts to recover exact FPF claims, not evidence that maintenance caused coherence or that a described crossing obtains. Their objects are related, but they are not parts of one additional whole by that fact.

FPF needs this joint model-use relation organization selectable as `U.Structure` so it can serve as EntityOfConcern for comparison and maintenance work without becoming a heterogeneous holon, a description, or one universal semantic-locality reference.

