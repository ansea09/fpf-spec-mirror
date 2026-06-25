---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:3"
section_title: "Role-Relation Expressions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__007_role-relation-expressions.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:3 — Role-Relation Expressions"
line_start: 5013
line_end: 5048
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

#### A.2.7:3.1 - Role-Requirement Substitution

Use role-requirement substitution when one role value can satisfy another required role in the same bounded context.

```text
SeniorWeldingInspector <= WeldingInspector
```

Read this as: an assignment to `SeniorWeldingInspector` may satisfy a method or work-admission requirement for `WeldingInspector` when the bounded context declares that substitution and the assignment window is current.

The relation is not kind subsumption. `SeniorWeldingInspector` is not a subtype of a system kind; it is a role value related to another role value for local requirement satisfaction. It is also not capability evidence, public naming, or method identity. A senior inspector role may still require a separate capability claim under `A.2.2`, a method relation under `A.3.1`/`A.3.2`, or a naming settlement under `F.5`/`F.18`.

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

A bundle expression becomes a durable role value only when the bounded context declares it as a role with its own role description, role-state expectations, capability requirements, and method or work relations where current.

