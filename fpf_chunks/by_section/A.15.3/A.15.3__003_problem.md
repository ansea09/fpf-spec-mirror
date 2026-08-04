---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__003_problem.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:2 — Problem"
line_start: 25329
line_end: 25338
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.6.1"
  - "A.6.5"
  - "A.6.RCD"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "U.WorkPlan"
keywords:
  - "WorkPlan claim content"
  - "actual-use predicate"
  - "baseline replay"
  - "concrete RefKind and policy"
  - "direct owner"
  - "edition pin"
  - "exact declaration member"
  - "intended-performance designator"
  - "no actuality by plan"
  - "open-world omission"
  - "participant/argument/result meaning"
  - "positive planned designation"
  - "semantic cardinality"
---

### A.15.3:2 - Problem

Without this boundary, five failures recur:

1. **Generic slot creation.** Any description field named input, output, role, result, or parameter is treated as a SlotSpec.
2. **Declaration-family collapse.** RelationSignature SlotSpecs and operation arguments or results are placed in one undifferentiated slot schema.
3. **Plan-as-actual inference.** A planned value is treated as an obtaining relation participant or actual operation binding.
4. **Description-as-declaration inference.** A `U.MethodDescription` that mentions an input or effect is treated as if it declared a reusable participant locus.
5. **Baseline rewrite.** Performed values are copied back into the plan, erasing substitution and variance.

