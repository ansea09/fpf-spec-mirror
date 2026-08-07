---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
section_id: "A.2.7:7"
section_title: "Failure Modes and Repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__009_failure-modes-and-repairs.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "A.2.7 — Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
  - "A.2.7:7 — Failure Modes and Repairs"
line_start: 6095
line_end: 6109
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

### A.2.7:7 - Failure Modes and Repairs

| Failure | Why it fails | Repair |
|---|---|---|
| Job-title order used for admission | The title order does not state the receiving-use predicate. | Declare a directional `RoleAdmissionSubstitutionRelation` for the exact method or work condition. |
| `RoboticsEngineerRole` treated as a system subkind | Role meaning is confused with holder kind. | Keep the holder's system kind stable and state `RoleQualificationRelation`; add substitution only if admission is also intended. |
| Independence asserted without a joint condition | A system applying the receiving method cannot determine which holder, work, and window combination is incompatible. | Put that exact condition into `RoleIncompatibilityPredicateSlot`. |
| Bundle name treated as one role | Holder allocation and independent assignments disappear. | Keep `RoleBundleRelation` and its allocation predicate; admit a separate role value only through A.2. |
| Taxonomy row treated as relation occurrence | Episteme form is confused with predicate obtaining. | State the direct predicate first; use the row as an assertion and support it under evidence rules. |
| Positive assertion reference used to create an occurrence | A reference and interval are filled before current case facts satisfy the direct predicate and before the identity rule recovers one occurrence. | State the case facts, test the predicate, apply the direct identity rule when the receiver needs occurrence identity, and only then designate the recovered occurrence. Without a recovered occurrence, use the direct relation kind or another independently identified entity as the assertion's EntityOfConcern and keep proposed fillings in the ClaimGraph. |
| Relation structure produces a decision | A non-agentive structure is made to act. | Name the system, method, checking work, and outcome governed by the receiving pattern. |
| Graph treated as role ontology | Representation identity replaces selected relation identity. | Name the `RoleRelationStructure` and exact occurrences; use C.29 for the graph's preserved and lost structure. |
| Temporal window declared as a participant | A receiving or descriptive window is confused with the direct occurrence's world-side extent. | Remove the temporal SlotSpec; derive maximal continuous obtaining extent and state `roleRelationExtent` or a target evaluation window only in the appropriate assertion or check. |
| Bridge used as role-substitution licence | Semantic correspondence is overread as suitability, reliance, assignment, or a receiving outcome. | Keep the exact Bridge, bounded-use assertion, A.10 or B.3 reliance, local A.2.7 relation, and actual receiving work as separate objects. |

