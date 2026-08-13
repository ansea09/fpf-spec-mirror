---
chunk_kind: "child"
pattern_id: "A.6.RSIR"
pattern_title: "Relation, Signature, Interface, Role, and Slot Precision Restoration"
section_id: "A.6.RSIR:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIR/A.6.RSIR__012_rationale.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.6.RSIR — Relation, Signature, Interface, Role, and Slot Precision Restoration"
  - "A.6.RSIR:10 — Rationale"
line_start: 17571
line_end: 17578
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

### A.6.RSIR:10 - Rationale

The RSIR cluster needs a first-level pattern because E.10 remains a cheap trigger scan, while direct relation, declaration, interface, system-role, Work, publication, evidence, and status patterns retain their own objects and predicates. Bare *role* first uses the thinner `E.10.ROLE` entry; RSIR receives only its direct-relation, declaration, interface, operation, or representation branch.

The main ontological principle is separation among participant, declaration, application and binding, assertion and designation, and representation. An actual direct-relation participant retains its direct kind under one participant meaning. A corresponding `SlotSpec`, when reusable typed relation declaration is current, states a declaration-local `SlotKind`, exact `ValueKind`, and `refMode`. An assertion or description remains a C.2.1 episteme; its direct claim family supplies predicate, polarity, or use, and A.6.5 types a participant designation only against a compatible current `SlotSpec`. An A.6.1 declaration states reusable operation meaning, while one exact application and obtaining binding relate that occurrence to an actual value. A C.29 representation position may correspond to any of those objects without becoming one.

The second principle is direct governance. Once the current object is recovered, the pattern that defines or constrains that object governs the repair. RSIR only identifies the subject pattern.

