---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__013_relations.md"
commit_sha: "f2fdd062c1518c9b1a1be1b6ad795627cffad2f1"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:12 — Relations"
line_start: 51058
line_end: 51070
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.22"
  - "C.22.2"
  - "E.18.1"
  - "E.23"
  - "G.11"
keywords:
  - "actual adverse condition"
  - "actual adverse episode"
  - "assessment and evidence separation"
  - "condition-to-predicate input rule"
  - "exact problem-for entity and use"
  - "independent criterion-applicability relation"
---

### C.22.PFR:12 - Relations

- `A.6.REL` governs explicit individuation of both PFR participants and PFR itself when a receiving use needs identity.
- `A.6.5` governs the two PFR participant SlotSpecs and the four applicability SlotSpecs.
- `A.19` governs the characteristic space used by `CharacteristicSpacePredicate`; the selected direct consumer governs its condition-to-input rule and comparator semantics, `A.19.CPM` governs comparison when that is the consumer, and `G.4` governs typed acceptance clauses when acceptance is the consumer.
- `C.16`, `A.18`, and direct condition or measurement patterns govern characteristics, scales, actual characteristic assignments or state relations, and measurements. F.9 governs any cross-reference-scheme bridge named by the input rule; none of these adds a PFR participant.
- `C.22` governs selector-facing task typing and TaskSignature assignment after a problem-side episteme is usable.
- `C.22.2` governs ProblemCard claims, signals, forecasts, scenarios, anticipated-condition cues, descriptions, next use, and publication without creating PFR; the exact direct claim pattern governs each claim carried there.
- `A.15.1` and `A.3.4` govern repair work and changes to the actual-condition relation.
- `E.18.1`, `E.23`, and direct NQD and OEE patterns govern repeated problematization, method search, work, evaluation, and continuation; relations locating or ordering those occurrences in a transformation-flow structure do not enter PFR identity.
- `C.27.TA` governs temporal aspect statements when interval publication or temporal adequacy is current.
- `A.10`, `B.3`, and `G.11` govern evidence use, assurance, and source or claim currentness.

