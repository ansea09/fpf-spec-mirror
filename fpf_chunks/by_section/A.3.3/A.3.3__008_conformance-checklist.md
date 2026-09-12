---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__008_conformance-checklist.md"
commit_sha: "7fd134984ec4ca1fd22b8b296e0bbb58aeece4ab"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:7 — Conformance Checklist"
line_start: 9292
line_end: 9321
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.3"
  - "C.16"
  - "C.27"
  - "C.27.TA"
  - "C.29"
keywords:
  - "calibration"
  - "configuration"
  - "constraints"
  - "dynamics"
  - "initial data"
  - "observation relation"
  - "permitted alternatives"
  - "prediction"
  - "predictive memory"
  - "probability law"
  - "simulation"
  - "state construction"
  - "transition law"
---

### A.3.3:7 - Conformance Checklist

**CC-A3.3-1 (Membership and identity).** A.3.3 judges one already identified `U.Episteme`. That same individual is `U.Dynamics` only when its exact C.2.1 `EntityOfConcern` is the changing subject and its ClaimGraph, under its effective `U.ReferenceScheme`, declares both a state space and a transition law. A.3.3 adds no second identity.

**CC-A3.3-2 (Local meanings and applicability).** Interpret characteristic names under the effective `U.ReferenceScheme`. State units, operating region, time base, approximation regime, claim scope when needed, qualification window and source-currentness condition as claim content or their separately governed values.

**CC-A3.3-3 (EntityOfConcern).** Name the changing EntityOfConcern. Joint modeling uses the independently identified joint subject required by :4.1.

**CC-A3.3-4 (State space).** The state description identifies the participants and variable meanings, their allowed combinations, and the information required by the law. Characteristics retain their units, Scales and comparability rules; topology, geometry or coordinate transformations are supplied when the use needs them. Use :4.4.1 when this description must be constructed.

**CC-A3.3-5 (Transition law).** The law states a relation, map, kernel, equation, rule, learned predictor or simulation rule for the declared time base. Its permitted alternatives, conditions selecting among them and any supplied probability law remain recoverable under :4.4.1.

**CC-A3.3-6 (Observation relation).** Evidence use states how exact Work-side facts when present and separately identified work records, telemetry, measurements, observation records, or source records become observed coordinates. Direct observation is declared rather than assumed.

**CC-A3.3-7 (Constraints and applicability).** Constraints, invariants, operating region, approximation regime, parameter range, horizon, and scale window are stated before prediction or gate use.

**CC-A3.3-8 (Control or planning procedure).** When a reusable planning or control way uses the dynamics, identify that Method under A.3.1. Apply A.3.2 to an episteme claimed to describe it; the dynamics membership test remains :4.1.

**CC-A3.3-9 (Observed facts and calibration).** Attach resource actuals, timestamps and observations to the Work, measurement or source they describe. Relate them to the dynamics through :4.5. Apply its C.2.1 identity and edition conditions when calibration changes the model.

**CC-A3.3-10 (Prediction use).** Predicted Coordinates used for comparison or gating state the exact model edition, domain, horizon, currentness, error or uncertainty, and every observation, validation, sensitivity, stability, or normalization-composition condition required by that consumer's policy. No universal non-expansiveness or commutation test substitutes for the direct decision rule.

**CC-A3.3-11 (Temporal use).** State temporal aspects through C.27.TA and establish the adequacy required of an authored temporal claim through C.27, as specified in :4.3.

**CC-A3.3-12 (Representation transfer).** Apply :4.7 when representation transfer changes the law's permitted use, and carry the resulting conditions into the dynamics account.

**CC-A3.3-13 (Source-label repair).** Recover the relation asserted by an ambiguous source label under :4.8 before applying a membership predicate.

**CC-A3.3-14 (Actual change).** When an actual transformation is claimed, establish A.3.4's occurrence basis specified in :4.3. A predicted or simulated trajectory describes change under the model's premises.

