---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor–Subholon Feedback Loop"
section_id: "B.2.5:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__002_problem-frame.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "B.2.5 — Supervisor–Subholon Feedback Loop"
  - "B.2.5:1 — Problem Frame"
line_start: 30407
line_end: 30412
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

### B.2.5:1 - **Problem Frame**

Many of the most successful and resilient holons, both natural and engineered—from scientific paradigms and bacterial cells to the internet and human sensorimotor control—share a common architectural motif: a **Layered Supervisory Architecture**. In this architecture, the complex task of managing the holon is decomposed into a stack of functional layers. Each layer operates at a different spatiotemporal scale and level of abstraction, communicating with its neighbors through well-defined interfaces.

The paper "Towards a Theory of Control Architecture" by Matni, Ames, and Doyle (2024) provides a rigorous foundation for understanding such architectures in the context of control systems. FPF generalizes these insights to all holon types. For example, a **`U.System`** like an aircraft might have a Guidance, Navigation, and Control (GNC) architecture realized by distinct `Transformer`s. Similarly, a **`U.Episteme`** like a large scientific theory has layers: foundational axioms (which act as a "decision making" layer), core theorems (a "trajectory planning" layer), and specific applications or derived lemmas (a "feedback control" layer). This layered structure is a convergent solution to the fundamental problem of managing complexity.

