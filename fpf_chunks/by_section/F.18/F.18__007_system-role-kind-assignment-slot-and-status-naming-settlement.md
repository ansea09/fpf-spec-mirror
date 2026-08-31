---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:5"
section_title: "System-Role-Kind, Assignment, Slot, and Status Naming Settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__007_system-role-kind-assignment-slot-and-status-naming-settlement.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:5 — System-Role-Kind, Assignment, Slot, and Status Naming Settlement"
line_start: 99343
line_end: 99460
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "B.3"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "F.0.1"
  - "F.1"
  - "F.13"
  - "F.14"
  - "F.15"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.5"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.2"
  - "G.6"
keywords:
---

### F.18:5 - System-Role-Kind, Assignment, Slot, and Status Naming Settlement


This settlement keeps naming aligned with the object already recovered. Bare *role* is a trigger handled by `E.10.ROLE`, not a reusable kind head.

#### F.18:5.1 - System-Role-Kind Names

A durable system-role-kind name designates one exact local kind admitted through C.3 and A.2. Recover that kind through its candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. A practice or source reference can locate the definition or signal that two definitions should be compared; it does not identify the kind. Candidates are entities already admitted under A.1 as `U.System`, including a person, team, organization, or non-human technical object. The Tech designation normally ends in `...SystemRole`, for example `ReviewerSystemRole`, `ShipbuilderSystemRole`, or `ServiceProviderSystemRole`. `SystemRole` is compound morphology, not a universal governed value. The name creates no system admission, kind membership, assignment, agency, capability, or Work.

A system-role-kind name must not include:

- the holder of an assignment or the assignment occurrence;
- capability evidence or skill level;
- method or method-family selection;
- performed Work;
- status value or gate result;
- source, evidence, publication, or assurance use.

If a phrase such as `SeniorReviewer`, `NightOperator`, or source wording such as *evidence role* appears, recover the current claim first. The result may be an exact local system-role kind, one direct assignment occurrence, a status assertion, an evidence-use relation, a Work admission condition, another governed value, or a local source phrase. Do not force all of them into one system-role-kind name.

#### F.18:5.2 - System-Role-Assignment Names

A system-role-assignment name designates one already recoverable obtaining occurrence of an exact direct species under `U.SystemRoleAssignment` and A.2.1; the system-role-kind name does not identify that occurrence. Recover the admitted holder system, the exact assigned local system-role kind, and only additional participants needed to distinguish that direct species. A taxonomy, reference scheme, description, display, or generic context episteme is not a mandatory assignment participant. Assignment extent follows uninterrupted predicate truth; an assertion or occurrence-description episteme may state a known interval separately. A durable assignment name uses a `NameCard` whose `GovernedValueRef` resolves to that occurrence. If public or cross-context reuse is needed, apply section 4.4; until it passes, retain the card locally and mark the row pending. Neither a name, card, row, nor publication occurrence makes the assignment obtain.

`Holder#Role:Context@Window` is source notation only. Recover the holder System, local system-role kind, assignment occurrence and its declared species when one exists, and any separately applicable context, schedule, interpretation, or Work relation. The source token is neither a Tech name nor proof of assignment, capability, or performed Work.

#### F.18:5.3 - Capability, Method, and Work Names

Keep these separate:

- `ShipbuilderSystemRole` names one exact local system-role kind;
- `ShipbuildingCapability` names a capability of an admitted `U.System`, including an acting holon admitted as a system for that capability claim;
- `ShipbuildingMethod` names a method or method family;
- `HullAssemblyWork` names a work family or planning-level work label until an exact performed occurrence is current.

A role-derived or role-method-coupled expression is only a naming cue. First recover the exact value it refers to. If that value is an exact Method or Method family under A.3.1, choose a Method name. If it is an exact `U.MethodDescription`, `U.WorkPlan`, or dated `U.Work` occurrence, name that description episteme, plan episteme, or occurrence separately under A.3.2, A.15.2, or A.15.1; those names are not Method names. If the expression refers to another value, use the rule that defines or tests that value. Only then use F.18 to choose a durable name. An exact relation involving a system-role kind or assignment may constrain who may use a Method or perform Work; it neither creates nor names the Method, description, plan, or Work occurrence.

Treat an action nominal such as `testing`, `assembly`, `maintenance`, `evaluation`, or `inspection` as a morphology cue, not a governed kind. Placement in function- or flow-structure prose identifies no `U.Function`. If the function-like use remains claim-bearing while its exact object or relation is hidden, apply `A.6.F`; if it is already recoverable, name the exact method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, performed-work occurrence, or other governed value under the rule that defines or tests it. Only then use F.18 to choose a durable name. A WBS element, activity, or Work Package remains plan- or assignment-episteme content about intended work; none of these uses identifies a performed Work occurrence admitted under `U.Work`.

A durable name for performed Work points to one dated occurrence already grounded under `A.15.1`. An action word, plan row, local work-family label, or `U.WorkPlan` does not create that occurrence or an assignment.

