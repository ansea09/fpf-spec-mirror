---
chunk_kind: "child"
pattern_id: "C.28.MR"
pattern_title: "Derive an Intervention Consequence by Mechanism Replacement"
section_id: "C.28.MR:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28.MR/C.28.MR__005_solution.md"
commit_sha: "98777b284b6a41fa3481a1230a16182d0f323c2a"
heading_path:
  - "C.28.MR — Derive an Intervention Consequence by Mechanism Replacement"
  - "C.28.MR:4 — Solution"
line_start: 62274
line_end: 62335
dependencies:
  - "A.3.3.TR"
  - "B.5.MPC"
  - "B.5.RR"
  - "C.28"
  - "C.29.1"
keywords:
---

### C.28.MR:4 - Solution

**Choose the intervention and question → recover the mechanisms and input law → replace the selected mechanisms → solve the affected relations → obtain the requested consequence → return its interpretation and useful limit.**

These moves form a derivation. A few equations can carry the complete small result.

#### C.28.MR:4.1 - Specify what is changed and what is asked

Name the modeled variable or mechanism, the proposed replacement and the result needed for use. Include the time or horizon when it changes the question. “Set the alarm to zero now” and “keep its output at zero for the next hour” describe different interventions in a model with later feedback.

For a constant intervention, use `do(X=x)` to mean replacing the equation for X by the constant x. For a changed rule, state that rule and the information it may use: for example, a controller's command as a function of the readings available before the command. C.28:4.10 distinguishes the relevant action-policy families when that choice matters.

Specify a comparison only when one is wanted. A value under one intervention, a difference between two interventions and a difference from natural behavior have different required inputs. A question about the same historical case under another action also needs the factual observations and the resulting information about that case's underlying inputs. Recover that counterfactual basis through C.28 before treating a population intervention answer as an answer about the observed case.

#### C.28.MR:4.2 - Recover the model that gives the replacement meaning

Write or recover each relevant mechanism in a form such as `X_i = f_i(parents, U)`. The function tells how the modeled quantity is determined by other modeled quantities and by U, the inputs left outside these mechanisms. Recover their domains and the joint distribution of U, or their given values for a deterministic calculation.

Keep the subject interpretation with the equations. An equation's left-hand side is selected by the causal account. Algebraically rearranging `I=V/R` to `V=IR` preserves the equality but does not decide which physical component an intervention replaces. In :5.2 the supply controls V and the resistor relates V to I.

Preserve common inputs and their dependence. If two disturbances arise from one shared event, retain that event or their joint law when calculating both effects. A simulation must generate one compatible joint input for a case; independent resampling of its components would change the model.

Recover only the mechanisms needed to determine the queried consequence and their relevant conditions. A missing actuator relation may prevent a physical consequence while still allowing a useful comparison inside an explicitly assumed model. State that assumption where the result uses it.

#### C.28.MR:4.3 - Construct the modified model

Replace each targeted mechanism by its stated constant or function. Retain the other mechanism functions and the supplied input law. Then let their output values follow from the new inputs to those functions.

For a randomized replacement, give its randomization law and its dependence on existing inputs. An independent randomizer is one possible specification. If the proposed change also alters the environment or population, include that change in the compared model instead of silently treating it as part of a constant intervention.

Keep a replacement's scope visible in time. In a discrete-time model, identify the affected update steps. In an event-driven model, identify the triggering condition and the state change it initiates. A.3.3.TR helps construct the relevant continuation rule from interactions, events and subject laws when that rule is missing.

At the physical interpretation, ask whether the proposed action also changes another modeled mechanism. Changing a supply command and attaching a device that forces its output can have different consequences for current limits and other connections. Add the relevant effects before using the modified model to answer that physical question.

#### C.28.MR:4.4 - Solve what the intervention query requires

For an acyclic model, evaluate the retained and replaced functions in dependency order. For a time-stepped model, propagate from its initial conditions through the selected horizon. For simultaneous equations or continuous dynamics, use the solution method and conditions appropriate to those relations.

Check the transformed relations themselves when a replacement can change existence or select among several solutions. A solver's first returned branch may leave other admitted answers. If all admitted solutions agree on the queried quantity, that agreement can answer the question. If their answers differ, retain the possible answers, derive a useful bound, or expose the condition needed to choose among them. If the model has no relevant solution for inputs the query includes, return that obstruction and repair the model or question.

For probabilistic results, the selected solutions must define the requested random quantity under the input law. Existence of one numerical trace supplies less than a uniquely determined distribution. A general proof is unnecessary when a direct finite calculation settles the present query.

For a dynamically triggered jump, recover the event-order or flow/jump choice if it changes the result. A model's steady-state solution alone does not determine what happens during a transient. The hybrid-system approach discussed in :11 supplies one current treatment with explicit conditions; the subject model still determines which treatment is appropriate.

#### C.28.MR:4.5 - Calculate the consequence under the retained conditions

Let `Y_g(u)` be the queried output obtained with replacement g and input u. For a finite input population with probabilities `p(u)`, its mean is

`E[Y_g] = sum_u p(u) Y_g(u).`

Use the corresponding integral for a continuous input law when it exists. For a contrast between g and h in the same population, evaluate both under that population's law. A paired simulation can reuse each joint input u for both computations. Preserve the dependence of inputs within each computation.

A symbolic expression, an inequality or a bound can be sufficient. Numerical precision should serve the receiving choice or explanation. If an estimate is required, distinguish its computational or sampling error from uncertainty about the causal model and its parameters.

#### C.28.MR:4.6 - Return the result and reopen only what changes it

Return the consequence together with the replacement, model assumptions and comparison or horizon needed to interpret it. The equations and answer already produced may suffice. Use C.28's reusable support form only when another use needs a referenced conclusion.

Keep the mathematical result conditional on the supplied causal account. When the receiving question concerns an actual device or organization, connect the proposed action to the modeled replacement and ask which unmodeled interaction could change this result. Obtain further evidence only when that unresolved question can change the use. B.5.MPC connects the physical account, mathematical construction, computation and observation when this passage needs work.

When a parameter, intervention scope or mechanism changes, revisit the dependent derivation. Preserve unaffected relations and calculations. A changed event time can require another continuation; a changed source of disturbance can require another joint input law. Stop when the requested result or a useful supported limit is available.

