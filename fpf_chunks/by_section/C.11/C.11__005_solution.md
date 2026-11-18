---
chunk_kind: "child"
pattern_id: "C.11"
pattern_title: "Decision Theory (Decsn-CAL)"
section_id: "C.11:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.11/C.11__005_solution.md"
commit_sha: "ffd3e6add6f2de6931c1da794f74c86d071fb9fd"
heading_path:
  - "C.11 — Decision Theory (Decsn-CAL)"
  - "C.11:4 — Solution"
line_start: 59274
line_end: 59733
dependencies:
  - "A.10"
  - "A.13"
  - "A.18"
  - "A.19"
  - "A.6.5"
  - "A.6.P"
  - "C.11.CRC"
  - "C.11.DUA"
  - "C.17"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.26"
  - "C.38"
  - "C.39"
  - "C.40"
  - "C.9"
  - "E.10.LRN"
  - "G.5"
keywords:
  - "ChoiceResult"
  - "ChoiceRule"
  - "DecisionSubject"
  - "OptionSet"
  - "ValueOfComputation"
  - "ValueOfInformation"
  - "choose now"
  - "comparison basis"
  - "decision theory"
  - "non-shared comparison frame"
  - "probe again"
  - "probe-worthiness"
  - "question order"
  - "reject current set"
  - "reroute"
---

### C.11:4 - Solution
#### C.11:4.1a - Causal-use hook for choice records

When a choice depends on an effect, intervention, counterfactual, causal-policy, or off-policy claim, the `ChoiceResult` keeps the decision question local and cites the C.28 support result as one basis.

```text
ChoiceResult.causalUseSpec?:
  causalUseQuestionRef?: CausalUseQuestionRef
  targetCausalityLadderRung: CausalityLadderRung
  causalUseClaimKind: CausalUseClaimKind
  causalActionPolicyClass?: CausalActionPolicyClass
  causalSupportComponentRefs?: CausalSupportComponentRefs
  causalUseEvidenceDesignRef?
  causalUseSupportResultRef?: CausalUseSupportResultRef
  supportedUse
  unsupportedUse
```

Omit the tail when causal support changes neither the comparison nor the chosen result. If causal wording changes the result, include the tail or downgrade the wording. A C.28 result does not choose, permit, or deploy an option; C.11 uses it with the other decision premises and may still select, defer, or abstain.

#### C.11:4.1 - Primary EntityOfConcern and admissible choice result

`C.11` governs theory-side choice among already-available options. Its selected decision result states what should be chosen from the current `OptionSet`, including whether further probing, information gathering, or computation is rational before the choice is fixed.

The OptionSet choice question begins only after an option set already exists. It does not form complete ways of obtaining one result, govern open-ended generation of options, or govern the execution order of a plan after a choice has already been made.

#### C.11:4.2 - Decision discipline over a live option set

Apply the `ChoiceRule` to the available `OptionSet`. A completed comparison yields one explicit `ChoiceResult` under that rule. If the basis still leaves the requested single choice open, §4.2.4 explains what to return to the holder now.

1. **Identify the chooser.**
   Name the `DecisionSubject`. Use `DecisionSubjectGranularity` to identify the unit to which the choice is attributed in this arrangement, for example a controller, a committee or an organization acting through a delegate. If attribution to a component or its containing system changes the result, establish their actual relation and which decision each makes.
   Distinguish the chooser from participants who provide evidence, advice or execution. Use `A.13` for a disputed claim about agency and the applicable assignment or mandate for a claim about who can decide.

2. **Freeze the current option set.**
   State the already-available options being compared now as one `OptionSet`.
   If the rows are only labels or fragments and the question is several complete ways to obtain the same result, stop here and apply `C.38`. Use `C.39` when a way to obtain the result still needs explanation, or `C.40` when usable material needs feasible variation and examination. Use `C.18` when generation-account or archive/front claims are needed.

3. **Make the comparison basis explicit.**
   State the preference or measure, current facts and uncertainty, and the `OutcomeModel` used to estimate each option’s consequences. Identify the use for which the options must qualify and any condition that excludes an option regardless of its score. Apply the same interpretation, horizon and material assumptions across options.
   The comparison is not usable if some options are being judged under one belief state and other options under one later, unmarked update.
   If rival outcome models give different rankings, compare all relevant options under each credible model. Show which conclusions hold across them and which depend on an unresolved assumption. A new measurement may update a parameter or the model. A disputed preference or mandate requires its own decision.

