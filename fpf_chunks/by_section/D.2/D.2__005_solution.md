---
chunk_kind: "child"
pattern_id: "D.2"
pattern_title: "Multilevel Ethics For Holon Work"
section_id: "D.2:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.2/D.2__005_solution.md"
commit_sha: "f4bad21274b54b57071afb2210a8bdb9f61a1c95"
heading_path:
  - "D.2 — Multilevel Ethics For Holon Work"
  - "D.2:2 — Solution"
line_start: 69337
line_end: 69384
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

Name the local gain, who or what may bear a loss, and the levels or scopes that make this an ethical concern. State the next question to settle. Recognition is complete when those sides and the next use are clear; an already qualified `D.3` conflict or `D.4` decision question can be used directly.

Use `MultilevelEthicsEntry@Context` when the practitioner or a recipient needs to recover these connections for comparison or revision. Keep its content in the existing answer or working note when that suffices. Add evidence, value-frame editions, and supporting relations where the stated concern actually relies on them:

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
  evidenceRefs?
  uncertaintyOrCurrentnessCondition?
  nextSubjectPatternLocator
```

The entry has one job: make the multilevel concern recognizable and choose its next use. It does not require a separate dossier or new inquiry before the concern can be discussed. A proposed inquiry goes through `C.11.DUA` when its receiving contribution or feasibility is unresolved; conflict description and decision use remain with `D.3` and `D.4`.

For this pattern, holon work includes material systems and epistemes when they are the affected EntityOfConcern. An architectural description, standard, model card, policy publication, or research program may be the affected episteme; the pattern still asks which levels, scopes, affected holons, interests, responsibilities, and consequences are live.

