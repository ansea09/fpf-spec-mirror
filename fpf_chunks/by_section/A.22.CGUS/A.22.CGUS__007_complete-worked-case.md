---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:5"
section_title: "Complete Worked Case"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__007_complete-worked-case.md"
commit_sha: "685a0d04e8c8b8c3ac0a571d72be15daf004c72f"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:5 — Complete Worked Case"
line_start: 37527
line_end: 37621
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.29"
  - "C.30"
  - "C.32"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.23"
  - "E.24.PUB"
  - "F.17"
  - "F.18"
  - "F.9"
  - "G.11"
keywords:
---

### A.22.CGUS:5 - Complete Worked Case

Return to the design review from `4.1`. The ordinary card becomes formal only because the team now needs to retain and compare the review basis across editions.

```text
selectedCGUSRef: DesignReviewAlternatives@DR-27
A22IdentityBasis:
  selectedConstituentRefs[]:
    DesignCandidate-A
    ThermalCheckResult-A
    ServiceCheckResult-A
    RepairProposal-A
    AcceptCandidate-Continuation
    RepairCandidate-Continuation
  selectedObtainingRelationOccurrenceRefs[]:
    ThermalCheckAboutCandidate@DR-27
    ServiceCheckAboutCandidate@DR-27
    RepairProposalTargetsCandidate@DR-27
  relationOccurrenceRecoveryRows[]:
    - relationOccurrenceRef: ThermalCheckAboutCandidate@DR-27
      predicateDefinitionRef: CheckResultAboutDesignCandidatePredicate
      participantRefsInPredicateOrder[]: [ThermalCheckResult-A, DesignCandidate-A]
    - relationOccurrenceRef: ServiceCheckAboutCandidate@DR-27
      predicateDefinitionRef: CheckResultAboutDesignCandidatePredicate
      participantRefsInPredicateOrder[]: [ServiceCheckResult-A, DesignCandidate-A]
    - relationOccurrenceRef: RepairProposalTargetsCandidate@DR-27
      predicateDefinitionRef: RepairProposalTargetsDesignCandidatePredicate
      participantRefsInPredicateOrder[]: [RepairProposal-A, DesignCandidate-A]
  appliedConstraintClaimRefs[]:
    AcceptIfBothChecksSatisfied
    RepairIfAnyCheckViolatedAndProposalTargetsCandidate
  namedSelectionUseFrame:
    questionOrAction: which review continuation is available now?
    admissibleAction: show the enabled, disabled, and unknown alternatives for this review
    stopOrReturnCondition: return to an unresolved test or relation; recheck when either result, the proposal relation, or the window changes
forbiddenOverread?: displayed order as performed Work, or an available branch as authorization
constraintGovernedProfileBasis:
  locusBindingRows[]:
    - <DesignReviewAlternatives@DR-27, candidate, design under review, DesignCandidate-A>
    - <DesignReviewAlternatives@DR-27, thermal-result, thermal finding, ThermalCheckResult-A>
    - <DesignReviewAlternatives@DR-27, service-result, service finding, ServiceCheckResult-A>
    - <DesignReviewAlternatives@DR-27, repair-proposal, proposed repair, RepairProposal-A>
    - <DesignReviewAlternatives@DR-27, accept, accept continuation, AcceptCandidate-Continuation>
    - <DesignReviewAlternatives@DR-27, repair, repair continuation, RepairCandidate-Continuation>
  potentialContinuationRows[]:
    - AcceptCandidate-Continuation, constrained by AcceptIfBothChecksSatisfied
    - RepairCandidate-Continuation, constrained by RepairIfAnyCheckViolatedAndProposalTargetsCandidate
continuationJudgements[]:
  - candidate: AcceptCandidate-Continuation
    basisKind: conditionEvaluation
    predicateOrTest: AcceptIfBothChecksSatisfied
    applicability: both named results concern DesignCandidate-A
    caseInputs: [ThermalCheckResult-A, ServiceCheckResult-A]
    currentFacts: [thermal violated, service satisfied]
    requiredPolarity: both satisfied
    observedOutcome: notSatisfied
    dependentOccurrences: [ThermalCheckAboutCandidate@DR-27, ServiceCheckAboutCandidate@DR-27]
    window: ReviewWindow-DR-27
    result: disabled
    reason: thermal check is violated
  - candidate: RepairCandidate-Continuation
    basisKind: conditionEvaluation
    predicateOrTest: RepairIfAnyCheckViolatedAndProposalTargetsCandidate
    applicability: the proposal concerns DesignCandidate-A
    caseInputs: [ThermalCheckResult-A, ServiceCheckResult-A, RepairProposal-A]
    currentFacts: [thermal violated, service satisfied, RepairProposalTargetsCandidate@DR-27 obtains]
    requiredPolarity: at least one violation and the targeting relation obtains
    observedOutcome: satisfied
    dependentOccurrences: [ThermalCheckAboutCandidate@DR-27, ServiceCheckAboutCandidate@DR-27, RepairProposalTargetsCandidate@DR-27]
    window: ReviewWindow-DR-27
    result: enabled
    reason: one check is violated and the repair proposal concerns this design
currentContinuationSet: enabled [RepairCandidate-Continuation]; disabled [AcceptCandidate-Continuation]; unknown []
stopOrNextAction: show repair as available; recheck when either result, the proposal relation, or the window changes
```

The structure has two potential continuations although this case enables only repair. The relation rows state their predicates and ordered participants; the judgement rows state the tests, applicability, inputs, facts, polarity, dependent occurrences, window, outcomes, and reasons.

If `RepairProposalTargetsCandidate@DR-27` or its participant binding is missing, the repair result becomes `unknown — proposal target not established`. If the structure's identity was established on another sufficient basis, only this case result is incomplete. If that occurrence belongs to the claimed identity basis, this structure claim also remains provisional.

If a later thermal check passes while the service check still passes, acceptance becomes enabled and repair becomes disabled. If the constituents, selected occurrences, constraints, use frame, locus bindings, and potential topology have not changed, the CGUS keeps its identity and membership. A replacement result episteme or relation occurrence must first be compared under the A.22 discriminators.

#### A.22.CGUS:5.1 - A missing intermediate capability changes the continuation

In this constructed learning case, a dancer has the strength and static axis control needed by a figure and can recall its sequence. The known limitation is maintaining balance during its required rotation. The figure's continuation depends on that coordinated performance, not just on adequate strength and memory.

| Alternative | Relevant conditions in this case | Present result |
| --- | --- | --- |
| Perform the complete figure under its intended conditions. | The required balance during rotation cannot yet be sustained. | Unavailable for the intended performance; naming the figure or its steps does not remove the gap. |
| Practise the rotational coordination under a suitable reduced demand. | A domain-appropriate exercise, suitable space and the needed support are available in the stipulated case. | Available as practice of the intermediate performance. It does not establish ability to perform the full figure. |

During the rotation, balance coordination would constitute part of turning; that turn would constitute part of the figure. These are connections through current performance, not three successive tasks. The practice alternative can exercise the first connection without already performing the intended figure.

When the coordination can be sustained, return to the encompassing figure and vary the relevant conditions before drawing a broader capability conclusion. The case condition and its continuation judgement can change without changing the potential alternatives. The subject's training Method supplies the exercise and assessment; CGUS makes their effect on the available continuation explicit.

