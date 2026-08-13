---
chunk_kind: "child"
pattern_id: "D.3"
pattern_title: "Interlevel Ethical Conflict Structure"
section_id: "D.3:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.3/D.3__005_solution.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "D.3 — Interlevel Ethical Conflict Structure"
  - "D.3:2 — Solution"
line_start: 69172
line_end: 69214
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "B.1"
  - "B.3"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "C.30.ILC"
  - "D.1"
  - "D.2"
  - "D.4"
  - "D.5"
  - "E.10.ROLE"
  - "E.17"
keywords:
---

### D.3:2 - Solution

Record an `InterlevelEthicalConflictStructure@Context`:

```text
InterlevelEthicalConflictStructure@Context:
  conflictConcernRef
  boundedContextRef
  affectedEntityOfConcernRefs
  declaredLevelOrScopeRefs
  affectedHolonRefs
  affectedEpistemeRefs?
  collectionOrMembershipRelationRefs?
  partWholeRelationRefs?
  roleWordRecoveryRefs?: E.10.ROLE results when role wording occurs
  localSystemRoleKindRefs?: FinSet(U.KindRef)
  systemRoleClassificationJudgmentRefs?: FinSet(U.RelationRef)
  systemRoleAssignmentRows?: FinSet({
    assignmentSpeciesRef: U.RelationKindRef constrained under U.SystemRoleAssignment
    assignmentOccurrenceRef: U.RelationRef constrained to an obtaining occurrence of assignmentSpeciesRef, with actual participants, holder, applicability, and extent recoverable
  })
  interestOrConcernRefs
  valueFrameRefs
  agencyCharacteristicOrThresholdRefs?
  responsibilityRelationRefs?: exact direct responsibility predicates with participants and occurrence identity
  responsibilityMissingGovernorRefs?: exact A.6.RCD results
  otherEthicalRelationRows?: FinSet({
    relationFamilyRef: exact admitted direct-relation family other than responsibility
    relationRef?: exact obtaining occurrence of that family
    missingGovernorRef?: exact A.6.RCD result for that family
  })
  methodOrWorkRefs?
  transformationRefs?
  evidenceRefs
  uncertaintyRefs
  consequenceHorizonRefs
  conflictRelationRefs
  nonConflictOverread
  nextUseSubjectPatternLocator
```

This structure may be represented by a table, graph, formal predicate, narrative case, or another selected description form. The representation is not the conflict itself. If a mathematical lens does work in the claim, cite `C.29`; if the publication form changes admissible use, cite `E.17`.

