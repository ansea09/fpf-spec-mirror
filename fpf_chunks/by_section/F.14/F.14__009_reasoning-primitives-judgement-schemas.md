---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti‑Explosion Control (Roles & Statuses)"
section_id: "F.14:8"
section_title: "Reasoning primitives (judgement schemas)"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__009_reasoning-primitives-judgement-schemas.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "F.14 — Anti‑Explosion Control (Roles & Statuses)"
  - "F.14:8 — Reasoning primitives (judgement schemas)"
line_start: 74665
line_end: 74694
dependencies:
  - "F.1"
  - "F.10"
  - "F.11"
  - "F.12"
  - "F.13"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.7"
  - "F.8"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:8 - Reasoning primitives (judgement schemas)

> Pure mental moves; no tools, no workflows.

Let **`rowOf(τ)`** be the Concept‑Set row of template **τ**, **`senseOf(τ)`** its SenseCell, **`win(τ)`** its window set.

1. **Row reuse admissibility**
   `intent(τₙ) ≡ intent(row r) ∧ ∃σ: senseOf(σ) in r ⊢ reuseRow(τₙ → r)`
   *Reading:* If the proposed template’s intent matches an existing row with a local SenseCell, reuse the row.

2. **Bundle recommendation**
   `alwaysTogether{α,β} ∧ distinct(α,β) ⊢ bundle({α,β})`
   *Reading:* If two distinct Roles occur together by design, name the Bundle.

3. **SoD necessity**
   `conflictRisk{α,β} ∧ sameHolder ∧ sameWindow ⊢ SoD(α ⟂ β)`
   *Reading:* If the same Holder in the same window would create a conflict, require SoD.

4. **Hybrid rejection**
   `SoD(α ⟂ β) ⊢ forbid(hybrid(α,β))`
   *Reading:* A SoD pair cannot be fused into one Role.

5. **Windowing over multiplication**
   `status σ showsVariantsAcross(w₁,…,wₖ) ⊢ keepOneStatus(σ) ∧ win(σ)={w₁,…,wₖ}`
   *Reading:* Variants across time/scale become windows, not new Status names.

6. **Facet over rename**
   `modifier m changes circumstance ¬ essence ⊢ preferFacet(τ,m)`
   *Reading:* If a modifier alters circumstances only, represent it as a facet/window.

