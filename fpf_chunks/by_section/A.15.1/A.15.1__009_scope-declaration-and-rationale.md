---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:7"
section_title: "Scope Declaration and Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__009_scope-declaration-and-rationale.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:7 — Scope Declaration and Rationale"
line_start: 21877
line_end: 21882
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

### A.15.1:7 - Scope Declaration and Rationale

* **Applicability:** Use the same occurrence test for pragmatic costing, architectural accountability, teaching examples, and source or evidence questions; when the current claim is only about a description, publication, source, or evidence relation, apply the governing pattern for that claim.
* **Scope declaration:** Universal; temporal semantics and episode policy are **context‑local** via `U.BoundedContext`.
* **Rationale:** Gives FPF a clean, actionable notion of **occurrence** compatible with `U.RoleAssignment`, direct `Work.performedBy = RoleAssignment` wording, and derived `RoleEnactmentFact` when a named fact is needed, so that costing, quality, and audit rest on **runs**, not on plans or recipes.

