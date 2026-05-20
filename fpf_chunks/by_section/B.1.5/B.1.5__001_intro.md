---
chunk_kind: "child"
pattern_id: "B.1.5"
pattern_title: "Γ_method — Order‑Sensitive Method Composition & Work Enactment"
section_id: "B.1.5:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5/B.1.5__001_intro.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "B.1.5 — Γ_method — Order‑Sensitive Method Composition & Work Enactment"
  - "B.1.5:intro — Intro"
line_start: 29056
line_end: 29062
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

## B.1.5 - Γ_method — Order‑Sensitive Method Composition & Work Enactment
> **► decided‑by: A.14 Advanced Mereology**
**A.14 compliance —** Methods compose over **SerialStepOf/ParallelFactorOf** on **MethodDescription/Method** graphs (order, not parthood); stuff‑like inputs are modelled via **PortionOf** on resources and accounted in **Γ_work**; method/version history uses **PhaseOf**; mapping quality is handled via **CL** (B.3).

> **Plain‑English headline.**
> **Γ\_method** composes **ordered step specifications** into a **single MethodDescription** (design‑time) that **describes** a composite **Method**, and governs its **run‑time enactment as Work** (pre/post, capability typing, MIC honouring) while delegating **resource accounting** to **Γ\_work** and **order semantics** to **Γ\_ctx**.

