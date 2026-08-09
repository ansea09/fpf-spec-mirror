---
chunk_kind: "child"
pattern_id: "A.6.5"
pattern_title: "Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
section_id: "A.6.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.5/A.6.5__002_problem-frame.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "A.6.5 — Relation-Declaration Slot Discipline - SlotKind, ValueKind, RefKind, and participant-designation discipline"
  - "A.6.5:1 — Problem frame"
line_start: 18925
line_end: 18959
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

### A.6.5:1 - Problem frame

**Plain name.** Relation-declaration slot discipline.

**Use this when.** Use this pattern after the direct relation kind has been recovered and a reusable typed declaration of its participants is current for another assertion, comparison, substitution, or reference use. Typical triggers are one relation declaration reused across patterns, another relation referring to an explicitly individuated occurrence, or an engineer checking a proposed replacement participant against the declared ValueKind.

**Primary working reader and concern.** The intended reader is an engineer making one relation declaration reusable while keeping actual relation participants, the `RelationSignature` episteme, relation-participant designations in assertions or descriptions, relation obtaining, and relation occurrence identity distinct.

**Primary EntityOfConcern.** One `SlotSpec` declaration in one exact `RelationSignature`.

**First useful move.** Write the readable relation sentence, name its direct governing pattern, and identify the relation kind and relation-participant meanings. For every relation-participant meaning whose reusable typed declaration is current, add one SlotSpec to the `RelationSignature`, using the compact declaration notation `SlotSpec = <SlotKind, ValueKind, refMode>`. The angle brackets and ordered entries belong to that notation; they are not parts or participants of the world-side relation. `refMode` states how an assertion or relation-occurrence description episteme carrying a relation-participant designation denotes the actual participant; it does not turn the reference or SlotSpec into that participant. If the direct relation or its relation obtaining predicate is still unclear, stop and return to `A.6.P` or `A.6.RSIR`; declaration notation cannot recover a missing ontology.

**First-minute result.** For `Robot_7 holds InspectorRole`, use the admitted A.2.1 declaration. When reusable participant typing is current, its four SlotSpecs are `HolderSystemSlot : U.System / U.EntityRef`, `RoleValueSlot : U.Role / ByValue`, `RoleTaxonomyEpistemeSlot : U.Episteme / U.EpistemeRef`, and `EffectiveReferenceSchemeSlot : U.ReferenceScheme / ByValue`. A current assertion designates those participants and states its `AssignmentInterval` separately. Stop there unless later work must substitute a participant or distinguish this assignment episode from another.

**What goes wrong if missed.** In `Robot_7 holds InspectorRole`, the holder system, the role value, the declaration-local SlotKind, and a participant designation carried by an assertion episteme can collapse into one word such as "role" or "holder". A later claim then cannot tell what may be substituted, what retains identity, or whether it refers to a system, a role value, an assignment occurrence, or an assertion about that occurrence.

**What this buys.** Engineers retain a readable relation sentence while its load-bearing uses gain exact participant typing, unambiguous reference use, and a clear return to the pattern that governs predicate truth and occurrence identity.

**Not this pattern when.** Use `A.6.P` or `A.6.RSIR` first while the relation kind or its participants remain unresolved. Use `A.6.REL` for relation-occurrence identity, `A.6.0` for the containing `U.Signature`, `C.2.1` for an assertion or description, and `C.3` for a local kind needed by typed quantification. In every other case, select the pattern governing the direct relation before applying this slot discipline.

Select A.6.5 by the engineering use, not by a domain catalogue: one already recovered direct relation needs reusable participant typing in assertions or occurrence descriptions. Its `RelationSignature` contains one SlotSpec for each participant meaning actually reused, with a declaration-local SlotKind, the participant's exact ValueKind, and one designation mode. The worked cases below are contrasts only; none supplies another relation's predicate or owner.

The following governed objects meet at this boundary and remain distinct:

1. an obtaining relation occurrence in the world;
2. the direct relation kind and its predicate;
3. a `RelationSignature` episteme whose content includes SlotSpecs corresponding to the direct relation's relation-participant meanings and restates its predicate, applicability, and identity rule for reuse;
4. a `SlotSpec` containing the declaration-local SlotKind name for one relation-participant meaning, its actual-participant ValueKind, and its designation mode;
5. an assertion or other episteme claiming that the relation obtains.

Use the `A.6.REL` relation-object architecture. A **relation-participant meaning** is the relation-local semantic content specifying one domain contribution to the obtaining predicate. An **actual relation participant** is the concrete entity participating in an obtaining occurrence under that meaning while retaining its intrinsic kind. A `SlotSpec` is declaration content corresponding to the relation-participant meaning. A **relation-participant designation** is the value or governed reference carried by an assertion or relation-occurrence description episteme to denote the actual participant. Source-specific vocabulary keeps its meaning inside the source representation or ontology until an explicit correspondence relates it to the named FPF object.

The RelationSignature and SlotSpecs are declaration content about reusable relation semantics. The world-side relation obtains under its direct predicate and identity rule independently of those epistemes.
In Tech register, `SlotKind` is the declaration-local kind by which one `RelationSignature` distinguishes a relation-participant meaning. World-side relation prose names the meaning and actual participant directly; the relation occurrence contains no SlotKind. In an assertion or relation-occurrence description episteme, the corresponding SlotSpec distinguishes a relation-participant designation carried by value or by a reference of the declared RefKind. External representation elements retain their source-specific names. A declared correspondence must relate such an element to a named SlotSpec before an FPF relation claim can reuse it.

