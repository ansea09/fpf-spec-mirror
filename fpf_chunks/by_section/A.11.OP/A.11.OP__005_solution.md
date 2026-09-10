---
chunk_kind: "child"
pattern_id: "A.11.OP"
pattern_title: "Decision-Relevant Least Action and Operational Parsimony"
section_id: "A.11.OP:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.11.OP/A.11.OP__005_solution.md"
commit_sha: "ce6fcc3b99b10e42f4b258f84091355b2ee5ab24"
heading_path:
  - "A.11.OP — Decision-Relevant Least Action and Operational Parsimony"
  - "A.11.OP:4 — Solution"
line_start: 23636
line_end: 23699
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
  - "C.11.DUA"
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

Passing one branch establishes only a substantive contribution for this use and horizon. It does not establish that the work can be obtained or is worth requiring. Complete any live worth or choice question through its direct owner before selecting the requirement.

#### A.11.OP:4.1 - Name the use and nearest substantive horizon

1. Name the proposed requirement and the declared use for which mandatory status is being considered.
2. End the horizon at the nearest named substantive decision, receiving use, selected transformation result, assurance use, or recovery use that can justify the requirement.
3. Name the possible result or removal consequence that reaches that horizon. Do not use the requirement's own status, completion flag, receipt, or other administrative transition as its receiver.

The nearest substantive horizon is not necessarily the next event. It may include a later decision when the dependency from the present result to that decision is stated. End it before any further use whose receiver and dependency have not been named.

#### A.11.OP:4.2 - Compare keeping and removing through three branches

| Admission branch | Passing condition | Boundary of the result |
| --- | --- | --- |
| **Decision-changing result** | At least one materially plausible result changes a named subject branch or selection among named alternatives inside the horizon. An information-gathering action passes when one of its possible results changes a later policy even if the immediate action stays the same. | The passing basis is the result-to-decision dependency. Obtainability, expected contribution after uncertainty, burden and eventual choice remain open. |
| **Selected realization** | The action performs a required part of an already selected transformation or obtains the required subject result. A deterministic step needs no fabricated rival outcomes. | This branch establishes the action's contribution to the selected result; it presupposes selection and leaves feasibility, authorization, actual Work, and result status to their direct owners. |
| **Assurance or recoverability preservation** | Removing the action changes a named assurance or recoverability condition on which the declared use relies. | This branch preserves that condition; its required level and evidential basis come from the direct assurance or recovery owner. |

Compare the concrete situation with and without the requirement. A passing branch removes the objection that the work contributes nothing. Retain it only as far as its direct basis justifies requiring it. An already selected transformation or established reliance can supply that basis without another comparison.

When a proposed inquiry could matter but its worth remains open, apply `C.11.DUA` to the actual demand and receiving question. Identify the attainable observation, what it could change, and its whole cost within the receiving horizon. Compare available continuations through `C.11` when a local choice is needed. A useful possible result can still arrive too late, require unavailable means, or cost more than its contribution. Keep the presently supported answer or select a feasible alternative under its actual limits. Do not invent an OptionSet or an inquiry merely to certify that none is needed.

If no branch passes, remove the requirement or leave it as an optional convenience. Convenience and prior investment do not supply the missing receiving difference.

#### A.11.OP:4.3 - Judge material plausibility through the subject claim

*Materially plausible* means more than logical possibility and less than certainty. The direct owner of the claimed consequence supplies its standard of evidence. A low-probability result can remain material when its consequence changes exposure or the admissible policy. A large information volume is material only when some possible result changes a named receiving use.

When the branches cannot be distinguished, name the exact claim and missing basis and return them to that claim's direct owner. Keep the qualified answer already supported. A bounded experiment is one possible continuation only when an attainable result and worthwhile contribution justify its whole burden under §4.2. Unresolved usefulness alone does not select an experiment or create permanent mandatory status.

#### A.11.OP:4.4 - Return authority and claims to their direct owners

Apply this screen only inside the space left by every applicable direct authority. The direct owner establishes the obligation or floor and resolves disputes about its basis or applicability.

When the requirement itself is being appraised, use `C.11.DUA` to compare the protected bearer and interest, the threshold and horizon, the causal contribution claimed, and who bears the burden. Identify who can amend the requirement and whether that amendment is feasible in time. Keep its merits and present force distinct: neither a protective label nor a burdensome rule settles the merits, and an unfavorable appraisal supplies no unilateral waiver. The legal, ethical and domain claims remain with their direct owners.

A passing branch establishes only the named contribution. Every downstream claim remains with the direct pattern named in Relations; obtain the required result by value instead of treating this screen as its substitute.

#### A.11.OP:4.5 - Keep the result light and reopenable

For ordinary use, say:

> Keep `<requirement>` for `<declared use>` until `<nearest substantive horizon>` because `<named contribution and the basis for requiring this work>`.

or:

> Remove or demote `<requirement>` for `<declared use>` because keeping and removing it produce the same substantive decision and result and change no relied-on assurance or recovery condition.

If a proposed inquiry has a contribution but is unavailable or not worthwhile, finish with the current supported answer and selected continuation. Keep a short reason or limitation in that result when the recipient needs it; add no empty probe fields or separate omission account.

A named later use that must cite, compare, audit, or rely on the disposition records it in the existing record kind appropriate to that use. Otherwise the one-sentence result is complete.

Reopen the disposition when the horizon, plausible results, selected transformation, direct duty, assurance floor, recovery reliance, or burden-bearing alternative changes.

#### A.11.OP:4.6 - Keep framework layers distinct

FPF owns this cross-domain admission principle. A Method Engineering DPF may use it when deciding which requirements should be mandatory in a named Method situation; that DPF still owns the Method-specific design. A local practice framework may bind the principle to its own execution and assurance mechanisms. Those mechanisms retain local scope, and the FPF admission condition must still be established for the declared use.

