---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__005_solution.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:4 — Solution"
line_start: 62212
line_end: 62377
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.17.0"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller and plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:4 - Solution

Treat LCA-like source descriptions as possible inputs to a control-structure description under C.30. Recover one exact described holon, any actual architecture relation, one selected control structure, the exact controlled holon, actual control-role assignments, independently obtaining observation, actuation, reference, supervision, and feedback relations, and any rate or control-layer relation that changes the next architecture move. A.22 identifies the selected structure from exact constituents, selected obtaining relation occurrences, applied constraint claims, and the receiving-use frame; a note, diagram, list, or description creates none of them. If a source label is not yet control-specific, apply `C.30.STRAT` first. Then state admissible use and the next governing-pattern application.

The ordinary minimum may stop with a compact `ControlStructureViewNote`:

```text
ControlStructureViewNote:
  architectureRelationOccurrenceRef?: ArchitectureRelationRef
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim
  describedHolonRef?: U.HolonRef
  selectedControlStructureRef?:
  controlledHolonRef:
  selectedControlRelationRef:
  feedbackClosureState: closed | oneWay | unclear
  controlLayerRelationRef?:
  rateBandRef?:
  observationBoundaryRef?:
  actuationBoundaryRef?:
  feedbackBoundaryRef?:
  externalityBoundaryRef?:
  stratificationRepairRef?:
  nextGoverningPatternApplicationRef?:
  admissibleUse:
  nonAdmissibleUse:
  stopCondition:
```

Use `rateBandRef?`, `controlLayerRelationRef?`, and `externalityBoundaryRef?` only when that object or relation changes the control-structure use. Otherwise the note may stop after one actual control relation, feedback-closure state, and next governing-pattern application. Generic stratification labels stay with `C.30.STRAT` until a control-specific relation is recovered.

When a recovered control-layer relation is used to justify decomposition, substitution, or design reliance, recover the inter-layer assumption-guarantee relation or mark the control-layer relation as orientation only. `interLayerControlRelationRefs?` is used only when the relation is already control-specific and is used for decomposition, substitution, design reliance, safety, or stability claims.

```text
InterLayerControlRelationNote:
  upperLayerAssumptionRefs:
  lowerLayerGuaranteeRefs:
  observationConditionRefs:
  actuationAuthorityRefs:
  latencyBoundRefs?:
  rateEnvelopeRefs?:
  violationFallbackRefs:
  admissibleUse:
  nonAdmissibleUse:
```

Use this note only when a recovered control-layer relation is used for decomposition, substitution, safety or stability claim, or architecture decision claim. It is not proof and does not make the relation obtain. Otherwise keep C.30.LCA at the small note or ordinary description form, or return the source label to `C.30.STRAT`.

