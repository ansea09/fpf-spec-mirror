---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:13a"
section_title: "SoTA Alignment"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__015_sota-alignment.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:13a — SoTA Alignment"
line_start: 20167
line_end: 20177
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
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

### A.15.1:13a - SoTA Alignment

**SoTA alignment rule.** A source tradition counts here only when it preserves the local `U.Work` distinction: dated occurrence, role-assigned performer, enacted method, method-description source when live, time window, affected referent, resources, outcome, and evidence path.

| Source tradition | Local invariant adopted | Shortcut rejected |
| --- | --- | --- |
| 4D extensional and BORO-style occurrence modeling | Work identity is tied to occurrence extent plus execution anchors; parts, retries, resumptions, and overlaps are explicit. | Treating a method factor, diagram, or log entry as proof of a work occurrence. |
| Process mining, audit, and operations-management practice | Logs, telemetry, and event records evidence work only after they are bound to performer, method, time window, context, and affected referent. | Treating telemetry alone as `U.Work`. |
| Temporal-interval and aggregation practice | Roll-ups require declared `Γ_time`, `Γ_work`, and overlap policy; partial order and overlap are not hidden in step labels. | Mixing union, hull, parent cost, and child cost without a declared policy. |
| Provenance, observability, and quality-measurement practice | Work records carry evidence paths and currentness hooks without letting evidence, assurance, or gate claims replace the occurrence. | Using an evidence path, assurance statement, or gate result as if it were the performed work. |

