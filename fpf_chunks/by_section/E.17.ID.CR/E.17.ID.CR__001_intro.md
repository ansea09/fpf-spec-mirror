---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "ComparativeReviewUnit - bounded comparison over comparative review units"
section_id: "E.17.ID.CR:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__001_intro.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "E.17.ID.CR — ComparativeReviewUnit - bounded comparison over comparative review units"
  - "E.17.ID.CR:intro — Intro"
line_start: 83423
line_end: 83459
dependencies:
  - "A.15"
  - "A.15.4"
  - "A.16.0"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.9"
  - "A.6.P"
  - "B.5.2"
  - "B.5.2.0"
  - "C.11"
  - "C.2.2a"
  - "E.14"
  - "E.17.AUD.LHR"
  - "E.17.AUD.OOTD"
  - "E.17.EFP"
  - "F.9"
  - "F.9.1"
keywords:
---

## E.17.ID.CR - ComparativeReviewUnit - bounded comparison over comparative review units

> **Status:** Stable

**Plain-name.** Bounded comparison over comparative review units.

**Use this when.** Use this pattern when a team needs one small comparison note, comparison sheet, or guided review aid over already available source epistemes or source publications. The unit should make one bounded contrast or a small set of contrast rows inspectable while the shared review frame stays visible and downstream claim or effect remains outside.

**First-minute working moment.** A team has two or more source-pinned notes, sheets, views, or review aids on the table. They need one honest comparison unit: two design options for one release, two methods for one task family, two vendor bulletins for one control scope, two research syntheses for one uncertainty question, or two programme strategies for one initiative. The job is not yet action selection, approval, ontology repair, or wider work-process control. It is to compare without pretending that the comparison note already became a decision.

**First output.** Use the ordinary seven-row card:

```text
ComparativeReviewUnit:
  ReviewedSources:
  SharedReviewFrame:
  ComparedAlternatives:
  ComparisonCriterionOrRows:
  BoundedLift:
  BlockedDownstreamClaimOrEffect:
  BoundaryTrigger:
```

**What goes wrong if missed.** A comparison unit is either dismissed as harmless prose or overread as equivalence, action selection, gate pressure, release approval, work or reliance guidance, or adjudication authority. The team then argues about hidden authority instead of inspecting the bounded contrast.

**What this buys in practice.** The team can compare already available sources, inspect one bounded contrast or a small comparison sheet, and use the boundary trigger to name any crossed claim and the pattern that governs that claim.

**Not this pattern when.** If the primary question is no longer the bounded comparison unit or its shared review frame, name the crossed claim and apply the governing pattern for that claim: source transformation, bridge, explanation face, prompt or action selection, ontology or `EntityOfConcern` change, decision, work or reliance, gate, assurance, adjudication, or reduced-use source rendering.

**Quick working-fit check.**
1. Am I working over the comparative review unit itself?
2. Does the shared review frame stay preserved, with compared alternatives still distinct when they are distinct?
3. Is one bounded contrast or small row set being made visible?
4. Is the downstream claim or effect still outside?

If yes, stay here and use the ordinary card. If no, use the neighboring-work boundary in `E.17.ID.CR:4.5`.

