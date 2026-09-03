---
chunk_kind: "child"
pattern_id: "A.11.OP"
pattern_title: "Decision-Relevant Least Action and Operational Parsimony"
section_id: "A.11.OP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.11.OP/A.11.OP__005_solution.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.11.OP — Decision-Relevant Least Action and Operational Parsimony"
  - "A.11.OP:4 — Solution"
line_start: 23564
line_end: 23629
dependencies:
  - "A.11"
  - "A.11.OP"
  - "A.15.7"
  - "A.3.1"
  - "A.3.2"
  - "B.3"
  - "C.19.2"
  - "E.11.PUA"
  - "E.11.PUR"
  - "E.13"
  - "E.23"
  - "E.5"
keywords:
---

### A.11.OP:4 - Solution

Apply one bounded admission question before making the proposed action or apparatus mandatory.

> **Admission rule.** An author or method designer **MUST NOT** make a proposed action or apparatus mandatory unless at least one materially plausible result can change a named substantive decision or branch within the declared horizon, the action realizes an already selected transformation or required subject result, or removing it changes a named assurance or recoverability condition on which the declared use relies.

Passing one branch means only that the requirement is not ceremonial for this use and horizon. It does not establish authorization, sufficiency, completion, optimality, minimum cost, safety, legal permission, or precedence.

#### A.11.OP:4.1 - Name the use and nearest substantive horizon

1. Name the proposed requirement and the declared use for which mandatory status is being considered.
2. End the horizon at the nearest named substantive decision, receiving use, selected transformation result, assurance use, or recovery use that can justify the requirement.
3. Name the possible result or removal consequence that reaches that horizon. Do not use the requirement's own status, completion flag, receipt, or other administrative transition as its receiver.

The nearest substantive horizon is not necessarily the next event. It may include a later decision when the dependency from the present result to that decision is stated. It does not extend through an unnamed audit, unspecified future reuse, a merely possible receiver, or an indefinite claim that the action may be useful someday.

#### A.11.OP:4.2 - Compare keeping and removing through three branches

| Admission branch | Passing condition | What the branch does not establish |
| --- | --- | --- |
| **Decision-changing result** | At least one materially plausible result changes `continue`, `repair`, `stop`, `reopen`, selection among named alternatives, or another named subject branch inside the horizon. Information can pass when it changes a later policy even if the immediate action stays the same. | It does not prove that the result will occur, choose the eventual branch, or make information valuable without a receiving decision. |
| **Selected realization** | The action performs a required part of an already selected transformation or obtains the required subject result. A deterministic step does not need fabricated rival outcomes. | It does not select or authorize the transformation, identify actual Work, or prove completion, delivery, acceptance, or value. |
| **Assurance or recoverability preservation** | Removing the action changes a named evidence, exposure, option-preservation, restart, rollback, or recovery condition on which the declared use relies. | It does not set the assurance floor, create reliance, or let a precautionary label substitute for direct evidence and assurance patterns. |

Compare the concrete situation with and without the requirement. If one branch passes, retain the requirement at no more formality than its direct owner and named reliance need justify. If several forms pass, return their comparison to the direct choice, apparatus, architecture, or Method Engineering owner rather than inventing one scalar minimum.

If no branch passes, remove the requirement or leave it as an optional convenience. Do not preserve mandatory status merely because the action is cheap, familiar, automated, prestigious, measurable, or already present.

#### A.11.OP:4.3 - Judge material plausibility through the subject claim

*Materially plausible* means more than logical possibility and less than certainty. The applicable subject, evidence, causal, risk, decision, or assurance pattern supplies the basis appropriate to the consequence. A low-probability result can remain material when its consequence changes exposure or the admissible policy. A large information volume is not material unless some result can change a named receiving use.

When the basis needed to distinguish branches is absent, return the missing basis or run a bounded experiment whose possible results can genuinely change the named decision. Do not convert uncertainty about usefulness into a permanent mandatory requirement.

#### A.11.OP:4.4 - Return authority and claims to their direct owners

Apply this screen inside the space left by current authority. Law and regulation, `E.5` Guard-Rails, `B.3` assurance floors, and a direct evidence, gate, duty, or safety pattern remain controlling. If their basis or applicability is disputed, return to that authority; do not use operational parsimony as an appeal court.

A passing result also leaves downstream claims separate:

- `A.3.1` and `A.3.2` establish Method and MethodDescription identity;
- `A.15.1` establishes dated Work, while `A.15.7` selects a next action during ongoing Work;
- `C.11`, `C.19.2`, `A.19`, and Method Engineering compare qualifying alternatives under their own conditions;
- `A.10`, `B.3`, and the applicable gate or duty pattern establish evidence, assurance, acceptance, and authority claims; and
- `E.13` repairs proxy displacement, while `E.23` governs operations inside a repeated evaluated improvement loop.

The admission result supplies none of those conclusions by itself.

#### A.11.OP:4.5 - Keep the result light and reopenable

For ordinary use, say:

> Keep `<requirement>` for `<declared use>` until `<nearest substantive horizon>` because `<named branch and receiving difference>`.

or:

> Remove or demote `<requirement>` for `<declared use>` because keeping and removing it produce the same substantive decision and result and change no relied-on assurance or recovery condition.

Create a durable claim-bearing episteme only when a named later use must cite, compare, audit, or rely on the disposition. Use an existing record kind appropriate to that use. Do not mint an `OperationalParsimonyRecord` or require a checklist merely to show that this pattern was consulted.

Reopen the disposition when the horizon, plausible results, selected transformation, direct duty, assurance floor, recovery reliance, or burden-bearing alternative changes.

#### A.11.OP:4.6 - Keep framework layers distinct

FPF owns this cross-domain admission principle. A Method Engineering DPF may use it when designing requirements, architecture, support, trials, or practical-worth comparisons for a named Method situation; that DPF still owns those Method-specific decisions. A local practice framework may bind the principle to its own execution and assurance mechanisms; those local mechanisms neither become FPF law nor prove that the general admission condition holds.

