---
chunk_kind: "child"
pattern_id: "B.1.5.RS"
pattern_title: "Evaluate a Method Replacement in Its Encompassing Uses"
section_id: "B.1.5.RS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.5.RS/B.1.5.RS__005_solution.md"
commit_sha: "a9845e2c1029313e518c91a459ff7fab39e2831e"
heading_path:
  - "B.1.5.RS — Evaluate a Method Replacement in Its Encompassing Uses"
  - "B.1.5.RS:4 — Solution"
line_start: 44571
line_end: 44625
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

Identify the constituent, its candidate replacement and the gain: for example, reduced delay, effort or dependence on a scarce specialist. State what changes in the operation, its inputs, outputs, interactions or realization.

Keep a proposed replacement separate from one already performed. Use A.3.1 to settle any needed identity claim: exposing a hidden step, changing an implementation within an admitted variation and proposing another Method need not have the same answer.

#### B.1.5.RS:4.2 - Recover the receiving wholes

Follow the proposed change to each receiving use covered by the decision. An indirect use can matter even if an intermediate whole returns the same value, for instance when its timing or explanation changes. For a change restricted to one use, establish any consequences for others through resources, commitments or interfaces shared with it. For a wider adoption claim, establish which uses are covered and why the argument applies throughout that scope.

Bound the search by the proposed adoption and its conditions. An interface rule that guarantees every required contribution can cover a class of unnamed users. If an uncovered use could alter the decision, restrict the adoption to the supported scope or obtain the missing condition.

For each whole, recover:

- what it supplies or assumes at the constituent's entry;
- what result or interaction it needs from the constituent;
- timing, ordering, coordination and resource conditions that affect this use;
- what variation or loss it can tolerate.

Plain statements are sufficient when they make the comparison executable. Use an existing interface or formal contract when it already states these conditions.

#### B.1.5.RS:4.3 - Compare the contribution under those conditions

Apply the proposed constituent to the receiving conditions. Follow what it supplies through the affected part of the whole, including an interaction before final output when the whole relies on it.

Choose an argument, available observations, calculation or trial that can discriminate the decision at proportionate cost. A known violation can reject a general replacement without testing every input. A successful example can reveal a usable construction but does not automatically support all inputs.

When an approximation is proposed, state the property preserved for the receiving use: a bound, ordering, feasible action, specified error or other needed consequence. Equal rounded answers on one example do not establish preservation of a different property.

When one replacement must support several uses, follow their permitted combinations over the relevant period. Two uses can exhaust the same finite supply even in succession. A single configuration may work for all of them, or a choice by the authorized participant may depend on information available before the commitment. Establish that the proposed arrangement meets the shared and individual requirements under those conditions. If only one specified use is commissioned, test the dependencies needed for that use.

#### B.1.5.RS:4.4 - Classify the replacement by use

| Comparison result | What can follow |
| --- | --- |
| The needed contribution and conditions are preserved. | Report that the replacement is compatible with that use under the established conditions. |
| Preservation holds only under a narrower condition. | Identify the condition of compatibility and the uses requiring another solution. |
| An adapter or changed combination can restore the needed contribution. | Treat that adaptation as part of the candidate and check its burden and behavior. |
| A required contribution is lost. | Reject the replacement for that whole, change the requirement through the relevant decision, or choose another candidate. |
| Information does not distinguish compatibility from failure. | State what the supplied evidence establishes and which condition would decide compatibility. Seek further evidence when the decision warrants that inquiry or when obtaining the evidence is itself commissioned. |

This is a directed conclusion. Replacing A by B in one use does not show that A can replace B, that they are the same Method, or that B is preferable in all uses.

#### B.1.5.RS:4.5 - Adopt or retain alternatives

If you are commissioned to recommend or choose an alternative, compare the compatible options at the supported scope, including adaptation, learning, operation and maintenance costs. Separate variants can be worthwhile when their different strengths justify their cost. The person with authority over adoption decides whether and when to introduce the chosen replacement.

For an ongoing operation, use its ordinary rules for introducing change and retaining continuity. State the condition that would require reconsideration: changed inputs, another receiving whole, a tighter timing limit, lost support or a newly relevant result property.

Return the decision in the form its receiver needs. Where the conclusion is only recognition of a plausible substitute, say so. A claim of guaranteed preservation needs an argument appropriate to that claim. Use B.3 when a named assurance claim about its support is current; a local decision under uncertainty uses C.11 and C.11.DUA.

