---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__005_solution.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:4 — Solution"
line_start: 51676
line_end: 51778
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
  - "C.30.TGA-FLOW-REL"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller/plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:4 - Solution

Treat LCA-like material as a control-structure view under `C.30`. Recover the described architecture claim, the control roles, the control relations, the relevant rate bands or declared control-layer labels, and the boundary refs that make the view checkable. Then state the admissible use and the non-admissible overread.

Use `rateBandRefs?`, `controlLayerRefs?`, and `externalityBoundaryRefs?` only when rate, control-layer, or externality wording carries a live claim. Otherwise the ordinary note may stop after one control relation, loop posture, any live layer or rate label, and the neighboring proof or support exit if that exit is live.

When a layer relation is used to justify decomposition, substitution, or design reliance, recover the inter-layer assumption-guarantee relation or mark the layer relation as orientation only. `interLayerControlRelationRefs?` opens only when the layer relation is used for decomposition, substitution, design reliance, safety, or stability claim kinds.

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

Open this note only when a layer relation is used for decomposition, substitution, safety or stability support, or architecture decision support. It is not proof. Otherwise keep C.30.LCA at the small note or ordinary view form.



```text
ControlStructureView@Context ::= {
  architectureClaimRef : ArchitectureOf@ContextRef,
  descriptionContext   : DescriptionContext(
    DescribedEntityRef = architectureClaimRef,
    BoundedContextRef = ArchitectureOf@Context.boundedContextRef,
    ViewpointRef = viewpointRef
  ),
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
  declaredSystemLevelRefs?  : FinSet(SystemLevelRef),
  aggregationScopeRefs?     : FinSet(AggregationScopeRef),
  organizationLevelRefs?    : FinSet(OrganizationLevelRef),
  workEvidenceScopeRefs?    : FinSet(ScopeRef),
  scaleWindowRefs?          : FinSet(ScaleWindowRef),
  feedbackRelationRefs      : FinSet(QualifiedRelationRecordRef),
  observationBoundaryRefs?  : FinSet(BoundaryRef),
  actuationBoundaryRefs?    : FinSet(BoundaryRef),
  externalityBoundaryRefs?  : FinSet(BoundaryRef),
  controlledSystemRefs?     : FinSet(U.HolonRef),

  rateSeparationSupportRefs? : FinSet(C27TemporalClaimRef | TemporalAdequacySupportRef),
  dynamicsSupportRefs?       : FinSet(A3_3DynamicsRef),
  gateDecisionRefs?          : FinSet(A20ConstraintValidityRef | A21GateDecisionRef),
  TGAPathSliceRefs?        : FinSet(PathSliceId),
  stabilitySupportRefs?    : FinSet(DynamicsRef | StabilityEvidenceSupportRef),
  evidenceSupportRefs?     : FinSet(A10EvidenceGraphRef | G6EvidenceSupportRef),
  assuranceSupportRefs?    : FinSet(B3AssuranceRef),
  causalUseSupportRefs?    : FinSet(C28ApplicationRef),
  scaleAuditRef?           : ArchitectureScaleAuditRecordRef,
  MLAOutputRefs?           : FinSet(MLAOutputRef),

  admissibleUse,
  nonAdmissibleUse,
  sourceReturnCondition
}
```

**Role reading.**

| Source label | FPF reading |
|---|---|
| Plant or controlled system | `U.System` whose state evolves; reusable state-evolution claims use `A.3.3`. |
| Regulator or controller | System in a control role enacting a method over observations and actuations. |
| Planner | Upstream role or method producing targets, plans, references, or allowed regions for regulators. |
| Observer or estimator | Role or method producing state estimates, observations, or evidence-facing readouts. |
| Supervisor | Role or method governing subordinate holons, gates, policy changes, or control-mode changes. |

**Layer, level, tier, stack, and rate rule.** `Control layer` may remain as an LCA source label only when the record names the control role, relation, rate band, and bounded context. When the source says layer, level, tier, or stack, recover exactly one or more of: `controlLayerRef`, `declaredSystemLevelRef`, `aggregationScopeRef`, `rateBandRef`, `organizationLevelRef`, `workEvidenceScopeRef`, `scaleWindowRef`, or `publicationSectionRef` when the wording only names a document layer. `System level` is not a synonym for control layer. Use it only for a declared system level or aggregation scope, with the relevant `B.2.5` supervisor-subholon relation or comparable declared relation recovered. A layer label is not a structure kind, not a system level, not a rate band, and not evidence of separation by itself. In renormalization, coarse-graining, or mathematical-lens use, prefer `scale`, `scale window`, `coarse-graining scale`, `coarse-graining step`, or `resolution` for the lens itself.

**B.2.5 boundary.** `B.2.5` remains the supervisor-subholon feedback-loop check pattern. `C.30.LCA` can cite a `B.2.5` relation when a supervisor-subholon loop is part of the control view. It does not use `B.2.5` prose as proof of stability, safety, causality, evidence sufficiency, gate validity, or assurance. If an episteme appears in a control example, the acting `Transformer`, publication or review practice, and publication/support relation are named; an episteme does not sense, judge, plan, adapt, or act as an agent.

**TGA boundary.** A TGA path slice may support the control view when flow or transduction relation is live. The TGA graph remains a description or view of flow/transduction structure. It does not become the functional architecture, the control structure, or proof of control adequacy.

**C.29 boundary.** LCA may be an accepted local control-theory description in one context and a transferable mathematical lens in another. When transfer, prediction, assurance input, or reusable cross-domain explanation is live, use `MLA.FullCard` or at least `MLA.MiniCard`. Dynamics, temporal adequacy, and causal claims are still assigned to `A.3.3`, `C.27`, and `C.28`.

**Nesting and scale rule.** If a control-structure view nests without a local depth limit, the record uses `scaleAuditRef?` when the nesting affects latency, stability, observability, accountability, or assurance.

**Worked slice A - LCA diagram used as proof.** A safety note says: `The Layered Control Architecture proves the plant is safe because the supervisor monitors the lower controller.` A conforming repair keeps the control-structure view and names planner/controller/plant/supervisor relations, observation and actuation boundaries, and any rate bands. Safety and assurance support move to `B.3`, evidence to `A.10` or `G.6`, temporal adequacy to `C.27`, and dynamics/stability to `A.3.3` or the appropriate dynamics support.

**Worked slice B - multi-rate controller.** A control stack has a slow planner, a faster regulator, and an observer with a different update period. `C.30.LCA` records the roles, relations, and rate bands. It does not claim rate adequacy. If the rate relation matters for oscillation, latency, stability, or safety, the next admissible move is `C.27` plus dynamics or assurance support as live.

**Worked slice C - supervisor-subholon loop.** A subsystem is supervised by an external controller that changes allowed modes. `C.30.LCA` records the supervisor-subholon relation and may reference `B.2.5`. If the text claims that this loop authorizes work, passes a gate, or proves a policy constraint, the claim exits to `A.15`, `A.20`, or `A.21`.

