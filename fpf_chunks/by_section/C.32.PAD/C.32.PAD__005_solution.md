---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__005_solution.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:4 — Solution"
line_start: 66691
line_end: 66784
dependencies:
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

### C.32.PAD:4 - Solution

Create `ArchitectureDecisionRelation@Project` before writing an ADR-like publication record. Treat it as the architecture decision relation that includes the exact composite project `U.Work` and binds it to the candidate basis, selected architecture option, affected structures, architecture-characteristic trade-offs, rationale, consequences, method expectations, work split, and reopen conditions.

Work in this order:

1. Name the exact composite project `U.Work` participant and the decision subject: described holon, bounded context, decision question, and status. If the decision designates a project system-of-interest, cite the exact existing `U.System` or the pre-inception intended-system claim, keep every Work/change/use fact separately governed, and cite a `SystemOfInterestRole` assignment only with its named A.2 role/taxonomy interpretation and separately obtaining A.2.1 assignment. A decision designation proves no compound project-selection truth; return `missing-substrate[project-selection-conjunction]` when that stronger truth is required.
2. Cite the candidate basis. Use `C.32` for the candidate palette, `C.32.MLAO` for residual-reducing multilevel candidate frames, `C.32.CONWAY` when an influence-source architecture and transformed-side architecture content shaped the candidate, and `C.32.FAIL` for repaired candidate errors. Cite a C.32.CONWAY synthesis frame while either side is modal or the direct influence relation is unresolved; cite an exact pair row only for its already obtaining direct occurrence and two obtaining C.30 architecture-relation participants.
3. Cite comparison or selection input only when it exists. Explicit comparison belongs to `A.19.CPM`; set-returning selection belongs to `A.19.SelectorMechanism`; selected-set publication belongs to `G.5`; local choice belongs to `C.11`.
4. State the selected architecture option or bounded exception. Name the affected selected structures and the governing pattern for each structure claim.
5. Record the architecture-characteristic trade-off. Use criteria rows from `C.32.ACS`, eval results from `C.32.ACE`, measurement support from `C.16`, Q-Bundles from `C.25`, modularity or scale support from `C.31`, and `C.29` structural-information lens uses for compressed recoverable structure, accepted description loss, hidden dependency, and source-return. None of those lenses, measures, or bundles decides the architecture by itself.
6. Record rationale, rejected options, accepted losses, and consequences. A rejected option can remain useful as a stepping stone or archive item; do not turn it into a failure unless the receiving failure pattern is triggered.
7. Bind the decision to architecture descriptions. Use `C.30.AD` for architecture-description adequacy and `C.30.ASV` for selected-structure view adequacy. A diagram, model, file, or view can describe the decision basis; it does not become the decision relation.
8. Bind the decision to method-use instructions when the architect needs developers to use a method, pattern, style, toolchain step, or work practice so the described or transformed-side holon is intended to gain or preserve the named structure. Use `A.15`, `A.15.1`, `A.15.2`, `A.15.5`, `A.6.M`, `E.8`, `E.11.PUR`, and `C.24` according to the live claim.
9. State the architect-developer split. Name architect-owned selected structures, developer-owned refinement objects, source-return conditions, readiness exits, and governance exits. When the split depends on holon level, changed whole, or BOSC-triggered boundary pressure, fill `holonTransitionOrBOSCTriggerRefs?` through `B.2.P` claim-kind recovery or `B.2` whole reidentification instead of leaving a generic level note.
10. Choose a publication projection only after the decision relation is clear. Use `C.32.ADR` for ADR-like publication projection; use `E.17` and `E.24.PUB` for publication-face and publication-use claims.
11. Add evidence, assurance, gate, and governance exits only when those claims are being made. Use `A.10`, `B.3`, `A.21`, and the local governance pattern rather than adding those statuses to the decision relation by name.
12. Write reopen and supersession conditions. Reopen when the candidate basis changes, a protected architecture characteristic crosses its guardrail, an independently typed influence-source structure or arrangement no longer fits the transformed-side actual or modal architecture content, a stronger source changes the accepted loss, or the decision's method-use instruction proves unusable.

If one project question uses an E.18.NET network, first preserve that network's independent A.22/E.18.NET selection. A persistent project-network judgment stays in its C.2.1 result episteme under A.15.6, and architecture use docks through C.30.TFS-REL. A C.32.CONWAY exact pair row may be cited in `architectureCorrespondenceRowRefs[]` of a network record, but that citation is only a qualified reading: it adds no network member or cross-flow occurrence, and PAD repeats none of the network's member, relation, constraint, endpoint, or use-frame fields.

#### C.32.PAD:4.1 - Decision readiness

A C.32.PAD decision is ready to draft when the current decision relation identifies the exact composite project `U.Work` participant and can cite at least one candidate basis, one affected selected structure, one architecture-characteristic trade-off or declared reason for no live trade-off, one expected work consequence, one reopen condition, and any triggered `holonTransitionOrBOSCTriggerRefs?` or `structuralInformationLensUseRefs?` needed to preserve source return. When system-of-interest, role-assignment, architecture-influence, or network fields are present, their exact A.15.6, A.2/A.2.1, C.32.CONWAY, E.18.NET, and C.30.TFS-REL preconditions must already be satisfied or the reference remains absent.

If the candidate basis is absent, return to `C.32`. If architecture-characteristic rows are absent, return to `C.32.ACS` or `C.25`. If the decision only says "the metric is best", return to `C.32.ACE`, `C.16`, or `A.19.CPM` before deciding. If the intended work method is not recoverable, return to `A.15`. If an existing system, role assignment, project-network judgment, network selection, architecture use, or influence pair is unresolved, return to its direct owner and keep only the truthful designation, modal claim, candidate frame, or explicit stop in PAD.

