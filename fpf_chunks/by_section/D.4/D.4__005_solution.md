---
chunk_kind: "child"
pattern_id: "D.4"
pattern_title: "Ethical Mediation and Decision Use"
section_id: "D.4:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.4/D.4__005_solution.md"
commit_sha: "21296c8aaf3611b63ee6a2bb11e439e828ffb9a3"
heading_path:
  - "D.4 — Ethical Mediation and Decision Use"
  - "D.4:2 — Solution"
line_start: 77436
line_end: 77505
dependencies:
  - "A.1.CSD"
  - "A.10"
  - "A.20"
  - "A.21"
  - "B.3"
  - "B.5.QD.CF"
  - "C.11"
  - "C.11.DUA"
  - "C.28"
  - "C.29"
  - "C.30.ILC"
  - "C.39"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.5"
keywords:
---

### D.4:2 - Solution

Recover the conflict, develop feasible alternatives, compare their consequences and constraints under the stated value premises, and give a warranted recommendation or decision. Keep the concerns that remain unresolved visible in that result. A short answer can complete this work.

#### D.4:2.1 - Develop and compare a continuation

1. **Recover the decision and the affected concerns.** Use the D.3 account to identify who or what may gain or lose, over which horizon, and why those consequences matter. Check whether the proposed chooser can make the decision in question. Paying for a project, being represented in a survey, being affected by its result and having authority to decide are different relations. Return a consequential missing party to A.1.CSD; return an unresolved value premise to D.1.
2. **Separate the end from the proposed means.** A valued result can be pursued through means that create another objection. Ask which feature, condition or operation produces that objection and what could supply the valued result without it. B.5.QD.CF develops that question when an assumed necessary means creates the conflict; C.39 supplies construction of another way. Consider continuing the present work, narrowing the change, changing its conditions or refusing it when those are feasible alternatives. A proposed alternative remains a proposal until its required contributions are available.
3. **Compare the same alternatives under the live value premises.** Preserve each side's affected participants, consequences, constraints and uncertainty. An encompassing system's gain does not by itself establish priority over a constituent's loss. Where different value frames give different orderings, keep those orderings distinct. An alternative that is no worse under every retained ordering and better under at least one can remove a need to trade those values for this choice. This conclusion is limited to the alternatives, premises and affected concerns actually compared. If a trade-off remains, state the priority, compromise or other reason proposed for making it. Authority to choose does not make that reason correct or establish others' agreement.
4. **Resolve only the uncertainty that changes this use.** Separate disagreement about consequences from disagreement about which consequences or duties should govern. A causal inquiry can improve the former; it does not by itself settle the latter. Use available support and qualified uncertainty. Where an intended use requires a stronger claim, C.28 or the corresponding subject method supplies its basis; C.11.DUA compares an attainable inquiry with a narrower recommendation, a different option or a stop. Include delay, burden shifted to other parties and displaced work. Preserve a binding requirement's current force while examining its merits or a feasible revision.
5. **Return the supported recommendation or decision.** If the comparison basis and available options are settled, C.11 supplies the local choice. If the value conflict remains unresolved, give the conditional alternatives, the missing agreement or authority, or an explicit refusal or impasse. Do not manufacture a common scalar to force a winner. State a residual consequence and a reconsideration condition when they matter to this use. A recommendation does not establish consent, permission or performed work.

Use the same reasoning when the option is advice, publication, a technical change or a change to a method. Identify how its possible use can affect other participants; describing one's contribution as analysis leaves that question open. The relevant causal and responsibility relations still need their own basis.

#### D.4:2.2 - Retain the decision basis when the work needs it

Use an `EthicalMediationDecisionUse` account when another participant needs to inspect, compare, authorize or later revise the result. The necessary content can remain in the existing answer or decision record. The following form groups that content; use only the optional detail needed for this decision:

```text
EthicalMediationDecisionUse:
  conflictDescriptionRef: exact C.2.1 U.Episteme identified through D.3
  affectedEntityOfConcernRef
  affectedSystemRefs?
  valueFrameEditionRefs
  decisionQuestionRef?
  intendedDecisionUse?
  intendedWorkUse?
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  optionRefs
  proposedMediationRefs?
  refusalOrStopCondition?
  evidenceDemandRefs?
  causalReturnRefs?
  assuranceReturnRefs?
  architectureResidualReturnRefs?
  acceptedResidualRefs?
  decisionRecordRefs?
  decisionOrRepairSystemRefs?: independently admitted U.System refs
  localSystemRoleKindRefs?: exact local U.Kind refs
  systemRoleClassificationAssertionRefs?: FinSet(U.EpistemeRef)
  intendedWorkPlanOrCommitmentRefs?: prospective plan or commitment content
  intendedAssignmentRequirementRefs?: prospective requirement content; creates no assignment occurrence
  performedWorkRows?:
    - performerSystemRef: exact U.System
      workOccurrenceRef: exact dated U.Work
      assignmentSpeciesRef?: exact directly declared species under U.SystemRoleAssignment, when assignment-bound attribution is claimed
      assignmentOccurrenceRef?: obtaining occurrence of that species with actual participant values, applicability, and extent covering the Work
      f6AttributionRef?: exact performedUnderAssignment occurrence, for that attribution
      holderEquality?: performerSystemRef = assignmentOccurrenceRef.HolderSystemSlot, for that attribution
      methodRef:
      workExtentRef:
      containingSystemRef:
  responsibilityRelationRefs?: exact direct predicate, participants, applicability, and occurrence identity
  responsibilityMissingGovernorRefs?: exact A.6.RCD results
  authorityRelationRefs?: exact direct relation refs
  authorityMissingGovernorRefs?: exact A.6.RCD results
  permissionRelationRefs?: exact direct relation refs
  permissionMissingGovernorRefs?: exact A.6.RCD results
  commitmentRelationRefs?: exact direct relation refs
  commitmentMissingGovernorRefs?: exact A.6.RCD results
  admissibleUse
  inadmissibleOverread?
  strongerSourceReturnCondition?
```

The record names the current ethical use of the conflict: mediate, refuse, continue under explicit residual, demand evidence, ask a causal question, ask for assurance, return to architecture, or make a bounded decision.

Name the affected EntityOfConcern and any affected Systems, the value-frame editions, the decision question and options, and the intended decision or Work use. Add ClaimScope and a qualification window when they delimit that use. State the proposed mediation or refusal and any accepted residuals. If evidence, causal adequacy, assurance, architecture residuals, responsibility, permission, or actual Work remains unresolved, return only that question to the pattern that defines it. These values delimit the mediation; a generic context field does not.

