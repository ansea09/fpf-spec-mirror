---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Γ_method — Order‑Sensitive Method Composition & Work Enactment"
section_id: "B.1.5:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__003_problem.md"
commit_sha: "562813fb466950d9c49bc6d2e76ec2626f4df697"
heading_path:
  - "B.1.5 — Γ_method — Order‑Sensitive Method Composition & Work Enactment"
  - "B.1.5:2 — Problem"
line_start: 29908
line_end: 29917
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.3.1"
  - "B.1"
  - "B.1.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
keywords:
  - "concurrent"
  - "method composition"
  - "plan vs run"
  - "sequential"
  - "workflow"
---

### B.1.5:2 - Problem

Without a dedicated, order‑aware method operator:

1. **DesignRunTag conflation.** Authors mix **MethodDescription** (blueprint) and **Work** (execution), producing artifacts that have both planned and executed attributes.
2. **Order erasure.** Sequences with crucial **pre/post‑conditions** get collapsed into sets; reordering breaks correctness while still “passing” naive aggregation.
3. **Capability mismatches.** Step outputs do not match the next step’s required inputs, but this is hidden in untyped edges; composite methods become non‑executable.
4. **Work leakage.** Costs and resource flows are **inlined** into method definitions; later models double‑count or violate conservation (Γ\_work was created to prevent this).
5. **Synergy by arithmetic.** Throughput or quality jumps caused by **proper joins** or **coordination** are misreported as simple sums or averages—violating WLNK and obscuring when a **Meta‑Holon Transition (B.2)** should be declared.

