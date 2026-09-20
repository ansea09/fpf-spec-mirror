---
chunk_kind: "child"
pattern_id: "B.1.5.RS"
pattern_title: "Replace a Constituent Method in Its Encompassing Uses"
section_id: "B.1.5.RS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5.RS/B.1.5.RS__005_solution.md"
commit_sha: "685a0d04e8c8b8c3ac0a571d72be15daf004c72f"
heading_path:
  - "B.1.5.RS — Replace a Constituent Method in Its Encompassing Uses"
  - "B.1.5.RS:4 — Solution"
line_start: 39485
line_end: 39539
dependencies:
  - "A.3.1"
  - "B.1.5"
  - "B.1.5.EW"
  - "B.1.5.RS"
  - "C.11.DUA"
  - "C.29"
keywords:
---

### B.1.5.RS:4 - Solution

Compare the candidate against what the encompassing work needs, then carry the changed contribution through that work. State the direction and conditions of the result.

#### B.1.5.RS:4.1 - Name the proposed change

Identify the current constituent, its candidate replacement and the gain: for example, reduced delay, effort or dependence on a scarce specialist. State what changes in the operation, its inputs, outputs, interactions or realization.

Keep a proposed replacement separate from one already performed. Use A.3.1 to settle any needed identity claim: exposing a hidden step, changing an implementation within an admitted variation and proposing another Method need not have the same answer.

#### B.1.5.RS:4.2 - Recover the receiving wholes

Identify the encompassing Methods or work arrangements whose use can change. Follow an indirect use through the intermediate whole while it affects the decision. Include a second receiving use when the constituent is shared; local success in the first use is not evidence for the second.

This is a search bounded by the intended replacement. If the actual users cannot be recovered, restrict adoption to the known uses or return the missing use information that prevents a broader decision. Do not require an inventory of all imaginable uses.

For each relevant whole, recover:

- what it supplies or assumes at the constituent's entry;
- what result or interaction it needs from the constituent;
- timing, ordering, coordination and resource conditions that affect this use;
- what variation or loss it can tolerate.

Plain statements are sufficient when they make the comparison executable. Use an existing interface or formal contract when it already states these conditions.

#### B.1.5.RS:4.3 - Compare the contribution under those conditions

Apply the proposed constituent to the receiving conditions. Follow what it supplies through the affected part of the whole, including an interaction before final output when the whole relies on it.

Choose an argument, available observations, calculation or trial that can discriminate the decision at proportionate cost. A known violation can reject a general replacement without testing every possible input. A successful example can reveal a usable construction but does not automatically support all inputs.

When an approximation is proposed, state the property preserved for the receiving use: a bound, ordering, feasible action, specified error or other needed consequence. Equal rounded answers on one example do not establish preservation of a different property.

If the same implementation must serve several wholes simultaneously, examine their joint demands. Separate success under incompatible settings is not one shared implementation. Compare retained variants or changed coordination where that is useful.

#### B.1.5.RS:4.4 - Classify the replacement by use

| Comparison result | What can follow |
| --- | --- |
| The needed contribution and conditions are preserved. | Adopt the replacement for that use at the supported scope. |
| Preservation holds only under a narrower condition. | Restrict use to that condition and retain a suitable alternative elsewhere. |
| An adapter or changed combination can restore the needed contribution. | Treat that adaptation as part of the candidate and check its full burden and behavior. |
| A required contribution is lost. | Reject the replacement for that whole, change the requirement through the relevant decision, or choose another candidate. |
| Information does not distinguish compatibility from failure. | Keep the uncertainty bounded and obtain more only if it can change a worthwhile next action. |

This is a directed conclusion. Replacing A by B in one use does not show that A can replace B, that they are the same Method, or that B is preferable in all uses.

#### B.1.5.RS:4.5 - Adopt or retain alternatives

Choose at the supported scope, accounting for adaptation, learning, operation and maintenance costs. Retain separate variants when their different strengths justify the burden; a single universal replacement is not required.

For an ongoing operation, use its ordinary rules for introducing change and retaining continuity. State the condition that would require reconsideration: changed inputs, another receiving whole, a tighter timing limit, lost support or a newly relevant result property. No separate certificate or trial is required merely to record that an existing basis was sufficient.

Return the decision in the form its receiver needs. Where the conclusion is only recognition of a plausible substitute, say so. A claim of guaranteed preservation needs the argument or assurance appropriate to that claim under B.3; a local decision under uncertainty uses C.11 and C.11.DUA.

