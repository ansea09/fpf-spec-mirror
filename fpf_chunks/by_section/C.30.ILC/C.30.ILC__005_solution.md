---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__005_solution.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:4 — Solution"
line_start: 61591
line_end: 61692
dependencies:
  - "A.10"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "D.3"
  - "D.4"
  - "G.5"
  - "G.6"
keywords:
  - "cross-scope residual"
  - "declared scope"
  - "first architecture move"
  - "frustration"
  - "interlevel conflict"
  - "local repair"
  - "residual-bearing locus"
  - "structure kind"
---

### C.30.ILC:4 - Solution

Create a `CrossScopeArchitectureResidualTriageRecord@Context` when an architecture concern is carried by residuals across declared holon levels, declared scopes, or level-bearing structure relations.

```text
CrossScopeArchitectureResidualTriageRecord@Context ::= {
  describedHolonRef,
  boundedContextRef,
  architectureConcernCue,

  declaredHolonLevelRefs?: FinSet(DeclaredHolonLevelRef),
  declaredScopeRefs: FinSet(AggregationScopeRef | DeclaredSystemLevelRef |
                            ControlLayerRef | WorkEvidenceScopeRef |
                            OrganizationScopeRef | SystemEnvironmentScopeRef |
                            RateBandRef | ScaleWindowRef |
                            PublicationSectionRef | OtherDeclaredScopeRef),
  structureKindRefs: FinSet(ArchitectureStructureKindRef),

  interlevelConflictDescription?,
  conflictCarrierRefs?:
    FinSet(ConstraintRef | ObjectiveRef | AdmissibilityConditionRef |
           TempoRef | ResourceAllocationRef | InformationTransferRelationRef |
           AssuranceRequirementRef | OtherDeclaredConflictCarrierRef),
  localScopeOptimizationClaim?,
  widerScopeOptimizationClaim?,
  conflictingConstraintRefs?,
  conflictingCharacteristicRefs?,
  conflictingQBundleRefs?,

  symptom,
  crossScopeResidualDescription,
  crossScopeResidualLocusKind:
    hiddenCoupling | interfaceException | controlRateConflict |
    scaleWindowLoss | evidenceReuseFailure | regulatoryBespokeResidue |
    workMethodException | dataSemanticDrift |
    placementJurisdictionConflict | securityTrustBoundaryBreak |
    otherDeclared,
  frustrationResidualBefore?,
  complexityGrowthPressure?,
  localRepairAttempted?,
  whyLocalRepairInsufficient?,

  firstAdmissibleArchitectureMove:
    splitDeclaredHolonLevel | mergeDeclaredHolonLevel |
    splitDeclaredScope | mergeDeclaredScope |
    splitDeclaredSystemLevel | mergeDeclaredSystemLevel |
    addMediator | addInterfaceGrammar | addControlLayer |
    addEvidenceScope | addWorkMethodScope | changeAllocation |
    exposeHiddenCoupling | acceptBoundedException |
    applyD3D4 | applyC28 | noArchitectureMove,

  triggeredGoverningPatternRefs?,
  admissibleNextMove,
  stopCondition,
  sourceReturnCondition?
}
```

**Layer, level, tier, stack, and declared-scope labels.** `Declared holon level` is the general level-bearing recovery field for this pattern; system level and episteme level are special cases when the described holon or selected structure makes them relevant to the claim. `System level` may remain as ordinary recognition language when a practitioner would naturally use it, but the record recovers the project-side scope references through `declaredHolonLevelRefs` or `declaredScopeRefs`; a system level is not the default architecture level. When the source says layer, level, tier, or stack, recover exactly one or more of: `declaredHolonLevelRef`, `controlLayerRef`, `declaredSystemLevelRef`, `aggregationScopeRef`, `rateBandRef`, `organizationLevelRef`, `workEvidenceScopeRef`, `scaleWindowRef`, or `publicationSectionRef` when the wording only names a document layer. A move such as `splitDeclaredHolonLevel`, `splitDeclaredScope`, or, in the special system-level case, `splitDeclaredSystemLevel` is admissible only when the affected declared holon level, declared scope, selected structure, declared system level, aggregation scope, control layer, organization scope, work scope, evidence scope, system scope, environment scope, rate band, scale window, publication section, or source-return condition is named. A layer label is not a structure kind, not a system level, not a rate band, and not evidence of separation by itself.

