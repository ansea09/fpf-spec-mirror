---
chunk_kind: "child"
pattern_id: "E.10.D2"
pattern_title: "Intension–Description–Specification Discipline (I/D/S)"
section_id: "E.10.D2:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.D2/E.10.D2__001_intro.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "E.10.D2 — Intension–Description–Specification Discipline (I/D/S)"
  - "E.10.D2:intro — Intro"
line_start: 53575
line_end: 53585
dependencies:
  - "A.7"
  - "C.2.1"
  - "C.2.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.10"
  - "F.15"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
  - "U.EpistemeSlotGraph"
keywords:
  - "I/D/S"
  - "description"
  - "intension"
  - "specification"
  - "testable"
  - "verifiable"
---

## E.10.D2 - Intension–Description–Specification Discipline (I/D/S)

*Definitional pattern — normative, notation‑agnostic*

> **One‑sentence summary.** For every intensional FPF-governed entity (e.g., `U.Role`, `U.Method`, `U.System`, `U.Work`, `U.PromiseContent`), clearly distinguish the **thing itself** (*Intension*), its **context‑bound Description** (KU), and its **formal Specification** (KU). Use **–Spec** only when strict, testable invariants and an acceptance harness exist; otherwise use **–Description**. This keeps semantics clean, didactic, and testable across all FPF patterns.

**Status.** Definitional pattern.
**Builds on:** A.7 **Strict Distinction (Clarity Lattice)**; E.10.D1 **D.CTX (Context ≡ U.BoundedContext)**; C.2.1 **U.EpistemeSlotGraph (DescriptionContext, IDS‑13)**; C.2.3 **Unified Formality Characteristic (F)**.
**Coordinates with.** F.4 **Role Description**; F.5 **Naming Discipline**; F.10 **Evaluation**; F.15 **SCR/RSCR Harness**.
**Non‑goals.** No editors, workflows, registries, or storage formats. No tooling commitments.

