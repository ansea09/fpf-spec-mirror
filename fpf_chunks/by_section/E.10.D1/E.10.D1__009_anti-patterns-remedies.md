---
chunk_kind: "child"
pattern_id: "E.10.D1"
pattern_title: "Lexical Discipline for “Context” (D.CTX)"
section_id: "E.10.D1:8"
section_title: "Anti‑patterns & Remedies"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D1/E.10.D1__009_anti-patterns-remedies.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "E.10.D1 — Lexical Discipline for “Context” (D.CTX)"
  - "E.10.D1:8 — Anti‑patterns & Remedies"
line_start: 76971
line_end: 76981
dependencies:
  - "A.2.1"
  - "A.4"
  - "A.7"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.6"
  - "F.7"
  - "F.9"
keywords:
  - "U.BoundedContext"
  - "anchor"
  - "context"
  - "domain"
  - "frame"
---

### E.10.D1:8 - Anti‑patterns & Remedies

| Anti‑pattern                  | Symptom                                                           | Why harmful                          | Remedy (normative)                                                           |
| ----------------------------- | ----------------------------------------------------------------- | ------------------------------------ | ---------------------------------------------------------------------------- |
| **A1 Context-as-situation**   | “Context” used for narrative sections                             | Ambiguity                            | Use **Problem Frame**; reserve Context for `U.BoundedContext` (D‑CTX‑4).     |
| **A2 Anchor-speak**           | “role anchor”, “ontology anchor”                                   | Redundant token; hides locality      | Replace with **SenseCell** or **ConceptSet(Row).Column** (D-CTX-2, D-CTX-8). |
| **A3 Domain context**         | “Workflow domain context”, etc.                                   | Family ≠ formal context              | Use **Domain family** + explicit list of Context ids (D‑CTX‑3).              |
| **A4 Context hierarchy**      | Context A “is‑a” Context B                                        | Leaks meanings; blocks loss policies | Remove hierarchy; use **F.9 Bridge** with loss policy (D‑CTX‑6).         |
| **A5 Time‑as‑context**        | “Runtime context” vs “Design context”                             | Multiplies Contexts incorrectly         | Use **TimeScope tags** (C‑7); keep one Context (D‑CTX‑5).                    |
| **A6 Cross‑lingual blending** | Mixing language labels as one context despite divergent semantics | Hidden drift                         | Split Contexts per **D‑CTX‑7** or document shared semantics if truly bound.  |

