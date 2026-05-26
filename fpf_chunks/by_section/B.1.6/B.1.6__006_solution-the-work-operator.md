---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:5"
section_title: "Solution — The Γ\\_work Operator"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__006_solution-the-work-operator.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:5 — Solution — The Γ\\_work Operator"
line_start: 30221
line_end: 30284
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

### B.1.6:5 - Solution — The Γ\_work Operator

**Intent.** Provide a universal, conservative way to compose resource spending across parts and steps, without talking about control‑flow (that is Γ\_method’s job).

#### B.1.6:5.1 - Operator signature

```
Γ_work : (S : Set[U.Work], M_spec : U.MethodDescription?) → W_tot : U.Work
```

* **S — Work set.** A finite set of `U.Work` instances to be rolled up (parts, phases, episodes, or boundary partitions). Each Work MUST carry (or reference) a **Boundary Ledger** (§5.3) and a typed resource ledger on an explicit basis. Where a stock is subdivided, the split uses `PortionOf`; where a run is time‑sliced, the slices use `PhaseOf` (A.14).

  If `S` contains overlaps (shared stocks, shared ports, or overlapping time windows), the fold MUST apply an explicit **overlap / de‑duplication policy** declared in the relevant `U.BoundedContext` (A.15.1:5.3); otherwise the result is undefined (double counting).

* **M_spec — optional.** If present, it provides *ex‑ante* yield/efficiency (η) and declared equivalence maps for **planning** or **basis normalization**. It MUST NOT overwrite measured deltas; planned and measured Work MUST be reported separately (CC‑B1.6.8).

* **Result W_tot — U.Work.** A composite Work whose **resource ledger** is the Γ_work fold of the input ledgers (plus any declared overheads/residuals). It is accompanied by a **Boundary Ledger** (see §5.3) and references its parts for auditability.

> **Do not confuse:** Γ\_work neither schedules nor orders steps; it composes **resource deltas attached to Work**. If you need order, use Γ\_method at design‑time and Work’s run‑time relations (`precedes`, `PhaseOf`, `overlaps`) with Γ\_time for temporal coverage.
#### B.1.6:5.2 - What counts as “Work”

Work is defined **with respect to a declared boundary** of the holon being transformed or assembled:

* **Boundary‑relative delta (conservative form):**
  For any resource type *q* measured on boundary *B* during a run,

  ```
  Work_B(q) = Inflow_B(q) − Outflow_B(q) − ΔStock_inside(q)
  ```

  where **ΔStock\_inside(q)** is the change of internal stock over the run (positive when the stock grows).

* **Embodiment split:**
  Work can be split into **Dissipation** (lost to environment) and **Embodied** (retained in produced holons as state). Both are part of the same Work vector; the split is a reporting choice, not a second algebra.

* **Heterogeneous vectors:**
  Γ\_work treats different resource types as a **typed vector space** (no implicit conversion). Equivalences (e.g., joules↔bits via a declared model) are allowed only if **declared in M\_spec** or in a domain CAL; otherwise vectors remain multi‑dimensional.

#### B.1.6:5.3 - Boundary Ledger (normative output metadata)

Every Γ\_work result **MUST** include a **Boundary Ledger**:

* **(i) Boundary scope:** which `U.Boundary` was used (source holon, ports).
* **(ii) Time window:** start/stop or `PhaseOf` slice identifiers.
* **(iii) Basis:** the ordered list of resource types and units.
* **(iv) Method context & lineage:** reference(s) to the governing `U.MethodDescription`(s) (and, if known, `U.Method`), plus the Work lineage (which Work IDs were folded to produce `W_tot`).
* **(v) Accounting authority:** identity of the system(s) that executed, metered, and/or audited the reported ledgers (often the performer/transformer per Work part, plus the aggregator for a roll‑up).

This ledger is what makes cross‑model Work totals comparable and auditable (A.10).
#### B.1.6:5.4 - The invariant quintet instantiated (overview)

Γ\_work preserves B.1 invariants; the detailed proofs and corner cases are in Part 2.

* **IDEM (idempotence):** Folding a singleton zero‑delta Work (or adding a zero‑delta Work to any fold) does not change totals; the zero‑delta ledger is the identity element.
* **COMM / LOC (local commutativity / locality):** For **independent** boundary/stock partitions, composed Work is additive and independent of local fold order.
* **WLNK (weakest‑link bound):** Effective Work is capped by the scarcest **critical** input on the boundary (no Work can exceed available supply).
* **MONO (monotonicity):** Increasing an available resource cannot decrease Work (for the same boundary and time window); decreasing dissipation or improving η cannot reduce feasibility.
#### B.1.6:5.5 - How Γ\_work relates to Methods (and to Γ\_method)

* **Design‑time:** `M_spec` (a `U.MethodDescription`) may declare an intended yield **η** and admissible equivalences between resource types (e.g., heat→mechanical). These are **assumptions** until validated by run‑time Work.
* **Run‑time:** A `U.Work` instance (enacting a MethodDescription under a `U.RoleAssignment`) produces measured deltas across its declared boundary/time window. Γ\_work composes those deltas; it does not speculate nor retroactively “fix” measurements.
* **Sequencing:** If multiple MethodDescriptions are ordered/branched (process view), use **Γ\_method** to define that coordination at design‑time. At run‑time, model the corresponding segments as Work parts and fold them with Γ\_work (Work adds in serial and parallel), while time coverage is handled by Γ\_time.

> **Didactic tip:** Think of **Γ\_method** as the **coordination story**, and **Γ\_work** as the **receipt of what it cost**, both anchored to the same boundary and time window.
