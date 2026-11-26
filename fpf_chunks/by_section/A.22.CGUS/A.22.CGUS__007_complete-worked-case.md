---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Which Continuations Are Available? — Constraint-Governed Unfolding Structure (CGUS)"
section_id: "A.22.CGUS:5"
section_title: "Complete Worked Case"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__007_complete-worked-case.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "A.22.CGUS — Which Continuations Are Available? — Constraint-Governed Unfolding Structure (CGUS)"
  - "A.22.CGUS:5 — Complete Worked Case"
line_start: 42565
line_end: 42654
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

Return to the design review from `4.1`. The team now needs to determine whether reviews across editions use the same qualified unfolding structure or a different one. Recover the formal basis below for that comparison.

```text
selectedCGUSRef: DesignReviewAlternatives@DR-27
A22IdentityBasis:
  selectedConstituentRefs[]:
    DesignCandidate-A
    RepairProposal-A
    AcceptCandidate-Continuation
    RepairCandidate-Continuation
  selectedObtainingRelationOccurrenceRefs[]:
    RepairProposalTargetsCandidate@DR-27
  relationOccurrenceRecoveryRows[]:
    - relationOccurrenceRef: RepairProposalTargetsCandidate@DR-27
      predicateDefinitionRef: RepairProposalTargetsDesignCandidatePredicate
      participantRefsInPredicateOrder[]: [RepairProposal-A, DesignCandidate-A]
  appliedConstraintClaimRefs[]:
    AcceptIfBothChecksSatisfied
    RepairIfAnyCheckViolatedAndProposalTargetsCandidate
  namedSelectionUseFrame:
    questionOrAction: which review continuations satisfy the two-check rule for DesignCandidate-A?
    admissibleAction: show enabled, disabled, unknown or error results for the current case
    stopOrReturnCondition: recheck a case when its result inputs or window change; reidentify the structure when its selected basis changes
forbiddenOverread?: displayed order as performed Work, or an available branch as authorization
constraintGovernedProfileBasis:
  locusBindingRows[]:
    - <DesignReviewAlternatives@DR-27, candidate, design under review, DesignCandidate-A>
    - <DesignReviewAlternatives@DR-27, repair-proposal, proposed repair, RepairProposal-A>
    - <DesignReviewAlternatives@DR-27, accept, accept continuation, AcceptCandidate-Continuation>
    - <DesignReviewAlternatives@DR-27, repair, repair continuation, RepairCandidate-Continuation>
  potentialContinuationRows[]:
    - AcceptCandidate-Continuation, constrained by AcceptIfBothChecksSatisfied
    - RepairCandidate-Continuation, constrained by RepairIfAnyCheckViolatedAndProposalTargetsCandidate
caseBasis:
  checkResultRefs: [ThermalCheckResult-A, ServiceCheckResult-A]
  resultAboutCandidateOccurrences:
    - <ThermalCheckAboutCandidate@DR-27, CheckResultAboutDesignCandidatePredicate, [ThermalCheckResult-A, DesignCandidate-A]>
    - <ServiceCheckAboutCandidate@DR-27, CheckResultAboutDesignCandidatePredicate, [ServiceCheckResult-A, DesignCandidate-A]>
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
currentContinuationSet: enabled [RepairCandidate-Continuation]; disabled [AcceptCandidate-Continuation]; unknown []; error []
stopOrNextAction: show repair as available; recheck when the case results or window change
```

The structure has two potential continuations although this case enables only repair. The selected proposal-to-design relation belongs to its identity basis. Thermal and service result epistemes, and their about-candidate relations, belong to the current case basis; they are not constituents or selected relation occurrences of this structure.

If the proposal-to-design relation cannot be established, this formal structure claim remains provisional. The ordinary explanation can still report repair as unknown. Do not treat an unknown identity-bearing relation as an established constituent of a qualified CGUS.

A later passing thermal check is a different result episteme and supplies a new case input. With service still satisfied, acceptance becomes enabled and repair becomes disabled. The selected design, proposal, continuation candidates, proposal-to-design relation, constraints, use frame, loci and potential topology are unchanged, so the same CGUS remains available for that new case.

Now hold the original facts fixed and change the review rule. In the second edition acceptance still requires both checks to pass. Under its remit the repair branch can take a targeted proposal only when the service check is violated. In DR-27 the thermal check failed and the service check passed. The first edition therefore makes repair available. The second makes neither acceptance nor repair available for this case. The applied repair constraint has changed. The second structure binds its four loci to the same design, proposal, acceptance continuation and repair continuation respectively. It keeps the proposal-to-design relation and the selection use. Its potential repair continuation now takes the service-violation constraint. The unavailable repair in this case remains a potential branch for a case with a service violation and a targeted proposal. A new printed edition that merely rephrased the original rule while preserving the selected constituents, relations, applied constraints, use frame, bindings and potential branches could still describe the same structure.

#### A.22.CGUS:5.1 - A missing intermediate capability changes the continuation

In this constructed learning case, a dancer has the strength and static axis control needed by a figure and can recall its sequence. The known limitation is maintaining balance during its required rotation. The figure's continuation depends on that coordinated performance, not just on adequate strength and memory.

| Alternative | Relevant conditions in this case | Present result |
| --- | --- | --- |
| Perform the complete figure under its intended conditions. | The required balance during rotation cannot yet be sustained. | Unavailable for the intended performance; naming the figure or its steps does not remove the gap. |
| Practise the rotational coordination under a suitable reduced demand. | A domain-appropriate exercise, suitable space and the needed support are available in the stipulated case. | Available as practice of the intermediate performance. It does not establish ability to perform the full figure. |

During the rotation, balance coordination would constitute part of turning; that turn would constitute part of the figure. These are connections through performance, not three successive tasks. The practice alternative can exercise the first connection without already performing the intended figure.

When the coordination can be sustained, return to what the dancer is asked to perform. If the required turn and the other constituents can be performed together under the conditions of that figure, the capability claim can extend to it. If a partner steadies the turn, establish which balance the dancer maintained and what the partner supplied. That performance can demonstrate the supported figure. For an unaided figure, use grounds for that dancer sustaining the required balance without the partner’s support. Use adequate prior performances, a domain rule or a suitable trial when a wider capability is at issue. The case condition and its continuation judgement can change without changing the potential alternatives. The subject's training Method supplies the exercise and assessment; CGUS makes their effect on the available continuation explicit.

