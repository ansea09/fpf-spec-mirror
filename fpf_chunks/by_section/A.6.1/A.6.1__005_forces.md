---
chunk_kind: "child"
pattern_id: "A.6.1"
pattern_title: "U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
section_id: "A.6.1:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.1/A.6.1__005_forces.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.6.1 — U.Mechanism - Law‑governed application to a SubjectKind over a BaseType"
  - "A.6.1:3 — Forces"
line_start: 9231
line_end: 9242
dependencies:
  - "A.19"
  - "A.2.6"
  - "A.6.0"
  - "C.16"
  - "E.10.D1"
  - "G.10"
  - "G.11"
keywords:
  - "AdmissibilityConditions"
  - "Bridge‑only"
  - "LawSet"
  - "Mechanism"
  - "OperationAlgebra"
  - "Transport"
---

### A.6.1:3 - Forces

**Locality vs transport.** Semantics are **context-local**; crossing contexts is **Bridge-only** (Part F and B.3); penalties are recorded in **R or R_eff**; **F and G** stay invariant.

**Expressivity vs legality.** Rich operators must stay inside **CHR legality** and **CG-Spec** constraints: no ordinal averages and no cross-unit arithmetic without lawful unit alignment.

**Time determinacy.** Explicit **Γ_time**; no implicit *latest*. (Required in USM’s `ContextSlice`.)

**Slot clarity vs specialisation depth.** Multi‑level specialisations require explicit **SlotSpecs** (A.6.5) and monotone refinement of **ValueKinds**; SlotKinds are stable across levels (no implicit positional parameters).

**Signature hygiene.** Obey `SignatureManifest` discipline (A.6.0:4.4.1): explicit `imports` and `provides`, acyclic imports, and no redeclare. Treat imported signatures as **opaque**: reference only their `provides` symbols and ClaimIds, and keep realizations monotone.

