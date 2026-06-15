---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__010_consequences.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:9 — Consequences"
line_start: 20899
line_end: 20907
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.15.1-A.15.4"
  - "A.15.4"
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
  - "E.16"
  - "E.17"
  - "E.17.EFP"
keywords:
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.WorkPlan"
  - "actual U.Work"
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "source-restoration boundary"
  - "work admission display"
---

### A.15:9 - Consequences

| Benefits | Trade-offs and Mitigations |
| :--- | :--- |
| **Unambiguous Communication:** Provides a shared, precise vocabulary for teams to discuss roles, methods, work plans, work occurrences, and results, eliminating the ambiguity of source terms like "process." | **Initial Learning Curve:** Requires teams to learn and internalize the distinctions between the core entities. *Mitigation:* The "Chef" analogy and clear archetypes serve as powerful didactic tools. FPF tooling should guide users with templates. |
| **End-to-End Auditability:** The framework creates a "digital thread" that links every operational event (`Work`) back to its authorizing role, context, and specification. This is critical for regulated industries and for root cause analysis. | **Increased Formality:** Requires more explicit modeling than informal approaches. *Mitigation:* This is a strategic investment. The upfront cost of formal modeling is offset by downstream savings in debugging, re-work, and compliance efforts. |
| **Enables True Modularity:** By separating capability from execution, the framework allows for easier substitution. A `MethodDescription` can be updated without invalidating past `Work` records. A `Holder` can be replaced with another, as long as it possesses the same `Capability`. | - |
| **Foundation for role-source accountability:** The model makes it possible to state role-bound work rules without making the role or publication act. For example: "Only a holder acting under `AuditorRole` in a `U.RoleAssignment` satisfying the governing role, holder, and bounded-context constraints can perform the `U.Work` that instantiates the `ApproveRelease` capability." | - |

