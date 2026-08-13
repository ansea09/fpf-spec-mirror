---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__005_solution.md"
commit_sha: "11f2345e65e4b2ec5b84c0cecde4c9485834d28d"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:4 — Solution"
line_start: 8418
line_end: 8562
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

### A.3.3:4 - Solution

#### A.3.3:4.1 - Definition

`U.Dynamics` is a same-individual dependent kind of `U.Episteme`. Membership holds when one already identified episteme has the changing subject as its exact C.2.1 `EntityOfConcern` and its ClaimGraph, interpreted under the effective `U.ReferenceScheme`, substantively declares both a state space and a state-transition law for that subject. The law may include exogenous inputs, constraints, disturbances, and an observation relation.

The C.2.1 ClaimGraph, exact `EntityOfConcern`, and effective `U.ReferenceScheme` remain the episteme's identity discriminators. A.3.3 adds no context field or second dynamics identity. A `U.ClaimScope`, operating region, applicability window, qualification interval, parameter regime, or scale band enters only through the exact claim that uses it and its subject pattern; changing one can change claim content without becoming an ambient container.

`U.Dynamics` can be deterministic or stochastic, continuous, discrete, or hybrid. It can make state-change claims about physical systems, software services, organizations, epistemes, claim portfolios, resource states, architecture characteristics, or another exact EntityOfConcern. If several subjects are jointly modelled, the exact C.2.1 EntityOfConcern must itself be an independently identified collection, system, or other admitted subject; list proximity does not create one.

It does not prescribe what an agent should do. A semantic way of doing belongs to `U.Method`; an episteme describing one admitted Method belongs to `U.MethodDescription`; a dated occurrence belongs to `U.Work`; a planned occurrence belongs to `U.WorkPlan`; an actual bounded change belongs to `U.Transformation`; a mechanism law belongs to `U.Mechanism`; a selected organization belongs to A.22 `U.Structure`; and evidence, publication, result, reliance, assurance, gate, and authorization claims remain with their subject patterns. None of those objects establishes dynamics membership by being cited, adjacent, displayed, or used.

If empirical grounding is claimed, state the exact C.2.1 `EpistemeEmpiricalGroundingRelation`. A calibration source, observation record, dated calibration Work, evaluation result, A.10 evidence-provenance path, or B.3 assurance claim remains separately identified and does not become an intrinsic grounding field of `U.Dynamics`.

#### A.3.3:4.2 - Dynamics statement

Use this compact aid only when the ordinary sentence is insufficient for the current decision:

```text
Dynamics statement:
  CandidateEpisteme:
  EntityOfConcern:
  EffectiveReferenceScheme:
  StateSpace:
  TransitionLaw:
  TimeReference:
  Stochasticity:
  InputsOrDisturbances:
  ObservationRelation:
  ConstraintsOrInvariants:
  ClaimScopeIfReliedOn:
  OperatingRegionAndApplicabilityWindow:
  CalibrationOrParameterSourceIfReliedOn:
  PredictionUse:
  EvidenceOrAssurancePathIfReliedOn:
  StopCondition:
```

This aid is not an instruction sequence, identity schema, record kind, method description, selected structure, or second carrier. C.2.1 identifies the candidate episteme. The rows expose the minimum claim content and separately governed references needed to keep a law of change distinct from Method, MethodDescription, Structure, Work, actual transformation, result, publication, evidence, reliance, assurance, and authority.

#### A.3.3:4.3 - Working distinction table

| Current claim | Governing pattern |
| --- | --- |
| state space and transition law for changing state | `A.3.3 U.Dynamics` |
| semantic way of doing | `A.3.1 U.Method` |
| claim-bearing episteme whose exact EntityOfConcern is one admitted Method and whose claims substantively describe that Method; text, code, diagram, model, proof script, or protocol may represent those claims | `A.3.2 U.MethodDescription` for membership; `C.29` and publication patterns for representation or availability when current |
| planned dated work | `A.15.2 U.WorkPlan` |
| dated work occurrence and actuals | `A.15.1 U.Work` |
| mechanism algebra, admissible operation, or law-governed application over a subject kind | `A.6.1 U.Mechanism` and `E.20` |
| formal object, invariant, postulate set, or mathematical substrate | `A.6.0`, `C.29`, or the direct mathematical pattern |
| observation, trace, conformance result, source, or provenance used as evidence | `A.10` and direct evidence-related patterns |
| assurance case, trust calculus, or safety argument | `B.3` or the direct assurance pattern |
| gate passage, release, authority, or permission to act | `A.20`, `A.21`, or the direct gate or authority pattern |
| actual bounded change identified by exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification | `A.3.4 U.Transformation` |
| freshness, delay, rhythm, currentness, inertia, cadence, or validity window as a positive temporal aspect | `C.27.TA` |
| adequacy or supported use of an authored temporal claim | `C.27` |