```text
ControlStructureView ::= ArchitectureDescription & U.View & {
  viewEpistemeRef: U.EpistemeRef,
  claimGraph: exactly one C.2.1 ClaimGraph,
  entityOfConcernRef: selectedControlStructureRef,
  effectiveReferenceScheme: U.ReferenceScheme, byValue,
  selectedControlStructureRef: U.StructureRef,
  structureKindRef = ControlStructure,

  viewpointRef: U.ViewpointRef,
  viewpointConformanceRelationRef: EpistemeViewpointConformanceRelationRef,
  concernRefs?: FinSet(U.EntityRef),

  describedHolonRef?: U.HolonRef,
  architectureRelationOccurrenceRefs?: FinSet(ArchitectureRelationRef),
  architectureClaimRefs?: FinSet(U.EpistemeRef constrained to ArchitectureClaim),
  claimScope?: U.ClaimScope, byValue,
  modelUseStructureRef?: U.StructureRef,
  empiricalGroundingRelationRefs?: FinSet(EpistemeEmpiricalGroundingRelationRef),
  controlledHolonRef: U.HolonRef,

  plannerRoleAssignmentRefs?: FinSet(U.RoleAssignmentRef),
  controllerRoleAssignmentRefs?: FinSet(U.RoleAssignmentRef),
  observerRoleAssignmentRefs?: FinSet(U.RoleAssignmentRef),
  supervisorRoleAssignmentRefs?: FinSet(U.RoleAssignmentRef),
  controlMethodRefs?: FinSet(U.MethodRef),

  selectedControlRelationRefs: FinSet(U.RelationRef),
  observationRelationRefs?: FinSet(U.RelationRef),
  actuationRelationRefs?: FinSet(U.RelationRef),
  referenceProvisionRelationRefs?: FinSet(U.RelationRef),
  feedbackRelationRefs?: FinSet(U.RelationRef),
  controlLayerRelationRefs?: FinSet(U.RelationRef),
  rateBandRefs?: FinSet(RateBandRef),
  interLayerControlRelationRefs?: FinSet(U.RelationRef),
  supervisorSubholonRelationRefs?: FinSet(U.RelationRef),

  observationBoundaryRefs?: FinSet(BoundaryRef),
  actuationBoundaryRefs?: FinSet(BoundaryRef),
  feedbackBoundaryRefs?: FinSet(BoundaryRef),
  externalityBoundaryRefs?: FinSet(BoundaryRef),
  transformationFlowPathSliceRefs?: FinSet(PathSliceId),

  stratificationRepairRefs?: FinSet(C30STRATRepairRef),
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  downstreamGoverningPatternApplicationRefs?,
  representationRefs?: FinSet(U.EntityRef),
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef),
  publicationFormRefs?: FinSet(U.EntityRef),
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier),
  admissibleUse,
  nonAdmissibleUse,
  sourceReturnCondition?
}
```

The full view is the same C.2.1 episteme identified by its exact claim graph, selected-control-structure EntityOfConcern, and effective scheme. Its direct E.17.0 conformance occurrence has exactly that candidate episteme and one exact viewpoint episteme as participants; the fixed five-part predicate and participant-determined identity govern it. Authoring, A.6.3 construction, a `viewpointRef`, query, selection, bundle membership, diagramming, rendering, publication, or current use does not make it obtain.

`controlledHolonRef` names the holon whose state is observed or changed by independently obtaining control relations and may be the described holon or one of its exact parts. Architecture claims, `ClaimScope`, model-use structure, concern, and empirical grounding remain optional neighboring objects or relations. `modelUseStructureRef` appears only when an independently selected DDD-style bounded-model-use structure changes interpretation or selection.

Every positive control-role assignment and control-relation reference identifies an actual occurrence admitted by its direct pattern. The description, control note, view record, or diagram neither creates those occurrences nor acts. Representation, publication occurrence, form, and carrier likewise remain separate from the selected structure and view episteme.

#### C.30.LCA:4.0a - Safety-loss control-structure note

Use a `SafetyLossControlStructureNote` only when safety wording is being used for a loss-control claim and the practitioner first needs the architecture-side loss-control structure, not a safety-case verdict:

```text
SafetyLossControlStructureNote:
  lossOrHarm:
  hazardOrUnsafeState:
  unsafeControlActionOrMissingControl:
  controlledProcessOrPlantRef:
  controlConstraintRef:
  feedbackOrObservabilityBoundary:
  timingOrRateBoundary:
  operationalDesignScopeOrMisuseScope:
  foreseeableMisuseRefs?:
  architectureStructureKindRefs:
    ControlStructure | ConstraintRequirementStructure |
    SecurityTrustBoundaryStructure | InformationDataStructure |
    EvidenceAssuranceStructure
  governingPatternApplicationRefs:
    A.3.3 dynamics, C.27.TA temporal aspect or rate, and C.27 authored temporal-claim adequacy,
    C.28 causal-use, A.10 or G.6 evidence,
    B.3 assurance, A.20 or A.21 gate
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive safety-triggered architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace the generic control-structure view and does not replace evidence, assurance, gate, causal, dynamics, or temporal claims.

**Role interpretation.**

| Source label | FPF recovery |
|---|---|
| Plant or controlled holon | `U.Holon` whose state evolves; reusable state-evolution claims use `A.3.3`. |
| Regulator or controller | System in a control role enacting a method over observations and actuations. |
| Planner | Acting system in a planner role; the enacted method may structure setpoint, plan, reference, or allowed-region production. |
| Observer or estimator | Acting system in an observer or estimator role; the enacted method may structure state estimates, observations, or evidence-facing readouts. |
| Supervisor | Acting system in a supervisor role; the enacted method or policy may structure work that constrains subordinate holons, gates, policy changes, or control-mode changes. |

**Control-specific stratification gate.** `Layer`, `level`, `tier`, and `stack` enter C.30.LCA only after `C.30.STRAT` or the local sentence recovers a control-role assignment, direct control relation, inter-layer control relation, rate band, or `B.2.5` supervisor-subholon relation. A label by itself does not establish control structure or separation.

**B.2.5 boundary.** `B.2.5` governs the supervisor-subholon feedback relation. `C.30.LCA` may cite such a relation as part of the selected control structure, but stability, safety, causality, evidence, gate, and assurance claims still use their direct governing patterns. If an episteme appears in a control example, name the acting system, its role assignment, enacted method when current, and any publication, source-to-use, or work-reliance relation. An episteme does not sense, decide, plan, adapt, or act as an agent.

**Transformation-flow boundary.** An `E.18` transformation-flow path slice may supply flow-structure, path, crossing, or transformation-flow-structure input to the control view when that relation is being used. The transformation-flow graph expression remains a mathematical description or view of transformation-flow structure. It does not become the functional architecture, the control structure, or proof of control adequacy.

**C.29 boundary.** An LCA can be a model used for one selected control structure, or it can be used as a transferable mathematical lens. Open `C.29` only when transfer, prediction, reusable cross-domain explanation, or mathematical-lens use is being claimed. Dynamics, rate bands, authored temporal-claim adequacy, and causal claims remain with `A.3.3`, `C.27.TA`, `C.27`, and `C.28`.

**Nesting and scale rule.** If a control-structure view nests without a local depth limit, the record uses `scaleAuditRef?` when the nesting affects latency, stability, observability, accountability, or assurance.

**Worked slice A - LCA diagram used as proof.** A safety note says: `The Layered Control Architecture proves the plant is safe because the supervisor monitors the lower controller.` A conforming repair keeps the control-structure view and names planner, controller, plant, and supervisor relations, observation and actuation boundaries, and any rate bands. Safety and assurance claims use `B.3`, evidence to `A.10` or `G.6`, temporal-aspect and rate-band claims to `C.27.TA`, authored temporal-claim adequacy to `C.27`, and dynamics or stability claims use `A.3.3` or the appropriate dynamics claim.

**Worked slice B - multi-rate controller.** A source says a control stack has a slow planner, a faster regulator, and an observer with a different update period. Apply `C.30.LCA` to the case only after the stack label has been recovered as control roles, relations, and rate bands; otherwise the label is recovered first by `C.30.STRAT`. C.30.LCA does not claim rate adequacy. If the rate relation matters for oscillation, latency, stability, or safety, the next admissible use is `C.27.TA` for temporal aspect or rate-band structure, plus `C.27` only when an authored temporal-claim adequacy question is under repair, and the dynamics or assurance pattern named by value when that claim kind is being made.

**Worked slice C - supervisor-subholon loop.** A subsystem is supervised by an external controller that changes allowed modes. `C.30.LCA` records the supervisor-subholon relation and may reference `B.2.5`. If the text claims that this loop authorizes work, passes a gate, or proves a policy constraint, the claim uses `A.15`, `A.20`, or `A.21`.

**Currentness and smallest reopen.** When a decisive input changes, reopen only the control-structure locus and use conclusion that depend on it. A changed selected control structure or controlled holon reopens the affected `ControlStructureViewNote` or full description/view; a changed role assignment or direct relation reopens that exact assignment or occurrence and its dependent structure selection; changed feedback, rate, or control-layer relations reopen only their matching relation or boundary fields; changed view conformance reopens only the E.17.0 admission; and a changed source edition reopens its source-to-use and source-return locus. A changed safety or proof claim, or a changed direct governor, reopens only that neighboring claim or governor-owned relation unless a control-structure input also changed. Update the affected locus, demote full view use to a note or orientation, narrow use, or reopen the control-structure question; unrelated structures and claims stay closed.

