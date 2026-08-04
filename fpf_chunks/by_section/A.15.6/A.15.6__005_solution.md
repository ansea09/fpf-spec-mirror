---
chunk_kind: "child"
pattern_id: "A.15.6"
pattern_title: "Project, Process, and Case Recovery through Work, Method, and Transformation"
section_id: "A.15.6:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.6/A.15.6__005_solution.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.15.6 — Project, Process, and Case Recovery through Work, Method, and Transformation"
  - "A.15.6:4 — Solution"
line_start: 26337
line_end: 26468
dependencies:
  - "A.1"
  - "A.1.STM"
  - "A.12"
  - "A.15.1"
  - "A.15.2"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.22"
  - "A.3.1"
  - "A.3.4"
  - "A.6.1"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "C.2.1"
  - "E.17"
  - "E.18"
  - "E.18.NET"
  - "E.24.PUB"
keywords:
---

### A.15.6:4 - Solution

Recover the direct subject selected by the working concern. Apply the subject's governing pattern, then relate plans, systems, transformations, results, descriptions, and publications to it through their own direct relations.

#### A.15.6:4.1 - Recover an actual project as composite `U.Work`

In Plain use, **actual project** denotes one composite `U.Work` occurrence: the performed work whole. A temporary organization participates in or coordinates that work; a `U.WorkPlan` specifies intended work; a `U.Transformation` identifies bounded change of an affected referent; project cards, repositories, and dashboards describe or publish claims about these objects. None supplies a second identity for the work whole.

First admit the candidate composite Work under `A.15.1`. Name every actual performer `U.System` and its covering `U.RoleAssignment`; state every explicit `performedUnderAssignment`, the exact `U.Method` the whole enacts, its governed temporal extent, and its `executedWithin` containing system. Admit each included Work occurrence independently and state the exact obtaining work-part relation that connects it to the whole. A shared project label, plan membership, continuity policy, or temporal containment establishes neither the composite Work nor its parthood.

Only then apply five project-specific qualification tests to the admitted Work:

1. The composite work has a temporary or transient boundary with a start and a completion or termination condition.
2. An accepted intention episteme whose claims state the intended objective and any intended product, service, result, or value is linked to the work through a direct plan or decision relation.
3. A work-part and continuity policy says how interrupted, resumed, split, or merged work retains or changes identity; the policy decides an actual ambiguity but does not create the Work or its parts.
4. At least one independently admitted performed Work occurrence is connected to the composite Work by an exact obtaining work-part relation.
5. For each claim used to qualify the project, name what the claim is about — the participating system, affected referent, transformation, result referent, or another subject actually asserted — and say how that subject matters to the Work. Then choose one truthful claim form: state an obtaining direct relation of the needed kind; use an exact `A.6.1` binding for one reusable-operation application; state a local production, inception, or completion claim under `A.15.PROD`, or another relation-defined claim under `A.6.RCD`; or return one non-assertability result. For non-assertability, state whether the reason is `factually unsupported`, `missing-information`, or `missing-governor`. Only `missing-governor` means that no pattern currently admits the relation or claim needed for the question, so only that reason reopens ontology. Project wording and container membership supply none of these links.

No performed work means no actual project occurrence yet. A proposal, charter, authorization, schedule, budget decision, or funded intention can establish a `U.WorkPlan` and related commitments. It does not backdate performed work, a future system, an assignment, an actual change, or a result.

The project occurrence uses the identity, temporal extent, parts, episodes, continuity, and relation-specific aggregation defined in `A.15.1`. Project wording adds no second identity rule. When a reader asks for the project result, ask first: **What exactly is the result, and result of or for what?** Keep that referent in the kind or claim already established for it, then apply test 5. If the required relation or claim kind exists but the case facts make the assertion false, return one non-assertability result with reason `factually unsupported`; if that kind exists but a required fact cannot be recovered, use `missing-information`; only when no pattern admits the required relation or claim use `missing-governor` and reopen ontology. Otherwise keep an intended target in the plan.

Whole-project roll-up requires exact work-parthood plus an aggregation policy defined for the one relation and measure being aggregated. Outputs, effects, verdicts, epistemes, deliveries, and uses do not become one result merely because they share the project label.

#### A.15.6:4.1a - Connect project work to its project system-of-interest and network question

Start with an ordinary sentence: **this project work is intended to change, produce, restore, evaluate, or prepare the use of this system**. Then name the composite project `U.Work`, the system or intended-system designator, the plan or decision that selected it, the concrete change or use being pursued, and the next decision that needs the designation.

The primary expression is **project system-of-interest**, inherited from systems engineering without adding target, aim, or goal semantics. `systemOfConcern` may be used as a historical Plain synonym. Neither expression admits a system, role, relation, or project kind.

