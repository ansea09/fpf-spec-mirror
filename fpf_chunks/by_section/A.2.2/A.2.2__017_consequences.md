---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability"
section_id: "A.2.2:16"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__017_consequences.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.2.2 — U.Capability"
  - "A.2.2:16 — Consequences"
line_start: 2694
line_end: 2702
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.3"
  - "A.3"
  - "U.BoundedContext"
  - "U.Dynamics"
  - "U.PromiseContent"
  - "U.RoleAssignment"
keywords:
  - "ability"
  - "action"
  - "measures"
  - "performance"
  - "skill"
  - "work scope"
---

### A.2.2:16 - Consequences

| Benefits                                                                                           | Trade‑offs / mitigations                                                                                                      |
| -------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **Truthful planning.** Schedulers and managers can ask “can do?” independently of “assigned now?” | **Extra column in tables.** Adding scope, measures, and valid-through is a small authoring cost that repays itself in fewer reschedules. |
| **Safer gating.** Steps gate on both role and ability; fewer silent failures.                      | **Two checks instead of one.** Keep the checklist simple: *badge + bounds*.                                                   |
| **Clear service design.** Services become explicit promises built on visible abilities.            | **Temptation to over‑promise.** Keep service SLOs within demonstrated capability measures.                                    |
| **Clean separation with Dynamics and PBS/SBS.** No more “process” or “function” soup.              | **Some retraining.** Use the litmus tables (from the lexical rules) during onboarding.                                        |

