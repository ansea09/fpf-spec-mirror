---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__013_sota-echoing.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:11 — SoTA-Echoing"
line_start: 2548
line_end: 2557
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
keywords:
  - "RCS/RSG"
  - "RoleEnactmentFact"
  - "Standard"
  - "context"
  - "holder"
  - "performedBy"
  - "role"
---

### A.2.1:11 - SoTA-Echoing

| Practice line | Current source line | FPF adoption |
| --- | --- | --- |
| OntoUML and UFO role modeling treat roles as context-dependent classifications rather than intrinsic substance kinds. | UFO and OntoUML work through the 2020s, including the 2026 gUFO line, keeps role-like and relation-like structures explicit rather than turning every slot filling, relation position, or use relation into a new object kind. | Adopt the holder-role separation: the same holder can bear different roles in different contexts without becoming a new system kind. |
| Bounded-context practice in domain-driven design and distributed-system architecture treats names as local to a context and requires explicit translation across boundaries. | Modern DDD and microservice architecture practice keeps role names local to a model boundary and treats cross-boundary sameness as a bridge, not as label equality. | Adopt context-local role meaning and require bridges or direct context relations for cross-context role reuse. |
| Modern identity, access-management, zero-trust, and policy-as-code practice separates subject, role or attribute relation, policy decision, and resource action. | NIST SP 800-207 (2020) separates authentication and authorization functions before resource access; NIST SP 800-53 Rev. 5 and its 2025 update expose control, assessment, authorization, and control-currentness material explicitly. | Adapt this separation: `U.RoleAssignment` is not capability, permission, gate passage, policy decision, or performed work; those claims stay in direct neighboring patterns. |
| Safety, quality, and security assurance practice uses traceable responsibility and separation-of-duties checks rather than role labels alone. | Current security and assurance control practice keeps accountability, assessment, authorization, and monitoring as checkable relations over systems and records rather than as names alone. | Adopt the replay chain from work occurrence to role assignment, role value, context, role-state admission, and evidence when current. |
| Provenance and evidence graph practice separates the work that produced a report from later evidence-use of the report. | Contemporary provenance and evidence-graph practice distinguishes event or work occurrence, produced episteme, and later evidence or assurance use. | Adopt the episteme boundary: reports, standards, datasets, and model cards participate through evidence, status, source, publication, requirement, or assurance relations, not as role-assignment holders. |

