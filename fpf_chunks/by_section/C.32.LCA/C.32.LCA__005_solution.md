---
chunk_kind: "child"
pattern_id: "C.32.LCA"
pattern_title: "Construct and Compare a Control Architecture"
section_id: "C.32.LCA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.LCA/C.32.LCA__005_solution.md"
commit_sha: "996ae39ce00b4a9c9b59b48a4f1446b2175dcffb"
heading_path:
  - "C.32.LCA — Construct and Compare a Control Architecture"
  - "C.32.LCA:4 — Solution"
line_start: 76719
line_end: 76915
dependencies:
  - "A.3.3.PI"
  - "B.2.5"
  - "C.30.LCA"
  - "C.32"
  - "C.32.MWA.PP"
keywords:
---

### C.32.LCA:4 - Solution

Construct the arrangement from the result and its causal dependencies, then compare the complete alternatives. The following sections explain connected operations, not a mandatory sequence of meetings or a prescribed stack of controllers. Begin at the first missing contribution; retain an adequate model, decision or component result.

The architectural result changes the organization through which control occurs. **C.43** supplies the broader connection between the current situation, possible continuation, choice, realized influence and revision; use it directly when those answers can be joined within an adequate existing arrangement. The present Method constructs an arrangement when that joining requires different information, timing, allocation, means or interaction. Its result then returns to the ongoing control question.

#### C.32.LCA:4.1 - Recover the controlled situation and the consequence that matters

State what is meant to change, for whom, by when, and within which protected conditions. “Make the system faster” leaves the decision unresolved. “Reach the receiving position within two updates without exceeding the actuator limit” identifies a result and a constraint. “Have the approved panel installed by 16:00 without spending an unauthorized budget” identifies a different result and different conditions.

Identify the acting participants, the subject affected, the available interventions, and the observations that can inform their selection. Recover what an existing arrangement does from an actual consequential episode or an adequate model. For a proposed arrangement, explain the intended dependence without describing it as already operating.

A feedback claim needs an observation, an influence returned to the subject, and a rule and case facts coupling that influence to the observation. **B.2.5** supplies this recovery. Use the result here to find which dependence must be constructed or changed. A dashboard that nobody uses to change action supplies information but not that control dependence.

Keep the selected structure and its representation distinct. **C.30.LCA** helps recover the observation, command, reference, feedback and timing relations represented in a view. Use those relations as inputs, then examine their consequences below. An organizational chart may omit an external supplier who controls a needed release; including that relationship does not make the supplier part of the enterprise.

#### C.32.LCA:4.2 - Separate the goal, its realization and the right to revise it

Distinguish the intended outcome, the constraints that remain binding, and the choices available within them. A destination, an allowed operating region, a customer commitment and a preferred cost are different inputs to a decision. Some are negotiable by the present participant; others must be retained or returned to someone with the relevant authority.

Three changes often require different treatment:

- **Change the immediate action while preserving the goal.** Correct a disturbance, choose another route, reschedule an available resource or use an already qualified fallback.
- **Change an operational goal within the current mandate.** Select the next job, change a waypoint or choose among already authorized service priorities. Recompute the consequences for the work that depends on the earlier choice.
- **Change the mandate, promised result or architecture.** Renegotiate the deadline, remove a required output, obtain a new allocation right or change the available means. Include the time and conditions needed to make that change effective.

These are choices, not necessarily three organizational levels or three people. One actor can perform several of them; different actors can participate in one choice.

Construct the return from infeasibility to goal revision. Identify the observation or forecast that makes the present goal doubtful, the alternative outcomes still available, and who can select among them. Include the receiving work affected by that revision. A planner's failure to find a plan is evidence about that search under its conditions; it is not, by itself, proof that no feasible plan exists. A physical bound or an exhaustive argument can establish a stronger impossibility result.

While the revised decision is unavailable, specify the continuation that remains permitted. Continuing, holding a command, reducing demand, switching to another qualified method or stopping can each be right under different subject conditions. Stopping is not automatically safe: an aircraft, a chemical process and an unfinished organizational obligation have different consequences.

#### C.32.LCA:4.3 - Construct the information that makes the decision possible

Begin with the future distinction the decision needs. To decide whether work can finish today, a count of unfinished jobs may be insufficient if their remaining effort differs. To constrain a moving system, the last reported position may be insufficient if motion since that observation is unknown.

