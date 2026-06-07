---
chunk_kind: "child"
pattern_id: "B.1"
pattern_title: "Universal Algebra of Aggregation (Γ)"
section_id: "B.1:10"
section_title: "Anti-Patterns & Conceptual Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1/B.1__011_anti-patterns-conceptual-repairs.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "B.1 — Universal Algebra of Aggregation (Γ)"
  - "B.1:10 — Anti-Patterns & Conceptual Repairs"
line_start: 28567
line_end: 28575
dependencies:
  - "A.1"
  - "A.9"
  - "B.1.x"
  - "B.2"
keywords:
  - "COMM"
  - "IDEM"
  - "LOC"
  - "MONO"
  - "WLNK"
  - "aggregation"
  - "composition"
  - "gamma operator"
  - "holon"
  - "invariants"
---

### B.1:10 - Anti-Patterns & Conceptual Repairs

| Anti-Pattern | Symptom | Conceptual Fix |
| :--- | :--- | :--- |
| **Averaging Risk** | A dashboard shows a high overall reliability score for a system by averaging a high-reliability component with a low-reliability one. | Enforce the **WLNK** invariant. The aggregate reliability must be `min(R_parts)`, not `avg(R_parts)`. |
| **Order-Dependent Builds**| The same set of software patterns produces a different final build depending on the compilation order. | Enforce **COMM/LOC**. Identify the hidden dependency between the patterns and either remove it or make it explicit, moving to `Γ\_ctx` if necessary. |
| **Improvement Paradox** | A team replaces a component with a better one, but a system-level KPI gets worse. | Enforce **MONO**. This indicates a hidden, negative coupling. The model must be updated to make this coupling an explicit constraint or interaction. |
| **Synergy by Narrative** | A claim is made that the whole is greater than the sum of its parts, without a formal mechanism. | This violates **WLNK**. If the synergy is real (e.g., due to redundancy or a new feedback loop), it must be modeled as a **Meta-Holon Transition** (Pattern B.2). |

