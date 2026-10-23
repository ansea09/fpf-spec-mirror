---
chunk_kind: "child"
pattern_id: "D.1"
pattern_title: "Clarify an Ethical Claim's Value Basis (Value Plurality)"
section_id: "D.1:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/D.1/D.1__005_solution.md"
commit_sha: "a5ac87ac15e78517d12bc66155b9da3ca254b643"
heading_path:
  - "D.1 — Clarify an Ethical Claim's Value Basis (Value Plurality)"
  - "D.1:2 — Solution"
line_start: 90814
line_end: 90905
dependencies:
  - "A.1"
  - "A.1.CSD"
  - "A.10"
  - "A.7"
  - "B.3"
  - "B.5.RA"
  - "B.5.RR"
  - "C.11"
  - "C.11.DUA"
  - "C.28"
  - "C.30.ILC"
  - "D.1"
  - "D.2"
  - "D.3"
  - "D.4"
  - "D.5"
  - "E.2"
keywords:
---

### D.1:2 - Solution

Start with the ethical claim or question, the affected EntityOfConcern, the value concern, and the present use of the answer. Name evidence and material uncertainty when the answer relies on them. If the task is to recognize the concern, a short statement of the value concern and next question completes that task; use `D.3` when its sides and tension need description.

To judge a use ethically admissible, explain how the value premises and available evidence support that judgement and where it remains limited. Recognizing a concern supplies neither that judgement nor permission to act.

Use an `EthicalValueFrame@Context` when the present reasoning or a later reader needs to compare value premises, distinguish the uses a judgement supports, or revisit a premise that can change it. This content can remain in the answer or an existing decision record. The following form groups the applicable content:

```text
EthicalValueFrame@Context:
  ethicalClaimRef
  affectedEntityOfConcernRef
  intendedEthicalUse
  claimScopeRef?: U.ClaimScope
  qualificationWindowRef?
  valueConcernRefs
  valueFrameEditionRefs?
  ethicalTheoryOrTraditionRefs?
  affectedHolonRefs?
  affectedSystemRefs?
  affectedEpistemeRefs?
  directResponsibilityRelationRefs?
  systemRoleAssignmentRefs?: FinSet(U.RelationRef constrained to U.SystemRoleAssignment)
  methodOrWorkRefs?
  transformationRefs?
  evidenceRefs?
  uncertaintyOrCurrentnessCondition?
  admissibleUse
  inadmissibleOverread?
  strongerSourceReturnCondition?
```

Include a source-return condition when a particular stronger claim or changed use needs it. Use `C.11.DUA` when the contribution or burden of a proposed frame, report, or evidence request is unresolved. The form creates no obligation to invent a further check or explain an inactive one.

This frame makes the value premises inspectable; the ethical judgement still needs its own reasoning. A utilitarian consequence claim, a deontic constraint, a virtue or character claim, a care-ethics concern, a rights claim, a professional-duty claim, and a project-specific value trade-off may all be admissible starting points, but they must not be presented as the same claim merely because the same word "ethical" appears.

#### D.1:2.1 - Make the value premise do explanatory work

A value label identifies a concern; a reason explains why that concern supports the proposed judgement. State the value premise, the relevant facts and the step joining them. For example, a prediction of greater aggregate benefit can support a recommendation only under a premise giving that benefit the relevant priority. A right can constrain the recommendation under a different premise even when the prediction is correct. Use `B.5.RA` when the argument must be recovered from a source, including a rhetorical question or an analogy.

Keep the grounds of acceptance distinct. Evidence can support a claim about consequences or the conditions in which a person agreed. A normative premise states what ought to count, what may be required or which treatment is permissible. Explaining a tradition's history can help interpret its premise; neither that history nor a model of a system establishes the premise's moral authority. When the premise is contested, preserve the conditional conclusion and identify what accepting another premise would change.

The following argument develops one such conditional basis for decisions about people's participation. It supplies reasons that can be examined and applied; FPF does not select this basis as its final ethical doctrine.

#### D.1:2.2 - Personal authority, voluntary participation and reciprocal limits

Use this reasoning when a proposal treats a person's body, work or participation as available because a planner can describe a useful larger system. The question is who may decide that person's contribution, on what grounds and within what limits.

##### D.1:2.2.1 - State the normative starting point

One possible starting point gives each person presumptive moral authority over the use of their own body and participation. On this view, another person's valuable plan creates a reason to request cooperation, but the value of that plan alone does not authorize the required personal contribution. This is a claim about how people should be treated, not a claim that they always control their circumstances.

Some accounts develop this position through **self-ownership**. The working claim here is the stated personal authority; a stronger ownership theory needs its further premises. Whether rights can be transferred, which rights cannot be waived, and which obligations qualify them are substantive ethical questions. A person's moral standing is also distinct from their present ability to decide or act. Children and people temporarily unable to decide do not become resources available to a planner; a protective or representative arrangement needs its own basis and limits.

For this argument, accept a second premise: comparable persons have the same presumptive standing, and a difference in treatment needs a relevant reason. Equal standing does not mean equal knowledge, skill, resources or preferences. Those differences can change who can perform work or give useful advice without establishing a right to command another person.

