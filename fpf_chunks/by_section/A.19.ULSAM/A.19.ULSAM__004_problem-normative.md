---
chunk_kind: "child"
pattern_id: "A.19.ULSAM"
pattern_title: "Unified Lawful Scale Aggregation Mechanism (ULSAM)"
section_id: "A.19.ULSAM:2"
section_title: "Problem (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ULSAM/A.19.ULSAM__004_problem-normative.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.19.ULSAM — Unified Lawful Scale Aggregation Mechanism (ULSAM)"
  - "A.19.ULSAM:2 — Problem (normative)"
line_start: 26991
line_end: 27001
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.19.UINDM"
  - "A.19.ULSAM"
  - "A.19.USCM"
keywords:
  - "CG-Spec.SCP"
  - "CG-Spec.Γ_fold"
  - "MinimalEvidence"
  - "fold_Γ?"
  - "lawful aggregation"
  - "scale-lawful fold"
  - "tri-state guard (pass"
  - "ΓFoldRef"
---

### A.19.ULSAM:2 - Problem (normative)

How do we define an aggregation step that:
1) is **explicit** (separate from scoring/comparison/selection),
2) is **scale-lawful** and legality-gated (`CSLC` + `CG‑Spec.SCP`),
3) is **Γ‑fold-policy-bound** (`CG‑Spec.Γ_fold` or explicit override),
4) is **evidence-gated** with tri‑state guards (no `unknown → 0/false` coercions),
5) is **auditable** (editions, effective fold, contributor surface),
6) preserves **kernel stability** while allowing SoTA evolution via wiring,
7) remains **didactically readable** (one governing pattern; no scavenger hunt).

