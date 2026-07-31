---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:12b"
section_title: "Lowering, repair, and refresh conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__015_lowering-repair-and-refresh-conditions.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:12b — Lowering, repair, and refresh conditions"
line_start: 25456
line_end: 25463
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

### A.15.3:12b - Lowering, repair, and refresh conditions

Use ordinary A.15.2 plan content when no reusable declaration member is needed. When typed use is needed, return `missing-governor` if the intended-performance designator, declaration edition, member designator, designation rule, cardinality, actual-use predicate, or defining pattern is missing; an operation argument or result also requires its operation designator. Do not replace that blocker with a generic slot-bearing description.

State prohibitions, exclusions, required absence, and completeness under their plan-constraint or negative-claim patterns instead of using omission or an empty filler. A later missing-filler, substitution, or variance result needs a comparison policy whose closure or negative criterion applies to the case facts.

Revise the WorkPlan ClaimGraph when the target member, planned value, intended-performance designator, condition, or relied-on declaration edition changes. If a C.2.1 identity discriminator changes, identify another WorkPlan episteme and relate it to the earlier one only when `EpistemeEditionRelation` obtains. Preserve the earlier WorkPlan reference already cited by work or another actual use. Refresh only a declaration, reference resolution, policy, or WorkPlan episteme whose changed resolution would alter the later decision; re-evaluate an actual-use change under its relation predicate or A.6.1 application predicate.

