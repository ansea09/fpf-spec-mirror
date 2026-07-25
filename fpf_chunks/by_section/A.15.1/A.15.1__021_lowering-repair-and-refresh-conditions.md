---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:16"
section_title: "Lowering, Repair, and Refresh Conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__021_lowering-repair-and-refresh-conditions.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:16 — Lowering, Repair, and Refresh Conditions"
line_start: 24701
line_end: 24708
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "F.6"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing system"
  - "covering U.RoleAssignment"
  - "enacted method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:16 - Lowering, Repair, and Refresh Conditions

Lower a candidate assertion that an individual is Work admitted under `U.Work` when the occurrence designator, actual performer system, covering assignment and any explicit F.6 attribution, actual enacted method, temporal extent, or `executedWithin` relation cannot be recovered. If the receiving claim additionally relies on a work-to-referent, direct-relation or A.6.1 binding, or resource-use fact, lower that dependent claim when its independently obtaining relation cannot be recovered; do not lower the Work occurrence merely because an unneeded affected referent or delta is absent. Require a continuity-policy basis only when an identity, episode, retry, resumption, or aggregation claim actually depends on ambiguous segmentation. Lower a candidate work-part claim when the downstream use does not need a named work part or when the candidate is only an interval, event-log row, telemetry segment, method-description constituent, component behavior, mechanism material, or wording cue. The acceptable lowered object is the exact temporal relation, plan episteme, readiness-gap claim, evidence episteme, telemetry slice, method-description reference, unresolved-segmentation note, missing-relation blocker, `A.15.4` repair request, or direct neighboring object, not a backdated Work occurrence or gratuitous work part.

Repair the work assertion or description when a subsequent source changes the resolved temporal extent, actual performer system, covering assignment or F.6 attribution, actual enacted method, selected method-description reference, direct binding, resource-use claim, work-to-referent relation, containing system, or work-part relation. Reidentify only when the direct A.15.1 boundary rules or an exact policy current to a named ambiguous use require it. A changed continuity-policy edition repairs the dependent identity, episode, retry, resumption, or aggregation judgment; it does not rewrite the Work occurrence or its actual history. Repair a result or consequence through the one matching §4.6 owner rather than editing Work.

Refresh before cross-context model use, aggregation, comparison, measurement, acceptance, release reliance, gate use, evidence use, assurance use, QD or OEE archive use, or P2W carry-through use. If the claim being made after refresh is no longer about performed work, use the direct pattern for that object or relation and retain a Work-occurrence reference only when the receiving claim actually depends on that occurrence.

