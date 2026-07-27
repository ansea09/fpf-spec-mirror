---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Domain-Concept Bridge"
section_id: "B.5.3:6"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__007_consequences.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "B.5.3 — Domain-Concept Bridge"
  - "B.5.3:6 — Consequences"
line_start: 40541
line_end: 40548
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.5"
  - "A.7"
  - "B.3.3"
  - "C.2.1"
  - "C.3"
  - "E.17"
  - "E.24.UK"
  - "F.1"
  - "F.18"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "bounded context"
  - "bridge scope"
  - "concept bridge"
  - "domain vocabulary"
  - "local sense"
  - "role assignment boundary"
---

### B.5.3:6 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Domain language stays usable:** Experts keep familiar words without forcing every word into the kernel. | **Bridge overhead:** Load-bearing local terms need a small bridge record. Keep it short and reopen stronger patterns only when a claim becomes load-bearing. |
| **Kernel stays lean:** New kinds require explicit admission and ontic support. | **More precise modeling choices:** The bridge may reveal that one local word hides several FPF values. That is the point: split them before they drive work. |
| **Cross-document clarity:** Requirements, diagrams, dashboards, simulations, and reports can be compared without pretending they are the same artifact. | **Need for current context:** Bridges are context-scoped; do not move them across projects without checking scope and loss. |

