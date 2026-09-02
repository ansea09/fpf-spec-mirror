---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
section_id: "A.6.5:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__012_sota-echoing.md"
commit_sha: "421266f0a37ab295b1ffd9e214ace6541e21f5be"
heading_path:
  - "A.6.5 — Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
  - "A.6.5:11 — SoTA-Echoing"
line_start: 19513
line_end: 19523
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

### A.6.5:11 - SoTA-Echoing

| Current line | What it contributes | FPF adoption and practical effect |
|---|---|---|
| [Lean 4 reference: structures and fields](https://lean-lang.org/doc/reference/latest/The-Type-System/Inductive-Types/) | The current official Lean language reference makes each structure field and its type explicit; a later field type may depend on an earlier field. | **Adapt as a formal stress test.** In a SlotSpec, the declaration-local SlotKind and exact participant ValueKind are explicit. FPF does not infer that a Lean structure is a world-side relation or ontic. This disciplines the formal reduced case in A.6.5:5.5, where operand order remains local to the mathematical representation and an explicit correspondence relates operands to `RelationSignature` SlotSpecs before FPF reuse. |
| [TypeDB `relates` statement](https://typedb.com/docs/typeql-reference/statements/relates/) | In current TypeDB 3.x syntax, each external role type is declared through a named relation type, with explicit scope when equal labels occur under different relation types. | **Adapt the declaration locality.** FPF uses `SlotKind`, not `SystemRole`, for the declaration-local name of a participant meaning inside a `RelationSignature`; the exact system-role kind remains the by-value participant under a direct assignment species' `AssignedSystemRoleKindSlot`, and occurrence identity remains with A.2.1 rather than storage identity. This prevents `HolderSystemSlot`, `AssignedSystemRoleKindSlot`, and `InspectorSystemRole` from collapsing in A.6.5:5.1. |
| [RDF 1.2 Concepts](https://www.w3.org/TR/rdf12-concepts/) | The RDF 1.2 Candidate Recommendation of 7 April 2026 distinguishes triple terms, propositions, asserted triples, and reifiers used in further statements. | **Adopt the separation.** A graph term or reifier may represent an assertion, but it does not replace the world-side relation, direct obtaining condition, or SlotSpec. This is the boundary exercised by the episteme case in A.6.5:5.3. |
| Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint | The current comparison line exposes relation aspects, reification choices, and higher-order typing pressure. | **Use as a stress comparator.** Keep relation occurrence, signature, assertion, and local typed projection distinct without importing the source taxonomy as FPF ontology. This tests the three-way dispatch in A.6.5:4.6 and the result-qualification case in A.6.5:5.4. |

Reopen only the affected rule or worked case when a current source revises a premise used here: declaration locality or field typing; the separation of an assertion, reifier, or representation from the world-side relation; or the higher-order-typing stress on the three-way dispatch. A newer edition by itself does not reopen the pattern.

