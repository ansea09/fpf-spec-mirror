---
chunk_kind: "parent"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: null
section_title: null
source_path: "FPF-Spec.md"
output_path: "by_pattern/A.3.3.md"
commit_sha: "cda9087f48e0bce2c5f9d5f4389e7e025c7678f5"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
line_start: 9011
line_end: 9294
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
  - "C.27"
  - "C.27.TA"
  - "C.29"
keywords:
  - "calibration"
  - "dynamics"
  - "observation relation"
  - "prediction"
  - "simulation"
  - "state space"
  - "transition law"
---

## A.3.3 - U.Dynamics: State-Space and Transition-Law Episteme

> **Type:** Definitional pattern
> **Status:** Stable
> **Normativity:** Normative

### A.3.3:1 - Problem frame

Use this pattern when you need a reusable account of how a particular subject's state can change: which differences the state must retain, the law relating earlier and later state, and the conditions in which that law applies.

**First useful move.** Name the changing subject, the state coordinates and their meanings, and the transition law in one ordinary sentence. For example: “In this two-substance mixture, the remaining masses in kilograms change from (a,b) to (a/2,b/4) after each treatment cycle; the instrument reports a+b.” The first question is whether the observed total contains enough information to predict the next total. Section 5.6 works out the answer.

If the ordinary statement is sufficient for the current comparison, stop. Add the observation, calibration or assurance account when the receiving use needs it. Before making a prediction, conformance or gate-use claim, name the exact applicability window and any observation relation that use requires; stop that use if a required condition is unavailable.

The practical gain is a prediction based on sufficient state information, with an explicit way to compare it with observations. A model fitted to the wrong state can lose a distinction that changes the answer.

This pattern identifies the episteme that states the model's state space and transition law. Section 4.1 gives its membership rule. For a known model and a settled calculation, use the domain calculation directly. When the question instead concerns a procedure, an actual event or another receiving use, use the conditional contributions in :4.3.

### A.3.3:2 - Problem

A time series describes observations but leaves the next state to be explained. A control instruction selects an action but may leave its physical effect unspecified. Even a declared law can give an inadequate prediction when its chosen state hides a consequential difference, as the two-substance case shows.

A usable account must therefore connect the changing subject, the state distinctions, the transition law and the observations. Its applicability and support must be sufficient for the particular prediction or decision, which may demand more than the initial model comparison.

### A.3.3:3 - Forces

| Force | Tension |
| --- | --- |
| Universality and domain richness | One kernel pattern must cover ODEs, PDEs, Markov kernels, queues, discrete events, Bayesian updates, enterprise characteristic evolution, and architecture-quality change without flattening the domain-specific model. |
| Model and world | `U.Dynamics` is an episteme, while evidence comes from dated work, telemetry, observation, and source relations. |
| Continuous, discrete, stochastic, and hybrid forms | Time references, update rules, likelihood models, and disturbances differ; the state-space and transition-law declaration must keep them explicit. |
| Prediction and intervention | The same law can support exploration, while a control action may require additional validation and assurance. |
| Mathematical power and transfer risk | Mathematical form can make prediction precise, but transfer across domains, scales, or representations needs `C.29` and sometimes `A.6.0`. |
| Freshness and gate pressure | Predictions are attractive when observation is slow or expensive; gate use still needs stated currentness and applicability conditions. |

### A.3.3:4 - Solution

#### A.3.3:4.1 - Definition

`U.Dynamics` is a same-individual dependent kind of `U.Episteme`. Membership holds when one already identified episteme has the changing subject as its exact C.2.1 `EntityOfConcern` and its ClaimGraph, interpreted under the effective `U.ReferenceScheme`, substantively declares both a state space and a state-transition law for that subject. The law may include exogenous inputs, constraints, disturbances, and an observation relation.

The C.2.1 ClaimGraph, exact `EntityOfConcern`, and effective `U.ReferenceScheme` remain the episteme's identity discriminators. A.3.3 adds no context field or second dynamics identity. A `U.ClaimScope`, operating region, applicability window, qualification interval, parameter regime, or scale band enters only through the exact claim that uses it and its subject pattern; changing one can change claim content without becoming an ambient container.

`U.Dynamics` can be deterministic or stochastic, continuous, discrete, or hybrid. It can make state-change claims about physical systems, software services, organizations, epistemes, claim portfolios, resource states, architecture characteristics, or another exact EntityOfConcern. If several subjects are jointly modelled, the exact C.2.1 EntityOfConcern must itself be an independently identified collection, system, or other admitted subject.


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

