---
chunk_kind: "child"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: "E.24:5.7"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24/E.24__012_rationale.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
  - "E.24:5.7 — Rationale"
line_start: 86785
line_end: 86797
dependencies:
  - "A.19.ECS"
  - "A.6.0"
  - "A.6.3"
  - "A.6.5"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.14"
  - "E.17.0"
  - "E.21"
  - "E.24"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "U.View"
keywords:
---

### E.24:5.7 - Rationale

FPF needs a pattern for ontic introduction because many important ontology units require one exact identity rule and several direct relation patterns to remain coherent. The repair is not to make one record-shaped episteme or universal head relation stand in for every nearby object. It is to give the ontic stable identity, state the smallest independently governed relation set needed by dependent use, single out an identity-bearing relation only when the subject's direct owner does, and add RelationSignature declarations only where dependent uses need them.

`U.Episteme` is the main stress case. C.2.1 identifies one episteme through claim content, exact EntityOfConcern, and effective reference scheme, while separate direct relations govern grounding and edition continuity. A `RelationSignature` declares reusable participant typing only when another use needs it. If a card is current, classify its actual use through `E.24:4.3a`; neither its layout nor its publication makes the episteme's claims true.

Role assignment is the second stress case. `U.Role` remains a work-facing role value, and generic `U.RoleAssignment` is a direct relation occurrence with exactly four participants: an admitted `U.System` holder, one `U.Role` value, the identified role-taxonomy episteme, and the effective `U.ReferenceScheme`. A.2.1 states obtaining and occurrence identity; its `RelationSignature` declares four SlotSpecs corresponding to those four relation-participant meanings for repeated assertion and reference use. `AssignmentInterval` belongs to an assertion or occurrence description. A selected `BoundedModelUseStructure` belongs to the receiving assertion or use unless a separately governed narrower relation kind makes it a required participant and states the stronger predicate.

This preserves ontology compactness without inventing a new kind for every participation name. Use `U.Role` only for a work-facing role value assigned to an admitted `U.System`. For another relation-participant meaning, the direct relation pattern states that meaning and the admitted actual-participant kind; a reusable `RelationSignature` may declare the corresponding SlotKind without changing the actual participant's kind.
Without E.24, FPF ontology development oscillates between two bad moves. One move invents a new umbrella name and leaves the mixed ontology intact. The other refuses the new name but still leaves several patterns carrying duplicated local slot doctrine. E.24 gives a bounded ontology decision: use an existing governing pattern, introduce a durable ontic, state only the needed claims in a bounded local episteme under C.2.1, or stop unresolved. A separate source-use status preserves or strengthens the source relation without replacing that ontology decision.

The pattern is deliberately about the introduction decision. It does not define every ontic and does not become a registry of system, episteme, method, mechanism, architecture, source, quality, temporal, dynamics, or change objects. Each accepted subject matter still needs its own governing pattern; a bounded local episteme may carry claims for one declared use but does not govern the ontology.