Specify the state, transition account and future input assumptions used by the prediction. Retain pending actions, occupied resources or accepted commitments when their differences change the continuation. Separate the subject's state from the information available about it.

Use **A.3.3.PI** when the retained information needs construction or repair. Compare two admissible situations that the proposed description merges, under the same future inputs and change rule. If their decision-relevant continuations differ, preserve the missing distinction, use sufficient history, or propagate a set or distribution of possibilities. A bound can settle the decision without identifying the exact state.

Date an observation by when it describes the subject, not only when its message arrived. Bring it to the decision time using the known intervening actions and dynamics, or retain the uncertainty those missing facts create. If a model requires information that cannot arrive in time, compare a different observation arrangement, a more conservative action, another model or a different decision allocation.

Construct the forecast for the actual use. A one-step predictor repeatedly applied, a direct longer-horizon predictor and an upper bound can support different conclusions. The model used for planning may differ from the model needed to qualify rapid correction, but the correspondence between their inputs, outputs and retained distinctions must be explained.

Internal simulation and actual intervention supply different returns. A simulated failure can change the proposed action before execution. An observed result after execution updates the state estimate and may challenge the model. Do not count repeated replanning as progress in the controlled subject.

#### C.32.LCA:4.4 - Derive a division of decisions from the whole dependence

Start with a feasible incumbent or a whole-problem account, not a fixed number of layers. Ask which decisions need which observations, available actions, resources and time. Group decisions when their strong interaction makes separate choice costly or unreliable. Separate them when different information or response demands make one undivided computation or authorization path impractical.

For every proposed separation, recover the dependence it removes from local consideration. Suppose two devices share a power supply limited to 10 kW. Each local plan can meet its device's 8 kW demand while their simultaneous demands total 16 kW. Giving both plans a copy of the resource limit does not preserve the joint constraint. Where the work permits different allocations or times, possible constructions include a shared allocation decision, fixed compatible reservations, a request-and-grant interaction, or staggered work. They have different waiting, utilization and change costs. If both devices must draw 8 kW simultaneously, no allocation fits the 10 kW supply; change the available supply, the demand or the simultaneity requirement.

The same question applies to planning and tracking. A planner that ignores actuator effort or response delay can select references that its tracker cannot realize. The joining contribution must restrict the references, supply a feasible trajectory, change the tracking arrangement, or revise the demand. Merely adding a feedback arrow leaves that work undone.

Recover functional contributions before assigning their bearers. Estimating state, choosing among goals, constructing a trajectory or work plan, correcting a deviation and handling an exception can each contribute without requiring a separate module, department or person. State the effect each must obtain, the inputs and initial conditions it needs, and the conditions it must preserve. Then associate it with a possible System or participant and the means through which that effect could be obtained. One bearer can carry several contributions; several bearers can cooperate in one contribution. Keep existence, capability, access and proposed allocation as separate claims.

Construct the cooperation in both directions. Work back from the required intervention to the decision, information and means that make it possible. Follow each missing intermediate result to a possible producer. Then follow a consequential demand forward from the available observations and initial conditions: what changes, what becomes usable next, and how those changes obtain the receiving effect. Explain where contributions must coincide, wait or retain a result between updates. A state estimate that expires before authorization, or a command whose execution has no available bearer, defeats that candidate even if every named function is sensible.

**C.32.MWA.PP:4.3–4.7** supplies the general construction across Method, Work, performer, means and allocation structures, including their joint demands. Use that account where the proposed division leaves performance or support unresolved. Here the additional connection is control-specific: explain how the joined contributions turn an observation into a permitted influence on the subject, and how the resulting observation can change the next decision. Change the division or its possible realization when that connection fails; preserve already adequate contributions.

For each candidate, explain how a local result becomes usable by the next participant and how a consequential limitation returns. The result is a candidate arrangement with an operating mechanism, not a collection of independently desirable boxes.

#### C.32.LCA:4.5 - Compare serious architectural alternatives

Retain alternatives that change the mechanism, not just the labels. The following are recurring choices, not an exhaustive classification.

A command or reference governor adjusts the requested input to an already qualified closed loop using its current condition and applicable constraints. It is an alternative to redesigning that loop.

