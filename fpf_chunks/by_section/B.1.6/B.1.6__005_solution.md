---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__005_solution.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:2 — Solution"
line_start: 36086
line_end: 36136
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.27"
  - "C.29"
  - "E.17"
keywords:
---

### B.1.6:2 - Solution

Recover a `WorkResourceAggregation@Context`:

```text
WorkResourceAggregation@Context:
  aggregationConcernRef
  parentWorkOccurrenceRef?
  workOccurrenceRefs
  boundedContextRef
  transformedOrAffectedEntityRef?
  holonDelimitationRefs
  boundaryCrossingRelationRefs?
  timeWindowRef
  phaseRelationRefs?
  resourceBasisRefs
  resourceMeasureRefs
  resourceLedgerRefs
  overlapOrDeduplicationPolicyRef?
  methodRefs?
  methodDescriptionRefs?
  workPlanRefs?
  evidenceOrMeasurementRefs
  aggregationRuleRef
  aggregatedResourceValueRef
  admissibleUse
  nonAdmissibleOverread
  strongerSourceReturnCondition
```

The record is a resource-aggregation relation over work evidence. It is not a method, not a method description, not proof that planned work happened, not a new holon level, and not a whole reidentification claim.

Resource readiness is a neighboring claim, not a measured aggregation result. Planned capacity, reserved inventory, staffing availability, or a full-kit-looking label may be cited as a work-plan, source, or readiness reference, but `A.15.5` governs whether intended work is ready to enter performed-work execution. `B.1.6` governs only the resource-accounting basis, ledger, evidence, aggregation rule, and aggregated value for dated work occurrences or explicitly narrowed planned estimates.

#### B.1.6:2.1 - Direct Owner Map

| Current claim | Direct owner |
| --- | --- |
| Semantic way of doing | `A.3.1` |
| Description of the way of doing, including algorithm text or SOP | `A.3.2` |
| Planned work window or planned assignment | `A.15.2` |
| Work-entry readiness, full-kit condition, or resource readiness before work entry | `A.15.5` |
| Dated performed work occurrence and occurrence evidence | `A.15.1` |
| Work-resource aggregation over dated work occurrences | `B.1.6` |
| Holon delimitation, ports, interfaces, or part-whole boundary used for accounting | `A.1`, `B.1`, `A.14`, `C.13`, or the direct relation owner named by value |
| Boundary-crossing change under conditions | `A.3.4` |
| Phase relation or temporal coverage | `B.1.4` and `A.14`; use `C.27` when temporal claim adequacy is current |
| Measurement construction, units, scales, thresholds, or comparability | `C.16`, `C.16.P`, or `C.29` |
| Evidence provenance, source currentness, or source-use relation | Use `A.10` for evidence-use relations. Use `E.17` for publication and publication-use relations. Use the direct publication or source owner when a more specific source-use claim is being made. |
| Apparent free efficiency, synergy, or whole reidentification | `B.2.P`, then B.2-family owner only if recovered |

