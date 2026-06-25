---
chunk_kind: "child"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: "E.24:7"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24/E.24__010_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
  - "E.24:7 — Common Anti-Patterns and How to Avoid Them"
line_start: 77241
line_end: 77253
dependencies:
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "A.6.5"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.27.TA"
  - "C.29"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.14"
  - "E.18"
  - "E.2.DA"
  - "E.20"
  - "E.21"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.24:7 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Shadow-kind by repetition | The same local record appears in several patterns and starts being cited as an object. | Apply E.24; either write a durable ontic pattern or lower the construct to a local use frame. |
| Draft locus as authority | A ToC row is cited as if it supplied current governing text. | Treat it as investigation cue only; use current governing patterns until the pattern exists. |
| Slot list without identity | A pattern lists fields but never says what identifies the ontic. | Add stable identity criteria or lower the construct to a local use frame. |
| Pattern nest as ontology | The numbering area is treated as the semantic unit. | Declare `semanticArea`, `ontologicalNeighborhood`, and primary `EntityOfConcern` separately. |
| New name as solution | The repair invents a smoother term while the typed values remain mixed. | Recover kinds, slots, semantic area, and ontological neighborhood first; name only after the ontology is settled. |
| Slot-position kind inflation | A role-like, method-like, temporal, source, or publication position receives a fresh kind name only because it occupies a slot. | Keep the value's kind under its governing pattern and record the slot position separately. |
| Interface metaphor for slots | A slot relation, SlotSpec, relation position, or filler constraint is called an interface only because that word feels familiar. | Rename to the slot-language term unless a governing boundary/interface pattern makes interface meaning current. |
| Typed paraphrase overload | A readable subject sentence is rewritten as a full chain of kinds, slots, and source-ontology labels without changing the claim. | Keep the subject sentence and annotate only the decision-changing slot or value under decision. |

