---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:4"
section_title: "How Role Relation Structure Is Used"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__008_how-role-relation-structure-is-used.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:4 — How Role Relation Structure Is Used"
line_start: 5867
line_end: 5910
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

### A.2.7:4 - How Role Relation Structure Is Used

Role relation structure is normally used by neighboring patterns as one selected structure, sometimes informally called the local role architecture:

```text
MethodRoleAdmissionCheck:
  methodRef: WeldInspectionMethod
  requiredRoleValue: WeldingInspector
  proposedAssignmentRoleValue: SeniorWeldingInspector
  substitutionRef: SeniorWeldingInspector <= WeldingInspector
```

```text
WorkAdmissionCheck:
  holderRef: SurgeonA
  proposedAssignments: SurgeryPerformer, SurgeryVerifier
  incompatibilityRef: SurgeryPerformer incompatibleWith SurgeryVerifier
  window: AssignmentWindow
```

The role relation structure supplies one role-substitution relation used by the method role-admission or work-admission check. The method, method family, method relation structure, work plan, performed work, capability envelope, and evidence use remain governed by their direct patterns. When a method relation or method composition structure also needs to be named, the current object is `MethodRelationStructure@BoundedContext` under `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current; method-algebra notation is a lens over that structure, not a hidden product of roles.

#### A.2.7:4.1 - Naming role-relation and role-method expressions

Role relation work may leave behind something people need to name in ordinary project prose. The named object is not always an atomic `U.Role` value. It may be a holder-in-role statement, a context-local role expression, a role-admission substitution relation, an incompatibility relation, a role-bundle expression, a durable combined role value, a coupled role-method expression, a method name, or a work name.

Recover the named object before choosing the label:

| Source wording | Recovered object | Ordinary wording consequence |
| --- | --- | --- |
| "Vasya is an engineer" | holder-in-role claim: Vasya has a current assignment to an engineering role value in the bounded context | ordinary prose may say "engineer" without `Role`; the FPF record still separates holder, role value, assignment, and window |
| "robotics engineer" or "engineer-roboticist" | engineering role value or local engineering-role expression qualified by robotics domain, robotics-engineering method family, practice, or governed work field | ordinary label may stay "robotics engineer" or "engineer-roboticist"; `RoboticsEngineerRole` is optional Tech-register spelling only when durable reference needs it |
| "engineer and roboticist" | two independent role values and two assignments, if `RoboticistRole` is current separately from `EngineerRole` | use only when the project really needs two independent roles |
| "engineer-roboticist and musician" | one robotics-qualified engineering role expression or role value plus one independent musician role value | preferred ordinary wording when robotics qualifies engineering, while musician is separate |
| "engineer-roboticist-musician" | one declared combined role value or one named role-bundle expression | use only when the bounded context declares that combined value or bundle name; otherwise it hides independent assignments |
| "robot engineering", "music performance", or "teaching robots music" | method, method family, work, or work family | name under `A.3.1`, `A.3.2`, or `A.15`; these are not role-relation products merely because their labels share role words |
| "role algebra", "role graph", "role matrix", or "role embedding" | mathematical or representation description of selected role relation structure | name the lens or representation only when that description is the governed value; otherwise name the recovered role relation, role expression, assignment, method, or work |

`Role` and `Method` suffixes are optional Tech-register disambiguators. They are not ordinary-name requirements and they do not create the FPF kind. A user-facing sentence may say "Vasya is an engineer-roboticist and musician" without saying "role" when the FPF record or surrounding context lets a reader recover the role expression, role values, holder assignments, methods, and work separately.

Hyphenation is not algebra by itself. Use a hyphenated ordinary label when it helps a reader see a recovered factor, domain, practice, method-family qualification, or combined role expression. Use "and" when the current point is multiple independent role assignments. Do not mechanically concatenate operands into a Tech label.

The math-lens boundary is narrow. A role-algebra, graph, matrix, embedding, distributed, or neural representation is a lens over role values, role-admission substitution relations, incompatibility relations, role-factor or qualification expressions, and role-bundle expressions. The lens is not itself the role, holder, assignment, method, work, or capability. The name attaches to the recovered object or expression, not to the notation that helped recover it.

