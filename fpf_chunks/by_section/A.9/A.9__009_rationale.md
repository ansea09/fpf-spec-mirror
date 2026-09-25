---
chunk_kind: "child"
pattern_id: "A.9"
pattern_title: "Choose and Check an Aggregation Law for the Intended Result"
section_id: "A.9:8"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.9/A.9__009_rationale.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "A.9 — Choose and Check an Aggregation Law for the Intended Result"
  - "A.9:8 — Rationale"
line_start: 24071
line_end: 24076
dependencies:
  - "A.19.CN"
  - "A.19.ULSAM"
  - "B.1"
  - "B.2"
  - "C.29"
keywords:
  - "aggregation law"
  - "bounds"
  - "cross-scale consistency"
  - "dependency model"
  - "intended result"
  - "ordered composition"
  - "singleton identity"
---

### A.9:8 - Rationale

A common Γ notation locates a construction but cannot choose between joint success, alternative success, additive accounting and ordered composition. Those results have different laws even when some inputs or symbols coincide. Selecting the receiving meaning before the operation prevents a syntactically valid calculation from answering the wrong question.

Checking only the needed property also keeps the burden proportionate. A request to reorder exact additive contributions requires a different argument from a safety bound or a floating-point reproducibility claim. Retaining that distinction preserves a supported result while a different property remains unknown.