`transitionLaw`, `observationRelation`, `constraintsOrInvariants`, and `calibrationOrParameterSourceIfReliedOn` are ClaimGraph content or exact references inside the `U.Dynamics` episteme unless another governing pattern independently identifies one as an episteme, source, relation, or structure.

`observationRelation` specifies how the model connects its state to the observed quantity. For a deterministic observation, give the map `y = h(x)`, where `x` is the model state and `y` the observed quantity. Identity observation (`h(x) = x`) is allowed only when the claim says the state coordinate is directly observed.

When proposing an exact deterministic one-step law on measured or aggregated coordinates, check whether two admitted states with the same current values of those coordinates, time and inputs can give different next coordinate values. Such a pair disproves that proposed law. Section 5.6 shows how to recover the missing predictive information or give a bounded answer.

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

### A.3.3:5 - Archetypal Grounding

#### A.3.3:5.1 - Reactor control

A reactor team models temperature and concentration with a nonlinear ODE and disturbances. Identify the reactor as the changing subject, specify the two state coordinates, and declare the ODE, disturbances and applicable operating region. The resulting episteme meets :4.1 when those state-space and law claims are present under its reference scheme.

For a thermocouple comparison, the observation relation selects temperature from the modeled state. Align the observed and predicted temperatures over the comparison window, then use the tolerance and validation conditions required by :4.6. Changes to a control policy change the model's input; selecting and describing that policy uses the Method contributions in :4.3.

If the question concerns an actual regeneration of the catalyst bed, recover that event's boundary, observed bed conditions and continuity or reidentification under A.3.4. A proposed trajectory remains available for prediction; the actual-change claim needs the occurrence facts.

#### A.3.3:5.2 - Reliability and operations

A service platform models backlog, arrival rate and incident recovery with a queueing or birth-death model. Compare its predicted behavior with the stipulated service objective under the model's operating assumptions. If that comparison is used for a release decision, apply :4.6.

#### A.3.3:5.3 - Evolutionary architecture

An architecture group tracks latency, coupling, operational cost, and change lead time across releases. An episteme about that architecture can be `U.Dynamics` when its `ClaimGraph` declares a state space over those characteristics and a discrete-time transition map as the transition law.

#### A.3.3:5.4 - Knowledge dynamics

A claim portfolio uses belief, evidence weight, source currentness, and contestability as state coordinates. An episteme declaring a Bayesian or likelihood update as the transition law over that claim-state space is `U.Dynamics`. Identify which incoming observation changes a belief coordinate under the update rule. Name the source content used to support or challenge the specified claim for that update.

#### A.3.3:5.5 - Natural physical evolution

A `U.Dynamics` episteme can model the Moon's motion around Earth using an orbital state space and transition law.

#### A.3.3:5.6 - When the observed total is not enough to predict

A team wants to predict how much of two removable substances will remain after treatment. For this worked model, let `a_n` and `b_n` be their nonnegative remaining masses in kilograms after `n` cycles. Assume that each cycle leaves half of the first substance and a quarter of the second, with no new material added:

`a_(n+1) = a_n/2`, `b_(n+1) = b_n/4`.

The instrument reports only their total, `y_n = a_n + b_n`. The model's state is `(a_n, b_n)`; its observation relation maps that pair to the total. The states `(1, 0)` and `(0, 1)` both give `y_0 = 1 kg`, but their next totals are `1/2 kg` and `1/4 kg`. No deterministic law using only the current total can reproduce the next total for every admitted state.

Retain the two masses when they are available. If only totals are observed, two successive exact readings recover the composition in this model: solve `a_0 + b_0 = y_0` and `a_0/2 + b_0/4 = y_1`, giving `a_0 = 4y_1 - y_0` and `b_0 = 2y_0 - 4y_1`. These masses must be nonnegative. Substitution into the next-cycle law gives `y_2 = (3/4)y_1 - (1/8)y_0`; the same recurrence applies at every later cycle. The prediction now uses one previous total as well as the current one. Equivalently, take that pair of totals as the predictive state.

