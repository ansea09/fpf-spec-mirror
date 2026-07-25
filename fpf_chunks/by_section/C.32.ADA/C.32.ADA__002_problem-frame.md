---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__002_problem-frame.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:1 — Problem frame"
line_start: 65385
line_end: 65439
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

**First-minute use slice.** A reviewer receives a PAD decision relation and ADR projection for a modularization decision. Using C.32.ADA, the reviewer declares the use: "ready for developer work and ADR publication." The reviewer scores each coordinate with a short rationale. Candidate traceability is `4 wellExpressedForDeclaredUse`, architecture-characteristic trade-off is `3 sufficientlyExpressedForDeclaredUse`, method docking is `2 partiallyExpressedForDeclaredUse`, and publication projection is `4 wellExpressedForDeclaredUse`. The result does not approve the decision. It directs repair to the method-use instruction, responsible roles, readiness exit, and expected structure effect before the decision can guide developer work.

The primary `EntityOfConcern` is `ArchitectureDecisionAdequacyEvaluation@Project`: an evaluation record over one `ArchitectureDecisionRelation@Project`, optional `ArchitectureDecisionRecordProjection@Project`, and declared use.

`ArchitectureDecisionAdequacyEvaluation@Project` is not a new `U.*` kind, not a gate, not evidence, not assurance, not pattern-quality evaluation, and not a replacement for `C.32.PAD`. It is a typed adequacy evaluation that sends weak coordinates back to their governing repair patterns.

What goes wrong if C.32.ADA is missed: a decision can appear complete because it has a record, rationale, or diagram, while it is unusable for the declared work. Weak candidate basis, hidden trade-offs, missing method instructions, absent source-return, and vague supersession conditions remain invisible until implementation or review fails.

What C.32.ADA buys in practice: the project can evaluate architecture decisions by complete coordinate set, keep kinds distinct, and repair the weakest live coordinates without turning adequacy into a single score.

Ordinary working move: declare the evaluation use, evaluate every coordinate with an ordinal value and rationale, then return each weak coordinate to the smallest governing pattern that can repair it.

Adoption test: after using C.32.ADA, another practitioner can see the declared use, complete coordinate values, rationales, repair targets, and stop condition for the architecture decision.

Not this pattern when the current object is FPF pattern quality, measurement validity, evidence support, assurance, gate passage, candidate synthesis, comparison, selection, local choice, or ADR publication projection itself. Use the receiving pattern named in `Relations`.

The first useful output is `ArchitectureDecisionAdequacyEvaluation@Project`:

```text
ArchitectureDecisionAdequacyEvaluation@Project:
  evaluationId:
  declaredUse:
  architectureDecisionRelationRef:
  architectureDecisionRecordProjectionRef?
  evaluatorRoleRef:
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

