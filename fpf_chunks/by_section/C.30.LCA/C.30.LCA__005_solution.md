---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__005_solution.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:4 — Solution"
line_start: 57885
line_end: 58031
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
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
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

Treat LCA-like material as a control-structure view under `C.30`. Recover the described architecture claim, the selected control structure or control-structure relation set, the control roles, the control relations, the relevant rate bands or recovered control-layer labels, and the boundary refs that make the view checkable. If the source label is not yet control-specific, apply `C.30.STRAT` before applying C.30.LCA to the case. Then state the admissible use and the non-admissible overread.

The ordinary minimum may stop with a compact `ControlStructureViewNote`:

```text
ControlStructureViewNote:
  architecture claim or described holon plus context:
  selected control structure or relation:
  one control relation:
  loop state: closed | one-way | unclear:
  control-layer or rate label recovered?: yes | no | C.30.STRAT needed:
  boundary refs used?: observation | actuation | feedback | externality | not used:
  governing pattern for proof, evidence, causal, gate, or assurance claim, if that claim is being made:
  admissibleUse:
  nonAdmissibleUse:
  stop condition:
```

Use `rateBandRefs?`, `controlLayerRefs?`, and `externalityBoundaryRefs?` only when rate, recovered control-layer, or externality wording carries a control-structure claim being made. Otherwise the ordinary note may stop after one control relation, loop state, and the proof-governing pattern application named by value if that claim is being made. Generic stratification labels stay with `C.30.STRAT` until recovered.

When a recovered control-layer relation is used to justify decomposition, substitution, or design reliance, recover the inter-layer assumption-guarantee relation or mark the control-layer relation as orientation only. `interLayerControlRelationRefs?` is used only when the relation is already control-specific and is used for decomposition, substitution, design reliance, safety, or stability claim kinds.

```text
InterLayerControlRelationNote:
  upperLayerAssumptionRefs:
  lowerLayerGuaranteeRefs:
  observationRequirementRefs:
  actuationAuthorityRefs:
  latencyOrRateEnvelopeRefs:
  violationFallbackRefs:
  admissibleUse:
  nonAdmissibleUse:
```

Use this note only when a recovered control-layer relation is used for decomposition, substitution, safety or stability claim, or architecture decision claim. It is not proof. Otherwise keep C.30.LCA at the small note or ordinary view form, or return the source label to `C.30.STRAT`.

```text
ControlStructureView@Context ::= {
  architectureClaimRef : ArchitectureOf@ContextRef,
  descriptionContext   : DescriptionContext(
    EntityOfConcernRef = selectedControlStructureEntityOfConcernRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = viewpointRef
  ),
  selectedControlStructureEntityOfConcernRef :
    U.StructureRef | FinSet(QualifiedRelationRecordRef),
  viewpointRef (= descriptionContext.ViewpointRef),
  structureKindRef = ControlStructure,

  controlRoleRefs : FinSet(PlannerRef | RegulatorRef | ControllerRef |
                           ObserverEstimatorRef | PlantProcessRef | SupervisorRef),
  controlRelationRefs       : FinSet(QualifiedRelationRecordRef),
  controlLayerRefs?         : FinSet(ControlLayerRef),
  rateBandRefs?             : FinSet(RateBandRef),
  interLayerControlRelationRefs? : FinSet(InterLayerControlRelationRef(
    assumptionRefs,
    guaranteeRefs,
    allowedControlActionRefs,
    observationRequirementRefs,
    actuationAuthorityRefs,
    latencyOrRateEnvelopeRefs,
    violationFallbackRefs
  )),
  stratificationRepairRefs? : FinSet(C30STRATRepairRef),
  supervisorSubholonRelationRefs? : FinSet(B25SupervisorSubholonRelationRef),
  feedbackRelationRefs      : FinSet(QualifiedRelationRecordRef),
  observationBoundaryRefs?  : FinSet(BoundaryRef),
  actuationBoundaryRefs?    : FinSet(BoundaryRef),
  externalityBoundaryRefs?  : FinSet(BoundaryRef),
  controlledHolonRefs?     : FinSet(U.HolonRef),

  rateSeparationClaimRefs? : FinSet(C27TemporalClaimRef | TemporalAdequacyClaimRef),
  dynamicsClaimRefs?       : FinSet(A3_3DynamicsRef),
  gateDecisionRefs?          : FinSet(A20ConstraintValidityRef | A21GateDecisionRef),
  transformationFlowPathSliceRefs? : FinSet(PathSliceId),
  stabilityClaimRefs?    : FinSet(DynamicsRef | StabilityEvidenceRef),
  evidenceClaimRefs?     : FinSet(A10EvidenceGraphRef | G6EvidenceRef),
  assuranceClaimRefs?    : FinSet(B3AssuranceRef),
  causalUseClaimRefs?    : FinSet(C28ApplicationRef),
  scaleAuditRef?           : ArchitectureScaleAuditRecordRef,
  MathLensUseOutputRefs?           : FinSet(MathLensUseOutputRef),

  admissibleUse,
  nonAdmissibleUse,
  sourceReturnCondition
}
```

