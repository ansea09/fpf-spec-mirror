---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__005_solution.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:4 — Solution"
line_start: 9075
line_end: 9213
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

### A.3.3:4 - Solution

#### A.3.3:4.1 - Definition

`U.Dynamics` is a same-individual dependent kind of `U.Episteme`. Membership holds when one already identified episteme has the changing subject as its exact C.2.1 `EntityOfConcern` and its ClaimGraph, interpreted under the effective `U.ReferenceScheme`, substantively declares both a state space and a state-transition law for that subject. The law may include exogenous inputs, constraints, disturbances, and an observation relation.

The C.2.1 ClaimGraph, exact `EntityOfConcern`, and effective `U.ReferenceScheme` remain the episteme's identity discriminators. A.3.3 adds no context field or second dynamics identity. A `U.ClaimScope`, operating region, applicability window, qualification interval, parameter regime, or scale band enters only through the exact claim that uses it and its subject pattern; changing one can change claim content without becoming an ambient container.

`U.Dynamics` can declare a deterministic transition, permitted alternatives, a probability law over continuations, or a combination of these. Its time description can be continuous, discrete or hybrid. It can make state-change claims about physical systems, software services, organizations, epistemes, claim portfolios, resource states, architecture characteristics, or another exact EntityOfConcern. If several subjects are jointly modelled, the exact C.2.1 EntityOfConcern must itself be an independently identified collection, system, or other admitted subject.


If empirical grounding is claimed, state the exact C.2.1 `EpistemeEmpiricalGroundingRelation`.

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
  TransitionChoices:
  ProbabilityLawIfSpecified:
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

These rows are an optional aid for the minimum claim content and separately governed references needed by the current use. C.2.1 identifies the candidate episteme.

#### A.3.3:4.3 - Conditional contributions to the work

Use a contribution below when its question arises while constructing or using the state-law account.

| Question now requiring an answer | Contribution |
| --- | --- |
| Which reusable way is being identified, and does the episteme describe that way? | A.3.1 identifies the `U.Method`; A.3.2 tests whether an episteme substantively describes that admitted Method. |
| Does a proposed whole Method have the claimed parts and whole behavior? | B.1.5 establishes the exact part Methods, obtaining `methodPartOf` relations, whole-forming claims and constraints, whole semantics, boundary and reidentification. |
| What work is planned, or what was actually performed? | A.15.2 identifies the `U.WorkPlan` episteme coordinating possible future Work; A.15.1 independently admits dated performed `U.Work` and establishes its actuals. |
| Is one actual bounded change established? | A.3.4 requires the exact changed referent, temporal extent under its continuity rule or formal ordering boundary, boundary conditions, actual characteristic-state and obtaining direct-relation facts, and continuity or reidentification. |
| Which independently selected organization of constituents and obtaining relations is being used? | A.22 identifies that Structure, including a selected transformation-flow organization. |
| Which operation or law-governed application is admissible over the subject kind? | A.6.1 identifies the `U.Mechanism` episteme declaring the operation family, laws and admissibility conditions. Use E.20 when introducing or revising a mechanism definition in FPF. |
| Which mathematical substrate or transferred representation supports the model? | Use the direct mathematical Method; use A.6.0 when the model needs a reusable formal-substrate declaration. Section :4.7 specifies the C.29 transfer question. |
| Which observations or source claims support the model or comparison? | A.10 supplies the evidence-provenance account; :4.5 states how observations are compared with the law. |
| Which temporal aspect, such as freshness, delay or a validity window, does the use require, and is the authored temporal claim adequate? | C.27.TA supplies the temporal-aspect description; C.27 assesses the authored temporal claim. |
| What assurance or decision does reliance on the prediction require? | B.3 supplies assurance and A.20 supplies a needed internal-constraint result. Use A.21 for a gate decision or the applicable decision pattern for another decision. Apply :4.6's prediction-use conditions. |

#### A.3.3:4.4 - State-space and transition-law fields

The following optional view groups the claim content of one C.2.1 episteme:

```text
U.Dynamics membership view {
  candidateEpisteme: U.Episteme
  entityOfConcern: EntityOfConcern
  effectiveReferenceScheme: U.ReferenceScheme
  claimGraph: {
    stateSpace: state-space declaration over FPF characteristics
    transitionLaw: state-transition claim
    timeReference: continuous | discrete | hybrid
    transitionChoices: permitted continuations and conditions selecting among them
    probabilityLawIfSpecified?: conditional probability law over continuations
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

`transitionLaw`, `observationRelation`, `constraintsOrInvariants`, and `calibrationOrParameterSourceIfReliedOn` are ClaimGraph content or exact references inside the `U.Dynamics` episteme unless another governing pattern independently identifies one as an episteme, source, relation, or structure.

`observationRelation` specifies how the model connects its state to the observed quantity. For a deterministic observation, give the map `y = h(x)`, where `x` is the model state and `y` the observed quantity. Identity observation (`h(x) = x`) is allowed only when the claim says the state coordinate is directly observed.

When proposing an exact deterministic one-step law on measured or aggregated coordinates, check whether two admitted states with the same current values of those coordinates, time and inputs can give different next coordinate values. Such a pair disproves that proposed law. Section 5.6 shows how to recover the missing predictive information or give a bounded answer.

For a proposed stochastic one-step law on aggregated coordinates, compare the next-observation distributions from the states it merges under the same time and inputs. If those distributions differ, the current aggregate omits predictive information. Retain a more informative state, condition a distribution over hidden states on the available history, or use a bound sufficient for the question. Equality for every merged group supports the aggregated one-step law under those conditions; longer use must preserve the later outputs and conditions it needs. Section :5.8 separates this question from long-run averaging.

##### A.3.3:4.4.1 - Construct the state and allowed continuations

1. **Start with the question and participants.** Name what can change, which result is needed and the conditions being considered. From the relevant subject account, identify the interacting participants and which of their differences can affect that result.
2. **Describe allowed configurations.** State how the participants may be arranged and which values are compatible. Separate constraints on configurations from interactions that drive change. Use independent coordinates when they simplify the work; retain an implicit constraint when eliminating it is difficult or would hide a needed relation.
3. **Recover the information needed for continuation.** Separate changing state from parameters held fixed by the model and externally supplied inputs. Determine the initial data required by the proposed law. A position may also need its velocity; a computation may need its instruction position and saved local values. For a field, name its argument domain and value quantities, then obtain the needed initial and boundary data from its law and the modeled arrangement.
4. **Construct the transition.** Use the subject's laws or operation rules to relate admitted states under the inputs. Work a small case. Check that the proposed continuation respects the constraints. If a constraint leaves the next state unresolved, supply the missing interaction or operation rule, or retain the alternatives it permits.
5. **Interpret the alternatives.** State who or what can select a continuation and under which conditions. Use a probability law when one is supplied or supported for that use. Counting possible continuations establishes their number; probabilities require a rule assigning them weights. The distinction changes the result in :5.9.
6. **Test the description and choose the return.** Apply the state-sufficiency comparison above to the prediction or observation needed now. Return the state and transition account, a sufficient range or conditional conclusion, or the state distinction, law, input or observation still needed. Use C.11.DUA when choosing whether further information is worth obtaining.

The construction can finish before a complete dynamics model exists: a useful result may identify the missing physical interaction or computational rule. Section :4.1 admits `U.Dynamics` only when the episteme substantively states both the state space and the transition law.

#### A.3.3:4.5 - Evidence, prediction, conformance, drift, and calibration

Let `D` be a `U.Dynamics` about exact EntityOfConcern `E`. Let `W` denote only exact dated `U.Work` occurrences when Work is current, and let `O` denote separately identified observation, telemetry, source, or measurement records.

| Derived value | Meaning |
| --- | --- |
| `trace(W, O, D)` | ordered observed values produced by the declared observation relation from exact Work-side facts when present and separately identified telemetry, source, observation, or measurement records |
| `initialState(W, O, D)` | stated, measured, or estimated state at trace start, with the exact statement or result and its subject pattern recoverable |
| `predict(D, initialState, inputs, horizon)` | trajectory or distribution generated by the transition law over the declared horizon |
| `insideOperatingRegion(D, state)` | check that `state` satisfies D's constraints and invariants; separately name the prediction or use and its relevant time or horizon, then check D's applicability window for that use |
| `residuals(prediction, trace, alignment)` | discrepancies between the selected prediction and observed trace values under the stated alignment; `prediction` is the result of the identified `predict(D, initialState, inputs, horizon)` calculation |
| `fits(D, trace, tolerancePolicy)` | conformance verdict under a declared tolerance, likelihood, interval, or distributional policy |
| `drift(D1, D2, domain)` | divergence between two dynamics versions over a declared operating domain |

These expressions name claim-side calculations or questions. When an observation, conformance, drift, measurement, evaluation, gate, or assurance result is claimed, the applicable evaluation or measurement declaration states the criterion and result semantics, and the actual application and result are identified separately; C.2.1 identifies any persisted result episteme, and use A.10 or B.3 only for the separately claimed reliance or assurance use.

Calibration Work and its domain result may support a later dynamics episteme whose changed ClaimGraph receives its own C.2.1 identity; an `EpistemeEditionRelation` obtains only when C.2.1's exact continuation predicate is separately established.

#### A.3.3:4.6 - Prediction use in comparison or gating

A prediction used for comparison, release, gate, assurance, or work preparation states the exact dynamics edition, predicted Coordinates, operating region, horizon, and relevant error or uncertainty. State any time step, parameter regime or source-currentness condition on which the prediction or receiving use depends. The direct consumer's policy then states which observation, validation, sensitivity, robustness, stability, or normalization-composition conditions that use requires.

A fresh observation may replace or check the prediction when the policy calls for it. A non-expansive bound, another sensitivity bound, or commutation with a normalization step is required only when the named use relies on that property. If the required conditions are absent or fail, the prediction cannot carry that use. State a needed currentness claim through `C.27.TA`. Use `C.27` when a separate authored temporal-claim adequacy question remains. Obtain a needed internal-constraint result through A.20; use A.21 for a gate decision or the applicable decision pattern for another decision.

#### A.3.3:4.7 - Apply or transfer a dynamics model

Stay in A.3.3 when the transition law or observation relation uses accepted local dynamics under one explicit semantic basis and applicability boundary.

Use C.29 when the law's use depends on a contested transfer, cross-domain analogy, learned or speculative mathematical lens, scale change, abstraction, quotienting or reusable explanation across contexts. Establish the preserved and lost structure, operating region or scale window, applicable rival, lens-use boundary and stop condition. Then state the resulting dynamics law and its observation, constraint and calibration conditions here. The direct prediction consumer still determines reliance under :4.6.

#### A.3.3:4.8 - Recover an ambiguous source claim

When a source label such as “process” or “model” leaves the asserted relation unclear, recover one concrete claim before assigning a kind. Establish U.Dynamics membership on the episteme under :4.1 and a Method claim on the semantic way of doing under A.3.1. When an episteme is also claimed to describe that Method, apply A.3.2's membership rule independently. Section 4.3 supplies the other conditional contributions; use E.10.ARCH if the represented relation remains unresolved.

