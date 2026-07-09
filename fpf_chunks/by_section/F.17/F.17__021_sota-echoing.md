---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:16"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__021_sota-echoing.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:16 — SoTA-Echoing"
line_start: 87964
line_end: 87974
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

### F.17:16 - SoTA-Echoing

| Practice family | What F.17 takes | Practical consequence |
| --- | --- | --- |
| ISO 704:2022 terminology work | A term entry separates object, concept, definition, and designation. | UTS rows keep names separate from the governed object and from source wording. |
| ISO 25964 and W3C SKOS knowledge-organization practice | Concepts, labels, notes, and typed cross-vocabulary mappings are distinct. | F.17 uses `F.9` bridge references for sameness, near-identity, and loss instead of inferring them from spelling. |
| Public naming, controlled-vocabulary, schema, or editioning practice | Public names need stability, editioning, and deprecation discipline. | UTS rows have row ids, row editions, and currentness conditions. |
| Safety and assurance writing | Reader-facing labels must not overclaim authority, evidence, or admissible use. | Each row states admissible use and the tempting misuse it blocks. |

Currentness rule: when `F.5`, `F.8`, `F.9`, `F.10`, `F.15`, `F.18`, `A.2`, `A.2.1`, `A.2.7`, `A.6.5`, `A.10`, `B.3`, `E.17`, or `E.10.D2` changes the governed value, admissible use, bridge, source-use boundary, status-family boundary, role boundary, or naming decision, recheck only the affected UTS rows and examples.

