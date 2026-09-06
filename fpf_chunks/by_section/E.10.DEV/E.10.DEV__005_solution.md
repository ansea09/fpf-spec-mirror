---
chunk_kind: "child"
pattern_id: "E.10.DEV"
pattern_title: "Recovering What Development or Evolution Means in the Current Claim"
section_id: "E.10.DEV:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.10.DEV/E.10.DEV__005_solution.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "E.10.DEV — Recovering What Development or Evolution Means in the Current Claim"
  - "E.10.DEV:4 — Solution"
line_start: 76700
line_end: 76758
dependencies:
  - "A.15"
  - "A.2.2"
  - "A.3.3"
  - "A.3.4.P"
  - "B.4"
  - "C.17"
  - "C.19"
  - "C.27.TA"
  - "C.29"
  - "C.36"
  - "C.36.P"
  - "E.10"
  - "E.10.ARCH"
  - "E.10.LRN"
  - "E.10.MOVE"
  - "E.23.CAE"
  - "E.23.CDI"
  - "F.19"
keywords:
---

### E.10.DEV:4 - Solution

Recover the current claim from the subject and use rather than from the umbrella word.

1. **Bound the wording span.** Open only the expression whose interpretation changes a claim, inference, or action.
2. **Name the changed or represented subject.** Identify the exact System, capability, organization, campaign, population, lineage, archive or front arrangement, model, plan subject, episteme, or other direct subject.
3. **State continuity or membership.** Name only the identity, reidentification, membership, generation, lineage, edition, or retention rule needed by this use.
4. **Separate neighboring objects.** Keep actual change, intervention Work, Method, plan, result episteme, evidence, representation, and later effect distinct.
5. **Expose direction or value only when claimed.** Name the objective, characteristic, scale, polarity, viewpoint, and evidence needed by the receiving use. The word *development* does not establish improvement.
6. **State posture.** Mark the claim's posture—for example, actual, observed, reconstructed, predicted, simulated, proposed, recommended, or planned.
7. **Choose one direct branch.** Split the sentence when it carries several independently actionable claims.
8. **Stop after recovery.** The allowed recovery outcomes are the repaired claim, ordinary non-use, quote-only use, missing information, direct owner, or exact architecture gap. State the next use or stop for the selected outcome.

#### E.10.DEV:4.1 - Optional DevelopmentEvolutionWordingRecoveryLine

Write the ordinary sentence first. Keep the following temporary line only when another use must inspect or replay the recovery:

```text
DevelopmentEvolutionWordingRecoveryLine:
  triggerSpan:
  changedOrRepresentedSubjectRef:
  continuityOrMembershipBasis?:
  posture:
  directionOrValueBasis?:
  recoveredClaim:
  directPatternRefs:
  blockedOverread?:
  nextUseOrStop:
  currentnessOrReopen?:
```

`blockedOverread?` states a rejected reading only when independent local evidence makes that reading plausible to the intended reader and deleting the boundary would change understanding, selection, safety, reliance, stop, or action. This temporary line supports inspection or replay of the wording repair; admission of a substantive product uses its direct owner. Omit fields the receiving use does not need.

#### E.10.DEV:4.2 - Direct branches

| Recovered current claim | Direct route and boundary |
| --- | --- |
| One identified entity actually changed under conditions | Use `A.3.4`, `A.3.4.P`, `B.4`, and `C.27.TA` as applicable. A sequence, record, intervention, or expected result does not establish the actual transformation or identity-through-change claim. |
| One holder has or changed capability for a named Work family | Use current `A.2.2` for the capability and A.10 for relied-on evidence. When a prior result now fails, transfers poorly, or varies with conditions and a distinction among envelope and support, applicability, access or activation, adaptation, enactment, and capability-claim revision can change the next question, use current `E.23.CAE` only for that differential. Its disposition is not a `ChoiceResult`, authorization, trajectory selection, or selected development Work. Candidate `E.23.CDI` may govern a separate capability-development Method only after its own admission and a separate applicable steering or choice result selects capability development. Keep provider Work, representative later Work, transfer, effect, and causal contribution separate. |
| An organization, campaign, producing arrangement, or product-development arrangement changed | Identify the actual kind and its direct owner, then the Work, Methods, authority, interfaces, capabilities, evidence, and effects needed by the claim. Use System or programme classification when that owner's rules establish it. Use `A.3.4`, `C.30`, `C.32.MWA`, A.15 family, current OCE contributions, and the owning DPF as applicable. Establish any success claim under its declared basis. |
| An episteme, problem formulation, body of knowledge, or MethodDescription changed | Identify the exact episteme and edition or ClaimGraph, its EntityOfConcern and effective ReferenceScheme, source return, evidence use, and currentness; use `C.2.1`, `C.22.2` for the problem formulation, `A.3.2` only for an exact one-Method description, `A.6.3.RT`, A.10, and `G.11` as applicable. Revision Work or publication does not by itself establish truth, a changed Method, or a developed holder. |
| A cultural population or discipline generated, transmitted, reconstructed, recognized, selected, retained, or lost variants | Use `C.36` and `C.36.P`. Preserve the population or practice boundary, period, variants, relations, intervention, and evidence. |
| A non-cultural population or lineage evolved | Recover only the dimensions on which this claim or its use relies. Possible dimensions include population or lineage identity, membership, generation, reproduction or inheritance, variation, selection, retention or loss, environment, distribution, posture, and evidence. Use an admitted domain owner for their meaning and requirements; otherwise return the named non-cultural population or lineage architecture gap. Do not substitute `C.36` or one-holder `B.4`. |
| An engineering search changed its archive, front, pool, generator policy, or possibility space | Use `C.17`–`C.19`, `G.5`, and `G.11`. Archive or front history is not population evolution unless the population relations independently obtain. |
| A model predicts or simulates development or evolution | Use `A.3.3`, `A.19`, `C.29`, and `C.27`; name model edition, state or position space, transition law, observation relation, validity boundary, and posture. Model output is not actual change. |
| A practitioner proposes development opportunities or a programme | Use `C.22.2`, `C.11.CRC`, `C.11`, A.15.2, and the owning domain Method. Recommendation, choice, WorkPlan, performed Work, and observed effect remain different results. |
| The current expression means learning, teaching, training, model fitting, inference, or information acquisition | Use `E.10.LRN`, then the direct subject pattern. Learning neither absorbs nor classifies every development branch. |
| The wording is ordinary or quoted and supports no FPF inference | Preserve it and stop. Recover a branch only if a later use relies on the stronger claim. |

#### E.10.DEV:4.3 - Coordination with trajectory wording

The phrase *development trajectory* does not require two full repairs by spelling alone.

- Start with `E.10.DEV` when the action-changing doubt is which subject is developing, what remains identifiable, or whether improvement is asserted. If that repair also makes the path wording harmless, stop.
- Continue to `E.10.MOVE` only when the trajectory itself still carries a separate claim about position space, order, segment identity, actual, predicted, or planned posture, or representation.
- Start with `E.10.MOVE` when the bearer and development claim are already clear and only the path or trajectory posture is unresolved. Invoke `E.10.DEV` afterward only if a distinct development or evolution ambiguity remains.

Both routes must converge on the same direct subject claim or exact gap. Neither child creates a `DevelopmentTrajectory` kind, and no recovery note is required for a clear local sentence.