| Alternative | When it can answer the question | Cost or limit to examine |
| --- | --- | --- |
| One controller or one timely decision point | The needed information and action rights are available together, and the computation or decision fits the useful window. | Information collection, scarce attention, computation and response delay can become limiting. |
| An already qualified loop with a command or reference governor | The loop's response is adequate, but requested commands can violate its qualified conditions. | The governor can delay or alter the requested outcome; it needs an applicable model and admissible initial situation. |
| Layered planning and correction | Different decisions need different horizons, representations or response times, and a useful interface can preserve their dependence. | Model mismatch, stale information, repeated computation, interface constraints and delay must be included. |
| Local decisions with coordination of shared conditions | Participants can act independently within allocations or agreements, while specified interactions need reconciliation. | Negotiation, conflicting commands, duplicated reservations and unavailable authority can defeat apparent autonomy. |
| Change the work or the physical arrangement | Removing a dependency, changing a capability or changing the demanded result costs less than coordinating the existing arrangement. | Transition cost, lost flexibility, changed commitments and consequences for other users remain part of the comparison. |

Use **C.32** to develop the candidate palette when several structures change together. For an identified conflict across scopes, **C.32.MLAO** helps generate alternatives that reduce it while exposing the burden moved elsewhere. Bring those candidates back to the information, timing and joint-condition construction here.

A policy in a lower control layer need not be less accurate than a decision in an upper control layer. Rapid tracking accuracy, predictive accuracy, semantic understanding, search quality and adaptability are different characteristics. Compare the required characteristics under the actual resource conditions. A rule such as “strategy is slow” is a possible arrangement, not a substitute for that comparison.

#### C.32.LCA:4.6 - Construct the exchange that makes the parts work together

For each consequential connection, explain what the sender supplies, how the receiver interprets it, which action it can change, and which limitation or result returns. Specify the semantics before choosing a message format or transport.

A target value, a trajectory segment and an instruction to achieve an outcome impose different work on the receiver. A target may be held until replaced; a segment can specify its evolution; an outcome request can leave the means open. Determine which interpretation the receiver can realize and which uncertainty remains with the sender. In a technical realization, hold, reset, interpolation and delay rules can change the closed-loop dynamics.

Keep the following meanings distinct when the receiving action depends on them:

- an observation or estimate of what is the case;
- a prediction of what could or is expected to happen under stated inputs;
- a decision selecting a continuation;
- a command or request addressed to a participant;
- an accepted commitment to supply a result under conditions;
- a report of the action or result that actually occurred.

A decision does not necessarily authorize its recipient, and a request does not establish acceptance. An organization may require an explicit commitment; a technical protocol may instead have a specified execution rule. Construct the connection that actually governs the case.

Early communication is useful when a receiver can do worthwhile preparation before the final result exists. Name that preparatory action, the information it needs and its reversibility. Reserving a test slot can reduce later waiting while displacing other work. Preparing material can save time while creating waste if the intended design changes. Compare those consequences with waiting for confirmation; do not treat earlier messages as a free acceleration.

Include the response to change. If a plan, estimate or commitment is replaced, identify which pending action must be cancelled, revised or allowed to finish. Distinguish a message received from a message interpreted and used. Where conflicting editions would change execution, establish which instruction applies and how the recipient learns of its replacement.

Connect the proposed exchange to effective action. Identify who can request the result, who can commit the affected means, who can perform the work, and who can accept or return its result. For the needed contribution, state the supplied result, usable inputs, scope, time window, acceptance conditions and response to refusal or failure. A participant's right to choose an action and another participant's commitment to carry it out are distinct conditions; either can be missing.

Use **C.32.MWA.PP:4.7–4.9** to construct and compare the joint workload, commitments and transition. Reuse existing effective arrangements whose scope and conditions fit. When a new permission, reservation or agreement is needed, identify its owner and the obtainable act that could establish it, including the time and participation required. Keep the candidate conditional until that act and its conditions are established. A design specification explains the intended relation; the actual authorization, acceptance or provision supplies a different fact. Return those effective conditions, or their precise unresolved remainder, to the timing analysis and continuation choice.

#### C.32.LCA:4.7 - Derive useful timing from the action window

Start from the last time at which an action can still obtain the required consequence. Work backward through the necessary detection, communication, decision and execution. Include waiting for an available processor, person, authorization or resource, not only active processing time.

For a serial path with applicable upper duration bounds, a sufficient timing condition is

\[
t_{\mathrm{change}}+
L_{\mathrm{detect}}+
L_{\mathrm{deliver}}+
L_{\mathrm{decide}}+
L_{\mathrm{execute}}
\leq t_{\mathrm{needed}}.
\]

