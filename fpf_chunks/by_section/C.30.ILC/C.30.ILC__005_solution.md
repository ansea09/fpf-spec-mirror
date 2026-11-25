---
chunk_kind: "child"
pattern_id: "C.30.ILC"
pattern_title: "Cross-Scope Architecture Residual Triage"
section_id: "C.30.ILC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.ILC/C.30.ILC__005_solution.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "C.30.ILC — Cross-Scope Architecture Residual Triage"
  - "C.30.ILC:4 — Solution"
line_start: 78261
line_end: 78379
dependencies:
  - "A.10"
  - "A.22"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
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

When an architecture concern involves residuals across declared levels or scopes, identify the related structures, the conflicting conditions and the locus where the loss remains. Preserve an adequate ordinary account; use `CrossScopeArchitectureResidualTriageRecord@Context` when its fields help retain or compare those distinctions. The record does not itself establish the conflict. When a bounded exception would address it, determine what makes that exception effective. A standing rule may already cover the case. If the decision is reserved, an architect can propose the exception and explain its scope. Giving it effect requires the decision entrusted to the named person, service or joint body. Where no exception is permitted, seek a design within the constraint.

```text
CrossScopeArchitectureResidualTriageRecord@Context ::= {
  describedHolonRef,
  architectureConcernCue,
  intendedArchitectureUse,
  claimScopeRef?: U.ClaimScope,
  qualificationWindowRef?,
  boundedModelUseStructureRef?,

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
    applyD3D4 | applyC28 | otherDeclared | noArchitectureMove,

  triggeredPatternLocators?,
  admissibleNextMove,
  stopCondition,
  sourceReturnCondition?
}
```

**Layer, level, tier, stack, and declared-scope labels.** Use `declaredHolonLevelRefs` for levels in the established composition of the holon kind at issue. A mismatch between a particular work occurrence and its constituent actions, for instance, can matter to a handover. For control functions, ranges of operation and other scopes, recover the relation the claim actually uses (C.30.STRAT:4.2). `System level` may remain as ordinary recognition language when a practitioner would naturally use it, but the record recovers the project-side scope references through `declaredHolonLevelRefs` or `declaredScopeRefs`; a system level is not the default architecture level.

When the source says layer, level, tier, or stack, recover one or more of: `declaredHolonLevelRef`, `controlLayerRef`, `declaredSystemLevelRef`, `aggregationScopeRef`, `rateBandRef`, `organizationLevelRef`, `workEvidenceScopeRef`, `scaleWindowRef`, or `publicationSectionRef` when the wording only names a document layer.

A move such as `splitDeclaredHolonLevel`, `splitDeclaredScope`, or, in the special system-level case, `splitDeclaredSystemLevel` is admissible only when the affected declared holon level, declared scope, selected structure, declared system level, aggregation scope, control layer, organization scope, work scope, evidence scope, system scope, environment scope, rate band, scale window, publication section, or source-return condition is named.

A layer label is not a structure kind, not a system level, not a rate band, and not evidence of separation by itself.

**Interlevel conflict, frustration residual, and complexity-growth recovery.** A conflict is architecture-shaping only when the account identifies the declared holon levels or declared scopes, the selected structure or structure kind that carries them, and the conflict carrier: constraint, objective, admissibility condition, tempo, resource allocation, information-transfer relation, or assurance requirement. A frustration residual is architecture-shaping when the cross-scope loss persists after attempted local repair, or when a stated reason shows why that repair would leave the loss unresolved. Complexity-growth pressure is only a candidate reason to add, split, mediate, or stabilize structure when that change is expected to reduce the residual enough to justify the new cost and its own residue.

Identify the constraints whose combination matters, their connections and what their sources establish. When different models group the arrangements differently, check whether the apparently conflicting conditions can occur together in the use under inquiry. If separate summaries lost their pairing, restore the joint constraint before attributing a conflict to the architecture. The loss of that relation can itself answer a question about the descriptions. If an exchange can return an acknowledgement no earlier than 10 seconds after a request and the receiver accepts it only within 5 seconds of that same request, the design cannot complete that exchange as specified. The two bounds already settle the design decision. To attribute a particular cell stop to this conflict, establish which request was outstanding at the deadline, whether a reply had arrived by then and which rule actually stopped the cell. A competing explanation matters when it changes the causal account or the action the recipient needs. Apply C.28 when attributing a change in the rate of stops across jobs to the retuning.

