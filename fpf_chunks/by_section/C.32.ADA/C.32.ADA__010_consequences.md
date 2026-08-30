---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__010_consequences.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:9 — Consequences"
line_start: 66577
line_end: 66585
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.13"
  - "E.17"
  - "E.21"
  - "E.22"
  - "E.24.PUB"
keywords:
  - "ArchitectureDecisionAdequacyEvaluation@Project"
  - "E.21 labels"
  - "architecture decision adequacy"
  - "complete coordinate set"
  - "declared use"
  - "method docking"
  - "no average"
  - "publication projection"
  - "repair target"
---

### C.32.ADA:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| Adequacy is coordinate-based. | Review can point to exact repairs instead of vague approval or rejection. | Evaluation takes longer than reading a record once. |
| Declared use controls stop condition. | A decision can be adequate for one use and inadequate for another without contradiction. | Teams must state intended use before scoring. |
| No average is allowed. | Weak but critical coordinates stay visible. | Some dashboards and summaries need redesign. |
| Explicit repair conditions and subject-pattern locators are mandatory. | Review results become actionable. | Reviewers must recover the exact missing assertion and the pattern description containing its definition or constraint. |