Every System claimed as an actual performer must already have its A.13 core, and A.15.1 must independently admit the dated Work from its Method, temporal extent, containing System, and other required direct facts. Add an assignment occurrence and F.6 only when the naming account or receiving use expressly represents precise assignment-bound attribution; then the assignment covers the Work interval, names that already recovered performer as holder, and retains every participant required by its declared `U.SystemRoleAssignment` species. Missing or failed F.6 leaves the Work and its durable name intact. A compact naming account cites only the identities needed by its receiving use. Add a continuity policy only when interruption, retry, a changed Method or binding, or competing designators make occurrence identity material.

Keep neighbouring direct subject and resource-use claims, `A.15.PROD` production claims, measurement-result epistemes, evaluation results, `C.11` choices or decisions, delivery occurrences, acceptance verdicts, and downstream-effect claims separately named under their direct patterns.
When the underlying boundary wording still hides the relation, apply `A.6.P.WMR`. Use `F.18` only after an exact governed value and its use are recovered through a direct subject relation, an exact `A.6.1` application binding, or an exact local `A.15.PROD`/`A.6.RCD` claim. An exact non-assertability result independently records `factually unsupported`, `missing-information`, or `missing-governor`; none authorizes durable naming, and only `missing-governor` is an ontology blocker that names the affected use and future subject pattern or relation declaration. This section selects and tests a name. It does not define a second work-occurrence or work-result recovery algorithm.

Method-relation and method-composition names are method-side names too. If a phrase names serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, fallback, or dispatch among methods, first decide which object the phrase names.

- If admitted submethods make one composite way of doing, name the composite `U.Method`. Use A.3.1 for that Method and B.1.5 or another direct composition pattern for its exact composition relation.
- If the phrase names relations among methods without making one whole Method, name the relations first. When a named use depends on how several such relations are organized, select that `U.Structure` under A.22 and designate it `MethodRelationStructure`; state the question and prohibited overread that bound the selection. Identify and constrain each included method-side relation—for example, composition, refinement, substitution, iteration, decomposition, family membership, selection, or fallback—through its A.3.1, G.5, or other defining rule. A claim-bearing episteme that describes such a relation remains separate under C.2.1, and any Work-use relation remains under A.15.
- If the current object is a separately identified episteme that describes one exact admitted Method, `A.3.2` may classify it as `U.MethodDescription`; F.18 names that episteme separately from the Method.
- If an episteme instead describes the selected relation structure, `C.2.1` keeps that structure as its exact `EntityOfConcern`; the episteme is not thereby a `U.MethodDescription`.

F.18 settles a durable name only after one of those exact objects has been recovered. Algebraic, graph, categorical, process-calculus, matrix, embedding, distributed, or neural notation names the lens or representation only when that lens is the governed value.

#### F.18:5.4 - System-Role-Kind Relations, Method Relations, System-Role–Method Relations, and Lens Names

System-role-kind-relation expressions remain ordinary expressions or direct relations unless their exact local kinds and relation predicates are already admitted. An algebraic, graph, matrix, embedding, distributed, or neural description is a lens over the selected `SystemRoleKindRelationStructure`; it is not automatically the named kind, holder, assignment, Method, or Work.

First recover what the name is for:

| Expression or source phrase | What can be named | Naming rule |
| --- | --- | --- |
| `R1 <= R2` | one exact directional admission-substitution relation occurrence between two independently admitted local system-role kinds, identified by the ordered kinds, receiving-use rule, applicability, and only meaning-changing semantic-basis editions | Name or cite the exact relation occurrence or a selected `SystemRoleKindRelationStructure`; keep any assertion or policy record, current assignment, receiving check, and outcome separate. Admit another system-role kind only when its own C.3 identity and membership basis warrant it. |
| `R1 incompatibleWith R2` | one exact symmetric incompatibility relation occurrence between two independently admitted local system-role kinds, identified by the unordered pair, same- or different-holder rule, Work identity, overlap test, applicability, and only meaning-changing semantic basis | Name or cite the exact relation occurrence or a selected `SystemRoleKindRelationStructure`, not another system-role kind. Exact assignments and the receiving Work remain separate inputs and do not replace the two kind participants. |
| `R1 and R2` | two independently admitted system-role kinds; any assignment occurrences are separate and are required only when the receiving sentence also claims them | Use “and” in ordinary prose. Keep the two kind claims recoverable, and do not infer assignments or make a compound kind by hyphenating the labels. |
| `R1 bundle R2`, or quoted source shorthand `RoleBundle := R1 and R2` | one order-insensitive finite-set relation among exact system-role kinds, with a joint-admission and holder-allocation predicate | Keep it as a bundle relation. A convenient bundle name does not admit a compound system-role kind; such a kind would need its own independent C.3 identity and use. |
| `R1` qualified by a domain, practice, Method family, or ordinary work field | either one independently admitted local system-role kind or a residual A.2.7 qualification relation between two kinds | Before naming a kind, recover its C.3 candidate domain, operative membership condition, intended member/non-member boundary, and continuity rule. A domain, practice, ordinary work field, Method, Work family, or performed Work occurrence remains a separate value or comparison cue. Keep a non-monotonic restriction as its exact relation and do not infer admission substitution. |
| Method-like phrase derived from a system-role label | Method, Method family, MethodDescription, WorkPlan, or Work occurrence | Name the recovered object through `A.3.1`, `A.3.2`, or `A.15`; cite the exact system-role-kind relation separately when it constrains admission or performance. |
| algebraic, graph, matrix, embedding, distributed, or neural representation of system-role kinds or their relations | mathematical or representation description of a selected `SystemRoleKindRelationStructure` | Name the lens only when the representation itself is the object being named; otherwise name the recovered kind, relation occurrence, selected structure, Method, assignment, or Work. |
| Method algebra, Method graph, Method matrix, process calculus, selector calculus, or Method embedding | mathematical or representation description of exact method-side relations or their selected `MethodRelationStructure` | Name the lens only when the representation itself is the object being named; otherwise name the exact relation, selected structure, Method family, MethodDescription, WorkPlan, Work occurrence, or neighboring relation. |

