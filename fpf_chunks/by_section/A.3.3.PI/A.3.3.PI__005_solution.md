---
chunk_kind: "child"
pattern_id: "A.3.3.PI"
pattern_title: "Retain the Information Needed for Prediction"
section_id: "A.3.3.PI:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.PI/A.3.3.PI__005_solution.md"
commit_sha: "685a0d04e8c8b8c3ac0a571d72be15daf004c72f"
heading_path:
  - "A.3.3.PI — Retain the Information Needed for Prediction"
  - "A.3.3.PI:4 — Solution"
line_start: 10117
line_end: 10186
dependencies:
  - "A.3.3"
  - "A.3.3.CC"
  - "A.3.3.TR"
  - "B.5.FM"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.29.1"
keywords:
---

### A.3.3.PI:4 - Solution

Begin with the future distinction needed in the work. Compare the situations merged by the proposed description, construct a description or uncertainty account that retains the consequential differences, and use it at the required horizon.

#### A.3.3.PI:4.1 - Specify the future question and the available account

Name the quantity, event or choice being predicted, the horizon and the inputs over that horizon. Specify the accuracy or decision boundary when it changes what information is needed. Predicting a total after one treatment cycle, determining whether it will be below a limit, and estimating a long-run average can require different information.

Recover the rule of change, observation meanings, sampling times and available initial information. Separate uncertainty about the state from uncertainty about the rule or future input. A longer observation history cannot replace an unspecified intervention.

State what the proposed description retains: present readings, model coordinates, past inputs and outputs, derived features or weights over possible states. Where future actions are chosen by a controller, retain the action assumptions needed by the comparison.

#### A.3.3.PI:4.2 - Compare situations merged by the description

Construct two admitted states or histories with the same retained description. Keep the rule, input conditions and future question fixed. Derive their relevant continuations. A difference in the requested result identifies information lost by that description.

For a deterministic discrete model, let x be its state, u its input, F(x,u) the next state and z = r(x) the retained description. An update z' = G(z,u) is well-defined when r(F(x,u)) has the same value for every admitted x having the same z, for each input covered by the claim. This condition says how to construct G: choose any compatible x, apply F and retain r of the result. All compatible choices must give the same answer. C.29.1 supplies the general comparison of operations under a representation change.

A prediction of one selected output at a fixed horizon may need less information than an update of the entire retained state. Compare the output that the question asks for. If the result will be used repeatedly, also determine how to update the information from which the next prediction is made.

For a probabilistic model, compare the distributions of the relevant future result under the merged states or histories. The current readout can conceal different next-event probabilities even when the full model is Markov, as :5.2 shows.

One divergent pair refutes sufficiency for a claim covering both cases. Matching a few pairs supports only those comparisons. A general sufficiency claim needs an argument or subject Method covering its stated class; a local counterexample or conditional forecast may already be enough for the present work.

#### A.3.3.PI:4.3 - Choose the least costly useful repair

Use the missing distinction to choose a repair.

- **Retain additional state values.** Keep component amounts, velocity, operating mode, pending input or another variable whose difference changes the result. Include a way to obtain or estimate it in the intended use.
- **Retain relevant history.** Use observations and intervening actions to infer the missing state or construct a direct recurrence. Derive the needed history length from the rule and observation account where possible.
- **Retain an uncertainty account.** Carry the admitted state set or a distribution over possible states and propagate it through the rule. Use probability weights when a probability model is supplied.
- **Answer a weaker question that still serves the work.** A range, threshold decision or shorter-horizon result can be sufficient even when a unique future value remains unresolved.

Compare the available repairs by what they change in the decision and by their cost. C.11.DUA helps decide whether another measurement or calculation is worth obtaining. Use an already adequate bound directly.

A finite history can close some models, including the two-substance example. Other projections need a longer history, an approximate memory account or retained uncertainty. Choose the repair from the dynamics and the intended error, rather than assuming a fixed number of observations always reconstructs the state.

#### A.3.3.PI:4.4 - Construct the prediction and its update

For an algebraic reconstruction, solve the observation and change equations for the hidden values. Check the admitted domain and substitute the result back. Derive a recurrence if the next prediction will use a rolling history. Include how to discard old information and incorporate the next reading.

For a set of possible states, apply the change rule to that set under the admitted inputs, then use the observation relation to obtain possible outputs. A simpler enclosing interval can be enough for a threshold question. Keep the direction of the bound that makes the decision valid.

For a finite hidden-state probability model, let Pij be the probability of transition from state i to state j, and let pi be the current probability of state i given the observations and actions already used. First predict the next-state weights:

    predicted_pj = sum_i(pi * Pij)

When a new observation y arrives, multiply each predicted weight by the observation likelihood Lj(y), then divide by the sum of those products. For a discrete readout, Lj(y) is the probability of y in state j. For a continuous readout with a modeled density, use that density at y. Under the Markov and observation assumptions, the normalized weights summarize the history for the next prediction. Use the transition probabilities for the action actually taken when actions affect the model.

Supply the initial weights and observation likelihoods from the selected model. If the normalizing sum is zero, this update cannot supply posterior weights. Check the observation account, initial possibilities and numerical calculation before proceeding. The weights describe the current uncertainty about the modeled state.

For example, two equally weighted hidden states have Gaussian observation densities with means 0 and 1 and variance 1. An observation y=0 gives likelihoods proportional to 1 and exp(-1/2), so the first state's updated probability is 1/(1+exp(-1/2)), about 0.622. Using the probability of a single value would give zero for both continuous distributions and prevent this valid update.
A learned predictor offers another construction. Train or select it for the output, horizon, inputs and error that matter. A direct prediction several steps ahead and repeated application of an approximate one-step model can behave differently. Evaluate the intended use, including how the predictor receives the information available at each step.

#### A.3.3.PI:4.5 - Test the horizon, error and changing conditions

Work a case through to the requested future result. Include a pair merged by the simpler description when one motivated the repair. Identify which retained information now changes the calculation.

When readings are imperfect, propagate their stated uncertainty far enough to determine whether it changes the result. A reconstruction can amplify observation error even when the underlying equations have a unique solution. Parameter and input uncertainty require their own treatment; changing a sampling interval can change the update rule.

Check repeated use at its claimed horizon. A universally valid closed update can be iterated while its domain and input assumptions hold. A good fit over one observed step does not provide that result for an approximate predictor. Check the errors or bounds relevant to its use and shorten the horizon or change the account when needed.

Keep forecast performance and aggregate statistics tied to their questions. A model can reproduce a long-run average yet lose the history that changes the next-event probability. Conversely, a useful short-horizon predictor may not reproduce long-run behavior.

#### A.3.3.PI:4.6 - Return the prediction with the information needed to reuse it

Return the prediction, bound or unresolved distinction in the work where it is needed. Keep its observation meanings, inputs, horizon and consequential assumptions available in the calculation or explanation.

If additional information is worthwhile, identify the measurement, state distinction or model contribution that would change the answer. A result can be useful while the actual hidden state remains unknown. Reopen the affected comparison when the input policy, law, observation scheme or question changes, using B.5.MPC.R where several accounts must change together.

