---
chunk_kind: "child"
pattern_id: "F.11"
pattern_title: "Method Quartet Harmonisation"
section_id: "F.11:8"
section_title: "Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.11/F.11__009_invariants-normative.md"
commit_sha: "9a9a42e4d154021ca3f7415e0009a4214832f65f"
heading_path:
  - "F.11 — Method Quartet Harmonisation"
  - "F.11:8 — Invariants (normative)"
line_start: 92625
line_end: 92634
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.3"
  - "A.3.1"
  - "A.3.2"
  - "D.CTX"
  - "E.10.D1"
  - "F.1"
  - "F.10"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.7"
  - "F.9"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Work"
keywords:
  - "Actuation"
  - "Method"
  - "MethodDescription"
  - "Role–Method–Work alignment"
  - "Work"
---

### F.11:8 - Invariants (normative)

1. **DesignRunTag honesty.** Statements about **Method or MethodDescription** (design) **MUST NOT** be used as if they were statements about **Work or Actuation** (run) without an explicit Bridge and Window.
2. **Box discipline.** Every claim about “how”, “recipe”, “run”, or “control output” **MUST** point to the correct box in the quartet.
3. **Context locality.** Terms (*process*, *activity*, *task*, *command*) **MUST** be read as **SenseCells** in their Contexts (F.3); Cross‑context equivalence is a matter for F.7/F.9 Bridges.
4. **Status placement.** *Approved* attaches to MethodDescription; *Observed/Measured* attach to Work; *Satisfied/Violated* attach to clauses about Work outcomes within a **Window** (F.10).
5. **Actuation as Work‑part.** Actuation **MUST** be modelled as **occurring within** (or as a specialised form of) Work on the run stance; it does **not** replace Work.
6. **Naming clarity.** Technical/Plain labels for the quartet **SHOULD** be distinct (F.5); avoid homonymous single‑word labels when Contexts collide.
7. **Bridge guard.** Cross‑context moves **MUST** declare **kind** (≈, ⊑, ⊒, ⋂, ⊥, Interpretation), **CL**, and **Loss** (F.7/F.9).

