---
chunk_kind: "child"
pattern_id: "A.19.ULSAM"
pattern_title: "Unified Lawful Scale Aggregation Mechanism"
section_id: "A.19.ULSAM:10"
section_title: "Rationale (didactic, informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ULSAM/A.19.ULSAM__012_rationale-didactic-informative.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "A.19.ULSAM — Unified Lawful Scale Aggregation Mechanism"
  - "A.19.ULSAM:10 — Rationale (didactic, informative)"
line_start: 40264
line_end: 40272
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
  - "tri-state guard (pass\\"
  - "ΓFoldRef"
---

### A.19.ULSAM:10 - Rationale (didactic, informative)

Aggregation is a **semantic commitment**: it changes a set/vector of measures into a single measure, and therefore changes what later comparison/selection can legitimately claim. In CHR, that commitment must be explicit, admissibility-gated, and auditable.

Keeping ULSAM as its own mechanism preserves:
- the boundary between **method choice** (SoTA packs) and **operation declaration**,
- the boundary between **planned baseline** (pins chosen in WorkPlanning) and **run-time audit** (what executed),
- and the engineer-facing clarity that “we folded here, not everywhere”.

