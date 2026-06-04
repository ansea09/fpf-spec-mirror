---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:5"
section_title: "Proof Kit (ready‑to‑reuse obligations for Γ\\_ctx / Γ\\_time)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__006_proof-kit-ready-to-reuse-obligations-for-ctx-time.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:5 — Proof Kit (ready‑to‑reuse obligations for Γ\\_ctx / Γ\\_time)"
line_start: 29425
line_end: 29477
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
keywords:
  - "composition"
  - "order-sensitive"
  - "temporal aggregation"
  - "time-series"
---

### B.1.4:5 - Proof Kit (ready‑to‑reuse obligations for Γ\_ctx / Γ\_time)

This Proof Kit instantiates the generic obligations from **B.1.1 §6** for the order/time flavours. Attach these items whenever you apply Γ\_ctx or Γ\_time to a `DependencyGraph D`.

#### B.1.4:5.1 - Γ\_ctx obligations

* **CTX‑IND (Independence & Joins).**
  Declare **which branches are independent** (no hidden shared state, no side-effects that leak across branches). For every **join**, state a **join-soundness condition** (compatible input and output types plus preconditions and postconditions).
  *Claim:* Under CTX‑IND, parallel folds of independent branches commute locally; any topological sort consistent with `σ` yields the same result (NC‑3).

* **CTX‑ORD (OrderSpec).**
  Provide the **OrderSpec `σ`** as a partial order (or total order) text, including where joins occur.
  *Claim:* Given `D_ctx` and `σ`, the fold is deterministic (NC‑1) and carries a stable **context identifier** (NC‑2).

* **CTX‑WLNK (Critical Path).**
  Identify the **critical path** (or a cutset) whose weakest step caps the property of the whole: throughput, safety, assurance, etc.
  *Claim:* The whole is bounded by the weakest element along the critical path (WLNK).

* **CTX‑MONO (Monotone characteristics).**
  List the characteristics that cannot degrade the whole when improved: e.g., ↓ step duration, ↓ error rate, ↑ step reliability, ↑ join soundness.
  *Claim:* Improving only monotone characteristics cannot make the aggregated process worse (MONO).

* **CTX‑IDEM (Singleton).**
  Provide the one‑step singleton witness: Γ\_ctx of a single `SerialStepOf`‑free node returns that step unchanged (IDEM).

* **CTX‑SCOPE/BOUND.**
  Affirm a **single DesignRunTag** (`design` or `run`) and list any **U.Interaction** that crosses a holon boundary (do not recast it as parthood).

#### B.1.4:5.2 - Γ\_time obligations

* **TIME‑CARR (Carrier Identity).**
  State explicitly the **carrier holon** whose history is being reconstructed.
  *Claim:* All `PhaseOf` arcs refer to the same carrier; if identity changes, model a Transformer producing a new holon (A.12), not another phase.

* **TIME‑COV (Coverage & Non‑overlap).**
  Provide the target **TimeWindow τ** and the list of phases with intervals; justify any gaps or overlaps (resolution limits, business rules).
  *Claim:* Phases cover τ without overlap; otherwise the fold is not admissible (T‑3).

* **TIME‑ORD (Chronological Discipline).**
  Assert that fold order is non‑decreasing in time; reversing adjacent slices is forbidden.
  *Claim:* Temporal idempotence holds on a single slice, and chronological composition preserves consistency (T‑1, T‑2).

* **TIME‑WLNK (Temporal Weakest‑Link).**
  Identify time‑critical constraints: missing essential phases, minimal sampling resolution, minimal integrity of a crucial epoch.
  *Claim:* The property of the whole (over τ) is capped by the weakest phase/epoch.

* **TIME‑MONO (Monotone characteristics).**
  List monotone improvements: ↑ coverage, ↑ timestamp precision, ↑ measurement accuracy, ↑ calibration quality.
  *Claim:* Such improvements cannot degrade the aggregate.

* **TIME‑SCOPE/BOUND.**
  Keep design‑time hypothetical timelines and run‑time actual logs separate; route resource statements for phases to **Γ\_work** (not Γ\_time).

