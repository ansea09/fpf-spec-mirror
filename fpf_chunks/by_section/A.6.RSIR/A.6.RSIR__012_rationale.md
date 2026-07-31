---
chunk_kind: "child"
pattern_id: "A.6.RSIR"
pattern_title: "Relation, Signature, Interface, Role, and Slot Precision Restoration"
section_id: "A.6.RSIR:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.RSIR/A.6.RSIR__012_rationale.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.6.RSIR — Relation, Signature, Interface, Role, and Slot Precision Restoration"
  - "A.6.RSIR:10 — Rationale"
line_start: 17289
line_end: 17296
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
  - "E.17"
  - "F.10"
  - "F.18"
  - "F.19"
  - "G.6"
keywords:
  - "API"
  - "RelationSignature"
  - "SlotSpec"
  - "actual participant"
  - "assertion or description designation"
  - "direct relation participant"
  - "exact operation application and binding"
  - "interface"
  - "operation argument or result declaration"
  - "participant meaning"
  - "port"
  - "reduced-use source label"
  - "relation-signature-interface-role-slot recovery"
  - "representation position and correspondence"
  - "role"
  - "role assignment"
  - "shadow ontology"
---

### A.6.RSIR:10 - Rationale

The RSIR cluster needs a first-level pattern because `E.10` should remain a trigger and lexical-governance pattern, while `A.6.P`, `A.6.5`, `A.6.M`, `A.6.F`, `A.2`, `A.15`, and publication, evidence, and status patterns each govern only their respective objects.

The main ontological principle is participant, declaration, application and binding, assertion and designation, and representation separation. An actual direct-relation participant retains its direct kind under one participant meaning. A corresponding `SlotSpec`, when reusable typed relation declaration is current, states a declaration-local `SlotKind`, exact `ValueKind`, and `refMode`. In an assertion or description, `C.2.1` governs the episteme's identity and content, the direct claim family governs predicate, polarity, or use, and `A.6.5` governs participant-designation typing only against a compatible current `SlotSpec`; an ordinary assertion can name actual participants without one. An A.6.1 `ArgumentDeclaration` or `ResultDeclaration` states reusable operation meaning, while one exact application and obtaining binding relate that independently identified occurrence to an actual bound value. A C.29 representation position may correspond to any of those meanings without becoming the participant, declaration, application, or binding.

The second principle is direct governance. Once the current object is recovered, the pattern that governs that object governs the repair. RSIR only identifies the direct governing pattern.

