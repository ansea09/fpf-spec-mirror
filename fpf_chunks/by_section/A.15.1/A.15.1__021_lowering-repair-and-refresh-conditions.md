---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:16"
section_title: "Lowering, Repair, and Refresh Conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__021_lowering-repair-and-refresh-conditions.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:16 — Lowering, Repair, and Refresh Conditions"
line_start: 24731
line_end: 24738
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
  - "U.Work admitted kind"
  - "actual binding"
  - "affected referent"
  - "enactsMethod"
  - "episode"
  - "no automatic transformation"
  - "occurrence assertion and record separation"
  - "overlap"
  - "performed resource-use fact"
  - "performedBy"
  - "retry"
  - "work continuity"
  - "work part"
  - "world-side dated occurrence"
---

### A.15.1:16 - Lowering, Repair, and Refresh Conditions

Lower a candidate assertion that an individual is Work admitted under `U.Work` when occurrence designator, performer-assignment, actual enacted-method, temporal, `executedWithin`, affected-referent, current direct-relation or A.6.1 binding, resource-use relation, or continuity-policy basis needed by the receiving use cannot be recovered. Lower a candidate work-part claim when the downstream use does not need a named work part or when the candidate is only an interval, event-log row, telemetry segment, method-description constituent, component behavior, mechanism material, or wording cue. The acceptable lowered object is the exact temporal relation, plan episteme, readiness-gap claim, evidence episteme, telemetry slice, method-description reference, missing-relation blocker, `A.15.4` repair request, or direct neighboring object, not a backdated Work occurrence or gratuitous work part.

Repair the work assertion or description when a subsequent source changes the resolved temporal extent, performer assignment, actual enacted method, selected method-description reference, direct binding, resource-use claim, affected referent, containing system, work-continuity policy, or work-part relation. Repair a neighboring `B.1.4` or `B.1.6` result when its overlap or aggregation policy changes; that policy change alone does not rewrite Work. Reidentification follows the occurrence facts and exact continuity policy; a changed description, record, evidence set, publication, or aggregation result alone does not rewrite Work. Repair a neighboring change, evaluation, evidence, production, delivery, or acceptance claim under its own pattern.

Refresh before cross-context model use, aggregation, comparison, measurement, acceptance, release reliance, gate use, evidence use, assurance use, QD or OEE archive use, or P2W carry-through use. If the claim being made after refresh is no longer about performed work, use the direct pattern for that object or relation and retain a Work-occurrence reference only when the receiving claim actually depends on that occurrence.