##### D.1:2.2.2 - Use reciprocity to expose a missing justification

Suppose a designer claims that knowing how to improve a project permits imposing its work on another person, while denying that the other person may impose work on the designer under comparable conditions. With the equal-standing premise, the designer's identity cannot justify this asymmetry. A relevant difference must do the work: for example, an applicable commitment or a justified authority limited to that decision. If no such difference is established, either the special permission must be withdrawn or the equal-standing premise must be rejected and the alternative defended.

This is the useful force of the reciprocal question: what would justify the same rule when the positions are exchanged? Preserve the facts that matter to the rule, including a real mandate, vulnerability and effects on others. Asking only whether the proposer personally likes the treatment is weaker: people have different preferences, and someone willing to endure a burden may still lack permission to impose it on others. Reciprocity examines the consistency and grounds of the proposed rule; it does not independently prove the starting premises or settle every conflict.

Combined with the personal-authority premise, the result is a reason to seek an authorized contribution rather than count the person as already available. When no applicable prior commitment or other justified authority covers the move, a plan requires the person's valid agreement or a different way of obtaining the result. Reusing an adequate existing commitment within its limits does not require asking for permission again.

##### D.1:2.2.3 - Explain what consent can authorize

Consent matters under this value basis because it lets the person exercise the authority the premise assigns to them. It must concern the proposed act or a sufficiently clear class of acts. A signature, silence or presence in a group cannot establish its scope and validity without the circumstances that give that response its meaning.

Examine the information and understanding needed for this choice, the person's decision capacity, the pressure involved and the practical ability to refuse. Where a person's agreement is obtained through a threat of a penalty that the adopted ethical basis does not justify, that compliance does not supply voluntary consent. Dependence or limited alternatives can make voluntariness doubtful; their presence calls for a judgement under the applicable ethical and domain standards, rather than an automatic inference either of valid consent or of its absence.

An agreement to contribute gives the recipient only the authorization it actually supplies. Agreeing to a defined task need not authorize a new purpose, wider disclosure or another person's participation. The applicable basis must also establish the conditions for changing or ending a commitment; permission to begin does not by itself answer every question about withdrawal. Some protections may remain non-waivable under that basis. Consent between two parties cannot by itself dispose of a third party's rights or settle harm imposed on that party.

When consent is absent or insufficient, retain the unmet condition. A narrower task, different terms, supported voluntary participation or another provider can sometimes meet the project's purpose. Where the question is which alternative to choose or how to resolve a conflict with another duty, use `D.3` and `D.4`.

##### D.1:2.2.4 - Keep system structure and rights separate

A person can participate in an organization or be a physical component of a working arrangement while retaining moral claims against what that arrangement demands. Describing the organization's useful function does not establish a duty to serve it. Conversely, a person's refusal does not establish that every obligation they previously undertook has disappeared. Identify the proposed act and the relation that could authorize it.

Ownership of a tool, authority over work, membership in a group and physical part-whole relations answer different questions. Treating possessions as an extension of a person may express a moral argument for protecting them, but extending the personal-authority premise to property requires an account of legitimate possession and its limits. It does not make every owned object a physical part of its owner. Likewise, a sponsor's control of funds or equipment does not confer control over every person the project affects.

Dissolving an organization and killing its members have different consequences. A model that calls both entities living systems cannot supply the missing ethical comparison. Investigate the actual consequences for people, including dependence on the organization and the costs of transition, instead of deriving either unconditional preservation or harmless dissolution from the metaphor.

##### D.1:2.2.5 - Identify the premise that changes the conclusion

A consent-based account can recognize duties to others and limited powers that do not depend on consent to each individual act. Their justification must be supplied rather than hidden in the word "system". A valid employment commitment may authorize a bounded assignment. A protective duty or public authority may be offered as another basis; its source, scope, safeguards and application need the relevant ethical and domain reasoning. Calling compliance consent would conceal the difference.

Other value frames can give different reasons for the same decision. A consequence-based account asks whether the proposed intervention produces better supported outcomes than feasible alternatives, with its chosen treatment of distribution and rights. A public-justification account asks whether the governing rule and its unequal powers can be justified to those subject to it, including a basis for binding dissenters. A care-based account may give special weight to dependence and responsibilities arising from a relationship. These lines can support or oppose a particular use of authority; none follows merely from system scale or the number of supporters.

Locate the disagreement: the standing assigned to persons, the priority of a duty, the validity of an authorization, a predicted consequence or the interpretation of a rule. That tells the practitioner what could change the judgement. A conditional argument for voluntary cooperation establishes neither that all public projects fail nor that every collective decision needs unanimous consent. Whether an artificial system has moral standing is also a separate question from whether it can pursue goals or perform a task.

The practical result is an explained boundary on a proposed action: which contribution may be requested or required under which premises, which agreement or authority supports it, and what remains unresolved. `D.3` describes a resulting value conflict; `D.4` develops and compares ways to continue.

