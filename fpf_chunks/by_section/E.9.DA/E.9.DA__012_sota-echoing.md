---
chunk_kind: "child"
pattern_id: "E.9.DA"
pattern_title: "DRR Decision-Adequacy Evaluation CharacteristicSpace"
section_id: "E.9.DA:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/E.9.DA/E.9.DA__012_sota-echoing.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "E.9.DA — DRR Decision-Adequacy Evaluation CharacteristicSpace"
  - "E.9.DA:11 — SoTA-Echoing"
line_start: 69104
line_end: 69114
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
| Feedback needs desired condition, current condition, next action, and tactics. | Sadler and Hattie and Timperley feedback traditions, carried through `E.22` and `E.23`. | `ShortRationale`, evidence locus, finding and proposal rows, and checked no-proposal dispositions stay separate. |
| Source evidence must mutate the decision. | Current FPF `E.8`, `E.19`, `E.21`, and living-source discipline require non-decorative source use. | `SoTAAndEvidenceUseInDecision` checks changed decision payload, not citation presence. |
| Improvement remains multi-coordinate and trade-off sensitive. | MCDA, Pareto, and QD, OEE, and NQD lines inherited through `E.22` and `E.23`. | The evaluation asks what became worse and keeps repeated improvement outside `E.9.DA`. |
| Decision-adequacy measures can become targets. | Goodhart and Campbell, management-accounting surrogation, specification-gaming, and reward-hacking lines. | `E.9.DA` forbids all-`5` or `5-defensible` repair targeting; values rise only when decision content becomes stronger for declared authoring use, and `E.13` governs any proxy-to-value claim about those values. |

