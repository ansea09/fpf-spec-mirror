---
chunk_kind: "child"
pattern_id: "F.4"
pattern_title: "Role Description (RCS + RoleStateGraph + Checklists)"
section_id: "F.4:7"
section_title: "Normative invariants (template discipline)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.4/F.4__008_normative-invariants-template-discipline.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "F.4 — Role Description (RCS + RoleStateGraph + Checklists)"
  - "F.4:7 — Normative invariants (template discipline)"
line_start: 72551
line_end: 72563
dependencies:
  - "A.11"
  - "A.2.1"
  - "A.7"
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "E.10.D2"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.RoleAssignment"
  - "U.Types"
keywords:
  - "Role Characterisation Space (RCS)"
  - "RoleStateGraph (RSG)"
  - "invariants"
  - "role template"
  - "status template"
---

### F.4:7 - Normative invariants (template discipline)

1. **context‑local grounding.** Every Role Description **MUST** cite exactly one **SenseCell** as its semantic anchor.
2. **EntityOfConcern / Description / specification-use separation.**
   * A **Role Template** **MUST NOT** encode deontic, access, or measurement rules.
   * A **Status Template** **MUST NOT** encode behaviour or control flow.
3. **Time honesty.** The card’s stance (**DesignRunTag**) **MUST** match the Context’s stance (F.1).
4. **Minimality.** Invariants **SHOULD** be the **fewest that decide** the assignment; avoid procedural sequences.
5. **No Cross‑context smuggling.** A single card **MUST NOT** import foreign semantics; if two Contexts are needed, the relation is handled later in **F.9**.
6. **Label fidelity.** **Tech** label **MUST** be idiomatic to the Context; **Plain** label **MUST** not widen the sense (F.3).
7. **Binding Standard (roles).** A **Role Template** is the **design‑time mask**; at run‑time, a **`U.RoleAssignment`** creates **System‑in‑Role** instances that are subject to the card’s invariants.
8. **Assertion Standard (statuses).** A **Status Template** is a **badge**; asserting it **commits** to the card’s evaluation invariants and to the Context’s way of checking them (later anchored via SenseCells, not formulas here).

