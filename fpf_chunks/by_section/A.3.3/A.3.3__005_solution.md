---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__005_solution.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:4 — Solution"
line_start: 6839
line_end: 6967
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
  TimeReference:
  Stochasticity:
  InputsOrDisturbances:
  ObservationRelation:
  ConstraintsOrInvariants:
  ApplicabilityWindow:
  CalibrationOrParameterSource:
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
| observation, trace, conformance result, source, or provenance used as evidence | `A.10` and direct evidence-related patterns |
| assurance case, trust calculus, or safety argument | `B.3` or the direct assurance pattern |
| gate passage, release, authority, or permission to act | `A.20`, `A.21`, or the direct gate or authority pattern |
| bounded transformation under conditions | `A.3.4 U.Transformation` |
| freshness, delay, rhythm, currentness, inertia, cadence, or validity window as a positive temporal aspect | `C.27.TA` |
| adequacy or supported use of an authored temporal claim | `C.27` |

#### A.3.3:4.4 - State-space and transition-law fields

```text
U.Dynamics {
  context: U.BoundedContext
  entityOfConcern: EntityOfConcern
  stateSpace: state-space declaration over FPF characteristics
  transitionLaw: claim graph inside U.Dynamics
  timeReference: continuous | discrete | hybrid
  stochasticity: deterministic | stochastic
  inputsOrDisturbances?: CharacteristicSet
  observationRelation?: claim graph or relation reference inside U.Dynamics
  constraintsOrInvariants?: claim graph inside U.Dynamics
  applicabilityWindow?: ConditionSet
  calibrationOrParameterSource?: source or calibration episteme reference
}
```

`stateSpace` is the state-space declaration of this `U.Dynamics` episteme. It uses FPF characteristics with units, scales, and comparability rules, and may cite `A.19` or `C.16` when characteristic or measurement construction is being made. It is not the same object as a receiving-evaluation `CharacteristicSpace` used to score an object for improvement. The dynamics state space may include topology, geometry, aggregation policy, or coordinate transformations when trajectories or comparisons need them.

`transitionLaw` is paradigm-agnostic. It can be an equation, relation, kernel, finite-state transition, queueing model, Bayesian update, Petri-net firing relation, simulation rule, learned predictor, or hybrid model, provided the state space and applicability window are declared.

`transitionLaw`, `observationRelation`, `constraintsOrInvariants`, and `calibrationOrParameterSource` are components or claim graphs inside the `U.Dynamics` episteme unless another governing pattern makes one of them a separately addressable episteme, source, or relation value. Naming one component does not split `U.Dynamics` into several unrelated epistemes.

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

If neither condition is satisfied, prediction does not carry the gate or comparison claim. Use observation, state currentness through `C.27.TA`, use `C.27` when authored temporal-claim adequacy is the concern, or move the gate claim to `A.20`, `A.21`, or the direct authority pattern.

Every use of `Phi_dt` states its applicability window: operating region, horizon, scale band, time step, parameter regime, and source-currentness condition.

#### A.3.3:4.7 - A.3.4, C.27.TA, C.27, and C.29 boundaries

`A.3.4` governs bounded transformation under conditions. A dynamics episteme can model, predict, simulate, or constrain a transformation, but it is not the transformation itself.

`C.27.TA` names positive temporal aspects: freshness, delay, rhythm, currentness, inertia, cadence, trajectory, recovery timing, stabilization timing, and validity window. `C.27` judges adequacy or supported use of authored temporal claims that use those aspects. A `Dyn2TemporalClaimAdequacyCard` or temporal classification is not itself a law of change.

Stay in `A.3.3` when `transitionLaw` or `observationRelation` uses accepted local dynamics, Markov kernels, ODEs, simulations, queueing theory, control theory, or domain theory inside one context.

Use `C.29` when the law depends on contested transfer, cross-domain analogy, learned or speculative mathematical lens, scale change, abstraction, quotienting, or reusable explanation across contexts. The `C.29` output states preserved structure, lost structure, operating-region or scale window, rival lens when current, lens-use boundary value, and stop condition. `A.3.3` remains the governing pattern for state space, transition law, observation, constraints, and calibration semantics.

#### A.3.3:4.8 - Method, mechanism, and governing-pattern constellation boundary

A source label such as `process`, `algorithm`, `dynamics`, `workflow`, `model`, `controller`, or `simulator` may point to linked slot positions under `E.10.ARCH`, not to one typed value. Recover the relevant slots first, then split the linked values:

* `U.Method` for the semantic way of doing;
* `U.MethodDescription` for the representation describing that way;
* `U.Dynamics` for the state-space and transition-law episteme;
* `U.Mechanism` for an admissible operation or law-governed application over a subject kind;
* `U.WorkPlan` and `U.Work` for planned and dated occurrences;
* `TransformationFlowStructure` for selected flow structure when the source is describing a flow-shaped arrangement of transformations;
* evidence, gate, authority, and assurance values when those claims are current.

The linkage among relation positions does not become a process, method, mechanism, dynamics model, plan, work occurrence, or evidence object. Assign one typed value as both `U.Method` and `U.Dynamics` only when a governing pattern explicitly admits that dual typing for the current claim.

