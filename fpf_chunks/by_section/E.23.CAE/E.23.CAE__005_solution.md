---
chunk_kind: "child"
pattern_id: "E.23.CAE"
pattern_title: "Capability Access and Expression Differential Probe"
section_id: "E.23.CAE:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23.CAE/E.23.CAE__005_solution.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "E.23.CAE — Capability Access and Expression Differential Probe"
  - "E.23.CAE:4 — Solution"
line_start: 90309
line_end: 90404
dependencies:
  - "A.15.7"
  - "A.15.8"
  - "A.2.2"
  - "C.11"
  - "C.36"
  - "E.10.LRN"
  - "E.23"
  - "E.23.CDI"
keywords:
---

### E.23.CAE:4 - Solution

#### E.23.CAE:4.1 - Bind the claim before probing

Name only the values that can change the probe or its later use:

1. the exact holder System;
2. the named Work family or exact current demand;
3. the capability envelope, measures, evidence, and qualification window currently relied upon;
4. the prior qualified result or reference condition;
5. the present failure or unstable expression;
6. the relevant performer and support configuration;
7. any development, rehearsal, procedure change, parameter update, model update, calibration, or other change that must be held fixed where safe;
8. protected conditions and probe limits; and
9. the receiving question that a differential observation could change.

If the holder or Work family is unclear, return to `A.2.2`. If the current demand is already outside the claimed envelope, return `outsideClaimedEnvelope` and stop the loss diagnosis. If a known configuration failure fully explains the case, use `A.15.8` and stop here.

For a compact retained account, use this local shape only when another use needs it:

```text
CapabilityAccessExpressionProbe@Use:
  holderRef:
  workFamilyOrDemand:
  claimedEnvelopeAndWindow:
  priorReferenceCondition:
  presentObservation:
  controlledChangeCondition:
  protectedConditions:
  disposition:
  strongestSurvivingRival:
  unsupportedUse:
  candidateRoutes:
```

This card is a local Method result, not a new FPF kind. Its fields create no capability, context, memory, choice, authorization, Work, or causal relation.

#### E.23.CAE:4.2 - Run the differential probe

1. **Check the demand against the claim.** Confirm that the current task belongs to the Work family and capability envelope being relied upon. Compare measures and qualification windows before calling a difference loss or transfer failure.
2. **Recover the relevant configuration.** Name actual or intended performers, roles, tools, records, interfaces, authority, environmental conditions, state, and other supports only where their direct rules apply. Use `A.15.8` when one exact Work or WorkPlan configuration is current.
3. **Hold development and updating fixed.** During the contrast, avoid new teaching, rehearsal, procedure rewrite, fine-tuning, parameter update, recalibration, or other development where safe and feasible. If the probe necessarily changes the holder, mark the affected distinction unresolved or narrow the claim.
4. **Return to a qualified reference condition.** Recreate a previously successful or separately qualified condition without further development. Prefer an `A → B → A` or equivalent return when order, recency, or transition history can matter. Reappearance rejects simple global loss under those tested conditions; it does not establish general transfer.
5. **Vary a decision-bearing condition.** Change the smallest condition that can distinguish live rivals: an overt cue, cue reliability, preceding decision state or uncertainty, role, record, authority, tool, task or context identifier, state feedback, blocked versus interleaved order, transition frequency, or another domain-relevant condition. A label or visible setting is not assumed to be the effective context.
6. **Observe applicability separately.** Ask whether the relevant Method, response, routine, policy, or prior case is selected as applicable before judging execution. For a person this may involve recognition or choice; for an organization it may involve routing, role, record, or authorization; for AI or robotics it may involve task/context identification, policy routing, or function activation. These are different mechanisms occupying one observational position.
7. **Separate availability, adaptation, enactment, and result.** Where the case permits, observe whether the response can be accessed or activated, whether it can be transformed for the changed demand, whether the actual performer arrangement can enact it, and whether the required result obtains. A later failure does not by itself establish an earlier one.
8. **Compare live rivals.** Retain every explanation still compatible with the observations. Ordinary cue effects, interference, envelope mismatch, configuration loss, applicability failure, access or activation failure, adaptation failure, enactment failure, and actual holder change are not synonyms.
9. **Return a disposition and candidate routes.** State the earliest supported distinction, evidence and conditions, strongest surviving rival, unsupported overread, and patterns or domain Methods that could receive the result. Do not select a route merely because the probe produced a disposition.

These steps organize observations, not a universal cognitive pipeline. A holder may implement them through simultaneous, recurrent, distributed, or structurally different processes.

#### E.23.CAE:4.3 - Qualify the disposition

