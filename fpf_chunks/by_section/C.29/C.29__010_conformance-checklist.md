---
chunk_kind: "child"
pattern_id: "C.29"
pattern_title: "Mathematical Lens Use"
section_id: "C.29:9"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29/C.29__010_conformance-checklist.md"
commit_sha: "cda9087f48e0bce2c5f9d5f4389e7e025c7678f5"
heading_path:
  - "C.29 — Mathematical Lens Use"
  - "C.29:9 — Conformance Checklist"
line_start: 58857
line_end: 58892
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.4"
  - "A.19"
  - "A.3.3"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "A.6.RCD"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18.1"
  - "C.19.1"
  - "C.2.P"
  - "C.26"
  - "C.27"
  - "C.27.TA"
  - "C.28"
  - "C.29"
  - "C.31.ASAP"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.18.1"
  - "E.19"
  - "E.8"
  - "E.9"
  - "F.19"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.5"
  - "G.9"
keywords:
  - "LensUseBoundaryValue"
  - "coarse-graining"
  - "invariants"
  - "learned lens"
  - "lens mapping mode"
  - "lost structure"
  - "mathematical lens"
  - "ontology smuggling"
  - "preserved structure"
  - "rival lens"
  - "scale window"
  - "stop condition"
  - "structure-preserving representation"
  - "validation boundary"
---

### C.29:9 - Conformance Checklist

Use this checklist after constructing or delimiting the result in :4.1. Its conditions concern the actual correspondence, consequence and receiving use; a completed form alone does not satisfy them.

