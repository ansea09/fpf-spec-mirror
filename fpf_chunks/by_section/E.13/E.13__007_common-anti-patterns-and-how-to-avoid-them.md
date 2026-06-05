---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility & Value Alignment"
section_id: "E.13:6"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__007_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.13 — Pragmatic Utility & Value Alignment"
  - "E.13:6 — Common Anti-Patterns and How to Avoid Them"
line_start: 60863
line_end: 60870
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

### E.13:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Perfectly Engineered Irrelevance"** | The team delivers a technically brilliant system that is formally verified and validated, but no one wants to use it because it doesn't solve a real problem. | **CC-E13.3** forces the team to build a working, end-to-end slice of value (the MVE) *first*. This grounds the entire project in a demonstrated solution to a real user need from day one. |
| **The "Metric Myopia"** | The team becomes obsessed with improving a specific KPI, ignoring clear indicators that this is not improving—and may even be harming—the overall user experience or business goal. | **CC-E13.2** mandates the Proxy-Audit Loop. This forces a periodic, strategic step-back, where the `Strategist` role is constitutionally required to ask, "Are we still measuring what matters?" |
| **The "Big Design Up Front" Trap** | The team spends months creating a vast, abstract, and highly detailed model of a system before ever building a single working component. | The **MVE Mandate** prevents this. It forces an iterative, pragmatic "build-to-learn" approach, ensuring that models are always grounded in a working reality. |

