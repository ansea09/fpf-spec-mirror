---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__007_archetypal-grounding.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:5 — Archetypal Grounding"
line_start: 16069
line_end: 16078
dependencies:
  - "A.1"
  - "A.2.1"
  - "A.6.0"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.17.0"
  - "E.8"
  - "F.6"
  - "U.EpistemeSlotRelation"
  - "U.MultiViewDescribing"
  - "U.Signature"
keywords:
  - "argument position"
  - "pass-by-reference"
  - "pass-by-value"
  - "reference"
  - "signature"
  - "slot"
  - "substitution"
  - "value"
---

### A.6.5:5 - Archetypal Grounding

**System case: refrigerator functional architecture.** A refrigerator functional diagram may describe a transformation-flow structure: compressor, condenser, expansion valve, evaporator, sensors, controller, and refrigerant flow. An interface or port in that description is not automatically a generic interface kind. If the current EntityOfConcern is the functional port between evaporator and compressor, recover the functional or transformation-flow relation first, then declare SlotSpecs such as `UpstreamTransformationSlot`, `DownstreamTransformationSlot`, `TransferredMediumSlot`, `BoundaryConditionSlot`, and `ObservedCharacteristicSlot`. The refrigerant, components, controller, and temperature characteristic remain fillers governed by their own patterns.

**Episteme case: model evaluation result.** A `ModelEvaluationResult` episteme can use `EntityOfConcernSlot` with ValueKind `U.Method`, `DatasetSlot` with ValueKind `U.Entity`, `TargetCharacteristicSlot` with ValueKind `U.Characteristic`, `GroundingHolonSlot` with ValueKind `U.Holon`, and `ClaimGraphSlot` with ValueKind `U.ClaimGraph` by value. Retargeting `DatasetSlot` from `Dataset_A` to `Dataset_B` changes a reference filler. Editing the threshold inside `ClaimGraphSlot` changes embedded claim content. Those are different operations.

**Role case: inspection work.** A maintenance context assigns `InspectorRole` to `Robot_7` for a window. The role assignment relation can fill `RoleHolderSlot = Robot_7`, `RoleValueSlot = InspectorRole`, `BoundedContextSlot = MaintenanceLine_A`, and `AssignmentWindowSlot = from 2026-06-15T09:00 to 2026-06-15T11:00`. The robot's capability remains `U.Capability`, the inspection method remains `U.Method` or `U.MethodDescription`, the planned inspection remains `U.WorkPlan`, and the performed inspection remains `U.Work`.

**Evidence case: one report for two claims.** One report episteme can be used as evidence for Claim A and Claim B. The episteme is not assigned two evidence roles. FPF creates two evidence-use relations with different `EvidenceTargetClaimSlot` fillers and any distinct scope, polarity, relevance-window, or weight-model fillers.

