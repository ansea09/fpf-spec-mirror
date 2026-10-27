---
chunk_kind: "child"
pattern_id: "C.40.OI"
pattern_title: "Bound an Opportunity Inquiry"
section_id: "C.40.OI:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.40.OI/C.40.OI__005_solution.md"
commit_sha: "00a27c2889bb2f7b8e0a7669075826e74d4dd270"
heading_path:
  - "C.40.OI — Bound an Opportunity Inquiry"
  - "C.40.OI:4 — Solution"
line_start: 84731
line_end: 84829
dependencies:
  - "A.15.9"
  - "B.5.PI"
  - "C.11.DUA"
  - "C.40.NU"
  - "C.40.OC"
  - "C.40.PC"
  - "E.10.DEV"
keywords:
---

### C.40.OI:4 - Solution

Bound the inquiry so it can direct the selected useful action and identify a sufficient return or truthful stopping point.

#### C.40.OI:4.1 - Identify the subject and claim posture

Name what may develop or be changed at the grain that matters now: a particular person, organization, community arrangement, AI model-and-scaffold configuration, facility, platform, research programme, episteme, or another exact subject. If identification is provisional, state the candidate boundary and what would settle it.

Mark the claim posture. A proposed future contribution is not actual change. A plan is not performed Work. A model prediction is not an observed result. If *development* or *evolution* still hides the subject, continuity rule, or value claim, use [`E.10.DEV`](https://github.com/ailev/FPF/blob/main/FPF-Spec.md) and return with the direct subject owner.

#### C.40.OI:4.2 - Identify a receiving use or an exploratory question

For a proposed contribution, state who or what could use it, in which situation, and what practical difference would matter. The receiving use may be the subject's later Work, a service used by another System, an organization's market or operating contribution, a research use, or a decision that consumes a qualified opportunity.

Keep the receiver's useful difference separate from the subject's desired learning, prestige, procurement, technology adoption, or internal activity. If no receiver or receiving situation can yet be named, keep that question open rather than inventing demand.

An inquiry can still start from material that someone can use or change: permitted records, a working procedure, a model or another construction. Name an available operation and a difference worth examining within the inquiry's resources and permissions. [C.40](https://github.com/ailev/FPF/blob/main/FPF-Spec.md) supplies that development Method. Its result can suggest a receiving use for C.40.NU or C.40.PC to investigate. A useful local result can also finish the inquiry; it need not become an opportunity.

#### C.40.OI:4.3 - Separate the return time from the development horizon

State when the inquiry's result must be usable and over what horizon the proposed development or its consequences matter. For example, an inquiry can return by Friday about a contribution intended to improve work over four months. The available effort within that window belongs in §4.5: six staff-hours is a resource ceiling, not the inquiry's elapsed duration. Add another change or consequence horizon only when it changes the question or protections.

Name conditions that the inquiry may not silently trade away. Depending on the subject and use, these can include safety, legal or professional limits, privacy, confidentiality, workload, service continuity, accessibility, resource ceilings, reversibility, distributional consequences, or preservation of future options. The direct practice owns their meaning and evidence.

#### C.40.OI:4.4 - State the reason to explore and separate its status

Write why exploration is warranted now. Distinguish:

- a qualified receiving problem or demand;
- an observed dissatisfaction or changed constraint;
- a proposed contribution or explicit problem hypothesis;
- a supplier promise, technology signal, or PatternID used only as a search lead; and
- curiosity that is valuable only if a bounded inquiry can be afforded.

Preserve competing formulations when they would send the inquiry toward different contributions. Use the direct problem-structuring pattern when deciding among those formulations is itself the current Work.

#### C.40.OI:4.5 - Establish available means and permissions

Identify what can actually be used before the inquiry must return: people's time and capability, source access, conversations, computation and other relevant means. Check who can obtain and interpret the proposed result. An available effort ceiling is not yet a reason to spend it; select the budget with the result in §4.6.

Count the work the inquiry would require from everyone affected, including preparation, obtaining the result, interpretation and use. Include delay, displaced work and downside where they can change the choice. A short interview can require substantial preparation or interrupt someone whose contribution is needed elsewhere.

Permission to inspect a source, interview a participant, or run a desk study does not authorize an intervention, access to restricted records, procurement, advice, or implementation. If the proposed inquiry cannot respect a protected condition, select a permitted alternative or return the exact gap. Keep any stronger evidence condition for a later consequential commitment visible.

#### C.40.OI:4.6 - Choose a worthwhile first result and enough inquiry

Identify a result that could improve the answer or next inquiry. Depending on what is already known, it may be:

- a change-relevant characterization from `C.40.OC`;
- materially different search leads from `C.40.NU`;
- a worthwhile problem and proposed contribution from `C.40.PC`;
- an admissible advising question or blocker from the applicable professional engagement Method; or
- a qualified result from the practice that owns a missing premise.

Say what plausible answers would change: the next question, a possible contribution, a supported claim, an admissible action or a justified stop. When the future receiver is unknown, use the local exploratory question from §4.2. Discriminating explanations or discovering a useful operation can justify inquiry before an intervention is selected.

Compare the attainable inquiry with what the present basis already supports. A narrower answer, smaller probe, different source, deferral or stop may serve the use better. Compare their whole burdens under §4.5 and the protections, not uncertainty alone. Use [C.11.DUA:4.1–4.4](https://github.com/ailev/FPF/blob/main/FPF-Spec.md) when the connection between the receiving question, evidence demand and worthwhile continuation needs development. Qualitative judgement is enough when it settles that choice.

Select the affordable inquiry whose attainable contribution is worth that burden, or finish with the supported answer now. State what would be enough for this use before spending the selected budget: for example, one evidenced difficulty and a question that distinguishes two plausible contributions. This condition need not settle every unknown. If the inquiry cannot reach it within the permitted means, return the narrower supported result or exact gap; exhausting a budget supplies no missing evidence.

For an outside-practice contribution, [A.15.9:4.1](https://github.com/ailev/FPF/blob/main/FPF-Spec.md), steps 2–3, connects reuse of an available answer with the decision to obtain more. When acquisition is worthwhile, its later steps bound the request and qualify the returned result for use. Asking for it does not supply it.

Start at that selected contribution. Publication order does not require the earlier PatternIDs to be used.

#### C.40.OI:4.7 - Return the bounded inquiry or exact gap

Use ordinary prose first. The following compact form can support a handoff when several people must inspect the same boundary:

```text
BoundedOpportunityInquiry@Context:
  subjectAndBoundary:
  claimPosture:
  receivingUseAndReceiver:
  inquiryReturnTime:
  changeOrConsequenceHorizon:
  protectedConditions:
  reasonToExploreAndStatus:
  knownPremises:
  suggestedButUnqualifiedPremises:
  inquiryBudgetAndPermissions:
  selectedResultAndSufficiency:
  directOwnerOrNextPattern:
  stopOrReopenCondition:
```

This is a local working form. An unsettled future receiver can remain unknown while the local question guides the inquiry. Keep the fields that change the next action or how another reader can use the result.

A complete return can be modest: “By Friday, use three of the six available staff-hours to locate one evidenced incident-handoff difficulty and the next question it warrants, using permitted examples and two brief clarifications. Preserve service workload and confidential records. This is enough to choose what to investigate next for Mira's work over four months; it does not select a course.” Section 5.1 shows why that inquiry earns its budget.

#### C.40.OI:4.8 - Stop, reuse, and reopen locally

Finish the boundary-setting work when the selected result, worthwhile effort, sufficient return and responsible practice are clear, or when the supported answer or exact gap already completes the present use. The inquiry itself stops at that sufficient return, a relevant blocker or its agreed limit; extending it requires a changed contribution comparison. Do not widen merely to increase idea count.

Reopen only the affected boundary when the subject, receiver, receiving use, horizon, protected condition, posture, authority, source premise, or effort budget changes. A changed characteristic need not erase an otherwise usable inquiry; a changed receiving use may.

#### C.40.OI:4.9 - What changes in practice

Instead of starting with a course, tool, provider, maturity label, or long opportunity list, the practitioner can now say what is being explored and why, over what horizon, under which protections, at what cost, and which result is needed next. A proposed contribution also needs its prospective receiving use. That is enough to begin responsibly without pretending that a recommendation or choice already exists.

