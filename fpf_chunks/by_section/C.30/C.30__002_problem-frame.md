---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__002_problem-frame.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:1 — Problem frame"
line_start: 51745
line_end: 51816
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

Use this pattern when architecture talk is doing more than naming modules, diagrams, documents, tool outputs, or a general engineering topic. Apply C.30 when the question under repair is what architecture claim is being described, what selected structures carry it, what artifact role the text or model being inspected has, and what the next admissible architecture move is.

The ordinary first output is intentionally small:

```text
ArchitectureQuestionCard@Project:
  describedHolonRef:
  boundedContextRef:
  architectureConcernCue:
  claimReadinessClass:
    preClaimCue | problemCardReady | architectureClaimReady | nonArchitectureClaimReady
  plainPromptLabel?:
  selectedStructureKindRefs: FinSet(ArchitectureStructureKindRef)
  collapseCue:
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

Use the cue only to choose the first architecture move: described holon, bounded context, one candidate structure kind, artifact role, and one admissible next move. If those fields cannot yet be named, keep the material as a concern cue or `ProblemCard@Context`-style issue rather than promoting it to `ArchitectureOf@Context` by wording alone. ISO 42010-style concern language may remain as lineage or project wording, but C.30 recovers the FPF representation fields as `architectureConcernCue`, `governingArchitectureConcernRefs?`, or `architectureConcernNotes?`.

`ArchitectureQuestionCard@Project` is a project-side triage aid for choosing one architecture move. Quality scores, risk ratings, proof, evidence, assurance, gate, decision, release, or publication-authority claims are governed by their FPF patterns when they are being made.

Use this when:

- a practitioner says "architecture" and needs to know whether the claim being made is about a holon, selected structure, architecture description, view, carrier, decision, work, evidence, assurance, or mathematical lens;
- downgrade an artifact to publication, diagram, carrier, source relation, or generated relation graph when it is not a Description or view;
- name the selected architecture-relevant structure and the next architecture move before writing a full architecture-description record;
- state a minimal architecture structural view only when it changes the next move;
- keep architecture-description machinery conditional instead of making every architecture discussion a multi-view description exercise;
- state `NoMathLensUseNeeded` when no mathematical lens changes the next architecture move;
- apply C.29 when a formal substrate, preserved and lost structure, or mathematical-lens use is being claimed.

Use a conditional `ArchitectureDescription@Context` bridge only when durable architecture-description use is being made: cross-team reuse, regulated or safety use, reusable design, comparison, source or lens reuse, or another named full-mode architecture-description use. Ordinary use stops at `ArchitectureQuestionCard@Project` when it makes one next architecture move clear. If the architecture description itself becomes the EntityOfConcern under repair, use `C.30.AD`.

What goes wrong if C.30 is missed: architecture collapses into a document, a module diagram, a workflow graph, a mathematical lens, a benchmark, a maturity score, or a decision record. Then the practitioner cannot see which holon is described, which structures matter, what the first architecture move is, which source or lens relation is being relied on, and which non-architecture claim must be governed elsewhere.

What C.30 buys in practice: a practitioner can separate architecture claim, selected structure, architecture description, view, publication, source relation, and non-architecture claim kind, then choose one small next architecture move.

Not this pattern when the EntityOfConcern under repair is only a general selected structure, a full architecture description, an architecture structural view, a TGA flow relation, an LCA/control view, a mathematical-lens use, measurement, evidence, assurance, gate, work, decision, or publication. Use `A.22`, `C.30.AD`, `C.30.ASV`, `C.30.TGA-FLOW-REL`, `C.30.LCA`, `C.29`, `C.16`, `A.10`, `G.6`, `B.3`, `A.20`, `A.21`, `A.15`, `C.11`, or `E.17` respectively, and keep C.30 only for the architecture-claim portion if that portion is being claimed.

Thin precision-restoration pointer: if the issue under repair is still whether *architecture*, *architecture description*, *structural view*, *module diagram*, *model*, *artifact*, *functional architecture*, or a source label such as *layer*, *level*, *tier*, *stack*, *block*, *expert*, *cache*, *router*, or *gate* names an architecture claim, description, view, carrier, source, structure, or non-architecture governing-pattern application, use `C.30.P` and `C.30.STRAT` as triggered before applying C.30 to the recovered architecture portion. Keep the trigger tables in those patterns; C.30 is applied only after `ArchitectureOf@Context`, selected architecture-relevant structure, conditional `ArchitectureDescription@Context` bridge use, `C.30.AD` application, or the non-architecture application named by value is recoverable.

