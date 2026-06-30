---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__002_problem-frame.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:1 — Problem frame"
line_start: 67128
line_end: 67139
dependencies:
  - "A.19.ECS"
  - "E.10"
  - "E.19"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9"
  - "F.19"
keywords:
---

### E.9.DA:1 - Problem frame

Use `E.9.DA` when one `DRR` must be reliable enough for a declared FPF authoring use: pattern drafting, host amendment, selected-locus distribution, accepted-decision carry-through, source-use carry-through, scope-boundary decision, split decision, or architecture-hold decision.

Not this pattern when the evaluated object is one authored pattern version, one admission or refresh review, one local wording repair, or a measurement-law problem. Use `E.21`, `E.19`, `E.10` and its precision-restoration neighbours, or `C.16`, `A.17`, `A.18`, and `A.19` for those objects.

First useful move: name `DRRVersionRef` by value, declared authoring use, selected-locus disposition map, and qualification window; then evaluate every decision-adequacy coordinate in this pattern. Missing decisions lower coordinates and produce repair, split, or hold status inside the same evaluation.

What goes wrong if missed: a formally valid `DRR` may still be too weak for drafting. It may summarize sources instead of deciding, mention neighbours without obligations, hide rejected alternatives, leave trigger words unresolved, or omit the first drafting action.

Primary EntityOfConcern in plain terms: the decision-adequacy claim of one `DRR` version for a declared FPF authoring use.

