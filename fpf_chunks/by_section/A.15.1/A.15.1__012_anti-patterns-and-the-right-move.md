---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:11"
section_title: "Anti‑patterns (and the right move)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__012_anti-patterns-and-the-right-move.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:11 — Anti‑patterns (and the right move)"
line_start: 20409
line_end: 20419
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

### A.15.1:11 - Anti‑patterns (and the right move)

* **"The log is the process."** Dumping telemetry without occurrence references (method-description source when live, performer, time window, affected referent, context) -> **Not Work**. Create a Work record and link the log as evidence.
* **Record-only transforms.** ETL or replication of records with no declared affected referent (product or dataset as product) -> **Not Work** in this context; either declare the dataset as the product referent or move it to `U.WorkPlan` or the relevant operations pattern.
* **Silent cross‑context acceptance.** “Ops accepted it, so audit accepts it.” → Add a **Bridge** or re‑judge in audit context.
* **Method-description edition drift in mid-run.** Swapping SOP v5->v6 without recording -> split into episodes or record method-description override.
* **Budget on the method.** Charging costs to Method or Role -> Book **only** to Work; keep estimates in method descriptions or plans.
* **Part ambiguity.** Mixing retries, episodes, and operational parts with no declared relation → Choose and declare the part relation.
* **Union-hull confusion.** Changing KPI coverage silently between reports -> declare `Γ_time` policy per KPI.
* **Double‑count in overlaps.** Summing child and parent resource ledgers → Declare and apply an overlap policy.

