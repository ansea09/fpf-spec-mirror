---
chunk_kind: "child"
pattern_id: "C.16"
pattern_title: "Measurement & Metrics Characterization (MM‑CHR)"
section_id: "C.16:15"
section_title: "Relations - Placement (Informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16/C.16__017_relations-placement-informative.md"
commit_sha: "4675defebdedb082b60afbb7d5f581932908920e"
heading_path:
  - "C.16 — Measurement & Metrics Characterization (MM‑CHR)"
  - "C.16:15 — Relations - Placement (Informative)"
line_start: 52586
line_end: 52615
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
  - "Scale order"
  - "Unit"
  - "actual bindings"
  - "bounded later use"
  - "calibration"
  - "comparability"
  - "dated measurement work"
  - "indication-producing procedure"
  - "input/output quantities"
  - "measurand"
  - "measurement result"
  - "measurement subject"
  - "measurement-model construction"
  - "method"
  - "model"
  - "provenance"
  - "uncertainty"
---

### C.16:15 - Relations - Placement *(Informative)*

**Measurement-relation construction.** C.16.MR derives a relation from the sought property, measuring arrangement and consequential influences, and obtains a first conditional result. This construction can support a proposed measurement. For a result from an actual measurement, use the conditions above for the performed work and its interpretation.

**Indication interpretation.** C.16.IR begins with an available measurement relation and determines which values or comparisons an indication supports. Use it when influential unknowns, lost distinctions or uncertainty can change the requested answer. It can return a sufficient bound while other quantities remain unknown.

**Measurement repair.** C.16.RM begins when an existing measurement disagrees with an expectation or cannot resolve the distinction needed for use. It chooses which model, arrangement or calculation to change, recovers a result from the available observations when possible, and tests the changed contribution at the scope of the receiving question.

**Architecture measurement boundary.** `C.32.P2S`, `C.32.PAD`, and `C.32.ADA` may cite C.16 readings only after the characteristic, bearer, scale, coordinate, value, unit when relevant, and admissible use are declared. C.16 readings do not become architecture characteristics, decision criteria, eval programs, evidence, gates, or decision authority by themselves.

**Structural-information measurement boundary.** `C.33`, `C.34`, and `C.35` may name captured structure, lost structure, similarity, preservation, entropy, epiplexity estimate, compression, generated-carrier adequacy, or search-output context. When a claim about any of those uses a value, score, coordinate, threshold, dashboard reading, or eval result, state the measurement construction and admissible-use assertions under the exact C.16 and evaluation/criteria predicates, with their subject patterns used as locators.

**Precision-restoration relation.** `C.16.P` is the first-stage wording-use restoration pattern for characteristic, scale, coordinate, score, metric, axis, dimension, and related characterization wording when the measurement object is not yet recoverable. Once the wording is resolved, use C.16 for the measurement-chain question or the pattern for the recovered non-measurement claim.
**C.27 temporal-claim relation.**

- C.27 may flag: a rate/rate-change reading whose admissible use depends on admissible measurement construction, evidence, sampling window, or finite-difference method.
- This pattern keeps: measurand and measurement-subject identity, method, model, calibration, input/output quantities, uncertainty, dated work, measurement result, result episteme, comparability basis, units, sampling window, and provenance routing.
- Non-admissible use: a rate-change label is not a measurement template, and temporal words such as velocity, acceleration, throughput, cadence, or recovery speed are not admissible measures by themselves.
- Neighboring-pattern use: when load-bearing, the claim cites `baseCharacteristicRef`, the relevant measure reference, sampling window, construction method such as `DHCMethodRef`, and `C16RouteRef`; C.27 keeps only the temporal-claim adequacy question.

**C.28 causal-use relation.** C.16 governs measurement construction, result interpretation, uncertainty, and direct comparability. C.28 governs the causal-use relation when the same result episteme is used to claim effect, intervention success, causal fairness, policy optimality, counterfactual comparison, off-policy causal evaluation, causal-RL evaluation, or causal method superiority. A C.16-admissible measurement result is therefore not by itself admissible for causal use under C.28.

**Evidence, currentness, and assurance.** Use A.10 and G.6 for source recovery and provenance for the exact method, model, calibration, Work, inputs, result episteme, and later use. Use G.11 for currentness and B.3 when an actual named assurance claim is current. Evidence, provenance, currentness, and assurance do not by themselves establish the C.16 measurement result.

**Kernel.** MM‑CHR *imports* the canonical Characteristic vocabulary and the CSLC discipline fixed by A.17 and A.18; it does not redefine them. CharacteristicSpace reasoning (for change) lives in the patterns that consume MM‑CHR readings.

**Using patterns.** KD‑CAL, Arch‑CAL, G.4, and other consumers cite C.16 measurement-result epistemes and then ground their own comparison, evaluation, acceptance, aggregation, or decision work. They do not produce a measurement merely by naming a template, score field, criterion, or evidence profile.

**Unification (F‑cluster).** External standards (e.g., ISO 80000 quantity types; W3C SOSA/SSN observable properties; QUDT units/quantity kinds) are related via Concept‑Set rows and Bridges; MM‑CHR treats those alignments as context supplied by F‑patterns, not as local re‑definitions.

