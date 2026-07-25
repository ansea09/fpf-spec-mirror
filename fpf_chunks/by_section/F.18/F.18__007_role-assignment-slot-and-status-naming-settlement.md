---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:5"
section_title: "Role, Assignment, Slot, and Status Naming Settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__007_role-assignment-slot-and-status-naming-settlement.md"
commit_sha: "504747d26299e3963dc0457bf48d4e2a791d926a"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:5 — Role, Assignment, Slot, and Status Naming Settlement"
line_start: 93144
line_end: 93254
dependencies:
  - "A.15.1"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.6.RSIR"
  - "C.2.1"
  - "E.10"
  - "E.10.ARCH"
  - "E.24.PUB"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
  - "F.13"
  - "F.14"
  - "F.15"
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

### F.18:5 - Role, Assignment, Slot, and Status Naming Settlement

This settlement makes several naming boundaries explicit.

#### F.18:5.1 - Role Names

A durable role name names one governed `U.Role` value interpreted through one named role-taxonomy episteme under its effective by-value `U.ReferenceScheme`. If one selected model-use structure, role-relation structure, claim scope, or project-work relation changes the naming use, cite that object separately; the name does not create it. Good role names normally use role morphology, for example `ReviewerRole`, `ShipbuilderRole`, or `ServiceProviderRole`.

A role name must not include:

- the holder that fills a role assignment;
- capability evidence or skill level;
- method or method-family selection;
- performed work;
- status value or gate result;
- source, evidence, publication, or assurance use.

If a phrase such as `SeniorReviewer`, `NightOperator`, or source wording like evidence role appears, recover the governed values first. The result may be a role value, a holder assignment, a status assertion, an evidence-use relation, a work admission condition, or a local source phrase. Do not force all of them into one role name.

#### F.18:5.2 - Holder Assignment Names

A holder-assignment name denotes one already recoverable obtaining `U.RoleAssignment` occurrence governed by `A.2.1`; the role name itself does not identify that occurrence. Before naming it, recover its four actual participants: the admitted holder system, role value, role-taxonomy episteme, and effective reference scheme. Also recover the uninterrupted assignment episode. The currently known `AssignmentInterval` remains assertion- or occurrence-description content, not a fifth participant. A durable name uses a `NameCard` whose `GovernedValueRef` resolves to that occurrence. If public or cross-context reuse is needed, apply the section 4.4 gate; until it passes, retain the card locally and mark the row pending. Neither a name, card, row, nor publication occurrence makes the assignment obtain.

`Holder#Role:Context@Window` is source notation only. Recover the exact referent behind `Context`, its kind, and the direct relation that makes it relevant. A selected `BoundedModelUseStructure` stays in the receiving assertion or use and appears only when it changes interpretation. The token is neither a role name nor proof of assignment, capability, or performed work.

#### F.18:5.3 - Capability, Method, and Work Names

Keep these separate:

- `ShipbuilderRole` names a role value;
- `ShipbuildingCapability` names a capability of an admitted `U.System`, including an acting holon admitted as a system for that capability claim;
- `ShipbuildingMethod` names a method or method family;
- `HullAssemblyWork` names a work family or planning-level work label until an exact performed occurrence is current.

A role-derived or role-method-coupled expression is only a naming cue. First recover the exact value it refers to. If that value is an exact method or method family under `A.3.1`, choose a method name. If it is an exact `U.MethodDescription`, `U.WorkPlan`, or dated `U.Work` occurrence, name that description episteme, plan episteme, or occurrence separately under `A.3.2`, `A.15.2`, or `A.15.1`; those names are not method names. If the expression refers to another value, use that value's direct owner. `F.18` chooses a durable name only after this recovery. A role relation may constrain who may use the method or perform the work; it neither creates nor names the method, description, plan, or work occurrence.