When the designated system already exists, identify that same entity under its admitted `U.System` kind. The plan or decision may say why it matters to the project, but that designation does not put the system inside a project container. Actual links still come from relations that obtain: an exact work-to-referent or work-to-change relation, one independently identified transformation, a branch-local A.15.PROD production or inception claim, an evaluation, a participation or use relation, or another direct owner. Include only links used by the named decision.

When the system is only intended, keep its designator and expected change or use inside the `U.WorkPlan`, decision, system description, or other claim episteme. Before its identity rule first holds, there is no future `U.System`, role-assignment holder, or transformation of that not-yet-existing system. A.15.PROD may later state the identity-inception boundary. After inception, relate the actual system to the earlier description through the applicable reference or identity claim, then test project designation, participation, and any role assignment at their own times.

Project designation and role assignment do not entail one another. Materialize `SystemOfInterestRole` only after A.2 names the role value, taxonomy episteme, effective scheme, and one concrete enactment-facing participation. Only when assignment identity or its window matters does A.2.1 add the admitted holder, obtaining assignment, and uninterrupted extent. Designation, passive affectedness, or a familiar label supplies none of these facts; an obtaining role assignment does not prove project designation. A patient record, damage claim, measurement result, or other non-system case subject can remain central to project Work but cannot hold that role.

When one project question spans operation or use of the project system-of-interest together with production, identity inception, later change, verification, feedback, or recursive builder questions, E.18.NET may select the relevant independently identified TFS or nested-network members. The selection must pass its four A.22 discriminators: direct members, obtaining cross-member relation occurrences, applied constraints, and one `networkUseFrame`; all endpoint bindings must resolve. If a member or relation is ungrounded, keep a Plain proposed network explanation and name the missing member, governor, false or unresolved predicate, occurrence, or binding. The selected network is a non-agentive `U.Structure`, not the project, performed Work, a case, or evidence of work parthood.

If the network-selection judgment must persist, use one ordinary C.2.1 result episteme whose exact EntityOfConcern is that selected network and whose claim says only why it answers the named project question for the stated basis and qualification window. Project Work, transformations, case closure, production, evidence, and decisions remain separate subjects and claims. A record creates none of them and creates no `projectHasNetwork` relation.

**Stop before asserting a compound project-selection claim.** A plan or decision designation and every independently obtaining Work, change, production, evaluation, delivery, acceptance, or use fact remain usable. When a named decision also needs one compound truth that this project selected this system, return `missing-substrate[project-selection-conjunction]` until one selected constructor substrate and edition define its inputs, output claim, applicability, and truth semantics. The A.6.RCD conjunction probe and reference scheme are not that substrate.

Keep the four inputs to that bounded question visible without turning their conjunction into a predicate: (1) the composite Work has passed A.15.1 admission and the five project-specific tests in section 4.1; (2) one identified plan or decision designates the actual system and states the intended change, production, evaluation, or later use; (3) every cited work-to-referent, work-to-change, transformation, production, evaluation, delivery, acceptance, or use fact has its own direct governor and obtains independently; and (4) the account names the concrete decision or action for which the designation matters.

For `PumpUnit-3`, the independently admitted composite Work and parts, five project-specific qualifications, plan, upgrade decision, and pump-change facts remain useful. The designation fails if the plan or decision does not designate `PumpUnit-3`, even when Work and pump change exist. The satisfied facts and this contrast create neither a predicate nor a relation occurrence. Reopen A.6.RCD only when an exact substrate is selected, repeated use needs one stable predicate rule, or a downstream decision must reidentify the same selection occurrence.

#### A.15.6:4.2 - Recover a process concern through `U.Method`, an exact selected `U.Structure`, or `TransformationFlowStructure`

When the question is about repeatability, ordering, throughput, variation, control, or improvement, select the exact reusable subject:

- `U.Method` when the concern is a way of doing with preconditions, effects, interfaces, and composition;
- an exact `U.Structure` under `A.22` when the organization of method-side objects and relations changes the next question or admissible action;
- `TransformationFlowStructure` when the question is about loci, transfer relations, crossings, coupled flow valuations, split-and-join organization, or refresh slices.

Before selecting the method-side `U.Structure`, identify every constituent independently, state every selected obtaining relation under the pattern that admits it, and state each applied constraint. Then name the selection question, the action the selected organization permits, and the overread it forbids. Only after these four discriminators identify the structure may you call it `MethodRelationStructure` for that selection question. The phrase is a local designator, not a U-kind, relation type, method, flow, work occurrence, or holon; the label and an `@BoundedContext` suffix contribute no locality or identity. If any discriminator is absent, keep the obtaining direct relations unbundled and do not select a positive structure.

