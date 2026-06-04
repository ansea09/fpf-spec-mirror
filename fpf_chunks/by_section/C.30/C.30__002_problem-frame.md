---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__002_problem-frame.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:1 — Problem frame"
line_start: 51153
line_end: 51223
dependencies:
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
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
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

Use this pattern when architecture talk is doing more than naming modules, diagrams, documents, tool outputs, or a general engineering topic. Open C.30 when the live question is what architecture claim is being described, what selected structures carry it, what artifact role the current text or model has, and what the next admissible architecture move is.

The ordinary first output is intentionally small:

```text
ArchitectureQuestionCard@Project:
  describedHolonRef:
  boundedContextRef:
  liveArchitectureConcernCue:
  claimReadinessClass:
    preClaimCue | problemCardReady | architectureClaimReady | nonArchitectureClaimReady
  plainPromptLabel?:
  activeStructureKindRefs: FinSet(ArchitectureStructureKindRef)
  currentCollapseCue:
  firstArchitectureMove:
  ordinaryNotThisPatternBoundary:
  governingPatternApplicationRefs:
```

Use `ArchitectureConcernCue` only to recognize the architecture problem family that chooses the first structure kind and architecture move:

```text
ArchitectureConcernCue:
  changeLocalization | substitutionOrReplacement | flowBottleneck |
  controlOrRateMismatch | dataCustodyOrStateResidence |
  physicalSeparationOrPlacement | evidenceReuseOrAssuranceReuse |
  scaleWindowOrCoarseningLoss | runtimeFailureMode |
  crossScopeResidual | descriptionViewLoss | otherDeclared
```

Typical architecture problem cues:

```text
changeLocalizationFailure
substitutionFailure
crossViewMismatch
flowBottleneckOrHiddenCrossing
controlRateOrRecoveredControlLayerMismatch
dataCustodyOrStateResidenceUnclear
placementOrJurisdictionMismatch
evidenceReuseFailure
sourceReturnNeeded
crossScopeResidual
generatedViewLoss
```

Use the cue only to choose the first architecture move: described holon, bounded context, one candidate structure kind, artifact role, and one admissible next move. If those fields cannot yet be named, keep the material as a concern cue or `ProblemCard@Context`-style issue rather than promoting it to `ArchitectureOf@Context` by wording alone. ISO 42010-style concern language may remain as lineage or project wording, but C.30 recovers the FPF representation fields as `liveArchitectureConcernCue`, `governingArchitectureConcernRefs?`, or `architectureConcernNotes?`.

`ArchitectureQuestionCard@Project` is a project-side triage aid for choosing one architecture move. Quality scores, risk ratings, proof, evidence, assurance, gate, decision, release, or publication-authority claims exit to their exact neighboring FPF patterns when they become live.
The action palette for `firstArchitectureMove` is deliberately short:

- name or narrow the described holon and bounded context;
- choose the live structure kind;
- downgrade an artifact to publication, diagram, carrier, source relation, or generated relation graph when it is not a Description or view;
- repair a collapsed function, module, flow, control, interface, or signature claim;
- open a minimal architecture structural view only when it changes the next move;
- assign C.29, A.10, B.3, A.20, A.21, C.28, A.15, C.11, C.16, or another exact governing pattern only when its claim kind is live;
- state `NoMathLensUseNeeded` when no mathematical lens changes the next architecture move;
- stop with one admissible next architecture move.

A conditional `ArchitectureDescription@Context` bridge opens only when durable architecture-description use is live: cross-team reuse, regulated or safety use, reusable design, comparison, source or lens reuse, or another named full-mode architecture-description use. Ordinary use stops at `ArchitectureQuestionCard@Project` when it makes one next architecture move clear. If the architecture description itself becomes the live EntityOfConcern, use `C.30.AD`.

What goes wrong if C.30 is missed: a module diagram, TGA graph, LCA sketch, control sketch, mathematical-lens output, generated relation graph, ADR, dashboard, or benchmark result is treated as the architecture; architecture then starts carrying non-architecture claim kinds it cannot carry.

What C.30 buys in practice: a practitioner can separate architecture claim, selected structure, architecture description, view, publication, source relation, and non-architecture claim kind, then choose one small next architecture move.

Not this pattern when the live question is only structure as such, an architecture structural view, or a TGA graph relation, path relation, or crossing relation. Use `A.22`, `C.30.ASV`, `E.18`, or `C.30.TGA-FLOW-REL` as appropriate. If another live claim is present, use the exact governing pattern and keep C.30 only to the architecture claim, selected-structure, or conditional architecture-description-use portion.

Thin precision-restoration pointer: if the live issue is still whether *architecture*, *architecture description*, *structural view*, *module diagram*, *model*, *artifact*, *functional architecture*, or a source label such as *layer*, *level*, *tier*, *stack*, *block*, *expert*, *cache*, *router*, or *gate* names an architecture claim, description, view, carrier, source, structure, or exact non-architecture receiving-pattern application, use `C.30.P` and `C.30.STRAT` as triggered before C.30 receives the recovered architecture portion. Do not copy the trigger tables into C.30; C.30 resumes after `ArchitectureOf@Context`, selected architecture-relevant structure, conditional `ArchitectureDescription@Context` bridge use, `C.30.AD` application, or the exact non-architecture application is recoverable.
