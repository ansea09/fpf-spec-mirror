---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__002_problem-frame.md"
commit_sha: "169e3e09c04a4174ce4c26682cf181a0d255b6f7"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:1 — Problem frame"
line_start: 84234
line_end: 84296
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

Use this pattern to publish a project architecture proposal for discussion or an effective project architecture decision for people who will act on it. A team can use an ADR, a decision memo, a trade-study record or a certification rationale. For a decision in force, identify the `ArchitectureDecisionRelation@Project` or the equivalent decision under the project’s governing practice.

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

A project can publish a record-shaped text that hides the actual architecture decision, or copy architecture descriptions, diagrams, and method material into a record without telling the reader what decision was made and what work must change.

A decision record can be small, readable, updateable, and tied to candidate synthesis, selected structures, architecture characteristics, method-use instructions, work split, confirmation evals, and source-return.

Start with the proposal readers are to discuss or the decision they can act on. Establish its status and choose the content readers need to examine, use or reopen it. For an effective decision, make the PAD decision relation recoverable.

After using the record, a reader can identify the decision to be made, the options and what can be done at the stated status. For an adopted design the reader can recover the outcome, grounds, consequences, changes to methods or work, how to check implementation and when to reopen the choice.

Use `C.32.PAD` when the decision content needs development; drafting its record can support that work without a second artifact. Keep an unresolved proposal visibly proposed. Use the subject pattern when the current question is architecture-description adequacy, a general MVPK face, evidence, assurance, gate passage, local choice, performed work or pattern authoring. Use the pattern for the next question named in `Relations`.

The first useful output is the readable decision record. `ArchitectureDecisionRecordProjection@Project` can organize its content when a structured account is useful; include the fields needed by the declared use:

```text
ArchitectureDecisionRecordProjection@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureDecisionRecordProjectUseRelationRef?: U.RelationRef governed by the exact record-use, publication-use, or work-use pattern
  projectionId:
  architectureDecisionRelationRef?: identify the effective decision here or by value when reporting that it was made
  architectureDecisionDescriptionRef: the recoverable content and its status, including a proposal when that is what is published
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

Here `@Project` is a compatibility and retrieval cue only. It does not make the projection a project, project work, or the architecture decision relation. When this record projection is local to one project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work`, while `architectureDecisionRecordProjectUseRelationRef` identifies the direct relation by which the record is published for, relied on by, or otherwise used in that work under the corresponding subject pattern. The decision relation, its description, the publication projection, any publication occurrence, and the composite project work remain separately identifiable.

