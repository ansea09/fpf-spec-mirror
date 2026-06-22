---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Γ_method — Order‑Sensitive Method Composition & Work Enactment"
section_id: "B.1.5:11"
section_title: "Rationale (informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__012_rationale-informative.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "B.1.5 — Γ_method — Order‑Sensitive Method Composition & Work Enactment"
  - "B.1.5:11 — Rationale (informative)"
line_start: 31794
line_end: 31802
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

### B.1.5:11 - Rationale (informative)

* **Order is semantic.** Many failures stem from pretending that order does not matter; Γ\_method makes **non‑commutativity** explicit (via Γ\_ctx) while keeping the operator set small.
* **Strict Distinction.** The split between **Method** (semantic), **MethodDescription** (spec), **Work** (occurrence), **Γ\_method** (order/type checks), **Γ\_work** (resource ledgers), and **assurance** implements A.15, preventing category errors (semantics vs execution vs claims).
* **Mereology alignment.** Using **SerialStepOf / ParallelFactorOf** (A.14) keeps method composition orthogonal to structural composition (**ComponentOf**) and temporal phasing (**PhaseOf**).
* **Assurance readiness.** Identifying cutsets and mapping CL points during planning makes B.3 application straightforward and auditable.
* **Interfaces matter.** MIC prevents accidental coupling and makes integration points auditable.
* **Separation of concerns.** Γ\_method composes behaviour; Γ\_work accounts resources; B.3 assesses quality—keeping algebraic reasoning sound.

