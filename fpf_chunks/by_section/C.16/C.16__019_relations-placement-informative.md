---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:15"
section_title: "Relations - Placement (Informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__019_relations-placement-informative.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:15 — Relations - Placement (Informative)"
line_start: 43769
line_end: 43789
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "B.3"
  - "C.26"
  - "C.26.1"
keywords:
  - "CSLC"
  - "U.DHCMethod(Ref)"
  - "U.EvidenceStub"
  - "U.Measure"
  - "U.Unit"
  - "direct comparability"
  - "measurement"
  - "measurement template"
  - "polarity"
  - "probe-changing-state"
  - "scoring method disclosure"
  - "shared-frame check"
---

### C.16:15 - Relations - Placement *(Informative)*
**Architecture measurement boundary.** `C.32.P2S`, `C.32.PAD`, and `C.32.ADA` may cite C.16 readings only after the characteristic, bearer, scale, coordinate, value, unit when relevant, and admissible use are declared. C.16 readings do not become architecture characteristics, decision criteria, eval programs, evidence, gates, or decision authority by themselves.

**Structural-information measurement boundary.** `C.33`, `C.34`, and `C.35` may name captured structure, lost structure, similarity, preservation, entropy, epiplexity estimate, compression, generated-carrier adequacy, or search-output context. When any of those become a value, score, coordinate, threshold, dashboard reading, or eval result, C.16 and the receiving eval or criteria pattern govern measurement construction and admissible use.

**Precision-restoration relation.** `C.16.P` is the first-stage wording-use restoration pattern for characteristic, scale, coordinate, score, metric, axis, dimension, and related characterization wording when the measurement or characteristic object is not yet recoverable. C.16 keeps the measurement substrate and resumes after the bearer, characteristic, scale, coordinate/value, unit, evidence stub, or exact non-C.16 governing pattern has been recovered.
**C.27 temporal-claim relation.**

- C.27 may flag: a rate/rate-change reading whose admissible use depends on admissible measurement construction, evidence, sampling window, or finite-difference method.
- This pattern keeps: measurement construction, comparability, units, sampling windows, evidence, and admissible metric use.
- Non-admissible use: a rate-change label is not a measurement template, and temporal words such as velocity, acceleration, throughput, cadence, or recovery speed are not admissible measures by themselves.
- Neighboring-pattern use: when load-bearing, the claim cites `baseCharacteristicRef`, the relevant measure reference, sampling window, construction method such as `DHCMethodRef`, and `C16RouteRef`; C.27 keeps only the temporal-claim adequacy question.

**C.28 causal-use relation.** C.16 governs measurement templates, readings, score meanings, scale admissibility, direct comparability, and evidence-stub adequacy. C.28 governs the causal-use relation when the same reading is used to claim effect, intervention success, causal fairness, policy optimality, counterfactual comparison, off-policy causal evaluation, causal-RL evaluation, or causal method superiority. A C.16-admissible measure is therefore not by itself admissible for causal use under C.28.

**Kernel.** MM‑CHR *imports* the canonical Characteristic vocabulary and the CSLC discipline fixed by A.17 and A.18; it does not redefine them. CharacteristicSpace reasoning (for change) lives in the patterns that consume MM‑CHR readings.

**Using patterns.** KD‑CAL, Arch‑CAL and others *instantiate* templates and produce measures; MM‑CHR remains a neutral measurement substrate. Trade‑off analyses and architectural trajectories operate over coordinates that MM‑CHR makes available, not inside MM‑CHR.

**Unification (F‑cluster).** External standards (e.g., ISO 80000 quantity types; W3C SOSA/SSN observable properties; QUDT units/quantity kinds) are related via Concept‑Set rows and Bridges; MM‑CHR treats those alignments as context supplied by F‑patterns, not as local re‑definitions.

