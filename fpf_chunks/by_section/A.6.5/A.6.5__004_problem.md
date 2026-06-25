---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
section_id: "A.6.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__004_problem.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.6.5 — U.RelationSlotDiscipline - SlotKind, ValueKind, RefKind, and slot-operation discipline"
  - "A.6.5:2 — Problem"
line_start: 15882
line_end: 15895
dependencies:
  - "A.1"
  - "A.2.1"
  - "A.6.0"
  - "A.6.2"
  - "A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.3"
  - "E.10"
  - "E.17.0"
  - "E.8"
  - "F.6"
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

### A.6.5:2 - Problem

Without a shared slot discipline, FPF texts fall into recurring category errors.

1. **Slot, value, and reference are treated as one object.** A field such as `entityOfConcernRef` is read as the slot, the described object, and the stored reference at the same time.
2. **Kernel kinds are used as slot names.** Writers say "the `U.Holon` of this relation" when they mean a local slot whose filler has ValueKind `U.Holon`.
3. **Role words become argument-position words.** "The role of the subject" or "provider role in the relation" may mean an actual `U.Role`, a local SlotKind, an evidence-use position, a service-access relation, or ordinary prose.
4. **Reference suffixes drift.** A `*Ref` token is sometimes used for a value kind, sometimes for a field, and sometimes for a slot. Downstream readers cannot tell what is being retargeted.
5. **Substitution rules cannot be localized.** If a text cannot say which SlotKind stays fixed and which ValueKind remains compatible, "replace X with Y" becomes a hand-waved compatibility claim.
6. **Interface and port wording overgeneralizes.** "Interface" may mean module interface, signature, port, protocol, API description, service-access package, or boundary claim bundle. A.6.5 helps declare slots inside those values, but it does not create a generic `U.Interface`.
7. **Evidence and status relations are mistaken for roles.** An episteme used as evidence, a standard used as a requirement, or a publication used as a status source is treated as a `U.RoleAssignment` case even though the current claim is evidence use, source use, publication use, assurance use, or status use.

The practical failure is simple: local convenience produces global incoherence.

