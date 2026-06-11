---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:8"
section_title: "Invariants — edge cases and proof sketches"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__009_invariants-edge-cases-and-proof-sketches.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:8 — Invariants — edge cases and proof sketches"
line_start: 30680
line_end: 30715
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

### B.1.6:8 - Invariants — edge cases and proof sketches

#### B.1.6:8.1 - IDEM (idempotence)
Let `S = {W}` be a singleton Work set. If the resource ledger carried by `W` satisfies `Work_B(q)=0` for all basis components *q* (i.e., no net delta across the declared boundary over the window), then

```
Γ_work(S) = 0  (the zero vector)
```

Trivial by definition: no measured boundary‑relative delta implies zero spent‑resource Work.

#### B.1.6:8.2 - COMM/LOC (local commutativity / locality)
Let `S` be partitioned into independent subsets `{Sᵢ}` whose boundary partitions `{Bᵢ}` are disjoint and cover **B** (6.1). Since each subset’s ledger is evaluated with its own meters and time slices (6.2), and vector addition is commutative/associative, any local fold order yields the same `Σ_i Γ_work(Sᵢ)`. Hence Γ\_work inherits commutativity/locality **under independence**.
*Note:* If subsets share a stock variable (or an undeclared transfer), independence fails and the modeller must either (i) refactor boundaries / Work decomposition to restore independence, or (ii) model the shared stock explicitly in ΔStock\_inside(q) for the **parent** B.

#### B.1.6:8.3 - WLNK (weakest‑link)
Let **Q\*** be the critical input set with availability caps `Avail_B(q*)`. Since the delta definition measures **net** consumption across B (inflow–outflow–Δstock), and no external creation is allowed, each `Work_B(q*)` cannot exceed `Avail_B(q*)`. If the plan suggests more, you have either (a) a measurement error, (b) a missing equivalence declaration in `M_spec`, or (c) a true emergent synergy that must be modelled as **MHT** (new redundancy/substitution capability).

#### B.1.6:8.4 - MONO (monotonicity)
Monotonicity is interpreted along three characteristics; in all cases “improvement” never makes the whole **worse** (i.e., never increases required Work nor decreases feasibility):

* **Availability monotonicity:** Increasing `Avail_B(q)` for any non‑critical q leaves `Work_B(q)` unchanged (availability is not auto‑consumed); increasing it for a critical q cannot increase `Work_B(q)` and weakly increases feasibility.
* **Yield monotonicity (η):** For a fixed output target, increasing declared or measured **η** weakly **decreases** the required `Work_B(q)` in the inputs, never increases it.
* **Loss monotonicity:** Decreasing dissipation (better insulation, better compression) weakly **decreases** `Dissipated_B(q)`; total Work cannot go up as a result.

#### B.1.6:8.5 - Compatibility with Γ\_method
Let a process be composed by Γ\_method from steps `{S_k}`, each with its own boundary partition `{B_k}` and time slice `{τ_k}`. If independence holds between steps at the resource boundary level (no hidden cross‑leaks), the summed Work

```
Σ_k Work_Bk(q, τ_k)
```

is invariant to any topological sort consistent with Γ\_method’s order (Γ\_method may change *when* costs are incurred; Γ\_work adds *how much* is spent).

**Manager note.** When reviewing a plan, inspect **Γ\_method** (is the order/capability sound?). When reviewing results, inspect **Γ\_work** (do the boundary‑relative deltas and units make sense?). Use **PhaseOf** to align both views over time.

