---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:2"
section_title: "Policy clauses (normative; synchronized with Core)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__003_policy-clauses-normative-synchronized-with-core.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:2 — Policy clauses (normative; synchronized with Core)"
line_start: 44899
line_end: 44939
dependencies:
  - "A.0"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.5"
  - "E.23"
  - "E.3"
  - "E.5"
  - "F.7"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.8"
  - "G.9"
keywords:
  - "BLP‑waiver"
  - "Scale‑Audit"
  - "general‑method preference"
  - "iso‑scale parity"
  - "scale‑amenability"
  - "slope vector"
  - "α/δ tolerances"
---

### C.19.1:2 - Policy clauses (normative; synchronized with Core)

**BLP‑1 — Scale‑Audit requirement.**
Any DRR that selects a **narrower/hand‑engineered** method over a **general/scalable** alternative while claiming scale advantage, BLP override, selector-facing method preference, publication-facing method superiority, or durable project-side method preference **MUST** include a **Scale‑Audit**:
(a) **Parity harness**: equal **FreshnessWindows**, a common **ComparatorSet**, **replicates/seeds**, **set-returning** evaluation; **Dominance = ParetoOnly** unless a CAL policy says otherwise (policy‑id cited).
(b) **Budget sweeps**: vary **compute**, **data**, and **FoA** within a fixed safety envelope; **pin** any unsweepable knob and record the invariant.
(c) **Slopes & uncertainty**: report ∂quality/∂compute, ∂quality/∂data, and (where applicable) ∂coverage/∂FoA, with **CI/error bars** and **edition/policy pins** in telemetry. Use **bootstrapped CIs** or repeated‑seed estimates; disclose heteroscedasticity handling.
(d) **Resources**: publish **Resrc‑CAL** accounts (time/energy/FLOPs) and assurance deltas (B.3).
(e) **Objective vector**: list **Q/Risk/Cost** and—**only if policy promotes them**—illumination/coverage telemetry metrics.
(f) **DoE recipe**: for ≥2 active knobs, apply a **fractional factorial** or **Latin‑hypercube** with ≥ 3 levels per knob to avoid aliasing; justify any lower design.
(g) **Knee & regret tests**: if claiming a heuristic wins, show either (i) a **knee** inside the audited window for the general method (per SLL‑5 policy thresholds) or (ii) **budget‑constrained regret** over the sweep where the heuristic dominates within CI.

**BLP‑2 — Preference rule (with α/δ tolerances).**
Among admissible options with comparable assurance (within **δ**) and budget (within **α**), prefer the method whose **slope vector** **Pareto‑dominates** over the audited range; if no dominance within error bounds, prefer the **more general** method; else resolve by the **E/E‑LOG** tie‑breakers declared in policy. (Agentic contexts implement this as **ATC‑2**; **BLP_delta_α/δ** live in **ATC.Policy**.)

> **BLP‑2.1 — Valid waiver grounds (override transparency).**
> Overrides of BLP‑2 are allowed **only** when:
> • **Deontic override:** regulation/ethics make the general method inapplicable (E.5/E.3).
> • **Scale‑probe overturn:** under **iso‑scale parity** in the declared **ScaleWindow**, the heuristic **sustainedly outperforms** with uncertainty accounted for.
> • **Complementary bias:** the heuristic is an **inductive bias** that **improves** the general method **without blocking scale** (graceful degradation as `S` grows).
> All overrides record a **BLP‑waiver** with rationale, responsible role, and expiry/review in the DRR.

**BLP‑2.2 — Task-family specialization compatibility.**
A bounded task-family specialization remains **BLP-compatible** when it is produced by a **general, scale-amenable substrate**, when it acts as a complementary bias that does not block scale, or when it survives the ordinary **BLP** comparison discipline on the same declared task family and work target. If the user is not claiming scale advantage or overriding a general method, a bounded task-family specialization may be used with explicit task family, work target, budget guard rails, and evidence source or evidence locus. Full **Scale-Audit** is triggered by scale-advantage, override, selector-facing publication, publication-facing superiority, or durable reusable-method claim, not by the mere existence of specialization. `BLP` therefore governs whether the narrower current method was generated, compared, audited, waived, and overridden admissibly; it does **not** require the final local behavior at every moment to look maximally generic.

Low-human-overlap or newly discovered approaches remain admissible when the task family, budget guard rails, and evidence source or evidence locus are explicit by value and the same `Scale‑Audit`, `α/δ`, waiver, and override discipline is preserved.
**BLP‑3 — Minimal‑prescription default.**
Author **rules‑as‑prohibitions** (negative constraints) instead of stepwise scripts; encode limits in **Φ policy tables** (and **Φ_plane**) and allow agents to **sequence autonomously** within those constraints. Scripts are permissible only when mandated by safety/regulation or with compelling DRR evidence reviewed under E.3/E.5.

**BLP‑4 — Heuristic‑Debt register (mandatory).**
Record **Heuristic Debt** only when an admitted heuristic functions as reusable method-family policy, selector-facing method preference, durable override of a general scale-amenable alternative, DRR-backed scale waiver, or project-side method choice that claims scale advantage or BLP override. Ordinary local bounded tactics that make no reusable-method, scale-advantage, selector-facing, or override claim may remain local and bounded without Heuristic Debt publication. `BLP.HeuristicDebtEntry` is a `C.19.1`-local or `G.11`-linked policy/debt entry; it is not a universal `U.*` record kind unless separately admitted through `F.18`, `C.3`, and `E.9`. For a live debt entry, record scope, responsible role, expiry/review window, and a de-hardening plan; track in **CalibrationLedger/BCT** and cite in SCR.

**BLP‑5 — Continuous‑learning posture.**
Where product policy allows, enable **feedback‑driven adaptation** (preference learning, critique loops) within Guard‑Rails and privacy controls; disabling adaptation requires DRR justification and review date.

**BLP‑6 — Precedence & safeguards.**
BLP is constitutional (instantiates **P‑10/P‑11/P‑7/P‑1**), but **does not supersede Guard‑Rails (E.5) or precedence rulings (E.3)**. Where **NQD/E/E‑LOG** promotes illumination into dominance, **BLP adopts that lens** for the audited window.

**BLP‑7 — Publication discipline.**
Scale‑Audit artefacts **SHALL** be exported to **G.11** with edition pins, CI level, α/δ, ComparatorSet, and **BLP.Policy@Context** reference so downstream selectors can reuse evidence without re‑running audits.

