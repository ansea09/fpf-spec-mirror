---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
section_id: "A.2.5:13"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__016_relations.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.2.5 — RoleStateRelation@BoundedContext - Role State Space and Enactable-State Admission"
  - "A.2.5:13 — Relations"
line_start: 4165
line_end: 4178
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:13 - Relations

| Related pattern | Relation |
| --- | --- |
| `A.2` | Governs the role value whose state space is being described. |
| `A.2.1` | Governs `U.RoleAssignment`, the relation referenced by `StateAssertion`. |
| `A.2.2` | Governs capability and operating envelope; role state may depend on capability evidence but does not replace capability. |
| `A.2.7` | Governs role-requirement substitution, incompatibility, and bundle expressions; A.2.5 adds state-sensitive admission when current. |
| `A.15`, `A.15.1`, `A.15.2` | Govern method, work plan, performed work, and `performedBy = U.RoleAssignment`. |
| `A.6.5` | Governs SlotSpec discipline used to keep role-state relation slots distinct. |
| `A.6.RSIR` | Recovers whether confusing source words point to role, role assignment, role state, signature, interface, slot, evidence, status, capability, method, or another governed object. |
| `A.10`, `B.3`, `C.2.1`, `C.28`, `E.17`, `F.10`, `G.6`, `E.10.D2` | Govern direct evidence-use, status-use, source-use, publication-use, assurance-use, and episteme-boundary cases that do not become role-state ontology. |
| `C.27` and temporal patterns | Govern windows, currentness, freshness, and stale-state claims when those are current. |

