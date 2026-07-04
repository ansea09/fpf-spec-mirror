---
chunk_kind: "child"
pattern_id: "E.2"
pattern_title: "The Eleven Pillars"
section_id: "E.2:6"
section_title: "Policy — Bitter‑Lesson Preference (BLP)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.2/E.2__007_policy-bitter-lesson-preference-blp.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "E.2 — The Eleven Pillars"
  - "E.2:6 — Policy — Bitter‑Lesson Preference (BLP)"
line_start: 63815
line_end: 63837
dependencies:
  - "C.18"
  - "C.19"
  - "C.5"
  - "E.1"
  - "E.3"
  - "E.5"
  - "F.7"
  - "F.9"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "P-1 to P-11"
  - "constitution"
  - "core values"
  - "invariants"
  - "pillars"
  - "principles"
  - "rules"
---

### E.2:6 - Policy — Bitter‑Lesson Preference (BLP)

**Intent.** Favor **general, computation‑leveraged**, and **freedom‑of‑action** methods over hand‑tuned, brittle heuristics *when safety and legality are held constant*. This codifies the empirical trend that methods which scale with **data, compute, and search breadth** outpace bespoke rule‑engineering. **Applicability:** beyond ML, this policy covers **search/optimization**, **control**, **simulation‑based inference**, and other computational sciences where capability improves with scale and exploration. When **NQD/E/E‑LOG** promotes **novelty/coverage (illumination)** telemetry into dominance (via an explicit **CAL** policy; **policy‑id recorded in SCR**), these telemetry metrics are included in BLP comparisons for the audited window.

**BLP‑1 — Scale‑Audit Requirement.** Any DRR that selects a more specialized/hand‑engineered method over a general/scalable alternative **MUST** include a **Scale‑Audit**:
* (a) **Parity harness**: same **ComparatorSet**, **freshness window**, and **evaluation seeds/replicates**; set-returning evaluation (see **G.5/G.9**). Dominance criterion: **Pareto‑only** by default across the declared objective vector; any alternative requires a documented waiver by **Gov‑CAL** under **E.3** precedence.
* (b) **Budgets**: sweep **compute** (**steps/tokens/params/time/energy**, as applicable), **data** (size/quality), and **freedom‑of‑action** (from script‑like instructions → minimal prohibitions) **under a fixed risk/safety envelope**. If any parameter cannot be swept, **pin** it and record the invariant.
* (c) **Slopes & uncertainty**: report ∂quality/∂compute, ∂quality/∂data, and (where applicable) ∂coverage/∂**freedom‑of‑action** and **∂novelty/∂budget**; include **error bars/CI** from multi‑seed trials; publish edition pins and policy‑IDs in SCR/telemetry (**G.11**).
* (d) **Resources**: publish **Resrc‑CAL** accounts (time/energy/FLOPs) and assurance deltas (B.3).
* (e) **Objective declaration**: list the **objective vector** (quality, risk, cost, **and any illumination telemetry explicitly promoted into dominance via CAL** with **policy‑id recorded in SCR**) used for Pareto comparison.

**BLP‑2 — Preference Rule.** Given admissibility and comparable assurance (within δ) and budget (within α), prefer the method whose **slope vector** is **Pareto‑dominant** over the audited range (per **BLP‑1c/1e**). If no dominance holds within error bounds, prefer the **more general** method (fewer domain‑specific heuristics, greater transfer via Bridges Φ/Ψ); otherwise resolve via **E/E‑LOG** tie‑breakers declared in policy.

**BLP‑3 — Minimal‑Prescription Default.** Author **rules‑as‑prohibitions** (negative constraints) over step‑by‑step scripts. Encode limits in **Φ policy tables** (and **Φ_plane** where applicable) instead of procedural checklists; allow the agent/system to sequence functions autonomously under those constraints (SoS‑LOG). **Pre/post‑conditions and test harnesses remain permitted**; **scripts** are permissible only when mandated by safety/regulation, or with compelling evidence recorded in the DRR **and reviewed under E.3 precedence / E.5 Guard‑Rails**.

**BLP‑4 — Heuristic‑Debt Register.** Any hand‑tuned rule admitted for pragmatic reasons **MUST** be registered as **Heuristic Debt** with: scope, responsible role, expiry/review window, measurable replacement target under BLP‑2, and a de-hardening/sunset plan. Track in **CalibrationLedger/BCT (Baseline Change Tracker)** and cite in SCR.

**BLP‑5 — Continuous‑Learning Posture.** Where product policy allows, enable **feedback‑driven adaptation** (e.g., preference learning, critique loops) within Guard‑Rails (**E.5**) and privacy/regulatory controls, with appropriate opt‑outs where required. Disabling adaptation requires DRR justification and a review date.

**BLP‑6 — Precedence & Safeguards.** BLP is a **Gov/Arch** policy instantiated by Pillars **P‑10 (Open‑Ended Evolution)**, **P‑11 (SoTA Alignment)**, **P‑7 (Pragmatic Utility)**, and **P‑1 (Cognitive Elegance)**. It does **not** override safety/ethics (**E.5**) **nor** E.3 precedence rulings; where BLP conflicts with Guard‑Rails, **Guard‑Rails prevail**. When **NQD/E/E‑LOG** elevates illumination to dominance for exploration mandates, BLP **adopts that lens** rather than overriding it.

*Informative SoTA contexts (post‑2015):* set-returning selection across **LLM prompt‑programming vs fine‑tuned task models**; **preference‑learning families (RLHF ↔ DPO)**; **QD archives (MAP‑Elites/CMA‑ME/DQD/QDax)**; **open‑ended environment–method co‑evolution (POET‑class)**; **offline RL vs Decision Transformer parity**; and beyond ML, **optimization/control** (model‑based planning vs hand‑tuned controllers) and **simulation‑based inference** in the sciences. These are **illustrative only**; use the parity harness instead of single‑winner leaderboards.

