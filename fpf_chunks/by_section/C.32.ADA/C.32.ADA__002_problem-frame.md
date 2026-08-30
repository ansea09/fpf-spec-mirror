---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__002_problem-frame.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:1 — Problem frame"
line_start: 66330
line_end: 66402
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.13"
  - "E.17"
  - "E.21"
  - "E.22"
  - "E.24.PUB"
keywords:
  - "ArchitectureDecisionAdequacyEvaluation@Project"
  - "E.21 labels"
  - "architecture decision adequacy"
  - "complete coordinate set"
  - "declared use"
  - "method docking"
  - "no average"
  - "publication projection"
  - "repair target"
---

### C.32.ADA:1 - Problem frame

Use this pattern when a project architecture decision, its method docking, or its ADR-like publication projection must be evaluated for adequacy before use, review, handoff, governance, or improvement.

Primary working reader: an architect, reviewer, or architecture-responsible practitioner checking whether a project architecture decision is good enough for a declared use and which repair should happen next.

Typical entry phrases:

```text
"The decision is written, but can developers actually use it?"
"The ADR looks complete; is the architecture decision itself adequate?"
"Which part is weak: candidate basis, trade-off, method instruction, work split, or publication projection?"
"We need a scale like E.21, but for architecture decisions rather than pattern quality."
"Do not average the decision; tell us what must be repaired."
```

**First-minute use slice.** `ArchitectureReviewService-4` first has the A.13 core for decision-adequacy evaluation, and A.15.1 independently admits `DecisionAdequacyEvaluationWork-12` from 10:00 to 10:20 on 2026-08-12. The Work enacts `DecisionAdequacyEvaluationMethod-2` and occurs within `ProjectArchitectureReviewService-4`. This slice expressly represents evaluator accountability: `ArchitectureReviewerAssignment-6` is an obtaining occurrence of directly declared species `ArchitectureReviewerAssignment`, held by the already recovered performer and covering the Work, and the separate F.6 relation is recorded. A Work-only ADA record would omit those assignment and attribution refs; failed F.6 would leave the evaluation Work intact. One separate result episteme states the declared use and coordinate outcomes. It does not approve the decision; it directs the exact bounded repairs needed before the decision can guide developer Work.

The primary governed object is `ArchitectureDecisionAdequacyEvaluation@Project`: a C.32.ADA-local evaluation record over one `ArchitectureDecisionRelation@Project`, optional `ArchitectureDecisionRecordProjection@Project`, and declared use. It is not the evaluated decision, evaluation Work, or result episteme.

`ArchitectureDecisionAdequacyEvaluation@Project` is a local record form, not a new `U.*` kind, gate, evidence, assurance, pattern-quality evaluation, or replacement for `C.32.PAD`. Its coordinate table expresses the ADA result content; when that result must be a durable claim, one separately identified C.2.1 episteme states it. The dated evaluation remains separate `U.Work`, and any actual evaluation operation application remains with its subject pattern.

What goes wrong if C.32.ADA is missed: a decision can appear complete because it has a record, rationale, or diagram, while it is unusable for the declared work. Weak candidate basis, hidden trade-offs, missing method instructions, absent source-return, and vague supersession conditions remain invisible until implementation or review fails.

What C.32.ADA buys in practice: the project can evaluate architecture decisions by complete coordinate set, keep kinds distinct, and repair the weakest live coordinates without turning adequacy into a single score.

Ordinary working move: declare the evaluation use, evaluate every coordinate with an ordinal value and rationale, then state the repair condition for each weak coordinate and cite the smallest subject-pattern locus containing the required definition or constraint.

Adoption test: after using C.32.ADA, another practitioner can see the declared use, complete coordinate values, rationales, repair targets, and stop condition for the architecture decision.

Not this pattern when the current object is FPF pattern quality, measurement validity, evidence support, assurance, gate passage, candidate synthesis, comparison, selection, local choice, or ADR publication projection itself. Use the pattern for the next question named in `Relations`.

The first useful output is `ArchitectureDecisionAdequacyEvaluation@Project`:

```text
ArchitectureDecisionAdequacyEvaluation@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureDecisionEvaluationProjectUseRelationRef?: U.RelationRef governed by the exact evaluation-use or work-use pattern
  evaluationId:
  claimScopeRef: U.EntityRef referencing one U.ClaimScope
  selectedContextSliceRefs:
  effectiveReferenceScheme:
  referencePlane?:
  evaluationWindow:
  decisionQuestionInputProjectionRef:
  evaluatorSystemRef?: U.EntityRef constrained to U.System
  evaluatorSystemRoleKindRef?: U.KindRef
  evaluatorSystemRoleClassificationJudgmentRef?: U.RelationRef
  evaluatorAssignmentSpeciesRef?: U.RelationKindRef constrained under U.SystemRoleAssignment
  evaluatorAssignmentOccurrenceRef?: U.RelationRef constrained to U.SystemRoleAssignment
  evaluationWorkRef?: U.EntityRef constrained to U.Work
  evaluationPerformedUnderAssignmentRef?: U.RelationRef constrained to one obtaining F.6 performedUnderAssignment relation
  evaluationOperationApplicationRefs?: subject-pattern relation or A.6.1 application references
  adequacyResultEpistemeRef?: U.EpistemeRef
  declaredUse:
  architectureDecisionRelationRef:
  architectureDecisionRecordProjectionRef?:
  coordinateValues:
    - coordinateRef:
      value: 0|1|2|3|4|5
      valueLabel: absent|namedOnly|partiallyExpressedForDeclaredUse|sufficientlyExpressedForDeclaredUse|wellExpressedForDeclaredUse|exceptionallyExpressedForDeclaredUse
      adjacentValueRationale:
      evidenceOrSourceRefs?
      repairPatternRef?
      repairInstruction:
  strongestBlockingCoordinates:
  noAveragePolicy: true
  stopCondition:
  reevaluationTrigger:
```

Here `@Project` is a compatibility and retrieval cue only. A project-local ADA record names both the composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining record-use relation in `architectureDecisionEvaluationProjectUseRelationRef`; the evaluated decision's own project relation, the suffix, or either field alone is insufficient. `evaluatorSystemRoleKindRef` and `evaluatorSystemRoleClassificationJudgmentRef` remain optional and separate. When actual evaluation is claimed, the evaluator first has its A.13 core and `evaluationWorkRef` names Work independently admitted under A.15.1. Assignment species, occurrence, and `evaluationPerformedUnderAssignmentRef` are optional and appear only when the record or receiving use expressly represents precise assignment-bound attribution; any present F.6 ref uses the same obtaining A.13 assignment, and its absence or failure leaves the Work intact. Any operation application and result episteme remain separate. Kind, classification, assignment, Work, attribution, application, responsibility, and result do not substitute for one another.

