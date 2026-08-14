---
chunk_kind: "child"
pattern_id: "C.19.1"
pattern_title: "Bitter‑Lesson Preference (BLP)"
section_id: "C.19.1:2"
section_title: "Policy clauses (normative; synchronized with Core)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19.1/C.19.1__003_policy-clauses-normative-synchronized-with-core.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "C.19.1 — Bitter‑Lesson Preference (BLP)"
  - "C.19.1:2 — Policy clauses (normative; synchronized with Core)"
line_start: 50331
line_end: 50371
dependencies:
  - "A.0"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "B.1.6"
  - "B.3"
  - "C.16"
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
  - "alpha and delta tolerances"
  - "general-solution preference"
  - "iso‑scale parity"
  - "scale‑amenability"
  - "slope vector"
---

### C.19.1:2 - Policy clauses (normative; synchronized with Core)

**BLP‑1 — Scale‑Audit requirement.**
Any DRR that selects a **narrower hand‑engineered** method, module, platform, system form, organization form, evidence-bearing episteme/work arrangement, or other solution bearer over a **general scale-amenable** alternative while claiming scale advantage, BLP override, selector-facing preference, publication-facing superiority, or durable project-side preference **MUST** include a **Scale‑Audit**:
(a) **Parity harness**: equal **FreshnessWindows**, a common **ComparatorSet**, replicate counts, seed records, and **set-returning** evaluation; **Dominance = ParetoOnly** unless a CAL policy says otherwise (policy‑id cited).
(b) **Budget sweeps**: vary **compute**, **data**, and **FoA** within a fixed safety envelope; **pin** any unsweepable knob and record the invariant.
(c) **Slopes and uncertainty**: report ∂quality over ∂compute, ∂quality over ∂data, and, where applicable, ∂coverage over ∂FoA, with **confidence intervals, error bars, edition pins, and policy pins** in telemetry. Use **bootstrapped confidence intervals** or repeated‑seed estimates; disclose heteroscedasticity handling.
(d) **Resources**: publish resource accounts for time, energy, and FLOPs through **A.15.1**, **B.1.6**, **C.16**, and **A.10** as applicable, and publish assurance deltas under **B.3**.
(e) **Objective vector**: list quality, risk, cost, and only policy-promoted illumination or coverage telemetry metrics.
(f) **DoE recipe**: for ≥2 active knobs, apply a **fractional factorial** or **Latin‑hypercube** with ≥ 3 levels per knob to avoid aliasing; justify any lower design.
(g) **Knee & regret tests**: if claiming a heuristic wins, show either (i) a **knee** inside the audited window for the general method (per SLL‑5 policy thresholds) or (ii) **budget‑constrained regret** over the sweep where the heuristic dominates within CI.

**BLP‑2 — Preference rule with alpha and delta tolerances.**
Among admissible options with comparable assurance within **delta** and budget within **alpha**, prefer the bearer whose **slope vector** **Pareto‑dominates** over the audited range; if no dominance within error bounds, prefer the **more general** bearer; otherwise resolve by the **E and E‑LOG** tie‑breakers declared in policy. Agentic contexts implement this as **ATC‑2**; **BLP_delta_alpha_delta** values live in **ATC.Policy**.

> **BLP‑2.1 — Valid waiver grounds (override transparency).**
> Overrides of BLP‑2 are allowed **only** when:
> • **Admissibility override:** guard rails, ethics, or precedence make the general bearer inadmissible (`E.5`, `E.3`).
> • **Scale‑probe overturn:** under **iso‑scale parity** in the declared **ScaleWindow**, the heuristic **sustainedly outperforms** with uncertainty accounted for.
> • **Complementary bias:** the heuristic is an **inductive bias** that **improves** the general method **without blocking scale** (graceful degradation as `S` grows).
> All overrides record a **BLP-waiver** with rationale, admitted review System, direct waiver-review responsibility relation or exact A.6.RCD missing governor, and expiry or review in the DRR. Any system-role kind or assignment needed by the review Work is cited separately.

**BLP‑2.2 — Task-family specialization compatibility.**
A bounded specialization remains **BLP-compatible** when it is produced by a **general, scale-amenable substrate**, acts as a complementary bias that does not block scale, or survives the ordinary **BLP** comparison discipline on the same declared task family and work target. The specialization may be any narrower bearer relevant to that task family—for example, a method, module, platform variant, system form, organization form, agent behavior, evidence-bearing episteme, or work arrangement. If the user is not claiming scale advantage or overriding a general bearer, a bounded specialization may be used with explicit task family, work target, budget guard rails, and evidence source or evidence locus. A full **Scale-Audit** is required when any of these claims is current: scale advantage, override, selector-facing result declaration, publication-facing superiority, or durable reusable-bearer status. Mere specialization does not trigger it. Apply `BLP` to test whether the narrower current bearer was generated, compared, audited, waived, and overridden admissibly; do **not** require the final local behavior at every moment to look maximally generic.

Low-human-overlap or newly discovered approaches remain admissible when the task family, budget guard rails, and evidence source or evidence locus are explicit by value and the same `Scale‑Audit`, alpha and delta, waiver, and override discipline is preserved.
**BLP‑3 — Minimal‑prescription default.**
Author **rules‑as‑prohibitions** (negative constraints) instead of stepwise scripts; encode limits in **Φ policy tables** and **Φ_plane** and allow agents to **sequence autonomously** within those constraints. Scripts are permissible only when mandated by safety or regulation, or with compelling DRR evidence reviewed under E.3 and E.5.

**BLP‑4 — Heuristic‑Debt register (mandatory).**
Record **Heuristic Debt** only when an admitted heuristic functions as reusable solution-family policy, selector-facing preference, durable override of a general scale-amenable alternative, DRR-backed scale waiver, or project-side choice that claims scale advantage or BLP override. Ordinary local bounded tactics that make no reusable-bearer, scale-advantage, selector-facing, or override claim may remain local and bounded without Heuristic Debt publication. `BLP.HeuristicDebtEntry` is a `C.19.1`-local or `G.11`-linked policy and debt entry; it is not a universal `U.*` record kind unless separately admitted through `F.18`, `C.3`, and `E.9`. For a live debt entry, record scope, admitted review System, direct debt-review responsibility relation or exact A.6.RCD missing governor, expiry or review window, and a de-hardening plan; any exact system-role kind or assignment needed by review Work remains separate. Track the entry in **CalibrationLedger** or **BCT** and cite it in SCR.

**BLP‑5 — Continuous-learning discipline.**
Where product policy allows, enable **feedback‑driven adaptation** (preference learning, critique loops) within Guard‑Rails and privacy controls; disabling adaptation requires DRR justification and review date.

**BLP‑6 — Precedence & safeguards.**
BLP is constitutional (instantiates **P‑10**, **P‑11**, **P‑7**, and **P‑1**), but **does not supersede Guard‑Rails (E.5) or precedence rulings (E.3)**. Where **NQD** or **C.19 E‑LOG** promotes illumination into dominance, **BLP adopts that lens** for the audited window.

**BLP‑7 — Publication discipline.**
Scale‑Audit artefacts **SHALL** be exported to **G.11** with edition pins, CI level, alpha and delta tolerances, ComparatorSet, and **BLP.Policy@Context** reference so downstream selectors can reuse evidence without re‑running audits.