Each bound must cover its whole contribution under the compared conditions. Periodic observation contributes the worst wait until the next observation as well as the observation work. A computation bound must include the resource arrangement under which it can be achieved. A decision bound must include the availability of a participant with the required authority.

This sum applies to the stated serial path. For parallel or returning work, construct the timing from its dependencies and resource occupations. Identify when each required input and permission can be available, which resource each action occupies, and when it releases that resource. Reconcile different names for the same person, device or capacity before assigning intervals. A machine may continue a cycle after its operator is free; an allocation must reflect that actual occupation rather than charging both for the whole elapsed cycle.

Construct a candidate schedule by placing each action after its required inputs and authorizations, in intervals where all the resources it needs are jointly available. Preserve any required uninterrupted duration, overlap, synchronization and recurring demand. At a join requiring all outputs, the receiving action can start only after the latest required output is available; its own duration still contributes to final completion. Use **C.32.MWA.PP:4.7** for the joint workload and commitment construction. A failed placement rejects that schedule; it does not prove that a different order or allocation is impossible. A necessary bound can establish a stronger rejection: required occupation exceeding the available qualified capacity in the same window cannot be repaired by rescheduling within that window.

For example, two otherwise parallel branches each require ten minutes from the same editor before their outputs can be used together. With one continuously available editor and no other required work, serializing the two edits gives a twenty-minute completion. A deadline fifteen minutes after both edits become available is impossible under those conditions, although either branch alone fits. A second qualified and authorized editor, a changed operation or a later deadline changes a different premise of the construction.

Retain a timing summary only when the receiving answer follows from what it keeps. Total free time can conceal incompatible windows; an average rate can conceal a late individual response. Derive the response time or useful bound from the retained dependencies, availability and occupation conditions. If two allowed arrangements share the proposed summary but give different answers, retain the distinguishing condition, derive a bound that covers both, or restrict the claim. Failure to find such a pair does not establish sufficiency. This specializes the information question in :4.3 to the time and capacity needed by the control decision. An average duration does not establish a worst-case deadline.

Choose an observation or decision rhythm from how rapidly a consequential difference can develop and how long a useful response takes. Periodic checking, event-triggered messages and prediction of an approaching limit are alternatives. An event trigger needs an obtainable detector and a response route; otherwise “notify on exception” supplies no timing result.

Separate update period, end-to-end latency and prediction horizon. A planner can update slowly while predicting far ahead; a fast controller can use a delayed estimate. Changing one quantity may change model error, computation, communication load or the available response. Recompute the affected dependence rather than assuming that more frequent updates are better.

Before the next update, specify what the current action may do and why that continuation remains acceptable. If a premise can fail sooner than a response can arrive, obtain a local protective action, shorten the exposure, change the observation or reduce the promised operating region. A monitoring arrangement cannot protect a condition it notices only after the last useful action.

#### C.32.LCA:4.8 - Establish joint conditions and a usable continuation

For each relied-on component or participant result, state its inputs, operating conditions, output and limits. Then check the connection in both directions: does the supplier's result satisfy what the receiver needs, and can the rest of the arrangement keep supplying the conditions on which that result depends?

Begin with a jointly possible situation. Two controllers can each require the other to have already restored the shared condition. Two teams can each promise to start when the other releases the only specialist. Such mutual expectations supply neither an initial action nor a continuation. Construct an initial allocation, a compatible joint condition or another arrangement.

Next follow a consequential action or change through the whole. Establish what remains true, what must be updated and what is available next. A successful isolated execution does not establish repeated continuation.

For a modeled controller interconnection, derive or obtain the joint dynamics rather than combining separate stability labels. Include reference changes, state estimation, hold rules, actuator limits and computational delay. A technical result can establish an admissible region, an error bound, recursive feasibility, stability or goal attainment; retain the property actually established. These results are not interchangeable.

For example, an invariant error bound can justify a margin in a planner constraint while leaving the question of reaching its goal unresolved. A continuous inequality proved only in a region applies until the first exit unless remaining in that region is established separately. Under mode switching, one invariant set respected by every allowed transition is a useful sufficient condition; different invariant sets for individual modes do not establish safe transitions between them.

Organizational continuation needs a different construction. An accepted commitment must have a capable participant, available means, compatible other commitments and the right to perform the promised action. Establish how an unavailable input, refusal, changed priority or missed window is handled. A promise can be part of the plan's basis without becoming a mathematical guarantee of performance. If the plan needs a deterministic deadline, justify the duration bounds and availability it relies on; otherwise retain the appropriate scenario, uncertainty or conditional promise.

