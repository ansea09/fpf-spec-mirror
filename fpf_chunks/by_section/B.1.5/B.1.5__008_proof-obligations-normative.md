---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Γ_method — Order‑Sensitive Method Composition & Work Enactment"
section_id: "B.1.5:7"
section_title: "Proof obligations (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__008_proof-obligations-normative.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "B.1.5 — Γ_method — Order‑Sensitive Method Composition & Work Enactment"
  - "B.1.5:7 — Proof obligations (normative)"
line_start: 30526
line_end: 30543
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

### B.1.5:7 - Proof obligations (normative)

**At planning time (Γ\_method^plan):**

1. **PO‑PLAN‑ORDER.** Provide `OrderSpec σ`; produce `orderSpecHash`.
2. **PO‑PLAN‑TYPE.** For every edge, show **capability continuity**: `OutType(step_i) ⊢ InType(step_j)` or provide a typed **adapter StepSpec**.
3. **PO‑PLAN‑MIC.** For each step interaction, decide **Promote/Forward/Encapsulate** and justify in MIC.
4. **PO‑PLAN‑CL‑POINTS.** Identify integration edges whose **CL** will matter for B.3; record intended sources of mapping evidence.
5. **PO‑PLAN‑NO‑WORK.** Confirm that costs/resources are **not** aggregated here; point to the planned **Γ\_work** composition (by reference).

**At run time (Γ\_method^run) producing `U.Work`:**

1. **PO‑RUN‑PRE/POST.** Demonstrate that pre‑conditions hold before each step; check post‑conditions after.
2. **PO‑RUN‑NC.** Show compliance with Γ\_ctx **NC‑1..3** (determinism with σ, context hash, partial‑order soundness).
3. **PO‑RUN‑MIC‑HONOUR.** Record that only MIC‑declared external interactions occurred.
4. **PO‑RUN‑WORK.** Attach the **Γ\_work** result (spent resources, yields, dissipation) aligned with the same order/join structure.
5. **PO‑RUN‑ASSURANCE.** Provide the observed values for the cutset steps and the actual **CL** of integration mappings to feed B.3 assurance.

