---
chunk_kind: "child"
pattern_id: "E.24"
pattern_title: "U.Ontic and Ontic Introduction Discipline"
section_id: "E.24:5.7"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.24/E.24__012_rationale.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "E.24 — U.Ontic and Ontic Introduction Discipline"
  - "E.24:5.7 — Rationale"
line_start: 73744
line_end: 73759
dependencies:
  - "A.15"
  - "A.19.ECS"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "A.6.5"
  - "B.3.5"
  - "C.13"
  - "C.2.1"
  - "C.2.P"
  - "C.2.P.DR"
  - "C.27.TA"
  - "C.29"
  - "C.30.STRAT"
  - "E.10"
  - "E.10.ARCH"
  - "E.14"
  - "E.18"
  - "E.2.DA"
  - "E.20"
  - "E.21"
  - "E.24.CD"
  - "E.24.PUB"
  - "E.24.UK"
  - "E.8"
  - "E.9"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.24:5.7 - Rationale

FPF needs a pattern for ontic introduction because many important FPF ontology units are not one term, one field, one taxonomy branch, or one U-kind. They are small typed slot relations with identity criteria, slots, admissible values, record or publication species, dependent patterns, and action-facing use boundaries.

The compactness gain is the central reason for `U.Ontic`. A taxonomy-heavy design tends to create a new type for each contextual position: reviewer, evidence reviewer, architecture reviewer, work reviewer, mechanism reviewer; method, mechanism, procedure, process, algorithm; record, evidence record, gate record, authority record. An ontic design instead keeps a small number of governed ontology units and lets many objects fill typed relation slots. A relation slot works like a parameter position in a relation-function: the value is typed and constrained by the slot, but it does not become a new kind merely because it fills that position.

`U.Episteme` is the main stress case inside FPF. `C.2.1` does not define epistemes by a long taxonomy of descriptions. It defines stable identity and a small slot relation: EntityOfConcernSlot, claim graph, viewpoint, reference scheme, grounding, publication-form and source boundaries, and dependent episteme patterns plus publication patterns. The same small slot relation can hold many claim kinds, descriptions, views, publications, and project cases without minting a new episteme kind for each one.

Role participation is the second stress case. It is not the claim that roles are slots, slots are roles, or role is a special case of slot. `U.Role` remains useful because holons participate in contexts under context-bound role values, and `U.RoleAssignment` remains useful because the assignment binds holder, role, context, and window before work can be enacted through that assignment. The compactness gain comes from representing `U.RoleAssignment` as a typed relation with slot positions while preserving the governing kinds of the filled holon, role, context, window, method, plan, and work values.

This prevents a separate ontology for every participation name while preserving the real action-facing gain of the role patterns. "Engineer", "reviewer", "evidence reviewer", and "operator" do not become new system kinds merely because they appear in project language. They are recovered, when the case requires it, as role values and assignment relations under A.2, A.2.1, and A.15. Conversely, arbitrary relation participants such as a transformed television, an evidence target, an input, an output, a base, or a dependent are slot fillers or relation participants under their governing patterns, not `U.Role` values merely because ordinary language can say they "play a role."

Without E.24, FPF ontology development oscillates between two bad moves. One move invents a new umbrella name and leaves the mixed ontology intact. The other refuses the new name but still leaves several patterns carrying duplicated local slot doctrine. E.24 gives a bounded authoring decision: use an existing governing pattern, introduce a durable ontic, keep a local use frame local, or keep the source label quote-only or reduced-use.

The pattern is deliberately about the introduction decision. It does not define every ontic and does not become a registry of system, episteme, method, mechanism, architecture, source, quality, temporal, dynamics, or change objects. Each accepted subject matter still needs its own governing pattern or accepted local frame.

