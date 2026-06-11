---
chunk_kind: "child"
pattern_id: "C.18"
pattern_title: "Open‑Ended Search Calculus (NQD‑CAL)"
section_id: "C.18:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.18/C.18__005_solution.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "C.18 — Open‑Ended Search Calculus (NQD‑CAL)"
  - "C.18:4 — Solution"
line_start: 43405
line_end: 43453
dependencies:
  - "A.1"
  - "A.15"
  - "A.17-A.19"
  - "B.5.2.1"
  - "C.16"
  - "C.17"
  - "C.19"
  - "C.2"
  - "G.11"
  - "G.5"
  - "G.6"
keywords:
  - "CandidateSet"
  - "DescriptorMapRef"
  - "DistanceDefRef"
  - "EmitterPolicyRef"
  - "Front vs ExplorationArchive"
  - "IlluminationSummary report-only telemetry"
  - "InsertionPolicyRef"
  - "NQD-CAL"
  - "NQDArchive"
  - "provenance editions"
  - "Γ_nqd.generate"
  - "Γ_nqd.illuminate"
  - "Γ_nqd.selectFront"
  - "Γ_nqd.updateArchive"
---

### C.18:4 - Solution
Provide Γ_nqd.* operators and U.Types for DescriptorMap, Archive/Niche, policies, and illumination telemetry summaries; bind measurement legality to MM‑CHR and policy control to E/E‑LOG. (Exports/Type notes/Operator specs below are normative parts of this Solution.)

- Operators (Γ):
  - `Γ_nqd.generate(seed?, EmitterPolicyRef, Budget, DescriptorMapRef, QualityMeasuresRef, NoveltyMetricRef, CoverageGrid, CellCapacity K=1, EpsilonDominance ε=0, DedupThreshold?, InsertionPolicyRef?) → CandidateSet<U.Hypothesis>`
  - `Γ_nqd.updateArchive(Archive, CandidateSet, InsertionPolicyRef?) → Archive'`
  - `Γ_nqd.illuminate(Archive) → IlluminationSummary{coverage, QD-score, occupancyEntropy, filledCells}` (report‑only telemetry summary; not a dominance characteristic unless a policy explicitly promotes it).
  - `Γ_nqd.selectFront(Archive|CandidateSet, characteristics={Q components, Novelty@context, ΔDiversity_P, …}) → ParetoFront`

**Type notes.**
- `U.DescriptorMap (Tech; twin‑labelled Plain) : Hypothesis → ℝ^d` (declares encoder, invariances, version, **CharacteristicSpaceRef**). Publish Tech/Plain per **E.10**; declare `DescriptorMapRef.edition` and `DistanceDefRef.edition`. **Dimensionality rule.** **Require `d≥2` only when QD/illumination surfaces are active**; for non‑QD contexts `d≥1` is lawful.
- `NQD.CandidateSet` ≡ `Set<U.Hypothesis>` with attached per‑item vectors `{Q_i, N_i, D_i:=ΔDiversity_P, S_i?, provenance_i}`.
- `U.NQDArchive` holds per‑cell elites and genealogy refs; context‑local.
- `U.Niche` is a region in CharacteristicSpace (grid bucket / CVT centroid / cluster).
- `U.EmitterPolicyRef` points to a named policy in **C.19 E/E‑LOG**.
- `U.InsertionPolicyRef` — named archive‑update policy (e.g., `replace_if_better | replace_worst | bounded_age | bounded_regret`); versioned.
- `U.IlluminationSummary` is a **telemetry summary** over `Diversity_P` (see C.17), not a dominance characteristic.

**Operator specs (normative).**
- `Γ_nqd.generate(… )` SHALL:
  (a) respect **Budget**,
  (b) compute `{Q_i}` (vector), `N_i` (Novelty@context), `D_i := ΔDiversity_P(h_i | Pool)` under the same CharacteristicSpace & TimeWindow as the Pool, and optional `S_i` (Surprise),
  (c) deduplicate by `DedupThreshold` in CharacteristicSpace,
  (d) record `DescriptorMapRef.edition`, `DistanceDefRef.edition`, `EmitterPolicyRef`, `ε`, `K`, `Seeds`, and genealogy references (parent/seed ids) to enable replay and selection auditing.
