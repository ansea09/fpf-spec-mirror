---
chunk_kind: "child"
pattern_id: "E.11.PUR"
pattern_title: "Pattern-Use Applicability, Recommendation, and Coordination"
section_id: "E.11.PUR:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.11.PUR/E.11.PUR__011_rationale.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "E.11.PUR — Pattern-Use Applicability, Recommendation, and Coordination"
  - "E.11.PUR:10 — Rationale"
line_start: 79383
line_end: 79388
dependencies:
  - "A.15"
  - "A.19"
  - "A.19.CPM"
  - "A.19.ECS"
  - "A.21"
  - "A.6.5"
  - "C.22.PFR"
  - "C.24"
  - "C.30"
  - "E.10.MOVE"
  - "E.11"
  - "E.11.PUA"
  - "E.18"
  - "E.18.1"
  - "G.11"
keywords:
---

### E.11.PUR:10 - Rationale

Applicability, recommendation, and coordination answer different questions. Applicability asks whether a candidate's conditions hold. Recommendation asks which applicable use best serves the current concern. Coordination asks how several candidate uses belong together. Keeping the questions separate prevents a familiar label or score from becoming an unexamined decision.

Pairwise precedence is intentionally narrow. A set of candidate pattern uses can be unordered, partially ordered, or totally ordered. Only a current dependency justifies an edge. A prerequisite-result edge needs both the exact expectation and an E.11.PUA closure whose result and category-correct basis satisfy the stated condition; neither a result label nor an expectation can do so. This preserves graph structure without turning every explanation into a chain or minting a generic result relation.