| ID | Requirement | Purpose |
|---|---|---|
| `CC-C29-0 Use condition` | Use C.29 only when a mathematical object, formalism, family, learned representation, or simulation object is used for explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer, or when a stable problem needs a first candidate lens that could change the next lens-use action. | Keeps local analogies lightweight. |
| `CC-C29-1 Mathematical move before record` | State the question, choose a concrete object, establish its correspondence and losses, and derive or delimit the consequence before selecting the sufficient record under :4.4. | Keeps recording subordinate to the mathematical work. |
| `CC-C29-2 Named mathematical object` | A mathematical phrase affecting explanation, decision, prediction, publication, comparison, assurance input, bridge, or reusable transfer names a concrete `CandidateMathObject`, not a prestige family label. | Blocks prestige vocabulary. |
| `CC-C29-2a Intervention preservation` | If `LensMappingMode` is abstraction, quotient, coarse-graining, macro-model, or simulation and causal use is being claimed, state whether intervention and counterfactual structure is preserved, approximated, or not claimed, then apply `C.28` for causal-use question and verdict. | Prevents causal abstraction laundering. |
| `CC-C29-3 Lens mapping mode` | State the `C.29`-local lens mapping mode and the concrete correspondence. If bridge semantics are claimed, apply `F.9`. | Makes the correspondence and any needed semantic Bridge explicit. |
| `CC-C29-4 Preserved structure` | State what structure the lens preserves. | Makes transfer testable. |
| `CC-C29-5 Lost structure` | State what does not transfer; if nothing is lost, justify an equivalence or isomorphism claim through the subject pattern. | Prevents map-territory collapse. |
| `CC-C29-6 Invariants exposed` | Name invariants, obstructions, fixed points, symmetries, conservation laws, dualities, distinctions, or diagnostic boundaries. | Makes the lens usefulness visible. |
| `CC-C29-6a First-principles family recovery` | When a first-principles lens-family row from `C.29:4.2b` is used for claim-bearing lens use, recover the concrete `CandidateMathObject` for the candidate family, preserved structure, lost structure, visible payoff, lens-use boundary value, and stop condition or neighboring-pattern application for that family. | Prevents family names such as boundary, cohomology, symmetry, variational, RG, diagonal, composition, probability, information, or structural-information compression from replacing actual MathLensUse recovery. |
| `CC-C29-6b Bounded-observer structural-information lens` | When MDL, epiplexity, compression, graph information, or description-recoverability changes the next lens-use action, recover `TargetPhenomenon`, source episteme or trace, bounded observer, candidate measure or code, mapping mode, preserved and lost selected structure, visible payoff, observation or postulate boundary, source-return condition, lens-use boundary value, and stop condition. | Makes the selected structure, observer and use limit recoverable. |
| `CC-C29-6c Architecture-local lens descriptions` | When `MLU.Description@RGArchitecture`, `MLU.Description@MultilevelLearningFrustration`, or another architecture-local lens description is used for claim-bearing lens use, recover declared scope or scale window, candidate mathematical object, mapping mode, preserved structure, lost structure, source-return condition, next lens-use action, and stop condition; apply the neighboring patterns that define or constrain architecture, scale-preference, measurement, evidence, assurance, selected-set, and decision claims. | Makes scope, lost structure and source return explicit. |
| `CC-C29-7 Lens-bounded prediction or distinction` | State the actual consequence or obstruction, its premises and the use selected under :4.4. For phenomenon prediction or consequential reliance, supply the required applicability and validation account. | Makes the result and its reliance boundary inspectable. |
| `CC-C29-8 State, observation, and evidence separation` | If state, observation, probe, readout, or evidence is being claimed, apply `A.3.3`, `A.19`, `C.16`, or `A.10` as needed. | Prevents passive-read and dashboard mistakes. |
| `CC-C29-8a Receiving use` | When the lens result contributes to a separately governed question, identify that question and follow :4.4.6's receiving action. | Connects the lens result to its receiving use. |
| `CC-C29-9 Scale window` | If scale, universality, knees, exponents, or coarse-graining are being claimed, declare the scale range and use `C.18.1` for scale-law adequacy, `C.19.1` for general method scale preference, and `C.31.ASAP` for architecture scale preference when the respective claim is made. | Prevents universalization. |
| `CC-C29-9a Temporal use boundary` | If the claim being made is about forecast, rate, trajectory, rhythm, recovery, convergence, stabilization, speed, temporal window, or rate-change as sufficient for a use, cite `C.27` or state that temporal adequacy is not being claimed. | Prevents mathematical prediction cues from replacing temporal-claim adequacy. |
| `CC-C29-10 Rival lens discipline` | Start with the principal rival or ordinary fallback; broaden only when the actual selection or superiority question requires it. Name the comparison criterion, cost, reader, scale window or receiving pattern that makes the claim testable. | Keeps the comparison proportionate to the intended use. |
| `CC-C29-10a Validation regime` | Apply :4.4's reliance rule and :4.5a. Phenomenon-model reliance requires validation regime, evaluation slice, uncertainty/approximation, failure case, applicability and any output-change condition. A conditional derivation states its assumptions and loss without claiming empirical adequacy. | Matches validation cost to the actual reliance. |
| `CC-C29-10b Source-use relation` | If a source changes C.29 declared lens use, name its `SourceUseRelation` with source material reference, declared C.29 output or lens-use boundary, source-use disposition, source-currentness or supersession condition, and output-change condition. Include a blocked source-prestige overread only when it passes F.19's plausible-reader test. | Separates the source-use relation from source-use disposition and makes its governing slots recoverable. |
| `CC-C29-10c Source-currentness and return condition` | If source material, source-use family, source-use decision, or a neighboring subject pattern changes the declared lens-use boundary for this output, state `SourceReturnCondition?` or `OutputChangeCondition?` and narrow, demote, replace, retire, or block the claim-bearing use. | Keeps SoTA currentness and neighboring-pattern currentness tied to the declared C.29 output rather than to source prestige or process evidence. |
| `CC-C29-11 LensUseBoundaryValue` | Label `LensUseBoundaryValue` as analogy-only prompt, diagnosticOnly, formal derivation, simulation, empirical fit, accepted domain theory, SoTA-echo candidate, or mechanized proof, with a matching declared-use boundary. | Prevents evidence laundering. |
| `CC-C29-12 No ontology smuggling` | Do not import source-domain ontology without separate proof or evidence and subject pattern. | |
| `CC-C29-13 Stop condition` | State the condition for narrowing, stopping, returning to source material, or applying a neighboring pattern. | Makes closure locally visible. |
| `CC-C29-14 Bridge discipline` | Cross-context mathematical transfer cites `F.9` when semantic correspondence between local senses is needed; Bridge and C.29 fields agree without duplicate writing. | Keeps semantics bounded. |
| `CC-C29-15 Causal-use discipline` | Causal-use claims apply `C.28`; C.29 cannot carry a causal-use verdict by itself. | Blocks causal laundering. |
| `CC-C29-16 Assurance discipline` | Assurance, release, reliability, and engineering-justification claims apply their direct subject patterns: `A.10` for evidence reliance, `B.3` only for an actual named assurance claim, the direct domain pattern for the release, reliability, or engineering-justification result, and relevant G patterns for their claims. | Prevents elegance from raising assurance directly. |
| `CC-C29-17 Meaning recovery` | If wording obscures the object, claim or participants needed for the current lens use, rewrite it so the reader can identify them and take the next lens-use action. Use `C.2.P` only when an unresolved epistemic distinction still prevents selecting or using the relevant pattern. If the meaning cannot be recovered, state the unresolved point and stop the dependent use. Keep ordinary wording when it already supplies the needed meaning. | Makes the statement and its next use recoverable. |
| `CC-C29-18 Plain and Tech balance` | A Plain sentence can remain when it aids recognition; if it makes ontology, evidence, causal, assurance, bridge, gate, work, decision, or use-boundary commitment, that commitment is recovered through the Tech fields or neighboring pattern. | Preserves didactic usefulness without shadow semantics. |
| `CC-C29-20 Repair failed conditions` | For each failed required condition, apply :4.5b and state the resulting repair, narrowed use, return or stop. | Makes the next corrective action or stop explicit. |

