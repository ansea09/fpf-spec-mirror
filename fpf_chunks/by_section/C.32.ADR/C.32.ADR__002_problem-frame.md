---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__002_problem-frame.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:1 — Problem frame"
line_start: 79381
line_end: 79443
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32.ADA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
keywords:
  - "ADR projection"
  - "ArchitectureDecisionDescription@Project"
  - "ArchitectureDecisionRecordProjection@Project"
  - "architecture decision record"
  - "consequences"
  - "method-use instruction"
  - "publication boundary"
  - "rationale"
  - "section function"
  - "supersession"
---

### C.32.ADR:1 - Problem frame

Use this pattern when an `ArchitectureDecisionRelation@Project` or equivalent project architecture decision must be published as an ADR-like record, decision memo, trade-study record, certification rationale, or similar decision-description record.

Primary working reader: an architect or architecture-responsible practitioner preparing a decision record for developers, reviewers, maintainers, operators, certifiers, or future architects.

Typical entry phrases:

```text
"The project decision is made; now we need an ADR that future developers can use."
"The record must show options, decision, rationale, consequences, and confirmation without becoming the decision itself."
"This is not a software project; can a trade-study memo play the ADR role?"
"The ADR package must link to architecture views without duplicating the whole architecture description."
"A future team must know when this decision is superseded or violated."
```

**First-minute use slice.** A platform architect has a C.32.PAD decision relation selecting event-carried integration with a bounded exception. Using C.32.ADR, the architect creates an ADR projection with section functions for problem frame, candidate options, decision outcome, rationale, consequences, method-use instruction, work split, confirmation eval, source-return links, and supersession. The file is short enough for developers to read, but it remains a publication projection of the decision description, not the decision relation and not the architecture itself.

The primary `EntityOfConcern` is `ArchitectureDecisionRecordProjection@Project`: a publication projection of `ArchitectureDecisionDescription@Project` into an ADR-like record or package. Select this pattern only when the work is to publish or package that decision description for a declared reader use; generic ADR advice that cannot be mapped to decision-section functions stays outside C.32.ADR.

`ArchitectureDecisionRecordProjection@Project` is not a new `U.*` kind and not a new root publication ontology. It publishes a project decision description for the declared reader use. Use `E.24.PUB` for actual publication and `E.17` when a source-backed face and source return are needed; use `C.32.PAD` for the decision relation.

What goes wrong if C.32.ADR is missed: the project either publishes a record-shaped text that hides the actual architecture decision, or it copies architecture descriptions, diagrams, and method material into a record without telling the reader what decision was made and what work must change.

What C.32.ADR buys in practice: a decision record can be small, readable, updateable, and still tied to candidate synthesis, selected structures, architecture characteristics, method-use instructions, work split, confirmation evals, and source-return.

Ordinary working move: start from a PAD decision relation, select the record's publication scope, map each necessary section to the decision content it carries, then publish only what the reader needs to use, check, or reopen the decision.

Adoption test: after using C.32.ADR, a future reader can recover the decision question, considered options, outcome, rationale, consequences, required method or work change, confirmation or eval path, source links, and supersession condition without mistaking the record for the architecture or the decision relation.

Use `C.32.PAD` when the decision content still needs development; drafting its record can support that work without a second artifact. Keep an unresolved proposal visibly proposed. Use the direct subject pattern when the current question is architecture-description adequacy, a general MVPK face, evidence, assurance, gate passage, local choice, performed work or pattern authoring. Use the pattern for the next question named in `Relations`.

The first useful output is the readable decision record. `ArchitectureDecisionRecordProjection@Project` can organize its content when a structured account is useful; include the fields needed by the declared use:

```text
ArchitectureDecisionRecordProjection@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureDecisionRecordProjectUseRelationRef?: U.RelationRef governed by the exact record-use, publication-use, or work-use pattern
  projectionId:
  architectureDecisionRelationRef:
  architectureDecisionDescriptionRef:
  publicationCarrierRef:
  publicationScopeRef:
  intendedReaderRefs:
  status:
  sectionFunctionRows:
    - sectionFunction:
      sectionHeadingOrCarrierSlot:
      sourceDecisionSlotRefs:
      requiredReaderUse:
      omittedByDesign?
      sourceReturnCondition?
  architectureDescriptionRefs:
  methodAndWorkRefs:
  confirmationOrEvalRefs:
  supersedesRecordRefs?
  supersededByRecordRef?
  updateOrReopenCondition:
  publicationUseRefs?
```

Here `@Project` is a compatibility and retrieval cue only. It does not make the projection a project, project work, or the architecture decision relation. When this record projection is genuinely local to one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work`, while `architectureDecisionRecordProjectUseRelationRef` identifies the direct relation by which the record is published for, relied on by, or otherwise used in that work under the corresponding subject pattern. The decision relation, its description, the publication projection, any publication occurrence, and the composite project work remain separately identifiable.

