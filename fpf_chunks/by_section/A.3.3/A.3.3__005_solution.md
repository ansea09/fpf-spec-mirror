---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__005_solution.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:4 — Solution"
line_start: 6594
line_end: 6715
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
  - "A.6.1"
  - "B.3"
  - "B.4"
  - "C.2.P.DR"
  - "C.27"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "F.18"
  - "U.BoundedContext"
  - "U.Mechanism"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "model"
  - "simulation"
  - "state evolution"
  - "state space"
---

### A.3.3:4 - Solution

#### A.3.3:4.1 - Definition

Within a `U.BoundedContext`, `U.Dynamics` is an `U.Episteme` that specifies a **state space** and a **state-transition law** for one or more EntitiesOfConcern, possibly under exogenous inputs, constraints, and observation relations.

`U.Dynamics` can be deterministic or stochastic, continuous, discrete, or hybrid. It can describe physical systems, software services, organizations, episteme states, claim states, resource states, architecture characteristics, or other holons whose state change is being modeled.

It does not prescribe what an agent should do. A semantic way of doing belongs to `U.Method`; an episteme describing that way belongs to `U.MethodDescription`; a dated occurrence belongs to `U.Work`; a planned occurrence belongs to `U.WorkPlan`; a mechanism law belongs to `U.Mechanism`; evidence and assurance claims belong to their own governing patterns.

#### A.3.3:4.2 - Dynamics statement

Use this compact statement when applying the pattern:

```text
Dynamics statement:
  EntityOfConcern:
  BoundedContext:
  StateSpace:
  TransitionLaw:
  TimeBase:
  Stochasticity:
  InputsOrDisturbances:
  ObservationRelation:
  ConstraintsOrInvariants:
  ApplicabilityWindow:
  CalibrationOrParameterBasis:
  PredictionUse:
  EvidenceRelation:
  StopCondition:
```

This statement is not an instruction sequence. It is the smallest episteme-facing record needed to keep the law of change separate from methods, work, evidence, and authority.

#### A.3.3:4.3 - Working distinction table

| Current claim | Governing pattern |
| --- | --- |
| state space and transition law for changing state | `A.3.3 U.Dynamics` |
| semantic way of doing | `A.3.1 U.Method` |
| text, code, diagram, model, proof script, or protocol describing a method | `A.3.2 U.MethodDescription` |
| planned dated work | `A.15.2 U.WorkPlan` |
| dated work occurrence and actuals | `A.15.1 U.Work` |
| mechanism algebra, admissible operation, or law-governed application over a subject kind | `A.6.1 U.Mechanism` and `E.20` |
| formal object, invariant, postulate set, or mathematical substrate | `A.6.0`, `C.29`, or the direct mathematical pattern |
| observation, trace, conformance result, source, or provenance used as evidence | `A.10` and evidence-neighbor patterns |
| assurance case, trust calculus, or safety argument | `B.3` or the direct assurance pattern |
| gate passage, release, authority, or permission to act | `A.20`, `A.21`, or the direct gate or authority pattern |
| freshness, delay, rhythm, currentness, inertia, or validity window of a claim | `C.27` |

#### A.3.3:4.4 - State-space and transition-law fields

```text
U.Dynamics {
  context: U.BoundedContext
  entityOfConcern: EntityOfConcern
  stateSpace: CharacteristicSpace
  transitionLaw: U.Episteme
  timeBase: continuous | discrete | hybrid
  stochasticity: deterministic | stochastic
  inputsOrDisturbances?: CharacteristicSet
  observationRelation?: U.Episteme
  constraintsOrInvariants?: U.Episteme
  applicabilityWindow?: ConditionSet
  calibrationOrParameterBasis?: U.Episteme
}
```

`stateSpace` uses FPF characteristics with units, scales, and comparability rules. It may include topology, geometry, aggregation policy, or coordinate transformations when trajectories or comparisons need them.

`transitionLaw` is paradigm-agnostic. It can be an equation, relation, kernel, finite-state transition, queueing model, Bayesian update, Petri-net firing relation, simulation rule, learned predictor, or hybrid model, provided the state space and applicability window are declared.

