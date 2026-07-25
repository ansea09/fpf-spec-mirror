---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:6.8"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__008_bias-annotation.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:6.8 — Bias-Annotation"
line_start: 24484
line_end: 24493
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "F.6"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing system"
  - "covering U.RoleAssignment"
  - "enacted method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:6.8 - Bias-Annotation

| Bias | How A.15.1 prevents it |
| --- | --- |
| Plan-as-work bias | `U.WorkPlan`, schedules, method descriptions, and intended parameter bindings stay separate from the dated occurrence. |
| Log-as-work bias | Telemetry, dashboards, provenance rows, and work publications can evidence or describe a work occurrence; they do not become the occurrence. |
| Method-as-occurrence bias | `U.Method` and `U.MethodDescription` identify or describe the way of doing; an independently grounded assertion that one Work individual is admitted under `U.Work` designates the dated performed occurrence. |
| Evidence-as-authority bias | Evidence, assurance, gate, release, and causal-use claims keep their governing patterns and do not follow from a work record by appearance. |
| Record-handling-as-transformation bias | Copying, formatting, evaluating, or publishing records can be grounded as Work occurrences admitted under `U.Work` without an automatic change claim. Any claimed record or dataset transformation still needs independent A.3.4 identity and exact work-to-change facts. |