#### A.3.3:4.4 - State-space and transition-law fields

The following is a claim-content view of one C.2.1 episteme, not another object identity or mandatory serialization:

```text
U.Dynamics membership view {
  candidateEpisteme: U.Episteme
  entityOfConcern: EntityOfConcern
  effectiveReferenceScheme: U.ReferenceScheme
  claimGraph: {
    stateSpace: state-space declaration over FPF characteristics
    transitionLaw: state-transition claim
    timeReference: continuous | discrete | hybrid
    stochasticity: deterministic | stochastic
    inputsOrDisturbances?: CharacteristicSet
    observationRelation?: claim or exact relation reference
    constraintsOrInvariants?: claim content
    claimScopeIfReliedOn?: U.ClaimScope
    operatingRegionAndApplicabilityWindow?: ConditionSet
    calibrationOrParameterSourceIfReliedOn?: exact source or calibration-episteme reference
  }
}
```

`stateSpace` is claim content of this `U.Dynamics` episteme. It uses characteristics with local meanings, units, scales, and comparability rules, and may cite `A.19` or `C.16` when characteristic or measurement construction is being claimed. It is not the same object as a receiving-evaluation `CharacteristicSpace` used to score an object for improvement. The dynamics state space may claim topology, geometry, aggregation policy, or coordinate transformations when trajectories or comparisons need them; an independently selected organization among exact constituents and obtaining relations remains A.22 `U.Structure`.

`transitionLaw` is paradigm-agnostic. It can be an equation, relation, kernel, finite-state transition, queueing model, Bayesian update, Petri-net firing relation, simulation rule, learned predictor, or hybrid model, provided the state space, semantic basis, and applicability boundary are declared.

`transitionLaw`, `observationRelation`, `constraintsOrInvariants`, and `calibrationOrParameterSourceIfReliedOn` are ClaimGraph content or exact references inside the `U.Dynamics` episteme unless another governing pattern independently identifies one as an episteme, source, relation, or structure. Naming or displaying one component does not split `U.Dynamics`, create a MethodDescription, or make a relation obtain.

`observationRelation` separates state from what can be measured, sampled, logged, estimated, or inferred. Identity observation is allowed only when the claim says the state coordinate is directly observed. Any exact measurement result, observation record, dated Work, provenance path, empirical-grounding relation, or assurance claim remains under its subject pattern.

#### A.3.3:4.5 - Evidence, prediction, conformance, drift, and calibration

Let `D` be a `U.Dynamics` about exact EntityOfConcern `E`. Let `W` denote only exact dated `U.Work` occurrences when Work is current, and let `O` denote separately identified observation, telemetry, source, or measurement records. Neither a record nor a Work occurrence is part of `D` merely because a trace cites it.

| Derived value | Meaning |
| --- | --- |
| `trace(W, O, D)` | ordered observed values produced by the declared observation relation from exact Work-side facts when present and separately identified telemetry, source, observation, or measurement records |
| `initialState(W, O, D)` | stated, measured, or estimated state at trace start, with the exact statement or result and its subject pattern recoverable |
| `predict(D, initialState, inputs, horizon)` | trajectory or distribution generated by the transition law over the declared horizon |
| `insideOperatingRegion(D, state)` | check against constraints, invariants, and applicability window |
| `residuals(D, trace)` | discrepancies between predicted and observed values under a stated alignment |
| `fits(D, trace, tolerancePolicy)` | conformance verdict under a declared tolerance, likelihood, interval, or distributional policy |
| `drift(D1, D2, domain)` | divergence between two dynamics versions over a declared operating domain |

These expressions name claim-side calculations or questions. A calculated value does not by itself establish an observation, conformance, drift, measurement, evaluation, gate, or assurance result. When such a result is claimed, the applicable evaluation or measurement declaration states the criterion and result semantics, and the actual application and result are identified separately; C.2.1 identifies any persisted result episteme, and use A.10 or B.3 only for the separately claimed reliance or assurance use.

