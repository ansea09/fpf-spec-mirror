---
chunk_kind: "child"
pattern_id: "E.17.ID.CR"
pattern_title: "Compare Sources Within a Shared Review Frame (ComparativeReviewUnit)"
section_id: "E.17.ID.CR:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.ID.CR/E.17.ID.CR__001_intro.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.ID.CR — Compare Sources Within a Shared Review Frame (ComparativeReviewUnit)"
  - "E.17.ID.CR:intro — Intro"
line_start: 115202
line_end: 115238
dependencies:
  - "A.15"
  - "A.15.2"
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

## E.17.ID.CR - Compare Sources Within a Shared Review Frame (ComparativeReviewUnit)

> **Status:** Stable

**Plain-name.** Bounded source comparison under a shared review frame.

**Use this when.** A team needs a small note, comparison sheet, or guided aid to compare available source epistemes or source publications. The unit should make one bounded contrast or a small set of contrast rows available for inspection, keep their shared review frame visible, and leave downstream claims and effects to the work that establishes them.

**First-minute working moment.** A team has two or more source-pinned notes, sheets, views, or review aids on the table. They need one comparison unit for their review: two design options for one release, two methods for one task family, two vendor bulletins for one control scope, two research syntheses for one uncertainty question, or two programme strategies for one initiative. The note compares the sources. Action selection, approval, ontology repair and wider control of the work remain separate. A comparison alone cannot decide among the options.

**First output.** One bounded comparison whose minimum content for ordinary use can be recovered in the unit or its immediate review context. A source-linked paragraph or small comparison table may suffice. The card below helps recover that content. The card can stay in the review context unless a receiving contract requires its separate publication. Include a blocked-use or boundary field only when it changes this comparison’s interpretation or use:

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

**What this buys in practice.** The team can compare the available sources, inspect one bounded contrast or a small comparison sheet, and identify a claim that goes beyond the comparison and the pattern that governs it when the boundary trigger fires.

**Not this pattern when.** If the primary question is no longer the bounded comparison unit or its shared review frame, name the crossed claim and apply the governing pattern for that claim: source transformation, bridge, explanation face, prompt or action selection, ontology or `EntityOfConcern` change, decision, work or reliance, gate, assurance, adjudication, or reduced-use source rendering.

**Quick working-fit check.**
1. Is the comparative review unit my work object?
2. Does the comparison preserve the shared review frame and keep distinct alternatives separate?
3. Is one bounded contrast or small row set being made visible?
4. Is the downstream claim or effect still outside?

If yes, stay here and keep the ordinary minimum recoverable. If no, use the neighboring-work boundary in `E.17.ID.CR:4.5`.

