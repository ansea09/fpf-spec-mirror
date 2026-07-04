---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__008_conformance-checklist.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:7 — Conformance Checklist"
line_start: 7172
line_end: 7199
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
  - "C.2.P.DR"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "F.18"
  - "U.BoundedContext"
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

**CC-A3.3-1 (Type).** `U.Dynamics` is an `U.Episteme` for a state-space and transition-law claim. It is not `U.Method`, `U.MethodDescription`, `U.WorkPlan`, `U.Work`, `U.Mechanism`, evidence, assurance, or gate authority.

**CC-A3.3-2 (Bounded context).** Every `U.Dynamics` is declared inside a `U.BoundedContext`. Units, characteristic names, operating region, time base, approximation regime, and source-currentness condition are local to that context.

**CC-A3.3-3 (EntityOfConcern).** The changing EntityOfConcern is named. It may be a physical holon, service, organization, episteme, claim portfolio, architecture, resource bundle, or other holon with modeled state.

**CC-A3.3-4 (State space).** The state space enumerates characteristics with units, scales, comparability rules, and any needed topology, geometry, aggregation policy, or invariantization rule.

**CC-A3.3-5 (Transition law).** The transition law states a relation, map, kernel, equation, rule, learned predictor, or simulation rule suitable for the declared time base and stochasticity.

**CC-A3.3-6 (Observation relation).** Evidence use states how work records, telemetry, measurements, or source records become observed coordinates. Direct observation is declared rather than assumed.

**CC-A3.3-7 (Constraints and applicability).** Constraints, invariants, operating region, approximation regime, parameter range, horizon, and scale window are stated before prediction or gate use.

**CC-A3.3-8 (No imperative overread).** `U.Dynamics` does not prescribe agent steps, responsibilities, or ordered work occurrences. Planning or control methods that use dynamics belong to `U.Method` and `U.MethodDescription`.

**CC-A3.3-9 (No actuals on dynamics).** Resource actuals, timestamps, work logs, and telemetry attach to work, evidence, or source values. Calibration creates a new or revised dynamics episteme.

**CC-A3.3-10 (Prediction use).** Predicted coordinates used for comparison or gating require fresh observation or a declared non-expansive, invariant-commuting transition map over the domain of use.

**CC-A3.3-11 (Temporal boundary).** Positive temporal aspects stay with `C.27.TA`; temporal-claim adequacy, freshness-use, delay-use, rhythm-use, inertia-use, and currentness-use claims stay with `C.27`; reusable transition laws stay with `A.3.3`.

**CC-A3.3-12 (C.29 boundary).** Contested, cross-domain, learned, speculative, scale-changing, or transferable mathematical-lens use is assigned to `C.29`; `A.3.3` keeps the dynamics semantics.

**CC-A3.3-13 (Source-label repair).** `Process`, `workflow`, `algorithm`, `model`, `controller`, `simulator`, and `dynamics` wording must not be repaired to `U.Dynamics` until the current slot is recovered: method, method description, work plan, dated work, selected transformation-flow structure, transition-law claim graph, evidence relation, or another governed value.