**Interlevel conflict, frustration residual, and complexity-growth recovery.** A conflict is architecture-shaping only when the record names the declared holon levels or declared scopes, the selected structure or structure kind that carries them, and the conflict carrier: constraint, objective, admissibility condition, tempo, resource allocation, information-transfer relation, or assurance requirement. A frustration residual is architecture-shaping only when local repair or local optimization leaves a persistent residual in another declared holon level, declared scope, or level-bearing structure relation. Complexity-growth pressure is only a candidate reason to add, split, mediate, or stabilize structure when that change is expected to reduce the residual enough to justify the new cost and its own residue.

`crossScopeResidualDescription` is not enough by itself. A residual becomes architecture-shaping only when its residual-bearing locus is declared: hidden coupling, interface exception, control-rate conflict, scale-window loss, evidence-reuse failure, regulatory bespoke residue, work-method exception, data-semantics drift, placement or jurisdiction conflict, security trust-boundary break, or another declared locus.

**Multilevel optimization boundary.** `C.30.ILC` can recognize that local optimization in one declared holon level or declared scope degrades another declared holon level or declared scope. It does not optimize the architecture and does not prove that one global function exists. Use `C.29` with `MLU.Description@MultilevelLearningFrustration` only when the mathematical representation supplies a recoverable mapping between declared levels, scopes, scale windows, or coarse-graining steps and states what structure is preserved and lost. Conflicting structures can enter this lens only when each structure is assigned to a declared holon level, scope, scale window, or coarse-graining step and the mapping shows why the conflict is interlevel. If scale window, RG relation, coarse-graining relation, preserved structure, lost structure, or conflict residual slope becomes an architecture scale-preference claim, use `C.31.ASAP` and keep any mathematical-lens claim in `C.29`. If the practitioner needs to generate or compare residual-reducing candidate architecture moves, apply `C.32.MLAO` for the residual-reducing multilevel candidate frame and `C.32` for the candidate palette. Use `G.5` only when selected-set publication is current, `C.11` when final local choice is current, and `C.32.PAD` when project architecture decision is current; `C.30.ILC` stops at the residual and first admissible move. If the case is only a conflict between two selected structures with no declared multilevel mapping or scale mapping, keep it in `C.30`, `C.30.ASV`, `D.3`, `D.4`, `C.28`, evidence, assurance, or decision patterns as applicable.

Anti-collapse rule: no generic frustration score, no risk-matrix residual, no ethical-mediation takeover, no physics or biology ontology transfer, no global-optimizer proof, no causal proof, and no assurance proof. A frustration or risk label does not govern the case until declared holon levels or declared scopes, the selected structure or structure kind that carries them, residual-bearing locus, and first architecture move are recoverable; `D.3` applies only when interlevel ethical conflict structure is current; `D.4` applies only when mediation or decision use of that structure is current.

**Stop condition.** Stop after `CrossScopeArchitectureResidualTriageRecord@Context` when it names the residual and the first admissible architecture move. It does not measure scale preference, generate candidate architectures, mediate ethical conflict, or select a decision. Apply a governing pattern only when a claim kind being made exists:

| Claim kind being made | Governing pattern to apply |
|---|---|
| measurement or characteristic claim | `C.16` or the characteristic pattern that governs the characteristic under evaluation |
| scale window, RG relation, coarse-graining relation, preserved structure, lost structure, or conflict residual slope | `C.31.ASAP` when an architecture scale-preference claim is being made; use `C.29` when mathematical-lens use is being claimed |
| multilevel learning or frustration mathematical-lens use with recoverable level mapping or scale mapping | `C.29` with `MLU.Description@MultilevelLearningFrustration` |
| candidate generation or residual-reducing candidate architecture moves | `C.32.MLAO` when the residual-reducing multilevel frame is current; `C.32` for the candidate palette; `G.5` when selected-set publication is current; `C.11` when final local choice is current; `C.32.PAD` when project architecture decision is current |
| final local choice | `C.11` |
| causal outcome claim | `C.28` |
| evidence or assurance | `A.10`, `B.3`, or `G.6` |
| ethical conflict structure, mediation, or decision use | `D.3` for interlevel ethical conflict structure; `D.4` for mediation and decision use of that structure |

