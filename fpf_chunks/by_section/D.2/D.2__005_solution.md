---
chunk_kind: "child"
pattern_id: "D.2"
pattern_title: "Recognize Ethical Concerns Across Levels and Scopes (Multilevel Ethics)"
section_id: "D.2:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.2/D.2__005_solution.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "D.2 — Recognize Ethical Concerns Across Levels and Scopes (Multilevel Ethics)"
  - "D.2:2 — Solution"
line_start: 96174
line_end: 96223
dependencies:
  - "A.1"
  - "A.15"
  - "A.3.4"
  - "B.1"
  - "C.11.DUA"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30.ILC"
  - "D.1"
  - "D.3"
  - "D.4"
  - "D.5"
keywords:
---

### D.2:2 - Solution

Start with the proposed action or arrangement and the local gain. If an adequate account of affected parties and consequences already exists, use it. Otherwise follow the changed work, use or dependency from the proposal to the entities that may bear its effects; use `A.1.CSD` when a consequential bearer or effect path remains unclear. Keep an obtaining relation distinct from a possible consequence and retain an unresolved bearer or path as unresolved.

Name the possible loss and the levels or scopes that make it an ethical concern, then state the next question to settle. Recognition is complete when the affected sides and next use are sufficiently clear; an already qualified `D.3` conflict or `D.4` decision question can be used.

Use `MultilevelEthicsEntry@Context` when the practitioner or a recipient needs to recover these connections for comparison or revision. Keep its content in the existing answer or working note when that suffices. Add evidence, value-frame editions, and supporting relations where the stated concern relies on them:

```text
MultilevelEthicsEntry@Context:
  ethicalConcernRef
  affectedEntityOfConcernRef
  valueFrameEditionRefs?
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  declaredLevelOrScopeRefs
  affectedHolonRefs
  affectedEpistemeRefs?
  roleWordRecoveryRefs?: E.10.ROLE results when the relevant role meaning needed clarification
  localSystemRoleKindRefs?: FinSet(U.KindRef)
  systemRoleClassificationAssertionRefs?: FinSet(U.EpistemeRef)
  systemRoleAssignmentRows?: FinSet({
    assignmentSpeciesRef: U.RelationKindRef constrained under U.SystemRoleAssignment
    assignmentOccurrenceRef: U.RelationRef constrained to an obtaining occurrence of assignmentSpeciesRef, with participants, holder, applicability, and extent recoverable
  })
  participationOrAffectedPartyRelationRefs?: direct relation refs
  participationOrAffectedPartyMissingGovernorRefs?: A.6.RCD results
  responsibilityRelationRefs?: direct relation refs
  responsibilityMissingGovernorRefs?: A.6.RCD results
  commitmentRelationRefs?: direct relation refs
  commitmentMissingGovernorRefs?: A.6.RCD results
  permissionRelationRefs?: direct relation refs
  permissionMissingGovernorRefs?: A.6.RCD results
  authorityRelationRefs?: direct relation refs
  authorityMissingGovernorRefs?: A.6.RCD results
  interestOrConcernRefs
  capabilityOrFunctioningConcernRefs?
  methodRefs?
  workRefs?
  transformationRefs?
  expectedConsequenceRefs
  evidenceRefs?
  uncertaintyOrCurrentnessCondition?
  nextSubjectPatternLocator
```

The entry has one job: make the multilevel concern recognizable and choose its next use. It does not require a separate dossier or new inquiry before the concern can be discussed. A proposed inquiry goes through `C.11.DUA` when its receiving contribution or feasibility is unresolved; conflict description and decision use remain with `D.3` and `D.4`.

Material systems and epistemes can be affected EntitiesOfConcern. For an episteme such as a standard, state which uses and interests make its change ethically relevant.

