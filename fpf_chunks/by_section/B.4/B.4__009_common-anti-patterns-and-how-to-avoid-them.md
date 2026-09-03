---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Canonical Evolution Loop"
section_id: "B.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "B.4 — Canonical Evolution Loop"
  - "B.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 40579
line_end: 40586
dependencies:
  - "A.12"
  - "A.15.1"
  - "A.4"
  - "B.3"
  - "B.4"
  - "B.4.1"
  - "B.5"
  - "B.5.1"
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

| Anti-Pattern | Observable symptom | How FPF prevents it conceptually |
| :--- | :--- | :--- |
| **The "Immaculate Conception"** | A feature or design appears with no observed basis or identity decision. | **CC-B4.1** and **CC-B4.2** connect the change to an observed basis and state whether the subject continues or has a successor. |
| **The "Self-Healing Illusion"** | "The system automatically improves itself" hides who or what performed the Work. | **CC-B4.3** requires a distinct acting-side System. An internal control or adaptation loop is valid when exact internal participants, their parthood, the Work, Methods, and phase transitions are identified; physical externality is not required. |
| **The "Perfect Hotfix"** | A quick run-time repair is reported as a complete successful loop, although design repair, evidence, or renewed-use confirmation did not occur. | Record only the urgent observation, change Work, deployment, and immediate result that actually occurred. Later description repair, testing, assurance, and follow-up operation are separate Work and may reopen the loop. A hotfix can compress time, not truth. |