**D.3 and D.4 boundary.** `D.3` handles interlevel ethical conflict structure: affected holons, systems, epistemes, collections, declared levels or scopes, interests or concerns, value frames, agency or responsibility thresholds, methods, work, transformations, evidence, uncertainty, and consequence horizons. `D.4` handles mediation and decision use of that `D.3` structure: mediation, refusal, evidence demand, causal return, assurance return, architecture return, accepted residual, and bounded decision use. `C.30.ILC` handles architecture-specific recognition: whether the conflict or residual is borne by declared holon levels or declared scopes inside a selected structure such as structural views, allocation, interfaces, control rates, work reuse, evidence reuse, scale windows, or coarse-graining loss. It is a triage and architecture-move pattern, not an ethical mediation pattern.

**Architecture-move examples.**

| Cue | Admissible architecture move | Non-admissible overread |
|---|---|---|
| Component optimization breaks integration | expose hidden coupling; add interface grammar; change allocation | Treat local performance as whole-holon adequacy. |
| Modularity reduces local work and increases exceptions | accept bounded exception; revise module boundary; add work scope or evidence scope | Average exceptions into a modularity score without declared scope, comparator, and measurement relation. |
| Local autonomy conflicts with control scope | add control layer; change allocation; apply `C.30.LCA` | Treat autonomy label as causal or safety proof. |
| Evidence reuse hides source loss | add evidence scope; add source-return condition; apply `A.10` or `G.6` | Treat reused evidence as automatically valid in the wider scope. |
| A scale window changes the residual | apply `C.31.ASAP`, with `C.29` when scale-lens use is being made | Treat two observations as a universal scale law. |
| A frustration lens with recoverable level mapping or scale mapping makes candidate moves comparable | use `C.29` for lens adequacy; use `C.32.MLAO` and `C.32` when a residual-reducing candidate palette is current; use `G.5` only when selected-set publication is current | Treat an unassigned or same-scope structure conflict as RG mathematics or frustration mathematics, or treat an interlevel residual without recoverable mapping as a global optimizer, proof, or selected architecture. |

**Worked slice A - clean module layout, bad flow.** A product team redraws modules so each component has an explicit responsibility relation or enactor relation, but order-to-cash flow now crosses more work transfers and exceptions rise. `C.30.ILC` names the module structure, transformation-flow structure, affected work scope, cross-scope residual, and first move: expose hidden coupling or apply `C.30.TFS-REL`. It does not turn the exception count into a modularity measure until `C.16` or the characteristic pattern governing the characteristic under evaluation is applied.

**Worked slice B - AI agent control conflict.** A local agent optimizes its local objective and violates a supervisor's allowed-mode constraint. `C.30.ILC` names the agent scope, supervisor scope or control scope, control relation, local optimization claim, residual-bearing locus, and local repair attempted. The first move may be add control layer, change allocation, or apply `C.30.LCA`. Safety, causality, and gate claims use their governing patterns.

**Worked slice C - evidence scope residue.** A reusable certification evidence set removes repeated evidence work for several product variants, but one variant has a hidden environment difference. `C.30.ILC` names the work scope or evidence scope and source-return condition. The practitioner applies `A.10` or `G.6` when an evidence-validity claim is being made.

**Worked slice D - frustration residual before synthesis.** Several decompositions reduce local module work but each creates a different integration, control-rate, or evidence-reuse residual in another declared scope. `C.30.ILC` records the residuals and first architecture moves. If the team needs a residual-reducing candidate palette, stop the C.30.ILC use and apply `C.32.MLAO` for the residual-reducing frame and `C.32` for the candidate palette. Use `G.5` only when the palette or retained set must become a public selected-set result. If the team claims a multilevel-learning lens or frustration lens, `C.29` carries the lens-use fields and stop condition only after the level mapping, scope mapping, scale-window mapping, or coarse-graining mapping and preserved structure and lost structure are recoverable.

