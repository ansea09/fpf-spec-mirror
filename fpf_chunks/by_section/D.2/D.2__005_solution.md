---
chunk_kind: "child"
pattern_id: "D.2"
pattern_title: "Multilevel Ethics For Holon Work"
section_id: "D.2:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.2/D.2__005_solution.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "D.2 — Multilevel Ethics For Holon Work"
  - "D.2:2 — Solution"
line_start: 68780
line_end: 68825
dependencies:
  - "A.1"
  - "A.15"
  - "A.3.4"
  - "B.1"
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

Open a `MultilevelEthicsEntry@Context`:

```text
MultilevelEthicsEntry@Context:
  ethicalConcernRef
  affectedEntityOfConcernRef
  valueFrameEditionRefs
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  declaredLevelOrScopeRefs
  affectedHolonRefs
  affectedEpistemeRefs?
  roleWordRecoveryRefs?: E.10.ROLE results when role wording occurs
  localSystemRoleKindRefs?: FinSet(U.KindRef)
  systemRoleClassificationAssertionRefs?: FinSet(U.EpistemeRef)
  systemRoleAssignmentRows?: FinSet({
    assignmentSpeciesRef: U.RelationKindRef constrained under U.SystemRoleAssignment
    assignmentOccurrenceRef: U.RelationRef constrained to an obtaining occurrence of assignmentSpeciesRef, with actual participants, holder, applicability, and extent recoverable
  })
  participationOrAffectedPartyRelationRefs?: exact direct relation refs
  participationOrAffectedPartyMissingGovernorRefs?: exact A.6.RCD results
  responsibilityRelationRefs?: exact direct relation refs
  responsibilityMissingGovernorRefs?: exact A.6.RCD results
  commitmentRelationRefs?: exact direct relation refs
  commitmentMissingGovernorRefs?: exact A.6.RCD results
  permissionRelationRefs?: exact direct relation refs
  permissionMissingGovernorRefs?: exact A.6.RCD results
  authorityRelationRefs?: exact direct relation refs
  authorityMissingGovernorRefs?: exact A.6.RCD results
  interestOrConcernRefs
  capabilityOrFunctioningConcernRefs?
  methodRefs?
  workRefs?
  transformationRefs?
  expectedConsequenceRefs
  evidenceRefs
  uncertaintyOrCurrentnessCondition
  nextSubjectPatternLocator
```

The entry record has one job: recognize that multilevel ethics is live and choose the next pattern to apply. It does not itself resolve the conflict.

For this pattern, holon work includes material systems and epistemes when they are the affected EntityOfConcern. An architectural description, standard, model card, policy publication, or research program may be the affected episteme; the pattern still asks which levels, scopes, affected holons, interests, responsibilities, and consequences are live.

