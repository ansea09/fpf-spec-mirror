---
chunk_kind: "child"
pattern_id: "F.15"
pattern_title: "SCR/RSCR Harness for Unification"
section_id: "F.15:7"
section_title: "Solution overview — the harness as a lattice of checks"
source_path: "FPF-Spec.md"
output_path: "by_section/F.15/F.15__008_solution-overview-the-harness-as-a-lattice-of-checks.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "F.15 — SCR/RSCR Harness for Unification"
  - "F.15:7 — Solution overview — the harness as a lattice of checks"
line_start: 73289
line_end: 73296
dependencies:
  - "B.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.1-F.14"
  - "F.14"
keywords:
  - "SenseCell testing"
  - "acceptance tests"
  - "regression tests"
  - "static checks"
  - "validation"
---

### F.15:7 - Solution overview — the harness as a lattice of checks

The harness arranges checks in three clusters:

* **S‑Local.** context‑local sanity (anchoring, clustering, two‑register labels).
* **S-Cross.** Cross-artefact coherence (row reuse, single-cell **Role Description**, bridge discipline, window honesty).
* **R‑Evo.** Evolution continuity (no silent rewrites, no vocabulary creep, bridge re‑validation).

