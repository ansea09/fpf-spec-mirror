---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet"
section_id: "F.17:1"
section_title: "Intent and applicability"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__002_intent-and-applicability.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "F.17 — Unified Term Sheet"
  - "F.17:1 — Intent and applicability"
line_start: 77492
line_end: 77506
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

### F.17:1 - Intent and applicability

`UnifiedTermSheet` is a reader-facing term publication for one bounded unification thread. It gives a careful reader one compact table of reviewed term rows: the chosen Tech and Plain names, the specified governed kind or governed value, the local senses, the bridge relation when cross-context use is claimed, and the small rationale that makes the naming decision reviewable.

The pattern is useful when a team has already done enough local sense work that a name can be reused without redoing the whole unification argument each time. It is especially useful for:

- public or cross-context role names;
- status-family names and status-window labels;
- durable relation, slot, interface, or signature names;
- FPF kind names and local concept names that appear in more than one bounded context;
- term rows cited by examples, training material, project standards, or tool interfaces;
- Part G, architecture, transformation, and evaluation vocabulary where row ids must stay stable across editions.

`F.17` does not create `U.Role`, `U.Status`, `U.Evidence`, `U.Method`, `U.Work`, `U.Episteme`, `U.Relation`, `U.SlotKind`, or any other underlying object. It publishes a term row for an already governed object, relation, slot, or local concept. The direct pattern remains responsible for the object and its admissible use.

