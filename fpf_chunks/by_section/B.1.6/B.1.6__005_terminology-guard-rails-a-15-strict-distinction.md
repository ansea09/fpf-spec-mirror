---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:4"
section_title: "Terminology guard‑rails (A.15 — Strict Distinction)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__005_terminology-guard-rails-a-15-strict-distinction.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:4 — Terminology guard‑rails (A.15 — Strict Distinction)"
line_start: 29792
line_end: 29801
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "B.1"
  - "B.1.2"
  - "B.1.4"
  - "B.1.5"
  - "C.5"
keywords:
  - "Resrc-CAL"
  - "cost"
  - "energy consumption"
  - "resource aggregation"
  - "work"
---

### B.1.6:4 - Terminology guard‑rails (A.15 — Strict Distinction)

> These rules are normative in this pattern; they exist to prevent the recurring confusion noted in prior drafts.

* **Method (U.Method)** — design‑time, abstract **way‑of‑doing** inside a bounded context; **not** an execution; it may be described by multiple MethodDescriptions and may or may not admit any step decomposition.
* **MethodDescription (U.MethodDescription)** — a design‑time `U.Episteme` that describes a Method (SOP/algorithm/proof/simulator/solver configuration, control law, or other viewpoint). A step/workflow graph is only one possible representation.
* **Process (view)** — a chosen representation of a MethodDescription as an ordered/partially‑ordered structure (steps, branches, synchronization); composed by **Γ\_method**.
* **Work (U.Work)** — a run‑time **occurrence**: dated enactment of a MethodDescription by a performer under a `U.RoleAssignment`. In this pattern, **Work** is treated under its *spent‑resource ledger* facet; composed by **Γ\_work**.
* **Transformer (T)** — a `U.System` playing the executing and/or auditing role for Work’s accounting (A.12); transformer identity belongs in the **Boundary Ledger**.
* **Mereology for resources (A.14):** use `PortionOf` for **quantitative splits** and `PhaseOf` for **time‑slices**; **do not** use `MemberOf` for resource stocks.
