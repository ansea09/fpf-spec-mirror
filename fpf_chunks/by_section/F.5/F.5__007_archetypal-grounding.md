---
chunk_kind: "child"
pattern_id: "F.5"
pattern_title: "Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
section_id: "F.5:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/F.5/F.5__007_archetypal-grounding.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "F.5 — Naming Discipline for U-kind Names and SystemRoleKindDescription Labels"
  - "F.5:5 — Archetypal Grounding"
line_start: 94480
line_end: 94511
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.6.5"
  - "A.6.RSIR"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.3"
  - "C.3.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.24.UK"
  - "F.10"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.6"
keywords:
  - "Plain and Tech designations"
  - "SystemRoleKindDescription label"
  - "U-kind name"
  - "local meaning"
  - "naming after ontology recovery"
  - "system-role-kind name"
---

### F.5:5 - Archetypal Grounding

#### F.5:5.1 - Public or Cross-Local Kind Name

A Concept-Set row compares SOSA `Observation`, metrology *measurement result*, ML practice *metric reading*, and a dashboard value exported for comparison. The row is a comparison and evidence surface, not admission or identity of a common result value.

Keep the concrete objects at their direct loci. Pump 14 was measured before the reading was recorded, but this naming example does not identify a dated Work occurrence. If a use needs that occurrence, recover its exact actual performer through A.13 and admit it independently under A.15.1. Attribute it under F.6 only when that use also consumes precise assignment-bound attribution.

C.16 constitutes the measurement result: a value attributed to the measurand together with the Characteristic, Scale, uncertainty, method, model, calibration basis, time stance, and measurement Work needed to interpret it. `Pump14PressureReading_2026-07-14T10-42Z` is one C.2.1 episteme that states that result; F.5 does not repeat either pattern's schema. The result and its episteme are distinct from raw output, indication, Pump 14's actual state, a later diagnosis, a criterion verdict, evidence, or a dashboard display. `Pump14CalibrationTrace_2026-07-14` is a provenance record whose G.6 and A.10 relations make the calibration and source path recoverable. A dashboard publication may cite the reading, and the Concept-Set row may cite the reading and trace; neither is the result, its episteme, provenance, or a generic relation that establishes them.

Only E.24.UK or the direct result pattern can admit a shared value and its invariants. After admission, use F.5 to select `Reading`, `Result`, or another neutral head no wider than that value. The spelling still creates no result or provenance identity.

#### F.5:5.2 - Local System-Role Kind and Its Description

Under `Plant-A-Maintenance-Scheme`, `PumpInspectorSystemRole` designates one exact local kind; it is not that kind. `PumpInspectorSystemRoleKindDescription-v3` is a separate C.2.1 episteme whose EntityOfConcern is the kind. Its ClaimGraph states which systems are candidates, the reading-and-judgment condition that distinguishes members, useful member and non-member probes, the continuity rule, current `KindSignature`, and effective scheme. Plant-A maintenance provenance locates that definition; it does not identify the kind. The Tech designation is `PumpInspectorSystemRole`; the Plain designation is “pump inspector”.

This worked slice needs an assignment identity, so `Robot7-PumpInspector-Assignment-2026Q3` is one occurrence of the directly declared `PlantAPumpInspectionAssignment` species under `U.SystemRoleAssignment`. The species' holder slot admits a `U.System`; its declaration-local assigned-kind slot uses the exact `PlantAMaintenanceSystemRoleKindDomain`; and its predicate applies within the Plant A maintenance scheme and obtains while the fixed holder is assigned under `PumpInspectorSystemRole` to supply the pump-inspection contribution. The occurrence identifies Robot-7 as holder and `PumpInspectorSystemRole` as assigned kind, and spans the maximal uninterrupted interval over which that predicate obtains for those values. This simple species declares no additional identity-bearing participant; a commission, position, or installation locus would become one only in a species whose predicate and identity actually require it.

This naming example does not identify Robot-7's inspection of Pump 14 as a dated Work occurrence. `Pump14InspectionFinding_2026-07-14T11-18Z` is a separate claim-bearing result episteme, and `Pump14InspectionTrace_2026-07-14` is the exact provenance record connected through G.6 and A.10.

The kind label helps readers recover the kind; the description episteme describes it. Neither says Robot-7 satisfies the kind, has an assignment, performed the inspection, produced the finding, or supplied its provenance. A suffix, NameCard, row, pattern section, or citation identifies none of those objects or relations.

#### F.5:5.3 - Evidence Use Is Not a System-Role Name

Source text may say `ModelFitEvidenceRole`. The repair is not a prettier role label. This naming example does not identify the model-fit evaluation as a dated Work occurrence. Recover the exact objects it does consume: `ModelFitResult_2026-07-15T09-22Z` is a separately constituted domain-local result episteme; `ModelFitTargetClaim-v5` is the target claim; and `ModelFitRunTrace_2026-07-15` is the provenance record connected through exact G.6 and A.10 relations. Keep any operation-result binding, result-episteme inception claim, evidence use, provenance, and current assurance claim separate, and apply the rule that defines or tests each relation.

A durable name, if needed, names one recovered evidence-use relation, status value, Work occurrence, result episteme, or provenance value. `ModelFitEvidenceRole`, a NameCard, row, or citation creates none of them and supplies no generic evidence-result relation. It is neither a local system-role kind nor a `SystemRoleKindDescription` label.

#### F.5:5.4 - Relation Position Is Not a System-Role Name

In a relation signature, “provider role” may mean the provider argument position. Use E.10.ROLE and A.6.RSIR to recover the participant meaning; use A.6.5 to declare `ProviderSlot`, its `ValueKind`, and its reference mode. A provider system's classification under a local `ProviderSystemRole` kind is a separate C.3 claim. When assignment identity is irrelevant to naming that relation position, say only that any provider assignment remains independently governed by A.2.1; do not invent an occurrence. When it is relevant, recover the assignment occurrence and its declared species rather than asserting that the provider simply “has an assignment”.

