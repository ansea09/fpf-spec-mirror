---
chunk_kind: "child"
pattern_id: "E.18"
pattern_title: "Transformation Flow Structure"
section_id: "E.18:15a"
section_title: "E.18.1 P2W Child-Pattern Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18/E.18__018_e-18-1-p2w-child-pattern-relation.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "E.18 — Transformation Flow Structure"
  - "E.18:15a — E.18.1 P2W Child-Pattern Relation"
line_start: 81787
line_end: 81790
dependencies:
  - "A.15.1"
  - "A.15.PROD"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.3.4"
  - "A.6.RCD"
  - "A.7"
  - "C.29"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.17"
  - "E.18.1"
  - "E.18.2"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P2W support"
  - "U.Transfer"
  - "adjacent governed loci"
  - "crossings"
  - "flow valuation"
  - "independently grounded actual transformations"
  - "no-automatic-composition boundary"
  - "selected transformation-flow structure"
---

### E.18:15a - E.18.1 P2W Child-Pattern Relation

`E.18.1` is a child pattern for problem-to-work carry-through. It governs the local P2W relation from an accepted `ProblemCard@Context` and carried ClaimGraph content to one next directly governed value or relation. A P2W use consumes this pattern's selected-structure discipline only when a named receiving use relies on an explicit `TransformationFlowStructure`, path, flow valuation, transfer, crossing, or gate position; when branches, joins, guards, or governing-pattern positions must be recoverable, `E.18.3` governs that fuller structure. In this split, `E.18.1` carries the accepted problem-side claim and local continuation, while `E.18` carries selected transformation-flow structure without making it mandatory for ordinary P2W use.