4. **Choose the dependence layer that governs the case.**
   Start from the evidential baseline when the choice is being compared through likely outcomes under the current `BeliefState`.
   Add one `InterventionModel` when taking one option changes the world through intervention rather than mere observation.
   Add one `CounterfactualModel` plus one `SubjunctiveDependenceRelation` when the case depends on one predictor, one structurally linked chooser, or one decision-procedure coupling that intervention talk alone does not capture.
   Use the least-committing dependence layer that still covers the live case, and do not switch layers across options without saying so explicitly.

5. **Compare a live inquiry alternative before commitment.**
   Consider another observation or computation when a plausible outcome could change the choice, the claim supporting it or the use for which it is admissible. Identify whose time or other resources the inquiry consumes. A mandatory check has the force and scope of its governing rule.
   Apply the probe-worthiness test to that alternative, stating the feasible probe, budget, cost and relevant information or computation value at the precision the choice needs. Otherwise this step adds no investigation or recording requirement. An empty form field does not activate inquiry, and no new search is required to certify that no other inquiry exists.
   Compare the best attainable next probe for this choice. A longer sequential experiment design can be a separate question. If an inquiry is binding, apply its governing terms to eligibility or use.
   When no worthwhile feasible probe remains, apply the choice rule to the evidence available. The cost of more inquiry can justify stopping. Selecting an option still needs grounds for its eligibility and preference. If a binding prerequisite remains unmet, keep the affected choice or use open, narrow it where the rule permits, or select an eligible alternative.
   If the expected gain warrants a feasible probe, return `probe again` and name it. After someone performs the probe, use its actual result to update the comparison. An inconclusive observation can leave the ranking unchanged.
   If one choice result is already fixed and the remaining probe would change only execution-path description, call-plan ordering, enactment budget, or checkpointing of that chosen option, stop treating the probe as local choice doctrine and apply `C.24`.

6. **Apply the `ChoiceRule` and report what it supports.**
   A completed comparison has one result form: `choose now`, `reject current set`, `probe again`, or `reroute because this is no longer local choice`. An open comparison can still inform the holder under §4.2.4.
   For `choose now`, give the option or retained set and its grounds. State whether the alternatives in a retained set are equally preferred or incomparable, and which further decision, if any, remains.
   If the result is `reject current set`, name the reason no current option survives under the present basis and, when more work follows, the neighboring question that now takes over.
   If the result is `probe again`, name the next probe and the exact comparison defect it is supposed to repair.
   State the conditions under which the result follows from the rule. If another person or system must adopt the recommendation, the result can go to them now.

##### C.11:4.2a - Receive heterogeneous premises without relabeling them as signals

An interesting observation, information-gain estimate, capability result, objective or reward, articulated former cue, or `C.17` characterization enters this pattern only under its exact source/result identity. Use `E.10.LRN` first when *learning* wording still hides that identity. Preserve the source and support needed for the bounded premise use. Reuse an adequate existing account; use `A.10` when the source-to-use account remains implicit or must be replayable. An applicable `RelianceDisposition` qualifies only that premise use.

An objective, reward, preference, or loss enters as the `EvaluativeMeasure`, `PreferenceOrder`, or `ChoiceRule` input it actually supplies and is not evidence by numerical form. When an `A.16.1` cue pack remains current as a source or provenance episteme, preserve that source identity and route the separately articulated endpoint result through its direct claim owner. A `C.17` novelty, surprise, use, or creativity characterization remains a characterization and does not license a move by itself.

No separate premise-qualification result sits between those owners and `C.11`. Use the qualified inputs in the live option/probe comparison and return only the existing `ChoiceResult`. When the missing comparison basis is specifically what a finite candidate contributes relative to the current configuration, use `C.11.CRC` to construct that ordinary comparison claim and return here. If every premise and the finite comparison are already explicit, proceed directly.

When a later outcome must first be compared with an earlier decision's actual relied-on basis, use `C.11.DBR` to localize the material difference and preserve unaffected uses. Return here when the current chooser, finite `OptionSet` and comparison basis are available. This prepares a particular reconsideration; it adds no qualification layer for otherwise ready premises.

##### C.11:4.2.1 - Well-formed comparison state


Well-formedness constraint: a live `C.11` comparison state is usable only when the decision record states the following, subject to the stated condition on inquiry:

