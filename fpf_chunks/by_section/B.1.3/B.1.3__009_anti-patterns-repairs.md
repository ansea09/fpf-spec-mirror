---
chunk_kind: "child"
pattern_id: "B.1.3"
pattern_title: "Γ_epist - Knowledge‑Specific Aggregation"
section_id: "B.1.3:8"
section_title: "Anti‑patterns & repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.3/B.1.3__009_anti-patterns-repairs.md"
commit_sha: "205de763b710fe9f2baecbcdae132ec8fdbbe38c"
heading_path:
  - "B.1.3 — Γ_epist - Knowledge‑Specific Aggregation"
  - "B.1.3:8 — Anti‑patterns & repairs"
line_start: 30414
line_end: 30426
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "C.2"
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
| **Homonym merge**        | Different concepts with same name silently merged | Insert **mapping edges** with CL; if CL too low, split by context or mark **provisional**. |
| **Context hop**          | Mixed units/vocabularies without declaration      | Declare **bounded context** and mappings; if purpose changes, use **MHT**.                 |
| **Version soup**         | Mixed time slices without clarity                 | Use **Γ\_time** to slice; compose current slice only; link others explicitly.              |
| **Work stuffing**        | Compute/curation cost blended into reliability    | Move costs to **Γ\_work**; keep R based on evidence, not spend.                            |
| **Orderless proof**      | Derivation steps treated as a set                 | Add **OrderSpec**; compose with Γ\_ctx inside Γ\_epist.                                    |
| **Synergy by narrative** | “New theory” claimed without BOSC evidence        | If closure/supervision actually emerges, declare **MHT**; otherwise lower claims.          |

