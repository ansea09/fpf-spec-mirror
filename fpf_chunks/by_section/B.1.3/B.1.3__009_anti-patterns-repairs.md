---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:8"
section_title: "Anti‑patterns & repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__009_anti-patterns-repairs.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:8 — Anti‑patterns & repairs"
line_start: 37174
line_end: 37186
dependencies:
  - "A.1"
  - "A.10"
  - "A.12"
  - "A.13"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "A.15.PROD"
  - "A.6.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.2"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
  - "U.Work"
keywords:
  - "KD-CAL"
  - "epistemic"
  - "knowledge aggregation"
  - "provenance"
  - "trust"
---

### B.1.3:8 - Anti‑patterns & repairs

| Anti‑pattern             | Symptom                                           | Repair                                                                                     |
| ------------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Truth‑averaging**      | Averaging confidence of conflicting claims        | Apply **pathwise min** with **CL** penalties; separate scopes or mark **provisional**.     |
| **Provenance amnesia**   | Sources/methods disappear in the aggregate        | Rebuild **SCR**; re‑run Γ\_epist with provenance union.                               |
| **Homonym merge** | Different concepts with the same name are silently merged | Declare the exact mapping. For cross-context meanings, identify and test the F.9 Bridge, state the bounded use and permitted loss, and keep low-CL or unresolved uses separate or **provisional**. |
| **Silent semantic crossing** | Local senses or schemes are mixed without a tested correspondence and use boundary | Declare the exact mappings; for cross-context meanings identify the F.9 Bridge, separate bounded-use claim, permitted loss, and any relied-on A.10 or B.3 result. |
| **Version soup** | Labels or time slices mix unchanged epistemes, distinct epistemes, edition continuity, publication, and Work history | Apply the C.2.1 identity triple first; test `EpistemeEditionRelation` separately; use A.14 only for a proper restriction of one unchanged episteme and A.15.1 for Work. Then aggregate only the exact recovered temporal relations the current use needs. |
| **Work stuffing**        | Compute/curation cost blended into reliability    | Move costs to **Γ\_work**; keep R based on evidence, not spend.                            |
| **Orderless proof**      | Derivation steps treated as a set                 | Add **OrderSpec**; compose with Γ\_ctx inside Γ\_epist.                                    |
| **Synergy by narrative** | A new theory or whole is claimed from explanatory gain alone | First identify the synthesized episteme through C.2.1. Open B.2 only if exact construction and identity facts leave an existing-whole versus candidate-new-whole question. |

