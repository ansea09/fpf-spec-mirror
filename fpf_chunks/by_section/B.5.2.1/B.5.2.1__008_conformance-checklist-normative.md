---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:6"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__008_conformance-checklist-normative.md"
commit_sha: "3dae70bd0ef74188bc5ed0414e6630331457d07b"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:6 — Conformance Checklist (normative)"
line_start: 46661
line_end: 46676
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

### B.5.2.1:6 - Conformance Checklist (normative)

**CC‑B.5.2.1‑1 (CHR discipline).** If this pattern is applied in a Context, that Context **SHALL** declare the Creativity‑CHR **Characteristics** with **A.18**‑style templates (type, unit/range, polarity). No new kernel terms are introduced.
**CC‑B.5.2.1‑2 (Instrumented generation).** Step 2 of **B.5.2** **SHALL** either (a) invoke *NQD‑Generate* or (b) justify a Context‑specific generator of equivalent effect (diversity + quality + novelty with measurable **Characteristics**).
**CC-B.5.2.1-3 (Diversity coupling).** Whenever a `D` reading is used, it SHALL be `ΔDiversity_P` computed against the current candidate Pool using the C.17 definition of `Diversity_P` under the same Context, CharacteristicSpace, kernel and TimeWindow.
**CC-B.5.2.1-Eligibility.** The MethodDescription SHALL state applicable input/seed conditions. Any actual generation Work SHALL meet its independently governed authority, assignment, scope/window and permission conditions. Assess each generated candidate’s must-constraints before admitting it to the comparison/front that consumes ConstraintFit; a result about that candidate SHALL NOT be a precondition for creating it. Preserve exclusions and their reasons.
**CC‑B.5.2.1‑4 (Non‑dominated candidate front).** The *CandidateSet* **MUST** include the **Pareto front** over the declared `DominanceSet`. If the Context consumes the ordinary default, cite that consumed `DefaultId.DominanceRegime` rather than restating one local default doctrine. Every exclusion SHALL retain its actual reason. A dominance exclusion names the dominating candidate and declared coordinates; deduplication cites its equivalence or distance rule; archive retention and post-front thinning cite their policies. Preserve the complete computed front before thinning and label a thinned result separately. `N`, `D=ΔDiversity_P`, `Surprise`, `IlluminationSummary`, and similar signals enter dominance only under an explicit recorded promotion policy; otherwise they remain archive, tie-break, or telemetry signals.
**CC‑B.5.2.1‑4a (Archive companion when retained exploration is in scope).** If the active policy depends on retained exploration, stepping-stone retention, or open-ended search, the emitted candidate package **MUST** include the corresponding `ExplorationArchive` or cite one explicit policy id that says archive mode is disabled for that run.
**CC-B5.2.1-5 (Hypothesis-led testing).** Before claiming empirical corroboration, the practitioner SHALL derive the consequences needed to interpret the test and retain how the tested hypothesis was obtained. Generation SHALL NOT assign an assurance level, require a new experiment or prescribe the next reasoning contribution independently of the receiving question.
**CC-B.5.2.1-6 (Coordinate comparability).** Dominance SHALL use compatible readings on each declared coordinate and its polarity. Any required transformation SHALL be explicit and preserve the comparator's relevant order distinctions; heterogeneous units across different coordinates alone SHALL NOT trigger mandatory normalization.
**CC‑B.5.2.1‑7 (Use‑Value separation). ** If Use‑Value (C.17 §4.2) is recorded outside the active `DominanceSet`, it SHALL remain outside Assurance scores and MAY inform decision lenses (Decsn‑CAL). If the current Context explicitly places `Use-Value` inside the active `Q` tuple, record that declaration together with its objective id / acceptanceSpec. Do not alter **R/G** semantics based on side-measure Use‑Value. (see **C.17 §4.2** for `Use-Value` and `ValueGain` definitions)
**CC‑B.5.2.1‑8 (Provenance).** Each `h_i` in the *CandidateSet* **MUST** reference its `provenance_i` sufficient to reproduce scores given the same `Policy(TimeWindow)`, score/metric versions, and `DeterminismSeed?`.
**CC‑B.5.2.1‑9 (Secondary metrics).** **I (illumination)** and **S (surprise)** SHALL be used only for tie‑breaking/reporting unless explicitly promoted by policy; the **primary dominance test uses the declared `DominanceSet`**, which under the ordinary default means the context-declared `Q` components.
**CC‑B.5.2.1‑10 (Cell capacity & ε).** If `K>1` or `ε>0` are used, the values MUST be declared and recorded in provenance; any thinning AFTER recording the front SHALL be documented in the DRR.
**CC-B.5.2.1-11 (Dominance set).** If the Context consumes the ordinary default `DefaultId.DominanceRegime`, the active dominance set **SHALL be the declared `Q` components** and provenance **SHALL** cite that consumed default plus the active C.19 policy or lens id. Any `Novelty@context` or `ΔDiversity_P` tie-break SHALL be named by that policy and use a constituted result on a compatible basis; an unused optional reading need not be produced. Promotion into dominance SHALL be explicit and recorded with the policy id.

