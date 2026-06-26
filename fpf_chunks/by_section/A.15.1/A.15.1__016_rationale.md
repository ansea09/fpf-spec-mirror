---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:13.0"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__016_rationale.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:13.0 — Rationale"
line_start: 21726
line_end: 21729
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
  - "actuals"
  - "event"
  - "execution"
  - "log"
  - "occurrence"
  - "run"
---

### A.15.1:13.0 - Rationale

`U.Work` is kept as a dated occurrence because method, method description, work plan, and result are different FPF objects. The same source phrase can point to several of them, but performed-work claims need occurrence evidence, time bounds, role assignment, and affected EntityOfConcern rather than a convenient method or plan label. This keeps work mereology, resource aggregation, and P2W carry-through grounded in what happened.

