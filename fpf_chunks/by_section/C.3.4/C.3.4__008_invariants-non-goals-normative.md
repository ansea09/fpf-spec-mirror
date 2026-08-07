---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:7"
section_title: "Invariants & Non‑goals (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__008_invariants-non-goals-normative.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:7 — Invariants & Non‑goals (normative)"
line_start: 45450
line_end: 45455
dependencies:
  - "C.2.1"
  - "C.3.1"
  - "C.3.2"
  - "C.3.3"
  - "C.3.A"
keywords:
  - "RoleMask declaration episteme"
  - "candidate-feature constraint"
  - "masked judgment"
  - "stable-refinement review"
  - "vocabulary binding"
---

### C.3.4:7 - Invariants & Non‑goals (normative)

* **No Scope leakage.** RoleMasks **cannot** widen/narrow **Claim scope (G)**; any context conditions are enforced by USM guards.
* **Identity preservation.** The carrier kind remains `k`; RoleMask does not change entityOfConcern.
* **Weakest-link unaffected.** RoleMask declarations do not alter weakest-link rules on F/R; guards route candidate-feature predicates to the exact masked judgment and context predicates to USM Scope.

