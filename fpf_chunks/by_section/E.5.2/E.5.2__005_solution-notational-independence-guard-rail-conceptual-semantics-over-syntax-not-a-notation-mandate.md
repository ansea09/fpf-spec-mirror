---
chunk_kind: "child"
pattern_id: "E.5.2"
pattern_title: "Notational Independence"
section_id: "E.5.2:4"
section_title: "Solution — Notational Independence Guard‑Rail (conceptual; semantics over syntax; not a notation mandate)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.2/E.5.2__005_solution-notational-independence-guard-rail-conceptual-semantics-over-syntax-not-a-notation-mandate.md"
commit_sha: "886e84cadcc302e1c622aec02a0a0ba1e1c3955d"
heading_path:
  - "E.5.2 — Notational Independence"
  - "E.5.2:4 — Solution — Notational Independence Guard‑Rail (conceptual; semantics over syntax; not a notation mandate)"
line_start: 73094
line_end: 73115
dependencies:
  - "E.5"
keywords:
  - "BPMN"
  - "UML"
  - "diagram"
  - "notation"
  - "semantics"
  - "syntax"
  - "tool-agnostic"
---

### E.5.2:4 - Solution — Notational Independence Guard‑Rail *(conceptual; semantics over syntax; not a notation mandate)*

1. **Semantics primacy**
   Normative content **SHALL** define concepts in linguistic form first
   (plain English + mathematics if needed). Visual or syntax examples
   are secondary illustrations.

2. **Equivalence clause**
   When an official alternate notation exists, the pattern must state:
   *“Representation A and Representation B are semantically equivalent
   under mapping M.”*

3. **Reference indirection**
   If the Core cites a diagram, it does so by *conceptual role*
   (“reference boundary schematic”) rather than by file or syntax name.

4. **Conceptual prefix neutrality**
   FPF **conceptual prefixes** (e.g., `U.`, `Γ_`, `ut:`, `tv:`, `ev:`, `mero:`) are  **cognitive namespaces**, not syntax tokens. Core patterns **MUST NOT**  tie their meaning to any concrete serialisation or URI scheme for these prefixes; any expansions are **illustrative only** and live in Tooling or Pedagogy.

5. **Cards and other "forms"**
Cards, tables and other "forms" are specified in the FPF Core only as conceptual models, not as data models; they do not require data-related or lint-specific notation. Conformance checklists and guards are also conceptual. Argumentation such as "this will ease machine checking" is forbidden; no machine checking is intended in the Core. Machine checks and linters live only in Tooling.

