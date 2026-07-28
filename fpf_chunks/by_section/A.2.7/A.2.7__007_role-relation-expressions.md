---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:3"
section_title: "Role-Relation Expressions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__007_role-relation-expressions.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:3 — Role-Relation Expressions"
line_start: 5377
line_end: 5427
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.5"
keywords:
  - "bundles (⊗)"
  - "incompatibility (⊥)"
  - "requiredRoles substitution"
  - "role algebra"
  - "separation of duties (SoD)"
  - "specialization (≤)"
---

### A.2.7:3 - Role-Relation Expressions

#### A.2.7:3.0 - Role Decomposition Boundary

Start from the object claim, not from the word used for it. If a role is decomposed, the admissible repairs are:

- role-admission substitution when one role assignment may satisfy a role-admission condition stated with another role value;
- factor or qualification when one role expression narrows a role by domain, practice, method family, work field, or context;
- bundle expression when several independent role assignments must be held together;
- separate role value when the bounded context needs its own role description, state expectations, capability-fit conditions, and method or work relations;
- role-state refinement under `A.2.5` when only enactable-state detail changes;
- capability-fit condition, responsibility relation, permission, commitment, or obligation under the direct owner when the decomposition actually names those objects;
- method or work decomposition under `A.15` when the source actually divides method into submethods or work into work-part relations.

Do not use role `partOf`. `U.Role` is a root work-facing role value under `A.2`, not an admitted holon kind under `A.1`.
Do not infer role parts from slots. `RoleAssignment`, role-state relations, evidence-use relations, and role-relation structures may declare SlotSpecs under `A.6.5`; those SlotSpecs are relation positions. Role descriptions may have episteme constituents. Neither case supplies parts of the `U.Role` value.

#### A.2.7:3.1 - Role-Admission Substitution

Use role-admission substitution when one role value can satisfy a role-admission condition stated with another role value in the same bounded context.

```text
SeniorWeldingInspector <= WeldingInspector
```

Read this as: an assignment to `SeniorWeldingInspector` may satisfy a method or work-admission condition stated with `WeldingInspector` when the bounded context declares that substitution and the assignment window is current.

The relation is not kind subsumption. `SeniorWeldingInspector` is not a subtype of a system kind; it is a role value related to another role value for local admission satisfaction. It is also not capability evidence, public naming, or method identity. A senior inspector role may still need a separate capability-fit claim under `A.2.2`, a method relation under `A.3.1`/`A.3.2`, or a naming settlement under `F.5`/`F.18`.

#### A.2.7:3.2 - Role Incompatibility

Use role incompatibility when the same holder cannot validly use overlapping assignments to two roles in the same context and window.

```text
SurgeryPerformer incompatibleWith SurgeryVerifier
```

This relation is often used for separation-of-duties or independence constraints. It does not create a commitment object, permission policy, or evidence record by itself. A work-admission check may use it to reject the proposed assignment combination.

#### A.2.7:3.3 - Role Bundle Expression

Use a role bundle expression when a frequent conjunction of roles is useful to name inside one context.

```text
IncidentLeadOnCall := IncidentCommander and Communicator and DecisionMaker
```

The bundle expression is satisfied by current assignments to all component roles under the same bounded context and required window. It is not a product of role values, not a new holder, not a method, and not a capability.

A bundle expression becomes a durable role value only when the bounded context declares it as a role with its own role description, role-state expectations, capability-fit conditions, and method or work relations where current.

