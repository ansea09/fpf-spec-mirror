---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics"
section_id: "A.3.3:6"
section_title: "Prediction Use In Gating (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__007_prediction-use-in-gating-normative.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "A.3.3 — U.Dynamics"
  - "A.3.3:6 — Prediction Use In Gating (normative)"
line_start: 6448
line_end: 6455
dependencies:
  - "A.19"
  - "B.4"
keywords:
  - "model"
  - "simulation"
  - "state evolution"
  - "state space"
---

### A.3.3:6 - Prediction Use In Gating (normative)

When **predicted** coordinates (from a dynamics model) are used for **comparison or gating**, one of the following **MUST** hold:
1) a **fresh observation** is available for the gate’s window; or
2) the applied flow/map `Φ_{Δt}` is proven **non‑expansive** (Lipschitz ≤ 1) under the declared distance overlay (see § 5.1.7), **and** it **commutes** with the invariantization step (§ 5.1.6) — i.e., `Quot/Fix_g ∘ Φ_{Δt} = Φ_{Δt} ∘ Quot/Fix_g` on the domain of use.

If neither condition is satisfied, using prediction for gating is **forbidden**; the system **MUST** fall back to observation. Any use of `Φ_{Δt}` **SHALL** declare its validity window (range, Δt).

