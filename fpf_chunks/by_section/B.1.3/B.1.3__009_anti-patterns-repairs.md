---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Knowledge Aggregation (Γ_epist): Synthesis and Target-Scheme Compilation"
section_id: "B.1.3:8"
section_title: "Anti‑patterns & repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__009_anti-patterns-repairs.md"
commit_sha: "d73588bdcb52ed173d7b4c1552b2ce199a548c64"
heading_path:
  - "B.1.3 — Knowledge Aggregation (Γ_epist): Synthesis and Target-Scheme Compilation"
  - "B.1.3:8 — Anti‑patterns & repairs"
line_start: 41882
line_end: 41894
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
  - "A.7"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.3"
  - "C.11"
  - "C.19.2"
  - "C.2"
  - "C.2.1"
  - "E.17"
  - "E.24.PUB"
  - "F.6"
  - "F.9"
  - "U.Work"
keywords:
---

### B.1.3:8 - Anti‑patterns & repairs

| Anti‑pattern             | Symptom                                           | Repair                                                                                     |
| ------------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| **Unsupported folding** | Incomparable scores are averaged, minimized, maximized, or converted from F | Identify support roles, scales, dependencies, and the receiving model. If none warrants aggregation, retain separate support and a bounded synthesis; do not hide counterevidence. |
| **Provenance amnesia** | Sources, methods or SCR links disappear | Restore the provenance and reconsider affected reliance. Repeat the affected synthesis when its claims, mappings or support calculation depended on what was lost. |
| **Homonym merge** | Different concepts with the same name are silently merged | Declare the exact mapping. For cross-context meanings, identify and test the F.9 Bridge, state the bounded use and permitted loss. Decide the proposed use under its applicable correspondence and reliance rules; leave it unresolved when required grounds are unresolved. |
| **Silent semantic crossing** | Local senses or schemes are mixed without a tested correspondence and use boundary | Declare the exact mappings; for cross-context meanings identify the F.9 Bridge, separate bounded-use claim, permitted loss, and the ordinary A.10 path and same-use `RelianceDisposition`. Retain the additional B.3 result when an actual named assurance claim is current. |
| **Version soup** | Labels or time slices mix unchanged epistemes, distinct epistemes, edition continuity, publication, and Work history | Apply the C.2.1 identity triple first; test `EpistemeEditionRelation` separately; use A.14 only for a proper restriction of one unchanged episteme and A.15.1 for Work. Then aggregate only the exact recovered temporal relations the current use needs. |
| **Work stuffing** | Compute/curation cost blended into reliability | Remove the unsupported inference from resource expenditure to warrant. Use B.1.6/**Γ\_work** only when a separate resource-aggregation claim is current. |
| **Orderless proof**      | Derivation steps treated as a set                 | Add **OrderSpec**; compose with Γ\_ctx inside Γ\_epist.                                    |
| **Synergy by narrative** | A new theory or whole is claimed from explanatory gain alone | First identify the synthesized episteme through C.2.1. Open B.2 only if exact construction and identity facts leave an existing-whole versus candidate-new-whole question. |

