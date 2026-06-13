---
chunk_kind: "child"
pattern_id: "A.2.2"
pattern_title: "U.Capability"
section_id: "A.2.2:12"
section_title: "Interaction with Service Promise Clauses (external promise content)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.2/A.2.2__013_interaction-with-service-promise-clauses-external-promise-content.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.2.2 — U.Capability"
  - "A.2.2:12 — Interaction with Service Promise Clauses (external promise content)"
line_start: 2659
line_end: 2670
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

### A.2.2:12 - Interaction with Service Promise Clauses (external promise content)

A **service promise clause** (a `U.PromiseContent`) is a consumer‑facing **external promise statement**. It relies on capability but is not identical to it.

> **Note.** The bare head noun *service* is polysemic; in normative prose it is treated as an **always‑unpack** token. Use A.6.8 (RPR‑SERV) to name the intended facet (promise clause vs endpoint vs work vs commitment).

* **From capability to service promise clause.** You normally **derive** a service promise clause by taking a capability and **fixing** the promise outward (e.g., “We guarantee close ≤ 5 days”).
* **From service promise clause back to capability.** If the promise raises the bar (e.g., tighter SLA), the underlying capability must meet or exceed it under the promise clause’s context.
* **Staffing.** Delivering on a service promise clause still requires **Role assignments**; capability alone does not authorize action.

**Memory aid:** Capability = *can do*; service promise clause = *promise to others that we will do*.

