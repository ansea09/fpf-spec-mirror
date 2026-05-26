---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:6"
section_title: "Archetypal grounding (worked micro‑examples)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__007_archetypal-grounding-worked-micro-examples.md"
commit_sha: "ae1ff1c7a231a2ec78d244b40d7805a5538c6608"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:6 — Archetypal grounding (worked micro‑examples)"
line_start: 29726
line_end: 29762
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

### B.1.4:6 - Archetypal grounding (worked micro‑examples)

Use these as templates; each fits on a page and references the obligations above.

#### B.1.4:6.1 - **Γ\_ctx — U.System (manufacturing route)**

* **Graph:** `Prep SerialStepOf Weld SerialStepOf Paint`; `QC ParallelFactorOf Paint` with a join; scope=`run`.
* **CTX‑IND:** `QC` is independent of `Prep/Weld` state; join requires “painted & inspected” flags aligned.
* **CTX‑ORD:** `σ` is total: `Prep → Weld → Paint`; `QC` runs in parallel with `Paint`, joins at `Finish`.
* **CTX‑WLNK:** Slowest/least reliable step on the critical path caps throughput and assurance.
* **CTX‑MONO:** ↓ duration of `Weld`; ↑ join condition coverage → cannot reduce overall safety.
* **Routing:** Costs/energy are handled per step with **Γ\_work**; structure of subassemblies remains in **Γ\_sys**.

#### B.1.4:6.2 - **Γ\_ctx — U.Episteme (order‑bound argument)**

* **Graph:** `PremiseA SerialStepOf LemmaB SerialStepOf Conclusion`; `Background ParallelFactorOf PremiseA`.
* **CTX‑IND:** `Background` does not alter `LemmaB` assumptions; join checks entailment preconditions.
* **CTX‑WLNK:** Weakest premise on the entailment spine caps the argument’s reliability.
* **SCR:** Γ\_epist on the final `Conclusion` produces a SCR linking every source; Γ\_ctx assures the order.

#### B.1.4:6.3 - **Γ\_time — U.System (asset history)**

* **Carrier:** *This* turbine T‑17.
* **Phases:** `Install [t0,t1)`, `Operate v1 [t1,t2)`, `Overhaul [t2,t3)`, `Operate v2 [t3,t4)`.
* **TIME‑COV:** Intervals cover `[t0,t4)` with no overlap; a gap between `t2` and `t2+ε` is justified as clock resolution.
* **TIME‑WLNK:** The weakest reliability epoch caps lifetime MTTF claimed for `[t0,t4)`.
* **Routing:** Work/energy footprints per phase via **Γ\_work**; structural upgrades (new rotor) are Transformers (A.12), not phases, if identity changes.

#### B.1.4:6.4 - **Γ\_time — U.Episteme (paper revisions)**

* **Carrier:** *This* paper P.
* **Phases:** `Draft v1`, `Review v2`, `Camera‑ready v3`.
* **TIME‑ORD/COV:** Non‑overlapping versions covering the documented interval; v3 supersedes v2, not a parallel branch.
* **TIME‑WLNK:** If v2 violated a key citation, overall reliability over `[v1,v3]` is capped by that epoch unless the violation is explicitly retracted and corrected in v3 (documented change).
* **Routing:** Γ\_epist aggregates the conceptual whole at each version; Γ\_time composes the revision history.


