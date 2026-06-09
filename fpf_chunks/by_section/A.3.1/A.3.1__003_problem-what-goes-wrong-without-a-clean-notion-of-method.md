---
chunk_kind: "child"
pattern_id: "A.3.1"
pattern_title: "U.Method"
section_id: "A.3.1:2"
section_title: "Problem (what goes wrong without a clean notion of “method”)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.1/A.3.1__003_problem-what-goes-wrong-without-a-clean-notion-of-method.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "A.3.1 — U.Method"
  - "A.3.1:2 — Problem (what goes wrong without a clean notion of “method”)"
line_start: 5926
line_end: 5932
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3"
  - "B.1"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Dynamics"
  - "U.PromiseContent"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.WorkPlan"
keywords:
  - "abstract process"
  - "how-to"
  - "procedure"
  - "recipe"
---

### A.3.1:2 - Problem (what goes wrong without a clean notion of “method”)

1. **Process soup.** “Process” gets used for recipe, execution, schedule, or org area. Planning, staffing, and audit blur together.
2. **Spec = run fallacy.** A flowchart (or code) is taken as if execution already happened; conversely, logs get mistaken for the recipe.
3. **Role leakage.** People encode assignments inside the recipe (“this step is the surgeon”), tying **who** to **how** and making reuse impossible.
4. **Notation lock‑in.** When “method” is defined as “a set of steps,” functional or logical styles become second‑class citizens and cannot be modeled cleanly.

