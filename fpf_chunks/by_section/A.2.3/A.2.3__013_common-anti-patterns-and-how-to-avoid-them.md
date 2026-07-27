---
chunk_kind: "child"
pattern_id: "A.2.3"
pattern_title: "U.PromiseContent (Promise Content)"
section_id: "A.2.3:9"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.3/A.2.3__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "A.2.3 — U.PromiseContent (Promise Content)"
  - "A.2.3:9 — Common Anti-Patterns and How to Avoid Them"
line_start: 3584
line_end: 3606
dependencies:
  - "A.1.1"
  - "A.15.1"
  - "A.15.2"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.6"
  - "A.2.8"
  - "A.3.1"
  - "A.3.2"
  - "A.6.8"
  - "A.6.C"
  - "E.10"
  - "F.12"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.ClaimScope"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.Scope"
  - "U.Work"
  - "U.WorkPlan"
  - "U.WorkScope"
keywords:
  - "SLA"
  - "SLO"
  - "Work evidence"
  - "acceptanceSpec"
  - "accessSpec"
  - "claim scope (G)"
  - "promise content"
  - "provider/consumer roles"
---

### A.2.3:9 - Common Anti-Patterns and How to Avoid Them

* **“The microservice **is** the service.”**
  Rewrite to facet-explicit terms (A.6.8): the microservice is typically a **service delivery system** (`U.System`), a **service access point** (`U.System`), or both. Keep the consumer-facing promised-outcome statement in `U.PromiseContent`, and represent accountability via `U.Commitment` if needed.

* **“The API **is** the service.”**
  The API is typically a **service access spec** (`accessSpec : MethodDescription`) (and systems playing interface roles). The **promise content** is the promised outcome and acceptance statement judged by `acceptanceSpec`.

* **“Our **process** is the service.”**
  Process or recipe is `U.Method` or `U.MethodDescription`; schedule is `U.WorkPlan`. The **promise content** is **what is promised to the consumer**.

* **“The **ticket** is the service.”**
  A ticket or case is `U.Work` (and perhaps a `WorkPlan` item). Evidence and outcomes sit on Work, not on the promise content.

* **“Attach cost to the service.”**
  Actual cost and time attach to `U.Work` only (A.15.1). Service metrics are computed **from** Work.

* **“Put service under BoM.”**
  Services are not structural parts. Keep PBS and SBS clean.

* **“Hard‑code people into the service.”**
  Name **role kinds** in the promise content (`U.PromiseContent`); run‑time performers are `U.RoleAssignment`s.

