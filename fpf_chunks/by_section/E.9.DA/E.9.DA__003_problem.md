---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__003_problem.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:2 — Problem"
line_start: 71563
line_end: 71578
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

### E.9.DA:2 - Problem

`E.9` defines the `DRR` kind and minimum decision-rationale form. It does not by itself say whether one concrete `DRR` is decision-bearing enough for downstream FPF authoring. Without `E.9.DA`, reviewers tend to approve headings, source volume, or clean prose while the pattern author still has to invent missing decisions.

Recurring failures:

1. The decision question is broad or implicit.
2. The selected answer is a summary rather than a decision.
3. Alternatives, rejected options, and outside-decision items are not closed.
4. Receiving loci are named but not assigned content obligations or non-obligations.
5. The selected FPF content architecture is explicit but wrong.
6. Source use is copied without saying what changed in the accepted decision.
7. Architecture descriptions, views, graphs, packets, or notes are treated as the FPF decision.
8. Administrative state becomes adequacy evidence.
9. Ordinal adequacy values become repair targets, so the `DRR` gains source rows, locus tables, boundary catalogues, or review proof while the selected answer and first drafting action do not become more decisive.

