---
chunk_kind: "child"
pattern_id: "A.15.7"
pattern_title: "Situation-Responsive Work Steering and Next-Action Selection"
section_id: "A.15.7:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.7/A.15.7__005_solution.md"
commit_sha: "59c455329e49715c64dc1b16f22c1efba6a3cf6f"
heading_path:
  - "A.15.7 — Situation-Responsive Work Steering and Next-Action Selection"
  - "A.15.7:4 — Solution"
line_start: 27339
line_end: 27382
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

Usually, one current Work occurrence may enact the domain Method and, when this steering Method is actually used, also enact the steering Method. Before either claim, use A.13 to identify the actual performer and A.15.1 to admit the dated Work independently. If this account must also say under which assignment the Work was performed, check that relation separately through F.6. Ground each `enactsMethod` claim separately; neither follows from the other. If the choice must be treated as a smaller Work occurrence, identify its own performer and Work basis and state its relation to the larger Work only when that relation actually obtains.

A domain Method may instead be an admitted composite containing the steering Method as a submethod. That requires the identity of both Methods and an exact composition relation under `A.3.1` and `B.1.5` or another direct composition rule. Method composition still does not prove that a particular Work occurrence enacted the submethod.

Reading this pattern, consulting a MethodDescription, following a plan, or receiving a recommendation establishes none of those Method, composition, or enactment claims.

#### A.15.7:4.2 - Run the seven-step steering Method

1. **Confirm current Work or close this entry.** Name the ongoing Work occurrence at the grain that changes the decision. When the performed-Work claim matters, first use A.13 to identify the actual performer, then let A.15.1 independently admit the dated occurrence from its performance history, enacted domain Method, time, and required containing-System relation. If this steering account must also identify the assignment under which the Work was performed, check that assignment separately through F.6; F.6 identifies neither performer nor assignment, and a failed check leaves the Work intact. If Work has not begun, stop using this pattern: use `A.15.2` for intended-work content, `A.15.5` for work-entry readiness, or `C.11` only when a known chooser must compare an already formed `OptionSet`. Do not turn intended Work into a current occurrence or every small action into separate Work.
2. **Use only action-guiding information about current facts.** Name the relevant observation, participant response, available material, resource or safety limit, commitment, case fact, or time pressure. If an observation, report, recommendation, displayed case-state claim, or other relied-on information may be out of date, has no checkable source, or has no stated time window for use, re-observe it or refresh it from its source; otherwise use a named safe fallback or stop. A directly checkable live cue needs an ordinary observation sentence, not a universal situation record or evidence dossier.
3. **Recover both Method positions.** State the domain Method and its relevant allowances and stops. State the steering Method only when it is actually used, and choose the separately grounded co-enactment or admitted-submethod account in §4.1. A description, plan, policy, score, case model, recommender, or dashboard may inform the decision; it neither acts nor decides.
4. **Form the smallest honest set of available actions.** Include only actions allowed now by the domain Method and named constraints. If the Method already requires one action and no material branch remains, follow it and stop using this pattern. If no acceptable action is known, use a subject-specific generation Method; use `C.18` only when an open-ended candidate archive and front are actually needed. Do not hide invention inside choice.
5. **Use the lightest truthful choice mode.** State the cue, comparison, quick forecast, value concern, or mandatory criterion that can change the answer. A reliable cue may select a familiar response after an applicability and consequence check. An unfamiliar or consequential case may require diagnosis, adaptation, or a quick mental or physical forecast. When several live alternatives genuinely require comparison, pass the chooser, current `OptionSet`, comparison basis, and probe question to `C.11`.
6. **Keep choosing, authority, and acting separate.** Name the deciding System and the intended performer. If the choice depends on permission, responsibility, commitment, capability, or authority, establish that exact relation instead of inferring it from a system-role label or recommendation score. If the required relation does not obtain or cannot be grounded, return to the System that must supply it or stop.
7. **Return decision, performer, and feedback separately.** State the selected action and the reason that distinguished it, the intended performer, and the nearest stop, fallback, new observation, or return to ongoing Work. If the choice changes intended-work content, update the `U.WorkPlan` separately. If the action is performed, follow step 1 to identify its actual performer and admit the dated Work; add F.6 only if the returned result must also identify the assignment under which the action was performed, and ground any operation application separately. Retain the resulting observation without rewriting the earlier Method or Work.

#### A.15.7:4.3 - Select the current branch

| Current situation | What to use now | Result and stop |
| --- | --- | --- |
| The domain Method already requires one action | Follow the Method or its selected description directly. | The required action and its existing stop; no steering or decision wrapper. |
| One familiar live cue points to one response and a quick consequence check passes | Use the recognition branch in this pattern. | One decision, intended performer, live cue, and nearest return to ongoing Work. |
| Several admissible actions remain and comparison can change the choice | Use `C.11`; add `A.19` kernels only when their comparison or selection result matters. | A `ChoiceResult` that fits the applicable constraints, then return here for performer and feedback. |
| The available actions are absent or inadequate | Use a subject-specific generation Method; use `C.18` only for an actual open-ended archive/front question. | New candidates or an honest failure to generate; no premature choice. |
| The action is fixed but calls to tools or services must be planned | Use `C.24`. | A call plan and checkpoint return; the call plan is not the underlying choice. |
| An observation, report, recommendation, case-state claim, or other action-guiding information is outdated or lacks usable time or source support | Re-observe it or obtain up-to-date information from a named source; otherwise use the named safe fallback or stop. | No action justified by an old recommendation, case-state claim, resource report, or participant-response report. |
| Safety, authority, capability, applicability, or current Work is unresolved | Use the pattern that defines or tests the missing claim—for example, `A.2.2` for capability, `A.15.1` for performed Work, and `A.15.5` only for work-entry readiness; keep safety, authority, and applicability with the pattern that defines them. | No fabricated action, permission, capability, Work, or Method change. |

#### A.15.7:4.4 - Keep the first result light

For a reversible local use, speak plainly: “Choose track B because the room response changed and it still satisfies the promised genre constraint; the DJ performs the transition; abandon it if the next cue shows the transition is failing.”

Only a named later use justifies a durable claim-bearing episteme. Identify it under `C.2.1`, state what exact decision or observation it concerns, and include only the source, currentness, authority, comparison, or assurance distinctions on which that use relies. Do not mint a general `SituationRecord`, `NextActionRecord`, or `FeedbackRecord` merely to preserve the template.

