---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__005_solution.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:4 — Solution"
line_start: 61422
line_end: 61598
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

Treat LCA-like source descriptions as possible inputs to a control-structure description under C.30. Recover one described holon, any actual architecture relation, one selected control structure, the controlled holon, independently obtaining observation, actuation, reference, supervision, and feedback relations, and the participant meaning in each relation.

Add participating Systems, local kinds, separate System-classification judgments, assignment species and obtaining occurrences, Methods, and actual Work only when each independently obtains. Use A.22 to identify the selected structure from its constituents, selected obtaining relation occurrences, applied constraint claims, and receiving-use frame; a note, diagram, list, description, kind, or assignment creates none of them. If a source label is not yet control-specific, apply `C.30.STRAT` first. Then state admissible use and the next pattern to use.

When the result must retain boundary, admissible-use, or handoff detail, expand the same `ControlStructureViewNote`:

```text
ControlStructureViewNote:
  architectureRelationOccurrenceRef?: ArchitectureRelationRef
  architectureClaimRef?: U.EpistemeRef constrained to ArchitectureClaim
  describedHolonRef?: U.HolonRef
  selectedControlStructureRef?:
  structureGap?:
  controlledHolonRef:
  selectedControlRelationRef:
  controlRelationParticipantRefs:
  feedbackClosureState: closed | oneWay | unclear
  controlLayerRelationRef?:
  rateBandRef?:
  observationBoundaryRef?:
  actuationBoundaryRef?:
  feedbackBoundaryRef?:
  externalityBoundaryRef?:
  stratificationRepairRef?:
  nextPatternUseRef?:
  admissibleUse:
  nonAdmissibleUse:
  stopCondition:
```

Use `rateBandRef?`, `controlLayerRelationRef?`, and `externalityBoundaryRef?` only when that object or relation changes the control-structure use. Otherwise the note may stop after one actual control relation, feedback-closure state, and the next pattern to use. Generic stratification labels stay with `C.30.STRAT` until a control-specific relation is recovered.

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

