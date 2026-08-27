---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:15"
section_title: "Relations - Placement (Informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__017_relations-placement-informative.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:15 — Relations - Placement (Informative)"
line_start: 47143
line_end: 47165
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16.P"
  - "C.2.1"
  - "C.28"
  - "C.29"
  - "G.11"
  - "G.4"
  - "G.6"
keywords:
  - "C.2.1 result episteme"
  - "Characteristic"
  - "Level/Coordinate"
  - "Scale"
  - "Unit"
  - "actual bindings"
  - "bounded later use"
  - "calibration"
  - "comparability"
  - "dated measurement work"
  - "input/output quantities"
  - "measurand"
  - "measurement result"
  - "measurement subject"
  - "method"
  - "model"
  - "polarity"
  - "provenance"
  - "uncertainty"
---

### C.16:15 - Relations - Placement *(Informative)*
**Architecture measurement boundary.** `C.32.P2S`, `C.32.PAD`, and `C.32.ADA` may cite C.16 readings only after the characteristic, bearer, scale, coordinate, value, unit when relevant, and admissible use are declared. C.16 readings do not become architecture characteristics, decision criteria, eval programs, evidence, gates, or decision authority by themselves.

**Structural-information measurement boundary.** `C.33`, `C.34`, and `C.35` may name captured structure, lost structure, similarity, preservation, entropy, epiplexity estimate, compression, generated-carrier adequacy, or search-output context. When any of those become a value, score, coordinate, threshold, dashboard reading, or eval result, state the measurement construction and admissible-use assertions under the exact C.16 and evaluation/criteria predicates, with their subject patterns used as locators.

**Precision-restoration relation.** `C.16.P` is the first-stage wording-use restoration pattern for characteristic, scale, coordinate, score, metric, axis, dimension, and related characterization wording when the measurement object is not yet recoverable. C.16 resumes after the measurand or subject, Characteristic, Scale, value, method, model, calibration, work, uncertainty, result episteme, or exact non-C.16 governor has been recovered.
**C.27 temporal-claim relation.**

- C.27 may flag: a rate/rate-change reading whose admissible use depends on admissible measurement construction, evidence, sampling window, or finite-difference method.
- This pattern keeps: measurand and measurement-subject identity, method, model, calibration, input/output quantities, uncertainty, dated work, measurement result, result episteme, comparability basis, units, sampling window, and provenance routing.
- Non-admissible use: a rate-change label is not a measurement template, and temporal words such as velocity, acceleration, throughput, cadence, or recovery speed are not admissible measures by themselves.
- Neighboring-pattern use: when load-bearing, the claim cites `baseCharacteristicRef`, the relevant measure reference, sampling window, construction method such as `DHCMethodRef`, and `C16RouteRef`; C.27 keeps only the temporal-claim adequacy question.

**C.28 causal-use relation.** C.16 governs measurement construction, result interpretation, uncertainty, and direct comparability. C.28 governs the causal-use relation when the same result episteme is used to claim effect, intervention success, causal fairness, policy optimality, counterfactual comparison, off-policy causal evaluation, causal-RL evaluation, or causal method superiority. A C.16-admissible measurement result is therefore not by itself admissible for causal use under C.28.

**Evidence, currentness, and assurance.** Use A.10 and G.6 for source recovery and provenance for the exact method, model, calibration, Work, inputs, result episteme, and later use. Use G.11 for currentness and B.3 for assurance when its threshold is met. Evidence, provenance, currentness, and assurance do not by themselves establish the C.16 measurement result.

**Kernel.** MM‑CHR *imports* the canonical Characteristic vocabulary and the CSLC discipline fixed by A.17 and A.18; it does not redefine them. CharacteristicSpace reasoning (for change) lives in the patterns that consume MM‑CHR readings.

**Using patterns.** KD‑CAL, Arch‑CAL, G.4, and other consumers cite C.16 measurement-result epistemes and then ground their own comparison, evaluation, acceptance, aggregation, or decision work. They do not produce a measurement merely by naming a template, score field, criterion, or evidence profile.

**Unification (F‑cluster).** External standards (e.g., ISO 80000 quantity types; W3C SOSA/SSN observable properties; QUDT units/quantity kinds) are related via Concept‑Set rows and Bridges; MM‑CHR treats those alignments as context supplied by F‑patterns, not as local re‑definitions.