**Multilevel optimization boundary.** First establish whether local optimization in one declared holon level or scope degrades another declared holon level or scope. This triage neither optimizes the architecture nor proves that one global function exists. A mathematical treatment needs a recoverable mapping between declared levels, scopes, scale windows or coarse-graining steps, with the distinctions preserved and lost for its use. Retain an adequate domain treatment directly. Use C.29 when formulation, transfer or reliance remains unresolved; its `MLU.Description@MultilevelLearningFrustration` form is optional unless the receiving interface requires it.

Conflicting structures can enter this lens only when each structure is assigned to a declared holon level, scope, scale window, or coarse-graining step and the mapping shows why the conflict is interlevel. If scale window, RG relation, coarse-graining relation, preserved structure, lost structure, or conflict residual slope becomes an architecture scale-preference claim, use `C.31.ASAP` and use C.29 for any remaining mathematical formulation, transfer or reliance question.

If the practitioner needs to generate residual-reducing candidate architecture moves, apply `C.32.MLAO` for the residual-reducing multilevel candidate frame and `C.32` for the candidate palette. Use `A.19.CPM` for comparison under a declared comparator, `G.5` only when selected-set result declaration is current, and `C.11` when final local choice is current. For audience publication, use `E.17` for a source-backed face and return to source and `E.24.PUB` for the publication occurrence and audience availability. Use `C.32.PAD` when a project architecture decision is current.

Stop the C.30.ILC use at the residual and first admissible move. If the case is only a conflict between two selected structures with no recoverable assignment to different declared levels or scopes, keep it in `C.30`, `C.30.ASV`, `D.3`, `D.4`, `C.28`, evidence, assurance, or decision patterns as applicable.

**Stop condition.** Stop when the account names the residual and the first warranted move, including a supported conclusion that no architecture move is needed. The triage does not measure scale preference, generate candidate architectures, mediate ethical conflict, or select a decision. Apply a subject pattern only when making a claim of its kind:

| Claim kind being made | Subject pattern to apply |
|---|---|
| measurement or characteristic claim | `C.16` or the characteristic pattern that defines or constrains the characteristic under evaluation |
| scale window, RG relation, coarse-graining relation, preserved structure, lost structure, or conflict residual slope | `C.31.ASAP` for an architecture scale-preference claim; `C.29` for a remaining mathematical formulation, transfer or reliance question. |
| multilevel learning or frustration mathematical treatment with recoverable level or scale mapping | Retain an adequate domain result; use `C.29` for an unresolved formulation, transfer or reliance question, with its MLU form when needed. |
| candidate generation or residual-reducing candidate architecture moves | `C.32.MLAO` when the residual-reducing multilevel frame is current; `C.32` for the candidate palette; `G.5` when selected-set result declaration is current; `E.17` for a source-backed publication face and source return and `E.24.PUB` for the publication occurrence and audience availability when publication is current; `C.11` when final local choice is current; `C.32.PAD` when a project architecture decision is current |
| final local choice | `C.11` |
| causal outcome claim | `C.28` |
| evidence or assurance | `A.10` for source recovery and bounded reliance; `G.6` for addressable provenance paths; `B.3` when a named assurance claim is current |
| ethical conflict description, mediation, or decision use | `D.3` for the interlevel ethical conflict description; `D.4` for mediation and decision use of that description |

**D.3 and D.4 boundary.** D.3 connects each ethical claim to the affected entity, declared level relation or scope, value premise and any frame edition used, expected consequence, horizon, and evidence use or uncertainty when current, then states the tension among the sides. Identify the conflict-description episteme when the receiving use needs to cite or revise it. A D.4 use takes that description into mediation, refusal, evidence demand, causal return, assurance return, architecture return, accepted residual, or bounded decision use.

