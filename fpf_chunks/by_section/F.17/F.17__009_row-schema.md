---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:7"
section_title: "Row schema"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__009_row-schema.md"
commit_sha: "1d5c1edd154b636a446b3887a6094be60c60faff"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:7 — Row schema"
line_start: 89761
line_end: 89786
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.SPR"
  - "A.2"
  - "A.2.1"
  - "A.2.7"
  - "A.22.CGUS"
  - "A.6.5"
  - "A.6.P"
  - "B.3"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "G.11"
keywords:
---

### F.17:7 - Row schema

Use these columns unless the sheet has a justified specialization.

| Column | Presence condition | Meaning |
| --- | --- | --- |
| `UTSRowId` | yes | Stable row id. It survives relocation of the row between blocks. |
| `Unification thread` | yes | Sheet-local identifier of the bounded naming thread; it does not replace any SenseCell bounded context. |
| `Block` | yes | Didactic block name. It has no subtype force. |
| `Governed value` | yes | Exact value being named, including a kind token when the name is for that token. |
| `Governed value kind` | yes | Exact kind of the governed value; use `U.Kind` when the governed value is itself a kind token. |
| `Direct pattern` | yes | Pattern that governs the underlying object or claim. |
| `Unified Tech name` | yes | Technical name selected under `F.5` and `F.18`. |
| `Unified Plain name` | yes | Plain-language twin selected under `F.5` and `F.18`. |
| `NameCardRef` | yes | Link to the `F.18` NameCard that selected or documented the published names. |
| `SenseCellRefs` | yes | References to local senses by bounded context and edition. |
| `BridgeRefs` | when cross-context use is current | `F.9` bridge ids with congruence level and loss note. |
| `Row rationale` | yes | One sentence explaining why this row is one term decision. |
| `Admissible use` | yes | What this row may be cited for. |
| `Not this use` | yes | The most tempting blocked use or misuse that this row does not permit. |
| `Row edition` | yes | Edition of the row. |
| `Currentness condition` | yes | Which direct-pattern or source change opens row review. |
| `Notes` | optional | Short teaching or homonym warning only. |

For `SenseCellRefs`, cite the bounded context and edition. If the local expression relies on a naming settlement, cite its `NameCardRef`. If the local sense relies on a publication or another episteme, cite a `LocalSenseBasisRelation@Context` with an exact `U.EpistemeRef` and, when needed, the exact publication-unit ref. Do not let a source title, file name, or NameCard substitute for the local sense or its basis relation.