- one `DecisionSubject` at one `DecisionSubjectGranularity`;
- one current `OptionSet`;
- one current comparison basis through `PreferenceOrder` or `EvaluativeMeasure`, plus one `BeliefState` and one `OutcomeModel`;
- one active dependence layer for the current comparison, unless the record explicitly says that comparison is still being reopened;
- when an inquiry alternative is live, an account of its feasibility, cost and possible contribution to the choice; when a decision or later use needs a retained inquiry limitation or reason, that minimum content in the same decision result.

An inactive inquiry item requires no empty value, no no-probe statement and no waiver. The chooser, option set, shared comparison basis and applicable dependence layer remain necessary.

The comparison is still unfinished, not yet wrong but not yet closeable, when any of the following remains true:

- the comparison moves between a participant’s preference and the collective decision without establishing whose rule applies;
- the option set is still changing while the record also claims to rank the options;
- one option is being judged under one belief state and another under one later update that is not itself declared as the next probe result;
- one heavier dependence layer is invoked for rhetorical force, but the record never states what defect of the lighter comparison it repairs;
- the record asks for more information without identifying a feasible inquiry and a plausible result that would change which option qualifies, the preference between options, or the claim on which the recipient could rely.

##### C.11:4.2.1a - Minimal admissible decision semantics

This minimal choice doctrine does not settle every decision-theory dispute, but it already supports some semantic distinctions by value and rules out others.

The comparison can use the following when their basis is explicit:

- an incomplete or partially ordered `PreferenceOrder`, with unresolved alternatives retained explicitly, a worthwhile further probe, or an unfinished comparison; incomparability alone does not justify `reject current set`, which requires the current rule to exclude every option;
- one `EvaluativeMeasure` for magnitude, threshold, or trade-off-sensitive cases, so long as the measure being used now is explicit enough to explain why the current result follows under it;
- one temporary unresolved criterion conflict, so long as the record says whether the present comparison is using one priority order, one threshold, one explicit trade-off measure, or one unfinished state that still blocks closure;
- one explicit `BeliefState` revision, so long as it enters the comparison as one named probe result or one named model repair rather than as one silent basis shift;
- a collective `DecisionSubject` when the decision is attributed to that body under its actual decision arrangement. If members disagree, establish the aggregation or delegation rule needed for the collective result.

The following are not admissible in this `C.11` body:

- silently totalizing one partial preference relation just to force `choose now`;
- silently switching from one criterion mix or one belief state to another across options;
- treating unresolved cross-scale or cross-collectivity conflict as a settled local ranking before the aggregation question has been resolved;
- using a record's form as a substitute for a stated comparison doctrine.

A partial order can leave alternatives incomparable. Equal preference means that the rule treats two alternatives as tied. If the receiving task accepts a set, the `retainedTieSet` field can list the retained alternatives and state which of these conditions holds. If the task needs one course, identify the applicable tie-break or the decision still needed.

##### C.11:4.2.2 - Probe-worthiness rule

Use the following three conditions to appraise an optional next probe for this choice. An independently binding condition continues to govern the affected option or use.

- the probe fits inside the remaining `ProbeBudget`;
- the expected improvement in the decision or its warranted use from the information or computation justifies the full `CostToProbe`, including delay and work displaced;
- a plausible result could change which option qualifies or is preferred, resolve a tie, reveal that the current set fails, change what use is warranted, or move the question elsewhere.

This is the local or myopic probe-worthiness rule for `C.11`: judge the best next feasible probe over the current `OptionSet`, not one whole non-myopic experiment design over longer horizons. Later sequential or non-myopic `OED` may strengthen this doctrine, but they do not relocate the local-choice question outside `C.11`.

Remaining uncertainty alone gives no reason to probe. State what plausible outcomes would change for the chooser. If every attainable result leaves the decision and its warranted use unchanged, this decision supplies no gain from that optional inquiry. An independently required check still follows its own rule.

If no worthwhile probe is available, state what the current basis and `ChoiceRule` support. If they leave the choice unresolved, name the missing premise or authority.

If the next probe would no longer change which option survives but would only change how one already-chosen option gets enacted, budgeted, or checkpointed, the question has already crossed to `C.24`.

##### C.11:4.2.3 - `ChoiceRule` versus `ChoiceResult`

`ChoiceRule` and `ChoiceResult` are not the same kind of thing.

- `ChoiceRule` is the doctrine or operator that says how the current comparison basis, dependence layer, and any applicable probe-worthiness value support one `ChoiceResult`.
- `ChoiceResult` records the conclusion reached by applying that rule to the present comparison.

