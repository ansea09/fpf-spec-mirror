---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "FPF Pattern Publication Form for Evaluation Guidance"
section_id: "E.8.ECSPF:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__003_problem.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "E.8.ECSPF — FPF Pattern Publication Form for Evaluation Guidance"
  - "E.8.ECSPF:2 — Problem"
line_start: 73493
line_end: 73507
dependencies:
  - "A.19.ECS"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.8.ECSPF:2 - Problem

An author can use `A.19.ECS` to produce a good evaluation characteristic-space specification without yet having guidance on publishing that specification as an FPF pattern. The author can use `E.8` to produce a good generic FPF pattern without yet having guidance on where to place a coordinate set, object-kind-fit rule, evidence basis, result-row shape, calibration points, status set, and stop condition when they are the pattern's main content.

Recurring failures:

1. **Publication-form/content collapse.** The accepted specification, its `CharacteristicSpace`, the authored pattern, a later evaluation, and the evaluation result are treated as one object.
2. **Table-first pattern.** Coordinate rows arrive before evaluated object kind, use, first move, FPF-publication boundary, and object-kind boundary.
3. **Checklist substitution.** Conformance rows replace the `Solution` instead of checking a readable evaluation method.
4. **Underpublished values.** Coordinate names are present, but reader or qualification limits, value meanings, missingness, polarity, protected trade-offs, comparison rule, status meanings, neighbouring exits, or stop and reopen conditions are missing.
5. **Wrong-kind examples.** Worked cases show only passing examples, so the pattern cannot teach below-floor and outside-declared-object-kind boundary outcomes.
6. **Neighbour theft.** Claims about evidence, assurance, gates, work, decisions, naming, measurement, OEE or NQD, or mathematical lenses are carried as if this evaluation-characteristic-space pattern defined or justified them.
7. **Pattern-quality confusion.** The author uses `E.21` to judge whether the FPF pattern version is good, but forgets that the new pattern must still carry the accepted evaluation characteristic-space specification for one evaluated object kind by value.
8. **Quality-carrier leakage.** `E.21` values, corpus projection, README/ToC/E.11/I.2 alignment, retrieval, cold-reader evidence, monolith parity, landing evidence, or developer/reviewer/executor correspondence for the publication form are written into the evaluation pattern as if they were the evaluated object's method.

