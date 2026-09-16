---
chunk_kind: "child"
pattern_id: "A.1.RI"
pattern_title: "Reidentifying an Object across Observations"
section_id: "A.1.RI:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.RI/A.1.RI__005_solution.md"
commit_sha: "8581bcf6502498b53aaa9fd42ed925a1371c08d1"
heading_path:
  - "A.1.RI — Reidentifying an Object across Observations"
  - "A.1.RI:4 — Solution"
line_start: 2015
line_end: 2075
dependencies:
  - "A.1"
  - "A.3.3.PI"
  - "A.3.3.TR"
  - "B.5.RR"
  - "B.5.TC"
  - "B.5.TU"
  - "C.11.DUA"
  - "C.16.IR"
  - "C.16.MR"
  - "C.2.1"
keywords:
---

### A.1.RI:4 - Solution

Recover the continuation question, construct the relevant associations under the subject rules, test their joint compatibility and use the distinctions they actually support.

**Name the continuing object → recover observations and rules → construct competing connections → test them together → resolve what the use needs → continue or reopen.**

#### A.1.RI:4.1 - Recover the continuation question

State which object the observations may concern and what would count as its continuation through the interval or change. A continuing software service, one process run and one execution of a requested job have different boundaries. Choose the object required by the question.

Recover the relevant temporal and contextual scope. Coordinates need a frame; a local process number needs the system and naming scope in which it was issued. If the observations use different references, establish their correspondence before comparing values.

State the receiving use. Estimating one object's displacement needs its association across observations. Estimating the mean position of a fixed observed population can leave those associations unresolved.

#### A.1.RI:4.2 - Separate observations, rules and assumptions

Recover the observations already available, their occasions and the limitations that matter to this question. Distinguish the observed indication from a position, identity or event inferred through it. C.16.MR and C.16.IR help when the measurement interpretation itself remains unresolved.

Recover the subject rules used to connect those observations: allowed changes, motion bounds, lifecycle events or other continuity conditions. Include the observation conditions needed by the connection. “Each object was observed once” and “the set of objects stayed fixed” are substantive premises when they make the association one-to-one.

Keep an assumed rule available as an assumption. A conclusion derived under it can be useful while a later question requires a different or better-supported account. Use the assurance and information work appropriate to that receiving question.

#### A.1.RI:4.3 - Construct the materially different connections

Construct the associations still possible under the available account. A connection states which observations concern the continuing object and how the subject rules permit the intervening change. In a small finite case, listing the alternatives can be enough. Larger cases can use the domain's assignment, constraint or probabilistic Methods.

Include a missed observation, new object, ended object or reused identifier when the observed situation and subject rules make that alternative live. For example, a process can terminate between reports and its number can later be reused. A fixed two-object motion exercise can instead supply persistence and complete detection as premises.

When several objects share observations, construct complete associations for the relevant group. Retain the conditions linking their choices. For independent point motions a pair of admissible paths may suffice; interacting bodies can require a joint evolution satisfying their interactions.

#### A.1.RI:4.4 - Test compatibility and the strength of the conclusion

Apply the subject constraints to each materially different connection. Construct a permitted realization where feasibility matters, or identify a violated condition that excludes it. A numerical solver can help perform this step; its returned result still needs the intended observation and subject interpretation.

Compare the surviving alternatives at the distinction required by the receiving use:

- When the supported premises and considered alternatives determine the association, use that conditional identification.
- When they exclude a proposed association, remove it from the current account.
- When materially different associations remain, retain the unresolved distinction.
- When none fits, inspect the failed observation, rule or assumption before extending the same account.

A best score answers the ranking question defined by that score. If the work uses the top-ranked association provisionally, carry its selection rule and relevant uncertainty into that use. Claiming that the observations uniquely determine it requires the corresponding exclusion of alternatives.

The strength of the identifying judgment changes with its basis.

#### A.1.RI:4.5 - Resolve only the distinction the next use needs

Try the receiving calculation or decision on the surviving alternatives. If each gives the needed result, continue with that result and leave the unused identity question open. Section :5.1 obtains the same mean position under both surviving associations.

If the difference changes the next action, determine which available fact, observation or subject constraint would distinguish the alternatives. Prefer an already available discriminator. Obtain more information when its likely contribution warrants its cost and delay; C.11.DUA supplies that choice.

Some work permits a provisional action with the unresolved risk. State what that action assumes and what observation would call for correction. Work that requires the identity to be settled must return to the missing identifying contribution. An unresolved identification need not stop other work whose result is unaffected.

#### A.1.RI:4.6 - Carry the result into use and revise it locally

Use the association to join the relevant observations, calculate the change or address the continuing object. Keep the premises and unresolved alternatives that can change that use.

Reopen the affected connection when a new observation, changed rule or detected observation error invalidates it. Preserve associations and calculations whose basis still holds. B.5.RR helps carry a changed premise through dependent reasoning.

The observations retain their own occasions and claims after their subject is identified. C.2.1 governs observation epistemes and their identities. For a use that needs a separately designated relation occurrence, apply A.6.REL using the direct relation pattern's predicate and occurrence-identity rule.

