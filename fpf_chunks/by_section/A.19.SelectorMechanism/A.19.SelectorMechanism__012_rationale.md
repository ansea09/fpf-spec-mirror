---
chunk_kind: "child"
pattern_id: "A.19.SelectorMechanism"
pattern_title: "Unified Selection Kernel, SelectorMechanism"
section_id: "A.19.SelectorMechanism:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.SelectorMechanism/A.19.SelectorMechanism__012_rationale.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.19.SelectorMechanism — Unified Selection Kernel, SelectorMechanism"
  - "A.19.SelectorMechanism:10 — Rationale"
line_start: 39203
line_end: 39213
dependencies:
  - "A.19.CHR"
  - "A.19.CN"
  - "A.19.CPM"
  - "A.19.ULSAM"
  - "A.19.USCM"
  - "A.6.1"
  - "A.6.5"
  - "C.22"
  - "E.18"
  - "G.0"
  - "G.5"
keywords:
  - "ComparisonResultSlot"
  - "SelectEligibility"
  - "SelectorMechanism"
  - "explicit criteria"
  - "finite basis of binary CPM applications"
  - "pass/degrade/abstain"
  - "required comparison coverage"
  - "selected candidate set"
  - "selection kernel"
---

### A.19.SelectorMechanism:10 - Rationale

Selection is where many systems accidentally convert admissible but nuanced information into an unjustified scalar decision. Making selection a separate, explicit mechanism boundary achieves two things that matter for engineering management:

1. **Technical integrity:** the declared guard tests the admissibility and evidence conditions needed by this selection.
2. **Organizational clarity:** it makes defaults and thresholds discussable, reviewable, and maintainable as explicit policy references.

The set‑returning default is not a preference for large retained sets; it is a correctness safeguard when the order is not total. Single-winner outcomes remain possible when the criteria select one candidate from the admitted comparison outcomes.

---

