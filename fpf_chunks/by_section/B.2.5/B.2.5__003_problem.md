---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor–Subholon Feedback Loop"
section_id: "B.2.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__003_problem.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "B.2.5 — Supervisor–Subholon Feedback Loop"
  - "B.2.5:2 — Problem"
line_start: 30340
line_end: 30349
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

### B.2.5:2 - **Problem**

While the concept of layered supervision is intuitive, its formal modeling is fraught with conceptual traps. Without a strict, principled distinction between different types of hierarchies, as mandated by **Strict Distinction (A.7)**, models become ambiguous. The primary challenge is to untangle three distinct hierarchies for any given holon:

1.  **The Structural Hierarchy (Levels):** The mereological (part-whole) decomposition of the holon's **carrier**. For a `U.System`, this is its physical composition (e.g., an engine is `ComponentOf` a car). For a `U.Episteme`, this is the structure of its `Symbol` carrier (e.g., a chapter is `ComponentOf` a book).
2.  **The Functional/Supervisory Hierarchy (Layers):** The decomposition of the management or reasoning task. This is a hierarchy of **`Transformer`s playing roles**. A `Transformer` in a higher layer (e.g., a scientific committee) `supervises` a `Transformer` in a lower layer (e.g., a research lab) by providing it with objectives or constraints.
3.  **The Dataflow Network:** The network of information exchange (`U.Interaction`) between these `Transformer`s in their respective roles (e.g., `funding decisions` flowing down, `research findings` flowing up).

Confusing these hierarchies leads to critical modeling errors. For example, treating a functional layer (a `U.Method` performed by a `Transformer`) as if it were a structural component (`ComponentOf` the holon it manages) is a category error that this pattern is designed to prevent.