A usable `ChoiceResult` gives the selected disposition and the grounds for it. It can inform a later decision or take effect directly under a delegated decision procedure. To establish which occurred, use the record of that decision or procedure.

The record has four result forms:

- `choose now`
- `reject current set`
- `probe again`
- `reroute`

A fifth soft result such as "keep thinking", "stay with the current view", or "the case is still complex" is not a conforming output. It is one unfinished state that still needs to be typed.

For `choose now`, the emitted `ChoiceResult` should show:

- the selected option or retained tie-set and the comparison basis supporting it;
- the outcome of a live inquiry comparison or a limitation needed by the decision or its recipient, when applicable.

For `reject current set`, the emitted `ChoiceResult` should show:

- that no member of the current `OptionSet` survives under the present comparison basis;
- the reason each option fails the stated conditions. Some options may fail for different reasons;
- the next neighboring question only when more work now follows, such as new option generation or one explicit escalation path.

For `probe again`, the emitted `ChoiceResult` should show:

- the next probe;
- the comparison defect that probe is expected to repair;
- the reason the probe is still worth its cost.

For `reroute`, the emitted `ChoiceResult` should show:

- the neighboring question and the pattern used to answer it;
- the reason this is no longer local choice among already-available options.

##### C.11:4.2.4 - Closure rule over the current `OptionSet`

The comparison may close as `choose now` only when all of the following are true together:

- the current `OptionSet` is stable enough that no further options are being invented for this comparison;
- the common basis and rule identify an eligible preferred option, or a set that the receiving task accepts. State whether the retained alternatives tie or remain incomparable;
- no feasible optional probe offers enough expected improvement in the selection or its warranted use to justify its full cost, and the selection meets the applicable prerequisites;
- the record still concerns local choice rather than pool policy, selector-result declaration, publication availability, or enactment.

The comparison may close as `reject current set` only when all of the following are true together:

- the current `OptionSet` is explicit and stable enough to reject as the present choice set;
- the current comparison basis is explicit enough to show why no member survives under the present basis;
- no feasible optional probe offers enough expected improvement to justify its cost in reconsidering that rejection or its warranted use;
- the result is still one local choice conclusion rather than a pool-policy, selector-result declaration, publication-availability, or enactment result.

Assess the probe conditions above from the current basis and any live inquiry alternative. They are conditions of a warranted choice, not a requirement to produce a separate account of omitted checking.

The comparison should close as `probe again` only when all of the following are true together:

- one next probe is named by value;
- that probe fits the remaining `ProbeBudget`;
- its expected contribution to the choice justifies its `CostToProbe`;
- at least one attainable result could change which option qualifies or is preferred, which claim or use is warranted, or where the question belongs. State what an inconclusive result would leave open when that matters.

The comparison should close as `reroute` when the record shows that the decision question has changed:

- to `C.38` when labels or fragments must first become complete-enough ways of obtaining the same result;
- to `C.39` when a way to obtain the result still needs explanation;
- to `C.40` when usable material needs feasible variation and examination;
- to `C.18` when the question concerns the generation account or archive/front stewardship;
- to `C.19` when the question is now how broadly to keep exploring or exploiting one candidate pool;
- to `C.24` when one choice result already exists and the next task is now sequencing, enactment, or execution-path probe work;
- to `G.5` when the next task is declaring or naming selector-facing selected-set content; when that result already exists, use `E.17` for its source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and audience availability.

If no closure condition holds, send the comparison the available basis supports. Identify the eligible alternatives, the missing comparison or priority, and who can settle it. For a requested single choice, retaining several candidates can inform the decision holder while their choice remains open. Record a `ChoiceResult` when the rule supports one of the four forms.

##### C.11:4.2.5 - Minimal decision-record form

A minimal `C.11` decision record has the shape below. Include `ProbeDecisionValue` only for a live inquiry alternative or an inquiry judgement whose content the decision or recipient needs. Include only the relevant information or computation value. A retained prose reason or limitation alone does not activate that block: put only the needed statement in `ChoiceResult`.

```text
DecisionSubject(...)
DecisionSubjectGranularity(...)
OptionSet(...)
ComparisonBasis(
  preferenceOrder or evaluativeMeasure,
  beliefState,
  outcomeModel,
  optional intervention/counterfactual/subjunctive layer
)
ChoiceRule(
  closure rule over the current basis and any applicable probe decision value
)
ProbeDecisionValue(  # conditional as described above
  probeActionSet,
  probeBudget,
  costToProbe,
  relevant valueOfInformation or valueOfComputation or both
)
ChoiceResult(
  choiceDisposition = choose_now | reject_current_set | probe_again | reroute,
  selectedOption or retainedTieSet or rejectedCurrentSet or nextProbe or rerouteOwner,
  grounds for this disposition under the current rule
)
```

