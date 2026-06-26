---
chunk_kind: "child"
pattern_id: "E.5.2"
pattern_title: "Notational Independence"
section_id: "E.5.2:4"
section_title: "Solution — Notational Independence Guard‑Rail (conceptual; semantics over syntax; not a notation mandate)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.5.2/E.5.2__005_solution-notational-independence-guard-rail-conceptual-semantics-over-syntax-not-a-notation-mandate.md"
commit_sha: "02a8b4bac1f141b1751421bf522e9dc489ae522e"
heading_path:
  - "E.5.2 — Notational Independence"
  - "E.5.2:4 — Solution — Notational Independence Guard‑Rail (conceptual; semantics over syntax; not a notation mandate)"
line_start: 64777
line_end: 64798
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
Cards, tables and other "forms" exist in FPF core only as conceptual model, not as data model, thus no need to data-related notation or notation for lint. Comformance checklist and quards is also conceptual, argumentation like "this will ease machine check" is forbidden, no machine checking is intended in core; machine checks and linters live only in Tooling.

