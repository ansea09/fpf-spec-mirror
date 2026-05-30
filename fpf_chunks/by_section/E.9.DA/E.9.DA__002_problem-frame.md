---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__002_problem-frame.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:1 — Problem frame"
line_start: 55595
line_end: 55620
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
keywords:
---

### E.9.DA:1 - Problem frame

Use `E.9.DA` when one `DRR` must become reliable enough for a declared FPF authoring use: pattern drafting, host amendment, receiving-locus distribution, accepted-decision carry-through, source-use carry-through, narrowing decision, split decision, or architecture-hold decision.

Use it especially when the `DRR` already follows `E.9` section shape but authors still disagree about whether the decision is decisive enough, carried by value, lexically exact enough, and actionable enough for pattern-host writing.

**Not this pattern when.** Use `E.9` to write the `DRR` kind and minimum decision-rationale form. Use `E.21` when the evaluated object is one authored FPF pattern version and the live claim is pattern quality. Use `E.19` when the evaluated object is one FPF pattern admission or refresh review. Use `E.10` when the live problem is lexical trigger repair in the `DRR` text. Use `C.16`, `A.17`, `A.18`, and `A.19` when the live problem is measurement legality, Characteristic and Scale discipline, or a general `CharacteristicSpace`.

**First useful move.** Name the bounded `DRR` version being evaluated, the declared `DRR` authoring use it is meant to carry, and the first pattern-drafting decision that would fail if the `DRR` stayed vague.

**Pattern-version handoff.** If the evaluated object is one FPF pattern version, do not start with `E.9.DA`. Start with the `E.21` fast reader move loop: name `<PatternVersionRef> for <WorkingReaderScope> under <IntendedUse> within <QualificationWindow>`, then read only the pattern's `Problem frame` and `Solution` until the first admissible action-guiding move is recoverable. Open `E.9.DA` only when the live blocker is whether an upstream `DRR` is decision-bearing enough for the pattern authoring use.

**Improvement-oriented quality-read question framing.** An `E.9.DA` read may cite an `E.22` `QualityReadQuestionFrame` when the caller needs to distinguish drafting-floor adequacy, exceptional decision-adequacy improvement, Pareto trade-off inspection, open-question discovery, or returned-finding absorption. If no purpose is declared, the ordinary default is a floor read for the declared downstream authoring use, not maximal DRR improvement.

**Ordinary-cost posture.** `E.9.DA` is not a preliminary audit before every pattern-quality read, admission review, or local wording repair. It opens only when a `DRR` decision-adequacy claim is live and a downstream author would otherwise have to invent a missing decision.

**Cheap stop.** If the `DRR` only records a small local editorial decision and no downstream pattern drafting or cross-pattern distribution depends on it, do not create a full adequacy read. Apply `E.9` directly and run `E.10` only for live wording.

**What goes wrong if missed.** A formally valid `DRR` can still be too weak for drafting: it may summarize sources instead of deciding, leave neighbour patterns as unclassified receiving loci, hide rejected alternatives, use broad trigger words as if they were exact kinds, or omit the practical drafting action that the decision is supposed to enable.

**What this buys.** `E.9.DA` gives authors and reviewers one compact way to say whether a `DRR` is admissible for the declared authoring use, admissible only after narrowing, still needs repair before drafting, must split into several decisions, or must hold for architecture decision.

**Governed object in plain terms.** The governed object is the `DRR` decision-adequacy claim for one exact `DRR` version under one declared authoring use.

**Primary working reader.** The first reader is an FPF author, reviewer, or steward who must decide whether pattern drafting can rely on the `DRR` without inventing missing decisions. The downstream reader is the pattern author who will turn the accepted decision into user-facing FPF pattern text.

