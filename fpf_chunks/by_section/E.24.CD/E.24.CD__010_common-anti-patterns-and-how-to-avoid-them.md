---
chunk_kind: "child"
pattern_id: "E.24.CD"
pattern_title: "Ontic Candidate Detection and First-Use Disposition"
section_id: "E.24.CD:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24.CD/E.24.CD__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "E.24.CD — Ontic Candidate Detection and First-Use Disposition"
  - "E.24.CD:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 85765
line_end: 85778
dependencies:
  - "A.1"
  - "A.14"
  - "A.15.1"
  - "A.19"
  - "A.19.ECS"
  - "A.3.4"
  - "A.6.0"
  - "A.6.5"
  - "A.6.F"
  - "A.6.P"
  - "A.6.RCD"
  - "A.6.RSIR"
  - "B.1"
  - "B.2"
  - "C.13"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.22.2"
  - "C.22.PFR"
  - "C.28"
  - "C.29"
  - "C.3"
  - "C.3.1"
  - "C.3.2"
  - "E.10"
  - "E.10.ARCH"
  - "E.17.0"
  - "E.18.1"
  - "E.23"
  - "E.24"
  - "E.24.PUB"
  - "E.24.UK"
  - "F.18"
  - "U.CharacteristicSpace"
keywords:
---

### E.24.CD:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Card-to-kind jump | A useful card is promoted into a `U.*` kind because it has repeated fields. | Recover its claims, subject, form, and carrier; use C.2.1 or E.24.PUB as triggered. |
| Structural U-kind jump | A heading, title, filename, or ToC row keeps `U.*` because the spelling is convenient. | Recover the subject and use E.24.UK for the admission question; naming follows the result. |
| Column-to-participant jump | A field label is treated as a relation-participant meaning, or a filled field as an actual participant; either is called a `SlotSpec` because of column position. | Recover the direct predicate, its relation-participant meanings, and its actual participants first. Keep the field as a representation element or participant designation; under `A.6.5`, declare a `SlotSpec` only inside a needed `RelationSignature` for that already recovered relation. |
| One-word candidate | A broad word is renamed and treated as settled. | Recover the subject and predicate; use E.10 and E.10.ARCH when only wording remains. |
| Local-kind inflation | A useful project criterion is promoted to durable public ontology. | Use C.3.2 and keep the local kind, declaration, judgment, and extension distinct. |
| Registry trap | The author keeps a list of possible ontics without deciding the blocked case. | State the work, apply one truthful governing pattern or name one precise unresolved stop, and stop. |
| Scoring before identity | A score form is filled before the subject and direct relation gap are known. | Recover the subject, identity rule, dependent uses, and missing coordination; use A.19.ECS only for an actual comparison. |
| Repetition-as-admission | Several forms or patterns share a label, so an ontic is inferred. | Require the E.24 entry facts: one subject identity and minimal relation set reused by named dependent patterns. |
| Negative-catalogue repair | The text lists only what the candidate is not. | State the positive subject, claim, governor, next action, and one blocked stronger reading. |

