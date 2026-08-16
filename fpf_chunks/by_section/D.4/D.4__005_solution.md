---
chunk_kind: "child"
pattern_id: "D.4"
pattern_title: "Ethical Mediation and Decision Use"
section_id: "D.4:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.4/D.4__005_solution.md"
commit_sha: "3d098629dc218572089f1890080c17d6f1d9a867"
heading_path:
  - "D.4 — Ethical Mediation and Decision Use"
  - "D.4:2 — Solution"
line_start: 68818
line_end: 68873
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "B.3"
  - "C.11"
  - "C.28"
  - "C.29"
  - "C.30.ILC"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.5"
keywords:
---

### D.4:2 - Solution

Record an `EthicalMediationDecisionUse@Context`:

```text
EthicalMediationDecisionUse@Context:
  conflictStructureRef
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
  systemRoleClassificationJudgmentRefs?: exact direct classification refs
  intendedWorkPlanOrCommitmentRefs?: prospective plan or commitment content
  intendedAssignmentRequirementRefs?: prospective requirement content; creates no assignment occurrence
  performedWorkRows?:
    - performerSystemRef: exact U.System
      workOccurrenceRef: exact dated U.Work
      assignmentSpeciesRef: exact directly declared species under U.SystemRoleAssignment
      assignmentOccurrenceRef: obtaining occurrence of assignmentSpeciesRef with actual participant values, applicability, and extent covering the Work
      f6AttributionRef: exact performedUnderAssignment occurrence
      holderEquality: performerSystemRef = assignmentOccurrenceRef.HolderSystemSlot
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
  inadmissibleOverread
  strongerSourceReturnCondition
```

The record names the current ethical use of the conflict: mediate, refuse, continue under explicit residual, demand evidence, ask a causal question, ask for assurance, return to architecture, or make a bounded decision.

Name the affected EntityOfConcern and any affected Systems, the value-frame editions, the decision question and options, and the intended decision or Work use. Add ClaimScope and a qualification window when they delimit that use. State the proposed mediation or refusal and any accepted residuals. If evidence, causal adequacy, assurance, architecture residuals, responsibility, permission, or actual Work remains unresolved, return only that question to the pattern that defines it. These values delimit the mediation; a generic context field does not.

