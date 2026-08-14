---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for System-Role and Status Name Families"
section_id: "F.14:15"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__016_sota-echoing.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "F.14 — Anti-Explosion Control for System-Role and Status Name Families"
  - "F.14:15 — SoTA-Echoing"
line_start: 95176
line_end: 95187
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.24.PUB"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.8"
  - "F.9"
  - "U.SystemRoleAssignment"
keywords:
  - "NameCard"
  - "assignment"
  - "designation"
  - "evidence use"
  - "permission"
  - "reuse"
  - "status names"
  - "system-role names"
  - "term row"
  - "vocabulary explosion"
---

### F.14:15 - SoTA-Echoing

F.14 does not import access-control, terminology, or status taxonomies as FPF ontology. It adopts their shared practical discipline: separate the governed value, designation, assignment, permission, status, evidence, publication, and currentness before making a durable name.

| Current pressure | Practice line | F.14 adoption |
| --- | --- | --- |
| System-role-kind labels are too weak for authorization, Work attribution, or capability. | RBAC, ABAC, zero-trust, and policy-as-code separate attributes, policy decision, resource action, and evidence. | Keep the kind name separate from the assigned system, capability, permission, policy, and Work. |
| Terminology practice distinguishes values or concepts, designations, local senses, records, and mappings. | Shared spelling is insufficient for identity or semantic equivalence. | Recover the value first; prefer light dispositions; use F.9, F.17, or F.18 only at their exact triggers. |
| Status dashboards often hide criteria. | Monitoring and assurance separate indicator, threshold, time window, status, evidence, decision, and display. | Keep status and presentation objects separate and use its subject pattern for each claim. |

SysML is intentionally not used as naming or ontology authority here. Its familiar role vocabulary does not establish a local system-role kind, assignment, capability, permission, Method, or Work.