A dated `U.Work` occurrence may support a process claim only after you recover the exact fact it demonstrates. To show method enactment, name the obtaining A.15.1 `enactsMethod -> U.Method` relation from that Work to the selected `U.Method`. To show one operation application, use an A.6.1 binding only when the exact reusable operation declaration, the particular application, and its typed argument or result bindings are recoverable. A shared label, compatible result, trace, record, or observation establishes neither fact. Measurements, exceptions, and evaluation evidence about the Work remain separate relations and epistemes. These facts do not retype the Work as the repeatable method or selected structure. When the claim is about the execution, a deviation, or incident work, select that `U.Work` separately.

Process remains useful Plain management wording. It does not introduce `U.Process`, an `@Process` suffix family, or a parallel work identity.

#### A.15.6:4.3 - Recover a case concern through one exact subject or claim

A case is Plain subject- or claim-centred working language, not `U.Case` and not automatically a network member or slice. Start with the closure question, then return one minimal result:

1. name the exact subject or claim and its direct identity and reference owner;
2. keep only the TFS, `SubflowRef`, `PathSliceId`, exposed position, selected network, Method, Work, transformation, evidence, decision, or neighboring direct claim needed to answer the closure question;
3. state the separately governed fact, evidence, or decision on which closure depends; and
4. name one downstream receiving use or position and say explicitly that this later use is outside the closed case.

The subject is not restricted to one continuing changed entity. A maintained system, patient, material batch, or other continuing referent may be followed through conditions and independently grounded A.3.4 transformations. An episteme case instead follows exact episteme identities: changed claim content identifies another episteme and historical continuity uses `EpistemeEditionRelation`, not transformation of one unchanged episteme. A characteristic inquiry distinguishes the bearer, value or assignment, measurement occurrence, and result episteme; an immutable value neither changes nor acts. One exact relation occurrence, decision, result, or independently selected edition-lineage structure may be the case subject when that is what the closure claim concerns.

Methods, Work, performers, assignments, plans, transformations, production claims, evidence, decisions, and publications enter only when the closure question needs them, and each keeps its direct owner. Plain “Method for transforming the case subject” is retrieval shorthand: Work enacts a Method, while change, production, inception, readiness, result, and closure each need separate grounds. A Method or completed Work alone closes no case and proves no transformation.

If a case claim must persist, use one or more ordinary C.2.1 epistemes. A persistent case record remains an ordinary episteme and has no slots; any typed participant `SlotSpec` belongs to the `RelationSignature` of the exact governing relation, not to that record. Each episteme takes its truthful EntityOfConcern from its own claim content; split closure, relation, evidence, and network-selection claims when they concern different subjects. Usually keep the needed facts separate. Use A.22 only when one named later task must reuse their organization as one thing and all four identity discriminators pass. Otherwise keep a direct plurality or the exact E.18/E.18.NET references that answer the question. A case file, dashboard, identifier, or filled record creates none of the subject, organization, closure, or downstream relation.

You may describe this working boundary without asserting a new relation. If a later task must assert and reidentify a relation from the case to its downstream use, first open that relation's direct owner. If no current pattern supplies the predicate, return its participants and `missing-governor`; prose and an episteme cannot make the relation obtain.

#### A.15.6:4.4 - Do not force the three readings into one view family

Project, process, and case wording is only a cue to inspect the claim. Under `C.2.1`, each description is identified through its actual claim content, one exact EntityOfConcern, and the effective reference scheme; a management topic does not assign that EntityOfConcern.

| Description wording | Recover the direct EntityOfConcern from what the claim actually says |
|---|---|
| project cost, completion, or result | Select the composite project `U.Work` only when cost, completion, or another predicate is actually asserted of that Work. If the claim is about a measure, transformation, produced entity, value, condition, verdict, decision, relation occurrence, or result episteme, select that exact subject instead. |
| process repeatability, variation, throughput, or improvement | Select `U.Method` only when the claim concerns the reusable way; select an exact A.22 `U.Structure` or `TransformationFlowStructure` only when it concerns that admitted organization. Otherwise select the exact measure, evaluation result, obtaining relation, relation-bearing claim, or admitted collection-as-whole of occurrences actually asserted. |
| case condition, trajectory, closure, or next downstream use | Select the exact subject or claim named by the closure question: a continuing referent and its conditions, an episteme edition thread, characteristic bearer or assignment, measurement or result episteme, relation occurrence, Work, decision, or another directly identified subject. Name the downstream receiving use but keep it outside the closed case. |

One description keeps one truthful EntityOfConcern. When independent claims have different direct subjects, keep separate epistemes rather than inventing a union concern. An exact E.17.0 viewpoint episteme states the concern and conformance rules for a description; it does not turn different direct subjects into views of one entity. When accounts with different EntityOfConcern values must be related, keep each episteme and its own viewpoint-conformance judgment explicit, then state the exact correspondence relations required by the Work that uses those accounts; source-event proximity creates neither conformance nor a new multi-view family.

