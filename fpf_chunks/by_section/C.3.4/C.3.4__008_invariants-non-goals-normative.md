---
chunk_kind: "child"
pattern_id: "C.3.4"
pattern_title: "RoleMask — Contextual Adaptation of Kinds (without cloning)"
section_id: "C.3.4:7"
section_title: "Invariants & Non‑goals (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.4/C.3.4__008_invariants-non-goals-normative.md"
commit_sha: "66e732dfef7a4a93ff23eec43b3f759a6664652d"
heading_path:
  - "C.3.4 — RoleMask — Contextual Adaptation of Kinds (without cloning)"
  - "C.3.4:7 — Invariants & Non‑goals (normative)"
line_start: 44998
line_end: 45003
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

