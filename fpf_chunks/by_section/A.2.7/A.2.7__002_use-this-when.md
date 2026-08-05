---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
section_id: "A.2.7:0"
section_title: "Use This When"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__002_use-this-when.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "A.2.7 — Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
  - "A.2.7:0 — Use This When"
line_start: 5703
line_end: 5727
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

### A.2.7:0 - Use This When

**Plain name.** Relations among role values that a later admission or interpretation check can use.

Use this pattern when a role taxonomy contains several `U.Role` values and an engineer must state how those values are related before a system applying a receiving method can evaluate an actual assignment.

Typical moments include these:

- an inspection method description names `InspectorRole`, while the proposed holder is assigned `SeniorInspectorRole`;
- the same system must not hold author and approver roles for the same work during overlapping windows;
- a surgical procedure needs several role assignments jointly, with an explicit allocation rule;
- `RoboticsEngineerRole` narrows the meaning of `EngineerRole`, but that narrowing does not yet say whether one role can satisfy an admission condition written for the other.

**Primary EntityOfConcern.** The EntityOfConcern is one `RoleRelationStructure`: a selected, dependent `U.Structure` over declared `U.Role` values and exact obtaining relation occurrences among them. `RoleRelationStructure` is not a new root U-kind and not a holon. It is the non-agentive organization selected because that organization matters for a receiving use. An admitted system performs the receiving evaluation work by a selected method.

**Primary working reader.** The first reader is an engineer, method designer, safety practitioner, clinical team designer, or manager deciding which role relations a later check may rely on. The next reader must be able to recover the exact role meanings, relation predicates, temporal extents, and assignment checks without treating a role label, diagram, or policy row as the relation itself.

**First useful move.** Name the role-taxonomy episteme and effective reference scheme, select the exact relation species needed by the receiving use, and write its `RelationSignature` with one `SlotSpec` for every participant and predicate. Stop at a readable direct assertion if no receiving use needs relation-occurrence identity. Individuate and reference an occurrence only when a later claim depends on that identity.

**What goes wrong if missed.** A job-title hierarchy is used as if it settled admission. A statement that two duties should be independent has no exact holder, work, and time condition. A named bundle hides whether one system or several systems must hold the roles. A qualification such as `robotics engineer` is silently treated as system-kind subsumption, capability, assignment, or performed work. The receiving check then appears decisive while its actual relation premise is unavailable.

**What this buys.** Role admission, separation of duties, semantic qualification, and joint allocation can be reviewed as different relations. The same relations can support manufacturing, medicine, organizational work, and software authorization without making software policy the general ontology. Actual holders remain systems, actual assignments remain `U.RoleAssignment` occurrences, and the system performing the check remains visible.

**Not this pattern when.** Use `A.2.1` when the question is which admitted `U.System` holds a role and during which assignment episode. Use `A.2.5` for a role-state predicate, `A.2.2` for capability, A.3 patterns for methods, and A.15 patterns for planned or performed work. When meanings cross reference schemes, use `F.9` and `A.6.9` first for the exact Bridge, then `C.2.1` for the separate bounded-use assertion and `A.10` or `B.3` for current reliance; Bridge truth alone is not an A.2.7 relation or use licence. Use `C.29` when a graph, matrix, algebra, or embedding is the object under evaluation.