Treat an action nominal such as `testing`, `assembly`, `maintenance`, `evaluation`, or `inspection` as a morphology cue, not a governed kind. Placement in function- or flow-structure prose identifies no `U.Function`. If the function-like use remains claim-bearing while its exact object or relation is hidden, apply `A.6.F`; if it is already recoverable, name the exact method, method description, required-transformation or required-effect claim, actual `U.Transformation`, `TransformationFlowStructure` locus, functional-view record, plan content, performed-work occurrence, or other governed value under its direct pattern before F.18 selects a durable name. A WBS element, activity, or Work Package remains plan- or assignment-episteme content about intended work; none of these uses identifies a performed Work occurrence admitted under `U.Work`.

A durable name for exact performed work names one occurrence already grounded under `A.15.1`, not the action nominal or plan row. The current naming use must be able to recover the performer through an obtaining `U.RoleAssignment`, actual `enactsMethod`, temporal extent, exact containing system, affected referent, and the direct bindings and resource-use facts material to the occurrence. Add the exact continuity policy only when interruption, retry, changed method or bindings, or competing designators make occurrence identity material. Keep neighboring direct subject or resource-use claims, `A.15.PROD` production claims, measurement-result epistemes, evaluation results, `C.11` choices or decisions, delivery occurrences, acceptance verdicts, and downstream-effect claims separately named under their direct governors.

When the underlying boundary wording still hides the relation, apply `A.6.P.WMR`. `F.18` starts only after an exact governed value and its use are recovered through a direct subject relation, an exact `A.6.1` application binding, or an exact local `A.15.PROD`/`A.6.RCD` claim. An exact non-assertability result independently records `factually unsupported`, `missing-information`, or `missing-governor`; none authorizes durable naming, and only `missing-governor` is an ontology blocker that names the affected use and future owner. This section selects and tests a name. It does not define a second work-occurrence or work-result recovery algorithm.

Method-relation and method-composition names are method-side names too. If a phrase names serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, fallback, or dispatch among methods, first decide which object the phrase names.

- If admitted submethods make one composite way of doing, name the composite `U.Method`. `A.3.1` governs that Method, and its exact composition relation stays with `B.1.5` or another direct composition owner.
- If the phrase names relations among methods without making one whole Method, select a `U.Structure` under `A.22` and designate it `MethodRelationStructure@BoundedContext`. Each included composition, refinement, substitution, iteration, decomposition, family-membership, selector, fallback, description, or work-use relation stays with its direct `A.3.1`, `G.5`, `A.15`, or composition owner.
- If the current object is a separately identified episteme that describes one exact admitted Method, `A.3.2` may classify it as `U.MethodDescription`; F.18 names that episteme separately from the Method.
- If an episteme instead describes the selected relation structure, `C.2.1` keeps that structure as its exact `EntityOfConcern`; the episteme is not thereby a `U.MethodDescription`.

F.18 settles a durable name only after one of those exact objects has been recovered. Algebraic, graph, categorical, process-calculus, matrix, embedding, distributed, or neural notation names the lens or representation only when that lens is the governed value.

#### F.18:5.4 - Role-Relation, Method-Relation, Role-Method, and Lens Names

Role-relation expressions remain expressions or relations unless the direct role pattern admits a durable role value and the NameCard settles its by-value reference scheme and local sense. A role-algebra, graph, matrix, embedding, distributed, or neural description is a lens over the selected role relation structure; it is not automatically the named role, holder, method, or work.

First recover what the name is for:

