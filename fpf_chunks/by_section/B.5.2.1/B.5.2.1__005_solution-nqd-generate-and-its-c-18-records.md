---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:4"
section_title: "Solution — NQD-Generate and its C.18 records"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__005_solution-nqd-generate-and-its-c-18-records.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:4 — Solution — NQD-Generate and its C.18 records"
line_start: 46602
line_end: 46623
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
---

### B.5.2.1:4 - Solution — **NQD-Generate and its C.18 records**

**Method name (Plain/Unified Tech).** *NQD‑Generate* — a **U.Method** that, given (i) a **HypothesisSpace** and (ii) a **CharacteristicSpace** with a **CoverageGrid**, returns a *finite* candidate package: a current **front over the declared `DominanceSet`** plus the retained archive/tie-break telemetry needed to keep diversity and novelty reviewable without making them default dominance dimensions.

**Minimal signature.**

* **Inputs (declared in MethodDescription):**
 `HypothesisSpace`, `CharacteristicSpace`, `Seeds?`, `Budget (time/compute)`, `EmitterPolicy` (**E/E-LOG policy id**), `QualityMeasures (Q components)`, `NoveltyMetric`, `CoverageGrid/Granularity`, `CellCapacity K? (default=1)`, `EpsilonDominance ε? (default=0)`, `TieBreakPolicy? (S/I)`, `DedupThreshold?`, `Policy(TimeWindow)`, `DeterminismSeed?`

* **Outputs:**
  CandidateSet = {h_i: (desc_i, Q_i, N_i?, D_i?:=ΔDiversity_P(h_i | Pool), S_i?, UseValue_i?), genealogy_i?, provenance_i (including **DHCMethodRef.edition** and **policyId** from E/E-LOG)} where `Q_i` is a vector and `provenance_i` captures generator settings and evaluation sources. The coordinate entries cite the constituted results actually used. When illumination is reported, carry IlluminationSummary separately as a report about its declared retained set. Unused optional readings need not be produced. If Use-Value is present, identify its objective or acceptance criterion and scope. For a gain claim, also identify the baseline and comparison or counterfactual Method; for a predicted reading, identify the model edition and assumptions under C.17. Note: `N`, `D`, `S`, and `I` are archive, tie-break, telemetry, or policy-promoted signals by default; only the declared `DominanceSet` enters the current front. `Use-Value` is decision-side/supporting unless the current Context explicitly declares it inside the active `Q` tuple / `DominanceSet`; when it is only recorded as a side measure, keep it outside dominance.

**Strategy (notation‑neutral).**

1. **Seeding and constructors.** Declare the explanatory question, hypothesis space and permitted variation operators in the MethodDescription. Initialize with admissible seeds: known explanations, random draws under that grammar or prior hypothesis-bearing epistemes with their grounds and limits. Name how an operator constructs a changed explanatory claim, for example by replacing a proposed mechanism or combining two mechanisms under a stated interaction assumption. When there are no seeds, use the declared finite enumeration or sampling rule.
2. **Construct and assess.** Apply the selected variation operators to the seeds or retained candidates within the budget; record each resulting hypothesis and its parent/operator provenance. Then test candidate must-constraints for comparison and evaluate each required Q component. Keep an excluded candidate and its reason distinguishable from a candidate not yet generated. Maintain up to K retained entries per declared cell; obtain only the N, ΔDiversity_P and Surprise readings actually used under C.17, and any required retained-set illumination report. Deduplicate under the declared rule and threshold.
3. **Budget‑bounded loop.** Iterate until budget or coverage‑convergence; return the **(ε‑)Pareto front** over the declared `DominanceSet`. When the Context consumes the ordinary default, that means the declared `Q` components under `DefaultId.DominanceRegime`, not one fresh local doctrine. Keep `N`, `D=ΔDiversity_P`, `Surprise`, and `IlluminationSummary` as archive/tie-break/telemetry signals unless one Context policy explicitly promotes one of them into dominance and records the policy id. `Use-Value` enters dominance only when the current Context explicitly declares it inside the active `Q` tuple; otherwise it may appear as one decision-side/supporting side note.
4. **Traceability.** Emit a **Design Rationale Record (DRR)**: grids/metrics versions, seed(s), policy and `TimeWindow`, which cells were filled, why items were dominated (list **Characteristics**), and how the final set was produced (including `ε`, `K`, and dedup). (Lightweight DRR is permitted per B.4 guidance.)
5. **Algorithmic freedom (informative).** Implementations MAY use MAP‑Elites/illumination, novelty search with local competition, Bayesian/surrogate‑assisted search, or deterministic enumerations; ε‑dominance or knee‑point thinning MAY be used *after* recording the full front in provenance.

> **No kernel growth.** This is a method/work use of `A.3`, `A.15`, and `B.1.5` plus a characteristic-space import; **no new Γ‑operator** is added (per **A.11**).