Exact syntax is unnecessary. The chooser, options, shared comparison basis, `ChoiceRule` and `ChoiceResult` are required. Inquiry content is required only under the stated condition; an absent block requires no placeholder or omission explanation.

Use branch language only when it changes the comparison being performed.

##### C.11:4.2.6 - Resource-aware choice over an archive or front

- When the `OptionSet` is drawn from a `Front`, `Archive`, or their composition, identify that source basis.
- Apply one declared decision lens over that source family rather than assuming an unstated universal winner rule.
- `CostToProbe`, `ValueOfInformation`, and `ValueOfComputation` belong to that lens-side choice doctrine.
- They may justify another probe, one changed local comparison outcome, or one stop decision, but they do not rename the current `DominanceSet` and do not declare one shortlist-family result.
- If one candidate remains worth probing because its expected information value still exceeds its expected cost, say that explicitly as one lens-side choice judgement.
- If one archive point remains worth probing because it may change the frontier later, keep that as one resource-aware choice claim, not as evidence that the point is already on the current front.
- For an actual `A.19.SelectorMechanism` application, retain its set-returning declaration and bindings:
  - `A.19.SelectorMechanism` remains the cited set-return floor
  - `SelectionSlot` remains the selector output floor
  - if later selector-facing set-result declaration is required, that set-returning floor may support one `Shortlist` or one `RankedShortlist` in `G.5` rather than one forced single winner

#### C.11:4.3 - Dependence layers and neighboring repairs

##### C.11:4.3.1 - Classical evidential baseline

Stay with the classical evidential baseline when the question is to compare already-available options through preferences, utilities or desirabilities, beliefs, and likely outcomes under uncertainty.

In this baseline, the options are being compared as evidence about what consequences are likely if they are chosen. This is the ordinary default when intervention structure, predictor-coupling, or context-sensitive non-commutativity do not affect the comparison.

Typical choice results are:

- `choose now` because the current shared `BeliefState` and `OutcomeModel` already make one option or tie-set survive, and no still-feasible probe is worth its cost;
- `probe again` because one further observation, measurement, or comparison pass could still change the ranking without requiring a heavier causal, subjunctive, or context-order repair;
- `reroute` because the current decision question is no longer comparing one fixed `OptionSet`, but has become search, pool policy, selector-result declaration, publication-availability, or enactment work.

The baseline remains unfinished when the comparison cannot keep a shared `BeliefState` and `OutcomeModel` across the options, or when a limitation already calls for a further dependence layer and the comparison still uses only the evidential baseline.

##### C.11:4.3.2 - Causal repair

Switch on one `InterventionModel` when taking one option changes the world through intervention rather than merely signaling which outcome was already likely.

The comparative question changes: the working question is no longer only what this option indicates about the outcome, but what this option causes in the outcome structure.

Typical choice results are:

- `choose now` because, under the declared intervention structure, one option now causally dominates or remains the survivor and no remaining feasible probe can change that comparison with enough expected gain to justify its cost;
- `probe again` because an uncertainty about the effect of an intervention prevents the current comparison and the proposed probe could change which option is preferred;
- `reroute` because the intervention-use question has already moved from local choice into enactment planning, protocol design, or one neighboring question.

The causal repair is incomplete if the comparison still treats options only as evidence after invoking causal language, or if an `InterventionModel` is named without stating what defect of the lighter evidential comparison it repairs.

##### C.11:4.3.3 - Success-first or subjunctive repair

Switch on one `CounterfactualModel` plus one `SubjunctiveDependenceRelation` when Newcomb-like, blackmail-like, or other predictor-coupled cases remain under-described by the older evidential-versus-causal split.

What changes here is that the comparison must stay answerable to linked decision procedures, predictors, or structurally similar choosers rather than only to direct intervention on one local event.

Typical choice results are:

- `choose now` because, under the declared counterfactual or subjunctive structure, one option survives once the predictor-coupled comparison is made explicit;
- `probe again` because one further model clarification, predictor assumption check, or decision-procedure comparison could still reverse the current survivor relation;
- `reroute` because the governing decision question is no longer settling local choice doctrine but has become one wider characterization, negotiation, or enactment question that only borrowed predictor-coupling language.

