---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:6"
section_title: "Fold rules (how Γ\\_work composes)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__007_fold-rules-how-work-composes.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:6 — Fold rules (how Γ\\_work composes)"
line_start: 29866
line_end: 29911
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

### B.1.6:6 - Fold rules (how Γ\_work composes)

#### B.1.6:6.1 - Boundary partition (across parts of a whole)
Let the system‑level boundary **B** be covered by a finite family of pairwise‑disjoint sub‑boundaries **{Bᵢ}** (ports, surfaces, interfaces) that together exhaust **B**. For any resource type *q* in the basis:

* **Partition additivity (normative):**

  ```
  Work_B(q) = Σ_i Work_Bi(q)
  ```

  Preconditions: (i) `Bi` are disjoint except for measure‑zero interfaces, (ii) meters are aligned (same units, same time window), (iii) internal stock changes ΔStock\_inside(q) are measured for the *same* closed region bounded by B.
  *Why it matters:* this is the cross‑scale rule that lets part‑level Work totals roll up to the whole without double counting.

#### B.1.6:6.2 - Time slicing (serial runs / phases)
Let the run be split by a set of non‑overlapping intervals **{τⱼ}** that cover the window **τ** (use `PhaseOf` to tag the slices). Then:

```
Work_B(q, τ) = Σ_j Work_B(q, τ_j)
```

This is the **temporal additivity** of Work. It is the Γ\_work analogue of Γ\_time’s coverage rule: we never “smear” or reorder; we sum non‑overlapping slices.

#### B.1.6:6.3 - Concurrent branches (parallel activity)
When two independent sub‑boundaries **B₁**, **B₂** are active over overlapping time, total Work still **adds**:

```
Work_B(q) = Work_B1(q) + Work_B2(q)
```

Independence here means: no shared port, no shared stock variable, no hidden transfer between B₁ and B₂ that bypasses the declared meters. If a shared internal stock exists, it must be accounted in ΔStock\_inside(q) for **B** to keep conservation exact.

> **Didactic contrast:** Γ\_method handles **duration** (Σ for serial, max for parallel). Γ\_work handles **resource** (Σ in both serial and parallel), because resource spending composes additively across disjoint boundary parts and disjoint time slices.

#### B.1.6:6.4 - Multi‑resource vectors and declared equivalences
Γ\_work never implicitly converts units. If a planning model needs an exchange (e.g., heat→mechanical, memory→compute), it must be **declared** in `M_spec` (or a domain CAL) as an **equivalence map** `E` applied **before** folding, yielding a new typed basis **E(basis)**. Absent such declaration, vectors remain multi‑dimensional and are added component‑wise.

#### B.1.6:6.5 - Availability gates (weakest‑link discipline)
Many runs require **critical** inputs (a subset **Q\*** of the basis) to be present at or above a threshold. Let `Avail_B(q*)` be the measurable availability for `q* ∈ Q*` on boundary B during τ. Then feasibility is constrained by:

```
Work_B(q*) ≤ Avail_B(q*),  for all q* ∈ Q*
```

If any inequality is violated, the fold **must fail** or the modeller must declare a **Meta‑Holon Transition (B.2)** that introduces redundancy/substitution as a new structural capability (changing Q\* or the equivalence map). This is WLNK in resource form.