If the description needs empirical grounding, identify the exact admitted holon and the `EpistemeEmpiricalGroundingRelation` governed by `C.2.1`. `GroundingHolonSlot` belongs to that relation's `RelationSignature`; it is not a slot of the description episteme. Project work, `U.Method`, a selected method-side `U.Structure`, `TransformationFlowStructure`, transformation, and affected referent do not acquire episteme or grounding-relation slots from the account.

#### A.15.6:4.5 - State exact project-local relations

An existing `@Project` name is a compatibility and retrieval cue. It does not establish identity, parthood, authority, viewpoint, or locality.

When a record or relation is genuinely local to one actual project, name its exact relation to the composite `U.Work` and use a typed reference:

| Current referenced object | Honest reference head |
|---|---|
| the selected composite project-work occurrence | `projectWorkOccurrenceRef : U.EntityRef`, constrained to ValueKind `U.Work` |
| another specific work occurrence | `workOccurrenceRef : U.EntityRef`, constrained to ValueKind `U.Work` |
| a repeatable method | `methodRef : U.EntityRef`, constrained to ValueKind `U.Method` |
| an exact selected method-side structure | `methodRelationStructureRef : U.EntityRef`, resolved to the exact `U.Structure` selected under `A.22`; the local designator `MethodRelationStructure` adds no kind or identity constraint |
| a transformation-flow structure | `transformationFlowStructureRef : U.EntityRef`, constrained to ValueKind `U.Structure` |
| the entity being changed | `affectedReferentRef : U.EntityRef`, narrowed to the ValueKind already admitted for that entity when the reference must carry that constraint |

Use `projectWorkOccurrenceRef` only for the identified project-work occurrence. Do not use a generic project reference when the relation actually concerns a `U.Method`, exact selected `U.Structure`, `TransformationFlowStructure`, affected referent, description, publication, viewpoint, source use, evidence, or authority.

#### A.15.6:4.6 - Apply work continuity rather than label continuity

For interrupted, resumed, split, merged, or performer-changing project work, apply the `A.15.1` work-part and continuity policy:

- performer or team replacement changes participation relations but need not change parent-work identity;
- interruption and resumption remain episodes of one parent work or become linked work occurrences according to the declared policy;
- split and merge use work-part, containing-work, predecessor, successor, or new-work identities;
- failed or terminated work remains actual project work even when its intended result is absent or adverse;
- continuous operations qualify as a project only when one finite composite Work first passes the complete A.15.1 admission basis and exact parthood, then passes the five project-specific qualifications.

The organization performing or coordinating project work is a neighboring `U.System`. Organization continuity does not decide project-work continuity.

#### A.15.6:4.7 - Run the direct-subject recovery sequence

1. Say the management claim in ordinary language without treating *project*, *process*, *case*, or *project system-of-interest* as a kind.
2. Ask what the next decision is about: one performed Work whole; a reusable Method; one selected method-side or transformation-flow structure; one project-level network question; or one case subject or claim and its closure.
3. Admit or select that subject through its owner: A.15.1 for Work, A.3.1 for `U.Method`, A.22 for a selected `U.Structure`, E.18 for one TFS, E.18.NET for a grounded network, A.3.4 for an actual change of one continuing referent, C.2.1 for an episteme, or the direct owner of the case subject. A label, interval, record, or local designator substitutes for none of these facts.
4. If a project names a project system-of-interest, decide whether the system already exists. Keep an intended future referent in plan or description content. For an actual system, keep recognition, plan or decision designation, each Work/change/use fact, any `SystemOfInterestRole` interpretation, and any assignment separate. Use section 4.1a for a project-network question or the exact compound-selection stop.
5. For a case, name the exact subject or claim, only the bounded references and direct claims needed for closure, the separately governed closure basis, and one named downstream use that remains outside the closed case. Persist only truthful C.2.1 claims; use A.22 only when one named later task must reuse the organization as one thing and all four identity discriminators pass.
6. Keep plans, performers, role assignments, transformations, results, decisions, evidence, descriptions, and publications distinct. For a result claim, ask what the result is and what it is a result of or for. Then use an obtaining direct relation, an exact A.6.1 application binding, a local A.15.PROD or A.6.RCD claim, or a non-assertability result marked `factually unsupported`, `missing-information`, or `missing-governor`. Only the last reopens ontology.
7. If a description is needed, recover its claim content, one truthful C.2.1 EntityOfConcern, and effective reference scheme after the direct subject is known. Select a `BoundedModelUseStructure` only when it changes how the next assertion is read or used; otherwise omit it.
8. If a local record refers to the selected subject, name the relation and use a typed reference. A suffix, record row, or case label adds no identity, locality, organization, or closure.
9. When these recovered results must re-enter the long dependency from outside use through architecture, Work, change, and recursive builders, continue through A.1.STM. Otherwise stop at the direct result that answers the decision.

