---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:16"
section_title: "Lowering, Repair, and Refresh Conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__021_lowering-repair-and-refresh-conditions.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:16 — Lowering, Repair, and Refresh Conditions"
line_start: 24283
line_end: 24290
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
  - "U.System"
  - "U.SystemRoleAssignment"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing System"
  - "covering U.SystemRoleAssignment"
  - "enacted Method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:16 - Lowering, Repair, and Refresh Conditions

Lower a candidate assertion that an individual is Work admitted under `U.Work` when the occurrence designator, any actual performer System, the F.6 attribution for that performer, temporal extent, at least one obtaining `enactsMethod` relation, or at least one required locally declared containing-system relation cannot be recovered. Lower an additional enactment claim separately when its exact relation cannot be recovered. If the receiving claim additionally relies on a Work-to-referent or resource-use relation, lower that dependent claim when its declared predicate, participants, or obtaining facts cannot be recovered. If it relies on an operation argument or result, lower that dependent claim when the identified A.6.1 application or exact binding is absent. Do not lower the Work occurrence merely because an unneeded affected referent, further containing boundary, or delta is absent. Require a continuity-policy basis only when an identity, episode, retry, resumption, or aggregation claim actually depends on ambiguous segmentation. Lower a candidate work-part claim when the downstream use does not need a named work part or when the candidate is only an interval, event-log row, telemetry segment, method-description constituent, component behavior, mechanism material, or wording cue. The acceptable lowered object is the exact temporal relation, plan episteme, readiness-gap claim, evidence episteme, telemetry slice, method-description reference, unresolved-segmentation note, missing-relation blocker, `A.15.4` repair request, or direct neighboring object, not a backdated Work occurrence or gratuitous work part.

Repair the Work assertion or description when a subsequent source changes the resolved temporal extent, actual performer system, covering assignment or F.6 attribution, enacted Method, selected method-description reference, direct binding, resource-use claim, work-to-referent relation, obtaining containing-system relation, or work-part relation. Reidentify only when the direct A.15.1 boundary rules decide the change or the selected policy's branch criterion applies to a named ambiguous use. When the selected continuity-policy episteme changes, repair the dependent identity, episode, retry, resumption, or aggregation judgment and cite the newly selected exact episteme. Call it a changed edition only when the exact C.2.1 `EpistemeEditionRelation` obtains; otherwise record a non-continuing replacement. Neither route rewrites the Work occurrence or its actual history. Repair a result or consequence through the matching §4.6 row rather than editing Work.

Refresh before cross-context model use, aggregation, comparison, measurement, acceptance, release reliance, gate use, evidence use, assurance use, QD or OEE archive use, or P2W carry-through use. If the claim being made after refresh is no longer about performed work, use the direct pattern for that object or relation and retain a Work-occurrence reference only when the receiving claim actually depends on that occurrence.

