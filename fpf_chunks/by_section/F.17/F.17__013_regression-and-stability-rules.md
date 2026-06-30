---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:11"
section_title: "Regression and stability rules"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__013_regression-and-stability-rules.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:11 — Regression and stability rules"
line_start: 86576
line_end: 86588
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "UTS"
  - "Unified Term Sheet"
  - "glossary"
  - "human-readable output"
  - "publication"
  - "summary table"
---

### F.17:11 - Regression and stability rules

Recheck only the rows affected by the changed object, name, bridge, or source.

| Rule | Trigger | Required response |
| --- | --- | --- |
| UTS-RSCR-01 | Bounded context edition changes | Keep old sense cells addressable and add or revise cells for the new edition. |
| UTS-RSCR-02 | Direct governing pattern changes the underlying object kind or admissible use | Recheck governed kind or value, direct pattern, admissible use, and blocked use. |
| UTS-RSCR-03 | `F.18` changes the selected name or name-card decision | Recheck Tech name, Plain name, NameCardRef, aliases, and rationale. |
| UTS-RSCR-04 | `F.9` changes bridge kind, congruence level, loss, or direction | Recheck BridgeRefs, row rationale, and cross-context use. |
| UTS-RSCR-05 | Row movement between blocks | Keep row id stable and state that block movement has no ontological force. |
| UTS-RSCR-06 | A role, status, evidence, source, publication, or description row is reused in another context | Recheck the direct governing pattern and the bridge before reuse. |

