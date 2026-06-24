---
chunk_kind: "child"
pattern_id: "F.18"
pattern_title: "Local-First Unification Naming Protocol"
section_id: "F.18:5"
section_title: "Role, Assignment, Slot, and Status Naming Settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/F.18/F.18__007_role-assignment-slot-and-status-naming-settlement.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "F.18 — Local-First Unification Naming Protocol"
  - "F.18:5 — Role, Assignment, Slot, and Status Naming Settlement"
line_start: 83543
line_end: 83632
dependencies:
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "A.6.RSIR"
  - "C.2.P"
  - "E.10"
  - "F.0.1"
  - "F.1"
  - "F.1-F.17"
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

### F.18:5 - Role, Assignment, Slot, and Status Naming Settlement

This settlement makes several naming boundaries explicit.

#### F.18:5.1 - Role Names

A durable role name names a `U.Role` value in a bounded context. Good role names normally use role morphology, for example `ReviewerRole`, `ShipbuilderRole`, or `ServiceProviderRole`.

A role name must not include:

- the holder that fills a role assignment;
- capability evidence or skill level;
- method or method-family selection;
- performed work;
- status value or gate result;
- source, evidence, publication, or assurance use.

If a phrase such as `SeniorReviewer`, `NightOperator`, or source wording like evidence role appears, recover the governed values first. The result may be a role value, a holder assignment, a status assertion, an evidence-use relation, a work admission condition, or a local source phrase. Do not force all of them into one role name.

#### F.18:5.2 - Holder Assignment Names

A holder assignment is governed by `A.2.1`, not by the role name itself. If the assignment needs a public name, name the assignment relation as such, for example:

```text
HolderAssignment:
  HolderRef:
  RoleRef:
  BoundedContextRef:
  AssignmentWindowRef:
```

`Holder#Role:Context@Window` may be used as a compact assignment notation where accepted by `A.2.1`. It is not a role name and not proof of capability.

#### F.18:5.3 - Capability, Method, and Work Names

Keep these separate:

- `ShipbuilderRole` names a role value;
- `ShipbuildingCapability` names a capability of a system or acting holon;
- `ShipbuildingMethod` names a method or method family;
- `HullAssemblyWork` names work or a work family.

Role-derived or role-method-coupled method names are method names when the current governed value is a method, method family, method description, work plan, or work occurrence. They are governed by `A.3.1`, `A.3.2`, and `A.15`, with `F.18` only choosing the durable name. A role relation structure may constrain who may use or perform the method; it does not produce the method name.

Method-relation and method-composition names are method-side names too. If a phrase names serial composition, parallel composition, guarded choice, iteration, refinement, substitution, decomposition, parameterization, method-family membership, fallback, or dispatch among methods, recover `MethodRelationStructure@BoundedContext` under `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current. Algebraic, graph, categorical, process-calculus, matrix, embedding, distributed, or neural notation names the lens or representation only when that lens is the governed value.

#### F.18:5.4 - Role-Relation, Method-Relation, Role-Method, and Lens Names

Role-relation expressions remain expressions or relations unless the bounded context creates a durable role value through `A.2`, `A.2.7`, role description, and `F.18` naming. A role-algebra, graph, matrix, embedding, distributed, or neural description is a lens over the selected role relation structure; it is not automatically the named role, holder, method, or work.

First recover what the name is for:

| Expression or source phrase | What can be named | Naming rule |
| --- | --- | --- |
| `R1 <= R2` | role-requirement substitution relation between role values or local role expressions | Name a new role only when the bounded context introduces that role value. Otherwise name the relation or cite it inside the governing method requirement, A.2.7 role-relation record, or work-admission check. |
| `R1 incompatibleWith R2` | incompatibility relation for assignments in one bounded context and window | Name the relation or constraint, not a new role. |
| `R1 and R2` | independent role values and assignments, when both remain current separately | Use "and" in ordinary prose; do not hide independent assignments by hyphenating them. |
| `R1 bundle R2` or `RoleBundle := R1 and R2` | role-bundle expression or durable bundle role value, if declared | Keep it as an expression unless a role description and context make a durable role value. |
| `R1` qualified by domain, practice, method family, or work field | local qualified role expression such as robotics-qualified engineering role | Ordinary labels may be `robotics engineer` or `engineer-roboticist`; `Role` suffix is optional Tech-register disambiguation. |
| method-like phrase derived from a role label | method, method family, method description, work plan, or work occurrence | Name under `A.3.1`, `A.3.2`, or `A.15`; cite the role relation separately when it constrains who may use or perform the method. |
| algebraic, graph, matrix, embedding, distributed, or neural representation of roles | mathematical or representation description of selected role relation structure | Name the lens only when the representation itself is the governed value; otherwise name the recovered role relation, role expression, method, or work. |
| method algebra, method graph, method matrix, process calculus, selector calculus, or method embedding | mathematical or representation description of selected `MethodRelationStructure@BoundedContext` | Name the lens only when the representation itself is the governed value; otherwise name the selected method relation structure, method family, method description, work plan, work occurrence, or neighboring relation. |
Ordinary speech can omit `Role` and `Method` suffixes when the current record or context makes the kind recoverable. Formal suffixes are useful when the name becomes cross-context, public, or easy to confuse with a method, capability, work occurrence, status, publication, or policy term.

#### F.18:5.5 - Status, Evidence, Source, and Publication Names

Status-like and evidence-like wording must go to direct patterns:

- status value or status assertion: `F.10` or `A.19.SPR`;
- evidence-use relation: `A.10`;
- assurance use: `B.3`;
- source use: `E.10.D2` or source-use patterns;
- publication or description use: `E.17` and `C.2.1`;
- gate or admission result: the relevant gate, decision, or assurance pattern.

Do not name these as `U.Role` values unless a work-facing role value is actually current. "This standard plays the role of evidence" is repaired to the appropriate evidence-use, source-use, or status-use relation; it is not a work-role assignment for the standard.

#### F.18:5.6 - Relation, Slot, Interface, Port, and Signature Names

If a name touches relation, slot, interface, port, boundary, protocol, API, or signature wording, use `A.6.RSIR` and direct governing patterns.

- `A.6.5` governs relation slot discipline and SlotSpecs.
- `A.6.0` governs signatures and law-governed declarations.
- `A.6.M` and architecture patterns govern module interfaces and architecture interfaces.
- `A.6.F`, transformation, and architecture patterns govern functional ports and functional structures.
- `A.6.C`, protocol, service-access, and commitment patterns govern API, protocol, and service-access cases.
- `E.17` governs publication or description interfaces.

`F.18` can publish a durable name for the recovered value. It does not decide which value the interface word names.

