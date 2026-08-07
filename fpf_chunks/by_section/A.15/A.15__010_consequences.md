---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment"
section_id: "A.15:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__010_consequences.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "A.15 — Role–Method–Work Alignment"
  - "A.15:9 — Consequences"
line_start: 24290
line_end: 24298
dependencies:
  - "A.10"
  - "A.12"
  - "A.15"
  - "A.15.1-A.15.5"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.20"
  - "A.21"
  - "A.4"
  - "A.6"
  - "A.6.B"
  - "A.6.C"
  - "B.3"
  - "C.24"
  - "C.26.2"
  - "C.28"
  - "C.29"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.16"
  - "E.17"
  - "E.17.EFP"
  - "E.18.1"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "appearance-based reliance boundary"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "work admission display"
  - "work-entry readiness"
---

### A.15:9 - Consequences

| Benefits | Trade-offs and Mitigations |
| :--- | :--- |
| **Unambiguous Communication:** Provides a shared, precise vocabulary for teams to discuss roles, methods, work plans, work occurrences, and results, eliminating the ambiguity of source terms like "process." | **Initial Learning Curve:** Requires teams to learn and internalize the distinctions between the core entities. *Mitigation:* The "Chef" analogy and clear archetypes serve as powerful didactic tools. FPF tooling can guide users with templates. |
| **End-to-End Traceability:** The framework links each admitted Work individual to its exact four-participant role assignment and enacted method through obtaining relations; a separate assertion may cite the method-description edition, plan, evidence relation, or evidence-provenance relation needed by the receiving use. This supports root-cause analysis without treating interpretation metadata as work. | **Increased Formality:** Requires more explicit modeling than informal approaches. *Mitigation:* Record only the relations needed by the receiving use; do not materialize the whole alignment when a shorter direct claim suffices. |
| **Enables True Modularity:** By separating capability-fit from execution, the framework allows for easier substitution. A `MethodDescription` can be updated without changing past Work occurrences; any assertion or record about those occurrences remains a separate episteme and retains whatever edition reference its receiving use requires. A holder can be replaced with another when the replacement holder satisfies the declared capability-fit condition. | - |
| **Foundation for role-source accountability:** The model makes it possible to state role-bound work rules without making the role or publication act. For example, only a holder acting under `AuditorRole` in a `U.RoleAssignment` with the exact auditor-role taxonomy and effective scheme, and satisfying the selected method and applicable capability-fit or gate conditions, can perform one approval Work occurrence admitted under `U.Work`; its exact speech-act or instituted-effect relation makes the approval claim current, not a label-defined Work subkind. | - |

