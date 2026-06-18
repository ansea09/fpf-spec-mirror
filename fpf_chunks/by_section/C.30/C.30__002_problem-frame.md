---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__002_problem-frame.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:1 — Problem frame"
line_start: 52238
line_end: 52273
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture question card"
  - "architecture-description boundary"
  - "artifact-as-architecture guard"
  - "grounded architecture"
  - "selected structure"
---

### C.30:1 - Problem frame

Use this pattern when the current question is an `ArchitectureOf@Context` claim: which selected `U.Structure` refs matter for one described `U.Holon` in one `U.BoundedContext`, and what next architecture move follows.

The first useful move is small:

```text
ArchitectureQuestionCard@Project:
  describedHolonRef:
  boundedContextRef:
  architectureConcernCue:
  sourcePhrase?, if useful:
  questionDisposition:
    concernCueOnly | problemCardReady | architectureClaimReady | nonArchitectureClaimReady
  selectedStructureRefs or selectedStructureKindRefs:
  inspectedMaterialRole, if current:
  firstArchitectureMove:
  architectureDescriptionBridge, if durable description use is current:
  governingPatternApplicationRefs, if another claim is being made:
  non-admissible overread:
```

`architectureConcernCue` is recognition wording only until it helps choose one selected structure kind and one architecture move. When a controlled cue is useful, use `changeLocalization`, `substitutionOrReplacement`, `flowBottleneck`, `controlOrRateMismatch`, `dataCustodyOrStateResidence`, `physicalSeparationOrPlacement`, `evidenceReuseOrAssuranceReuse`, `scaleWindowOrCoarseningLoss`, `runtimeFailureMode`, `crossScopeResidual`, `descriptionViewLoss`, or `otherDeclared`. Local phrases such as change localization failure, hidden crossing, source return, generated-view loss, or state-residence uncertainty may remain in `sourcePhrase?` or Plain prose. If the described holon, bounded context, selected structure, and first move cannot yet be named, set `questionDisposition` to `concernCueOnly` or `problemCardReady` rather than promoting it to `ArchitectureOf@Context` by wording alone.

`ArchitectureQuestionCard@Project` is a project-side triage aid for choosing one architecture move. `questionDisposition` records the card's current result: keep it as a concern cue, prepare a `ProblemCard@Context`, open an `ArchitectureOf@Context` claim, or name the non-architecture governing pattern. The card is not an evidence record, gate, decision, release record, quality score, risk rating, or publication-authority claim. When those claims are being made, name the governing FPF pattern and keep C.30 to the architecture-claim portion; later sections cite this boundary rather than repeating the full non-use catalogue.

Use a conditional `ArchitectureDescription@Context` bridge only when durable architecture-description use is current: cross-team reuse, regulated or safety use, reusable design, comparison, source or lens reuse, or another named full-mode architecture-description use. Ordinary use stops at `ArchitectureQuestionCard@Project` when it makes one next architecture move clear. If the architecture description itself becomes the `EntityOfConcern` under repair, use `C.30.AD`.

What goes wrong if C.30 is missed: the practitioner reasons from a document, module diagram, workflow graph, mathematical lens, benchmark, maturity score, or decision record instead of recovering the described holon, selected structures, first architecture move, and neighboring claim kind.

What C.30 buys in practice: a practitioner can separate architecture claim, selected structure, architecture description, view, publication form, source relation, and non-architecture claim kind, then choose one small next architecture move.

Not this pattern when the `EntityOfConcern` under repair is not an architecture claim, selected architecture-relevant structure, source relation, description relation, view relation, publication-role recovery for an architecture claim, or the thin architecture-description bridge needed for one architecture move. Use the direct governing pattern named by the recovered relation, and keep C.30 only for the architecture-claim portion if that portion is being claimed. Common neighboring claim boundaries are summarized in `C.30:12`.

Thin precision-restoration pointer: if the issue under repair is still whether *architecture*, *architecture description*, *structural view*, *module diagram*, *model*, *source material*, *functional architecture*, or a source label such as *layer*, *level*, *tier*, *stack*, *block*, *expert*, *cache*, *router*, or *gate* names an architecture claim, description, view, publication form, source relation, structure, or non-architecture governing-pattern application, use `C.30.P` or `C.30.STRAT` as triggered before applying C.30 to the recovered architecture portion. If the recovered issue is mathematical-lens use, apply `C.29`; when no mathematical-lens move changes the architecture work, keep ordinary prose or use `NoMathLensUseNeededNote` under C.29 rather than creating a C.30-local lens result. Keep the trigger tables in those patterns; C.30 is applied only after `ArchitectureOf@Context`, selected architecture-relevant structure, conditional `ArchitectureDescription@Context` bridge use, `C.30.AD` application, or the non-architecture application named by value is recoverable.

