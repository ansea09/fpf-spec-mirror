---
chunk_kind: "child"
pattern_id: "A.20"
pattern_title: "Constraint Validity for Transformation Steps"
section_id: "A.20:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.20/A.20__011_consequences.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "A.20 — Constraint Validity for Transformation Steps"
  - "A.20:9 — Consequences"
line_start: 34000
line_end: 34003
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "A.6.1"
  - "A.6.4"
  - "B.3"
  - "C.2.1"
  - "C.27"
  - "E.17"
  - "E.18"
  - "E.20"
  - "F.9"
  - "G.11"
keywords:
---

### A.20:9 - Consequences

The result is smaller and more reusable. A missing check can no longer disappear as success, and a gate can retain useful independent findings even after one internal failure. The cost is that a consequence-bearing use must name its required constraint set and cannot hide policy inside A.20 status words.

