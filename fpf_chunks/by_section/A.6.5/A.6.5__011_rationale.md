---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
section_id: "A.6.5:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__011_rationale.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "A.6.5 — Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
  - "A.6.5:10 — Rationale"
line_start: 19564
line_end: 19571
dependencies:
  - "A.15.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.P"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "C.29"
  - "C.3"
  - "E.24.UK"
keywords:
---

### A.6.5:10 - Rationale

SlotKind, ValueKind, and RefKind answer three different engineering questions about one `RelationSignature`: **which participant meaning does this declaration distinguish**, **what exact world-side kind must the corresponding actual participant have**, and **how does a receiving assertion or description episteme designate that participant**. Keeping the answers separate is enough to support typed substitution and honest reference use without adding a universal relation record.

The direct-relation definition remains essential. A pair of typed participants does not say whether the relation obtains or whether repeated occurrences with the same participants are identical. Constructive ontology therefore combines logical slot discipline with grounding and domain identity rather than treating a schema as the world.

The predicate boundary prevents a second collapse. Natural language often verbalizes relations, work, methods, and transformations. FPF admits their kinds through direct ontological tests, not through grammar. This keeps only systems as actors and as actual participants corresponding to `HolderSystemSlot`, while preserving the accepted holonhood of work and methods and the separate actual-bounded-change identity of transformations.