Calibration Work and its domain result may support a later dynamics episteme whose changed ClaimGraph receives its own C.2.1 identity; an `EpistemeEditionRelation` obtains only when C.2.1's exact continuation predicate is separately established. Calibration does not mutate the earlier episteme into Work, identify the result as dynamics, supply intrinsic grounding, or make the later law authoritative for a gate.

#### A.3.3:4.6 - Prediction use in comparison or gating

When predicted coordinates from `U.Dynamics` are used for comparison, release, gate, assurance, or work-preparation use, one of these conditions must hold:

1. a fresh observation is available for the gate or comparison window; or
2. the applied transition map `Phi_dt` is declared non-expansive under the declared distance structure, and the transition commutes with the invariantization or quotient step on the domain of use.

If neither condition is satisfied, prediction does not carry the gate or comparison claim. Use observation, state currentness through `C.27.TA`, use `C.27` when authored temporal-claim adequacy is the concern, or move the gate claim to `A.20`, `A.21`, or the direct authority pattern.

Every use of `Phi_dt` states its applicability window: operating region, horizon, scale band, time step, parameter regime, and source-currentness condition.

#### A.3.3:4.7 - A.3.4, C.27.TA, C.27, and C.29 boundaries

`A.3.4` governs one actual bounded change identified by the exact changed referent, maximal continuous temporal extent or exact formal ordering boundary, boundary conditions, actual characteristic-state and obtaining direct-relation facts, and continuity or reidentification. A dynamics episteme can model a possible change, predict a probable transition, simulate a trajectory, constrain a candidate, or assert that change is expected; none becomes an actual `U.Transformation` until that subject-side occurrence basis obtains. Prediction supplies no dated work, transformation participation, gate passage, release, permission, or other authority.

`C.27.TA` names positive temporal aspects: freshness, delay, rhythm, currentness, inertia, cadence, trajectory, recovery timing, stabilization timing, and validity window. `C.27` judges adequacy or supported use of authored temporal claims that use those aspects. A `Dyn2TemporalClaimAdequacyCard` or temporal classification is not itself a law of change.

Stay in `A.3.3` when `transitionLaw` or `observationRelation` uses accepted local dynamics, Markov kernels, ODEs, simulations, queueing theory, control theory, or domain theory under one explicit semantic basis and applicability boundary.

Use `C.29` when the law depends on contested transfer, cross-domain analogy, learned or speculative mathematical lens, scale change, abstraction, quotienting, or reusable explanation across contexts. The `C.29` output states preserved structure, lost structure, operating-region or scale window, rival lens when current, lens-use boundary value, and stop condition. `A.3.3` remains the governing pattern for state space, transition law, observation, constraints, and calibration semantics.

#### A.3.3:4.8 - Method, mechanism, and governing-pattern constellation boundary

A source label such as `process`, `algorithm`, `dynamics`, `workflow`, `model`, `controller`, or `simulator` may point to linked slot positions under `E.10.ARCH`, not to one typed value. Recover the relevant slots first, then split the linked values:

* `U.Method` for the semantic way of doing;
* `U.MethodDescription` for the claim-bearing episteme that substantively describes one admitted Method, while C.29 and publication patterns keep its representation, form, carrier, and availability separate;
* `U.Dynamics` for the state-space and transition-law episteme;
* `U.Mechanism` for an admissible operation or law-governed application over a subject kind;
* `U.WorkPlan` and `U.Work` for planned and dated occurrences;
* `TransformationFlowStructure` for selected flow structure when the source is describing a flow-shaped arrangement of transformations;
* evidence, gate, authority, and assurance values when those claims are current.

A transition graph, ordering, shared label, dynamics equation, MethodDescription node, selector row, or predicted trajectory also establishes no B.1.5 `methodPartOf` occurrence or composite Method. B.1.5 must independently recover exact part Methods, obtaining part relations, whole-forming claims and constraints, whole semantics, boundary and reidentification.

The linkage among relation positions does not become a process, method, mechanism, dynamics model, plan, work occurrence, or evidence object. Do not infer dual typing from a shared source or label. One episteme can meet A.3.2 only by describing one admitted Method, and one episteme can meet A.3.3 only by carrying the state-space and transition-law claims above; neither membership establishes the other, identifies the Method, selects an A.22 Structure, or supplies actual Work or transformation. No current FPF governor admits one individual as both the A.3.1 semantic way of doing and the A.3.3 state-change episteme; reopen that question only if a later direct admission rule states both memberships without letting either classification supply the other's facts.