`DescriptionContext.EntityOfConcernRef` names the selected control structure or control-structure relation set represented by `selectedControlStructureEntityOfConcernRef`. `architectureClaimRef` names the enclosing architecture claim and supplies the bounded context and described holon; it is not the EntityOfConcern of the control-structure view itself.

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

**Control-specific stratification gate.** `Layer`, `level`, `tier`, and `stack` enter C.30.LCA only after `C.30.STRAT` or the local sentence recovers a control-specific item: `controlLayerRef`, `controlRoleRef`, `controlRelationRef`, `interLayerControlRelationRef`, `rateBandRef`, bounded context, and, where the supervisor-subholon relation is being claimed, `B.2.5` supervisor-subholon relation. Generic system level, aggregation scope, organization level, work or evidence scope, scale window, coarse-graining, deployment tier, and publication section do not stay in C.30.LCA. A layer label is not a control structure, not a system level, not a rate band, and not evidence of separation by itself.

**B.2.5 boundary.** `B.2.5` remains the owner for the supervisor-subholon feedback relation. `C.30.LCA` can cite a `B.2.5` relation when a supervisor-subholon relation is part of the control view. Loop wording stays in C.30.LCA only when the current control view explicitly recovers a control-loop or dynamics claim under its direct owner. `C.30.LCA` does not use `B.2.5` prose as proof of stability, safety, causality, evidence sufficiency, gate validity, or assurance. If an episteme appears in a control example, name the acting system in the relevant role, the A.3.4 transformer-position only when a transformation claim is current, and any publication, review record, publication relation, source relation, or reliance relation. An episteme does not sense, judge, plan, adapt, or act as an agent.

**Transformation-flow boundary.** An `E.18` transformation-flow path slice may supply flow-structure, path, crossing, or transformation-flow-structure input to the control view when that relation is being used. The transformation-flow graph expression remains a mathematical description or view of transformation-flow structure. It does not become the functional architecture, the control structure, or proof of control adequacy.

**C.29 boundary.** LCA may be an accepted local control-theory description in one context and a transferable mathematical lens in another. When transfer, prediction, assurance input, or reusable cross-domain explanation is being claimed, use `MathLensUse.FullCard` or at least `MathLensUse.MiniCard`. Dynamics, temporal aspects or rate bands, authored temporal-claim adequacy, and causal claims are still assigned to `A.3.3`, `C.27.TA`, `C.27`, and `C.28`.

**Nesting and scale rule.** If a control-structure view nests without a local depth limit, the record uses `scaleAuditRef?` when the nesting affects latency, stability, observability, accountability, or assurance.

**Worked slice A - LCA diagram used as proof.** A safety note says: `The Layered Control Architecture proves the plant is safe because the supervisor monitors the lower controller.` A conforming repair keeps the control-structure view and names planner, controller, plant, and supervisor relations, observation and actuation boundaries, and any rate bands. Safety and assurance claims use `B.3`, evidence to `A.10` or `G.6`, temporal-aspect and rate-band claims to `C.27.TA`, authored temporal-claim adequacy to `C.27`, and dynamics or stability claims use `A.3.3` or the appropriate dynamics claim.

**Worked slice B - multi-rate controller.** A source says a control stack has a slow planner, a faster regulator, and an observer with a different update period. Apply `C.30.LCA` to the case only after the stack label has been recovered as control roles, relations, and rate bands; otherwise the label is recovered first by `C.30.STRAT`. C.30.LCA does not claim rate adequacy. If the rate relation matters for oscillation, latency, stability, or safety, the next admissible use is `C.27.TA` for temporal aspect or rate-band structure, plus `C.27` only when an authored temporal-claim adequacy question is under repair, and the dynamics or assurance pattern named by value when that claim kind is being made.

**Worked slice C - supervisor-subholon loop.** A subsystem is supervised by an external controller that changes allowed modes. `C.30.LCA` records the supervisor-subholon relation and may reference `B.2.5`. If the text claims that this loop authorizes work, passes a gate, or proves a policy constraint, the claim uses `A.15`, `A.20`, or `A.21`.