Use this note only when a recovered control-layer relation is used for decomposition, substitution, a safety or stability claim, or an architecture decision. It is not proof and does not make the relation obtain. Otherwise keep C.30.LCA at the small note or ordinary description form, or use `C.30.STRAT` to recover the source label.

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

  selectedControlRelationRefs: FinSet(U.RelationRef),
  controlRelationParticipantRefs: FinSet(U.EntityRef),
  observationRelationRefs?: FinSet(U.RelationRef),
  actuationRelationRefs?: FinSet(U.RelationRef),
  referenceProvisionRelationRefs?: FinSet(U.RelationRef),
  feedbackRelationRefs?: FinSet(U.RelationRef),
  controlLayerRelationRefs?: FinSet(U.RelationRef),
  rateBandRefs?: FinSet(RateBandRef),
  interLayerControlRelationRefs?: FinSet(U.RelationRef),
  supervisorSubholonRelationRefs?: FinSet(U.RelationRef),

  participatingSystemRefs?: FinSet(U.EntityRef constrained to U.System),
  localSystemRoleKindRefs?: FinSet(U.KindRef),
  systemRoleClassificationJudgmentRefs?: FinSet(U.RelationRef),
  assignmentRows?: FinSet({
    assignmentSpeciesRef: U.RelationKindRef constrained under U.SystemRoleAssignment,
    assignmentOccurrenceRef: U.RelationRef constrained to an obtaining occurrence of assignmentSpeciesRef
  }),
  actualControlWorkRefs?: FinSet(U.EntityRef constrained to U.Work),
  actualControlWorkAttributionRefs?: FinSet(U.RelationRef constrained to obtaining performedUnderAssignment relations),

  observationBoundaryRefs?: FinSet(BoundaryRef),
  actuationBoundaryRefs?: FinSet(BoundaryRef),
  feedbackBoundaryRefs?: FinSet(BoundaryRef),
  externalityBoundaryRefs?: FinSet(BoundaryRef),
  transformationFlowPathSliceRefs?: FinSet(PathSliceId),

  stratificationRepairRefs?: FinSet(C30STRATRepairRef),
  sourceToUsePathRefs?: FinSet(U.RelationRef),
  downstreamPatternUseRefs?,
  representationRefs?: FinSet(U.EntityRef),
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef),
  publicationFormRefs?: FinSet(U.EntityRef),
  carrierRefs?: FinSet(U.EntityRef constrained to U.PresentationCarrier),
  admissibleUse,
  nonAdmissibleUse,
  sourceReturnCondition?
}
```

The full view is the same C.2.1 episteme identified by its exact claim graph, selected-control-structure EntityOfConcern, and effective scheme. Its direct E.17.0 conformance occurrence has exactly that candidate episteme and one exact viewpoint episteme as participants. It obtains only when the fixed five-part predicate is true, and those participants determine its identity. Authoring, A.6.3 construction, a `viewpointRef`, query, selection, bundle membership, diagramming, rendering, publication, or current use does not make it obtain.

`controlledHolonRef` names the holon whose state is observed or changed by independently obtaining control relations and may be the described holon or one of its exact parts. Architecture claims, `ClaimScope`, model-use structure, concern, and empirical grounding remain optional neighboring objects or relations. `modelUseStructureRef` appears only when an independently selected DDD-style bounded-model-use structure changes interpretation or selection.

For every positive control-relation reference, identify the actual occurrence and use the relevant pattern to recover what its participants mean. Any participating System, local classification, assignment, Method, Work, or F.6 attribution also identifies its own independently admitted fact. A classification or assignment establishes neither control nor action.

The description, control note, view record, and diagram create none of these occurrences and do not act. Representation, publication occurrence, form, and carrier likewise remain separate from the selected structure and view episteme.

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
  claimPatternUseRefs:
    A.3.3 dynamics, C.27.TA temporal aspect or rate, and C.27 authored temporal-claim adequacy,
    C.28 causal-use, A.10 or G.6 evidence,
    B.3 assurance, A.20 or A.21 gate
  nonAdmissibleUse:
    not safety proof, not safety-case verdict, not regulatory acceptance
```

The note gives a positive safety-triggered architecture move: find the loss-control structure, controlled process or plant, constraint, foreseeable misuse, operational design scope, and action-relevant boundary. It does not replace the generic control-structure view and does not replace evidence, assurance, gate, causal, dynamics, or temporal claims.

**Control-participant interpretation.**

| Source label | FPF recovery |
|---|---|
| Plant or controlled holon | `U.Holon` whose state evolves; reusable state-evolution claims use `A.3.3`. |
| Regulator or controller | Recover the regulation or control relation and its participant meaning. If control Work is claimed, recover the exact performer System through A.13 and admit the Work independently through A.15.1 with its enacted Method. Add an assignment occurrence and F.6 only when the control account expressly consumes precise assignment-bound attribution. Add local classification only when relied on; assignment supplies none. |
| Planner | Recover the exact reference-provision, planning, or other direct relation. A planning System and planning Work are separate; for a plan, authority, or allowed-region result, use its own pattern. |
| Observer or estimator | Recover the observation or estimation relation and participant meaning. If observation or estimation Work occurred, recover the exact performer System through A.13 and admit the dated Work and enacted Method independently through A.15.1. Add assignment and F.6 only when precise assignment-bound attribution is expressly consumed; a reading or evidence result remains separate. |
| Supervisor | Recover the exact supervision or `B.2.5` supervisor-subholon relation. Use separate patterns for any constraining Work, policy change, authority, responsibility, gate, or control-mode change. |

**Control-specific stratification gate.** `Layer`, `level`, `tier`, and `stack` enter C.30.LCA only after `C.30.STRAT` or the local sentence recovers a direct control relation, inter-layer control relation, rate band, or `B.2.5` supervisor-subholon relation. An assignment alone is insufficient, and the label by itself establishes neither control structure nor separation.

