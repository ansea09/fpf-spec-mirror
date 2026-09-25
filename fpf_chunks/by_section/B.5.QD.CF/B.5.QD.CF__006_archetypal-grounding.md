---
chunk_kind: "child"
pattern_id: "B.5.QD.CF"
pattern_title: "Reformulate a Problem by Examining Its Conflicting Assumptions"
section_id: "B.5.QD.CF:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.QD.CF/B.5.QD.CF__006_archetypal-grounding.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "B.5.QD.CF — Reformulate a Problem by Examining Its Conflicting Assumptions"
  - "B.5.QD.CF:5 — Archetypal Grounding"
line_start: 45904
line_end: 45945
dependencies:
  - "B.1.5.EW"
  - "B.5.FM"
  - "B.5.QD"
  - "B.5.RA"
  - "B.5.TC"
  - "C.11.DUA"
  - "C.40.CD"
keywords:
---

### B.5.QD.CF:5 - Archetypal Grounding

The following constructed cases supply the conditions needed for their reasoning. They demonstrate different reformulations and a case in which the original demand remains impossible.

#### B.5.QD.CF:5.1 - Distinguish operating conditions without inventing a machine

A proposed device has one fixed setting p. The task requires p to be at least 6 during work and at most 2 during quiet operation. In the proposed design, both requirements constrain the same fixed value; no such value exists.

Recover the extra premise: the setting is fixed across those operating conditions. Let p_work and p_quiet describe the two values. The account is:

- p_work ≥ 6;
- p_quiet ≤ 2;
- p_work = p_quiet.

Keeping the two requirements and reconsidering the equality produces a construction question: **Can the device select different settings in the two distinguishable conditions?** The values (6,2) satisfy the revised inequalities. They identify what a switching construction would have to supply.

That answer is conditional. The device must be able to recognize the condition and reach the required setting in time, using the resources permitted by the task. If a transition takes three seconds while the retained requirement allows one second, this proposed transition fails. A faster operation, another construction or an authorized requirement change is still needed.

If instead both inequalities concern the same operation at the same time, separating their names would misrepresent the task. The inequality 6 ≤ p ≤ 2 remains impossible. The useful result then identifies the requirements that cannot both be retained.

#### B.5.QD.CF:5.2 - Replace an assumed means while retaining two outcomes

A team must reproduce an earlier calculation and use new prices for new calculations. A current file stores the quantity 3 and the price 10, so the earlier result is 30. Tomorrow the price becomes 12 and the new result must be 36.

The proposed practice keeps only one mutable price value. Reproducing the earlier result is taken to require keeping that value at 10; obtaining the new result requires changing it to 12. The conflict depends on that proposed means of recovering the earlier input.

Ask instead: **What information and operation reproduce the earlier calculation without freezing the current price?** For this case, the calculation is quantity times price. Retaining the input pair (3,10), the multiplication rule and the identity of the earlier calculation supplies its result 30. The current pair (3,12) supplies 36. A versioned input or a retained calculation record can therefore replace the supposed need for one unchanged current value.

The scope matters. This construction suffices for the supplied arithmetic question. If the earlier result used a rounding rule, exchange rate or other input, that contribution must also remain recoverable. A claim about who approved the transaction asks another question and is not established by recomputing 30.

Now change the retained requirements: every copy of the earlier price must be destroyed, and no equivalent information may remain, but the system must later recover that price uniquely. The retained-input proposal violates the deletion requirement. The conflict has not been repaired under these new conditions. The next case isolates why this stronger combination can be impossible.

#### B.5.QD.CF:5.3 - Return an impossibility instead of hiding retained information

A device receives one bit x, either 0 or 1. Complete erasure in this formal task means that, afterward, its entire accessible state is the same s for both inputs; there is no external record or later input revealing x. A deterministic operation g must then recover the original bit for either input.

For the input 0, recovery requires g(s)=0. For the input 1, it requires g(s)=1. The same operation on the same state cannot satisfy both. The required erasure and universal recovery are incompatible under the supplied model.

An external copy or a different final state would allow other constructions, but each changes the complete-erasure condition. Renaming an external copy as a pointer preserves information rather than meeting that condition. Returning a default value changes the recovery requirement. Neither is a solution to the original task.

The result can already end the construction search under these premises. If the work instead permits a retained distinction, develop that changed question explicitly. A later physical implementation also has a physical model and its own scope; the argument here establishes the finite information constraint stated above.