Choose the fallback for the protected result. Keeping a previous command can work only while its qualifying conditions remain true. Escalation can work only if the recipient can decide in time. A replacement performer can work only with the required competence, access and capacity. Compare these as actual continuations, not names in an exception list.

If the joint conditions cannot be established, return the exact unresolved or conflicting dependence. It may justify a different interface, smaller demand, different allocation, additional observation or a revised goal. Keep independently usable component results.

#### C.32.LCA:4.9 - Qualify learned contributions by their actual function

Learning is one way to obtain a contribution to the arrangement. Identify which contribution it supplies. A learned state estimate, forecast, action policy, representation or optimization surrogate has different inputs, outputs and failure consequences.

For a predictor, qualify the output, horizon, available observations, future-action assumptions and error relevant to the receiving decision. For a policy, qualify the actions it can select, the states and instructions it can receive, and the constraints of the actual subject. Agreement with recorded demonstrations and a useful closed-loop result are different tests.

Keep training, inference and online adaptation separate. A policy trained slowly can execute rapidly. An online update can change the policy while its input and output formats remain unchanged. Determine whether the relied-on error, timing or constraint result continues to apply to the updated component.

Compare the learned contribution with an adequate programmed or conventional controller at the same receiving use. Include data acquisition, training or calibration, inference resources, monitoring and recovery in the whole cost. Prefer the learned option when its supported capability changes the result enough to justify those burdens, not because the architecture contains a neural network.

If a separate filter or supervisor modifies a learned command, qualify the resulting combination. The modified command can preserve one constraint while changing a tracking or progress result. A human fallback also needs detection, sufficient time, usable information and actual authority.

The output of this operation is a qualified component use or a named missing result. It is not a general method for training every controller. When the application needs a bound that the learned supplier has not established, compare a narrower operating region, an applicable protective construction, a different supplier or a weaker warranted claim. Do not silently replace the missing bound with average benchmark performance.

#### C.32.LCA:4.10 - Compare the whole arrangements and the work of changing them

Compare candidates under the same required outcome, disturbances, resources, observation conditions and relevant horizons. A faster local algorithm evaluated on an easier demand is not a faster realization of the original problem. A delegated decision evaluated without its coordination and training cost is not the same organizational proposal.

Separate an unavailable candidate from a costly feasible one, and both from a candidate whose consequential premise remains unknown. Compare the coordinates that can change the decision: useful result, delay, constraint exposure, effort, computation, scarce capacity, participant burden, flexibility and recovery. A mathematical optimum remains relative to its model and objective; a project choice also has to respect its obligations.

Include the transition. A new controller needs initialization and an admissible switch. A new organizational allocation needs effective authority, informed participants and preserved obligations. Existing work and performed history do not disappear when the new arrangement is selected.

**C.11** supplies a reasoned local choice among the explained alternatives; the right to commit resources or direct action remains separately established under the actual permission and agreement relations; use **C.11.DUA** when the value of another observation, calculation or trial is itself unresolved. A constructed case can justify a conditional proposal. An effectiveness claim requires evidence from its intended use. Do not require a new trial when existing adequate evidence settles the decision, and do not count a simulated or taught example as operational evidence.

Return the chosen alternative, accepted trade-off and conditions of use to the receiving engineering or organizational decision. If only a candidate comparison was requested, it can finish here without authorizing implementation.

#### C.32.LCA:4.11 - Make the result usable and revise the affected dependence

Explain the result in the ordinary form needed by its users. It must make recoverable:

- the intended outcome and protected conditions;
- the participants, decisions and available interventions;
- the information, exchange and timing that connect them;
- the jointly feasible conditions, continuation and exception response;
- the serious alternative, accepted cost and basis of the present choice;
- the changed observation or condition that requires a different decision.

These are content requirements, not a mandatory record or a demand to model every relationship in the enterprise.

On new evidence, first identify the failed dependence. A fresh observation may only require a new state estimate. A different response can challenge the dynamics or capability. A blocked authorization can require a different allocation or commitment. A changed use can require a revised goal. Alter the architecture when the needed continuation cannot be obtained adequately within the existing arrangement.

Carry the change through its direct consumers. A new estimate can change the admissible command; that command can change arrival time; the changed arrival can defeat an organizational promise. Preserve unaffected results, and requalify the connections that actually changed.

