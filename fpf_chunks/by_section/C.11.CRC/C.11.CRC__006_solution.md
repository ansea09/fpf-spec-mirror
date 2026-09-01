---
chunk_kind: "child"
pattern_id: "C.11.CRC"
pattern_title: "Configuration-Relative Contribution Comparison"
section_id: "C.11.CRC:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11.CRC/C.11.CRC__006_solution.md"
commit_sha: "3c3f968398a938bc10e83da22d509b7b8f642d83"
heading_path:
  - "C.11.CRC — Configuration-Relative Contribution Comparison"
  - "C.11.CRC:4 — Solution"
line_start: 47373
line_end: 47435
dependencies:
  - "A.1.CSD"
  - "A.10"
  - "A.15"
  - "A.19"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.27"
  - "C.28"
  - "C.29"
keywords:
  - "candidate configuration S1"
  - "constraints"
  - "current configuration S0"
  - "finite change"
  - "interactions"
  - "marginal contribution"
  - "option effects"
  - "result and resource vectors"
  - "transition"
  - "uncertainty"
---

### C.11.CRC:4 - Solution

Construct the smallest finite counterfactual comparison that can change one named decision.

1. **Name the receiving decision.** State the deciding System, current `DecisionSubject`, decision deadline, current `OptionSet` or the option-set question that this comparison will inform, and which result could change the decision.
2. **Freeze the current configuration.** Name the actual or currently relied-on configuration `S0`, system boundary, affected Systems, holder or beneficiary, relevant environment, and what is held fixed only for this comparison. If the affected-System coordinate is missing and could change the comparison, use `A.1.CSD` first; bring back only consequence claims compatible with this `S0`/`Δ`/`S1`, horizon, evidence window, and receiving decision. A historical, empty, or ideal configuration is not the default baseline.
3. **Name the finite change.** State the addition, replacement, removal, intervention, or probe `Δ`, the realizable candidate configuration `S1`, admissibility conditions, implementation capability, transition Work, reversibility, and excluded variants.
4. **Fix horizon and scenarios.** State the interval, relevant states or scenarios, timing assumptions, and any decision or evidence window. Do not combine results from incompatible horizons without an explicit mapping.
5. **Declare result coordinates.** Name the result vector whose coordinates can change the decision and the protected coordinates that may not be silently scalarized. Include affected-System consequences and distributional differences when current.
6. **Declare resource coordinates.** Name the action, transition, information-acquisition, computation, attention, capital, time, material, energy, authority, and other resources that the field case actually consumes. Keep costs of evaluating and realizing the change distinct.
7. **Recover constraints and interactions.** State active and potentially activated constraints, complements, substitutes, thresholds, congestion, downstream effects, common causes, overlaps, and double-counting risks.
8. **Recover option effects.** State whether the finite change opens, closes, delays, preserves, or makes irreversible later options. Keep information value and option value as decision inputs, not already realized operating results.
9. **Qualify evidence and uncertainty.** Identify source claims, currentness, uncertainty, sensitivity/robustness results, transfer limits, rival explanations, and `A.10` reliance dispositions where an evidence-bearing claim is used.
10. **Write the comparison claim.** State what `S1` contributes relative to `S0` only under the declared coordinates, horizon, scenarios, constraints, interactions, and evidence. Use dominated, non-dominated, beneficial, harmful, or indeterminate wording only when the stated relation supports it; do not force one scalar winner.
11. **Route mathematical near-misses.** Apply the distinction in `C.11.CRC:4.2`; the finite comparison may consume a derivative, sensitivity, shadow price, variational, or inference result without becoming identical to it.
12. **Return to `C.11`.** `C.11` combines this claim with preferences, belief state, outcome model, probe worth, and other premises and emits one `ChoiceResult`. State the smallest configuration, horizon, evidence, resource, constraint, or option-set change that reopens this comparison.

#### C.11.CRC:4.1 - Lightweight comparison form

`ConfigurationRelativeContributionComparison@Context` is a form name for one ordinary comparison episteme. It is not a root U-kind, universal delta value, selector result, or decision.

```text
receivingDecisionRef:
currentConfigurationRef: S0
candidateFiniteChangeRef: Δ
candidateConfigurationRef: S1
systemBoundaryAndAffectedSystems:
horizonAndScenarios:
resultCoordinateRefs:
protectedCoordinateRefs:
resourceCoordinateRefs:
constraintsAndInteractions:
transitionAndImplementationBasis:
futureOptionEffects:
evidenceAndUncertaintyRefs:
comparisonClaim:
unsupportedOverreads:
reopenCondition:
nextGoverningPattern: C.11
```

Omit a field only when it cannot change this comparison and that omission is apparent from the bounded case. A polished record cannot compensate for a missing current configuration or decision.

#### C.11.CRC:4.2 - Mathematical and model-routing distinction

| Expression encountered | Exact question | Required boundary |
| --- | --- | --- |
| Finite difference or counterfactual configuration comparison | What changes between realizable `S0` and `S1` over the declared horizon? | Default here for indivisible, non-smooth, thresholded, path-dependent, or strongly interacting changes. Do not infer additivity. |
| Derivative or gradient | What is the local rate of change with respect to a coordinate under smoothness and small-change assumptions? | It approximates the finite contribution only when the validity region and remainder are adequate for `Δ`. |
| Sensitivity | How does a result vary with a parameter, assumption, input, model, or scenario? | It supplies robustness or assurance information; it need not describe a realizable configuration change. |
| Shadow price or dual variable | What is the local value of relaxing a formulated active constraint under the primal/dual model? | It depends on formulation, active set, regularity, units, and local region; it is not the contribution of an arbitrary asset or intervention. |
| Functional variation / calculus of variations | How does a functional change when the varied object is a function, path, trajectory, field, control, or shape in a declared admissible variation space? | Name the functional, admissible variations, constraints, boundary conditions, stationarity/extremum claim, sufficiency, and validation. An Euler–Lagrange equation is not a generic contribution claim or proof that a physical System optimizes. |
| Variational inference | Which member of an approximation family best approximates a target probability distribution under a declared divergence or bound? | The result is an approximate distribution and uncertainty account, not an extremal physical trajectory, capability acquisition, or general marginal value. |
| Evolutionary variation | How are retained variants generated and selected in an evolutionary or cultural process? | The shared word *variation* does not identify the mathematical object or Method above; route to `C.18`, `C.36`, or the field practice. |

This is why calculus of variations matters without becoming the default interpretation of marginality. When the candidate is a whole trajectory, field, function, control, or shape, pointwise finite-coordinate reasoning can miss the coupled admissible deformation. `C.29` governs the mapping from the world or domain model to that mathematical object, what structure is preserved or lost, and when the lens must stop. Specialist practice governs derivation, discretization, solver choice, optimality and sufficiency checks, and validation.

#### C.11.CRC:4.3 - Recognition and assurance split

**Recognition.** A user can recognize a conforming comparison when `S0`, finite `Δ`, `S1`, boundary, horizon, result and resource coordinates, interactions, uncertainty, and receiving decision are visible.

**Assurance.** Trust in the numbers and relations remains separate. Field evidence must support the baseline and candidate behavior; implementation capability and transition Work must be credible; causal claims use `C.28`; source reliance uses `A.10`; material assurance uses `B.3`; authority and permission use their direct patterns. This pattern creates none of those results.

