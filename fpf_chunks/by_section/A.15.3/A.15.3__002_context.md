---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__002_context.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:1 — Context"
line_start: 25629
line_end: 25634
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

### A.15.3:1 - Context

A WorkPlan may need more precision than *use this Method* or *perform this task*. An inspection plan may need to remember that `Robot_8_Ref` is intended for `HolderSystemSlot` in the cited `InspectionRobotSystemRoleAssignmentSignature` edition. A recognition plan may need to remember that `Pump_37_Ref` is intended for the declaration-local `candidate` argument.

The declaration already states the participant, argument, or result meaning. The WorkPlan states the intention. A.15.3 joins them only as plan content. It neither changes the declaration nor makes the planned value participate.