If that coupled structure is not live, do not activate this branch. If a predictor-coupled or success-first repair is named but the linked structure that changes the comparison is still unspecified, the branch is not yet load-bearing in the current decision.

##### C.11:4.3.4 - Active-inference neighboring repair

Bring the active-inference line into view when the chooser is embodied, online, and socially coupled, and when the decision cannot be understood as one disembodied choose-then-act moment.

The comparison is no longer over one frozen snapshot alone. It must now ask whether an additional observation, coupled update, or socially mediated or role-expectation clarification changes what should be done now.

This minimal choice doctrine makes that social-expectation pressure explicit, but it does not yet operationalize one full `ROE` or `SocialExpectationRegime` object model inside `C.11`. If the case hinges on that machinery, the decision record should state that this local `C.11` floor does not settle it.

Typical choice results are:

- `probe again` because one further embodied observation, coupled update, or explicit role-expectation clarification can still change the state estimate enough to reverse the current survivor relation;
- `choose now` when further delay would close the window for an eligible option and the current comparison supports choosing it;
- `reroute` because the question has already become enactment sequencing or agent-characterization work rather than local choice.

`C.11` keeps the choice question visible there, but `A.13` still governs the narrower question of what kind of agent or agential system is in play. For measured characteristic and evidence claims, use `A.17` for Characteristic identity and arity, `A.18` for Scale and Coordinate bindings, `A.19` for the declared space and reusable predicate, `C.16` for the measurement account, and `A.10` for bounded reliance on the evidence. `C.24` still governs sequencing and enactment once a choice result has already been fixed.

Do not invoke this line only because one agent is acting in the world. Invoke it when embodied coupling, online updating, or explicit social-expectation pressure changes what the chooser should do now from the current `OptionSet`.

##### C.11:4.3.5 - Quantum-like neighboring repair

Bring the quantum-like line into view when context effects, order effects, response-replicability tension, or incompatible-question structure change the comparative state enough that one simple commutative probability reading no longer fits.

What changes here is the practical structure of comparison. One order of questioning or one framing path may produce one different survivor relation from another. The comparison must therefore either stabilize the comparison under one declared order or show why one more clarifying pass is still needed.

This minimal choice doctrine keeps the branch at that measurement-sensitive recognition point. It does not yet claim one full quantum-like state-space package inside `C.11`; it claims only that the live comparison may need one explicit measurement-class or order-sensitive repair rather than one plain commutative reading.

Typical choice results are:

- `choose now` under one declared order or framing because rival orders no longer change which option survives;
- `probe again` because one framing-sensitive comparison pass, one further question order, one response-replicability check, or one explicit measurement-class clarification could still reverse the survivor relation;
- `reroute` when the current decision question is no longer deciding among live options but has become one selector-result declaration, publication-availability, or enactment problem that only borrowed order-effect language rhetorically.

Do not promote this line to the unmarked default unless those repaired limitations are live in the case.

Do not invoke this line merely because a case feels psychologically subtle. Invoke it when one changed order, framing, response pattern, or incompatible-question structure changes the comparison state or the survivor relation in the live choice.

Use the evidential comparison when its dependence assumptions suffice for the decision. If two approaches recommend different options, identify the assumption responsible and what could decide between their uses.

These approaches can model the same choice under different assumptions. A causal or order-sensitive model may reverse a recommendation. To claim that one model strictly refines another, compare their feasible possibilities for the same inquiry and interpretation under B.5.MR. Establish what the second preserves and which previously possible answer it excludes.
#### C.11:4.4 - Reroute as soon as the question stops being local choice

Use `C.11` while the question remains: from this current `OptionSet`, what should the `DecisionSubject` choose, and is another probe worth its cost before commitment?

A completed `ChoiceResult` answers the local comparison. Return it to the continuation that needs it, preserving the evidence, information and action conditions used in the choice. Under **C.43**, a changed goal, available means or later observation can reopen the appropriate contribution without requiring the whole control task to become one fixed option set. The local next-probe rule below is not a general solution for all sequential information acquisition.

Reroute immediately when the question changes:

