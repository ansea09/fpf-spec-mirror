---
chunk_kind: "child"
pattern_id: "G.0"
pattern_title: "Define Admissible Comparison and Aggregation for a Frame (CG-Spec)"
section_id: "G.0:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.0/G.0__003_problem.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "G.0 — Define Admissible Comparison and Aggregation for a Frame (CG-Spec)"
  - "G.0:2 — Problem"
line_start: 110830
line_end: 110838
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.CN"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.23"
  - "E.10"
  - "E.5"
  - "E.5.2"
  - "F.9"
  - "G.1"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "CG-Frame"
  - "CG-Spec"
  - "CL-routing"
  - "ComparatorSet"
  - "MinimalEvidence"
  - "RSCRTriggerKindId"
  - "ReferencePlane"
  - "ScaleComplianceProfile (SCP)"
  - "admissible comparison and aggregation"
  - "edition pins"
  - "evidence requirements"
  - "Γ-fold"
  - "Φ(CL)"
  - "Φ_plane"
---

### G.0:2 - Problem

Without a single, frame-level legality standard:

* comparisons and aggregations drift into *implicit assumptions* (hidden scalarisation; silent totalisation of partial orders),
* numeric gates run on “whatever is available” rather than declared evidence minima and lane/carrier requirements,
* cross-context reuse happens without explicit crossing visibility and stated losses,
* selection outcomes become hard to audit because legality, evidence minima, and penalty routing are not pinned and traceable.

