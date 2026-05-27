---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__005_solution.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:4 — Solution"
line_start: 52340
line_end: 52424
dependencies:
  - "A.10"
  - "A.22"
  - "A.6.F"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.TGA-FLOW-REL"
  - "D.3"
  - "D.4"
  - "G.5"
  - "G.6"
keywords:
  - "cross-scope residual"
  - "declared scope"
  - "frustration"
  - "interlevel conflict"
  - "local repair"
  - "source return"
  - "structure kind"
---

### C.30.ILC:4 - Solution

Create a `CrossScopeArchitectureResidualTriage@Context` record when an architecture concern is carried by residuals across declared scopes or structure kinds.

```text
CrossScopeArchitectureResidualTriage@Context ::= {
  describedHolonRef,
  boundedContextRef,
  liveArchitectureConcernCue,

  declaredScopeRefs: FinSet(AggregationScopeRef | DeclaredSystemLevelRef |
                            ControlLayerRef | WorkEvidenceScopeRef |
                            OrganizationScopeRef | SystemEnvironmentScopeRef |
                            RateBandRef | ScaleWindowRef |
                            PublicationSectionRef | OtherDeclaredScopeRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),

  localScopeOptimizationClaim?,
  widerScopeOptimizationClaim?,
  conflictingConstraintRefs?,
  conflictingCharacteristicRefs?,
  conflictingQBundleRefs?,

  symptom,
  crossScopeResidualDescription,
  crossScopeResidualCarrierKind:
    hiddenCoupling | interfaceException | controlRateConflict |
    scaleWindowLoss | evidenceReuseFailure | regulatoryBespokeResidue |
    workMethodException | dataSemanticDrift |
    placementJurisdictionConflict | securityTrustBoundaryBreak |
    otherDeclared,
  localRepairAttempted?,
  whyLocalRepairInsufficient?,

  firstAdmissibleArchitectureMove:
    splitDeclaredSystemLevel | mergeDeclaredSystemLevel | addMediator |
    addInterfaceGrammar | addControlLayer | addEvidenceScope |
    addWorkMethodScope | changeAllocation | exposeHiddenCoupling |
    acceptBoundedException | applyD3D4 | applyC28 |
    noArchitectureMove,

  triggeredGoverningPatternRefs?,
  admissibleNextMove,
  stopCondition,
  sourceReturnCondition?
}
```

**Layer, level, tier, stack, and system-level wording.** `System level` may remain as ordinary recognition language when a practitioner would naturally use it, but the record recovers it through `declaredScopeRefs`. When the source says layer, level, tier, or stack, recover exactly one or more of: `controlLayerRef`, `declaredSystemLevelRef`, `aggregationScopeRef`, `rateBandRef`, `organizationLevelRef`, `workEvidenceScopeRef`, `scaleWindowRef`, or `publicationSectionRef` when the wording only names a document layer. A move such as `splitDeclaredSystemLevel` is admissible only when the affected declared system level, aggregation scope, control layer, organization scope, work/evidence scope, system/environment scope, rate band, scale window, publication section, or source-return condition is named. A layer label is not a structure kind, not a system level, not a rate band, and not evidence of separation by itself.

`crossScopeResidualDescription` is not enough by itself. A residual becomes architecture-shaping only when its carrier is declared: hidden coupling, interface exception, control-rate conflict, scale-window loss, evidence-reuse failure, regulatory bespoke residue, work-method exception, data-semantics drift, placement or jurisdiction conflict, security trust-boundary break, or another declared carrier.

Anti-collapse rule: no generic frustration score, no risk-matrix residual, and no stakeholder-mediation takeover. A frustration or risk label is only a cue until declared scopes, structure kinds, residual carrier, and first architecture move are recoverable; stakeholder mediation applies `D.3`/`D.4` only when values, ethical conflict, or negotiation is live.

**Stop condition.** Stop after `CrossScopeArchitectureResidualTriage@Context` when it names the residual and the first admissible architecture move. It does not measure scale preference, generate candidate architectures, mediate stakeholder conflict, or select a decision. Apply an exact governing pattern only when a live claim kind exists:

| Live claim kind | Governing pattern to apply |
|---|---|
| measurement or characteristic claim | `C.16` or an admitted characteristic/measurement receiving pattern |
| scale or coarse-graining claim | `C.29` or an admitted scale/coarse-graining receiving pattern when the scale lens is live |
| candidate generation | `G.5` or an admitted candidate-generation receiving pattern |
| final local choice | `C.11` |
| causal outcome claim | `C.28` |
| evidence or assurance | `A.10`, `B.3`, or `G.6` |
| ethical or stakeholder mediation | `D.3` / `D.4` |
| mathematical-lens transfer | `C.29` |

**D.3/D.4 boundary.** `D.3` and `D.4` handle conflict topology, values, stakeholder mediation, and ethical negotiation. `C.30.ILC` handles architecture-specific recognition: whether the conflict is carried by declared scopes, structural views, allocation, interfaces, control rates, work/evidence reuse, scale windows, or coarse-graining loss. It is a triage and architecture-move pattern, not a negotiation pattern.

**Architecture-move examples.**

| Cue | Admissible architecture move | Non-admissible overread |
|---|---|---|
| Component optimization breaks integration | expose hidden coupling; add interface grammar; change allocation | Treat local performance as system adequacy. |
| Modularity reduces local work and increases exceptions | accept bounded exception; revise module boundary; add work/evidence scope | Average exceptions into a modularity score without declared basis. |
| Local autonomy conflicts with control scope | add control layer; change allocation; apply `C.30.LCA` | Treat autonomy label as causal or safety proof. |
| Evidence reuse hides source loss | add evidence scope; add source-return condition; apply `A.10`/`G.6` | Treat reused evidence as automatically valid in the wider scope. |
| A scale window changes the residual | apply `C.29` or an admitted scale/coarse-graining receiving pattern if the scale lens is live | Treat two observations as a universal scale law. |

**Worked slice A - clean module layout, bad flow.** A product team redraws modules so each component has an explicit responsibility/enactor relation, but order-to-cash flow now crosses more work transfers and exceptions rise. `C.30.ILC` names the module structure, flow/transduction structure, affected work scope, cross-scope residual, and first move: expose hidden coupling or open `C.30.TGA-FLOW-REL`. It does not turn the exception count into a modularity measure until `C.16` or an admitted characterization-support receiving pattern is live.

**Worked slice B - AI agent control conflict.** A local agent optimizes its local objective and violates a supervisor's allowed-mode constraint. `C.30.ILC` names the agent scope, supervisor/control scope, control relation, and local repair attempted. The first move may be add control layer, change allocation, or open `C.30.LCA`. Safety, causality, and gate claims use their exact governing patterns.

**Worked slice C - evidence scope residue.** A reusable certification evidence set removes repeated evidence work for several product variants, but one variant has a hidden environment difference. `C.30.ILC` names the work/evidence scope and source-return condition. It applies `A.10` or `G.6` when evidence validity becomes live.