- If the current rows are labels or fragments and the question is how several complete ways could obtain the same result, leave this pattern and work in `C.38` first.
- If a way to obtain the result still needs explanation, use `C.39`. If usable material needs feasible variation and examination, use `C.40`. Use `C.18` when the question concerns the generation account or archive/front stewardship.
- If the options already exist but the question is how broadly to keep exploring or exploiting the candidate pool, leave this pattern and work in `C.19`, where the next useful output is one explicit pool-policy result rather than one local `ChoiceResult`.
- If one option is already chosen and the question is how to sequence, budget, or enact that choice, leave this pattern and work in `C.24`, where the next useful output is one enactment-facing call plan or `CheckpointReturn`.
- If the question has shifted from deciding to declaring or naming selector-facing selected-set content, leave this pattern and work in `G.5`. Its next useful output may be a `Shortlist` or `RankedShortlist` when alternatives remain for later choice, a `JointUseSet` when every named member is included for one bounded use, a narrowed handoff, abstain, or escalation. None is one more local `ChoiceResult`.

  If that result already exists and the current question is presentation or availability to an audience, use `E.17` for the source-backed publication face and return to source and `E.24.PUB` for the publication occurrence and availability.

`ProbeBudget` covers the resources available for further observation or deliberation while the choice or reliance on it can still change. `ValueOfInformation` and `ValueOfComputation` express the expected improvement compared with deciding now. Once the choice and its permitted use are settled, the budget for performing or sequencing the selected work belongs to C.24. C.19 and C.24 may use these measures in their own decisions.

Outside this pattern remain candidate generation, pool-wide exploration policy, selector-facing set-result declaration, publication availability, and execution planning.

#### C.11:4.5 - Minimal inventory and mathematical floor

The minimum usable inventory for this pattern is:

- subject and option objects: `DecisionSubject`, `DecisionSubjectGranularity`, `OptionSet`;
- evaluative and epistemic objects: `PreferenceOrder`, `EvaluativeMeasure`, `BeliefState`, `OutcomeModel`;
- dependence and comparison objects: `InterventionModel`, `CounterfactualModel`, `SubjunctiveDependenceRelation`, `ChoiceRule`, `ChoiceResult`;
- probe and bounded-resource objects: `ProbeActionSet`, `ProbeBudget`, `CostToProbe`, `ValueOfInformation`, `ValueOfComputation`.

The applicable objects from this inventory are required because the decision record must carry one explicit path from the `OptionSet` through the `ChoiceRule` to the emitted `ChoiceResult`.

##### C.11:4.5.1 - Always explicit versus conditionally activated objects

A completed `C.11` decision record makes the following objects explicit. For a comparison sent while the decision is open, identify the usable premises and the missing basis under §4.2.4.

- `DecisionSubject` and `DecisionSubjectGranularity`;
- `OptionSet`;
- one evaluative basis through `PreferenceOrder` or `EvaluativeMeasure`;
- `BeliefState`;
- `OutcomeModel`;
- `ChoiceRule`;
- `ChoiceResult`.

The following objects activate when the case needs them:

- `InterventionModel` for causal repair;
- `CounterfactualModel` plus `SubjunctiveDependenceRelation` for success-first or predictor-coupled repair;
- For a live inquiry, identify its `ProbeActionSet`, `ProbeBudget` and `CostToProbe`. Use `ValueOfInformation` for new observations, `ValueOfComputation` for additional reasoning over available evidence, or both when the inquiry needs both.

Use these names or ordinary wording that makes the applicable objects and their roles in the comparison recoverable.

Immediate lexical commitments:

- the default chooser term is `DecisionSubject`, not `Agent`;
- `DecisionSubjectGranularity` identifies the unit to which the decision is attributed. A committee may decide for itself or on behalf of an organization under a mandate. Where scale matters, identify the actual part and whole. B.5.MR compares the levels of abstraction or refinement of two models for a given inquiry; the same chooser can use both models.
- use `A.6.P` if a relation's predicate or participants remain unclear, and `A.6.5` when its argument or slot structure needs clarification.

Local plain glosses for the load-bearing inventory:

- `DecisionSubject`: the system making the decision, which can be a person, an automated controller, a committee or another organized body;
- `DecisionSubjectGranularity`: the unit to which the choice is attributed in this arrangement. A committee member can submit an individual ranking and the committee can decide by vote;
- `OptionSet`: the concrete options already on the table now;
- `PreferenceOrder`: the current better-than / worse-than ordering over those options for this decision subject;
- `EvaluativeMeasure`: the explicit utility-style or desirability-style scoring measure used when the case needs magnitudes, thresholds, or trade-offs rather than only one ordering;
- `BeliefState`: the current uncertainty-bearing state about the world, the case, and the likely consequences of the options;
- `OutcomeModel`: the model that maps options plus the current uncertainty picture to the consequences that matter for this choice;
- `InterventionModel`: the part of the model that says how the world changes because one option is actually taken;
- `CounterfactualModel`: the model used to compare relevant non-actual alternatives or alternate decision procedures;
- `SubjunctiveDependenceRelation`: the dependence between this choice and one predictor, one linked chooser, or one structurally similar decision procedure when intervention talk alone is not enough;
- `ChoiceRule`: the rule for evaluating the current alternatives and any worthwhile probe, and for reaching one of the four result forms;
- `ChoiceResult`: the disposition that follows from applying that rule, with the grounds the receiving use needs;
- `ProbeActionSet`: checks, measurements, simulations or questions available while the choice or its warranted use can still change;
- `ProbeBudget`: the money, time, attention or delay available for those inquiries;
- `CostToProbe`: the resources an inquiry would consume, including the work or benefit displaced by its delay;
- `ValueOfInformation`: the expected improvement in the decision from using the possible observation results, compared with choosing on what is known now;
- `ValueOfComputation`: the expected improvement in the decision from performing the proposed additional computation. Compare either gain with the inquiry’s cost on the same basis and count that cost once.

A person may make a decision, an organization may decide by an agreed procedure, or an automated controller may choose under delegated limits. An analyst, AI assistant or tool can also supply comparisons while another party decides. Identify the actual arrangement before attributing the decision.

This floor is enough to keep choice doctrine inspectable and stable. It does not yet assume one full branch-specific quantum-like package or one cross-scale geometry-heavy package.

##### C.11:4.5.2 - Boundary on multilevel and social-expectation doctrine

`DecisionSubject` and `DecisionSubjectGranularity` identify who makes the choice and whether it is an individual or collective decision. Several participants can contribute evidence or carry out the chosen course. Attribution to a larger system requires grounds for its decision, such as a collective rule or an authorized delegate acting within a mandate.

This minimal choice doctrine does not fully settle the broader questions that can accompany that chooser-bearing scope, including:

- collective aggregation doctrine over conflicting preferences or criteria;
- conflicts between the objectives of a participant, a group and a containing organization whose decisions are linked in this case;
- one full `ROE` or social-expectation structure for socially scaffolded choice;
- one full multilevel or geometry-heavy formal package for those cross-scale or cross-collective questions.

If one of these questions matters to the choice, retain the unresolved aggregation, social-expectation or multilevel premise and obtain its needed support. The local choice record alone does not settle it.

#### C.11:4.6 - Minimal decision tuple and finish condition

A `C.11` decision record is complete only when it states:

- who or what is choosing: `DecisionSubject` at one `DecisionSubjectGranularity`;
- what is currently choosable: `OptionSet`;
- how the options are compared: `PreferenceOrder` or `EvaluativeMeasure`, plus `BeliefState` and `OutcomeModel`;
- which heavier dependence layer is active when the case needs it: `InterventionModel` for causal repair, or `CounterfactualModel` plus `SubjunctiveDependenceRelation` for success-first or predictor-coupled repair;
- what comparison doctrine currently governs the case: one explicit `ChoiceRule`;
- when an inquiry alternative is live, an account of its feasibility, cost and possible contribution to the choice; when a decision or later use needs a retained inquiry limitation or reason, that minimum content in the same decision result.
- what the current comparison concludes: one emitted `ChoiceResult` that says choose now, reject the current set, probe again, or reroute.
  That result must name either the selected option, the retained tie-set, the rejected current set, or the next probe or reroute named by value.

The result is usable when `ChoiceResult` follows from the stated comparison basis, `ChoiceRule` and any applicable probe decision value.

A `C.11` pass is finished enough for practical use when all three conditions hold:

- the current comparison basis is explicit enough to explain the stated `ChoiceResult`: why an option or tie-set survives, no current option survives, or probing or rerouting is needed;
- any live inquiry alternative has been resolved sufficiently to support the choice, and the result retains any inquiry reason or limitation needed by this decision or its recipient;
- the next question is explicit: `choose now`, `reject current set`, `probe again`, or `reroute`.

An inactive inquiry item adds no placeholder or omission account to this tuple or finish condition.

If the current rule leaves alternatives tied or incomparable, report which and what that means for the receiving task. A result that retains several eligible options can supply a request for a set. Choosing one of them requires a rule or a decision by the designated chooser.

If those conditions are missing, retain the unfinished comparison and identify the premise or decision still needed.