#### C.32.PAD:4.2 - Constructive architecture decision path

Some architecture decisions are constructive: they prescribe methods that developer roles or other exact assigned systems are expected to use so that later Work aims to produce or preserve intended structures. Admit that path only when the decision names:

- the obtaining architecture relation and selected structure, or the exact modal `ArchitectureClaim`, to be produced or preserved;
- the method description, architectural style, pattern use, or work practice to be used;
- the exact responsible role and, when assignment identity matters, its separately obtaining `U.RoleAssignment`; never substitute an influence-source architecture, toolchain structure, or other non-agentive structure for the performer;
- the expected structure effect on the described or transformed-side holon, kept modal until its direct C.30 architecture predicate obtains;
- the work-planning boundary and readiness or gate exit;
- the source-return condition and reopen trigger.

This keeps architecture decisions connected to work without treating the decision description, ADR file, method description, selected network, influence-source structure, or performed Work as the architecture, performer, or proof that the expected structure effect obtains.

#### C.32.PAD:4.3 - Minimum sufficient relation and slot-change impact

A small complete PAD instance can be this short:

```text
ArchitectureDecisionRelation@OrderFlow:
  decisionId: OrderFlowArchitectureDecision-2026Q3
  projectWorkOccurrenceRef: ProductFamilyQ3OrderArchitectureWork, exact admitted composite U.Work
  decisionSubjectRef: order-integration architecture for product-family Q3
  describedHolonRef: product-family order-flow system
  candidateBasisRefs: [C32CandidatePalette:order-flow-2026-06]
  selectedArchitectureOptionRefs: [event-carried integration with payment exception]
  selectedStructureEffects:
    - structureKindRef: module structure
      selectedStructureRef: order events between service modules
      decisionEffect: preserve service substitutability, accept added event-schema governance
      governingPatternRef: C.30.ASV
  architectureCharacteristicTradeoffs:
    - architectureCharacteristicRef: substitutability
      expectedGain: service replacement without order-flow rewrite
      acceptedLoss: additional schema-version coordination
      guardrailRef: version-skew eval band
  methodUseInstructions:
    - methodDescriptionRefOrPatternRef: event-schema change method
      expectedStructureEffect: compatible event contracts across service modules
      responsibleRoleRef: service-team developer role
      workBoundaryRef: team-owned schema refinement after architect-owned event boundary
  architectDeveloperSplit:
    architectOwnedStructureRefs: [event boundary, payment exception]
    developerOwnedRefinementRefs: [schema fields inside approved event boundary]
    sourceReturnCondition: return to PAD when refinement changes event boundary or version-skew band
  holonTransitionOrBOSCTriggerRefs?: [B.2.P: no new operational whole claimed for team-local schema refinement]
  structuralInformationLensUseRefs?: [C.29: event-flow view compresses deployment and rollout structure; source-return keeps model refs recoverable]
  publicationProjectionRef?: C.32.ADR:order-flow-adr
  reopenConditions: [payment latency guardrail crossed, schema-version coordination cost guardrail crossed]
  status: acceptedForDeveloperWork
```

When a filled field changes, repair the smallest owner that governs the changed content:

| Changed filled field | Immediate repair locus |
|---|---|
| `candidateBasisRefs` or `selectedArchitectureOptionRefs` | Return to `C.32`, `C.32.MLAO`, comparison or selection inputs, then update PAD before ADR projection. |
| `projectSystemOfInterestRef?`, `intendedProjectSystemClaimRef?`, or `systemOfInterestRoleAssignmentRef?` | Return to A.15.6 for actual-versus-intended designation and the compound-selection stop, and to A.2/A.2.1 for the named role/taxonomy interpretation and obtaining assignment. Keep every independently obtaining Work/change/use fact; remove any reference the decision alone was being used to prove. |
| `architectureInfluenceCorrespondenceRef?` | Return to C.32.CONWAY. Keep a frame for modal or unresolved sides and cite an exact pair row only for the already obtaining direct occurrence and its exact C.30 architecture-relation participants. |
| `transformationFlowStructureNetworkRef?`, `projectNetworkSelectionResultRef?`, or `architectureTransformationFlowStructureRelationRef?` | Return to E.18.NET for exact network identity, A.15.6/C.2.1 for the project-question judgment, and C.30.TFS-REL for architecture use. Update or remove only the affected refs; do not copy or repair network members, relations, constraints, endpoints, or use frame inside PAD. |
| `selectedStructureEffects` | Repair the architecture claim or selected-structure view in `C.30`, `C.30.AD`, or `C.30.ASV`; then update PAD consequences. |
| `architectureCharacteristicTradeoffs` | Repair `C.32.ACS`, `C.32.ACE`, `C.25`, `C.16`, or comparison input before relying on the decision. |
| `methodUseInstructions` or `architectDeveloperSplit` | Repair method, work, role, readiness, and work-boundary claims through `A.15` family, `E.8`, `E.11.PUR`, or `C.24`. |
| `holonTransitionOrBOSCTriggerRefs?` | Use `B.2.P` for wording and claim-kind recovery; use `B.2` only when the decision depends on whole reidentification. |
| `structuralInformationLensUseRefs?` | Use `C.29` to state which structure is preserved, compressed, hidden, or recoverable; return to source when the accepted loss changes. |
| `publicationProjectionRef?` | Repair only the publication projection through `C.32.ADR`, `E.17`, or `E.24.PUB`; do not rewrite the decision by template pressure. |
| `reopenConditions` or `supersedesDecisionRefs?` | Update PAD and the active ADR-like projection; old decisions remain historical unless a governed archival policy says otherwise. |

