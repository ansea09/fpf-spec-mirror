---
chunk_kind: "child"
pattern_id: "A.15.7"
pattern_title: "Situation-Responsive Work Steering and Next-Action Selection"
section_id: "A.15.7:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.7/A.15.7__005_solution.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.15.7 — Situation-Responsive Work Steering and Next-Action Selection"
  - "A.15.7:4 — Solution"
line_start: 31536
line_end: 31583
dependencies:
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.15.6"
  - "A.19"
  - "A.3.1"
  - "B.1.5"
  - "C.11"
  - "C.18"
  - "C.24"
  - "F.6"
  - "G.11"
keywords:
---

### A.15.7:4 - Solution

Use the following steering Method. Keep the answer as small as the current decision permits, and stop as soon as a direct result or honest blocker is available.

#### A.15.7:4.1 - Keep the two Method positions distinct

The **domain Method** is the reusable way whose current enactment is being steered. It states the applicable way of doing, participant meanings, intended result or preserved condition, allowed variation, and stops.

The **steering Method** supplied here uses current facts to choose one next action within those limits.

One current Work occurrence may enact the domain Method and, when this steering Method is actually used, also enact the steering Method. Before either claim, use A.13 to identify the actual performer and A.15.1 to admit the dated Work independently. If this account must also say under which assignment the Work was performed, check that relation separately through F.6. Ground each `enactsMethod` claim separately; neither follows from the other. If the choice must be treated as a smaller Work occurrence, identify its own performer and Work basis and state its relation to the larger Work only when that relation actually obtains.

A domain Method may instead be an admitted composite containing the steering Method as a submethod. That requires the identity of both Methods and an exact composition relation under `A.3.1` and `B.1.5` or another direct composition rule. Method composition still does not prove that a particular Work occurrence enacted the submethod.

Reading this pattern, consulting a MethodDescription, following a plan, or receiving a recommendation does not by itself establish those Method, composition, or enactment claims.

#### A.15.7:4.2 - Run the seven-step steering Method

1. **Confirm current Work or close this entry.** Name the ongoing Work occurrence at the grain that changes the decision. When the performed-Work claim matters, use the full A.15.1:4.1 admission test, including the candidate occurrence's common construction and every actual performer's A.13 core. Ground the claimed domain-Method enactment as section 4.1 explains. If this steering account must also identify the assignment under which the Work was performed, check that assignment separately through F.6; F.6 identifies neither performer nor assignment. Its failure alone leaves independently admitted Work intact; if the same finding questions a premise of that admission, recheck that premise and the claims that depend on it. If Work has not begun, stop using this pattern: use `A.15.2` for intended-work content, `A.15.5` for work-entry readiness, or `C.11` only when a known chooser must compare an already formed `OptionSet`. Do not turn intended Work into a current occurrence or every small action into separate Work.
2. **Use only action-guiding information about current facts.** Name the relevant observation, participant response, available material, resource or safety limit, commitment, case fact, or time pressure. Recover the source and time conditions that can change its use. A missing timestamp or the age of a record alone does not defeat still-applicable information. When a changed condition or missing required support defeats a relied-on claim, retain the other qualified information and name the affected limit. Use `C.11.DUA` to compare a feasible, timely refresh with a supported narrower action, the declared safe fallback or stopping. Obtain the needed evidence for the selected use; do not act on an unsupported premise because refresh is costly. A directly checkable live cue needs an ordinary observation sentence, not a universal situation record or evidence dossier.
3. **Recover both Method positions.** State the domain Method and its relevant allowances and stops. When this steering Method is being used, keep that contribution clear. Add a separately grounded co-enactment or admitted-submethod account under section 4.1 only when that relationship is asserted or needed by the receiving use; an ordinary next-action answer need not assert either. Use a description, plan, policy, score, case model, recommendation or dashboard for the information it supplies to the deciding System.
4. **Form the smallest honest set of available actions.** Include only actions allowed now by the domain Method and named constraints. If the Method already requires one action and no material branch remains, follow it and stop using this pattern. If no acceptable action is known, use a subject-specific generation Method; use `C.18` only when an open-ended candidate archive and front are actually needed. Do not hide invention inside choice.
5. **Use the lightest truthful choice mode.** State the cue, comparison, quick forecast, value concern, or mandatory criterion that can change the answer. A reliable cue may support a familiar response after an applicability and consequence check. A claim that it is better than alternatives additionally needs the comparison rule and basis that establish that claim. An unfamiliar or consequential case may require diagnosis, adaptation, or a quick mental or physical forecast. When several live alternatives genuinely require comparison, pass the chooser, current `OptionSet` and comparison basis to `C.11`. Include an inquiry question only when it is live under C.11's conditions; an already supported choice needs no invented probe or omission account.
6. **Keep choosing, authority, and acting separate.** Name the deciding System and the intended performer. If the choice depends on permission, responsibility, commitment, capability, or authority, establish that exact relation instead of inferring it from a system-role label or recommendation score. If the required relation does not obtain or cannot be grounded, seek the missing basis from an appropriate source or stop. An obligation for another System to supply it needs its own ground.
7. **Return decision, performer, and feedback separately.** State the selected action and the reason that distinguished it, the intended performer, and the nearest stop, fallback, new observation, or return to ongoing Work. If the choice changes intended-work content, update the `U.WorkPlan` separately. If the receiving claim needs a distinct Work occurrence for the performed action, follow step 1 for its performer and independent admission; add F.6 only for assignment-bound attribution. Otherwise retain the action and observation at the current Work grain. Ground any asserted operation application separately. Use the resulting observation for the next choice. If it challenges an earlier Method-enactment or Work claim, recheck that claim and its dependents as in step 1; correct or retract the claim when the new grounds refute it. Preserve the actual performance history.

