---
chunk_kind: "child"
pattern_id: "B.4"
pattern_title: "Coordinate Repeated Adaptation (Canonical Evolution Loop)"
section_id: "B.4:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.4/B.4__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d8dd955fddb923b5b946d2c5865d0665cff5a67e"
heading_path:
  - "B.4 — Coordinate Repeated Adaptation (Canonical Evolution Loop)"
  - "B.4:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 45945
line_end: 45952
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
---

### B.4:8 - **Common Anti-Patterns and How to Avoid Them**

| Anti-pattern | Observable symptom | Repair |
| :--- | :--- | :--- |
| **Change without a basis** | A feature or design appears with no observed basis or identity decision. | **CC-B4.1** and **CC-B4.2** connect the change to an observed basis and state whether the subject continues or has a successor. |
| **Unidentified internal adaptation** | "The system automatically improves itself" hides who or what performed the activity. | Identify who or what changes which subject. Use **CC-B4.3** for a Work claim. For an internal acting side, recover the distinct participants and their parthood under `A.12`, together with the Work, Method and phase facts the receiving claim consumes; physical externality is not required. |
| **Incomplete hotfix account** | A quick run-time repair is reported as a complete successful loop, although design repair, evidence, or renewed-use confirmation did not occur. | State only the urgent observation, change activity, deployment and immediate result that occurred. Later description repair, testing, assurance and follow-up operation are subsequent activities and may reopen the loop; qualify any particular Work occurrences under B.4:4.2. |

