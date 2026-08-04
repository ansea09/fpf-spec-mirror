---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:12a"
section_title: "P2W planned-filling use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__014_p2w-planned-filling-use.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:12a — P2W planned-filling use"
line_start: 25587
line_end: 25592
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

### A.15.3:12a - P2W planned-filling use

When P2W reaches intended work and a planned value reuses a declaration member admitted by 4.1, carry the WorkPlan, intended-performance designator, declaration edition, member designator, defining pattern, planned value, and each condition or pin whose change would alter the effective planned value or later comparison. The declaration pattern defines the member and actual-use rule; A.15.2 and A.15.3 state the intention. P2W creates neither the declaration, plan claim, participant, nor application binding.

If no reusable member is needed, carry ordinary A.15.2 plan content. If typed planned use is needed but the member, its meaning, its actual-use predicate, or its defining pattern is absent, carry `missing-governor` for that intended use. A planned-filling row does not carry performed work, readiness, evidence, gate, result, measurement, publication, delivery, acceptance, exclusion, or completeness claims. Preserve each separately—for example, A.15.1 identifies performed Work and A.15.5 decides work-entry readiness.

