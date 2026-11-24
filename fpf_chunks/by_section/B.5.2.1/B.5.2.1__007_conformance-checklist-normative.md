---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
section_id: "B.5.2.1:6"
section_title: "Conformance Checklist (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__007_conformance-checklist-normative.md"
commit_sha: "cadc8eb15721be464193af85206e345f34a64b04"
heading_path:
  - "B.5.2.1 — Instrument Abductive Hypothesis Generation with Novelty–Quality–Diversity (NQD)"
  - "B.5.2.1:6 — Conformance Checklist (normative)"
line_start: 52658
line_end: 52690
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


**CC‑B.5.2.1‑1 (CHR discipline).** If this pattern is applied in a Context, that Context **SHALL** declare the Creativity‑CHR **Characteristics** used by the generation and comparison with **A.18**‑style templates (type, unit/range, polarity).

**CC‑B.5.2.1‑2 (Instrumented generation).** When Step 2 calls for new generation, the performer **SHALL** invoke *NQD‑Generate* or use a Context-specific generator justified as equivalent for the required measurable Characteristics. A matching existing package may supply a commission to assess the returned candidates. A commission to perform a new run requires that execution.

**CC-B.5.2.1-3 (Diversity coupling).** An addition score `D` SHALL identify the candidate and retained baseline to which its `ΔDiversity_P` applies, with the common measurement basis required by C.17:5.1. For the score used in a past decision, recover the baseline used then. For a claim about the net change from several admissions or a replacement, account for the resulting membership on both sides of that comparison.

**CC-B.5.2.1-Eligibility.** The MethodDescription SHALL state applicable input/seed conditions. Any actual generation Work SHALL meet its independently governed authority, assignment, scope/window and permission conditions. Assess each generated candidate’s must-constraints before admitting it to the comparison/front that consumes ConstraintFit; a result about that candidate SHALL NOT be a precondition for creating it. Preserve exclusions and their reasons.

**CC‑B.5.2.1‑4 (Non‑dominated candidate front).** The *CandidateSet* **MUST** include the front for the identified eligible comparison population under the declared `DominanceSet`. A claim of completeness for a wider domain SHALL account for that domain at the requested distinction between candidate identities and objective values (C.18:4.4). If the Context consumes the ordinary default, cite that consumed `DefaultId.DominanceRegime` rather than restating one local default doctrine. Every exclusion SHALL retain its reason.

For a dominance exclusion, identify the eligible rival and decisive coordinates when known. An argument showing that every jointly admissible account contains a dominating rival also suffices, even if the rival changes between accounts. Cite the rule for deduplication, archive retention or thinning when used. Preserve the complete computed front for its stated population before thinning and label the thinned result separately.

`N`, `D=ΔDiversity_P`, `Surprise`, `IlluminationSummary`, and similar signals enter dominance only under an explicit recorded promotion policy; otherwise they remain archive, tie-break, or telemetry signals.

**CC‑B.5.2.1‑4a (Archive companion when retained exploration is in scope).** If the active policy depends on retained exploration, stepping-stone retention, or open-ended search, the emitted candidate package **MUST** include the corresponding `ExplorationArchive`. Supply the archive when the commission calls for it. Where the commission permits a run without an archive and the policy allows that mode, cite the policy id for the choice.

**CC-B5.2.1-5 (Hypothesis-led testing).** Before claiming empirical corroboration, the practitioner SHALL derive the consequences needed to interpret the test and retain how the tested hypothesis was obtained. Generation SHALL NOT assign an assurance level, require a new experiment or prescribe the next reasoning contribution independently of the receiving question.

**CC-B.5.2.1-6 (Coordinate comparability).** Dominance SHALL use compatible readings on each declared coordinate and its polarity. Any required transformation SHALL be explicit and preserve the comparator's relevant order distinctions; heterogeneous units across different coordinates alone SHALL NOT trigger mandatory normalization.

**CC‑B.5.2.1‑7 (Use‑Value separation).** If Use‑Value (C.17 §4.2) is recorded outside the active `DominanceSet`, it SHALL remain outside Assurance scores and MAY inform decision lenses (Decsn‑CAL). If the Context places `Use-Value` inside the active `Q` tuple, record that declaration together with its objective id / acceptanceSpec. Do not alter **R/G** semantics based on side-measure Use‑Value. (see **C.17 §4.2** for `Use-Value` and `ValueGain` definitions)

**CC‑B.5.2.1‑8 (Provenance).** Each `h_i` in the *CandidateSet* **MUST** reference its `provenance_i` sufficient to reproduce scores given the same `Policy(TimeWindow)`, score/metric versions, and `DeterminismSeed?`.

**CC‑B.5.2.1‑9 (Secondary metrics).** **I (illumination)** and **S (surprise)** SHALL be used only for tie‑breaking/reporting unless explicitly promoted by policy; the **primary dominance test uses the declared `DominanceSet`**, which under the ordinary default means the context-declared `Q` components.

**CC‑B.5.2.1‑10 (Cell capacity & ε).** If `K>1` or `ε>0` are used, the values MUST be declared and recorded in provenance; any thinning after recording the front SHALL be documented in the generation and comparison account.

**CC-B.5.2.1-11 (Dominance set).** If the Context consumes the ordinary default `DefaultId.DominanceRegime`, the active dominance set **SHALL be the declared `Q` components** and provenance **SHALL** cite that consumed default plus the active C.19 policy or lens id. Any `Novelty@context` or `ΔDiversity_P` tie-break SHALL be named by that policy and use a constituted result on a compatible basis; an unused optional reading need not be produced. Promotion into dominance SHALL be explicit and recorded with the policy id.

