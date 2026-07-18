---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:6.7"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__008_bias-annotation.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:6.7 — Bias-Annotation"
line_start: 22704
line_end: 22713
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "EpisodeOf_work"
  - "TemporalPartOf_work"
  - "actuals"
  - "concurrent work part"
  - "operational work part"
  - "performed enactment"
  - "trace"
  - "work occurrence"
---

### A.15.1:6.7 - Bias-Annotation

| Bias | How A.15.1 prevents it |
| --- | --- |
| Plan-as-work bias | `U.WorkPlan`, schedules, method descriptions, and intended parameter bindings stay separate from the dated occurrence. |
| Log-as-work bias | Telemetry, dashboards, provenance rows, and work publications can evidence or describe a work occurrence; they do not become the occurrence. |
| Method-as-occurrence bias | `U.Method` and `U.MethodDescription` identify or constrain the way of doing; `U.Work` records the dated performed enactment. |
| Evidence-as-authority bias | Evidence, assurance, gate, release, and causal-use claims keep their governing patterns and do not follow from a work record by appearance. |
| Record-only transformation bias | Record manipulation qualifies as `U.Work` only when the context declares the record or dataset as the affected product referent. |

