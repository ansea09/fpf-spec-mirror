---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor–Subholon Feedback Loop"
section_id: "B.2.5:6"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__007_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "B.2.5 — Supervisor–Subholon Feedback Loop"
  - "B.2.5:6 — Common Anti-Patterns and How to Avoid Them"
line_start: 30402
line_end: 30409
dependencies:
  - "A.1"
  - "B.2"
  - "U.Method"
keywords:
  - "control architecture"
  - "feedback loop"
  - "layered control"
  - "stability"
  - "supervisor"
---

### B.2.5:6 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Manager's View: What It Looks Like | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Ghost in the Machine"** | The model shows a collection of parts that somehow coordinate to achieve a global goal, but there is no identifiable mechanism or agent responsible for that coordination. | **CC-B2.5.1** forces the modeler to explicitly name the `Supervisor`. If no supervisor can be identified, then no supervisory loop exists, and the coordination is either an illusion or an un-modeled external factor. |
| **The "Functional Soup"** | A diagram mixes physical components and functional layers in the same hierarchy. The "Planning Layer" is shown as a "part of" the physical system. | **CC-B2.5.4** and the strict mereology of FPF (A.14) forbid this. A functional layer is realized *by* physical components, but it is not *part of* them. This prevents category errors. |
| **The "Perfect Communication" Fallacy** | The design of the control logic assumes that the supervisor has instant, infinite-bandwidth access to the state of all subsystems. The system fails in the real world due to network latency. | **Principle P-I (Information Constraint)** and its formal invariant **SSI-5** mandate that the stability analysis must account for the real-world constraints of the `Shared Medium`. |