`observationRelation` separates state from what can be measured, sampled, logged, estimated, or inferred. Identity observation is allowed only when the context says the state coordinate is directly observed.

#### A.3.3:4.5 - Evidence, prediction, conformance, drift, and calibration

Let `D` be a `U.Dynamics` in context `C`, and let `W` be dated `U.Work` records or observation records produced under `C`.

| Derived value | Meaning |
| --- | --- |
| `trace(W, D)` | ordered observed values produced by applying `D.observationRelation` to work records, telemetry, source records, or measurements |
| `initialState(W, D)` | stated, measured, or estimated state at trace start |
| `predict(D, initialState, inputs, horizon)` | trajectory or distribution generated by the transition law over the declared horizon |
| `insideOperatingRegion(D, state)` | check against constraints, invariants, and applicability window |
| `residuals(D, trace)` | discrepancies between predicted and observed values under a stated alignment |
| `fits(D, trace, tolerancePolicy)` | conformance verdict under a declared tolerance, likelihood, interval, or distributional policy |
| `drift(D1, D2, domain)` | divergence between two dynamics versions over a declared operating domain |

Calibration outcomes produce a new or updated dynamics episteme. They do not turn the old law into a dated work record and do not make the new law authoritative for gates without the gate pattern.

#### A.3.3:4.6 - Prediction use in comparison or gating

When predicted coordinates from `U.Dynamics` are used for comparison, release, gate, assurance, or work-preparation use, one of these conditions must hold:

1. a fresh observation is available for the gate or comparison window; or
2. the applied transition map `Phi_dt` is declared non-expansive under the declared distance structure, and the transition commutes with the invariantization or quotient step on the domain of use.

If neither condition is satisfied, prediction does not carry the gate or comparison claim. Use observation, reopen `C.27`, or move the gate claim to `A.20`, `A.21`, or the direct authority pattern.

Every use of `Phi_dt` states its applicability window: operating region, horizon, scale band, time step, parameter regime, and source-currentness condition.

#### A.3.3:4.7 - C.27 and C.29 boundaries

`C.27` may flag a temporal claim whose downstream use depends on a reusable transition law, prediction, simulation, calibrated control, or formal model. `A.3.3` keeps the law: state space, transition law, observation relation, constraints, simulation, prediction, calibration, and model-applicability discipline. A `Dyn2TemporalClaimAdequacyCard` or temporal classification is not itself a law of change.

Stay in `A.3.3` when `transitionLaw` or `observationRelation` uses accepted local dynamics, Markov kernels, ODEs, simulations, queueing theory, control theory, or domain theory inside one context.

Use `C.29` when the law depends on contested transfer, cross-domain analogy, learned or speculative mathematical lens, scale change, abstraction, quotienting, or reusable explanation across contexts. The `C.29` output states preserved structure, lost structure, operating-region or scale window, rival lens when current, lens-use boundary value, and stop condition. `A.3.3` remains the governing pattern for state space, transition law, observation, constraints, and calibration semantics.

#### A.3.3:4.8 - Method, mechanism, and governing-pattern constellation boundary

A source label such as `process`, `algorithm`, `dynamics`, `workflow`, `model`, `controller`, or `simulator` may point to linked slot positions under `E.10.ARCH`, not to one typed value. Recover the relevant slots first, then split the linked values:

* `U.Method` for the semantic way of doing;
* `U.MethodDescription` for the representation describing that way;
* `U.Dynamics` for the state-space and transition-law episteme;
* `U.Mechanism` for an admissible operation or law-governed application over a subject kind;
* `U.WorkPlan` and `U.Work` for planned and dated occurrences;
* evidence, gate, authority, and assurance values when those claims are current.

The linkage among relation positions does not become a process, method, mechanism, dynamics model, plan, work occurrence, or evidence object. Do not assign one typed value as both `U.Method` and `U.Dynamics` unless a governing pattern explicitly admits that dual typing for the current claim.

