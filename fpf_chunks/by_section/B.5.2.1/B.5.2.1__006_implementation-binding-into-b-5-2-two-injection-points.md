---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Creative Abduction with NQD"
section_id: "B.5.2.1:5"
section_title: "Implementation & Binding into B.5.2 (two injection points)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__006_implementation-binding-into-b-5-2-two-injection-points.md"
commit_sha: "d1f696e7c7767705206a8cacd9f6ed48e4dc5b02"
heading_path:
  - "B.5.2.1 — Creative Abduction with NQD"
  - "B.5.2.1:5 — Implementation & Binding into B.5.2 (two injection points)"
line_start: 40808
line_end: 40835
dependencies:
  - "A.17"
  - "A.18"
  - "B.4"
  - "B.5"
  - "B.5.2"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.19"
  - "G.5"
keywords:
  - "Creativity-CHR"
  - "DecisionSubject note"
  - "E/E-LOG"
  - "NQD binding"
  - "Novelty@context"
  - "Q-front"
  - "creative abduction"
  - "declared Q components"
  - "retained exploration/archive evidence"
  - "Γ_nqd.generate"
  - "ΔDiversity_P"
---

### B.5.2.1:5 - Implementation & Binding into **B.5.2** (two injection points)

**Step 2 — Generate candidates.**
**Precondition (USM+RSG).** Generation is permitted only when the **Claim/Work Scope** covers the TargetSlice (USM) **and** the performer’s **RoleAssignment** is in an **enactable RSG state** (Green-Gate law).

When the pattern is imported, replace or *supplement* freeform brainstorming with **NQD‑Generate**; the output is a *pool* of L0 hypotheses annotated by `{N, D, Q, S, I, V?}` **plus provenance/DRR refs**. The abductive step remains *abduction* (a conjecture), now instrumented and diverse by construction.

**Step 3 — Plausibility filters.** Apply B.5.2’s plausibility criteria, now with explicit hooks:

* **Falsifiability** → filter out ideas with no testable predictions in the **Shaping/Evidence** states (B.5 alignment).
* **Explanatory power** → prioritize candidates whose *Q‑improvements* (and attached rationales) align with the framed anomaly.

The *selected* “prime hypothesis” proceeds exactly as in B.5.2: formalize it as a new `U.Episteme` at **L0**, then move to Deduction/Induction.

Primary dominance test: compute the (ε-)Pareto front over the declared `DominanceSet`. When the Context consumes the ordinary default, that means the declared `Q` components. By default, `N (Novelty@context)` and `ΔDiversity_P` act only as tie-breakers unless a policy explicitly promotes them into the dominance set; `S (Surprise)` and `I (Illumination)` are also tie-break/report-only by default; `Use-Value` remains non-dominant unless the active `Q` tuple explicitly includes it.

**Ordinary fallback posture when no narrower local policy is specified**
> Do not mint one local dominance doctrine here. Consume the ordinary default `DefaultId.DominanceRegime` from `G.Core/G.5` together with the active `C.19` policy-side defaults; in ordinary Q-front use this means the declared `Q` components, with `ConstraintFit=pass` as **eligibility gate**.
> **Tie‑breakers:** `Novelty@context`, `ΔDiversity_P`, and `Surprise`; `IlluminationSummary (telemetry summary over Diversity_P)` remains report‑only unless a CAL policy promotes it.
> **Archive:** `K=1`, `ε=0`, deduplication in `CharacteristicSpace`.
> **Policy family:** one uncertainty-aware explore policy family with one declared regime key; `UCB`-class with moderate temperature and `explore_share ≈ 0.3–0.5` is one didactic starter profile, not the semantic default family.
> **Provenance (minimum):** record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef`, `TimeWindow`, `Seeds`.

“**Scope‑of‑claim annotation (descriptive).** Record the **BoundedContext** and **TimeWindow** that delimit where each **N/Q/D** measurement is intended to hold; this is for reasoning traceability only (no operational gates).”

Note — Status `Surprise` (scope and default role):
By default in B.5.2.1, `Surprise` functions solely as a secondary tie‑break among candidates that are otherwise Pareto‑equivalent on the Context’s primary characteristics. A Context policy MAY elevate `Surprise` into the dominance set, allowing it to enter the CreativitySpace dominance alongside the primary characteristics.  If no Context policy is specified, the default tie‑break role applies.