- `Γ_nqd.updateArchive` SHALL apply local competition per cell (keep up to K elites), preserve genealogy, and **enact the declared `InsertionPolicyRef`**; default is `replace_if_better` with deterministic tie‑breakers.
- `Γ_nqd.illuminate` SHALL return coverage and QD‑score computed against the declared grid and archive edition.
- `Γ_nqd.selectFront` SHALL compute the (ε‑)Pareto front over the declared characteristics; **Illumination** is excluded by default (report‑only).

**Pipeline:** apply **Eligibility (ConstraintFit=pass)** → **Dominance over the declared `DominanceSet`** → **Tie‑breakers (`Novelty@context`, `ΔDiversity_P`, `Surprise`; `Illumination` telemetry metric)**. When the context relies on the ordinary default, consume `DefaultId.DominanceRegime` from `G.Core/G.5` together with the active `C.19` emitter/archive policy instead of restating one local dominance doctrine here.
**Ordinary default Q-front mode:** When no narrower promotion policy is declared, dominance stays on the context-declared `Q` components while `N/ΔD` work through archive occupancy and tie-breakers. Any deviation SHALL be declared by policy id and recorded in provenance.

**Reproducibility & editions.** Each call SHALL emit provenance sufficient for replay: `{DHCMethodRef.edition, DescriptorMapRef.edition, EmitterPolicyRef (params), **InsertionPolicyRef**, DedupThreshold?, ε, K, Seeds, TimeWindow}`.
Telemetry hook: whenever IlluminationSummary increases (Δcoverage>0 or ΔQD‑score>0), the Context SHALL emit a Telemetry(PathSlice) record that cites {EmitterPolicyRef, DescriptorMapRef.edition, DistanceDefRef.edition, InsertionPolicyRef?, TimeWindow}. (Aligns with G.6/G.7/G.11 `PortfolioMode`/edition constraints.)

**Measurement alignment.** `Novelty@context`, `Use‑Value (ValueGain)`, `Surprise`, `Diversity_P` SHALL be measured per **C.17** (MM‑CHR templates). **IlluminationSummary** is a telemetry summary over `Diversity_P` (coverage/QD‑score); when CharacteristicSpace includes domain‑family cells, publish grid id and FamilyCoverage, plus **DescriptorMapRef.edition/DistanceDefRef.edition**.
.

#### C.18:4.1 - Front and archive are different returns

- Start from one declared `EligibilitySet`.
- Return the non-dominated `Front` over the declared `DominanceSet`.
- When archive mode is active, return the corresponding `ExplorationArchive` separately.
- Archive membership may use novelty, diversity, stepping-stone potential, or coverage policy and is not by itself evidence of membership in the current `Q-Front`.
- Keep `TieBreakerSet` and `TelemetrySet` explicit so diversity or illumination signals do not silently rewrite the front semantics.
- Use `RetentionIntent=steppingStone` when the point of retention is frontier expansion rather than current dominance.
- Here `EligibilitySet`, `DominanceSet`, `TieBreakerSet`, and `TelemetrySet` are comparison-bundle sets, while `RetentionIntent=steppingStone` is one archive-retention field value; none of them renames the returned `Front` or `ExplorationArchive`.
- If one line keeps both returns, say that the front answers current non-domination while the archive answers retained exploration value.
- When retained exploration value depends on future reachability or curriculum expansion across transitions, cite the declared reachability or transfer rule together with `LearningProgressSignal`, `CompetenceModelRef`, or `GoalSpaceExpansionCue`. That bridge stays archive/pool-policy-side unless one explicit policy promotes it; it does not require the heavier atlas layer and it does not rewrite front semantics.

