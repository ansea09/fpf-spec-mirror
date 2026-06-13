---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__002_problem-frame.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:1 — Problem frame"
line_start: 31122
line_end: 31134
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

### B.1.6:1 - Problem frame

FPF distinguishes **what is done** from **what it costs** to do it.

* **Method, MethodDescription, and design-time process:**
  A **Method** is the abstract **way‑of‑doing** inside a bounded context (A.15). A **MethodDescription** is a design‑time `U.Episteme` that describes a Method (SOP, algorithm, proof, simulator configuration, etc.).
  A **Process** is a *view* that represents a MethodDescription as an ordered/partially‑ordered composition (steps, branches, synchronization). In Cluster B, that ordering/coordination is handled by **Γ\_method** (B.1.5). **Not every MethodDescription admits a step decomposition**; Γ\_method applies only when a step/process view is chosen.

* **Work (run‑time; this pattern focuses on the resource facet):**
  **Work** is the dated run‑time **occurrence** of enacting a MethodDescription by a performer under a `U.RoleAssignment` (A.15). In this pattern we treat Work under its **spent‑resource facet**: the typed delta we can account for across a declared boundary and time window. Γ\_work defines how those deltas compose across parts and phases.

This separation makes models auditable and prevents category errors: **Γ\_method** composes *design‑time coordination* (a process view); **Γ\_work** composes *run‑time Work ledgers* (and never smuggles order semantics).

