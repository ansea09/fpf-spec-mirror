---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:12a"
section_title: "P2W planned-filling use"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__014_p2w-planned-filling-use.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:12a — P2W planned-filling use"
line_start: 25375
line_end: 25380
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

When P2W reaches intended work and one planned value depends on a reusable declaration admissible under A.15.3:4.1, carry the exact WorkPlan, intended-performance designator, target declaration edition, declaration member, direct owner, positive planned value or designation, and relied-on conditions or pins. The declaration's direct pattern must own the member's reusable meaning and corresponding later actual-use predicate; A.15.2 and A.15.3 own the intended-use claim. P2W defines neither the declaration nor the plan claim and turns no row into an actual participant or application binding.

If no reusable member is needed, carry ordinary A.15.2 plan content. If typed planned use is needed but the declaration member, reusable meaning, corresponding actual-use predicate, or direct owner is absent, carry the exact missing-governor blocker. If the source wording also carries performed-work, readiness, evidence, gate, result, measurement, publication, refresh, delivery, acceptance, exclusion, or completeness meaning, recover each separately under its direct governor.

