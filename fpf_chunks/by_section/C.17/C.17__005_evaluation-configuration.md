---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty and Value"
section_id: "C.17:3"
section_title: "Evaluation configuration"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__005_evaluation-configuration.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "C.17 — Characterising Generative Novelty and Value"
  - "C.17:3 — Evaluation configuration"
line_start: 49533
line_end: 49549
dependencies:
  - "A.0"
  - "A.1.1"
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.15.2"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.2.1"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.1.6"
  - "B.3"
  - "B.4"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "E.10.LRN"
  - "F.18"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.5"
  - "U.Mechanism"
keywords:
  - "ConstraintFit"
  - "Novelty"
  - "Use-Value"
  - "bounded quantitative result"
  - "evidence"
  - "incomparability"
  - "named comparison basis"
  - "qualitative-first evaluation"
  - "uncertainty"
---

### C.17:3 - Evaluation configuration

The configuration must make these questions answerable:

- Which bearer is evaluated, for which use and ClaimScope, over which selected slices and window?
- Which CharacteristicSpace and `A.19.ECS` specification supply the Characteristics, Scales, value meanings, missingness rules, and admissible comparisons?
- Which finite corpus or reference set supplies the comparison basis, and how were its members admitted?
- Which Method, model, encoder, distance definition, calibration, and uncertainty basis produced or supports each value?
- If the Method compares a representation or observation instead of the bearer directly, which bearer and representation or observation are related, what describing, projection, measurement, or other stated relation supports the inference, and do the corpus members use a compatible comparison basis? If not, state the mapping and relevant loss.
- Which objective, acceptance criterion, and must-constraints are current, and which source epistemes state them? Their inclusion in the configuration does not make their claims true.
- If the result claims improvement or gain, which baseline and comparison or counterfactual Method make the difference testable?
- Which evidence supports the difference, consequence, coordinate, or comparison conclusion, and what use may rely on it?

For each objective, criterion, or constraint on which the result depends, keep its EntityOfConcern, effective ReferenceScheme, edition or currentness basis, and subject-defined predicate recoverable. Do not use a generic container label to answer several of these questions at once. Add only the source, scheme, scope, model-use, comparison, or evidence relation the current claim needs.

Keep prospective and observed readings distinct. A prospective reading may use a surrogate model and stated assumptions to compare designs before use; an observed reading uses later Work, service, or other outcome evidence. Do not overwrite the prediction as though it had been an observation. Preserve both results when the comparison matters, and reopen only the coordinates and conclusions that relied on the superseded prediction.