| Differential disposition | Minimum useful observation | Candidate route | What the observation does not establish |
| --- | --- | --- | --- |
| `outsideClaimedEnvelope` | The current demand differs on an envelope coordinate excluded from or unsupported by the current capability claim. | Reframe the claim through `A.2.2`, or open development only through a separate next-action or choice result. | Loss or forgetting inside the old envelope. |
| `configurationOrSupportUnavailable` | Performance changes with a controlled performer, role, record, tool, interface, authority, state, or environment contrast. | `A.15.8` and the direct owner of the failed relation. | Changed holder capability or a human-like memory in a collective. |
| `responseAvailableUnderReferenceCondition` | The prior response or result reappears in a qualified reference condition without new development or update. | Probe applicability, transfer, adaptation, or enactment; then use the applicable steering or choice pattern. | Whole-envelope capability, a particular retrieval mechanism, or sufficient transfer. |
| `applicabilitySelectionFailureSupported` | The response can be produced when selected or prompted, but is not identified, routed, or authorized as applicable under the target demand. | Holder-specific HCD, organization, AI/robotics, or domain inquiry; `A.15.7` or `C.11` only under their own entry conditions. | One common recognition mechanism or the intervention to choose. |
| `accessOrActivationFailureSupported` | Applicability is established, yet access or activation changes under a controlled cue, task/context, or routing contrast before adaptation and enactment. | Holder-specific access, retrieval, activation, or routing inquiry. | Erased content, a universal latent context, or a sufficient repair. |
| `contextDependentExpressionOrInterferenceSupported` | Expression changes systematically with a qualified context, cue-reliability, or transition-statistics contrast and can reappear without development. | Holder-specific explanation and development Method when separately selected. | The hidden context representation or memory architecture that caused the observation. |
| `adaptationFailureSupported` | The response is selected and available, but cannot be transformed to the changed demand while enactment supports are adequate. | Direct adaptation or domain Method inquiry. | Loss of the original response or the correct adaptation Method. |
| `enactmentFailureSupported` | The response or adapted Method is selected and available, but performer assignment, coordination, authority, body, actuator, interface, tool, or another condition prevents actual Work or its result. | `A.15.8`, performer/authority owners, and the direct domain Method. | Capability change when the necessary performer arrangement did not obtain. |
| `capabilityClaimRevisionWarranted` | Qualified reference and target probes fail across relevant conditions, envelope and configuration rivals have been addressed, and holder-specific evidence supports changed ability in the stated window. | Reassess the `A.2.2` capability claim; use a separate steering or choice result before development. | A specific human, organizational, model, or controller memory mechanism. |
| `unresolvedDifferential` | Safety, missing reference evidence, concurrent updating, coupled changes, insufficient measures, or surviving rivals block a responsible distinction. | Obtain the missing evidence, use a protected test, narrow the claim, or stop. | Permission to choose the most familiar explanation. |

One case may support several ordered dispositions. Keep each observation and its limits visible. No disposition is a `ChoiceResult`, authorization, selected next Work, or performed Work.

#### E.23.CAE:4.4 - Keep recognition and assurance separate

**Recognition.** A quick return probe is warranted when the practitioner hears “it worked before,” “the model forgot,” “the team knows the routine,” “the dancer can do it only in class,” or another apparent-loss phrase and at least two live explanations would lead to different next Work.

**Assurance.** Stronger reliance needs proportionate evidence:

- a qualified reference basis rather than a nostalgic recollection or one cherry-picked success;
- commensurable measures, envelopes, configurations, and windows;
- protection against probe-induced learning, fatigue, priming, adaptation, or update;
- enough order, cue-reliability, and transition variation to address the live rival;
- replay, simulation, staged testing, or specialist assurance when live probing would be unsafe; and
- holder-specific evidence before claiming a memory mechanism, causal explanation, or actual capability change.

A cheap reversible probe can support a narrow disposition. A high-stakes capability-loss, safety, medical, employment, deployment, or public-performance decision may require a direct domain evaluation and assurance account before anyone relies on the result.

#### E.23.CAE:4.5 - Route without choosing

The first result should fit in six lines:

> **Claim tested:** [holder, Work family, envelope, window].
> **Controlled contrast:** [reference, changed condition, and what was held fixed].
> **Observation:** [what reappeared, disappeared, or changed first].
> **Disposition:** [qualified differential result].
> **Surviving rival and limit:** [what remains plausible and what is not established].
> **Candidate routes:** [patterns or domain Methods that could receive the result].

During ongoing Work, `A.15.7` can use the disposition as current information while recovering a next action. Use `C.11` only when a current chooser and `OptionSet` already exist and comparison or another probe can change the choice. `E.23.CAE` supplies neither pattern's result. Use `E.23.CDI` only after a separate applicable steering or choice result selects capability development.