**B.2.5 boundary.** Use `B.2.5` for the supervisor-subholon feedback relation. A `C.30.LCA` use may cite that relation as part of the selected control structure, but use the relevant patterns for stability, safety, causality, evidence, gate, and assurance claims. If action involving an episteme is claimed, recover the exact performing System through A.13 and admit the dated Work and enacted Method independently through A.15.1. Add an assignment occurrence and F.6 only when the account expressly consumes precise assignment-bound attribution; keep publication, source-to-use, and work-reliance relations separate. An episteme does not sense, decide, plan, adapt, or act.

**Transformation-flow boundary.** An `E.18` transformation-flow path slice may supply flow-structure, path, crossing, or transformation-flow-structure input to the control view when that relation is being used. The transformation-flow graph expression remains a mathematical description or view of transformation-flow structure. It does not become the functional architecture, the control structure, or proof of control adequacy.

**C.29 boundary.** An LCA can be a model used for one selected control structure, or it can be used as a transferable mathematical lens. Open `C.29` only when transfer, prediction, reusable cross-domain explanation, or mathematical-lens use is being claimed. Dynamics, rate bands, authored temporal-claim adequacy, and causal claims remain with `A.3.3`, `C.27.TA`, `C.27`, and `C.28`.

**Nesting and scale rule.** If a control-structure view nests without a local depth limit, the record uses `scaleAuditRef?` when the nesting affects latency, stability, observability, accountability, or assurance.

**Worked slice A - LCA diagram used as proof.** A safety note says: `The Layered Control Architecture proves the plant is safe because the supervisor monitors the lower controller.` A conforming repair keeps the control-structure view and names planner, controller, plant, and supervisor relations, observation and actuation boundaries, and any rate bands. Use `B.3` for safety and assurance, `A.10` or `G.6` for evidence, `C.27.TA` for temporal aspects and rate bands, `C.27` for authored temporal-claim adequacy, and `A.3.3` or the applicable dynamics pattern for dynamics or stability.

**Worked slice B - multi-rate controller.** A source says a control stack has a slow planner, a faster regulator, and an observer with a different update period. Apply `C.30.LCA` only after the stack label has been recovered as exact reference-provision, regulation, observation, or other control relations with their participant meanings and rate bands; otherwise use `C.30.STRAT` first. Systems, classifications, assignments, Methods, and Work are added only where independently current. A C.30.LCA description establishes no rate adequacy. If the rate relation matters for oscillation, latency, stability, or safety, next use `C.27.TA` for temporal aspect or rate-band structure, `C.27` when an authored temporal-claim adequacy question is under repair, and the dynamics or assurance pattern named by value when that claim kind is being made.

**Worked slice C - supervisor-subholon loop.** A subsystem is supervised by an external controller System. The C.30.LCA note records the supervisor-subholon relation and may reference `B.2.5`. If that System performs mode-change Work, recover it through A.13 and admit the Work and enacted Method independently through A.15.1. Add an assignment occurrence and F.6 only when this slice also expressly represents precise assignment-bound attribution; missing or failed F.6 leaves the mode-change Work intact. Authority, responsibility, gate passage, safety, stability, and policy-constraint results remain separate claims under their own patterns; the supervisor relation establishes none of them.

**Currentness and smallest reopen.** When a decisive input changes, reopen only the control-structure locus and the use conclusions that depend on it. A changed selected control structure or controlled holon reopens the affected `ControlStructureViewNote` or full description and view; a changed direct control relation or participant meaning reopens that occurrence and its dependent structure selection; a changed classification, assignment, Method, Work, or F.6 attribution reopens only that neighboring fact and any view use that relied on it. Changed feedback, rate, or control-layer relations reopen only their matching relation or boundary fields; changed view conformance reopens only the E.17.0 admission; and a changed source edition reopens its source-to-use and source-return locus. A changed authority, responsibility, safety, proof, evidence, assurance, or gate claim reopens only that neighboring claim unless a control-structure input also changed. Update the affected locus, demote full view use to a note or orientation, narrow use, or reopen the control-structure question; unrelated structures and claims stay closed.

