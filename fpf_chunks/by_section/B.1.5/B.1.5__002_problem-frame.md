---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Γ_method — Order‑Sensitive Method Composition & Work Enactment"
section_id: "B.1.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__002_problem-frame.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "B.1.5 — Γ_method — Order‑Sensitive Method Composition & Work Enactment"
  - "B.1.5:1 — Problem frame"
line_start: 30282
line_end: 30294
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

### B.1.5:1 - Problem frame

* **Strict Distinction (A.15)** separates **what a holon is** (structure), **how steps are ordered** (order), **how it unfolds** (time), **what it spends** (work/resources), and **what it values** (objectives).
* **Method, MethodDescription, and Work.**

  * **Method** is the **timeless semantic “way of doing”** (a context‑scoped capability; A.3.1): it specifies admissible preconditions, effects, and bounds, independent of any particular run.
  * **MethodDescription** is a **design‑time description** of a Method (knowledge on a carrier). It may be an **imperative step‑graph** (this pattern’s focus) or another admissible description form (functional/logical/dynamics/solver, etc.; A.3.2:4.2).
  * **Work** is the **dated run‑time occurrence** that enacts a pinned MethodDescription under a `U.RoleAssignment`, records concrete **slot fillings** (parameters/carriers), and books the **resource ledger** (A.15.1).
    Calling the description a “process” is common in some domains, but in FPF we keep **Method ≠ MethodDescription ≠ Work** to avoid category errors.
* **A.15 (Role–Method–Work Alignment)** supplies the **typed ordered relations** we need: **SerialStepOf** (strict precedence) and **ParallelFactorOf** (order‑concurrent branches with a join).
* **B.1.4 (Γ\_ctx/Γ\_time)** already handles **non‑commutativity** (order matters) and **temporal slicing**; **B.1.6 (Γ\_work)** handles **resource spending** and **efficiency**.
  **Γ\_method** sits **between** them: it composes methods **by order and capability** and **delegates** resource accounting to **Γ\_work**.

