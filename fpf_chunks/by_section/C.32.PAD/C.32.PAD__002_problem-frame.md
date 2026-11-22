---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__002_problem-frame.md"
commit_sha: "4ee69807f8e5d4fa438e8c9b5de001d91275cc31"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:1 — Problem frame"
line_start: 84070
line_end: 84192
dependencies:
  - "A.1.STM"
  - "A.10"
  - "A.15"
  - "A.15.6"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "E.11.PUR"
  - "E.17"
  - "E.18.NET"
  - "E.24.PUB"
  - "E.8"
  - "G.5"
keywords:
  - "ArchitectureDecisionRelation@Project"
  - "accepted loss"
  - "affected selected structure"
  - "architect-developer split"
  - "architecture-characteristic trade-off"
  - "method-use instruction"
  - "project architecture decision"
  - "reopen condition"
  - "selected architecture option"
---

### C.32.PAD:1 - Problem frame

Use this pattern when a project must commit to an architecture that will guide design, construction, operation or change. A commission to choose any conforming design can be satisfied with one qualified option. Choosing the best of several designs calls for a comparison. An agreement may already fix a design, leaving the project to establish feasibility and decide how to put the commitment into effect.

An architect or another practitioner responsible for the decision uses the pattern to settle what the project will pursue, which conditions bind it and what can be decided during implementation.

Typical entry phrases:

```text
"We have three candidate architecture configurations; which one becomes the project decision?"
"The candidate improves maintainability but worsens evidence reuse; what is the accepted trade-off?"
"Developers need to know which architectural style, method, or pattern use is now required."
"The architecture decision must say which structure is fixed by this decision and which refinement remains open."
"The ADR cannot be written yet because the decision relation is not clear."
```

**First-minute use slice.** A product-family team has evaluated three arrangements for modules, placement and supporting evidence. Within the authority granted for this release, its architect adopts one configuration. The decision fixes certain interfaces, accepts a stated loss of evidence reuse and leaves product teams free to choose local implementations within those constraints. Record the governing act, scope, remaining choices and condition for reconsideration. If the architect was commissioned to recommend, return the preferred configuration and its grounds to the person authorized to commit the project. An ADR can describe either status.

The primary `EntityOfConcern` is `ArchitectureDecisionRelation@Project`: an architecture decision relation over one bounded architecture question with one exact composite project `U.Work` as a participant. It links that work, the decision subject, candidate basis or binding condition, selected architecture option, affected structures, architecture characteristics, rationale, accepted losses, consequences, method and work expectations, publication projection, evidence or eval exits, and reopen conditions.

`ArchitectureDecisionRelation@Project` is not a new `U.*` kind. `@Project` is a compatibility and retrieval cue, not the source of project identity or scope. The relation is project-local only when `projectWorkOccurrenceRef` identifies the exact composite `U.Work` that participates in it. When another slot becomes load-bearing as an FPF object, recover the subject pattern for that object.

The **system-of-interest (SoI)** is the product System that a particular extended enterprise is organized to create, change, sustain in use or retire. A.1.STM:4.1 explains how to recover that organization, the agents' objectives and agreements. The decision's described holon can be the creator organization itself. Choose its architecture in light of the capability needed for the product use, and state which local result the work must establish and how it will be accepted under A.1.STM:4.1.1. The organization remains a creator when its development has a separate budget, contract or external provider, or when the business is sold. A distinct usable machine or component supply can have its own product SoI under that pattern's receiving-use and fitness grounds. Keep every product demand and shared condition that can change this decision. The singular System reference below addresses one designation; preserve other relevant designations and relations separately rather than binding a plurality to it.

When this decision designates a **project system-of-interest**, `projectSystemOfInterestRef?` names only an independently admitted existing `U.System`. Before identity inception, keep the intended referent in `intendedProjectSystemClaimRef?` as `U.WorkPlan`, decision, system description, or other claim content. A local kind is named separately in `systemOfInterestKindRef?`, while `systemOfInterestClassificationRef?` cites an independently obtaining classification judgment; neither entails an assignment. A current assignment uses separate species and occurrence refs, and the occurrence's holder is that System. Route any source phrase such as `SystemOfInterestRole` through `E.10.ROLE` before filling these fields. A taxonomy or scheme is not assignment content. Designation, kind, classification, assignment, Work, change, use facts, and the decision remain distinct. When a compound project-selection claim is needed, use A.15.6:4.1a to construct or reuse its sufficient local semantics and test the required facts. Return `missing-substrate[project-selection-conjunction]` only when the needed operator semantics are unavailable; retain unknown or failed case facts as those distinct outcomes.

