---
chunk_kind: "child"
pattern_id: "E.10.MOVE"
pattern_title: "Move and Readiness Wording Precision Restoration"
section_id: "E.10.MOVE:5"
section_title: "Archetypal Grounding - Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.MOVE/E.10.MOVE__006_archetypal-grounding-worked-slices.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "E.10.MOVE — Move and Readiness Wording Precision Restoration"
  - "E.10.MOVE:5 — Archetypal Grounding - Worked Slices"
line_start: 69255
line_end: 69291
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.16"
  - "A.16.0"
  - "A.21"
  - "A.3.4.P"
  - "B.1.6"
  - "C.24"
  - "C.30"
  - "C.30.AD"
  - "E.10"
  - "E.10.ARCH"
  - "E.11.PUR"
  - "E.17"
  - "E.18.1"
  - "E.24"
  - "G.6"
keywords:
---

### E.10.MOVE:5 - Archetypal Grounding - Worked Slices

#### E.10.MOVE:5.1 - "What is the next FPF move?"

Source sentence: "The next FPF move is to check architecture."

Repair:

```text
ProjectConcern: architecture uncertainty in a current project
SourceUseClass: seminarPatternUse
RecoveredRelations: PatternUseRecommendation@Context
DirectGoverningPatterns: E.11.PUR, C.30
RetainedPlainWording: "next useful move" may stay in teaching prose
BlockedOverread: no U.Move, no performed architecture work
FinalWordingOrBlocker: recommend C.30 as the next pattern use
RemainingReaderUse: write or inspect ArchitectureQuestionCard@Project
```

#### E.10.MOVE:5.2 - TameFlow `MOVE`

Source sentence: "The MOVE is full-kitted and ready."

Repair: source `MOVE` is wording from Steve Tendon's TameFlow framework. Recover target WorkPlan or PlanItem, `FullKitCondition`, `WorkEntryReadiness@Context`, and possible A.21 gate decision. Do not claim target `U.Work` occurred unless dated work evidence is current.

#### E.10.MOVE:5.3 - Workflow Diagram

Source sentence: "This workflow is the next move after problem framing."

Repair: if the diagram describes a transformation-flow structure or method description, use `A.3.4.P`, `E.18`, or `A.3.2`. If the current question is which FPF pattern use should follow problem framing, use `PatternUseRecommendation@Context`. Split if both claims are present.

#### E.10.MOVE:5.4 - Evidence Path

Source sentence: "Follow the evidence path to approval."

Repair: if a graph-theoretic or provenance path is current, use A.10 or G.6. If the claim is evidence support for a decision, use the evidence relation. If the claim is gate passage, use A.21. If the claim is work authorization or deontic permission, use the pattern that governs that claim. Do not turn evidence path wording into a route that authorizes work by resemblance.

