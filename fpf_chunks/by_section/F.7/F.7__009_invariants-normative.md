---
chunk_kind: "child"
pattern_id: "F.7"
pattern_title: "Concept‑Set Table"
section_id: "F.7:8"
section_title: "Invariants (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.7/F.7__009_invariants-normative.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "F.7 — Concept‑Set Table"
  - "F.7:8 — Invariants (normative)"
line_start: 77769
line_end: 77780
dependencies:
  - "A.6.9"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.BoundedContext"
keywords:
  - "columns"
  - "comparisons"
  - "concept-set"
  - "differences"
  - "row"
  - "table"
---

### F.7:8 - Invariants (normative)

1. **Context‑loyal cells.** Every non‑empty cell is a **SenseCell** address; no minted paraphrases.
2. **Bridge sufficiency.** For a *Concept‑Set* row, **every pair** of filled cells is connected by an **F.9 Bridge path** whose **bottleneck CL** ≥ **Row CL(min)** printed for the row.
3. **Scope declaration.** Each row **MUST** declare a **Row Scope** chosen from a small controlled set (e.g., *Naming-only*, *assignment/enactment-eligibility*, *KD-metric*, *Type-structure*).
4. **senseFamily uniformity.** All cells in a row belong to the **same senseFamily** (Role **or** Status **or** Type-structure **or** Measurement…).
5. **Temporal compatibility.** Either all cells share the **same stance**, or the row is a **contrast row** (no sameness claim).
6. **Loss disclosure.** If any Bridge in the row has a **loss note**, the row **MUST** include a **counter‑example** that illustrates that loss in one line.
7. **No stealth expansion.** Adding a new cell to a row **MUST NOT** lower the printed **Row CL(min)** without updating **Row Scope** or splitting the row.
8. **Parsimony.** A row with only one filled cell is **forbidden** (that would be local talk, not a Cross‑context concept).
9. **Didactic bound.** A row that cannot be read in **≤ 30 seconds** violates didactic primacy and must be split.

