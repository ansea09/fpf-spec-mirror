---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__012_sota-echoing.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:11 — SoTA-Echoing"
line_start: 58465
line_end: 58473
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

### E.9.DA:11 - SoTA-Echoing

| Claim | Practice basis | Local adoption |
|---|---|---|
| DRR adequacy is decision-content adequacy, not template completeness. | Architecture-description and ADR traditions keep concerns, alternatives, decisions, rationale, and consequences inspectable. | The `DRR` must carry selected answers, alternatives, consequences, and selected-locus decisions. |
| Multi-host FPF changes need selected-locus disposition. | Lightweight ADR practice is useful but too central-record-oriented for multi-pattern FPF changes. | `DRRSelectedLocusDispositionMap` states obligations and non-obligations by locus. |
| Source evidence must mutate the decision. | Current FPF `E.8`, `E.19`, `E.21`, and living-source discipline require non-decorative source use. | `SoTAAndEvidenceUseInDecision` checks changed decision payload, not citation presence. |
| Quality improvement remains multi-coordinate. | MCDA, Pareto, Goodhart, and QD lines inherited through `E.22`/`E.23` show why one visible value is insufficient. | The evaluation asks what became worse and keeps repeated improvement outside `E.9.DA`. |

