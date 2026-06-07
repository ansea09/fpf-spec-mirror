---
chunk_kind: "child"
pattern_id: "E.13"
pattern_title: "Pragmatic Utility & Value Alignment"
section_id: "E.13:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.13/E.13__002_problem-frame.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "E.13 — Pragmatic Utility & Value Alignment"
  - "E.13:1 — Problem Frame"
line_start: 61032
line_end: 61037
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

### E.13:1 - **Problem Frame**

The FPF provides a powerful engine for constructing formally correct and highly reliable holons. This power, however, introduces a subtle but profound risk: a team can create a perfectly verified and validated holon or episteme (`AssuranceLevel:L2`) that solves an irrelevant, misunderstood, or non-existent problem. The framework guarantees that the solution is *correct*, but it does not, by itself, guarantee that the solution is *useful*.

Furthermore, many of the most important system objectives—such as "safety," "usability," or "security"—are not directly measurable. They are assessed via **proxy characteristics** (e.g., "number of reported vulnerabilities" as a proxy for security). This practice is vulnerable to Goodhart's Law: when a proxy becomes the primary target, it often ceases to be a good measure of the original goal, as teams begin to optimize the proxy at the expense of the real objective.

