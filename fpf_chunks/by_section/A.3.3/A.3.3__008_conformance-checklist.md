---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__008_conformance-checklist.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:7 — Conformance Checklist"
line_start: 9220
line_end: 9249
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.5"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "F.18"
  - "F.19"
  - "U.ClaimScope"
  - "U.Mechanism"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Transformation"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "calibration"
  - "dynamics"
  - "observation relation"
  - "prediction"
  - "simulation"
  - "state space"
  - "transition law"
---

### A.3.3:7 - Conformance Checklist

**CC-A3.3-1 (Membership and identity).** A.3.3 judges one already identified `U.Episteme`. That same individual is `U.Dynamics` only when its exact C.2.1 `EntityOfConcern` is the changing subject and its ClaimGraph, under its effective `U.ReferenceScheme`, declares both a state space and a transition law. A.3.3 adds no second identity.

**CC-A3.3-2 (Semantic locality without a container).** Local meanings and characteristic names are interpreted under the effective `U.ReferenceScheme`; units, operating region, time base, approximation regime, claim scope when needed, qualification window and source-currentness condition remain explicit claim content or separately governed values. Its C.2.1 identity is determined by ClaimGraph, EntityOfConcern, and effective U.ReferenceScheme.

**CC-A3.3-3 (EntityOfConcern).** The changing EntityOfConcern is named. It may, for example, be a physical holon, service, organization, episteme, claim portfolio, architecture, resource bundle, or other EntityOfConcern with modeled state.

**CC-A3.3-4 (State space).** The state space enumerates characteristics with units, scales, comparability rules, and any needed topology, geometry, aggregation policy, or invariantization rule.

**CC-A3.3-5 (Transition law).** The transition law states a relation, map, kernel, equation, rule, learned predictor, or simulation rule suitable for the declared time base and stochasticity.

**CC-A3.3-6 (Observation relation).** Evidence use states how exact Work-side facts when present and separately identified work records, telemetry, measurements, observation records, or source records become observed coordinates. Direct observation is declared rather than assumed.

**CC-A3.3-7 (Constraints and applicability).** Constraints, invariants, operating region, approximation regime, parameter range, horizon, and scale window are stated before prediction or gate use.

**CC-A3.3-8 (No imperative overread).** `U.Dynamics` does not prescribe agent steps, responsibilities, or ordered work occurrences. A reusable planning or control way that uses dynamics is `U.Method`; only a separately identified claim-bearing episteme that passes A.3.2 is its `U.MethodDescription`.

**CC-A3.3-9 (No actuals on dynamics).** Resource actuals, timestamps, Work occurrences, work logs, and telemetry remain claims about their exact Work, record, evidence use, measurement, or source use under the applicable subject patterns. Calibration Work and its domain result may support a later dynamics episteme with its own C.2.1 identity; a continuing edition relation obtains only when C.2.1's separate predicate does.

**CC-A3.3-10 (Prediction use).** Predicted Coordinates used for comparison or gating state the exact model edition, domain, horizon, currentness, error or uncertainty, and every observation, validation, sensitivity, stability, or normalization-composition condition required by that consumer's policy. No universal non-expansiveness or commutation test substitutes for the direct decision rule.

**CC-A3.3-11 (Temporal boundary).** Positive temporal aspects stay with `C.27.TA`; adequacy or supported use of authored temporal claims stays with `C.27`; reusable transition laws stay with `A.3.3`.

**CC-A3.3-12 (C.29 boundary).** Contested, cross-domain, learned, speculative, scale-changing, or transferable mathematical-lens use is assigned to `C.29`; `A.3.3` keeps the dynamics semantics.

**CC-A3.3-13 (Source-label repair).** `Process`, `workflow`, `algorithm`, `model`, `controller`, `simulator`, and `dynamics` wording must not be repaired to `U.Dynamics` until the current slot is recovered: method, method description, work plan, dated work, selected transformation-flow structure, transition-law claim graph, evidence relation, or another governed value.

**CC-A3.3-14 (Actual-transformation boundary).** Possible, predicted, simulated, or probable change remains claim content. An actual `U.Transformation` requires the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification.

