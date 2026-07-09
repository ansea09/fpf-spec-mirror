---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Creative Abduction with NQD"
section_id: "B.5.2.1:4"
section_title: "Solution — Binding to Γ_nqd.generate (C.18)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__005_solution-binding-to-nqd-generate-c-18.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "B.5.2.1 — Creative Abduction with NQD"
  - "B.5.2.1:4 — Solution — Binding to Γ_nqd.generate (C.18)"
line_start: 36986
line_end: 37007
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

### B.5.2.1:4 - Solution — **Binding to Γ_nqd.generate (C.18)**

**Method name (Plain/Unified Tech).** *NQD‑Generate* — a **U.Method** that, given (i) a **HypothesisSpace** and (ii) a **CharacteristicSpace** with a **CoverageGrid**, returns a *finite* candidate package: a current **front over the declared `DominanceSet`** plus the retained archive/tie-break telemetry needed to keep diversity and novelty reviewable without making them default dominance dimensions.

**Minimal signature.**

* **Inputs (declared in MethodDescription):**
 `HypothesisSpace`, `CharacteristicSpace`, `Seeds?`, `Budget (time/compute)`, `EmitterPolicy` (**E/E-LOG policy id**), `QualityMeasures (Q components)`, `NoveltyMetric`, `CoverageGrid/Granularity`, `CellCapacity K? (default=1)`, `EpsilonDominance ε? (default=0)`, `TieBreakPolicy? (S/I)`, `DedupThreshold?`, `Policy(TimeWindow)`, `DeterminismSeed?`

* **Outputs:**
  CandidateSet = {h_i: (desc_i, Q_i, N_i, D_i:=ΔDiversity_P(h_i | Pool), S_i, I_i, UseValue_i?), genealogy_i?, provenance_i (including **DHCMethodRef.edition** and **policyId** from E/E-LOG)} where `Q_i` is a vector and `provenance_i` captures generator settings and evaluation sources. If Use‑Value is present, include the objective id / acceptanceSpec, counterfactual method (if predicted), and model edition per C.17. Note: `N`, `D`, `S`, and `I` are archive, tie-break, telemetry, or policy-promoted signals by default; only the declared `DominanceSet` enters the current front. `Use-Value` is decision-side/supporting unless the current Context explicitly declares it inside the active `Q` tuple / `DominanceSet`; when it is only recorded as a side measure, keep it outside dominance.

**Strategy (notation‑neutral).**

1. **Seeding.** Initialize with seeds (known solutions, random draws, or prior L0 hypothesis epistemes).
2. **Iterated illumination.** Propose variations, evaluate **Q** (per‑component); maintain up to **K** elites per cell (or descriptor bucket); compute **N/D/S/I** on the fly; deduplicate by `DedupThreshold` in **CharacteristicSpace**.
3. **Budget‑bounded loop.** Iterate until budget or coverage‑convergence; return the **(ε‑)Pareto front** over the declared `DominanceSet`. When the Context consumes the ordinary default, that means the declared `Q` components under `DefaultId.DominanceRegime`, not one fresh local doctrine. Keep `N`, `D=ΔDiversity_P`, `Surprise`, and `IlluminationSummary` as archive/tie-break/telemetry signals unless one Context policy explicitly promotes one of them into dominance and records the policy id. `Use-Value` enters dominance only when the current Context explicitly declares it inside the active `Q` tuple; otherwise it may appear as one decision-side/supporting side note.
4. **Traceability.** Emit a **Design Rationale Record (DRR)**: grids/metrics versions, seed(s), policy and `TimeWindow`, which cells were filled, why items were dominated (list **Characteristics**), and how the final set was produced (including `ε`, `K`, and dedup). (Lightweight DRR is permitted per B.4 guidance.)
5. **Algorithmic freedom (informative).** Implementations MAY use MAP‑Elites/illumination, novelty search with local competition, Bayesian/surrogate‑assisted search, or deterministic enumerations; ε‑dominance or knee‑point thinning MAY be used *after* recording the full front in provenance.

> **No kernel growth.** This is a method/work use of `A.3`, `A.15`, and `B.1.5` plus a characteristic-space import; **no new Γ‑operator** is added (per **A.11**).

