---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__003_problem.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:2 — Problem"
line_start: 72691
line_end: 72705
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

`A.19.ECS` can produce a good evaluation characteristic-space specification without saying how to publish that specification as an FPF pattern. `E.8` can produce a good generic FPF pattern without saying how a coordinate set, object-kind-fit rule, evidence basis, result-row shape, calibration points, status set, and stop condition should be placed when they are the pattern's main payload.

Recurring failures:

1. **Publication-form/content collapse.** The FPF pattern is treated as the evaluation itself, instead of a publication form for an evaluation characteristic-space specification.
2. **Table-first pattern.** Coordinate rows arrive before evaluated object kind, use, first move, FPF-publication boundary, and object-kind boundary.
3. **Checklist substitution.** Conformance rows replace the `Solution` instead of checking a readable evaluation method.
4. **Underpublished values.** Coordinate names are present, but value meanings, missingness, polarity, protected trade-offs, status meanings, or stop conditions are missing.
5. **Wrong-kind examples.** Worked cases show only passing examples, so the pattern cannot teach below-floor and outside-declared-object-kind boundary outcomes.
6. **Neighbour theft.** Evidence, assurance, gate, work, decision, naming, measurement, OEE/NQD, or mathematical-lens claims are carried as if the evaluation-characteristic-space pattern governed them.
7. **Pattern-quality confusion.** The author uses `E.21` to judge whether the FPF pattern version is good, but forgets that the new pattern must still publish the evaluation for one evaluated object kind by value.
8. **Quality-carrier leakage.** `E.21` values, corpus projection, README/ToC/E.11/I.2 alignment, retrieval, cold-reader evidence, monolith parity, landing evidence, or developer/reviewer/executor correspondence for the publication form is written into the evaluation pattern as if it were the evaluated object's method.