Ordinary speech may say “surgeon”, “reviewer”, or “operator” when the local sentence makes the intended system-role kind or assignment obvious. Use the concrete `...SystemRole` designation when stable technical reference to the kind is needed. Do not infer kind identity, assignment, relation, Method, capability, or Work from the ordinary word alone. Add a qualifier only when it distinguishes a live neighboring reading.

#### F.18:5.5 - Status, Evidence, Source, and Publication Names

Status-like and evidence-like wording must go to direct patterns:

- status value or status assertion: `F.10` or `A.19.SPR`;
- evidence-use relation: `A.10`;
- assurance use: `B.3`;
- source use: `E.10.D2` or source-use patterns;
- description-episteme identity: `C.2.1`;
- multi-view publication face or form: `E.17`;
- availability of one selected edition, expression by a form, and bearing by a carrier: `E.24.PUB`;
- gate or admission result: the relevant gate, decision, or assurance pattern.

Do not name these as system-role kinds or assignments unless that separate work-facing classification or direct assignment occurrence is actually current. “This standard plays the role of evidence” is repaired to the appropriate evidence-use, source-use, or status-use relation; it is not an assignment of the standard.

#### F.18:5.6 - Relation, Slot, Interface, Port, and Signature Names

If a name touches relation, slot, interface, port, boundary, protocol, API, or signature wording, use `A.6.RSIR` and subject patterns.

- Use A.6.5 for relation slot discipline and `SlotSpec` declarations.
- Use A.6.0 for signatures and law-defined declarations.
- `A.6.M` and architecture patterns define or constrain module interfaces and architecture interfaces.
- `A.6.F`, transformation, and architecture patterns define or constrain functional ports and functional structures.
- `A.6.C`, protocol, service-access, and commitment patterns define or constrain API, protocol, and service-access cases.
- Use C.2.1 for the identity and content of a claim-bearing interface-description episteme.
- Use E.17 for a multi-view publication face or form.
- Use E.24.PUB for availability of the selected edition and for the separate form-expression and carrier-bearing relations.

Before naming a relation-facing object, keep these settlements distinct:

| Object to name | Required prior settlement |
| --- | --- |
| reusable predicate-definition episteme | An `A.6.RCD` result records a reusable definition and `C.2.1` gives it one truthful exact `EntityOfConcern`; the name denotes the definition, not a relation kind |
| derived or primitive relation kind | `A.6.RCD`, `E.24`, and `E.24.UK` have admitted the kind and its direct subject pattern states obtaining, applicability, and occurrence identity |
| one obtaining relation occurrence | the subject pattern establishes obtaining and `A.6.REL` applies the admitted kind's identity rule |
| formula, query, path, graph, diagram, or other representation element | `C.29` states what it represents and the relevant correspondence; its name does not name the represented relation by default |
| designator or reference | the exact designation or reference relation resolves to the already settled object under its reference scheme |

One token may be reused only where the reference scheme and local sense preserve these distinctions; it cannot collapse definition, kind, occurrence, representation, and designator into one object.

`F.18` can settle a durable name for the recovered value. It does not decide which value the interface word names, create a public row, or make that row available.

Words such as *member*, *membership*, *belongs to*, and *in* do not by themselves identify one reusable relation. First use `E.10` to recover whether the sentence concerns mathematical inclusion, kind classification, relation participation, collection belonging, or constructive parthood. For a collection, an ordinary sentence such as “this edition belongs to this product series” is enough unless another use needs a reusable relation name. Name a reusable predicate only under the pattern that states who or what may belong, what makes belonging begin and end, and how recurrence and past belonging are handled. Do not create a `NameCard` or public name for generic `MemberOf` merely to abbreviate the ordinary sentence.

