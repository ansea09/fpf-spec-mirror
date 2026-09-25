---
chunk_kind: "child"
pattern_id: "A.6.A"
pattern_title: "Affordance and Action-Invitation Precision Restoration (ACT-INV)"
section_id: "A.6.A:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.A/A.6.A__006_archetypal-grounding.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "A.6.A — Affordance and Action-Invitation Precision Restoration (ACT-INV)"
  - "A.6.A:5 — Archetypal Grounding"
line_start: 19628
line_end: 19677
dependencies:
  - "A.15"
  - "A.16"
  - "A.16.0"
  - "A.16.1"
  - "A.16.2"
  - "A.3"
  - "A.6.B"
  - "A.6.P"
  - "A.6.REL"
  - "A.7"
  - "B.4.1"
  - "B.5.2.0"
  - "C.16.Q"
  - "C.2.2a"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.17"
  - "F.18"
  - "F.9"
keywords:
  - "action-first language"
  - "affordance"
  - "detection"
  - "inquiry question"
  - "physical opportunity"
  - "wording recovery"
---

### A.6.A:5 - Archetypal Grounding

#### A.6.A:5.1 - Tell

Read an affordance-like sentence as a question about its intended meaning. The result can be an ordinary supported claim, a proposed action, an inquiry question, or an exact gap. Keep the subject conditions that make that result usable. An optional record can express the result but does not give different subjects one obtaining predicate.

#### A.6.A:5.2 - Show (System case)

**Draft:** “The alarm calls for rollback.”

**Repair A — control and incident line**

Recover the proposed use: OpsTeam_Phoenix is considering RollbackMethod_R41 on Release_R41 in ProdCluster_EU_1 during RunWindow_RW. RollbackRunbook_R41 describes that Method. AlarmBundle_AB9 exposes the cue about ServiceState_S7; AnomalyPolicy_AP7 detected it. AlertTrace_91 and ErrorBudgetSeries_4 are candidate evidence for applying IncidentPolicy_IP2 over Horizon_H15m.

The first useful statement is: “Check whether the current incident-policy guard and authority permit this team to use RollbackMethod_R41 on Release_R41 in this window; the alarm alone does not settle that question.” If the rule and facts establish a required rollback, state that independently grounded duty or gate result. Otherwise retain the proposed action or the precise missing condition. Nothing in these supplied names asserts a performed rollback.

If the receiving operational review uses `VP.OperationsControl`, resolve its `U.ViewpointRef` under `OperationsControlScheme_2026`. `OperationsRollbackView_9` remains an independently identified C.2.1 episteme and a `U.View` only if its exact E.17.0 conformance obtains. These are optional, separately established references, not additional requirements to understand the alarm sentence.

**Recognizable near misses.** A runbook reference alone does not identify the Method selected for enactment. A viewpoint field does not make a dashboard a `U.View`. The alarm, a recovery note or a `PolicyHook` does not prove duty, gate passage or performed Work.

**Repair B — ecological and robot line**

**Draft:** “This handle affords pulling.”

Recover the proposed physical claim: ServiceRobot_R2 can pull DoorHandle_17 along Axis_A1 in Window_W1 while the door is closed, under the actual reach, grip and clearance conditions described by ReachEnvelope_RE2, GripClass_G1 and ClearanceProfile_CP3. The reach description is not the physical reach condition itself. PerceptionStack_PS4 is the detector; DepthFrame_883 and ContactModelRun_17 are candidate evidence.

**Result with the supplied information.** These names identify the question but provide neither the physical obtaining predicate nor its required readings. Return: “Can R2 pull this handle along A1 in W1 under the specified grip, clearance and reach conditions? The applicable physical rule and its supported inputs are still needed.” A rule that requires sufficient contact force or a collision-free path must say so and be supported by the relevant measurements or model result. Naming G1, CP3 or a model run does not establish those conditions.

When that subject rule and the evidence support the claim, return the qualified physical statement directly. If the receiving task instead needs an executable manipulation plan and already has a suitable domain method, use its required observations and constraint representation. Reuse any adequate existing interpretation; producing another recovery note adds nothing by itself. With the same robot, grip, clearance, reach and door facts, changing PS4 can change detection without changing the physical opportunity. Changing an operator cue can likewise change what the operator notices. Withdrawing the description changes its availability; it does not close the door or remove the opportunity. A different, information-constituted relation must be assessed under its own predicate rather than inferred from this physical case.

#### A.6.A:5.3 - Show (Episteme case)

**Draft:** “This problem asks for a better question.”

**Repair A — epistemic probe line**

`ProblemFramingEpisode_PF3` is the framing account, `ResearchTeam_A` the intended inquirer and `Reviewer_A1` the detector of the problem. Keep `ExemplarPack_EP3`, `OpenIssueSet_O2`, `EpisodeNotes_3` and `CounterexampleCard_2` as its named source context.

For this worked case, take EP3 to compare detected and missed handle opportunities with the robot, grip and clearance facts fixed. O2 asks whether a changed physical opportunity or a changed detector explains the discrepancy. CounterexampleCard_2 records the same physical configuration with a different detection result. The recovered question is: “With the physical conditions held fixed, does changing PS4's detection configuration change which pulling opportunities are detected?” The counterexample motivates that inquiry; it does not already establish its answer or a general detector effect.

This question is the first useful result. If further question construction is needed, the team can select the already admitted `ContrastiveQuestioningMethod_Q2`; `ContrastiveQuestioning_Q2` is its separate MethodDescription. An explanatory prompt follows B.5.2.0 when its conditions hold. Choosing the inquiry, scheduling it and actually performing it remain separate claims. No invitation occurrence or compulsory `OptionSet` precedes the question.

**Repair B — closure-advance line**

**Draft:** “The draft is ready for formalization.”

Recover the proposed clarification: `AuthorCollective_C1` would express `DraftHypothesis_H7` using `TypedInvariantSet_V1` within `ClaimScope_G1`. `ReviewPanel_R4` points to `AmbiguityMemo_8` and `ReviewCommentSet_5` as grounds for that move.

Return the actual question: “Which unresolved claims in H7 can V1 express under G1, and which ambiguities would remain?” If the receiving rule establishes readiness, state its qualified result and the proposed action. The named memo and comments alone establish neither readiness, Formality F, acceptance nor performed formalization. A sufficient question can remain open without becoming a generic invitation record.

