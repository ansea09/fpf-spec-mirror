---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:2"
section_title: "Solution - Core Role-Relation Structure"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__006_solution-core-role-relation-structure.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:2 — Solution - Core Role-Relation Structure"
line_start: 5005
line_end: 5042
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

### A.2.7:2 - Solution - Core Role-Relation Structure

`RoleRelationStructure@BoundedContext` is a relation structure declared inside one `U.BoundedContext`. A role-algebra description may be attached when notation helps inspection, but the structure remains the governed object.

```text
RoleRelationStructure:
  BoundedContextRef:
  RoleDescriptionRefs?:
  RoleValueSet:
  RoleExpressionSet?:
  RoleRequirementSubstitutionSet:
  IncompatibilityRelationSet:
  FactorOrQualificationExpressionSet?:
  BundleExpressionSet:
  MathematicalOrRepresentationDescriptionRefs?:
  UseRelationRefs:
```

**BoundedContextRef.** The role relation structure is local. A relation declared in `HospitalOR_2026` does not automatically apply in `PlantMaintenance_2026` or another hospital's governance context.

**RoleDescriptionRefs.** Role descriptions may supply the recognized meaning of role values or role expressions. They are description epistemes, not the holder, not the assignment, and not the algebraic lens.

**RoleValueSet.** The structure ranges over `U.Role` values governed by `A.2`.

**RoleExpressionSet.** The structure may include context-local role expressions such as qualified roles, bundle expressions, or labels that ordinary prose uses before a durable role value is declared.

**RoleRequirementSubstitutionSet.** The context may declare `AcceptedRoleForRequirement <= RequiredRole` as a role-requirement substitution relation. This is a local admissibility relation for method, work-admission, staffing, safety, or governance checks. It is not kind subsumption, org-chart rank, capability evidence, source-label equivalence, or public naming.

**IncompatibilityRelationSet.** The context may declare `RoleA incompatibleWith RoleB`. This means the same holder cannot use overlapping role assignments for both roles in the same bounded context and window when that incompatibility is current for the work claim.

**FactorOrQualificationExpressionSet.** The context may declare that one ordinary label is a qualified role expression, such as engineer qualified by robotics domain, method family, practice, or work field. This does not automatically create a separate `RoboticistRole` or a combined role value.

**BundleExpressionSet.** The context may declare `RoleBundle := Role1 and Role2 and Role3` as a role-bundle expression. The expression is satisfied only by valid assignments to each component role under the same bounded context and required window. It does not create a composite holder, composite capability, or method.

**MathematicalOrRepresentationDescriptionRefs.** A mathematical or representation description may use order, product, factorization, graph, matrix, embedding, neural representation, distributed model, or another lens to express the selected role relation structure. This description is governed like any lens use: it names what it represents, what it preserves, what it loses, and what it must not be overread to prove.

**UseRelationRefs.** A method step, work-admission check, staffing rule, safety case, naming decision, or governance rule may cite the role relation it uses.