#### A.15.7:4.3 - Select the current branch

| Current situation | What to use now | Result and stop |
| --- | --- | --- |
| The domain Method already requires one action | Follow the Method or its selected description directly. | The required action and its existing stop; no steering or decision wrapper. |
| One familiar live cue points to one response and a quick consequence check passes | Use the recognition branch in this pattern. | One decision, intended performer, live cue, and nearest return to ongoing Work. |
| Several admissible actions remain and comparison can change the choice | Use `C.11`; add `A.19` kernels only when their comparison or selection result matters. | A `ChoiceResult` under the applicable constraints. Return a fixed action here for performer and feedback; keep any retained tie-set explicit, and follow a `reject current set`, `probe again`, or `reroute` result to its stated next question. |
| The available actions are absent or inadequate | Use a subject-specific generation Method; use `C.18` only for an actual open-ended archive/front question. | New candidates or an honest failure to generate; no premature choice. |
| The action is fixed but calls to tools or services must be planned | Use `C.24`. | A call plan and checkpoint return; the call plan is not the underlying choice. |
| A changed condition or missing required support defeats an action-guiding claim | Keep the other qualified information; compare feasible, worthwhile refresh with a supported narrower action, the named safe fallback or stopping under §4.2. | Qualified information supports the selected continuation, with the affected limit stated. Age or a missing administrative time field alone does not invalidate an applicable claim. |
| Safety, authority, capability, applicability, or current Work is unresolved | Use the pattern that defines or tests the missing claim—for example, `A.2.2` for capability, `A.15.1` for performed Work, and `A.15.5` only for work-entry readiness; keep safety, authority, and applicability with the pattern that defines them. | The missing claim grounded under its own rule, or a named unresolved claim with return or stop; no action, permission, capability, Work, or Method change is inferred from the unresolved claim. |

A current account may treat an unexamined outcome or recurring adjustment as ordinary, so that no question enters this choice. `B.5.PI` uses a selected demonstration, handover or other ordinary work occasion to compare a result with its use and develop a question or retain an early cue. It requires actual access and attention, not a prior diagnosis. Use it when that contribution is needed; ordinary next-action selection does not require auditing every action.

When an available method repeatedly goes unconsidered at a relevant moment, use `A.15.11` to connect it with an occasion in the work. This can make a useful candidate available to step 4; the current constraints still determine which actions are admissible.

#### A.15.7:4.4 - Keep the first result light

For a reversible local use, speak plainly: “Choose track B because the room response changed and it still satisfies the promised genre constraint; the DJ performs the transition; abandon it if the next cue shows the transition is failing.”

When a current or later use needs an identified claim-bearing episteme, reuse a sufficient one or identify one under `C.2.1`. State the decision or observation it concerns and the distinctions on which that use relies. Arrange durable access when later reliance requires it.

