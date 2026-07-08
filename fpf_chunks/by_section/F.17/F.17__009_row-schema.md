---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:7"
section_title: "Row schema"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__009_row-schema.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:7 — Row schema"
line_start: 86768
line_end: 86791
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

### F.17:7 - Row schema

Use these columns unless the sheet has a justified specialization.

| Column | Required | Meaning |
| --- | --- | --- |
| `UTSRowId` | yes | Stable row id. It survives row movement between blocks. |
| `Block` | yes | Didactic block name. It has no subtype force. |
| `Governed kind or value` | yes | Exact FPF kind, local concept, relation kind, slot kind, role, status family, characteristic, or other governed value. |
| `Direct pattern` | yes | Pattern that governs the underlying object or claim. |
| `Unified Tech name` | yes | Technical name selected under `F.5` and `F.18`. |
| `Unified Plain name` | yes | Plain-language twin selected under `F.5` and `F.18`. |
| `NameCardRef` | when durable naming is current | Link to the `F.18` name-card decision. |
| `SenseCells` | yes | Local senses by bounded context and edition. |
| `BridgeRefs` | when cross-context use is current | `F.9` bridge ids with congruence level and loss note. |
| `Row rationale` | yes | One sentence explaining why this row is one term decision. |
| `Admissible use` | yes | What this row may be cited for. |
| `Not this use` | yes | The most tempting blocked use or misuse that this row does not permit. |
| `Row edition` | yes | Edition of the row. |
| `Currentness condition` | yes | What direct-pattern or source change requires row review. |
| `Notes` | optional | Short teaching or homonym warning only. |

For `SenseCells`, cite the bounded context and edition. If the source is a publication or source text, cite the source through the source-governing pattern; do not let the source title substitute for the local sense.

