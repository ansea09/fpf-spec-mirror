---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:0.1"
section_title: "Kind Settlement"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__002_kind-settlement.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:0.1 — Kind Settlement"
line_start: 4943
line_end: 4977
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

### A.2.7:0.1 - Kind Settlement

**Use this pattern when** a project needs context-local role substitution, incompatibility, factor, qualification, or bundle relations without turning labels or role-algebra notation into a second ontology.

**What goes wrong if missed.** Role labels start carrying type, capability, method, work, evidence, or permission claims, and a representation lens starts replacing the role relation structure in life.

**What this buys.** Role-relation claims stay small, local, and inspectable while role assignment, capability, method, work, evidence, source, status, publication, and lens claims keep their own governing patterns.

A.2.7 does not admit `U.RoleAlgebra` as a durable U-kind. The governed object is `RoleRelationStructure@BoundedContext`: a selected context-local relation structure over role descriptions, `U.Role` values, role expressions, substitution, incompatibility, and bundle-expression relations. A role algebra, graph, matrix, embedding, distributed model, or neural representation is a mathematical or representation lens over that structure, not the structure itself and not an operation on holder systems.

`RoleRelationStructure@BoundedContext` is the FPF object for context-local relations among role descriptions, declared role values, local role expressions, role-bundle expressions, and role-assignment-admission uses. It is not a new `U.*` kind beside `U.Role`; it is a selected relation structure over role-side values inside one bounded context. When project prose calls this "role architecture", the FPF object is still the selected role-relation structure in life; a role-algebra, graph, matrix, embedding, distributed, or neural description is a lens over that structure, not the structure itself and not an operation on holder systems. Coupled method relations are governed symmetrically as `MethodRelationStructure@BoundedContext` under `A.3.1`, `A.3.2`, `A.15`, `G.5`, or a direct method-composition pattern when current; A.2.7 names the role-relation side and the bridge to role-method naming.

Use this pattern when a method, work-admission rule, staffing rule, safety case, governance rule, or role description needs to say that one role value can satisfy another role requirement, two roles cannot be held together by the same holder during the same window, a role expression has a factor or domain qualification, or a frequent conjunction of roles is worth naming.

**Primary EntityOfConcern.** The EntityOfConcern is `RoleRelationStructure@BoundedContext`: a context-local role-relation and role-expression structure in one `U.BoundedContext`. Algebraic notation, matrices, partial orders, products, graphs, embeddings, neural representations, or other mathematical or representation expressions are descriptions or lenses of that structure. The role architecture in life is the selected relation structure among role values and role expressions; the lens is not the holder, not the performed work, not the living system, not the method, and not the role assignment.

**Primary working reader.** A manager, architect, method author, safety assessor, or model author who needs role-requirement substitution, separation-of-duties, role-factor or qualification expression, role-bundle expression, or ordinary name guidance without turning the role relation structure into capability, method, holder, work, evidence, status, or kind hierarchy.

**First useful move.** Name the bounded context, the role descriptions or role values being related, the local role expression or relation being claimed, and the assignment, method, work-admission, naming, or bridge check that will use that relation. Use a role-algebra lens only when mathematical notation helps state or check that relation.

**What goes wrong if missed.** Role names start acting like type hierarchy, org-chart hierarchy, permission policy, capability model, method family, staffing plan, or cross-context translation. Then FPF grows a second ontology beside `U.Role`, `U.RoleAssignment`, `U.Capability`, and method or work patterns, or treats algebraic notation as if it were the object in life.

**What this buys.** Context-local role relation structure gives a small, replayable set of role relations for role assignment, method-step checks, naming, and bridge work while keeping ability, work, method, evidence, and status claims in their governing patterns. Role-algebra notation remains a lens for describing those relations, not a substitute ontology.

**Not this pattern when.**


- If the current claim is who holds a role, use `A.2.1`.
- If the current claim is whether an assignment is currently in a work-admitting state, use `A.2.5`.
- If the current claim is ability, use `A.2.2`.
- If the current claim is a method, method family, or method description, use `A.3.1` or `A.3.2`.
- If the current claim is performed work or planned work, use `A.15`, `A.15.1`, or `A.15.2`.
- If the current claim is cross-context naming or translation, use F-family context and naming patterns such as `F.9` and `F.18`.
- If the current claim is evidence, source, status, assurance, publication, or description use, use `C.2.1`, `A.10`, `B.3`, `E.17.*`, `E.24.PUB`, or `A.7` as the direct governing pattern for that episteme-use claim.

