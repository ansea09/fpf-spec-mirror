---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 35006
line_end: 35013
dependencies:
  - "A.12"
  - "A.4"
  - "B.4.1-B.4.3"
keywords:
  - "DesignRunTag feedback"
  - "drift repair"
  - "evolution loop"
  - "observe-notice-stabilize-route"
  - "open-ended evolution"
---

### B.4:8 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Observable symptom | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Immaculate Conception"** | A new feature or design "just appears" in the specification, with no record of the problem it was meant to solve. | **CC-B4.1** and **CC-B4.3** mandate that every refinement must start with an *Observe* phase, performed by a named `Transformer`. There is no change without a documented observation and an agent who made it. |
| **The "Self-Healing Illusion"** | The model claims "the system automatically improves itself" without specifying the mechanism. | **CC-B4.3** forbids self-evolution. The model must explicitly show an *external* `Transformer` (which could be an automated control loop, but is still modeled as external to the holon being changed) that performs the Observe-Refine-Deploy cycle. |
| **The "Run-time Edit"** | An engineer makes a "quick fix" directly on a live system without updating the official design documents. | **CC-B4.2** enforces that all refinements happen in `design-time`. A "hotfix" is conceptually an emergency, accelerated run through the entire loop: the fix is observed, designed, and then deployed. |

