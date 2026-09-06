---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Domain-Concept Bridge"
section_id: "B.5.3:6"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__007_consequences.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "B.5.3 — Domain-Concept Bridge"
  - "B.5.3:6 — Consequences"
line_start: 41755
line_end: 41762
dependencies:
  - "A.13"
  - "A.15"
  - "A.2"
  - "A.6.5"
  - "A.7"
  - "B.3.3"
  - "C.2.1"
  - "C.3"
  - "E.10.ROLE"
  - "E.17"
  - "E.24.UK"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.7"
  - "F.8"
  - "F.9"
keywords:
  - "F.17 cell"
  - "basis relation"
  - "bounded use and loss"
  - "direct relation"
  - "domain vocabulary"
  - "source-local meaning"
---

### B.5.3:6 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Domain language stays usable:** Experts keep familiar words without forcing every word into the kernel. | **Recovery overhead:** A load-bearing expression needs its exact source-local claim and governed value. Keep the returned explanation short; recover F.17 cells and their basis relations for claims that need them, including F.9 Bridges, and add durable rows only when reuse needs them. |
| **Kernel stays lean:** New kinds require explicit admission and ontic support. | **More precise modeling choices:** The bridge may reveal that one local word hides several FPF values. That is the point: split them before they drive work. |
| **Cross-document clarity:** Requirements, diagrams, dashboards, simulations, and reports can be compared without pretending they are the same artifact. | **Need for an exact use boundary:** Do not reuse a source-local claim or semantic relation in another project, scheme, scope, or action without checking the actual changed values, tolerated loss, and reliance basis. |

