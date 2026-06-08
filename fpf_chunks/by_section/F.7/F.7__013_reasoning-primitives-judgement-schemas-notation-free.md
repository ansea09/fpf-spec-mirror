---
chunk_kind: "child"
pattern_id: "F.7"
pattern_title: "Concept‑Set Table"
section_id: "F.7:12"
section_title: "Reasoning primitives (judgement schemas, notation‑free)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.7/F.7__013_reasoning-primitives-judgement-schemas-notation-free.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "F.7 — Concept‑Set Table"
  - "F.7:12 — Reasoning primitives (judgement schemas, notation‑free)"
line_start: 71291
line_end: 71336
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

### F.7:12 - Reasoning primitives (judgement schemas, notation‑free)

> All judgements are **pure** (no side effects). “Contexts” are `U.BoundedContext`. `SC(C)` denotes a SenseCell in Context `C`. `CL(X↔Y)` is the congruence level of the **best** Bridge path (F.9) between SenseCells `X` and `Y` (bottleneck along that path).

#### F.7:12.1 - Row licensing

**Form.**
`S = {SC(C₁), …, SC(Cₙ)}, Scope = s, τ(s) = requiredCL ⊢ licensable(S,s) ⇔ (∀ i<j: CL(SC(Cᵢ)↔SC(Cⱼ)) ≥ requiredCL ∧ senseFamily (S) is uniform ∧ stance(S) compatible)`

**Reading.** A set of cells **licenses** a row of scope `s` iff every pair is bridged at or above the **required CL** for that scope, all cells sit in the **same senseFamily**, and **DesignRunTag** is compatible.

#### F.7:12.2 - Bottleneck CL for a row

**Form.**
`RowCL(S) = min_{i<j} CL(SC(Cᵢ)↔SC(Cⱼ))`

**Reading.** The row’s CL is the **minimum** congruence level across all pairs (the weakest link).

#### F.7:12.3 - Scope guard

**Form.**
`licensable(S,s) ∧ s ⊑ s' ⊢ licensable(S,s') only if RowCL(S) ≥ τ(s')`

**Reading.** You may **tighten scope** (use the row for a higher-scope purpose) only if the row’s `CL` meets the **higher threshold** for that scope.

#### F.7:12.4 - Contrast decision

**Form.**
`(∃ i<j: CL(SC(Cᵢ)↔SC(Cⱼ)) < τ(Naming‑only)) ⊢ publish‑contrast(S)`

**Reading.** If even **Naming‑only** cannot be licensed, publish a **contrast row** instead of forcing sameness.

#### F.7:12.5 - Row extension guard

**Form.**
`licensable(S,s) ∧ add SC(Cₖ) ⊢ licensable(S∪{SC(Cₖ)}, s) iff ∀ i: CL(SC(Cᵢ)↔SC(Cₖ)) ≥ τ(s)`

**Reading.** You may add a new cell only if it bridges to **every existing cell** at the row’s scope.

#### F.7:12.6 - Loss disclosure obligation

**Form.**
`licensable(S,s) ∧ (∃ i<j: lossNote on Bridge(SC(Cᵢ),SC(Cⱼ))) ⊢ row must carry ≥1 counter‑example`

**Reading.** Any loss note on any supporting Bridge obliges the row to include a **counter‑example one‑liner**.

