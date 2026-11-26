---
chunk_kind: "child"
pattern_id: "B.3.4"
pattern_title: "Can Earlier Evidence Still Support This Use? — Evidence Decay and Epistemic Debt"
section_id: "B.3.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.4/B.3.4__005_solution.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "B.3.4 — Can Earlier Evidence Still Support This Use? — Evidence Decay and Epistemic Debt"
  - "B.3.4:4 — Solution"
line_start: 47365
line_end: 47436
dependencies:
  - "A.10"
  - "B.3"
  - "C.11"
  - "C.19.2"
  - "C.27.TA"
  - "G.11"
keywords:
---

### B.3.4:4 - Solution

Qualify currentness at the claim and receiving use. Reconsider only the dependency reach for which a changed premise or an applicable review rule can alter the conclusion.

#### B.3.4:4.1 - Locate the condition that can change reliance

Identify the earlier result being used and the relevant conditions: for example, its configuration, operating envelope, measurement qualification or dependency. Establish whether available information still supports those conditions. An unchanged file is not proof that its environment is unchanged; an older file is not proof that its support has failed.

Use time-based review when a deterioration model or review policy warrants it. Use event-, dependency- or condition-based reconsideration when those define applicability. A newly discovered failure mode may reopen a result before a review date. A calendar reminder may instead find that the result remains applicable without a new experiment.

To design reconsideration, work back from the decision that could become unsound. Keep a component and its inspection result fixed and change the way the assembly uses it. If the earlier conclusion can now fail, identify an observable change in the assembly, its use or the support on which the argument relies. Choose who can detect it, how soon it must be detected and what the recipient can do by that time. When a condition can change between inspections, use a warranted bound on that change, a timely event signal or a suitably restricted use. A dated observation of the whole can settle a decision confined to its state on that date.

Keep three judgements distinct: whether the earlier evidence applies, whether it is sufficient for the present claim, and whether the proposed action satisfies its conditions. Currentness alone answers neither sufficiency nor permission.

#### B.3.4:4.2 - State what each date bounds

A `valid_until: ISO-8601-date | null` field is used only when the receiving claim or applicable rule has a calendar boundary to convey. State what the date bounds. A review-due date requests reconsideration; a qualification, right or resource-use end date can terminate an allowed use. Do not merge these meanings into a global expiry of the carrier.

An absent or `null` date means that this field supplies no calendar boundary. It asserts neither perpetual validity nor invalidity and creates no mandatory justification for a missing date. Applicable event or condition limits govern the use.

For a retrospective question, locate the change and the time it was discovered separately. A later inspection may show that the condition had already changed by a given date while leaving its first change time open. It can settle a question about the earlier state if that bound suffices. To establish what supported a decision at the time, identify the information then available and, where actual reliance is claimed, what the decision maker used.

Where a required review period applies, follow it until it is changed by someone with the necessary authority. Evaluate its protective purpose, threshold basis and displaced cost separately when deciding whether to propose that change. Questioning the policy is not permission to ignore it.

#### B.3.4:4.3 - Treat epistemic debt as an optional planning indicator

A team may call its outstanding evidence-review or maintenance obligations **epistemic debt (ED)**. If it needs a number, define the counted entities, dependency treatment, scale and applicable unit, policy purpose, and meaning of any action threshold. An `epistemic_debt_budget` is then a planning-policy limit, not a universal allowance of harm.

For example, a team may count overdue review obligations to plan assessor capacity. Ten duplicate paths to one obligation do not create ten obligations. Separate obligations consuming the same source may require different judgements for different uses. For a staffing decision, recover the work remaining, its due windows and the people able to do it. A single inspection may supply both uses. Distinct mandatory inspections sharing an assessor can compete for the same time even when each fits on its own. A count suffices when the question asks only how many obligations are overdue.

Elapsed days can contribute to a justified priority rule or deterioration model. B.3.4 supplies no default rate, sum or automatic level downgrade. A planning count is not a probability of failure, and zero overdue reviews does not establish an adequate assurance case.

#### B.3.4:4.4 - Choose the feasible response to the change

Determine which continuation the available support and applicable rules permit. Choose the response that addresses the change:

| Response | When useful | Result for the receiving use |
| --- | --- | --- |
| Continue on applicable support | Available information is sufficient for the unchanged bounded use. A scoped reconsideration, if needed, has found no relevant loss. | Retain the qualified result. No new experiment, waiver or separate no-refresh record is required merely to continue. |
| Narrow or restrict the use | Support remains sufficient for a smaller envelope or less demanding claim. | State the usable boundary and the limitation that changes the recipient's action. |
| Refresh or inspect | An obtainable check can resolve a material uncertainty or fulfil a binding review requirement. | Choose that check with regard to what its result can change, its cost, delay and displaced work; assess its result if the check is performed. |
| Suspend reliance or deprecate the affected result | The necessary support is absent or defeated and no permitted continuation carries the requested use. | Remove or qualify that reliance and communicate the affected reach. A status downgrade does not accept the underlying harm. |
| Apply an authorized exception | An applicable rule permits a bounded exception and a competent authority can grant it for this case. | Follow the mandate, scope, conditions and accountability. A senior title alone grants no authority over affected risk bearers. |

C.11 and C.19.2 support the choice of worthwhile additional evidence. An existing result may already establish the required condition for this use. A design commission can finish with the justified trigger, observation and response. A separately required inspection calls for the agreed work or evidence that the required inspection has taken place. If it cannot be performed in time, identify the unfulfilled requirement and any warranted action still available.

For an immediate unchanged use, stop with its usable result. When a later receiver needs a warning, limitation or retained reason to avoid unsupported reliance, keep that minimum content with the existing result or publication. A separate `DeprecationNotice` is useful when something is deprecated, not as proof that refresh was skipped.

#### B.3.4:4.5 - Follow affected dependencies and preserve expiry

Trace a changed premise to the conclusions whose argument uses it. Identify the subject, operating conditions and time each such conclusion covers. A lost premise can defeat one argument while another sufficient argument remains available. A shared premise can undermine several apparently independent judgements. Where the recipient needs them together, reconsider their fit for the same use, including a possible loss of compatibility while each separate result still holds. Reuse the branches whose grounds remain adequate.

Keep physical and institutional conditions intact. Expired calibration qualification, an unavailable configuration, ended resource support or an elapsed rights window can block the corresponding use even when the old report remains an accurate record of an earlier state. A justified deterioration model can make elapsed time material; cite that model rather than inferring universal decay.

A dashboard should distinguish a review due, a defeated premise and a restricted use. Its colour reports the declared indicator or disposition; that report alone does not establish the underlying claim. A failing test is a potentially relevant adverse result to assess now, not merely another overdue date.

#### B.3.4:4.6 - Worked cases: the same age, different decisions

**Bridge.** An earlier structural assessment supports a specified load envelope, conditional on its stated condition and inspection regime. For an unchanged limited use, available load and condition information and satisfied required inspections can preserve that support. The assessment's age alone adds no repeat assessment.

In the paired case, proposed traffic exceeds the assessed envelope. The earlier report alone leaves support for that traffic open. Check for another applicable assessment or a sufficient bound. If none decides the question, restrict the supported use or obtain the assessment the proposed load requires. Evidence that a proposed load is unsafe can settle a refusal.

Suppose the available inspection team can either inspect a suspected load-bearing defect or repeat an adequate check whose relevant conditions remain established. Examine the protected harm and the basis of the inspection requirement, what each result could change, and the cost of delay. Where the defect inspection can prevent that harm and the repeat adds no useful information, preserve the inspection capacity.

If a binding repeat requirement constrains that choice, account for it in the plan. When the commission or an applicable duty includes seeking a change, take the resource conflict to the authority that can amend the requirement.

A commission to set the review policy starts a step earlier. Identify which changes in load, structural condition or inspection access could affect each promised use. A change reported after a crossing may help reconstruct that crossing. A policy intended to prevent an unsupported crossing needs an effective response before entry. An existing load limit enforced at entry may already handle excess traffic. If the response depends on an operator, establish that the warning can reach the operator in time for a feasible action. A change in structural condition can require a different signal.

**Library.** The verified property of an unchanged library in its qualified configuration remains supported when the relevant assumptions and dependencies still hold. A new vulnerability affecting a dependency used by the security claim reopens that claim even before a review date. An unrelated vulnerability does not. Preserve unaffected functional results and any independently supported restricted service while addressing the security limitation.

A release recipient who would otherwise assume the affected security property needs that limitation in the released result.