When the decision uses a transformation-flow network, `transformationFlowStructureNetworkRef?` names only an independently selected E.18.NET `TransformationFlowStructureNetwork@Context <: U.Structure`; `projectNetworkSelectionResultRef?` may cite the separate C.2.1 judgment about why that network answers the project question, and `architectureTransformationFlowStructureRelationRef?` cites C.30.TFS-REL when architecture use is current. A network record, a C.32.CONWAY frame or exact pair row, and this decision create no network member, cross-flow occurrence, architecture-influence occurrence, architecture relation, or other world-side fact.

A team writes an architecture record, diagram, shortlist, ranking, or local choice without a recoverable architecture decision relation to exact project work. Later workers cannot tell which architecture configuration is selected, which structures are affected, which method they must use, which losses were accepted, or when the decision must be reopened.

Practitioners performing the project work can turn a candidate palette into one governed decision relation that can guide work, be described in an ADR-like record, support review, and be reconsidered as the architecture evolves.

Recover the decision to be made. Compare the feasible options if their differences affect the choice. If a binding condition fixes the design, identify it and check whether the project can fulfill it. State what the project commits to, how that affects subsequent work and what could reopen the decision.

Another practitioner can recover why the project will pursue this design, the structures and commitments affected, any alternatives and losses considered, the consequences for methods and work, and the conditions for reopening it.

Not this pattern when the current work is candidate synthesis, architecture-description adequacy, ADR publication projection, adequacy evaluation, evidence, assurance, gate passage, local choice, or performed work. Use the pattern for the next question named in `Relations` for those claims.

The first useful output is a recoverable project architecture decision. The following form can describe `ArchitectureDecisionRelation@Project`; ordinary prose can carry the same required values, and optional or inapplicable branches need not be filled:

```text
ArchitectureDecisionRelation@Project:
  decisionId:
  projectWorkOccurrenceRef: U.EntityRef constrained to exact composite U.Work
  projectSystemOfInterestRef?: U.EntityRef constrained to one independently admitted existing U.System
  intendedProjectSystemClaimRef?: U.WorkPlan, decision, system-description, or other claim episteme ref before identity inception
  systemOfInterestKindRef?: U.KindRef resolving to one exact local system-role kind
  systemOfInterestClassificationRef?: U.RelationRef resolving to the exact classification judgment for projectSystemOfInterestRef under systemOfInterestKindRef
  systemOfInterestAssignmentSpeciesRef?: U.RelationKindRef constrained under U.SystemRoleAssignment
  systemOfInterestAssignmentOccurrenceRef?: U.RelationRef constrained to an obtaining occurrence of systemOfInterestAssignmentSpeciesRef, with participants, applicability, extent, and projectSystemOfInterestRef as holder recoverable
  decisionSubjectRef:
  describedHolonRef:
  decisionQuestion:
  intendedDecisionUse:
  claimScopeRef: U.ClaimScope
  decisionWindowRef:
  candidateBasisRefs?: qualification of a sufficient option or the basis for comparing alternatives
  bindingConditionRefs?: when an agreement or other binding condition settles the design
  comparisonOrSelectionRefs?
  structuralInformationLensUseRefs?
  holonTransitionOrBOSCTriggerRefs?
  architectureInfluenceCorrespondenceRef?: C.32.CONWAY frame or exact pair-row ref
  transformationFlowStructureNetworkRef?: exact independently selected E.18.NET TransformationFlowStructureNetwork@Context ref
  projectNetworkSelectionResultRef?: exact C.2.1 result episteme whose EntityOfConcern is transformationFlowStructureNetworkRef
  architectureTransformationFlowStructureRelationRef?: exact C.30.TFS-REL use/trace ref when architecture uses that network
  selectedArchitectureOptionRefs:
  selectedStructureEffects:
    - structureKindRef:
      selectedStructureRef:
      decisionEffect:
      relationFunctionClaimRef:
  bindingConstraintRefs?: conditions that remain in force for the selected design
  noLiveTradeoffReason?: when the decision involves no trade-off
  architectureCharacteristicTradeoffs?:
    - architectureCharacteristicRef:
      criteriaRowRef?
      expectedGain:
      acceptedLoss?: when the choice entails this loss
      evalResultRef?
      guardrailRef?
  rationaleRefs:
  rejectedOptionRefs?: when an option was considered and rejected
  consequenceRows:
  architectureDescriptionRefs:
  methodUseInstructions:
    - methodDescriptionRefOrPatternRef:
      expectedStructureEffect:
      intendedPerformerSystemRef?: U.EntityRef constrained to U.System
      intendedPerformerKindRef?: U.KindRef
      intendedPerformerClassificationRef?: U.RelationRef resolving to an exact classification judgment
      currentPerformerAssignmentSpeciesRef?: U.RelationKindRef constrained under U.SystemRoleAssignment
      currentPerformerAssignmentOccurrenceRef?: U.RelationRef constrained to an obtaining occurrence of currentPerformerAssignmentSpeciesRef, with participants, applicability, extent, and intendedPerformerSystemRef as holder recoverable
      intendedAssignmentRequirementRef?: plan, policy, or decision-content ref stating a prospective assignment requirement; does not assert an assignment, commitment, or permission occurrence
      actualImplementationWorkRef?: U.EntityRef constrained to U.Work
      actualImplementationWorkAttributionRef?: U.RelationRef constrained to one obtaining F.6 performedUnderAssignment relation, only when the instruction represents attribution
      responsibilityRelationRef?: U.RelationRef resolving to an independently obtaining admitted domain relation
      responsibilityMissingGovernor?: exact A.6.RCD result when responsibility is required but no predicate is admitted
      authorityRelationRef?: U.RelationRef resolving to an independently obtaining admitted domain relation
      authorityMissingGovernor?: exact A.6.RCD result when authority is required but no predicate is admitted
      permissionRelationRef?: U.RelationRef resolving to an independently obtaining admitted domain relation
      permissionMissingGovernor?: exact A.6.RCD result when permission is required but no predicate is admitted
      commitmentRelationRef?: U.RelationRef resolving to an independently obtaining admitted domain relation
      commitmentMissingGovernor?: exact A.6.RCD result when commitment is required but no predicate is admitted
      workBoundaryRef:
      readinessOrGateExitRef?
  architectDeveloperSplit:
    decisionFixedStructureRefs:
    openRefinementScopeRefs:
    sourceReturnCondition:
  publicationProjectionRef?
  evidenceOrAssuranceExitRefs?
  governanceExitRefs?
  reopenConditions:
  supersedesDecisionRefs?
  status:
```

The decision result must make its selected option, affected structures, criteria and trade-offs, scope, window, consequences and status recoverable. The relation and a description of it remain distinct; no second generic result or context record is required.

The field names in this first-output form are publication-friendly filled-reference fields. Durable relation positions must be expressible through `A.6.5` SlotSpecs: each position has a local `SlotKind`, an admitted `ValueKind`, and a by-value or concrete `RefKind` filling mode. A field name such as `decisionSubjectRef` is not a SlotKind, not a U-kind, and not an ADR heading; it is the filled-reference field by which this relation record points to the value governed by the slot-bearing relation.

When an instruction cites actual implementation Work, recover each performer through A.13 and let `actualImplementationWorkRef` name the `U.Work` occurrence independently admitted through A.15.1. Assignment species and occurrence fields remain optional neighboring claims. Add `actualImplementationWorkAttributionRef` only when the instruction or receiving use represents precise assignment-bound attribution through the same obtaining A.13 assignment; missing or failed F.6 attribution alone leaves the Work ref intact while the referenced Work's independent A.13/A.15.1 grounds hold. The decision record creates none of these facts.

