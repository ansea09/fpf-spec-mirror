---
chunk_kind: "child"
pattern_id: "C.3.A"
pattern_title: "Typed Guard Macros for Kinds + USM (Annex)"
section_id: "C.3.A:3"
section_title: "Solution Overview (what these guards do)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.3.A/C.3.A__004_solution-overview-what-these-guards-do.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.3.A — Typed Guard Macros for Kinds + USM (Annex)"
  - "C.3.A:3 — Solution Overview (what these guards do)"
line_start: 40587
line_end: 40597
dependencies:
  - "A.2.6"
  - "C.3.x"
keywords:
  - "ESG"
  - "Kind-CAL"
  - "Method-Work"
  - "Typed guard"
  - "USM"
  - "regulatory profile"
---

### C.3.A:3 - Solution Overview (what these guards do)

All guards in this Annex share three invariants:

1. **Fail‑closed.** If any required predicate is undefined/false, the guard **denies** the transition.
2. **Deterministic.** Given a fixed **TargetSlice** (with explicit **Γ\_time**) and published declarations, evaluation yields one outcome.
3. **Separation of concerns.**
   *Typed compatibility* (same‑Context `⊑` or **KindBridge**) is **not** Scope.
   *Scope coverage* is a USM set‑membership judgment over **Context slices**.
   *Assurance penalties* (**Φ(CL)** for scope bridges; **Ψ(`CL^k`)** for kind bridges) reduce **R** only.

