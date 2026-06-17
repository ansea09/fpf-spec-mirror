---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__001_intro.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:intro — Intro"
line_start: 15514
line_end: 15533
dependencies:
  - "A.1"
  - "A.6.0"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "B.5"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.17.0"
  - "E.8"
  - "U.EpistemeSlotRelation"
  - "U.MultiViewDescribing"
  - "U.Signature"
keywords:
  - "argument position"
  - "pass-by-reference"
  - "pass-by-value"
  - "reference"
  - "signature"
  - "slot"
  - "substitution"
  - "value"
---

## A.6.5 - U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain name.** Relation slot discipline.

**Use this when.** Use this pattern when a relation, operator, record, episteme slot relation, signature vocabulary item, interface specification, method description, service-access description, role assignment, evidence-use relation, status-use relation, or transformation-flow structure needs named positions and typed fillers rather than a loose parameter list.

**Primary EntityOfConcern.** The EntityOfConcern is `U.RelationSlotDiscipline`: the FPF discipline for declaring the positions of a relation-bearing structure, the kinds of values admitted at those positions, and the reference or by-value mode used when a filled instance stores content.

**First useful move.** For the current relation-bearing value, name the governing pattern and write each relevant position as a `SlotSpec = <SlotKind, ValueKind, refMode>`. Then say whether the filled slot instance stores a value by value or stores a reference of a `RefKind`.

**What goes wrong if missed.** Teams treat "role", "argument", "field", "port", "parameter", "endpoint", "holder", "target", "source", "interface", or "ref" as if the word already said whether it is a position, a filler kind, a filled reference, a described object, or a neighboring relation. This creates duplicate ontology: the same project situation becomes a role in one pattern, an interface in another, a slot in a third, and an evidence relation in a fourth.

**What this buys.** A relation-bearing pattern can say exactly which slots it has, what may fill each slot, how filled instances point to or embed those fillers, and which neighboring pattern governs any role, capability, method, work, evidence, status, publication, or interface claim that appears near the relation.

**Not this pattern when.** Do not use `A.6.5` as a generic relation ontology, as a second `U.Signature`, as an interface root kind, as a role ontology, or as a universal wording-repair pattern. Use the direct governing pattern when the current question is relation identity (`A.6.P` or a relation-specific pattern), signature declaration (`A.6.0`), role value (`A.2`), role assignment (`A.2.1`), evidence use (`A.10`, `B.3`, `G.6`), status use (`F.10`), publication or view use (`E.17*`), module interface (`A.6.M` and architecture patterns), functional port or functional structure (`A.6.F`, `E.18`, architecture patterns), or wording-use triage (`E.10`, `E.10.ARCH`, `A.6.RSIR`).