`C.30.ILC` handles architecture-specific recognition: whether the conflict or residual is borne by declared holon levels or declared scopes within a selected structure. Such a residual may concern allocation, interfaces, control rates, work reuse, evidence reuse, scale windows, or coarse-graining loss. Structural views may help describe the selected structure and locate the residual. `C.30.ILC` is a triage and architecture-move pattern, not an ethical mediation pattern.

**Architecture-move examples.**

| Cue | Admissible architecture move | Non-admissible overread |
|---|---|---|
| Component optimization breaks integration | expose hidden coupling; add interface grammar; change allocation | Treat local performance as whole-holon adequacy. |
| Modularity reduces local work and increases exceptions | Use a covered exception, seek a decision about a proposed one, or revise the module boundary, work scope or evidence scope. | Treat a proposal as permission, or hide exceptions in an average with no declared scope, comparator and measurement basis. |
| Local autonomy conflicts with control scope | add control layer; change allocation; apply `C.30.LCA` | Treat autonomy label as causal or safety proof. |
| Evidence reuse hides source loss | add evidence scope; add source-return condition; use `A.10` for source recovery and bounded reliance, and `G.6` when the provenance path must remain addressable | Treat reused evidence as automatically valid in the wider scope. |
| A scale window changes the residual | apply `C.31.ASAP`, with `C.29` when scale-lens use is being made | Treat two observations as a universal scale law. |
| A frustration lens with recoverable level mapping or scale mapping makes candidate moves comparable | use `C.29` for lens adequacy; use `C.32.MLAO` and `C.32` when a residual-reducing candidate palette is current; use `G.5` only when selected-set result declaration is current | Treat an unassigned or same-scope structure conflict as RG mathematics or frustration mathematics, or treat an interlevel residual without recoverable mapping as a global optimizer, proof, or selected architecture. |

**Worked slice A — clean module layout, bad flow.** A team redraws its module boundaries and reports more order-to-cash exceptions. For the proposed layout, trace one eligible order through the required handoffs and identify any new transfer the design imposes. For the current workflow, compare the handoffs actually used for comparable orders before and after the change. The redrawn boundaries may simply expose transfers that already occurred. A new transfer can justify inspecting its interface. Attributing the rise in exceptions to that transfer requires comparing its effects under the relevant conditions. Use C.30.TFS-REL for the flow and C.16 for the exception measure. Suppose an order specification permits an alternate handoff for returns under a stated amount. A qualifying return can use it under that rule. If another order requires the customer’s agreement to the change, the team can explain the delay and request the exception. The original handoff stays due until the agreement takes effect.

**Worked slice B - AI agent control conflict.** A local agent optimizes its local objective and violates a supervisor's allowed-mode constraint. `C.30.ILC` names the agent scope, supervisor scope or control scope, control relation, local optimization claim, residual-bearing locus, and local repair attempted. The first move may be add control layer, change allocation, or apply `C.30.LCA`. Safety, causality, and gate claims use their subject patterns.

**Worked slice C - evidence scope residue.** A reusable certification evidence set removes repeated evidence work for several product variants, but one variant has a hidden environment difference. `C.30.ILC` names the work scope or evidence scope and source-return condition. The practitioner uses `A.10` for source recovery and bounded reliance, and `G.6` when the provenance path must remain addressable. Whether the evidence meets the certification requirements for that variant is tested under the applicable certification rule.

**Worked slice D - frustration residual before synthesis.** Several decompositions reduce local module work but each creates a different integration, control-rate, or evidence-reuse residual in another declared scope. `C.30.ILC` records the residuals and first architecture moves. If the team needs a residual-reducing candidate palette, stop the C.30.ILC use and apply `C.32.MLAO` for the residual-reducing frame and `C.32` for the candidate palette. Use `G.5` only when the palette or retained set must be declared as a selected-set result for downstream use.

A multilevel-learning or frustration treatment retains the relevant level, scope, scale-window or coarse-graining mapping and the distinctions it preserves or loses. Use C.29 for a remaining formulation, transfer or reliance question; an adequate domain result can finish without its record form.

