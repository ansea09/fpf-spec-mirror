---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility & Value Alignment"
section_id: "E.13:7"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__008_consequences.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "E.13 — Pragmatic Utility & Value Alignment"
  - "E.13:7 — Consequences"
line_start: 60869
line_end: 60877
dependencies:
  - "E.12"
  - "E.2"
keywords:
  - "Goodhart's Law"
  - "MVE"
  - "Proxy-Audit Loop"
  - "pragmatic"
  - "utility"
  - "value"
---

### E.13:7 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Defense Against Goodhart's Law:** The Proxy-Audit Loop is a concrete, operational defense against the common failure mode of optimizing for the wrong thing. It forces regular, strategic reflection on the meaning of metrics. | **Introduces Strategic Overhead:** The Proxy-Audit Loop and the creation of an MVE require dedicated time for strategic thinking and early implementation. *Mitigation:* This is not an expense but a strategic investment. This upfront effort is designed to prevent the far greater cost of developing the wrong system over months or years. |
| **Ensures Value-Driven Development:** The MVE Mandate guarantees that all major development efforts are grounded in a demonstrated, working solution to a real problem, however small. This prevents teams from investing significant resources in abstract models that have no proven path to practical application. | - |
| **Prevents "Analysis Paralysis":** By requiring an early, working example, this principle encourages an iterative, pragmatic development style. It forces teams to build and learn, rather than over-specifying in a vacuum. | - |
| **Positions FPF as an Engineering Discipline:** This pattern firmly anchors FPF as a tool for practical engineering, not just theoretical modeling. | - |

