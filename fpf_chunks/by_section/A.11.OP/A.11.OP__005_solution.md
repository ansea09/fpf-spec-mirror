---
chunk_kind: "child"
pattern_id: "A.11.OP"
pattern_title: "Decision-Relevant Least Action and Operational Parsimony"
section_id: "A.11.OP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.11.OP/A.11.OP__005_solution.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "A.11.OP — Decision-Relevant Least Action and Operational Parsimony"
  - "A.11.OP:4 — Solution"
line_start: 23601
line_end: 23658
dependencies:
  - "A.10"
  - "A.11"
  - "A.11.OP"
  - "A.15.1"
  - "A.15.7"
  - "A.19"
  - "A.3.1"
  - "A.3.2"
  - "B.3"
  - "C.11"
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

Passing one branch establishes only that the requirement is non-ceremonial for this use and horizon. Every stronger claim remains with its direct owner.

#### A.11.OP:4.1 - Name the use and nearest substantive horizon

1. Name the proposed requirement and the declared use for which mandatory status is being considered.
2. End the horizon at the nearest named substantive decision, receiving use, selected transformation result, assurance use, or recovery use that can justify the requirement.
3. Name the possible result or removal consequence that reaches that horizon. Do not use the requirement's own status, completion flag, receipt, or other administrative transition as its receiver.

The nearest substantive horizon is not necessarily the next event. It may include a later decision when the dependency from the present result to that decision is stated. End it before any further use whose receiver and dependency have not been named.

#### A.11.OP:4.2 - Compare keeping and removing through three branches

| Admission branch | Passing condition | Boundary of the result |
| --- | --- | --- |
| **Decision-changing result** | At least one materially plausible result changes a named subject branch or selection among named alternatives inside the horizon. An information-gathering action passes when one of its possible results changes a later policy even if the immediate action stays the same. | The passing basis is the result-to-decision dependency; likelihood and the eventual branch remain open. |
| **Selected realization** | The action performs a required part of an already selected transformation or obtains the required subject result. A deterministic step needs no fabricated rival outcomes. | This branch admits only the realizing action; it presupposes selection and leaves authorization, actual Work, and result status to their direct owners. |
| **Assurance or recoverability preservation** | Removing the action changes a named assurance or recoverability condition on which the declared use relies. | This branch preserves that condition; its required level and evidential basis come from the direct assurance or recovery owner. |

Compare the concrete situation with and without the requirement. If one branch passes, retain the requirement at no more formality than its direct owner and named reliance need justify. If several proposed actions or apparatus configurations pass, return their comparison to the pattern that directly governs those alternatives.

If no branch passes, remove the requirement or leave it as an optional convenience. Convenience and prior investment do not supply the missing receiving difference.

#### A.11.OP:4.3 - Judge material plausibility through the subject claim

*Materially plausible* means more than logical possibility and less than certainty. The direct owner of the claimed consequence supplies its standard of evidence. A low-probability result can remain material when its consequence changes exposure or the admissible policy. A large information volume is material only when some possible result changes a named receiving use.

When the branches cannot be distinguished, name the exact claim and missing basis and return them to that claim's direct owner. Alternatively, run a bounded experiment whose possible results can genuinely change the named decision. Unresolved usefulness does not create permanent mandatory status.

#### A.11.OP:4.4 - Return authority and claims to their direct owners

Apply this screen only inside the space left by every applicable direct authority. The direct owner establishes the obligation or floor and resolves disputes about its basis or applicability.

A passing branch establishes only that the requirement is non-ceremonial for the named use and horizon. Every downstream claim remains with the direct pattern named in Relations; obtain that result by value instead of treating this admission as its substitute.

#### A.11.OP:4.5 - Keep the result light and reopenable

For ordinary use, say:

> Keep `<requirement>` for `<declared use>` until `<nearest substantive horizon>` because `<named branch and receiving difference>`.

or:

> Remove or demote `<requirement>` for `<declared use>` because keeping and removing it produce the same substantive decision and result and change no relied-on assurance or recovery condition.

A named later use that must cite, compare, audit, or rely on the disposition records it in the existing record kind appropriate to that use. Otherwise the one-sentence result is complete.

Reopen the disposition when the horizon, plausible results, selected transformation, direct duty, assurance floor, recovery reliance, or burden-bearing alternative changes.

#### A.11.OP:4.6 - Keep framework layers distinct

FPF owns this cross-domain admission principle. A Method Engineering DPF may use it when deciding which requirements should be mandatory in a named Method situation; that DPF still owns the Method-specific design. A local practice framework may bind the principle to its own execution and assurance mechanisms. Those mechanisms retain local scope, and the FPF admission condition must still be established for the declared use.

