---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__007_bias-annotation.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:6 — Bias-Annotation"
line_start: 65459
line_end: 65469
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.21"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
  - "G.5"
keywords:
  - "ArchitectureDecisionRelation@Project"
  - "accepted loss"
  - "affected selected structure"
  - "architect-developer split"
  - "architecture-characteristic trade-off"
  - "method-use instruction"
  - "project architecture decision"
  - "reopen condition"
  - "selected architecture option"
---

### C.32.PAD:6 - Bias-Annotation

| Risk handled | How C.32.PAD handles it |
|---|---|
| Record-before-decision drift | The pattern requires `ArchitectureDecisionRelation@Project` before ADR-like publication projection. |
| Description-as-decision drift | Architecture descriptions remain `C.30.AD` objects; PAD records the decision relation that may cite them. |
| Metric-winner drift | Eval readings and metrics can inform trade-offs but do not select or decide by themselves. |
| Method-structure collapse | Method-use instructions and intended target structures are both recorded and kept distinct. |
| Work-split loss | Architect-owned structures, developer-owned refinement, and source-return conditions are explicit. |
| Evolution lock-in | Supersession and reopen conditions are part of the decision relation. |