If only the initial total is available, the model still gives a range: for integer `n ≥ 0`, `y_0/4^n ≤ y_n ≤ y_0/2^n`. Each extreme is attained by putting all the initial mass in one substance. Use this range when it answers the working question; otherwise obtain information about the composition. If the two substances instead have the same known retention factor `r` with `0 ≤ r ≤ 1`, the total alone obeys `y_(n+1) = r y_n`. Thus whether aggregation preserves the needed law depends on the modeled operations.

The calculation assumes exact readings and fixed retention factors. Applying it to treatment data requires accounting for measurement error and establishing the retention law over the intended operating range. [Lin and Lu, §§2.1–2.2](https://arxiv.org/html/1908.07725v5) explain the broader state/observation and model-reduction problem; the two-substance case here supplies an elementary construction.

### A.3.3:6 - Bias-Annotation

Available measurements can determine the chosen state too early. In :5.6, a convenient total conceals the composition that determines the next total. Compare states that share the proposed observation before treating it as sufficient for prediction.

A familiar equation or a well-fitting simulation can also encourage extrapolation beyond its established conditions. Keep the observation relation and applicable region visible when interpreting its result. The physical and organizational examples require their own domain laws and validation.

### A.3.3:7 - Conformance Checklist

**CC-A3.3-1 (Membership and identity).** A.3.3 judges one already identified `U.Episteme`. That same individual is `U.Dynamics` only when its exact C.2.1 `EntityOfConcern` is the changing subject and its ClaimGraph, under its effective `U.ReferenceScheme`, declares both a state space and a transition law. A.3.3 adds no second identity.

**CC-A3.3-2 (Local meanings and applicability).** Interpret characteristic names under the effective `U.ReferenceScheme`. State units, operating region, time base, approximation regime, claim scope when needed, qualification window and source-currentness condition as claim content or their separately governed values.

**CC-A3.3-3 (EntityOfConcern).** Name the changing EntityOfConcern. Joint modeling uses the independently identified joint subject required by :4.1.

**CC-A3.3-4 (State space).** The state space enumerates characteristics with units, scales, comparability rules, and any needed topology, geometry, aggregation policy, or invariantization rule.

**CC-A3.3-5 (Transition law).** The transition law states a relation, map, kernel, equation, rule, learned predictor, or simulation rule suitable for the declared time base and stochasticity.

**CC-A3.3-6 (Observation relation).** Evidence use states how exact Work-side facts when present and separately identified work records, telemetry, measurements, observation records, or source records become observed coordinates. Direct observation is declared rather than assumed.

**CC-A3.3-7 (Constraints and applicability).** Constraints, invariants, operating region, approximation regime, parameter range, horizon, and scale window are stated before prediction or gate use.

**CC-A3.3-8 (Control or planning procedure).** When a reusable planning or control way uses the dynamics, identify that Method under A.3.1. Apply A.3.2 to an episteme claimed to describe it; the dynamics membership test remains :4.1.

**CC-A3.3-9 (Observed facts and calibration).** Attach resource actuals, timestamps and observations to the Work, measurement or source they describe. Relate them to the dynamics through :4.5. Apply its C.2.1 identity and edition conditions when calibration changes the model.

**CC-A3.3-10 (Prediction use).** Predicted Coordinates used for comparison or gating state the exact model edition, domain, horizon, currentness, error or uncertainty, and every observation, validation, sensitivity, stability, or normalization-composition condition required by that consumer's policy. No universal non-expansiveness or commutation test substitutes for the direct decision rule.

**CC-A3.3-11 (Temporal use).** State temporal aspects through C.27.TA and establish the adequacy required of an authored temporal claim through C.27, as specified in :4.3.

**CC-A3.3-12 (Representation transfer).** Apply :4.7 when representation transfer changes the law's permitted use, and carry the resulting conditions into the dynamics account.

**CC-A3.3-13 (Source-label repair).** Recover the relation asserted by an ambiguous source label under :4.8 before applying a membership predicate.

**CC-A3.3-14 (Actual change).** When an actual transformation is claimed, establish A.3.4's occurrence basis specified in :4.3. A predicted or simulated trajectory describes change under the model's premises.

### A.3.3:8 - Common Anti-Patterns and How to Avoid Them

| Recognizable failure | Repair |
| --- | --- |
| Inferring a transition law from procedure text or a workflow diagram's layout | Recover the actual assertion under :4.8, then test for both a state space and a transition law under :4.1. |
| Treating telemetry as a law | Declare the proposed law, derive the observed coordinates through :4.5 and compare its consequences with the telemetry. |
| Using dashboard labels as state coordinates without their meanings | Recover the characteristics, units, scales and comparability rules, and check whether the chosen coordinates retain the needed predictive information. |
| Treating a simulation as release approval | Check its predicted result against the receiving decision's conditions in :4.6, then obtain that decision. |
| Extrapolating beyond established model conditions | State the applicable region, source-currentness condition and lowering condition; use :4.7 if the use requires transfer. |
| Relying on a learned prediction without its domain and error conditions | State its training domain, observation relation, error or uncertainty policy and applicability window before reliance. |

### A.3.3:9 - Consequences

An explicit state and transition law lets the practitioner calculate a possible trajectory and compare it with observations through a declared relation. A failed comparison can then change a particular state choice, parameter, observation account or applicability condition.

The work costs more than collecting measurements: the model needs interpretable characteristics and a supported law. A bounded prediction may be sufficient; a more consequential use may require additional observation, calibration or validation under :4.6.

### A.3.3:10 - Rationale

The needed prediction determines which state distinctions have to remain recoverable. The transition law expresses how those distinctions evolve, while the observation relation says which part of that state the available measurements reveal. Keeping these contributions explicit makes both successful prediction and a failure caused by lost information explainable, across different domain laws.

### A.3.3:11 - SoTA-Echoing

**Choose a predictive description for the question being asked.** In :5.6 the available observation is the total mass, but the next total depends on its hidden composition. Compare the descriptions under the same fixed retention law and exact-reading premises:

| Available description | What it answers | Added effort and limit |
| --- | --- | --- |
| One present total | Bounds the next total between one quarter and one half of the present total. | Cheapest when that interval settles the question; it cannot select one exact next value under unequal retention. |
| The two component masses | Determines the next state and total directly. | Requires observing or otherwise establishing the composition. |
| Two consecutive exact totals | Recovers the two masses, then predicts by the derived second-order recurrence. | Replaces a composition observation with a second timed reading; noisy readings require an error account. |

For a present total of 1 kg, the interval [0.25, 0.5] kg already settles whether the next total is at most 0.6 kg. It leaves an at-most-0.4 kg question unresolved. Acquire composition or a sufficiently informative history only when that remaining uncertainty matters. Equal retention restores a one-total transition law, so the extra state or reading becomes unnecessary.

[Lin and Lu, §§2.1–2.2](https://arxiv.org/html/1908.07725v5) supplies the methodological comparison line: selected observables can discard information that reappears as memory in a reduced description. Its exact projection identity still requires closure choices for a usable reduced model; its statistical treatment uses a stationary-process setting. The elementary calculation above is an authored construction. It selects the state–observation distinction in :4.1–:4.2 and the question-dependent choice in :5.6, with a measurable cost: additional coordinates or observations only when the cheaper description is insufficient.

**Strengthen support when the use changes.** For data-driven predictive control, [de Jong and colleagues, §§I–IV, especially III and Theorem IV.2](https://arxiv.org/html/2405.01292v1), compare iterated one-step lifted models with directly learned multi-step predictors. They choose the latter to avoid propagating one-step prediction errors across the horizon, at the cost of learning horizon-dependent prediction matrices and observables. Their constrained controller adds an interpolated initial state and terminal ingredients; recursive feasibility depends on the stated terminal-set assumption and a feasible preceding problem. These are contributions to a particular control problem.

Accordingly, :4.6 makes the intended consumer specify the prediction conditions and properties it relies on. A control decision that relies on recursive feasibility must establish the relevant model, constraints and feasibility conditions. An ordinary comparison can finish with the state, law, observation and applicability information sufficient for its question. The extra cost of a stronger guarantee is incurred by the use that needs it.

Reopen the chosen description when the observation error, retention law, horizon or question changes enough to defeat its information or error bound. Reopen a control use when its measured prediction errors or operating conditions defeat the assumptions supporting its selected guarantee.

### A.3.3:12 - Relations

C.2.1 supplies episteme identity, empirical-grounding and edition conditions. A.19 and C.16 supply characteristic and measurement construction; A.2.6 supplies a claim scope when the use relies on one.

When an independently selected bounded-model-use structure or obtaining model-use relation changes the receiving use, A.1.1 supplies that account. The other conditional contributions are specified at :4.3; :4.7 governs mathematical transfer into a dynamics use.

### A.3.3:End

