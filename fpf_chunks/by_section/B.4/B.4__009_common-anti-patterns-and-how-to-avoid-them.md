---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 40015
line_end: 40022
dependencies:
  - "A.12"
  - "A.4"
  - "B.4.1"
keywords:
  - "DesignRunTag feedback"
  - "drift repair"
  - "evolution loop"
  - "knowledge refinement"
  - "method refinement"
  - "observe-notice-stabilize-route"
  - "open-ended evolution"
---

### B.4:8 - **Common Anti-Patterns and How to Avoid Them**

| Anti-Pattern | Observable symptom | How FPF Prevents It (Conceptually) |
| :--- | :--- | :--- |
| **The "Immaculate Conception"** | A new feature or design "just appears" in the specification, with no record of the problem it was meant to solve. | **CC-B4.1** and **CC-B4.3** require an observed basis and the named Systems and dated Work through which the refinement was made. |
| **The "Self-Healing Illusion"** | The model claims "the system automatically improves itself" without specifying the mechanism. | **CC-B4.3** forbids self-evolution. The model must identify the external admitted System or Systems and the observation, refinement, and deployment Work they performed. An automated control loop can be such a System only when it is admitted independently of the holon being changed. |
| **The "Run-time Edit"** | An engineer makes a "quick fix" directly on a live system without updating the official design documents. | **CC-B4.2** enforces that all refinements happen in `design-time`. A "hotfix" is conceptually an emergency, accelerated run through the entire loop: the fix is observed, designed, and then deployed. |

