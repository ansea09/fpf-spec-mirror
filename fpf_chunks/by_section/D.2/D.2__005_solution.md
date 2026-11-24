---
chunk_kind: "child"
pattern_id: "D.2"
pattern_title: "Recognize Ethical Concerns Across Levels and Scopes (Multilevel Ethics)"
section_id: "D.2:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.2/D.2__005_solution.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "D.2 — Recognize Ethical Concerns Across Levels and Scopes (Multilevel Ethics)"
  - "D.2:2 — Solution"
line_start: 97080
line_end: 97130
dependencies:
  - "A.1"
  - "A.15"
  - "A.3.4"
  - "B.1"
  - "C.11.DUA"
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

Start with the proposed action or arrangement and the gain it promises. Use an existing account if it identifies the affected parties and explains the consequences that matter here. Otherwise trace the changes in work, use or dependency to the entities that may experience their effects. Say which connections already exist, which the proposal would create, and which effects are observed or predicted. If you cannot tell who might experience an effect or how it would reach them, use `A.1.CSD` to investigate and state what remains unknown.

Connect each material consequence to the party or entity affected, the value premise that makes it matter and the conditions under which the change could produce it. If the claim concerns a whole, establish how the effects on its constituents bear on the property in question. A saving for one office may be extra work for another. If the claim concerns other settings, establish which conditions of that explanation hold there. State the next question. Use D.3 when the sides and their tension need describing. When an adequate account of the conflict already exists, it can go directly into the D.4 comparison.

Use `MultilevelEthicsEntry@Context` when the practitioner or a recipient needs to recover these connections for comparison or revision. Keep its content in the existing answer or working note when that suffices. If an existing note says only “level or scope”, recover which relation, affected population or applicability condition the note identified. Retain a reference to a `U.WorkScope` with the capability it qualifies, or to a `U.PublicationScope` with the publication view or form it qualifies. If the meaning of the old label is still unclear, keep the original wording and identify that uncertainty. Add the evidence, value-frame editions and supporting relations on which the stated concern relies.

```text
MultilevelEthicsEntry@Context:
  ethicalConcernRef
  affectedEntityOfConcernRef
  valueFrameEditionRefs?
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  compositionRelationRefs?  // identified whole and constituent, when their relation matters
  affectedPopulationOrAreaRefs?  // who is included or where exposure occurs
  affectedHolonRefs?
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

