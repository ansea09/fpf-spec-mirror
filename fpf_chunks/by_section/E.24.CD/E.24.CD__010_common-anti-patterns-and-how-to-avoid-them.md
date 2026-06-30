---
chunk_kind: "child"
pattern_id: "E.24.CD"
pattern_title: "Ontic Candidate Detection"
section_id: "E.24.CD:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.CD/E.24.CD__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "E.24.CD — Ontic Candidate Detection"
  - "E.24.CD:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 79821
line_end: 79832
dependencies:
  - "A.19"
  - "A.19.ECS"
  - "A.6.5"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.2.DA"
  - "E.21"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.9.DA"
  - "F.18"
  - "F.19"
  - "U.CharacteristicSpace"
keywords:
---

### E.24.CD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Card-to-kind jump | A useful card is promoted into a `U.*` kind because it has repeated fields. | Recover the EoC and typed values; use `E.24.PUB` for publication form. |
| Structural U-kind jump | A heading, title, filename, or ToC row keeps `U.*` because it is convenient for search. | Recover the governed object and use `E.24.UK`; repair the structural name when the primary EoC is not that U-kind. |
| Table ontology by appearance | A table or schema field list is treated as a slot relation. | Ask whether the fields are publication columns, local record fields, or type-level slots with claim-impact. |
| One-word candidate | A broad word is renamed and treated as settled. | Use `E.10.ARCH` and E.24.CD together: recover typed values and slot relation before naming. |
| Registry trap | The author keeps a growing list of possible ontics without disposition. | Stop at one of the E.24.CD classifications and move to the next governing pattern. |
| Scoring before identity | A score form compares alternatives before the candidate EoC and slot relation are clear. | First write the sufficiency rationale; use `A.19.ECS` only when evaluation construction is actually current. |
| Negative-catalogue repair | The text lists neighboring EoCs only as things the candidate is not instead of naming positive values and boundaries. | Name the positive EoC, typed values, and governing patterns; keep the blocked overread to one row. |