| Expression or source phrase | What can be named | Naming rule |
| --- | --- | --- |
| `R1 <= R2` | one exact `RoleAdmissionSubstitutionRelation` occurrence between two interpreted role values under its receiving-use predicate, taxonomy episteme, by-value scheme, and qualification window | Name or cite the exact relation occurrence or selected `RoleRelationStructure`; keep any assertion or policy record, current assignment, receiving check, and outcome separate. Name a new role only when the direct role pattern independently admits that value. |
| `R1 incompatibleWith R2` | one exact `RoleIncompatibilityRelation` occurrence between two interpreted role values under its by-value incompatibility predicate and qualification window | Name or cite the relation occurrence or selected `RoleRelationStructure`, not a new role. Exact assignment occurrences, holder/work/time conditions, the receiving check, and its admit/reject/defer result remain in the predicate or neighbouring objects; they are not substituted for the two role-value positions. |
| `R1 and R2` | independent role values and assignments, when both remain current separately | Use "and" in ordinary prose; do not hide independent assignments by hyphenating them. |
| `R1 bundle R2` or `RoleBundle := R1 and R2` | role-bundle expression or durable bundle role value, if admitted | Keep it as an expression unless a direct role pattern admits a durable bundle value and its NameCard settles the reference scheme and local sense. |
| `R1` qualified by domain, practice, method family, or work field | local qualified role expression such as robotics-qualified engineering role | Ordinary labels may be `robotics engineer` or `engineer-roboticist`; `Role` suffix is optional Tech-register disambiguation. |
| method-like phrase derived from a role label | method, method family, method description, work plan, or work occurrence | Name under `A.3.1`, `A.3.2`, or `A.15`; cite the role relation separately when it constrains who may use or perform the method. |
| algebraic, graph, matrix, embedding, distributed, or neural representation of roles | mathematical or representation description of selected role relation structure | Name the lens only when the representation itself is the governed value; otherwise name the recovered role relation, role expression, method, or work. |
| method algebra, method graph, method matrix, process calculus, selector calculus, or method embedding | mathematical or representation description of selected `MethodRelationStructure@BoundedContext` | Name the lens only when the representation itself is the governed value; otherwise name the selected method relation structure, method family, method description, work plan, work occurrence, or neighboring relation. |
Ordinary speech can omit `Role` and `Method` suffixes when the governed kind, named role-taxonomy episteme where a role is current, effective reference scheme, exact local sense, and direct claim keep the distinction recoverable. Formal suffixes are useful when the name becomes cross-scheme, public, or easy to confuse with a method, capability, work occurrence, status, publication, or policy term.

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

Do not name these as `U.Role` values unless a work-facing role value is actually current. "This standard plays the role of evidence" is repaired to the appropriate evidence-use, source-use, or status-use relation; it is not a work-role assignment for the standard.

#### F.18:5.6 - Relation, Slot, Interface, Port, and Signature Names

If a name touches relation, slot, interface, port, boundary, protocol, API, or signature wording, use `A.6.RSIR` and direct governing patterns.

- `A.6.5` governs relation slot discipline and SlotSpecs.
- `A.6.0` governs signatures and rule-governed declarations.
- `A.6.M` and architecture patterns govern module interfaces and architecture interfaces.
- `A.6.F`, transformation, and architecture patterns govern functional ports and functional structures.
- `A.6.C`, protocol, service-access, and commitment patterns govern API, protocol, and service-access cases.
- `C.2.1` governs a claim-bearing interface-description episteme.
- `E.17` governs a multi-view publication face or form.
- `E.24.PUB` governs availability of the selected edition and the separate form-expression and carrier-bearing relations.

Before naming a relation-facing object, keep these settlements distinct:

| Object to name | Required prior settlement |
| --- | --- |
| reusable predicate-definition episteme | `A.6.RCD` has selected reusable definition and `C.2.1` gives it one truthful exact `EntityOfConcern`; the name denotes the definition, not a relation kind |
| derived or primitive relation kind | `A.6.RCD`, `E.24`, and `E.24.UK` have admitted the kind and its direct subject pattern states obtaining, applicability, and occurrence identity |
| one obtaining relation occurrence | the direct owner establishes obtaining and `A.6.REL` applies the admitted kind's identity rule |
| formula, query, path, graph, diagram, or other representation element | `C.29` states what it represents and the relevant correspondence; its name does not name the represented relation by default |
| designator or reference | the exact designation or reference relation resolves to the already settled object under its reference scheme |

One token may be reused only where the reference scheme and local sense preserve these distinctions; it cannot collapse definition, kind, occurrence, representation, and designator into one object.

`F.18` can settle a durable name for the recovered value. It does not decide which value the interface word names, create a public row, or make that row available.

