---
chunk_kind: "child"
pattern_id: "A.6.RSIR"
pattern_title: "Relation, Signature, Interface, Role, and Slot Precision Restoration"
section_id: "A.6.RSIR:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIR/A.6.RSIR__009_conformance-checklist.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "A.6.RSIR — Relation, Signature, Interface, Role, and Slot Precision Restoration"
  - "A.6.RSIR:7 — Conformance Checklist"
line_start: 17043
line_end: 17056
dependencies:
  - "A.10"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.3.4.P"
  - "A.6.0"
  - "A.6.1"
  - "A.6.5"
  - "A.6.A"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.REL"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.ROLE"
  - "E.17"
  - "F.10"
  - "F.18"
  - "F.19"
  - "G.6"
keywords:
  - "API"
  - "RelationSignature"
  - "SlotSpec"
  - "ambiguous role wording"
  - "direct relation participant"
  - "interface"
  - "operation declaration and binding"
  - "participant meaning"
  - "port"
  - "reduced-use source label"
  - "relation-signature-interface-role-slot recovery"
  - "representation position"
  - "system-role assignment"
  - "system-role kind"
---

### A.6.RSIR:7 - Conformance Checklist

1. The repair starts with project concern, not with a replacement word.
2. The current EntityOfConcern or claim kind is named before a subject pattern is applied.
3. The repair stops once the applicable rule and concrete next action are clear.
4. When reusable relation declaration is current, slot discipline uses `A.6.5` and states one complete `SlotSpec = <SlotKind, ValueKind, refMode>` inside one exact `RelationSignature`; actual participants and representation positions remain outside it.
5. A system-role-assignment claim names one occurrence and its declared `U.SystemRoleAssignment` species. The species defines the participant meanings and rule; the occurrence supplies its holder, assigned local kind, and any other participant that distinguishes it. Apply the direct rule for a system-role-kind description, `SystemRoleAssignmentStateRelation`, selected structure among system-role kinds, capability, Method, planned Work, or performed Work; do not apply RSIR merely to repeat that result.
6. Evidence-use and status-use cases are not represented through `U.SystemRoleAssignment` for epistemes. Apply `E.10.ROLE` once to bare *role*; if it recovers evidence use, status use, or another direct object, apply that object's rule and leave RSIR closed.
7. Interface wording is kept as a recognition cue but is not admitted as generic `U.Interface`.
8. Every neighboring object family selected in the dispatch table uses its defining or testing rule rather than being redescribed inside RSIR.
9. Relation-defined wording dispatches separately to the direct participant meaning and actual participant; a declaration-local `SlotSpec` when reusable typing is current; an assertion- or description-side designation whose episteme identity and content stay with `C.2.1`, whose predicate, polarity, and use stay with the direct claim family, and whose typing stays with `A.6.5` only when a compatible `SlotSpec` is current; a C.3 local kind when repeated quantification is current; or a representation position plus explicit correspondence. It does not create one umbrella qualification object.
10. Operation wording keeps A.6.1 `ArgumentDeclaration` or `ResultDeclaration` content, one independently identified exact application and obtaining argument or result binding, and any call or formula representation position distinct; it infers neither a public application kind nor production, a produced entity, a result episteme, evidence, or work from the binding.
11. Quote-only or reduced-use labels carry no action-facing claim beyond the claim admitted by the selected rule.

