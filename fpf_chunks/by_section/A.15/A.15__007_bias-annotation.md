---
chunk_kind: "child"
pattern_id: "A.15"
pattern_title: "Role–Method–Work Alignment (Contextual Enactment)"
section_id: "A.15:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15/A.15__007_bias-annotation.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "A.15 — Role–Method–Work Alignment (Contextual Enactment)"
  - "A.15:6 — Bias-Annotation"
line_start: 21493
line_end: 21509
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
  - "contextual enactment"
  - "coordinated-work evidence"
  - "role-method-work distinction"
  - "source-restoration boundary"
  - "work admission display"
  - "work-entry readiness"
---

### A.15:6 - Bias-Annotation

Lenses tested: **Gov**, **Arch**, **Onto and Epist**, **Prag**, **Did**. Scope: **Universal** for contextual enactment across engineering, operational, and knowledge-work settings.

Bias risks and mitigations:

* **Governance bias (Gov):** teams may over-treat role labels or approval displays as enough evidence that work happened.
  *Mitigation:* keep `U.RoleAssignment`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work` distinct, and let only `U.Work` carry actuals and resource use.
* **Architectural bias (Arch):** modelers may pull roles or capabilities into structural part hierarchies because those diagrams are already present.
  *Mitigation:* preserve role and capability as context-bound assignment and ability values, not parts.
* **Epistemic bias (Onto and Epist):** a documented recipe or schedule can be mistaken for proof of execution.
  *Mitigation:* require the traceability chain from `U.RoleAssignment` and `U.MethodDescription` to dated `U.Work`.
* **Pragmatic bias (Prag):** teams may keep using one overloaded source-side "process" word because it feels faster.
  *Mitigation:* resolve "workflow", "schedule", and "what happened" source cues through `U.Method`, `U.MethodDescription`, `U.WorkPlan`, and `U.Work`.
* **Didactic bias (Did):** the chef analogy can make the pattern seem intuitive while hiding the need for explicit model links.
  *Mitigation:* pair the analogy with the canonical relations and checklist.

