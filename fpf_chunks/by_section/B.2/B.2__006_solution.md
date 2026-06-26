---
chunk_kind: "child"
pattern_id: "B.2"
pattern_title: "Meta-Holon Transition - Whole Reidentification"
section_id: "B.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2/B.2__006_solution.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "B.2 — Meta-Holon Transition - Whole Reidentification"
  - "B.2:4 — Solution"
line_start: 32348
line_end: 32452
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "B.1"
  - "B.2"
  - "B.2.2"
  - "B.2.3"
  - "B.2.4"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30.ILC"
  - "C.32.P2S"
  - "E.24.UK"
  - "U.Episteme"
keywords:
---

### B.2:4 - Solution

Use B.2 as a whole-reidentification pattern with three artifacts: a trigger profile, an existing-whole explanation check, and a holon reidentification record.

#### B.2:4.1 - MHTTriggerProfile

`MHTTriggerProfile@Context` is a trigger and evidence profile for possible whole reidentification. It is not a U-kind and not MHT itself.

```text
MHTTriggerProfile@Context:
  existingWholeRef: U.Holon
  boundedContextRef:
  holonDelimitationChangeRef?
  objectiveOrEvaluationChangeRef?
  supervisionOrCoordinationChangeRef?
  capabilityOrClosureEvidenceRef?
  agencyThresholdRef?
  temporalConsolidationRef?
  contextReframeRef?
  evidenceRelationRefs:
  sourceUseRelationRefs?
  candidateResultHolonKindRef?
```

The profile asks whether enough has changed to make the old whole no longer the right EntityOfConcern. A single trigger is evidence for attention, not automatic admission.

#### B.2:4.2 - ExistingWholeExplanationCheck

Before declaring MHT, run:

```text
ExistingWholeExplanationCheck@Context:
  observedGainOrShiftRef:
  existingWholeRef:
  explanationByBetterParts?
  explanationByCorrectedPartRelation?
  explanationByImprovedMeasurement?
  explanationByRaisedCongruenceOrSourceQuality?
  explanationByMethodOrWorkRepair?
  explanationByTemporalCoverageRepair?
  explanationByArchitectureViewRepair?
  explanationByCapabilityOrFunctioningRepair?
  remainingWholeReidentificationQuestion:
```

If an existing-whole explanation is sufficient, do not declare MHT. Use the direct owner for the repair.

#### B.2:4.3 - HolonReidentificationRecord

Declare MHT only with a record that names the old whole, result whole, result kind, triggers, identity claim, and owner boundaries.

```text
HolonReidentificationRecord@Context:
  existingWholeRef: U.Holon
  boundedContextRef:
  selectedTriggerProfileRef: MHTTriggerProfile@Context
  existingWholeExplanationCheckRef: ExistingWholeExplanationCheck@Context
  mhtResultHolonRef:
  mhtResultSystemRef?
  mhtResultEpistemeRef?
  mhtResultWorkOccurrenceRef?
  mhtResultBoundedContextRef?
  mhtResultDisciplineRef?
  resultHolonKindAdmissionRef:
  identityContinuationOrReidentificationClaim:
  changedContentOwnerRefs:
  evidenceRelationRefs:
  sourceUseRelationRefs?
  mathLensUseRefs?
  blockedOverreads:
```

This record is not a U-kind and not an actor. It carries the reidentification claim and the direct owners of neighboring claims.

#### B.2:4.4 - Result References

Use result references as fields, not as kinds:

- `mhtResultHolonRef` for the reidentified whole;
- `mhtResultSystemRef` only when the result is admitted as `U.System`;
- `mhtResultEpistemeRef` only when the result is admitted as `U.Episteme`;
- `mhtResultWorkOccurrenceRef` only when the result is admitted as `U.Work`;
- `mhtResultBoundedContextRef` only when a bounded context is itself the result whole under its direct owner;
- `mhtResultDisciplineRef` only when the result is a discipline holon under `C.20`.

Do not use `post*` field names as live governed names. They hide the result kind and invite temporal shorthand.

#### B.2:4.5 - Agency Threshold

Agency is not a binary status and not a root kind. Treat agency as a characteristic-space threshold for a system in bounded context.

Use `A.13`, `A.19`, and `C.16` for the characteristic-space and threshold claim. Levin-line TAME work can discipline the multi-characteristic framing when agency evidence is relied on for the current claim. B.2 uses agency threshold only as one possible trigger in `MHTTriggerProfile@Context`, and only when crossing the threshold changes closure, supervision, objective, or whole identity.

#### B.2:4.6 - Acting-System Participation

When a source describes a system changing another holon, recover acting-system participation and transformation separately.

Use `A.12` for acting-side externalization, `A.3.4` for bounded transformation, and `A.15.1` for work occurrence. A system changing another holon does not become that holon's super-holon, and no `U.Transformer` kind is created.

#### B.2:4.7 - Mathematical-Lens Separation

Graph, algebra, RG-like, MSPD, benchmark, scaling, and morphism language can bear on MHT recognition only as mathematical or analytical expression.

Use `C.29` when the mathematical lens is relied on for the current claim. Use B.2 only after the holon identity claim is recovered and the existing-whole explanation check leaves a whole-reidentification question.

