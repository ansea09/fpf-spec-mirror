---
chunk_kind: "child"
pattern_id: "F.17"
pattern_title: "Unified Term Sheet (UTS)"
section_id: "F.17:9"
section_title: "Invariants (normative constraints)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.17/F.17__010_invariants-normative-constraints.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "F.17 — Unified Term Sheet (UTS)"
  - "F.17:9 — Invariants (normative constraints)"
line_start: 67415
line_end: 67431
dependencies:
  - "A.1.1"
  - "A.11"
  - "A.15"
  - "A.7"
  - "A.8"
  - "E.10"
  - "E.10.D1"
  - "E.10.P"
  - "F.1"
  - "F.1-F.12"
  - "F.10"
  - "F.12"
  - "F.15"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "UTS"
  - "Unified Term Sheet"
  - "glossary"
  - "human-readable output"
  - "publication"
  - "summary table"
---

### F.17:9 - Invariants (normative constraints)

1. **Locality.** Every SenseCell is **Context‑scoped** (E.10.D1). No global synonyms.
2. **Bridges only via F.9.** Cross‑context equivalence appears **only** as an explicit Bridge with **CL**. Any row citing > 1 **Context** must state at least one Bridge.
3. **Heterogeneity.** Across the UTS, coverage must involve **≥ 3 domain families** (F.1 Step 2; A.8).
4. **Scale‑map tags (optional but disciplined).** If used in Layout B:
   * **Σ (Summative):** concept’s quantitative properties aggregate across a population of executions/holders.
   * **Π (Conjunctive/Compositional):** concept composes by required conjunction (all‑of), not by averaging.
   * **μ (Micro/Atomic):** concept is inherently micro‑level (per single execution/holder).
     *(Tags aid teaching; they do not change semantics.)*
5. **Strict Distinction.** Use `U.Method` vs `U.MethodDescription`, `U.Work` vs `U.WorkDescription`, `U.Role` vs `U.RoleCharacterisation` correctly; do **not** collapse intensional objects with their descriptions.
6. **Dual register.** Every row has **Tech** and **Plain** labels per F.5.
7. **One‑breath rationale.** The `Unification Rationale` is a **single sentence** explaining the conceptual sameness despite local wording.
8. **Unified naming neutrality.** The **Unified Tech name** is the neutral FPF choice per F.5; it is **not** lifted wholesale from any single Context unless the Concept‑Set justification (F.7) shows identity.
9. **Column discipline.** Layout A uses **Bounded‑Context Columns (BCC)** only; Layout B uses **Discipline Columns (DC)** only. Mixing is non‑conformant.
10. **Plain‑twin discipline.** The single **Unified Plain name** lives in the left rail; BCC/DC cells carry senses only. Any additional Plain aliases are managed in LEX (tv:\*) and never minted per column.

