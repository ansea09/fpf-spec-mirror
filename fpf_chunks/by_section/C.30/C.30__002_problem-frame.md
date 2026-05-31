---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Architecture Description Adequacy (ADA)"
section_id: "C.30:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__002_problem-frame.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "C.30 — Architecture Description Adequacy (ADA)"
  - "C.30:1 — Problem frame"
line_start: 51323
line_end: 51396
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
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
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
  - "architecture description"
  - "architecture question card"
  - "artifact-as-architecture guard"
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
  claimPosture:
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
controlRateOrLayerMismatch
dataCustodyOrStateResidenceUnclear
placementOrJurisdictionMismatch
evidenceReuseFailure
sourceReturnNeeded
crossScopeResidual
generatedViewLoss
```

Use the cue only to choose the first architecture move. The cue is not a quality score, failure proof, risk rating, gate result, or decision.

Do not treat the cue as a quality, measure, risk score, decision, or free `ArchitectureConcern` ontology. If the concern cannot yet name described holon, bounded context, one candidate structure kind, and one admissible next architecture move, keep it as a concern cue or `ProblemCard@Context`-style issue; do not promote it to `ArchitectureOf@Context` by wording alone. ISO 42010-style concern language may remain as lineage or project wording, but C.30 recovers the FPF carrier as `liveArchitectureConcernCue`, `governingArchitectureConcernRefs?`, or `architectureConcernNotes?`.

This is a project-side triage aid, not `U.Architecture`, not evidence, not a decision, and not a mandatory publication.
The action palette for `firstArchitectureMove` is deliberately short:

- name or narrow the described holon and bounded context;
- choose the live structure kind;
- downgrade an artifact to publication, diagram, carrier, source-relation object, or generated relation graph when it is not a D/S view;
- repair a collapsed function, module, flow, control, interface, or signature claim;
- open a minimal architecture structural view only when it changes the next move;
- assign C.29, A.10, B.3, A.20, A.21, C.28, A.15, C.11, C.16, or another exact governing pattern only when its claim kind is live;
- state `NoMLANeeded` when no mathematical lens changes the next architecture move;

- stop with one admissible next architecture move.

The full `ArchitectureDescription@Context` opens only for durable publication, cross-team use, regulated or safety use, reusable design, FPF pattern example, comparison, reuse of a source, evidence, lens, or assurance relation, or a comparable full-mode claim kind. Ordinary use stops at `ArchitectureQuestionCard@Project` when it makes one next architecture move clear.

What goes wrong if C.30 is missed: a module diagram, Transduction Graph Architecture (TGA) graph, Layered Control Architecture (LCA)/control sketch, mathematical-lens output, generated relation graph, ADR, dashboard, or benchmark result is treated as the architecture; architecture then starts carrying evidence, assurance, gate, work, release, causal, or decision claim kinds it cannot carry.

What C.30 buys in practice: a practitioner can separate architecture claim, selected structure, architecture description, view, publication, source relation, and non-architecture claim kind, then choose one small next architecture move instead of opening a full measurement, synthesis, assurance, or decision apparatus by default.

Not this pattern when the live question is only structure as such. Use A.22. If it is an architecture structural view, use `C.30.ASV`. If it is a TGA graph, path, or crossing relation, use `E.18` and `C.30.TGA-FLOW-REL` when architecture-flow description is live. If it is evidence, assurance, causal use, gate, work, decision, publication authority, mathematical-lens adequacy, measurement, structural information, structural equivalence, morphism, or discovery aid, use the exact governing pattern or an admitted receiving pattern and keep C.30 only to the architecture-description portion.

Thin precision-restoration pointer: if the live issue is still whether *architecture*, *architecture description*, *structural view*, *module diagram*, *model*, *artifact*, *layer*, or *functional architecture* names an architecture claim, description, view, carrier, source, structure, or non-architecture receiving object, use `C.30.P` first. Do not copy the `C.30.P` trigger table into C.30; C.30 resumes after the architecture-description claim or exact non-architecture exit is recoverable.
