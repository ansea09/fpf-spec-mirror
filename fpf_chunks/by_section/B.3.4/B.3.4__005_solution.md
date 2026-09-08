---
chunk_kind: "child"
pattern_id: "B.3.4"
pattern_title: "Evidence Decay & Epistemic Debt"
section_id: "B.3.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.3.4/B.3.4__005_solution.md"
commit_sha: "2154d21570c891bd5ed30fd6e6136f17f1942cae"
heading_path:
  - "B.3.4 — Evidence Decay & Epistemic Debt"
  - "B.3.4:4 — Solution"
line_start: 39999
line_end: 40058
dependencies:
  - "A.10"
  - "B.3"
  - "C.11"
  - "C.19.2"
  - "C.27.TA"
  - "G.11"
keywords:
  - "age"
  - "changed premise"
  - "epistemic debt"
  - "evidence currentness"
  - "qualification window"
  - "refresh"
---

### B.3.4:4 - Solution

Qualify currentness at the claim and receiving use. Reconsider only the dependency reach for which a changed premise or an applicable review rule can alter the conclusion.

#### B.3.4:4.1 - Locate the condition that can change reliance

Identify the earlier result being used and the relevant conditions: for example, its configuration, operating envelope, measurement qualification or dependency. Establish whether available information still supports those conditions. An unchanged file is not proof that its environment is unchanged; an older file is not proof that its support has failed.

Use time-based review when an applicable deterioration model or review policy warrants it. Use event-, dependency- or condition-based reconsideration when those define applicability. A newly discovered failure mode may reopen a result before a review date. A calendar reminder may instead find that the result remains applicable without a new experiment.

Keep three judgements distinct: whether the earlier evidence applies, whether it is sufficient for the present claim, and whether the proposed action satisfies its actual conditions. Currentness alone answers neither sufficiency nor permission.

#### B.3.4:4.2 - Give dates their actual meaning

A `valid_until: ISO-8601-date | null` field is used only when the receiving claim or applicable rule has a calendar boundary to convey. State what the date bounds. A review-due date requests reconsideration; a qualification, right or resource-use end date can terminate an allowed use. Do not merge these meanings into a global expiry of the carrier.

An absent or `null` date means that this field supplies no calendar boundary. It asserts neither perpetual validity nor invalidity and creates no mandatory justification for a missing date. Applicable event or condition limits still govern the use.

Where a required review period applies, follow it until it is changed by someone with the necessary authority. Evaluate its protective purpose, threshold basis and displaced cost separately when deciding whether to propose that change. Questioning the policy is not permission to ignore it.

#### B.3.4:4.3 - Treat epistemic debt as an optional planning indicator

A team may call its outstanding evidence-review or maintenance obligations **epistemic debt (ED)**. If it needs a number, define the counted entities, dependency treatment, scale and unit, policy purpose, and meaning of the action threshold. An `epistemic_debt_budget` is then a named planning-policy limit, not a universal allowance of harm.

For example, a team may count distinct overdue review obligations to plan assessor capacity. Ten duplicate paths to one obligation do not create ten obligations. Separate obligations consuming the same source may still require different judgements for different uses.

Elapsed days can contribute to a justified priority rule or deterioration model. B.3.4 supplies no default rate, sum or automatic level downgrade. A planning count is not a probability of failure, and zero overdue reviews does not establish an adequate assurance case.

#### B.3.4:4.4 - Choose the feasible response to the actual change

Determine what the receiving use can support now. The following are possible responses, not a compulsory completion triad:

| Response | When useful | Result for the receiving use |
| --- | --- | --- |
| Continue on applicable support | Available information is sufficient for the unchanged bounded use. A scoped reconsideration, if needed, has found no relevant loss. | Retain the qualified result. No new experiment, waiver or separate no-refresh record is required merely to continue. |
| Narrow or restrict the use | Support remains sufficient for a smaller envelope or less demanding claim. | State the usable boundary and the limitation that changes the recipient's action. |
| Refresh or inspect | An obtainable check can resolve a material uncertainty or meet a justified current requirement. | Choose that check with regard to what its result can change, its cost, delay and displaced work; perform and assess it only when actually undertaken. |
| Suspend reliance or deprecate the affected result | The necessary support is absent or defeated and no permitted continuation carries the requested use. | Remove or qualify that reliance and communicate the affected reach. A status downgrade does not accept the underlying harm. |
| Apply an authorized exception | An applicable rule permits a bounded exception and a competent authority can grant it for this case. | Follow the actual mandate, scope, conditions and accountability. A senior title alone grants no authority over affected risk bearers. |

C.11 and C.19.2 supply the choice of worthwhile additional evidence. Rechecking available configuration or premise information need not be a new experiment. A possible experiment is not a Work commitment. If the desired check is unavailable, retain any independently warranted bounded action or limitation; do not fabricate an observation.

For an immediate unchanged use, stop with its usable result. When a later receiver needs a warning, limitation or retained reason to avoid unsupported reliance, keep that minimum content with the existing result or publication. A separate `DeprecationNotice` is useful when something is actually deprecated, not as proof that refresh was skipped.

#### B.3.4:4.5 - Follow affected dependencies and preserve real expiry

Trace a changed premise to the claims and uses that actually depend on it. Reopen those conclusions under their applicable evidence model. Shared paths do not multiply evidence or risk, and an unaffected use does not inherit a global downgrade from the carrier's age.

Keep actual physical and institutional conditions intact. Expired calibration qualification, an unavailable configuration, ended resource support or an elapsed rights window can block the corresponding use even when the old report remains an accurate record of an earlier state. A justified deterioration model can make elapsed time material; cite that model rather than inferring universal decay.

A dashboard should distinguish a review due, a defeated premise and a restricted use. Its colour reports the declared indicator or disposition, not the truth of the underlying claim. A failing test is a potentially relevant adverse result to assess now, not merely another overdue date.

#### B.3.4:4.6 - Worked cases: the same age, different decisions

**Bridge.** An earlier structural assessment supports a specified load envelope, conditional on its stated condition and inspection regime. For an unchanged limited use, available load and condition information and satisfied required inspections can preserve that support. The assessment's age alone adds no repeat assessment. In the paired case, proposed traffic exceeds the envelope: the earlier report does not support that use, however recent its cover date. Obtain the assessment or restriction needed for the changed load before relying on the stronger claim.

Suppose the available inspection team can either inspect a suspected load-bearing defect or repeat an already adequate check whose relevant conditions remain established. Examine the protected harm and the basis of the inspection requirement, what each result could change, and the cost of delay. Where the defect inspection can prevent that harm and the repeat adds no useful information, preserve the inspection capacity. If a currently binding repeat requirement prevents that choice, seek an authorized amendment; the resource conflict does not itself remove the requirement.

**Library.** The verified property of an unchanged library in its qualified configuration remains supported when the relevant assumptions and dependencies still hold. A new vulnerability affecting a dependency used by the security claim reopens that claim even before a review date. An unrelated vulnerability does not. Preserve unaffected functional results and any independently supported restricted service while addressing the security limitation. A release recipient who would otherwise assume the affected security property needs that limitation in the released result.

