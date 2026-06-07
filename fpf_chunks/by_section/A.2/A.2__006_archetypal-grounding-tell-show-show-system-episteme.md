---
chunk_kind: "child"
pattern_id: "A.2"
pattern_title: "Role Taxonomy"
section_id: "A.2:5"
section_title: "Archetypal Grounding (Tell–Show–Show: System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2/A.2__006_archetypal-grounding-tell-show-show-system-episteme.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "A.2 — Role Taxonomy"
  - "A.2:5 — Archetypal Grounding (Tell–Show–Show: System / Episteme)"
line_start: 1601
line_end: 1619
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.13"
  - "A.15"
  - "A.2.1-A.2.6"
keywords:
  - "U.RoleAssignment"
  - "assignment"
  - "context"
  - "function vs identity"
  - "holder"
  - "responsibility"
  - "role"
---

### A.2:5 - Archetypal Grounding (Tell–Show–Show: System / Episteme)

**Tell.** A single holon can be the *same bearer* across time while taking on different, context‑bound roles. A role is a *mask* (capability/obligation schema) that explains *what it is being* in a given `U.BoundedContext`; behavioural facts and resource deltas remain in `U.Method` / `U.Work`.

**Show.**

**System case — Cooling loop**
`PumpUnit#3#HydraulicPump:Plant‑A@2025‑08‑08..open`
`HydraulicPumpRole ↦bindsMethod↦ CentrifugalPumpingMethod` (design‑time, Context‑local eligibility)
`CentrifugalPumpingMethod ↦isDescribedBy↦ centrifugal_pump_curve.ld@v7` (MethodDescription viewpoint; step‑graph OR dynamics, as appropriate)
`run‑2025‑08‑08 isExecutionOf centrifugal_pump_curve.ld@v7; performedBy PumpUnit#3#HydraulicPump:Plant‑A@2025‑08‑08..2025‑08‑08` (run‑time Work)
*(Behavioural/resource facts live in Work; method semantics are governed by the referenced MethodDescription viewpoint.)*

**Episteme case — Standard in design**
`RFC‑9110.pdf#ProtocolStandard:WorldWideWeb` justifies `MethodDescription` selection; the **system** bearing `TransformerRole` is the design service that executed the selection work. The episteme did **not** act.

**Collective vs set (safety pitfall)**
A **set** `{Alice, Bob, 3.14}` has no behaviour; a **team** is a **system** with boundary, coordination **Method**, and supervision **Work**; only the latter can bear agentic roles.

